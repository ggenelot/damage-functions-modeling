"""
Module materialsmaterials_requirements.rest_economy_med
Translated using PySD version 3.13.4
"""

@component.add(
    name="cumulative materials demand RoE from 2015",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_materials_demand_roe_from_2015": 1},
    other_deps={
        "_integ_cumulative_materials_demand_roe_from_2015": {
            "initial": {},
            "step": {"materials_demand_by_roe_from_2015": 1},
        }
    },
)
def cumulative_materials_demand_roe_from_2015():
    return _integ_cumulative_materials_demand_roe_from_2015()


_integ_cumulative_materials_demand_roe_from_2015 = Integ(
    lambda: materials_demand_by_roe_from_2015(),
    lambda: xr.DataArray(
        0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
    ),
    "_integ_cumulative_materials_demand_roe_from_2015",
)


@component.add(
    name="cumulative materials to extract RoE from 2015",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_materials_to_extract_roe_from_2015": 1},
    other_deps={
        "_integ_cumulative_materials_to_extract_roe_from_2015": {
            "initial": {},
            "step": {"materials_to_extract_roe_from_2015": 1},
        }
    },
)
def cumulative_materials_to_extract_roe_from_2015():
    """
    Cumulative materials to be mined for the rest of the economy from 2015.
    """
    return _integ_cumulative_materials_to_extract_roe_from_2015()


_integ_cumulative_materials_to_extract_roe_from_2015 = Integ(
    lambda: materials_to_extract_roe_from_2015(),
    lambda: xr.DataArray(
        0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
    ),
    "_integ_cumulative_materials_to_extract_roe_from_2015",
)


@component.add(
    name="cumulative materials to extract RoE from initial year",
    units="Mt",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_materials_to_extract_roe_from_initial_year": 1},
    other_deps={
        "_integ_cumulative_materials_to_extract_roe_from_initial_year": {
            "initial": {},
            "step": {"materials_to_extract_roe": 1},
        }
    },
)
def cumulative_materials_to_extract_roe_from_initial_year():
    """
    Cumulative materials to be mined for the rest of the economy.
    """
    return _integ_cumulative_materials_to_extract_roe_from_initial_year()


_integ_cumulative_materials_to_extract_roe_from_initial_year = Integ(
    lambda: materials_to_extract_roe(),
    lambda: xr.DataArray(
        0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
    ),
    "_integ_cumulative_materials_to_extract_roe_from_initial_year",
)


@component.add(
    name="demand projection materials RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_demand_projection_materials_roe": 1},
    other_deps={
        "_integ_demand_projection_materials_roe": {
            "initial": {
                "initial_mineral_consumption_roe": 1,
                "matrix_unit_prefixes": 1,
            },
            "step": {"variation_demand_materials_roe": 1},
        }
    },
)
def demand_projection_materials_roe():
    """
    Projection of the demand of minerals (total consumption = primary + recycled) by the rest of the economy.
    """
    return _integ_demand_projection_materials_roe()


_integ_demand_projection_materials_roe = Integ(
    lambda: variation_demand_materials_roe(),
    lambda: initial_mineral_consumption_roe()
    * float(matrix_unit_prefixes().loc["BASE UNIT", "mega"]),
    "_integ_demand_projection_materials_roe",
)


@component.add(
    name="HISTORICAL VARIATION MATERIALS CONSUMPTION RoE",
    units="tonnes/(Year*Year)",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "historical_consumption_materials_roe": 2, "one_year": 1},
)
def historical_variation_materials_consumption_roe():
    """
    Historical variation (yearly) in the consumption (primary + recycled) of minerals by the rest of the economy.
    """
    return (
        historical_consumption_materials_roe(time() + 1)
        - historical_consumption_materials_roe(time())
    ) / one_year()


@component.add(
    name="materials demand by RoE from 2015",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "demand_projection_materials_roe": 1},
)
def materials_demand_by_roe_from_2015():
    """
    Materials demand by the rest of the economy from 2015
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: demand_projection_materials_roe(),
    )


@component.add(
    name="materials extraction demand RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 1,
        "eol_recycling_rates_minerals_roe": 1,
    },
)
def materials_extraction_demand_roe():
    """
    Minerals extraction demand projection of the rest of the economy accounting for the dynamic evolution of recycling rates.
    """
    return demand_projection_materials_roe() * (1 - eol_recycling_rates_minerals_roe())


@component.add(
    name="materials to extract RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_extraction_demand_roe": 1},
)
def materials_to_extract_roe():
    """
    Annual materials to be mined for the rest of the economy.
    """
    return materials_extraction_demand_roe()


@component.add(
    name="materials to extract RoE from 2015",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_to_extract_roe": 1},
)
def materials_to_extract_roe_from_2015():
    """
    Annual materials to be mined for the ithe rest of the economy from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: materials_to_extract_roe(),
    )


@component.add(
    name="total recycled materials RoE",
    units="Mt/Year",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "demand_projection_materials_roe": 1,
        "materials_extraction_demand_roe": 1,
    },
)
def total_recycled_materials_roe():
    """
    Total recycled materials rest of the economy.
    """
    return demand_projection_materials_roe() - materials_extraction_demand_roe()


@component.add(
    name="variation demand materials RoE",
    units="Mtonnes/(Year*Year)",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_variation_materials_consumption_roe": 1,
        "annual_gdp_real_1r_growth": 1,
        "demand_projection_materials_roe": 1,
        "matrix_unit_prefixes": 2,
        "slope_demand_material_roe_per_gdp": 1,
    },
)
def variation_demand_materials_roe():
    """
    Variation of demand (primary + recycled) of minerals by the rest of the economy.
    """
    return if_then_else(
        time() < 2015,
        lambda: historical_variation_materials_consumption_roe(),
        lambda: if_then_else(
            demand_projection_materials_roe() > 0.01,
            lambda: slope_demand_material_roe_per_gdp()
            * (
                annual_gdp_real_1r_growth()
                * float(matrix_unit_prefixes().loc["BASE UNIT", "mega"])
            ),
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
        ),
    ) * float(matrix_unit_prefixes().loc["BASE UNIT", "mega"])
