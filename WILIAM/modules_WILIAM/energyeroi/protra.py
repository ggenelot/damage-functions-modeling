"""
Module energyeroi.protra
Translated using PySD version 3.13.4
"""

@component.add(
    name="Clean water for OM required for PROTRA",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 1,
        "clean_water_intensity_csp_om": 1,
        "matrix_unit_prefixes": 2,
    },
)
def clean_water_for_om_required_for_protra():
    """
    Annual water required for the operation and maintenance of the capacity of PROTRA in operation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA PP solar CSP"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["PROTRA PP solar CSP"]] = (
        (
            protra_operative_capacity_stock_selected()
            .loc[:, :, "PROTRA PP solar CSP"]
            .reset_coords(drop=True)
            * clean_water_intensity_csp_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    return value


@component.add(
    name="Distilled water for OM required for PROTRA",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 2,
        "distilled_water_intensity_csp_om": 1,
        "matrix_unit_prefixes": 4,
        "distilled_water_intensity_pv_om": 1,
    },
)
def distilled_water_for_om_required_for_protra():
    """
    Annual water required for the operation and maintenance of the capacity of PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA PP solar CSP"]] = False
    except_subs.loc[:, :, ["PROTRA PP solar open space PV"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["PROTRA PP solar CSP"]] = (
        (
            protra_operative_capacity_stock_selected()
            .loc[:, :, "PROTRA PP solar CSP"]
            .reset_coords(drop=True)
            * distilled_water_intensity_csp_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar open space PV"]] = (
        (
            protra_operative_capacity_stock_selected()
            .loc[:, :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * distilled_water_intensity_pv_om()
            * float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    return value


@component.add(
    name="dynEROIst PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 9,
        "fenust_protra_eroi_exogenous": 4,
        "dynfenust_protra": 5,
    },
)
def dyneroist_protra():
    """
    Dynamic evolution of EROIst over time per PROTRA. For some technologies the EROI is computed fully endogenously and dynamically, while for other the EROIst has been set exogenously, but still it is affected by some dynamic factors (e.g., real CF).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[:, :, ["PROTRA PP hydropower dammed"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP hydropower dammed"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA PP hydropower dammed"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP hydropower dammed"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP geothermal"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP geothermal"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA PP geothermal"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP geothermal"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solid bio"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP solid bio"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA PP solid bio"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solid bio"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP oceanic"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP oceanic"]
            .reset_coords(drop=True),
            fenust_protra_eroi_exogenous()
            .loc[:, :, "PROTRA PP oceanic"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP oceanic"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP wind onshore"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP wind onshore"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA PP wind onshore"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP wind onshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP wind offshore"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP wind offshore"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA PP wind offshore"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP wind offshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar open space PV"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar urban PV"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP solar urban PV"]
            .reset_coords(drop=True),
            dynfenust_protra()
            .loc[:, :, "PROTRA PP solar urban PV"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar CSP"]] = (
        zidz(
            protra_to_allocated()
            .loc[:, :, "PROTRA PP solar CSP"]
            .reset_coords(drop=True),
            dynfenust_protra().loc[:, :, "PROTRA PP solar CSP"].reset_coords(drop=True),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA PP solar CSP"]] = False
    except_subs.loc[:, :, ["PROTRA PP solar urban PV"]] = False
    except_subs.loc[:, :, ["PROTRA PP solar open space PV"]] = False
    except_subs.loc[:, :, ["PROTRA PP wind offshore"]] = False
    except_subs.loc[:, :, ["PROTRA PP wind onshore"]] = False
    except_subs.loc[:, :, ["PROTRA PP oceanic"]] = False
    except_subs.loc[:, :, ["PROTRA PP solid bio"]] = False
    except_subs.loc[:, :, ["PROTRA PP geothermal"]] = False
    except_subs.loc[:, :, ["PROTRA PP hydropower dammed"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="dynFEnU decom PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_energy_requirements_for_decomm_protra": 1,
        "dynfenust_intensity_new_protra": 1,
        "protra_capacity_decommissioning_selected": 1,
    },
)
def dynfenu_decom_protra():
    """
    Dynamic energy used (in final terms) required to decommission PROTRA capacity which have ended their lifetime.
    """
    return (
        share_energy_requirements_for_decomm_protra()
        * dynfenust_intensity_new_protra().transpose(
            "NRG PROTRA I", "REGIONS 9 I", "NRG TO I"
        )
        * protra_capacity_decommissioning_selected().transpose(
            "NRG PROTRA I", "REGIONS 9 I", "NRG TO I"
        )
    ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")


@component.add(
    name="dynFEnU water OM PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "clean_water_for_om_required_for_protra": 1,
        "embodied_fe_intensity_clean_water": 1,
        "embodied_fe_intensity_distilled_water": 1,
        "distilled_water_for_om_required_for_protra": 1,
        "matrix_unit_prefixes": 2,
    },
)
def dynfenu_water_om_protra():
    """
    Dynamic energy use (in final terms) for water for O&M of VRES per technology.
    """
    return (
        (
            clean_water_for_om_required_for_protra()
            * embodied_fe_intensity_clean_water()
            + distilled_water_for_om_required_for_protra()
            * embodied_fe_intensity_distilled_water()
        )
        * float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        / float(matrix_unit_prefixes().loc["exa", "mega"])
    )


@component.add(
    name="dynFEnUst intensity new grids",
    units="EJ/TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_new_grids": 1,
        "protra_capacity_expansion_selected": 1,
    },
)
def dynfenust_intensity_new_grids():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for overgrids by PROTRA. Dynamic variable affected by recycling policies.
    """
    return zidz(
        required_embodied_fe_materials_for_new_grids().expand_dims(
            {"NRG TO I": _subscript_dict["NRG TO I"]}, 2
        ),
        protra_capacity_expansion_selected().transpose(
            "REGIONS 9 I", "NRG PROTRA I", "NRG TO I"
        ),
    ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")


@component.add(
    name="dynFEnUst intensity new PROTRA",
    units="EJ/TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "manufacturing_energy_intensity_protra": 1,
        "transport_materials_energy_intensity_protra": 1,
        "protra_capacity_expansion_selected": 1,
        "required_embodied_fe_materials_for_new_protra": 1,
    },
)
def dynfenust_intensity_new_protra():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for new PROTRA. Dynamic variable affected by recycling policies.
    """
    return (
        manufacturing_energy_intensity_protra()
        + transport_materials_energy_intensity_protra()
        + zidz(
            required_embodied_fe_materials_for_new_protra().expand_dims(
                {"NRG TO I": _subscript_dict["NRG TO I"]}, 2
            ),
            protra_capacity_expansion_selected().transpose(
                "REGIONS 9 I", "NRG PROTRA I", "NRG TO I"
            ),
        ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")
    )


@component.add(
    name="dynFEnUst intensity OM PROTRA",
    units="EJ/(Year*TW)",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_om_protra": 1,
        "protra_operative_capacity_stock_selected": 1,
    },
)
def dynfenust_intensity_om_protra():
    """
    Energy use (in final energy terms) per new installed capacity (TW) for O&M BY PROTRA. Dynamic variable affected by recycling policies.
    """
    return zidz(
        required_embodied_fe_materials_for_om_protra().expand_dims(
            {"NRG TO I": _subscript_dict["NRG TO I"]}, 2
        ),
        protra_operative_capacity_stock_selected().transpose(
            "REGIONS 9 I", "NRG PROTRA I", "NRG TO I"
        ),
    ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")


@component.add(
    name="dynFEnUst new grids",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_intensity_new_grids": 1,
        "protra_capacity_expansion_selected": 1,
    },
)
def dynfenust_new_grids():
    """
    Dynamic energy used (in final terms) for the construction of new grids related to new PROTRA. Dynamic variable affected by recycling policies.
    """
    return dynfenust_intensity_new_grids() * protra_capacity_expansion_selected()


@component.add(
    name="dynFEnUst new PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_intensity_new_protra": 1,
        "protra_capacity_expansion_selected": 1,
    },
)
def dynfenust_new_protra():
    """
    Dynamic energy used (in final terms) for the construction of new PROTRA capacity. Dynamic variable affected by recycling policies.
    """
    return dynfenust_intensity_new_protra() * protra_capacity_expansion_selected()


@component.add(
    name="dynFEnUst OM PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_intensity_om_protra": 1,
        "protra_operative_capacity_stock_selected": 1,
        "dynfenu_water_om_protra": 1,
    },
)
def dynfenust_om_protra():
    """
    Dynamic energy used (in final terms) for the operation and maintenance of PROTRA capacity stock. Dynamic variable affected by recycling policies.
    """
    return (
        dynfenust_intensity_om_protra() * protra_operative_capacity_stock_selected()
        + dynfenu_water_om_protra()
    )


@component.add(
    name="dynFEnUst PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_new_protra": 1,
        "dynfenust_new_grids": 1,
        "dynfenu_decom_protra": 1,
        "dynfenust_om_protra": 1,
        "protra_to_allocated": 1,
        "share_self_electricity_consumption_protra": 1,
    },
)
def dynfenust_protra():
    """
    Dynamic final energy use invested (equivalent to the denominator of the EROIst for PROTRA per technology).
    """
    return (
        dynfenust_new_protra()
        + dynfenust_new_grids()
        + dynfenu_decom_protra()
        + dynfenust_om_protra()
        + protra_to_allocated() * share_self_electricity_consumption_protra()
    )


@component.add(
    name="Embodied FE intensity clean water",
    units="MJ/kg",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_clean_water": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def embodied_fe_intensity_clean_water():
    """
    Embodied final energy intensity for clean water consumption in PROTRA plants.
    """
    return (
        embodied_pe_intensity_clean_water()
        * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="Embodied FE intensity distilled water",
    units="MJ/kg",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_distilled_water": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def embodied_fe_intensity_distilled_water():
    """
    Embodied final energy intensity for distilled water consumption in PROTRA plants.
    """
    return (
        embodied_pe_intensity_distilled_water()
        * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="EPTB dynamic",
    units="Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_lifetime": 1, "dyneroist_protra": 1},
)
def eptb_dynamic():
    """
    Energy payback time per RES for electricity generation.
    """
    return zidz(
        protra_lifetime().expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 2),
        dyneroist_protra().transpose("REGIONS 9 I", "NRG PROTRA I", "NRG TO I"),
    ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")


@component.add(
    name="EROIfinal PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_over_lifetime_protra": 2,
        "share_total_transmission_loss": 2,
        "share_self_electricity_consumption_protra": 1,
        "fenust_protra": 1,
        "unit_conversion_mj_ej": 1,
        "protra_capacity_expansion_selected": 1,
        "unit_conversion_mw_tw": 1,
        "fe_intensity_current_grids_om": 1,
    },
)
def eroifinal_protra():
    """
    EROI final (over the full lifetime of the infrastructure) per RES technology for generating electricity.
    """
    return zidz(
        to_over_lifetime_protra() * (1 - share_total_transmission_loss()),
        fenust_protra()
        + (
            share_total_transmission_loss().loc[:, "TO elec"].reset_coords(drop=True)
            * share_self_electricity_consumption_protra()
            * to_over_lifetime_protra().transpose(
                "REGIONS 9 I", "NRG PROTRA I", "NRG TO I"
            )
        ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")
        + fe_intensity_current_grids_om()
        * protra_capacity_expansion_selected()
        * unit_conversion_mw_tw()
        / unit_conversion_mj_ej(),
    )


@component.add(
    name="EROIst PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_over_lifetime_protra": 1, "fenust_protra": 1},
)
def eroist_protra():
    """
    EROIst (over the full lifetime of the infrastructure) by PROTRA.
    """
    return zidz(to_over_lifetime_protra(), fenust_protra())


@component.add(
    name="EXOGENOUS EROIst PROTRA",
    units="DMNL",
    subscripts=["NRG PROTRA I"],
    comp_type="Data, Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_data_exogenous_eroist_protra",
        "__data__": "_ext_data_exogenous_eroist_protra",
        "time": 1,
    },
)
def exogenous_eroist_protra():
    """
    Exogenous EROIst levels for those PROTRA for which we do not have computed the EROI endogenous and dynamically in the model.
    """
    value = xr.DataArray(
        np.nan, {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]}, ["NRG PROTRA I"]
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA PP hydropower dammed"]] = True
    value.values[def_subs.values] = _ext_data_exogenous_eroist_protra(time()).values[
        def_subs.values
    ]
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[["PROTRA PP geothermal"]] = True
    def_subs.loc[["PROTRA PP solid bio"]] = True
    def_subs.loc[["PROTRA PP oceanic"]] = True
    value.values[def_subs.values] = _ext_constant_exogenous_eroist_protra().values[
        def_subs.values
    ]
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["PROTRA PP hydropower dammed"]] = False
    except_subs.loc[["PROTRA PP geothermal"]] = False
    except_subs.loc[["PROTRA PP solid bio"]] = False
    except_subs.loc[["PROTRA PP oceanic"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_data_exogenous_eroist_protra = ExtData(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "time_RES_nuclear_index",
    "EROIst_initial_Hydro",
    "interpolate",
    {"NRG PROTRA I": ["PROTRA PP hydropower dammed"]},
    _root,
    {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    "_ext_data_exogenous_eroist_protra",
)

_ext_constant_exogenous_eroist_protra = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "EROIst_geot_elec",
    {"NRG PROTRA I": ["PROTRA PP geothermal"]},
    _root,
    {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    "_ext_constant_exogenous_eroist_protra",
)

_ext_constant_exogenous_eroist_protra.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "EROIst_solid_bioE_elec",
    {"NRG PROTRA I": ["PROTRA PP solid bio"]},
)

_ext_constant_exogenous_eroist_protra.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "EROIst_oceanic",
    {"NRG PROTRA I": ["PROTRA PP oceanic"]},
)


@component.add(
    name="FEnU water OM PTOTRA",
    units="EJ",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_selected": 1,
        "embodied_fe_intensity_distilled_water": 1,
        "embodied_fe_intensity_clean_water": 1,
        "distilled_water_for_om_required_for_protra": 1,
        "clean_water_for_om_required_for_protra": 1,
        "protra_lifetime": 1,
        "matrix_unit_prefixes": 4,
    },
)
def fenu_water_om_ptotra():
    """
    Energy use (in final terms) for water for PROTRA over all the lifetime of the infrastructure.
    """
    return (
        protra_capacity_expansion_selected()
        * (
            clean_water_for_om_required_for_protra()
            * embodied_fe_intensity_clean_water()
            + distilled_water_for_om_required_for_protra()
            * embodied_fe_intensity_distilled_water()
        )
        * protra_lifetime()
        * (
            float(matrix_unit_prefixes().loc["tera", "mega"])
            / float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        )
        * (
            float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
            / float(matrix_unit_prefixes().loc["exa", "mega"])
        )
    )


@component.add(
    name="FEnUst intensity PROTRA EROI exogenous",
    units="EJ/TW",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_protra_full_load_hours": 1,
        "protra_lifetime": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_wh_we": 1,
        "matrix_unit_prefixes": 1,
        "exogenous_eroist_protra": 1,
    },
)
def fenust_intensity_protra_eroi_exogenous():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for PROTRA for which we assume an exogenous EROIst value. We assume the same lifetime for PHS than for hydro.
    """
    return zidz(
        cf_protra_full_load_hours()
        * protra_lifetime()
        * (
            unit_conversion_j_wh()
            * unit_conversion_wh_we()
            / float(matrix_unit_prefixes().loc["exa", "tera"])
        ),
        exogenous_eroist_protra().expand_dims(
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
        ),
    )


@component.add(
    name="FEnUst OM PROTRA dynEROI",
    units="EJ",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_selected": 1,
        "dynfenust_intensity_om_protra": 1,
        "fenu_water_om_ptotra": 1,
        "protra_lifetime": 1,
    },
)
def fenust_om_protra_dyneroi():
    """
    Energy use over the lifetime for operation and maintenance of VRES for electricity generation (value W for dispatchable RES).
    """
    return (
        protra_capacity_expansion_selected() * dynfenust_intensity_om_protra()
        + fenu_water_om_ptotra()
    ) * protra_lifetime()


@component.add(
    name="FEnUst PROTRA",
    units="EJ",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenust_protra_eroi_exogenous": 1, "fenust_protra_dyneroi": 5},
)
def fenust_protra():
    """
    Final energy investments over lifetime PROTRA technologies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["PROTRA PP solar CSP"]] = False
    except_subs.loc[:, :, ["PROTRA PP solar open space PV"]] = False
    except_subs.loc[:, :, ["PROTRA PP solar urban PV"]] = False
    except_subs.loc[:, :, ["PROTRA PP wind onshore"]] = False
    except_subs.loc[:, :, ["PROTRA PP wind offshore"]] = False
    value.values[except_subs.values] = fenust_protra_eroi_exogenous().values[
        except_subs.values
    ]
    value.loc[:, :, ["PROTRA PP solar CSP"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA PP solar CSP"]
        .reset_coords(drop=True)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar open space PV"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar urban PV"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA PP solar urban PV"]
        .reset_coords(drop=True)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP wind onshore"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA PP wind onshore"]
        .reset_coords(drop=True)
        .expand_dims({"NRG PRO I": ["PROTRA PP wind onshore"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP wind offshore"]] = (
        fenust_protra_dyneroi()
        .loc[:, :, "PROTRA PP wind offshore"]
        .reset_coords(drop=True)
        .expand_dims({"NRG PRO I": ["PROTRA PP wind offshore"]}, 2)
        .values
    )
    return value


@component.add(
    name="FEnUst PROTRA dynEROI",
    units="EJ",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_new_protra": 1,
        "share_energy_requirements_for_decomm_protra": 1,
        "fenust_om_protra_dyneroi": 1,
        "to_over_lifetime_protra": 1,
        "share_self_electricity_consumption_protra": 1,
    },
)
def fenust_protra_dyneroi():
    """
    Energy use (in final terms) invested over lifetime per PROTRA (including installation of new capacity and O&M).
    """
    return (
        dynfenust_new_protra() * (1 + share_energy_requirements_for_decomm_protra())
        + fenust_om_protra_dyneroi()
        + to_over_lifetime_protra() * share_self_electricity_consumption_protra()
    )


@component.add(
    name="FEnUst PROTRA EROI exogenous",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fenust_intensity_protra_eroi_exogenous": 1,
        "protra_capacity_expansion_selected": 1,
    },
)
def fenust_protra_eroi_exogenous():
    """
    Final energy use invested over lifetime for those PROTRA for which the EROI is set exogenously.
    """
    return (
        fenust_intensity_protra_eroi_exogenous()
        * protra_capacity_expansion_selected().transpose(
            "REGIONS 9 I", "NRG PROTRA I", "NRG TO I"
        )
    ).transpose("REGIONS 9 I", "NRG TO I", "NRG PROTRA I")


@component.add(
    name="manufacturing energy intensity for PV panels",
    units="EJ/TW",
    subscripts=[
        "REGIONS 9 I",
        "NRG TO I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_intensity_manufacturing_pv_panels": 2,
        "share_new_pv_subtechn_land": 1,
        "unit_conversion_mw_tw": 2,
        "unit_conversion_mj_ej": 2,
        "share_new_pv_subtechn_urban": 1,
    },
)
def manufacturing_energy_intensity_for_pv_panels():
    """
    Energy spent for the manufacturing of PV panels
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        [
            "REGIONS 9 I",
            "NRG TO I",
            "PROTRA PP SOLAR PV I",
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
        ],
    )
    value.loc[:, :, ["PROTRA PP solar open space PV"], :] = (
        (
            sum(
                fe_intensity_manufacturing_pv_panels().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                ),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .expand_dims(
            {
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ]
            },
            3,
        )
        .values
    )
    value.loc[:, :, ["PROTRA PP solar urban PV"], :] = (
        (
            sum(
                fe_intensity_manufacturing_pv_panels().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                ),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .expand_dims(
            {
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ]
            },
            3,
        )
        .values
    )
    return value


@component.add(
    name="manufacturing energy intensity PROTRA",
    units="EJ/TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"manufacturing_energy_intensity_for_pv_panels": 1},
)
def manufacturing_energy_intensity_protra():
    """
    Manufacturing energy intensity (FE) for all PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA PP SOLAR PV I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, _subscript_dict["PROTRA PP SOLAR PV I"]] = sum(
        manufacturing_energy_intensity_for_pv_panels().rename(
            {
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
            }
        ),
        dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
    ).values
    return value


@component.add(
    name="required embodied FE materials for new grids",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_new_grids": 1},
)
def required_embodied_fe_materials_for_new_grids():
    """
    Required embodied final energy of total material consumption for overgrids.
    """
    return sum(
        required_embodied_fe_per_material_for_new_grids().rename(
            {"MATERIALS I": "MATERIALS I!"}
        ),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="required embodied FE materials for new PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_new_protra": 1},
)
def required_embodied_fe_materials_for_new_protra():
    """
    Required embodied final energy of total material consumption for new PROTRA
    """
    return sum(
        required_embodied_fe_per_material_for_new_protra().rename(
            {"MATERIALS I": "MATERIALS I!"}
        ),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="required embodied FE materials for OM PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_per_material_for_om_new_protra": 1},
)
def required_embodied_fe_materials_for_om_protra():
    """
    Required embodied final energy of total material consumption for O&M of PROTRA.
    """
    return sum(
        required_embodied_fe_per_material_for_om_new_protra().rename(
            {"MATERIALS I": "MATERIALS I!"}
        ),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="required embodied FE materials for PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_new_protra": 1,
        "required_embodied_fe_materials_for_om_protra": 1,
    },
)
def required_embodied_fe_materials_for_protra():
    """
    Required embodied final energy of total material consumption for PROTRA.
    """
    return sum(
        required_embodied_fe_materials_for_new_protra().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG PROTRA I!"],
    ) + sum(
        required_embodied_fe_materials_for_om_protra().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="required embodied FE per material for new grids",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "unit_conversion_kg_mt": 2,
        "unit_conversion_mj_ej": 2,
        "materials_required_for_new_grids_by_protra": 2,
        "embodied_fe_intensity_materials_36r": 2,
    },
)
def required_embodied_fe_per_material_for_new_grids():
    """
    Required embodied final energy of material consumption for overgrids.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 8 I": _subscript_dict["REGIONS 8 I"],
                "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 8 I", "NRG PROTRA I", "MATERIALS I"],
        ),
        lambda: materials_required_for_new_grids_by_protra()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        * embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 8 I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values
    value.loc[["EU27"], :, :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["NRG PROTRA I", "MATERIALS I"],
            ),
            lambda: materials_required_for_new_grids_by_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="required embodied FE per material for new PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 6,
        "unit_conversion_kg_mt": 6,
        "unit_conversion_mj_ej": 6,
        "materials_required_for_new_protra": 6,
        "embodied_fe_intensity_materials_36r": 6,
        "machining_rate_pv": 4,
        "scrap_rate": 8,
    },
)
def required_embodied_fe_per_material_for_new_protra():
    """
    Required embodied final energy of material consumption for new PROTRA.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS 8 I"], :, :] = True
    except_subs.loc[
        _subscript_dict["REGIONS 8 I"], ["PROTRA PP solar open space PV"], :
    ] = False
    except_subs.loc[_subscript_dict["REGIONS 8 I"], ["PROTRA PP solar urban PV"], :] = (
        False
    )
    value.values[except_subs.values] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 8 I": _subscript_dict["REGIONS 8 I"],
                "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 8 I", "NRG PROTRA I", "MATERIALS I"],
        ),
        lambda: materials_required_for_new_protra()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        * embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 8 I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values[except_subs.loc[_subscript_dict["REGIONS 8 I"], :, :].values]
    value.loc[_subscript_dict["REGIONS 8 I"], ["PROTRA PP solar open space PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 8 I": _subscript_dict["REGIONS 8 I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["REGIONS 8 I", "MATERIALS I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc[_subscript_dict["REGIONS 8 I"], "PROTRA PP solar open space PV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            * embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 8 I"})
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], ["PROTRA PP solar urban PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 8 I": _subscript_dict["REGIONS 8 I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["REGIONS 8 I", "MATERIALS I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc[_subscript_dict["REGIONS 8 I"], "PROTRA PP solar urban PV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            * embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 8 I"})
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[["EU27"], :, :] = True
    except_subs.loc[["EU27"], ["PROTRA PP solar open space PV"], :] = False
    except_subs.loc[["EU27"], ["PROTRA PP solar urban PV"], :] = False
    value.values[except_subs.values] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["NRG PROTRA I", "MATERIALS I"],
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values[except_subs.loc[["EU27"], :, :].values]
    )
    value.loc[["EU27"], ["PROTRA PP solar open space PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", "PROTRA PP solar open space PV", :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1)
        .values
    )
    value.loc[["EU27"], ["PROTRA PP solar urban PV"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
            lambda: materials_required_for_new_protra()
            .loc["EU27", "PROTRA PP solar urban PV", :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
            / ((1 + scrap_rate()) * (1 + machining_rate_pv() + scrap_rate())),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="required embodied FE per material for OM new PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "materials_required_for_om_protra": 2,
        "unit_conversion_kg_mt": 2,
        "unit_conversion_mj_ej": 2,
        "embodied_fe_intensity_materials_36r": 2,
    },
)
def required_embodied_fe_per_material_for_om_new_protra():
    """
    Required embodied final energy of material consumption for O&M new RES elec.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = if_then_else(
        switch_energy() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 8 I": _subscript_dict["REGIONS 8 I"],
                "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 8 I", "NRG PROTRA I", "MATERIALS I"],
        ),
        lambda: materials_required_for_om_protra()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        * embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 8 I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
    ).values
    value.loc[["EU27"], :, :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["NRG PROTRA I", "MATERIALS I"],
            ),
            lambda: materials_required_for_om_protra()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            * (unit_conversion_kg_mt() / unit_conversion_mj_ej()),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="share FEnU overgrids over total FEnU PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_new_grids": 1, "total_dynfenu_protra": 1},
)
def share_fenu_overgrids_over_total_fenu_protra():
    """
    Share new rids over total FEnU RES for PROTRA.
    """
    return zidz(
        sum(
            dynfenust_new_grids().rename(
                {"NRG TO I": "NRG TO I!", "NRG PROTRA I": "NRG PROTRA I!"}
            ),
            dim=["NRG TO I!", "NRG PROTRA I!"],
        ),
        total_dynfenu_protra(),
    )


@component.add(
    name="TO over lifetime PROTRA",
    units="EJ",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_protra": 1,
        "protra_capacity_expansion_selected": 1,
        "unit_conversion_wh_we": 1,
        "protra_lifetime": 1,
        "unit_conversion_j_wh": 1,
        "matrix_unit_prefixes": 1,
    },
)
def to_over_lifetime_protra():
    """
    Total electricity output expected to be generated over the full operation of the infrastructure of the new PROTRA capacity installed, assuming current performance factors.
    """
    return (
        cf_protra()
        * protra_capacity_expansion_selected()
        * (1 / (1 / unit_conversion_wh_we()))
        * protra_lifetime()
        * (unit_conversion_j_wh() / float(matrix_unit_prefixes().loc["exa", "tera"]))
    )


@component.add(
    name="Total blue water for OM required by PROTRA",
    units="Mt",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "clean_water_for_om_required_for_protra": 1,
        "distilled_water_for_om_required_for_protra": 1,
    },
)
def total_blue_water_for_om_required_by_protra():
    """
    Total blue water requirements for PROTRA.
    """
    return sum(
        clean_water_for_om_required_for_protra().rename(
            {"NRG TO I": "NRG TO I!", "NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG TO I!", "NRG PROTRA I!"],
    ) + sum(
        distilled_water_for_om_required_for_protra().rename(
            {"NRG TO I": "NRG TO I!", "NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG TO I!", "NRG PROTRA I!"],
    )


@component.add(
    name="Total dynFEnU PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenust_protra": 1},
)
def total_dynfenu_protra():
    """
    Dynamic final energy use invested for all PROTRA.
    """
    return sum(
        dynfenust_protra().rename(
            {"NRG TO I": "NRG TO I!", "NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG TO I!", "NRG PROTRA I!"],
    )


@component.add(
    name="Total FEnUst PROTRA EROI exogenous",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenust_protra_eroi_exogenous": 1},
)
def total_fenust_protra_eroi_exogenous():
    """
    Final energy use invested over lifetime for those PROTRA for which the EROI is set exogenously.
    """
    return sum(
        fenust_protra_eroi_exogenous().rename(
            {"NRG TO I": "NRG TO I!", "NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG TO I!", "NRG PROTRA I!"],
    )


@component.add(
    name="transport materials energy intensity PROTRA",
    units="EJ/TW",
    subscripts=["NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_materials_fe_intensity_pv_technologies": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def transport_materials_energy_intensity_protra():
    """
    Energy for transporting materials for all PROTRA (round-trip).
    """
    value = xr.DataArray(
        np.nan,
        {
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["NRG TO I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["TO elec"], _subscript_dict["PROTRA PP SOLAR PV I"]] = False
    value.values[except_subs.values] = 0
    value.loc[["TO elec"], _subscript_dict["PROTRA PP SOLAR PV I"]] = (
        (
            2
            * sum(
                transport_materials_fe_intensity_pv_technologies().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                ),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * unit_conversion_mw_tw()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 0)
        .values
    )
    return value
