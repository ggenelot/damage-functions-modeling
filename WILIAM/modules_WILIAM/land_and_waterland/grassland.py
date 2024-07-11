"""
Module land_and_waterland.grassland
Translated using PySD version 3.14.0
"""

@component.add(
    name="carbon capture due to change to regenerative grasslands",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_unsaturated_regenerative_management": 1,
        "land_use_area_by_region": 1,
        "factor_of_carbon_capture_of_grasslands": 1,
        "factor_of_carbon_capture_of_regenerative_grasslands": 1,
    },
)
def carbon_capture_due_to_change_to_regenerative_grasslands():
    """
    carbon capture in pastures soil due to improved agroecological managemet (hollistic management, Voisin's management) parameters not set
    """
    return (
        share_of_grasslands_under_unsaturated_regenerative_management()
        * land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True)
        * (
            factor_of_carbon_capture_of_regenerative_grasslands()
            - factor_of_carbon_capture_of_grasslands()
        )
        * 0
    )


@component.add(
    name="factor of grassland production",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "factor_of_gain_regenerative_grazing": 1,
        "share_of_grasslands_under_saturated_regenerative_management": 1,
        "share_of_grasslands_under_unsaturated_regenerative_management": 1,
    },
)
def factor_of_grassland_production():
    """
    Increase in grasslands production due to improved regenerative grazing
    """
    return 1 + factor_of_gain_regenerative_grazing() * (
        share_of_grasslands_under_unsaturated_regenerative_management()
        + share_of_grasslands_under_saturated_regenerative_management()
    )


@component.add(
    name="increase of share of mature regenerative grasslands",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_unsaturated_regenerative_management": 1,
        "saturation_time_of_regenerative_grasslands": 1,
    },
)
def increase_of_share_of_mature_regenerative_grasslands():
    return share_of_grasslands_under_unsaturated_regenerative_management() * (
        1 / saturation_time_of_regenerative_grasslands()
    )


@component.add(
    name="increase of share of regenerative grasslands",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_unsaturated_regenerative_management": 1,
        "share_of_grasslands_under_saturated_regenerative_management": 1,
        "soil_management_in_grasslands_sp": 1,
    },
)
def increase_of_share_of_regenerative_grasslands():
    """
    increment of share of pastures under regenetative grazing management
    """
    return if_then_else(
        share_of_grasslands_under_unsaturated_regenerative_management()
        + share_of_grasslands_under_saturated_regenerative_management()
        < 1,
        lambda: soil_management_in_grasslands_sp(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="share of grasslands under regenerative grasslands",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_grasslands_under_saturated_regenerative_management": 1,
        "share_of_grasslands_under_unsaturated_regenerative_management": 1,
    },
)
def share_of_grasslands_under_regenerative_grasslands():
    """
    share of all grassland (pastures) under regenerative managements, yields are assumed to increase (number of animals held per area)
    """
    return (
        share_of_grasslands_under_saturated_regenerative_management()
        + share_of_grasslands_under_unsaturated_regenerative_management()
    )


@component.add(
    name="share of grasslands under saturated regenerative management",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_share_of_grasslands_under_saturated_regenerative_management": 1
    },
    other_deps={
        "_integ_share_of_grasslands_under_saturated_regenerative_management": {
            "initial": {},
            "step": {"increase_of_share_of_mature_regenerative_grasslands": 1},
        }
    },
)
def share_of_grasslands_under_saturated_regenerative_management():
    """
    share of pastures under regenerative management where carbon capture stops because soil is saturated
    """
    return _integ_share_of_grasslands_under_saturated_regenerative_management()


_integ_share_of_grasslands_under_saturated_regenerative_management = Integ(
    lambda: increase_of_share_of_mature_regenerative_grasslands(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_share_of_grasslands_under_saturated_regenerative_management",
)


@component.add(
    name="share of grasslands under unsaturated regenerative management",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_share_of_grasslands_under_unsaturated_regenerative_management": 1
    },
    other_deps={
        "_integ_share_of_grasslands_under_unsaturated_regenerative_management": {
            "initial": {},
            "step": {
                "increase_of_share_of_regenerative_grasslands": 1,
                "increase_of_share_of_mature_regenerative_grasslands": 1,
            },
        }
    },
)
def share_of_grasslands_under_unsaturated_regenerative_management():
    """
    share of pasture area that has started the use of advanced regenerative methods and is already capturing carbon and soil is not saturated
    """
    return _integ_share_of_grasslands_under_unsaturated_regenerative_management()


_integ_share_of_grasslands_under_unsaturated_regenerative_management = Integ(
    lambda: increase_of_share_of_regenerative_grasslands()
    - increase_of_share_of_mature_regenerative_grasslands(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_share_of_grasslands_under_unsaturated_regenerative_management",
)


@component.add(
    name="soil management in grasslands sp",
    units="1/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_soil_management_in_grasslands_sp": 1,
        "year_initial_soil_management_in_grasslands_sp": 2,
        "time": 2,
        "year_final_soil_management_in_grasslands_sp": 2,
        "objective_soil_management_in_grasslands_sp": 1,
    },
)
def soil_management_in_grasslands_sp():
    """
    Policy to simulate the change of pastures management to advanced agroecological methods (hollistic management, Voisin's management) that stimulate the carbon capture in soils
    """
    return if_then_else(
        np.logical_and(
            switch_soil_management_in_grasslands_sp() == 1,
            np.logical_and(
                time() > year_initial_soil_management_in_grasslands_sp(),
                time() < year_final_soil_management_in_grasslands_sp(),
            ),
        ),
        lambda: objective_soil_management_in_grasslands_sp()
        / (
            year_final_soil_management_in_grasslands_sp()
            - year_initial_soil_management_in_grasslands_sp()
        ),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )
