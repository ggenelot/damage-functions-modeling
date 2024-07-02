"""
Module materialsprimary_demand_vs_availability_medeas
Translated using PySD version 3.14.0
"""

@component.add(
    name="cumulative materials to extract BU from 2015",
    units="Mt",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulated_total_materials_to_extract_for_electrified_transport_from_2015_9r": 1,
        "cumulated_extracted_materials_all_protras_from_2015": 1,
        "cumulated_materials_extracted_for_all_prosup_from_2015": 1,
    },
)
def cumulative_materials_to_extract_bu_from_2015():
    """
    Cumulative materials demand through bottom-up (BU) estimation for specific technologies from the year 2015.
    """
    return (
        cumulated_total_materials_to_extract_for_electrified_transport_from_2015_9r()
        + cumulated_extracted_materials_all_protras_from_2015()
        + cumulated_materials_extracted_for_all_prosup_from_2015()
    )


@component.add(
    name="indicator materials reserves availability",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_tot_cumulative_dem_vs_reserves_materials": 1},
)
def indicator_materials_reserves_availability():
    """
    =1 while the cumulative demand is lower than the estimated reserves, and =0 when the cumulative demand surpasses the estimated reserves.
    """
    return if_then_else(
        share_tot_cumulative_dem_vs_reserves_materials() < 1,
        lambda: xr.DataArray(
            1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="indicator materials resources availability",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_tot_cumulative_dem_vs_resources_materials": 1},
)
def indicator_materials_resources_availability():
    """
    =1 while the cumulative demand is lower than the estimated resources, and =0 when the cumulative demand surpasses the estimated resources.
    """
    return if_then_else(
        share_tot_cumulative_dem_vs_resources_materials() < 1,
        lambda: xr.DataArray(
            1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="risk indicator mineral availability",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "indicator_materials_resources_availability": 2,
        "indicator_materials_reserves_availability": 1,
    },
)
def risk_indicator_mineral_availability():
    """
    Risk indicator: - if cumulated primary demand > resources: 1 (high risk) - if cumulated primary demand > reserves but <:resources: 0.5 (medium risk) - if cumulated primary demand < reserves: 0 (no risk detected)
    """
    return if_then_else(
        indicator_materials_resources_availability() == 0,
        lambda: xr.DataArray(
            1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: if_then_else(
            np.logical_and(
                indicator_materials_reserves_availability() == 0,
                indicator_materials_resources_availability() == 1,
            ),
            lambda: xr.DataArray(
                0.5, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
        ),
    )


@component.add(
    name="share cumulative dem materials to extract BU techs vs total",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_bu_from_2015": 1,
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
    },
)
def share_cumulative_dem_materials_to_extract_bu_techs_vs_total():
    """
    Yearly share of cumulative demand of materials to extract from bottom-up (BU) vs. total.
    """
    return zidz(
        sum(
            cumulative_materials_to_extract_bu_from_2015().rename(
                {"REGIONS 9 I": "REGIONS 9 I!"}
            ),
            dim=["REGIONS 9 I!"],
        ),
        total_cumulative_demand_materials_to_extract_from_2015(),
    )


@component.add(
    name="share materials cumulative demand to extract vs reserves BU techs",
    units="DMNL",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_bu_from_2015": 1,
        "global_mineral_reserves_2015": 1,
    },
)
def share_materials_cumulative_demand_to_extract_vs_reserves_bu_techs():
    """
    Share of materials cumulative demand to extract in mines from bottom-up (BU) vs reserves of each material.
    """
    return zidz(
        cumulative_materials_to_extract_bu_from_2015(),
        global_mineral_reserves_2015().expand_dims(
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
        ),
    )


@component.add(
    name="share materials cumulative demand to extract vs resources BU techs",
    units="DMNL",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_bu_from_2015": 1,
        "global_mineral_resources_2015": 1,
    },
)
def share_materials_cumulative_demand_to_extract_vs_resources_bu_techs():
    """
    Share of materials cumulative demand to extract in mines from bottom-up (BU) vs resources of each material.
    """
    return zidz(
        cumulative_materials_to_extract_bu_from_2015(),
        global_mineral_resources_2015().expand_dims(
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
        ),
    )


@component.add(
    name="share minerals consumption alt techn vs total economy",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_global_materials_required_bu_techs": 2,
        "demand_projection_materials_roe": 1,
    },
)
def share_minerals_consumption_alt_techn_vs_total_economy():
    """
    Share of minerals consumptions of the alternative technologies with relation to the total.
    """
    return zidz(
        total_global_materials_required_bu_techs(),
        demand_projection_materials_roe() + total_global_materials_required_bu_techs(),
    )


@component.add(
    name="share RoE cumulative demand to extract vs reserves materials",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_roe_from_2015": 1,
        "global_mineral_reserves_2015": 1,
    },
)
def share_roe_cumulative_demand_to_extract_vs_reserves_materials():
    """
    Yearly share of cumulative demand of the rest of the economy to be extracted in mines of materials vs. reserves.
    """
    return zidz(
        cumulative_materials_to_extract_roe_from_2015(), global_mineral_reserves_2015()
    )


@component.add(
    name="share RoE cumulative demand to extract vs resources materials",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_roe_from_2015": 1,
        "global_mineral_resources_2015": 1,
    },
)
def share_roe_cumulative_demand_to_extract_vs_resources_materials():
    """
    Yearly share of cumulative demand of the rest of the economy to be extracted in mines of materials vs. resources.
    """
    return zidz(
        cumulative_materials_to_extract_roe_from_2015(), global_mineral_resources_2015()
    )


@component.add(
    name="share tot cumulative dem vs reserves materials",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
        "global_mineral_reserves_2015": 1,
    },
)
def share_tot_cumulative_dem_vs_reserves_materials():
    """
    Yearly share of total cumulative demand of materials vs. reserves.
    """
    return zidz(
        total_cumulative_demand_materials_to_extract_from_2015(),
        global_mineral_reserves_2015(),
    )


@component.add(
    name="share tot cumulative dem vs resources materials",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_cumulative_demand_materials_to_extract_from_2015": 1,
        "global_mineral_resources_2015": 1,
    },
)
def share_tot_cumulative_dem_vs_resources_materials():
    """
    Yearly share of total cumulative demand of materials vs. resources.
    """
    return zidz(
        total_cumulative_demand_materials_to_extract_from_2015(),
        global_mineral_resources_2015(),
    )


@component.add(
    name="total cumulative demand materials to extract from 2015",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_materials_to_extract_bu_from_2015": 1,
        "cumulative_materials_to_extract_roe_from_2015": 1,
    },
)
def total_cumulative_demand_materials_to_extract_from_2015():
    """
    Total cumulative demand materials to extract in mines.
    """
    return (
        sum(
            cumulative_materials_to_extract_bu_from_2015().rename(
                {"REGIONS 9 I": "REGIONS 9 I!"}
            ),
            dim=["REGIONS 9 I!"],
        )
        + cumulative_materials_to_extract_roe_from_2015()
    )


@component.add(
    name="TOTAL FLOW MATERIALS EXTRACTED CUMULATIVE 2005 2015",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_total_flow_materials_extracted_cumulative_2005_2015"
    },
)
def total_flow_materials_extracted_cumulative_2005_2015():
    """
    Cumulative material extraction 2005-2015 in order to adjust the reserves and resources to the 2005 year.
    """
    return _ext_constant_total_flow_materials_extracted_cumulative_2005_2015()


_ext_constant_total_flow_materials_extracted_cumulative_2005_2015 = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "calibration_BU_vs_RoE",
    "TOTAL_FLOW_MATERIALS_EXTRACTED_CUMULATIVE_2005_2015*",
    {"MATERIALS I": _subscript_dict["MATERIALS I"]},
    _root,
    {"MATERIALS I": _subscript_dict["MATERIALS I"]},
    "_ext_constant_total_flow_materials_extracted_cumulative_2005_2015",
)


@component.add(
    name="total flow materials to extract",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_to_extract_roe": 1,
        "total_materials_to_extract_bu_techs": 1,
    },
)
def total_flow_materials_to_extract():
    """
    Total flow of materials to extract from mines over time, i.e., the addition of the demand estimated through top-down and bottom-up methods.
    """
    return materials_to_extract_roe() + sum(
        total_materials_to_extract_bu_techs().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="total global materials required BU techs",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_electric_transport_9r": 1,
        "materials_required_for_protra": 1,
        "materials_required_for_prosup": 1,
    },
)
def total_global_materials_required_bu_techs():
    """
    Total materials required estimated through the bottom-up (BU) method for specific technologies.
    """
    return (
        sum(
            materials_required_for_new_electric_transport_9r().rename(
                {"REGIONS 9 I": "REGIONS 9 I!"}
            ),
            dim=["REGIONS 9 I!"],
        )
        + sum(
            materials_required_for_protra().rename(
                {"REGIONS 9 I": "REGIONS 9 I!", "NRG PROTRA I": "NRG PROTRA I!"}
            ),
            dim=["REGIONS 9 I!", "NRG PROTRA I!"],
        )
        + sum(
            materials_required_for_prosup().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
    )


@component.add(
    name="Total materials required",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 1,
        "total_global_materials_required_bu_techs": 1,
    },
)
def total_materials_required():
    """
    Total demand of minerals, i.e., the addition of the demand estimated through top-down and bottom-up methods.
    """
    return (
        demand_projection_materials_roe() + total_global_materials_required_bu_techs()
    )


@component.add(
    name="total materials required BU techs",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_electric_transport_9r": 1,
        "materials_required_for_protra": 1,
        "materials_required_for_prosup": 1,
    },
)
def total_materials_required_bu_techs():
    """
    Total materials required estimated through the bottom-up (BU) method for specific technologies.
    """
    return (
        materials_required_for_new_electric_transport_9r()
        + sum(
            materials_required_for_protra().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        )
        + materials_required_for_prosup()
    )


@component.add(
    name="total materials to extract BU techs",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_extracted_for_prosup": 1,
        "materials_extracted_for_protra": 1,
        "total_materials_to_extract_for_electric_transport_9r": 1,
    },
)
def total_materials_to_extract_bu_techs():
    """
    Total materials to extract through bottom-up (BU) estimation for specific technologies.
    """
    return (
        materials_extracted_for_prosup()
        + sum(
            materials_extracted_for_protra().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        )
        + total_materials_to_extract_for_electric_transport_9r()
    )
