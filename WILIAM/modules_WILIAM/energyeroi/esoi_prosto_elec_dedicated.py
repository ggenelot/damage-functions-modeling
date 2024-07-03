"""
Module energyeroi.esoi_prosto_elec_dedicated
Translated using PySD version 3.14.0
"""

@component.add(
    name="dynESOIst PROSTO elec dedicated",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"stored_energy_output_by_prosto": 1, "fenust_prosto_elec_dedicated": 1},
)
def dynesoist_prosto_elec_dedicated():
    """
    Dynamic evolution of the ESOIst of PROSTO elec dedicated (PHS and stationary batteries).
    """
    return zidz(
        stored_energy_output_by_prosto()
        .loc[:, _subscript_dict["PROSTO ELEC DEDICATED I"]]
        .rename({"PROSTO ELEC I": "PROSTO ELEC DEDICATED I"}),
        fenust_prosto_elec_dedicated(),
    )


@component.add(
    name="ESOIst initial PHS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eroist_ini_hydro_2015": 1,
        "cf_protra_full_load_hours": 1,
        "cf_prosto": 1,
    },
)
def esoist_initial_phs():
    """
    ESOI over the lifetime of PHS when the full potential is available.
    """
    return eroist_ini_hydro_2015() * (
        cf_prosto().loc[:, "PROSTO PHS"].reset_coords(drop=True)
        / cf_protra_full_load_hours()
        .loc[:, "PROTRA PP hydropower dammed"]
        .reset_coords(drop=True)
    )


@component.add(
    name="ESOIst PHS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_dedicated_lifetime": 1,
        "unit_conversion_wh_we": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
        "fenust_intensity_phs_exogenous": 1,
    },
)
def esoist_phs():
    """
    ESOIst over the lifetime of PHS.
    """
    return zidz(
        cf_prosto().loc[:, "PROSTO PHS"].reset_coords(drop=True)
        * float(prosto_dedicated_lifetime().loc["PROSTO PHS"])
        * (
            (unit_conversion_j_wh() / float(matrix_unit_prefixes().loc["exa", "tera"]))
            / (1 / unit_conversion_wh_we())
        ),
        fenust_intensity_phs_exogenous(),
    )


@component.add(
    name="FEnUst intensity PHS exogenous",
    units="EJ/TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_dedicated_lifetime": 1,
        "unit_conversion_wh_we": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
        "esoist_initial_phs": 1,
    },
)
def fenust_intensity_phs_exogenous():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for PHS. We assume the same lifetime for PHS than for hydro. Exogenous EROI assumed.
    """
    return zidz(
        cf_prosto().loc[:, "PROSTO PHS"].reset_coords(drop=True)
        * float(prosto_dedicated_lifetime().loc["PROSTO PHS"])
        * (
            unit_conversion_j_wh()
            * unit_conversion_wh_we()
            / float(matrix_unit_prefixes().loc["exa", "tera"])
        ),
        esoist_initial_phs(),
    )


@component.add(
    name="FEnUst intensity stationary batteries",
    units="EJ/TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_per_new_capacity_installed_ev_batteries_lfp": 1,
        "embodied_fe_intensity_materials_36r": 1,
        "unit_conversion_mj_ej": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def fenust_intensity_stationary_batteries():
    """
    Energy use (in final energy terms) per new installed capacity (MW) over lifetime for electric stationary batteries. LFP are assumed.
    """
    return sum(
        materials_per_new_capacity_installed_ev_batteries_lfp().rename(
            {"MATERIALS I": "MATERIALS I!"}
        )
        * embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I", "MATERIALS I": "MATERIALS I!"})
        .transpose("MATERIALS I!", "REGIONS 9 I"),
        dim=["MATERIALS I!"],
    ) * (unit_conversion_mw_tw() / unit_conversion_mj_ej())


@component.add(
    name="FEnUst PROSTO elec dedicated",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_dynamic_eroist": 2,
        "prosto_dedicated_capacity_expansion": 2,
        "fenust_intensity_phs_exogenous": 1,
        "fenust_intensity_stationary_batteries": 1,
    },
)
def fenust_prosto_elec_dedicated():
    """
    Energy use (in final terms) over the lifetime for installing PHS.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
        },
        ["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    )
    value.loc[:, ["PROSTO PHS"]] = (
        if_then_else(
            switch_nrg_dynamic_eroist() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: prosto_dedicated_capacity_expansion()
            .loc[:, "PROSTO PHS"]
            .reset_coords(drop=True)
            * fenust_intensity_phs_exogenous(),
        )
        .expand_dims({"NRG PRO I": ["PROSTO PHS"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO STATIONARY BATTERIES"]] = (
        if_then_else(
            switch_nrg_dynamic_eroist() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: prosto_dedicated_capacity_expansion()
            .loc[:, "PROSTO STATIONARY BATTERIES"]
            .reset_coords(drop=True)
            * fenust_intensity_stationary_batteries(),
        )
        .expand_dims({"NRG PRO I": ["PROSTO STATIONARY BATTERIES"]}, 1)
        .values
    )
    return value
