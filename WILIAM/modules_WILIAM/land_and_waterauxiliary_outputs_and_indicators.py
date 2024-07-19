"""
Module land_and_waterauxiliary_outputs_and_indicators
Translated using PySD version 3.13.4
"""

@component.add(
    name="accumulated sea level rise loss",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accumulated_sea_level_rise_loss": 1},
    other_deps={
        "_integ_accumulated_sea_level_rise_loss": {
            "initial": {},
            "step": {"increment_sea_level_rise_loss": 1},
        }
    },
)
def accumulated_sea_level_rise_loss():
    return _integ_accumulated_sea_level_rise_loss()


_integ_accumulated_sea_level_rise_loss = Integ(
    lambda: increment_sea_level_rise_loss(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_accumulated_sea_level_rise_loss",
)


@component.add(
    name="check summ all lands",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_productive_uses": 1,
        "accumulated_sea_level_rise_loss": 1,
        "historical_land_use_by_region": 2,
        "initial_time": 2,
    },
)
def check_summ_all_lands():
    return zidz(
        sum(
            land_use_area_productive_uses().rename({"LANDS I": "LANDS I!"}),
            dim=["LANDS I!"],
        )
        - accumulated_sea_level_rise_loss()
        - sum(
            historical_land_use_by_region(initial_time()).rename(
                {"LANDS I": "LANDS I!"}
            ),
            dim=["LANDS I!"],
        ),
        sum(
            historical_land_use_by_region(initial_time()).rename(
                {"LANDS I": "LANDS I!"}
            ),
            dim=["LANDS I!"],
        ),
    )


@component.add(
    name="demand for food",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food_before_losses": 1},
)
def demand_for_food():
    """
    Calculation of total demanded for food.
    """
    return sum(
        land_products_demanded_for_food_before_losses().rename(
            {"REGIONS 9 I": "REGIONS 9 I!", "LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["REGIONS 9 I!", "LAND PRODUCTS I!"],
    )


@component.add(
    name="increment sea level rise loss",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "cropland_loss_due_to_sea_level_rise_by_region": 1,
    },
)
def increment_sea_level_rise_loss():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: cropland_loss_due_to_sea_level_rise_by_region(),
    )


@component.add(
    name="land use area 1R",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1},
)
def land_use_area_1r():
    """
    Total land use area.
    """
    return sum(
        land_use_area_by_region().rename(
            {"REGIONS 9 I": "REGIONS 9 I!", "LANDS I": "LANDS I!"}
        ),
        dim=["REGIONS 9 I!", "LANDS I!"],
    )


@component.add(
    name="water stress 1R",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"water_stress_by_region": 2},
)
def water_stress_1r():
    """
    Total water strees.
    """
    return zidz(
        zidz(
            sum(
                water_stress_by_region()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
            27,
        )
        + zidz(
            sum(
                water_stress_by_region()
                .loc[_subscript_dict["REGIONS 8 I"]]
                .rename({"REGIONS 35 I": "REGIONS 8 I!"}),
                dim=["REGIONS 8 I!"],
            ),
            8,
        ),
        2,
    )
