"""
Module land_and_waterurban_land
Translated using PySD version 3.14.0
"""

@component.add(
    name="change of urban land dispersion",
    units="m2/people/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "time_historical_data_land_module": 1,
        "change_of_urban_land_dispersion_trends": 2,
        "switch_urban_land_density_sp": 1,
        "urban_land_dispersion_trends": 1,
        "objective_urban_land_density_sp": 1,
        "year_initial_urban_land_density_sp": 2,
        "year_final_urban_land_density_sp": 2,
    },
)
def change_of_urban_land_dispersion():
    """
    Evolution of the urban land density by trends
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: change_of_urban_land_dispersion_trends(),
        lambda: if_then_else(
            np.logical_and(
                switch_urban_land_density_sp() == 1,
                np.logical_and(
                    time() > year_initial_urban_land_density_sp(),
                    time() < year_final_urban_land_density_sp(),
                ),
            ),
            lambda: (objective_urban_land_density_sp() - urban_land_dispersion_trends())
            / (
                year_final_urban_land_density_sp()
                - year_initial_urban_land_density_sp()
            ),
            lambda: change_of_urban_land_dispersion_trends(),
        ),
    )


@component.add(
    name="change of urban land dispersion trends",
    units="m2/people",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urban_land_dispersion_trends": 1, "delayed_urban_land_dispersion": 1},
)
def change_of_urban_land_dispersion_trends():
    """
    historical_change_of_urban_land_density
    """
    return urban_land_dispersion_trends() - delayed_urban_land_dispersion()


@component.add(
    name="delayed urban land dispersion",
    units="m2/people",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_urban_land_dispersion": 1},
    other_deps={
        "_delayfixed_delayed_urban_land_dispersion": {
            "initial": {"initial_urban_land_dispersion": 1},
            "step": {"urban_land_dispersion_trends": 1},
        }
    },
)
def delayed_urban_land_dispersion():
    """
    delayed_urban_land_density
    """
    return _delayfixed_delayed_urban_land_dispersion()


_delayfixed_delayed_urban_land_dispersion = DelayFixed(
    lambda: urban_land_dispersion_trends(),
    lambda: 1,
    lambda: initial_urban_land_dispersion(),
    time_step,
    "_delayfixed_delayed_urban_land_dispersion",
)


@component.add(
    name="historical data of population with time",
    units="people",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "exogenous_population_9r": 1,
        "time": 1,
        "population_9_regions": 1,
    },
)
def historical_data_of_population_with_time():
    """
    Population. If the module is disconnected (SWITCH_LANDWATER=0) historical data is taken.
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: exogenous_population_9r(time()),
        lambda: population_9_regions(),
    )


@component.add(
    name="historical data of urban land with time",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_land_use_by_region": 1},
)
def historical_data_of_urban_land_with_time():
    """
    Urban land historical data with variation (LOOKUPS)
    """
    return (
        historical_land_use_by_region(time())
        .loc[:, "URBAN LAND"]
        .reset_coords(drop=True)
    )


@component.add(
    name="initial urban land dispersion",
    units="m2/(Year*people)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "historical_land_use_by_region": 2,
        "exogenous_population_9r": 1,
        "unit_conversion_m2_km2": 2,
        "initial_time": 3,
        "population_9_regions": 1,
    },
)
def initial_urban_land_dispersion():
    """
    initial_urban_land_density
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: zidz(
            unit_conversion_m2_km2()
            * historical_land_use_by_region(initial_time())
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
            exogenous_population_9r(initial_time()),
        ),
        lambda: zidz(
            unit_conversion_m2_km2()
            * historical_land_use_by_region(initial_time())
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
            population_9_regions(),
        ),
    )


@component.add(
    name="urban land dispersion ratio",
    units="m2/people",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_urban_land_dispersion_ratio": 1},
    other_deps={
        "_integ_urban_land_dispersion_ratio": {
            "initial": {"initial_urban_land_dispersion": 1},
            "step": {"change_of_urban_land_dispersion": 1},
        }
    },
)
def urban_land_dispersion_ratio():
    """
    the urban land ocupation ratio by region, in terms of area per person
    """
    return _integ_urban_land_dispersion_ratio()


_integ_urban_land_dispersion_ratio = Integ(
    lambda: change_of_urban_land_dispersion(),
    lambda: initial_urban_land_dispersion(),
    "_integ_urban_land_dispersion_ratio",
)


@component.add(
    name="urban land dispersion trends",
    units="m2/people",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_data_of_urban_land_with_time": 1,
        "unit_conversion_m2_km2": 1,
        "historical_data_of_population_with_time": 1,
    },
)
def urban_land_dispersion_trends():
    """
    Urban land historical ocupation, in terms of area per person
    """
    return (
        historical_data_of_urban_land_with_time() * unit_conversion_m2_km2()
    ) / historical_data_of_population_with_time()
