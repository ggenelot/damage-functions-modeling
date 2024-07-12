"""
Module materialsflow_analysis_medeas
Translated using PySD version 3.13.4
"""

@component.add(
    name="check RC RR",
    units="DMNL",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_rc_rr_minerals": 1, "rc_rate_mineral": 1},
)
def check_rc_rr():
    """
    comparison of the RC ratio of endogenous recycling and that set out by UNEP (2011)
    """
    return (
        -1
        + zidz(
            current_rc_rr_minerals().expand_dims(
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 1
            ),
            rc_rate_mineral().transpose("MATERIALS I", "REGIONS 9 I"),
        )
    ).transpose("REGIONS 9 I", "MATERIALS I")


@component.add(
    name="decrease remaining mineral reserves",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_bu_techs": 1, "mineral_mined_roe": 1},
)
def decrease_remaining_mineral_reserves():
    """
    decrease in mineral reserves due to mining
    """
    return mineral_mined_bu_techs() + mineral_mined_roe()


@component.add(
    name="decrease remaining mineral resources",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_bu_techs": 1, "mineral_mined_roe": 1},
)
def decrease_remaining_mineral_resources():
    """
    decrease in mineral resources due to mining
    """
    return mineral_mined_bu_techs() + mineral_mined_roe()


@component.add(
    name="increase remaining mineral reserves",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 2,
        "one_year": 2,
        "mineral_recycled_roe": 2,
        "mineral_mined_roe": 1,
        "over_recycling_bu_techs": 1,
        "total_global_materials_required_bu_techs": 2,
        "mineral_recycled_bu_techs": 2,
        "over_recycling_roe": 1,
        "mineral_mined_bu_techs": 1,
    },
)
def increase_remaining_mineral_reserves():
    """
    increase in mineral reserves due to recycling
    """
    return if_then_else(
        demand_projection_materials_roe() / one_year() - mineral_recycled_roe() > 0,
        lambda: if_then_else(
            total_global_materials_required_bu_techs() - mineral_recycled_bu_techs()
            > 0,
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
            lambda: mineral_mined_roe()
            + mineral_recycled_roe()
            + over_recycling_bu_techs()
            - demand_projection_materials_roe() / one_year(),
        ),
        lambda: mineral_mined_bu_techs()
        + mineral_recycled_bu_techs()
        + over_recycling_roe()
        - total_global_materials_required_bu_techs(),
    )


@component.add(
    name="increase remaining mineral resources",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_recycled_bu_techs": 2,
        "mineral_mined_bu_techs": 2,
        "mineral_recycled_roe": 2,
        "mineral_mined_roe": 2,
    },
)
def increase_remaining_mineral_resources():
    """
    increase in mineral resources due to recycling
    """
    return if_then_else(
        mineral_recycled_bu_techs() > mineral_mined_bu_techs(),
        lambda: mineral_recycled_bu_techs() - mineral_mined_bu_techs(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    ) + if_then_else(
        mineral_recycled_roe() > mineral_mined_roe(),
        lambda: mineral_recycled_roe() - mineral_mined_roe(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="indicator of mineral scarcity",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_minerals_reserves": 1,
        "remaining_mineral_resources": 2,
        "mineral_recycled_bu_techs": 2,
        "global_mineral_resources_2015": 2,
        "mineral_recycled_roe": 2,
        "global_mineral_reserves_2015": 2,
    },
)
def indicator_of_mineral_scarcity():
    """
    Indicator of mineral scarcity;factor that varies its value from 0 ('not scarce') to 1 ('very scarce') depending on the remaining resources and reserves of each mineral and the amount of each mineral recycled.
    """
    return if_then_else(
        remaining_minerals_reserves() > 0,
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: if_then_else(
            remaining_mineral_resources() > 0,
            lambda: zidz(
                global_mineral_resources_2015()
                - remaining_mineral_resources()
                - global_mineral_reserves_2015(),
                (
                    global_mineral_resources_2015()
                    + mineral_recycled_bu_techs()
                    + mineral_recycled_roe()
                )
                - (
                    global_mineral_reserves_2015()
                    + mineral_recycled_bu_techs()
                    + mineral_recycled_roe()
                ),
            ),
            lambda: xr.DataArray(
                1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
        ),
    )


@component.add(
    name="mineral end of use BU techs",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_of_decom_batteries_9r": 1,
        "material_intensity_weighted_average_new_pv": 1,
        "unit_conversion_mw_tw": 1,
        "protra_capacity_decommissioning_selected": 4,
        "material_intensity_new_capacity_wind_offshore": 1,
        "unit_conversion_kg_mt": 1,
        "material_intensity_new_capacity_wind_onshore": 1,
        "material_intensity_new_capacity_csp": 1,
    },
)
def mineral_end_of_use_bu_techs():
    """
    Mineral of the botto-up (BU) technologies dispositives end of use
    """
    return (
        mineral_of_decom_batteries_9r()
        + (
            sum(
                protra_capacity_decommissioning_selected()
                .loc[:, :, "PROTRA PP solar CSP"]
                .reset_coords(drop=True)
                .rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            )
            * material_intensity_new_capacity_csp()
            + sum(
                protra_capacity_decommissioning_selected()
                .loc[:, :, "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                .rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            )
            * material_intensity_weighted_average_new_pv()
            .loc[:, :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            + sum(
                protra_capacity_decommissioning_selected()
                .loc[:, :, "PROTRA PP wind offshore"]
                .reset_coords(drop=True)
                .rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            )
            * material_intensity_new_capacity_wind_offshore()
            + sum(
                protra_capacity_decommissioning_selected()
                .loc[:, :, "PROTRA PP wind onshore"]
                .reset_coords(drop=True)
                .rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            )
            * material_intensity_new_capacity_wind_onshore()
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="mineral end of use RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"stock_mineral_roe": 1, "average_residence_time_mineral_in_roe": 1},
)
def mineral_end_of_use_roe():
    """
    decom materials of the Rest of the economy
    """
    return stock_mineral_roe() / average_residence_time_mineral_in_roe()


@component.add(
    name="mineral mined BU techs",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_global_materials_required_bu_techs": 2,
        "mineral_recycled_bu_techs": 2,
        "over_recycling_bu_techs": 2,
        "over_recycling_roe": 2,
    },
)
def mineral_mined_bu_techs():
    """
    mineral mined demand of the BU technologies
    """
    return if_then_else(
        total_global_materials_required_bu_techs()
        - mineral_recycled_bu_techs()
        - over_recycling_bu_techs()
        - over_recycling_roe()
        > 0,
        lambda: total_global_materials_required_bu_techs()
        - mineral_recycled_bu_techs()
        - over_recycling_bu_techs()
        - over_recycling_roe(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="mineral mined RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 2,
        "one_year": 2,
        "mineral_recycled_roe": 2,
        "over_recycling_roe": 2,
        "over_recycling_bu_techs": 2,
    },
)
def mineral_mined_roe():
    """
    mineral mined for the mineral demand of the Rest of the economy
    """
    return if_then_else(
        demand_projection_materials_roe() / one_year()
        - mineral_recycled_roe()
        - over_recycling_roe()
        - over_recycling_bu_techs()
        > 0,
        lambda: demand_projection_materials_roe() / one_year()
        - mineral_recycled_roe()
        - over_recycling_roe()
        - over_recycling_bu_techs(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="mineral recycled BU techs",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_end_of_use_bu_techs": 1,
        "eol_recycling_rates_minerals_bu_techs": 1,
    },
)
def mineral_recycled_bu_techs():
    """
    mineral from decommissioned technologies calculated botto-up that can be recycled
    """
    return (
        sum(
            mineral_end_of_use_bu_techs().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        * eol_recycling_rates_minerals_bu_techs()
    )


@component.add(
    name="mineral recycled RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_end_of_use_roe": 1, "eol_recycling_rates_minerals_roe": 1},
)
def mineral_recycled_roe():
    """
    mineral recycled of the Rest of the economy
    """
    return mineral_end_of_use_roe() * eol_recycling_rates_minerals_roe()


@component.add(
    name="mineral supply BU techs",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_mined_bu_techs": 2,
        "mineral_recycled_bu_techs": 2,
        "over_recycling_roe": 2,
        "total_global_materials_required_bu_techs": 2,
    },
)
def mineral_supply_bu_techs():
    """
    total supply of minerals for BU technologies
    """
    return if_then_else(
        mineral_mined_bu_techs() + mineral_recycled_bu_techs() + over_recycling_roe()
        > total_global_materials_required_bu_techs(),
        lambda: total_global_materials_required_bu_techs(),
        lambda: mineral_mined_bu_techs()
        + mineral_recycled_bu_techs()
        + over_recycling_roe(),
    )


@component.add(
    name="mineral supply RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_mined_roe": 2,
        "mineral_recycled_roe": 2,
        "over_recycling_bu_techs": 2,
        "one_year": 2,
        "demand_projection_materials_roe": 2,
    },
)
def mineral_supply_roe():
    """
    mineral supply for the Rest of the economy
    """
    return if_then_else(
        mineral_mined_roe() + mineral_recycled_roe() + over_recycling_bu_techs()
        > demand_projection_materials_roe() / one_year(),
        lambda: demand_projection_materials_roe() / one_year(),
        lambda: mineral_mined_roe()
        + mineral_recycled_roe()
        + over_recycling_bu_techs(),
    )


@component.add(
    name="over recycling BU techs",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_recycled_bu_techs": 2,
        "total_global_materials_required_bu_techs": 2,
    },
)
def over_recycling_bu_techs():
    """
    Mt of minerals used in BU technologies for which the amount recycled is greater than the amount demanded by the alternative technologies.
    """
    return if_then_else(
        mineral_recycled_bu_techs() > total_global_materials_required_bu_techs(),
        lambda: mineral_recycled_bu_techs()
        - total_global_materials_required_bu_techs(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="over recycling RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mineral_recycled_roe": 2,
        "one_year": 2,
        "demand_projection_materials_roe": 2,
    },
)
def over_recycling_roe():
    """
    Mt of minerals used in the rest of economy for which the amount recycled is greater than the amount demanded by the rest of the economy.
    """
    return if_then_else(
        mineral_recycled_roe() > demand_projection_materials_roe() / one_year(),
        lambda: mineral_recycled_roe() - demand_projection_materials_roe() / one_year(),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="RC rate mineral",
    units="DMNL",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_recycled_mineral": 2, "total_demand_mineral": 2},
)
def rc_rate_mineral():
    """
    Recycled content rate of the all materials
    """
    return if_then_else(
        zidz(total_recycled_mineral(), total_demand_mineral()) > 1,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 9 I", "MATERIALS I"],
        ),
        lambda: zidz(total_recycled_mineral(), total_demand_mineral()),
    )


@component.add(
    name="remaining mineral resources",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_remaining_mineral_resources": 1},
    other_deps={
        "_integ_remaining_mineral_resources": {
            "initial": {
                "global_mineral_resources_2015": 1,
                "total_flow_materials_extracted_cumulative_2005_2015": 1,
            },
            "step": {
                "increase_remaining_mineral_resources": 1,
                "decrease_remaining_mineral_resources": 1,
            },
        }
    },
)
def remaining_mineral_resources():
    """
    Remaining mineral resources at each point in the simulation
    """
    return _integ_remaining_mineral_resources()


_integ_remaining_mineral_resources = Integ(
    lambda: increase_remaining_mineral_resources()
    - decrease_remaining_mineral_resources(),
    lambda: global_mineral_resources_2015()
    + total_flow_materials_extracted_cumulative_2005_2015(),
    "_integ_remaining_mineral_resources",
)


@component.add(
    name="remaining minerals reserves",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_remaining_minerals_reserves": 1},
    other_deps={
        "_integ_remaining_minerals_reserves": {
            "initial": {
                "global_mineral_reserves_2015": 1,
                "total_flow_materials_extracted_cumulative_2005_2015": 1,
            },
            "step": {
                "increase_remaining_mineral_reserves": 1,
                "decrease_remaining_mineral_reserves": 1,
            },
        }
    },
)
def remaining_minerals_reserves():
    """
    Remaining mineral reserves at each point in the simulation
    """
    return _integ_remaining_minerals_reserves()


_integ_remaining_minerals_reserves = Integ(
    lambda: increase_remaining_mineral_reserves()
    - decrease_remaining_mineral_reserves(),
    lambda: global_mineral_reserves_2015()
    + total_flow_materials_extracted_cumulative_2005_2015(),
    "_integ_remaining_minerals_reserves",
)


@component.add(
    name="stock mineral RoE",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stock_mineral_roe": 1},
    other_deps={
        "_integ_stock_mineral_roe": {
            "initial": {"initial_stock_mineral_roe": 1},
            "step": {"mineral_supply_roe": 1, "mineral_end_of_use_roe": 1},
        }
    },
)
def stock_mineral_roe():
    """
    stock of minerals in the Rest of the economy
    """
    return _integ_stock_mineral_roe()


_integ_stock_mineral_roe = Integ(
    lambda: mineral_supply_roe() - mineral_end_of_use_roe(),
    lambda: initial_stock_mineral_roe(),
    "_integ_stock_mineral_roe",
)


@component.add(
    name="total demand mineral",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_global_materials_required_bu_techs": 1,
        "one_year": 1,
        "demand_projection_materials_roe": 1,
    },
)
def total_demand_mineral():
    """
    Total demand of mineral
    """
    return (
        total_global_materials_required_bu_techs()
        + demand_projection_materials_roe() / one_year()
    ).expand_dims({"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0)


@component.add(
    name="total mineral mined",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_mined_bu_techs": 1, "mineral_mined_roe": 1},
)
def total_mineral_mined():
    """
    Total mineral mined (AT+RE)
    """
    return mineral_mined_bu_techs() + mineral_mined_roe()


@component.add(
    name="total mineral supply",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_supply_bu_techs": 1, "mineral_supply_roe": 1},
)
def total_mineral_supply():
    """
    Total mineral supply (AT+RE)
    """
    return (mineral_supply_bu_techs() + mineral_supply_roe()).expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="total recycled mineral",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mineral_recycled_bu_techs": 1, "mineral_recycled_roe": 1},
)
def total_recycled_mineral():
    """
    total recycled mineral
    """
    return (mineral_recycled_bu_techs() + mineral_recycled_roe()).expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )
