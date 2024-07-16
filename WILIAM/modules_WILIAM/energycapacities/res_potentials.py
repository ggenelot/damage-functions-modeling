"""
Module energycapacities.res_potentials
Translated using PySD version 3.14.0
"""

@component.add(
    name="actual rooftop use solar technologies",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "efficiences_pv_technology_panels": 2,
        "share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def actual_rooftop_use_solar_technologies():
    """
    Actual rooftop use calculated taking into account the actual share of solar PV subtechnologies.
    """
    return (
        protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", "PROTRA PP solar urban PV"]
        .reset_coords(drop=True)
        * protra_max_full_load_hours_after_constraints()
        .loc[:, "PROTRA PP solar urban PV"]
        .reset_coords(drop=True)
        * sum(
            (
                float(efficiences_pv_technology_panels().loc["C Si mono"])
                / efficiences_pv_technology_panels().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
            )
            * share_capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA PP solar urban PV", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                }
            )
            .transpose("PROTRA PP SOLAR PV SUBTECHNOLOGIES I!", "REGIONS 9 I"),
            dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
        )
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="EXOGENOUS PROTRA RES POTENTIALS SP",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROTRA RES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_exogenous_protra_res_potentials_sp"},
)
def exogenous_protra_res_potentials_sp():
    """
    scenario parameter for policy parameters
    """
    return _ext_constant_exogenous_protra_res_potentials_sp()


_ext_constant_exogenous_protra_res_potentials_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "EXOGENOUS_PROTRA_RES_POTENTIALS_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROTRA RES I": _subscript_dict["PROTRA RES I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROTRA RES I": _subscript_dict["PROTRA RES I"],
    },
    "_ext_constant_exogenous_protra_res_potentials_sp",
)


@component.add(
    name="POTENTIAL WIND OFFSHORE FIXED",
    units="EJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_offshore_fixed_by_eroi_min": 8,
    },
)
def potential_wind_offshore_fixed():
    """
    Potential wind offshore fixed selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_offshore_fixed_by_eroi_min()
        .loc[:, "EROI MIN 0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_offshore_fixed_by_eroi_min()
            .loc[:, "EROI MIN 2 1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_offshore_fixed_by_eroi_min()
                .loc[:, "EROI MIN 3 1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_offshore_fixed_by_eroi_min()
                    .loc[:, "EROI MIN 5 1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_offshore_fixed_by_eroi_min()
                        .loc[:, "EROI MIN 8 1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_offshore_fixed_by_eroi_min()
                            .loc[:, "EROI MIN 10 1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_offshore_fixed_by_eroi_min()
                                .loc[:, "EROI MIN 12 1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_offshore_fixed_by_eroi_min()
                                    .loc[:, "EROI MIN 15 1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS 36 I": _subscript_dict[
                                                "REGIONS 36 I"
                                            ]
                                        },
                                        ["REGIONS 36 I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL WIND OFFSHORE FIXED BY EROI MIN",
    units="EJ/Year",
    subscripts=["REGIONS 36 I", "EROI MIN POTENTIAL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_potential_wind_offshore_fixed_by_eroi_min"
    },
)
def potential_wind_offshore_fixed_by_eroi_min():
    """
    Potential wind offshore fixed by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_offshore_fixed_by_eroi_min()


_ext_constant_potential_wind_offshore_fixed_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_OFFSHORE_FIXED_BY_EROI_MIN",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    "_ext_constant_potential_wind_offshore_fixed_by_eroi_min",
)


@component.add(
    name="POTENTIAL WIND OFFSHORE FLOATING",
    units="EJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_offshore_floating_by_eroi_min": 8,
    },
)
def potential_wind_offshore_floating():
    """
    Potential wind offshore floating selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_offshore_floating_by_eroi_min()
        .loc[:, "EROI MIN 0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_offshore_floating_by_eroi_min()
            .loc[:, "EROI MIN 2 1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_offshore_floating_by_eroi_min()
                .loc[:, "EROI MIN 3 1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_offshore_floating_by_eroi_min()
                    .loc[:, "EROI MIN 5 1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_offshore_floating_by_eroi_min()
                        .loc[:, "EROI MIN 8 1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_offshore_floating_by_eroi_min()
                            .loc[:, "EROI MIN 10 1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_offshore_floating_by_eroi_min()
                                .loc[:, "EROI MIN 12 1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_offshore_floating_by_eroi_min()
                                    .loc[:, "EROI MIN 15 1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS 36 I": _subscript_dict[
                                                "REGIONS 36 I"
                                            ]
                                        },
                                        ["REGIONS 36 I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL WIND OFFSHORE FLOATING BY EROI MIN",
    units="EJ/Year",
    subscripts=["REGIONS 36 I", "EROI MIN POTENTIAL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_potential_wind_offshore_floating_by_eroi_min"
    },
)
def potential_wind_offshore_floating_by_eroi_min():
    """
    Potential wind offshore floating by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_offshore_floating_by_eroi_min()


_ext_constant_potential_wind_offshore_floating_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_OFFSHORE_FLOATING_BY_EROI_MIN",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    "_ext_constant_potential_wind_offshore_floating_by_eroi_min",
)


@component.add(
    name="POTENTIAL WIND ONSHORE",
    units="EJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 8,
        "potential_wind_onshore_by_eroi_min": 8,
    },
)
def potential_wind_onshore():
    """
    Potential wind onshore selected by the user depending on the EROI miniumun theshold.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: potential_wind_onshore_by_eroi_min()
        .loc[:, "EROI MIN 0"]
        .reset_coords(drop=True),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: potential_wind_onshore_by_eroi_min()
            .loc[:, "EROI MIN 2 1"]
            .reset_coords(drop=True),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: potential_wind_onshore_by_eroi_min()
                .loc[:, "EROI MIN 3 1"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: potential_wind_onshore_by_eroi_min()
                    .loc[:, "EROI MIN 5 1"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: potential_wind_onshore_by_eroi_min()
                        .loc[:, "EROI MIN 8 1"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            select_eroi_min_potential_wind_solar_sp() == 10,
                            lambda: potential_wind_onshore_by_eroi_min()
                            .loc[:, "EROI MIN 10 1"]
                            .reset_coords(drop=True),
                            lambda: if_then_else(
                                select_eroi_min_potential_wind_solar_sp() == 10,
                                lambda: potential_wind_onshore_by_eroi_min()
                                .loc[:, "EROI MIN 12 1"]
                                .reset_coords(drop=True),
                                lambda: if_then_else(
                                    select_eroi_min_potential_wind_solar_sp() == 10,
                                    lambda: potential_wind_onshore_by_eroi_min()
                                    .loc[:, "EROI MIN 15 1"]
                                    .reset_coords(drop=True),
                                    lambda: xr.DataArray(
                                        np.nan,
                                        {
                                            "REGIONS 36 I": _subscript_dict[
                                                "REGIONS 36 I"
                                            ]
                                        },
                                        ["REGIONS 36 I"],
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="POTENTIAL WIND ONSHORE BY EROI MIN",
    units="EJ/Year",
    subscripts=["REGIONS 36 I", "EROI MIN POTENTIAL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_potential_wind_onshore_by_eroi_min"},
)
def potential_wind_onshore_by_eroi_min():
    """
    Potential wind onshore by region and EROI minimum threshold.
    """
    return _ext_constant_potential_wind_onshore_by_eroi_min()


_ext_constant_potential_wind_onshore_by_eroi_min = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "POTENTIAL_WIND_ONSHORE_BY_EROI_MIN",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "EROI MIN POTENTIAL I": _subscript_dict["EROI MIN POTENTIAL I"],
    },
    "_ext_constant_potential_wind_onshore_by_eroi_min",
)


@component.add(
    name="remaining exogenous potential solar PV open space",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 2,
        "unlimited_protra_res_parameter": 1,
        "exogenous_protra_res_potentials_sp": 1,
        "protra_operative_capacity_stock_selected": 1,
        "switch_law2nrg_solarland": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "switch_energy": 1,
        "protra_max_full_load_hours": 1,
    },
)
def remaining_exogenous_potential_solar_pv_open_space():
    """
    Remaining exogenous potential solar PV open space after discounting the already capacity in place with the real operation CF. Solar PV availability coming from land-use enters the energy-capacity module directly through 'shortage_of_solar_land'. If SELECT_PROTRA_RES_POTENTIALS_SP=2 :OR: SWITCH_ENERGY=1 :OR: SWITCH_LAW2NRG_SOLARLAND=1 then the value is not taken in the allocate so '0' is writen ad hoc.
    """
    return (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: if_then_else(
                np.logical_or(
                    select_protra_res_potentials_sp() == 1,
                    np.logical_or(
                        switch_energy() == 0, switch_law2nrg_solarland() == 0
                    ),
                ),
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                - protra_operative_capacity_stock_selected()
                .loc[:, "TO elec", "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
    )


@component.add(
    name="remaining potential PROTRA RES CHP HP",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA RES CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "exogenous_protra_res_potentials_sp": 1,
        "protra_operative_capacity_stock_selected": 1,
        "protra_max_full_load_hours": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def remaining_potential_protra_res_chp_hp():
    """
    Remaining potential of RES for heat generation (including CHPs) in EJ/year.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "PROTRA RES CHP HP I": _subscript_dict["PROTRA RES CHP HP I"],
            },
            ["REGIONS 9 I", "PROTRA RES CHP HP I"],
        ),
        lambda: exogenous_protra_res_potentials_sp()
        .loc[:, _subscript_dict["PROTRA RES CHP HP I"]]
        .rename({"PROTRA RES I": "PROTRA RES CHP HP I"})
        - protra_operative_capacity_stock_selected()
        .loc[:, "TO heat", _subscript_dict["PROTRA RES CHP HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA RES CHP HP I"})
        * protra_max_full_load_hours()
        .loc[:, _subscript_dict["PROTRA RES CHP HP I"]]
        .rename({"NRG PROTRA I": "PROTRA RES CHP HP I"})
        * unit_conversion_tw_per_ej_per_year(),
    ).expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)


@component.add(
    name="remaining potential PROTRA RES PP",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA RES PP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_potential_wind": 1,
        "remaining_exogenous_potential_solar_pv_open_space": 1,
        "exogenous_protra_res_potentials_sp": 2,
        "protra_operative_capacity_stock_selected": 2,
        "protra_max_full_load_hours": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "remaining_solar_pv_rooftop_potential": 1,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def remaining_potential_protra_res_pp():
    """
    Remaining potential of RES for electricity generation in EJ/year. For solar PV it is the exogenous potential.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PROTRA RES PP I": _subscript_dict["PROTRA RES PP I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA RES PP I"],
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = (
        remaining_potential_wind()
        .loc[:, "TO elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = (
        remaining_exogenous_potential_solar_pv_open_space()
        .loc[:, "TO elec", "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = False
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar urban PV"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP oceanic"]] = False
    value.values[except_subs.values] = (
        (
            exogenous_protra_res_potentials_sp()
            .loc[:, _subscript_dict["PROTRA RES PP I"]]
            .rename({"PROTRA RES I": "PROTRA RES PP I"})
            - protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", _subscript_dict["PROTRA RES PP I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA RES PP I"})
            * protra_max_full_load_hours()
            .loc[:, _subscript_dict["PROTRA RES PP I"]]
            .rename({"NRG PROTRA I": "PROTRA RES PP I"})
            * unit_conversion_tw_per_ej_per_year()
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values[except_subs.loc[:, ["TO elec"], :].values]
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar urban PV"]] = (
        remaining_solar_pv_rooftop_potential()
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP oceanic"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 5,
            ),
            lambda: exogenous_protra_res_potentials_sp()
            .loc[:, "PROTRA PP oceanic"]
            .reset_coords(drop=True)
            - protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP oceanic"]
            .reset_coords(drop=True)
            * protra_max_full_load_hours()
            .loc[:, "PROTRA PP oceanic"]
            .reset_coords(drop=True)
            * unit_conversion_tw_per_ej_per_year(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP oceanic"]}, 2)
        .values
    )
    return value


@component.add(
    name="remaining potential wind",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA WIND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 4,
        "unlimited_protra_res_parameter": 2,
        "protra_operative_capacity_stock_selected": 5,
        "potential_wind_onshore": 1,
        "unit_conversion_tw_per_ej_per_year": 5,
        "exogenous_protra_res_potentials_sp": 2,
        "protra_max_full_load_hours": 5,
        "potential_wind_offshore_fixed": 2,
        "select_availability_unmature_energy_technologies_sp": 2,
        "potential_wind_offshore_floating": 1,
    },
)
def remaining_potential_wind():
    """
    Remaining wind potential ( onshore and offshore (fixed + floating) ) after discounting the already capacity in place with the real operation CF.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PROTRA WIND I": _subscript_dict["PROTRA WIND I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA WIND I"],
    )
    value.loc[:, ["TO elec"], ["PROTRA PP wind onshore"]] = (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: if_then_else(
                select_protra_res_potentials_sp() == 1,
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                - protra_operative_capacity_stock_selected()
                .loc[:, "TO elec", "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: potential_wind_onshore()
                .loc[_subscript_dict["REGIONS 9 I"]]
                .rename({"REGIONS 36 I": "REGIONS 9 I"})
                - protra_operative_capacity_stock_selected()
                .loc[:, "TO elec", "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP wind onshore"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP wind offshore"]] = (
        if_then_else(
            select_protra_res_potentials_sp() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter(),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: if_then_else(
                select_protra_res_potentials_sp() == 1,
                lambda: exogenous_protra_res_potentials_sp()
                .loc[:, "PROTRA PP wind offshore"]
                .reset_coords(drop=True)
                - protra_operative_capacity_stock_selected()
                .loc[:, "TO elec", "PROTRA PP wind offshore"]
                .reset_coords(drop=True)
                * protra_max_full_load_hours()
                .loc[:, "PROTRA PP wind offshore"]
                .reset_coords(drop=True)
                * unit_conversion_tw_per_ej_per_year(),
                lambda: if_then_else(
                    np.logical_or(
                        select_availability_unmature_energy_technologies_sp() == 1,
                        select_availability_unmature_energy_technologies_sp() == 3,
                    ),
                    lambda: (
                        potential_wind_offshore_fixed()
                        .loc[_subscript_dict["REGIONS 9 I"]]
                        .rename({"REGIONS 36 I": "REGIONS 9 I"})
                        + potential_wind_offshore_floating()
                        .loc[_subscript_dict["REGIONS 9 I"]]
                        .rename({"REGIONS 36 I": "REGIONS 9 I"})
                    )
                    - protra_operative_capacity_stock_selected()
                    .loc[:, "TO elec", "PROTRA PP wind offshore"]
                    .reset_coords(drop=True)
                    * protra_max_full_load_hours()
                    .loc[:, "PROTRA PP wind offshore"]
                    .reset_coords(drop=True)
                    * unit_conversion_tw_per_ej_per_year(),
                    lambda: potential_wind_offshore_fixed()
                    .loc[_subscript_dict["REGIONS 9 I"]]
                    .rename({"REGIONS 36 I": "REGIONS 9 I"})
                    - protra_operative_capacity_stock_selected()
                    .loc[:, "TO elec", "PROTRA PP wind offshore"]
                    .reset_coords(drop=True)
                    * protra_max_full_load_hours()
                    .loc[:, "PROTRA PP wind offshore"]
                    .reset_coords(drop=True)
                    * unit_conversion_tw_per_ej_per_year(),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP wind offshore"]}, 2)
        .values
    )
    return value


@component.add(
    name="remaining solar PV rooftop potential",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "solar_pv_rooftop_potential_c_si_mono": 1,
        "actual_rooftop_use_solar_technologies": 1,
    },
)
def remaining_solar_pv_rooftop_potential():
    """
    Remaining solar PV rooftop potential recalculated taking into account the actual share of solar PV subtechnologies.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: solar_pv_rooftop_potential_c_si_mono()
        - actual_rooftop_use_solar_technologies(),
    )


@component.add(
    name="remaining solar thermal rooftop potential",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_res_potentials_sp": 1,
        "unlimited_protra_res_parameter": 1,
        "solar_thermal_rooftop_potential": 1,
        "actual_rooftop_use_solar_technologies": 1,
    },
)
def remaining_solar_thermal_rooftop_potential():
    """
    Remaining solar thermal rooftop potential.
    """
    return if_then_else(
        select_protra_res_potentials_sp() == 0,
        lambda: xr.DataArray(
            unlimited_protra_res_parameter(),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: solar_thermal_rooftop_potential()
        - actual_rooftop_use_solar_technologies(),
    )


@component.add(
    name="SELECT AVAILABILITY UNMATURE ENERGY TECHNOLOGIES SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_availability_unmature_energy_technologies_sp"
    },
)
def select_availability_unmature_energy_technologies_sp():
    """
    Hypothesis to select the availability at large commercial scale in the future of today unmature/unproven energy technologies (H2, CCS, wind offshore floating, marine). It is possible to select individually which technology might be available, as well as none and all.
    """
    return _ext_constant_select_availability_unmature_energy_technologies_sp()


_ext_constant_select_availability_unmature_energy_technologies_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_AVAILABILITY_UNMATURE_ENERGY_TECHNOLOGIES_SP",
    {},
    _root,
    {},
    "_ext_constant_select_availability_unmature_energy_technologies_sp",
)


@component.add(
    name="SELECT PROTRA RES POTENTIALS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_protra_res_potentials_sp"},
)
def select_protra_res_potentials_sp():
    """
    =0: Unlimited RES potentials =1: Exogenous potentials (set here as scenario parameter hypothesis). =2: Endogenous for solar PV & CSP (depending on selected EROImin and link with land-use) and wind onshore & offshore (depending on selected EROImin) -see below PROTRA_RES_I marked in yellow-, exogenous for the remaining technologies
    """
    return _ext_constant_select_protra_res_potentials_sp()


_ext_constant_select_protra_res_potentials_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_PROTRA_RES_POTENTIALS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_protra_res_potentials_sp",
)


@component.add(
    name="SELECT ROOFTOP USE SOLAR TECHNOLOGIES SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_rooftop_use_solar_technologies_sp"
    },
)
def select_rooftop_use_solar_technologies_sp():
    """
    User select option for the use of rooftop of solar PV vs thermal.
    """
    return _ext_constant_select_rooftop_use_solar_technologies_sp()


_ext_constant_select_rooftop_use_solar_technologies_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_ROOFTOP_USE_SOLAR_TECHNOLOGIES_SP",
    {},
    _root,
    {},
    "_ext_constant_select_rooftop_use_solar_technologies_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_rooftop_use_solar_technologies_sp": 5,
        "efficiences_pv_technology_panels": 6,
        "solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp": 1,
        "solar_pv_rooftop_potential_c_si_mono_user_defined_sp": 1,
        "switch_energy": 1,
        "growth_land_uses_vs_2015": 1,
        "unit_conversion_pj_ej": 1,
    },
)
def solar_pv_rooftop_potential_c_si_mono():
    """
    Solar PV rooftop potential Si-monocrystaline assuming a fixed share of roofs dedicated to solar PV and thermal. Including linear variation with urban land surface.
    """
    return (
        if_then_else(
            select_rooftop_use_solar_technologies_sp() == 0,
            lambda: solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(
                float(efficiences_pv_technology_panels().loc["C Si mono"])
            )
            .loc[_subscript_dict["REGIONS 9 I"]]
            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
            lambda: if_then_else(
                select_rooftop_use_solar_technologies_sp() == 1,
                lambda: solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(
                    float(efficiences_pv_technology_panels().loc["C Si mono"])
                )
                .loc[_subscript_dict["REGIONS 9 I"]]
                .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                lambda: if_then_else(
                    select_rooftop_use_solar_technologies_sp() == 2,
                    lambda: solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(
                        float(efficiences_pv_technology_panels().loc["C Si mono"])
                    )
                    .loc[_subscript_dict["REGIONS 9 I"]]
                    .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                    lambda: if_then_else(
                        select_rooftop_use_solar_technologies_sp() == 3,
                        lambda: solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(
                            float(efficiences_pv_technology_panels().loc["C Si mono"])
                        )
                        .loc[_subscript_dict["REGIONS 9 I"]]
                        .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                        lambda: if_then_else(
                            select_rooftop_use_solar_technologies_sp() == 4,
                            lambda: solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(
                                float(
                                    efficiences_pv_technology_panels().loc["C Si mono"]
                                )
                            )
                            .loc[_subscript_dict["REGIONS 9 I"]]
                            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                            lambda: solar_pv_rooftop_potential_c_si_mono_user_defined_sp(
                                float(
                                    efficiences_pv_technology_panels().loc["C Si mono"]
                                )
                            )
                            .loc[_subscript_dict["REGIONS 9 I"]]
                            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                        ),
                    ),
                ),
            ),
        )
        * if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: growth_land_uses_vs_2015()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
        )
        / unit_conversion_pj_ej()
    )


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO 0PV 100TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 0% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_0PV_100TH_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_0pv_100th_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO 100PV 0TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 100% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_100PV_0TH_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_100pv_0th_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO 25PV 75TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 25% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_25PV_75TH_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_25pv_75th_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO 50PV 50TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 50% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_50PV_50TH_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_50pv_50th_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO 75PV 25TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a 75% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp(x, final_subs)


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "PV_PANEL_EFFICIENCY_C_Si_Mono",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_75PV_25TH_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_75pv_25th_sp",
)


@component.add(
    name="SOLAR PV ROOFTOP POTENTIAL C Si MONO USER DEFINED SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
        "__lookup__": "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
    },
)
def solar_pv_rooftop_potential_c_si_mono_user_defined_sp(x, final_subs=None):
    """
    Solar PV rooftop potential Si-monocrystaline assuming a share of rooftop for PV (vs solar thermal rooftop) defined by the user.
    """
    return _ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp(
        x, final_subs
    )


_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp = ExtLookup(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PV_PANEL_EFFICIENCY_C_Si_Mono_USER_DEFINED",
    "SOLAR_PV_ROOFTOP_POTENTIAL_C_Si_Mono_USER_DEFINED_SP",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_lookup_solar_pv_rooftop_potential_c_si_mono_user_defined_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_rooftop_use_solar_technologies_sp": 5,
        "solar_thermal_rooftop_potential_0pv_100th_sp": 1,
        "solar_thermal_rooftop_potential_100pv_0th_sp": 1,
        "solar_thermal_rooftop_potential_75pv_25th_sp": 1,
        "solar_thermal_rooftop_potential_50pv_50th_sp": 1,
        "solar_thermal_rooftop_potential_user_defined_sp": 1,
        "solar_thermal_rooftop_potential_25pv_75th_sp": 1,
        "switch_energy": 1,
        "growth_land_uses_vs_2015": 1,
        "unit_conversion_pj_ej": 1,
    },
)
def solar_thermal_rooftop_potential():
    """
    Solar thermal rooftop potential assuming a fixed share of roofs dedicated to solar PV and thermal. For current urban land.Including linear variation with urban land surface.
    """
    return (
        if_then_else(
            select_rooftop_use_solar_technologies_sp() == 0,
            lambda: solar_thermal_rooftop_potential_0pv_100th_sp()
            .loc[_subscript_dict["REGIONS 9 I"]]
            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
            lambda: if_then_else(
                select_rooftop_use_solar_technologies_sp() == 1,
                lambda: solar_thermal_rooftop_potential_25pv_75th_sp()
                .loc[_subscript_dict["REGIONS 9 I"]]
                .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                lambda: if_then_else(
                    select_rooftop_use_solar_technologies_sp() == 2,
                    lambda: solar_thermal_rooftop_potential_50pv_50th_sp()
                    .loc[_subscript_dict["REGIONS 9 I"]]
                    .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                    lambda: if_then_else(
                        select_rooftop_use_solar_technologies_sp() == 3,
                        lambda: solar_thermal_rooftop_potential_75pv_25th_sp()
                        .loc[_subscript_dict["REGIONS 9 I"]]
                        .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                        lambda: if_then_else(
                            select_rooftop_use_solar_technologies_sp() == 4,
                            lambda: solar_thermal_rooftop_potential_100pv_0th_sp()
                            .loc[_subscript_dict["REGIONS 9 I"]]
                            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                            lambda: solar_thermal_rooftop_potential_user_defined_sp()
                            .loc[_subscript_dict["REGIONS 9 I"]]
                            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
                        ),
                    ),
                ),
            ),
        )
        * if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: growth_land_uses_vs_2015()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
        )
        / unit_conversion_pj_ej()
    )


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL 0PV 100TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp"
    },
)
def solar_thermal_rooftop_potential_0pv_100th_sp():
    """
    Solar thermal rooftop potential 0% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp()


_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_0PV_100TH_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_0pv_100th_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL 100PV 0TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp"
    },
)
def solar_thermal_rooftop_potential_100pv_0th_sp():
    """
    Solar thermal rooftop potential 100% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp()


_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_100PV_0TH_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_100pv_0th_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL 25PV 75TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp"
    },
)
def solar_thermal_rooftop_potential_25pv_75th_sp():
    """
    Solar thermal rooftop potential 25% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp()


_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_25PV_75TH_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_25pv_75th_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL 50PV 50TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp"
    },
)
def solar_thermal_rooftop_potential_50pv_50th_sp():
    """
    Solar thermal rooftop potential 50% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp()


_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_50PV_50TH_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_50pv_50th_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL 75PV 25TH SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp"
    },
)
def solar_thermal_rooftop_potential_75pv_25th_sp():
    """
    Solar thermal rooftop potential 75% share of rooftop for PV (vs solar thermal rooftop).
    """
    return _ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp()


_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-data",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_75PV_25TH_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_75pv_25th_sp",
)


@component.add(
    name="SOLAR THERMAL ROOFTOP POTENTIAL USER DEFINED SP",
    units="PJ/Year",
    subscripts=["REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_solar_thermal_rooftop_potential_user_defined_sp"
    },
)
def solar_thermal_rooftop_potential_user_defined_sp():
    """
    Solar thermal rooftop potential share of rooftop for PV (vs solar thermal rooftop) defined by the user.
    """
    return _ext_constant_solar_thermal_rooftop_potential_user_defined_sp()


_ext_constant_solar_thermal_rooftop_potential_user_defined_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SOLAR_THERMAL_ROOFTOP_POTENTIAL_USER_DEFINED_SP*",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_constant_solar_thermal_rooftop_potential_user_defined_sp",
)


@component.add(
    name="SWITCH NRG LIMITED RES POTENTIALS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_limited_res_potentials"},
)
def switch_nrg_limited_res_potentials():
    """
    Can take two values: 1: limited RES potentials (either exogenous or endogenously) 0: unlimited RES potentials (although the annual growth rate can still be limited following energy module parametrization)
    """
    return _ext_constant_switch_nrg_limited_res_potentials()


_ext_constant_switch_nrg_limited_res_potentials = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_LIMITED_RES_POTENTIALS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_limited_res_potentials",
)


@component.add(
    name="UNLIMITED PROTRA RES PARAMETER",
    units="EJ/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unlimited_protra_res_parameter"},
)
def unlimited_protra_res_parameter():
    """
    This parameter represents a extremely high potential which is used in the model in order to represent that PROTRA RES are in practical unlimited.
    """
    return _ext_constant_unlimited_protra_res_parameter()


_ext_constant_unlimited_protra_res_parameter = ExtConstant(
    "model_parameters/energy/energy-potentials.xlsx",
    "PROTRA",
    "UNLIMITED_PROTRA_RES_PARAMETER",
    {},
    _root,
    {},
    "_ext_constant_unlimited_protra_res_parameter",
)
