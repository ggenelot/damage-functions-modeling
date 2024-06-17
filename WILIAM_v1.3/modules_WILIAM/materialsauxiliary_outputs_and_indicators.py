"""
Module materialsauxiliary_outputs_and_indicators
Translated using PySD version 3.14.0
"""

@component.add(
    name="Al consumption per capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"al_market_sales": 1, "world_population": 1},
)
def al_consumption_per_capita():
    """
    Aluminium consumption in kg/person/year.
    """
    return zidz(al_market_sales(), world_population() / 10**9)


@component.add(
    name="Al reserves to production ratio",
    units="Year",
    subscripts=["Al ORE GRADES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_al_known_reserves": 1, "al_market_sales": 1},
)
def al_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Al supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Al reserves, and increases in annual consumption.
    """
    return zidz(
        total_al_known_reserves()
        .loc[_subscript_dict["Al ORE GRADES I"]]
        .rename({"ORE GRADES I": "Al ORE GRADES I"}),
        al_market_sales(),
    )


@component.add(
    name="coal consumption per capita",
    units="EJ/(Year*person)",
    subscripts=["COAL TYPES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_production_capacity_ej": 1, "world_population": 1},
)
def coal_consumption_per_capita():
    return zidz(total_coal_production_capacity_ej(), world_population())


@component.add(
    name="coal reserves to production ratio",
    units="Years",
    subscripts=["COAL TYPES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_reserves": 1, "total_coal_production_capacity_ej": 1},
)
def coal_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(total_coal_reserves(), total_coal_production_capacity_ej())


@component.add(
    name="Cu consumption per capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cu_market_sales": 1, "world_population": 1},
)
def cu_consumption_per_capita():
    """
    Copper consumption in kg/person/year.
    """
    return zidz(cu_market_sales(), world_population() / 10**9)


@component.add(
    name="Cu reserves to production ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_cu_known_reserves": 1, "cu_market_sales": 1},
)
def cu_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Cu supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Cu reserves, and increases in annual consumption.
    """
    return zidz(total_cu_known_reserves(), cu_market_sales())


@component.add(
    name="cumulated materials to extract for the PV cells",
    units="Mt",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_cells": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_cells": {
            "initial": {},
            "step": {"new_material_extract_for_the_pv_cells": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_cells():
    """
    cumulated material demand of the cells of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_cells()


_integ_cumulated_materials_to_extract_for_the_pv_cells = Integ(
    lambda: new_material_extract_for_the_pv_cells(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_cells",
)


@component.add(
    name="cumulated materials to extract for the PV inverters and transformers",
    units="Mt",
    subscripts=["REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers": {
            "initial": {},
            "step": {"new_material_extract_pv_inverters_and_transformers": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_inverters_and_transformers():
    """
    cumulated material demand of the inverters and transformers of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers()


_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers = Integ(
    lambda: new_material_extract_pv_inverters_and_transformers().expand_dims(
        {
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ]
        },
        2,
    ),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_inverters_and_transformers",
)


@component.add(
    name="cumulated materials to extract for the PV panel frames",
    units="Mt",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_panel_frames": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_panel_frames": {
            "initial": {},
            "step": {"new_material_extract_pv_panel_frames": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_panel_frames():
    """
    cumulated material demand of the panels structures of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_panel_frames()


_integ_cumulated_materials_to_extract_for_the_pv_panel_frames = Integ(
    lambda: new_material_extract_pv_panel_frames(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_panel_frames",
)


@component.add(
    name="cumulated materials to extract for the PV panels mounting structures",
    units="Mt",
    subscripts=[
        "REGIONS 9 I",
        "MATERIALS I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures": 1
    },
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures": {
            "initial": {},
            "step": {"new_material_extract_pv_panels_mounting_structures": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_panels_mounting_structures():
    """
    cumulated material demand of the mounting structures of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures()


_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures = Integ(
    lambda: new_material_extract_pv_panels_mounting_structures(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        [
            "REGIONS 9 I",
            "MATERIALS I",
            "PROTRA PP SOLAR PV I",
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
        ],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_panels_mounting_structures",
)


@component.add(
    name="cumulated materials to extract for the PV wiring",
    units="Mt",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulated_materials_to_extract_for_the_pv_wiring": 1},
    other_deps={
        "_integ_cumulated_materials_to_extract_for_the_pv_wiring": {
            "initial": {},
            "step": {"new_material_extract_pv_wiring": 1},
        }
    },
)
def cumulated_materials_to_extract_for_the_pv_wiring():
    """
    cumulated material demand of the wiring of photovoltaic systems
    """
    return _integ_cumulated_materials_to_extract_for_the_pv_wiring()


_integ_cumulated_materials_to_extract_for_the_pv_wiring = Integ(
    lambda: new_material_extract_pv_wiring(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    ),
    "_integ_cumulated_materials_to_extract_for_the_pv_wiring",
)


@component.add(
    name="Fe consumption per capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_market_sales": 1, "world_population": 1},
)
def fe_consumption_per_capita():
    """
    Iron consumption in kg/person/year.
    """
    return zidz(fe_market_sales(), world_population() / 10**9)


@component.add(
    name="Fe reserves to production ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_known_reserves": 1, "fe_market_sales": 1},
)
def fe_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Fe supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Fe reserves, and increases in annual consumption.
    """
    return zidz(total_fe_known_reserves(), fe_market_sales())


@component.add(
    name="gas consumtion per capita",
    units="EJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_gas_extraction": 1, "world_population": 1},
)
def gas_consumtion_per_capita():
    return zidz(current_gas_extraction(), world_population())


@component.add(
    name="gas reserves to production ratio",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gas_reserves": 1, "current_gas_extraction": 1},
)
def gas_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(gas_reserves(), current_gas_extraction())


@component.add(
    name="materials consumption per capita",
    units="Mt/(Year*person)",
    subscripts=["METALS W I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_consumption_per_capita": 1,
        "fe_consumption_per_capita": 1,
        "cu_consumption_per_capita": 1,
        "ni_consumption_per_capita": 1,
    },
)
def materials_consumption_per_capita():
    """
    mateials consumption in kg/person/year.
    """
    value = xr.DataArray(
        np.nan, {"METALS W I": _subscript_dict["METALS W I"]}, ["METALS W I"]
    )
    value.loc[["Al W"]] = al_consumption_per_capita()
    value.loc[["Fe W"]] = fe_consumption_per_capita()
    value.loc[["Cu W"]] = cu_consumption_per_capita()
    value.loc[["Ni W"]] = ni_consumption_per_capita()
    return value


@component.add(
    name="materials share of secondary material",
    units="DMNL",
    subscripts=["METALS W I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_share_of_secondary_material": 1,
        "cu_share_of_secondary_material": 1,
        "fe_share_of_secondary_material": 1,
        "ni_share_of_secondary_material": 1,
    },
)
def materials_share_of_secondary_material():
    """
    Share of secondary material used to produce new material to be sold on the market.
    """
    value = xr.DataArray(
        np.nan, {"METALS W I": _subscript_dict["METALS W I"]}, ["METALS W I"]
    )
    value.loc[["Al W"]] = al_share_of_secondary_material()
    value.loc[["Cu W"]] = cu_share_of_secondary_material()
    value.loc[["Fe W"]] = fe_share_of_secondary_material()
    value.loc[["Ni W"]] = ni_share_of_secondary_material()
    return value


@component.add(
    name="new material extract for the PV cells",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "share_new_pv_subtechn_land": 1,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_kg_mt": 1,
        "material_intensity_pv_cells": 2,
        "scrap_rate": 2,
        "unit_conversion_mw_tw": 1,
        "rc_rate_mineral": 2,
        "protra_capacity_expansion_selected": 2,
    },
)
def new_material_extract_for_the_pv_cells():
    """
    annual material demand of the cells of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_cells().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_cells().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="new material extract PV inverters and transformers",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "material_intensity_pv_transformer_land": 1,
        "scrap_rate": 2,
        "material_intensity_pv_inverter": 2,
        "rc_rate_mineral": 2,
        "protra_capacity_expansion_selected": 2,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def new_material_extract_pv_inverters_and_transformers():
    """
    annual material demand of the inverters and transformers of photovoltaic systems
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "MATERIALS I": _subscript_dict["MATERIALS I"],
                },
                ["REGIONS 9 I", "MATERIALS I"],
            ),
            lambda: protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * (
                material_intensity_pv_inverter()
                .loc[:, "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                + material_intensity_pv_transformer_land()
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_inverter()
            .loc[:, "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate()),
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="new material extract PV panel frames",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "share_new_pv_subtechn_land": 1,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_kg_mt": 1,
        "material_intensity_pv_panel_frame": 2,
        "unit_conversion_mw_tw": 1,
        "scrap_rate": 2,
        "rc_rate_mineral": 2,
        "protra_capacity_expansion_selected": 2,
    },
)
def new_material_extract_pv_panel_frames():
    """
    annual material demand of the panels structures of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_panel_frame().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * material_intensity_pv_panel_frame().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="new material extract PV panels mounting structures",
    units="Mt/Year",
    subscripts=[
        "REGIONS 9 I",
        "MATERIALS I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "share_new_pv_subtechn_land": 1,
        "unit_conversion_kg_mt": 1,
        "unit_conversion_mw_tw": 1,
        "scrap_rate": 1,
        "rc_rate_mineral": 1,
        "material_intensity_pv_panels_mounting_structures": 1,
        "protra_capacity_expansion_selected": 1,
    },
)
def new_material_extract_pv_panels_mounting_structures():
    """
    annual material demand of the mounting structures of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ],
                "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            [
                "REGIONS 9 I",
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
                "PROTRA PP SOLAR PV I",
                "MATERIALS I",
            ],
        ),
        lambda: share_new_pv_subtechn_land()
        * protra_capacity_expansion_selected()
        .loc[:, "TO elec", _subscript_dict["PROTRA PP SOLAR PV I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        * material_intensity_pv_panels_mounting_structures().transpose(
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
            "PROTRA PP SOLAR PV I",
            "MATERIALS I",
        )
        * (1 - rc_rate_mineral())
        * (1 + scrap_rate())
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    ).transpose(
        "REGIONS 9 I",
        "MATERIALS I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    )


@component.add(
    name="new material extract PV wiring",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "pv_wiring_urban_total_intensity": 1,
        "share_new_pv_subtechn_land": 1,
        "share_new_pv_subtechn_urban": 1,
        "unit_conversion_kg_mt": 1,
        "unit_conversion_mw_tw": 1,
        "scrap_rate": 2,
        "rc_rate_mineral": 2,
        "pv_wiring_land_total_intensity": 1,
        "protra_capacity_expansion_selected": 2,
    },
)
def new_material_extract_pv_wiring():
    """
    annual material demand of the wiring of photovoltaic systems
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"],
        ),
        lambda: (
            share_new_pv_subtechn_land()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * pv_wiring_land_total_intensity().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
            + share_new_pv_subtechn_urban()
            * protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * pv_wiring_urban_total_intensity().transpose(
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I", "MATERIALS I"
            )
            * (1 - rc_rate_mineral())
            * (1 + scrap_rate())
        )
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="Ni consumption per capita",
    units="Mt/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ni_market_sales": 1, "world_population": 1},
)
def ni_consumption_per_capita():
    """
    Nickel consumption in kg/person/year.
    """
    return zidz(ni_market_sales(), world_population() / 10**9)


@component.add(
    name="Ni reserves to production ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ni_known_reserves": 1, "ni_market_sales": 1},
)
def ni_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of Ni supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new Ni reserves, and increases in annual consumption.
    """
    return zidz(total_ni_known_reserves(), ni_market_sales())


@component.add(
    name="oil consumption per capita",
    units="bbl/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"current_oil_extraction": 1, "world_population": 1},
)
def oil_consumption_per_capita():
    return zidz(current_oil_extraction(), world_population())


@component.add(
    name="oil reserves to production ratio",
    units="Years",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_known_reserves": 1, "current_oil_extraction": 1},
)
def oil_reserves_to_production_ratio():
    """
    The Reserves-to-Production (R/P) Ratio measures the number of years of fuel supplies left based on current annual consumption rates. Note that this can change through time through the discovery of new fuel reserves, and increases in annual consumption.
    """
    return zidz(oil_known_reserves(), current_oil_extraction())


@component.add(
    name="OIL URR EJ",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_urr": 1, "unit_conversion_oil_bbl_per_ej": 1},
)
def oil_urr_ej():
    """
    initial availability of resources+reserves of Oil
    """
    return oil_urr() / unit_conversion_oil_bbl_per_ej()


@component.add(
    name="reference Ni",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"time": 1},
)
def reference_ni():
    return np.interp(
        time(),
        [
            2010.0,
            2011.0,
            2012.0,
            2013.0,
            2014.0,
            2015.0,
            2016.0,
            2017.0,
            2018.0,
            2019.0,
            2020.0,
            2021.0,
        ],
        [
            1.465,
            1.607,
            1.668,
            1.785,
            1.87,
            1.89,
            2.002,
            2.14,
            2.313,
            2.443,
            2.441,
            2.851,
        ],
    )


@component.add(
    name="reference Ni value",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "reference_ni": 1, "world_population": 1},
)
def reference_ni_value():
    return if_then_else(
        time() >= 2010, lambda: reference_ni() / (world_population() / 10**9), lambda: 0
    )


@component.add(
    name="relative RURR Al",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_al_urr": 2, "al_cumulative_mining": 1},
)
def relative_rurr_al():
    """
    Remaining resources+reserves of aluminium as a share of the initial availability
    """
    return (total_initial_al_urr() - al_cumulative_mining()) / total_initial_al_urr()


@component.add(
    name="relative RURR coal",
    units="1",
    subscripts=["COAL TYPES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_urr": 2, "cumulative_coal_extracted": 1},
)
def relative_rurr_coal():
    """
    Remaining resources+reserves of coal as a share of the initial availability.
    """
    return (coal_urr() - cumulative_coal_extracted()) / coal_urr()


@component.add(
    name="relative RURR Cu",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_cu_urr": 2, "cu_cumulative_mining": 1},
)
def relative_rurr_cu():
    """
    Remaining resources+reserves of copper as a share of the initial availability.
    """
    return (total_initial_cu_urr() - cu_cumulative_mining()) / total_initial_cu_urr()


@component.add(
    name="relative RURR Fe",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_fe_urr": 2, "fe_cumulative_mining": 1},
)
def relative_rurr_fe():
    """
    Remaining resources+reserves of iron as a share of the initial availability
    """
    return (total_initial_fe_urr() - fe_cumulative_mining()) / total_initial_fe_urr()


@component.add(
    name="relative RURR gas",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urr_natural_gas": 2, "cumulative_extracted_gas": 1},
)
def relative_rurr_gas():
    """
    Remaining resources of natural gas as a share of the initial availability.
    """
    return (urr_natural_gas() - cumulative_extracted_gas()) / urr_natural_gas()


@component.add(
    name="relative RURR materials",
    units="DMNL",
    subscripts=["HYDROCARBONS W I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "relative_rurr_total_coal": 1,
        "relative_rurr_oil": 1,
        "relative_rurr_gas": 1,
    },
)
def relative_rurr_materials():
    """
    Remaining resources+reserves of materials as a share of the initial availability.
    """
    value = xr.DataArray(
        np.nan,
        {"HYDROCARBONS W I": _subscript_dict["HYDROCARBONS W I"]},
        ["HYDROCARBONS W I"],
    )
    value.loc[["Coal W"]] = relative_rurr_total_coal()
    value.loc[["Oil W"]] = relative_rurr_oil()
    value.loc[["Gas W"]] = relative_rurr_gas()
    return value


@component.add(
    name="relative RURR Ni",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_initial_ni_urr": 2, "ni_cumulative_mining": 1},
)
def relative_rurr_ni():
    """
    Remaining resources+reserves of nickel as a share of the initial availability
    """
    return (total_initial_ni_urr() - ni_cumulative_mining()) / total_initial_ni_urr()


@component.add(
    name="relative RURR oil",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"oil_urr": 2, "cumulative_total_oil_extraction": 1},
)
def relative_rurr_oil():
    """
    Remaining resources+reserves of oil as a share of the initial availability.
    """
    return (oil_urr() - cumulative_total_oil_extraction()) / oil_urr()


@component.add(
    name="relative RURR total coal",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_coal_urr": 2, "total_cumulative_coal_extracted": 1},
)
def relative_rurr_total_coal():
    """
    Remaining resources+reserves of coal as a share of the initial availability.
    """
    return (total_coal_urr() - total_cumulative_coal_extracted()) / total_coal_urr()


@component.add(
    name="relative RURR uranium",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_urr_uranium": 2, "cumulated_uranium_extraction": 1},
)
def relative_rurr_uranium():
    """
    Remaining resources+reserves of coal as a share of the initial availability.
    """
    return (
        initial_urr_uranium() - cumulated_uranium_extraction()
    ) / initial_urr_uranium()


@component.add(
    name="TOTAL COAL URR",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"coal_urr": 1},
)
def total_coal_urr():
    """
    initial availability of resources+reserves of Coal (brown + hard coal)
    """
    return sum(
        coal_urr().rename({"COAL TYPES I": "COAL TYPES I!"}), dim=["COAL TYPES I!"]
    )


@component.add(
    name="total cumulative coal extracted",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_coal_extracted": 1},
)
def total_cumulative_coal_extracted():
    """
    total cumulative of coal extracted (brown + hard).
    """
    return sum(
        cumulative_coal_extracted().rename({"COAL TYPES I": "COAL TYPES I!"}),
        dim=["COAL TYPES I!"],
    )


@component.add(
    name="TOTAL INITIAL Al URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_al_hidden_resources": 1, "initial_al_known_reserves": 1},
)
def total_initial_al_urr():
    """
    initial availability of resources+reserves of aluminium
    """
    return sum(
        initial_al_hidden_resources().rename({"Al ORE GRADES I": "Al ORE GRADES I!"})
        + initial_al_known_reserves().rename({"Al ORE GRADES I": "Al ORE GRADES I!"}),
        dim=["Al ORE GRADES I!"],
    )


@component.add(
    name="TOTAL INITIAL Fe URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_fe_hidden_resources": 1, "initial_fe_known_reserves": 1},
)
def total_initial_fe_urr():
    """
    initial availability of resources+reserves of Iron
    """
    return sum(
        initial_fe_hidden_resources().rename({"ORE GRADES I": "ORE GRADES I!"})
        + initial_fe_known_reserves().rename({"ORE GRADES I": "ORE GRADES I!"}),
        dim=["ORE GRADES I!"],
    )


@component.add(
    name="TOTAL INITIAL Ni URR",
    units="Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_ni_hidden_resources": 1, "initial_ni_known_reserves": 1},
)
def total_initial_ni_urr():
    """
    initial availability of resources+reserves of Nickel
    """
    return sum(
        initial_ni_hidden_resources().rename({"ORE GRADES I": "ORE GRADES I!"})
        + initial_ni_known_reserves().rename({"ORE GRADES I": "ORE GRADES I!"}),
        dim=["ORE GRADES I!"],
    )


@component.add(
    name="uranium consumption per capita",
    units="EJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"uranium_extraction_rate": 1, "world_population": 1},
)
def uranium_consumption_per_capita():
    return zidz(uranium_extraction_rate(), world_population())


@component.add(
    name="uranium RURR to production ratio",
    units="Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"rurr_uranium": 1, "uranium_extraction_rate": 1},
)
def uranium_rurr_to_production_ratio():
    return zidz(rurr_uranium(), uranium_extraction_rate())
