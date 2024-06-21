"""
Module land_and_waterland.land_demands
Translated using PySD version 3.14.0
"""

@component.add(
    name="accumulated error in solar land",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_accumulated_error_in_solar_land": 1},
    other_deps={
        "_integ_accumulated_error_in_solar_land": {
            "initial": {},
            "step": {"difference_solar_land": 1},
        }
    },
)
def accumulated_error_in_solar_land():
    """
    This variable is used to adjust solar land to the desired value via a proportional and integral feedback loop, the accumulated error enables integral feedback control
    """
    return _integ_accumulated_error_in_solar_land()


_integ_accumulated_error_in_solar_land = Integ(
    lambda: difference_solar_land(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_accumulated_error_in_solar_land",
)


@component.add(
    name="afforestation due to policies",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_afforestation_sp": 1,
        "time": 2,
        "year_initial_afforestation_sp": 2,
        "year_final_afforestation_sp": 2,
        "objective_afforestation_sp": 1,
        "initial_land_use_by_region": 1,
    },
)
def afforestation_due_to_policies():
    """
    Land demanded for afforestation due to policies
    """
    return if_then_else(
        np.logical_and(
            switch_afforestation_sp() == 1,
            np.logical_and(
                time() > year_initial_afforestation_sp(),
                time() < year_final_afforestation_sp(),
            ),
        ),
        lambda: (
            objective_afforestation_sp()
            * initial_land_use_by_region()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True)
        )
        / (year_final_afforestation_sp() - year_initial_afforestation_sp()),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="auxcheckshares",
    subscripts=["REGIONS 9 I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_land_use_change_from_others": 1},
)
def auxcheckshares():
    return sum(
        share_of_land_use_change_from_others().rename({"LANDS I": "LANDS I!"}),
        dim=["LANDS I!"],
    )


@component.add(
    name="changes of share of solar land",
    units="1/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "year_initial_solar_land_from_others_sp": 2,
        "year_final_solar_land_from_others_sp": 2,
        "objective_solar_land_from_others_sp": 1,
        "initial_share_of_land_use_changes_from_others_up": 1,
    },
)
def changes_of_share_of_solar_land():
    """
    Evolution of the shares of solar land from other uses
    """
    return if_then_else(
        np.logical_and(
            time() > year_initial_solar_land_from_others_sp(),
            time() < year_final_solar_land_from_others_sp(),
        ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
        lambda: zidz(
            objective_solar_land_from_others_sp()
            - initial_share_of_land_use_changes_from_others_up()
            .loc[:, :, "SOLAR LAND"]
            .reset_coords(drop=True),
            (
                year_final_solar_land_from_others_sp()
                - year_initial_solar_land_from_others_sp()
            ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
            },
            ["REGIONS 9 I", "LANDS I"],
        ),
    )


@component.add(
    name="difference solar land",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "land_for_solar_demanded": 1,
        "land_use_area_by_region": 1,
    },
)
def difference_solar_land():
    """
    Diference between desired solar land and present solar land in each time t
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: land_for_solar_demanded()
        - land_use_area_by_region().loc[:, "SOLAR LAND"].reset_coords(drop=True),
    )


@component.add(
    name="exo population variation exogenous",
    units="people/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 9,
        "deaths": 9,
        "births": 9,
        "time": 9,
        "imv_exogenous_population_variation": 9,
    },
)
def exo_population_variation_exogenous():
    """
    exogenous variation of population by region (9 regions), to be used when Land and water module is disconected from the rest of the model SWITCH LANDWATER=0
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc[_subscript_dict["REGIONS EU27 I"], :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!", "SEX I": "SEX I!"}),
            dim=["REGIONS EU27 I!", "SEX I!"],
        )
        - sum(
            deaths()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename(
                {
                    "REGIONS 35 I": "REGIONS EU27 I!",
                    "SEX I": "SEX I!",
                    "AGE COHORTS I": "AGE COHORTS I!",
                }
            ),
            dim=["REGIONS EU27 I!", "SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["EU27"]),
    )
    value.loc[["UK"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["UK", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["UK", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["UK"]),
    )
    value.loc[["CHINA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["CHINA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["CHINA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["CHINA"]),
    )
    value.loc[["EASOC"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["EASOC", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["EASOC", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["EASOC"]),
    )
    value.loc[["INDIA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["INDIA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["INDIA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["INDIA"]),
    )
    value.loc[["LATAM"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["LATAM", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["LATAM", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["LATAM"]),
    )
    value.loc[["RUSSIA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["RUSSIA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["RUSSIA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["RUSSIA"]),
    )
    value.loc[["USMCA"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["USMCA", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["USMCA", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["USMCA"]),
    )
    value.loc[["LROW"]] = if_then_else(
        switch_landwater() == 1,
        lambda: sum(
            births()
            .loc["LROW", :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        - sum(
            deaths()
            .loc["LROW", :, :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
            dim=["SEX I!", "AGE COHORTS I!"],
        ),
        lambda: float(imv_exogenous_population_variation(time()).loc["LROW"]),
    )
    return value


@component.add(
    name="forest plantations growth due to policies",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_forest_plantations_sp": 1,
        "time": 2,
        "year_initial_forest_plantations_sp": 2,
        "year_final_forest_plantations_sp": 2,
        "initial_land_use_by_region": 1,
        "objective_forest_plantations_sp": 1,
    },
)
def forest_plantations_growth_due_to_policies():
    """
    Growth of forest plantations driven by policies, it is added to the trends.
    """
    return if_then_else(
        np.logical_and(
            switch_forest_plantations_sp() == 1,
            np.logical_and(
                time() > year_initial_forest_plantations_sp(),
                time() < year_final_forest_plantations_sp(),
            ),
        ),
        lambda: (
            objective_forest_plantations_sp()
            * initial_land_use_by_region()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
        )
        / (year_final_forest_plantations_sp() - year_initial_forest_plantations_sp()),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="increment of cropland and solar demanded",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "gap_global_availability_of_crops": 2,
        "priorities_of_land_use_change_sp": 2,
        "initial_land_use_by_region": 2,
        "control_parameter_of_land_use_changes": 2,
        "accumulated_error_in_solar_land": 1,
        "difference_solar_land": 1,
        "ki_solar_feedback": 1,
        "kp_solar_feedback": 1,
    },
)
def increment_of_cropland_and_solar_demanded():
    """
    Land demanded for solar and cropland driven by shortage signals. It is added latter to the one driven by trends
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = (
        (
            -gap_global_availability_of_crops()
            * (
                1
                + priorities_of_land_use_change_sp()
                .loc[:, "CROPLAND RAINFED"]
                .reset_coords(drop=True)
            )
            * initial_land_use_by_region()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True)
            * float(control_parameter_of_land_use_changes().loc["CROPLAND RAINFED"])
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        (
            0
            * (
                -gap_global_availability_of_crops()
                * priorities_of_land_use_change_sp()
                .loc[:, "CROPLAND IRRIGATED"]
                .reset_coords(drop=True)
                * initial_land_use_by_region()
                .loc[:, "CROPLAND IRRIGATED"]
                .reset_coords(drop=True)
                * float(
                    control_parameter_of_land_use_changes().loc["CROPLAND IRRIGATED"]
                )
            )
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = 0
    value.loc[:, ["FOREST PRIMARY"]] = 0
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = (
        (
            (
                difference_solar_land()
                + accumulated_error_in_solar_land() * ki_solar_feedback()
            )
            * kp_solar_feedback()
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    return value


@component.add(
    name="increment of cropland and solar limited",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_land_use_by_region": 1,
        "maximum_annual_land_use_change": 1,
        "increment_of_cropland_and_solar_demanded": 4,
    },
)
def increment_of_cropland_and_solar_limited():
    """
    The same increment and increment of croplands and solar demanded but saturated at the maximum change per year observed historically
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["SOLAR LAND"]] = False
    value.values[except_subs.values] = (
        np.minimum(
            initial_land_use_by_region() * maximum_annual_land_use_change(),
            np.abs(increment_of_cropland_and_solar_demanded()),
        )
        * zidz(
            increment_of_cropland_and_solar_demanded(),
            np.abs(increment_of_cropland_and_solar_demanded()),
        )
    ).values[except_subs.values]
    value.loc[:, ["SOLAR LAND"]] = (
        increment_of_cropland_and_solar_demanded()
        .loc[:, "SOLAR LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="increment of urban land demanded",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "_smooth_increment_of_urban_land_demanded": 1,
        "urban_land_dispersion_ratio": 1,
        "unit_conversion_m2_km2": 1,
    },
    other_deps={
        "_smooth_increment_of_urban_land_demanded": {
            "initial": {"exo_population_variation_exogenous": 1},
            "step": {"exo_population_variation_exogenous": 1},
        }
    },
)
def increment_of_urban_land_demanded():
    """
    Increment of urban land demanded
    """
    return np.maximum(
        0,
        _smooth_increment_of_urban_land_demanded()
        * urban_land_dispersion_ratio()
        / unit_conversion_m2_km2(),
    )


_smooth_increment_of_urban_land_demanded = Smooth(
    lambda: exo_population_variation_exogenous(),
    lambda: xr.DataArray(
        10, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    lambda: exo_population_variation_exogenous(),
    lambda: 1,
    "_smooth_increment_of_urban_land_demanded",
)


@component.add(
    name="land for solar demanded",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "switch_landwater": 1,
        "exo_land_for_solar_demanded": 1,
        "land_use_by_protra": 1,
    },
)
def land_for_solar_demanded():
    """
    stock of land demanded for solar energy from the Energy module
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: if_then_else(
            switch_landwater() == 1,
            lambda: land_use_by_protra()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True),
            lambda: exo_land_for_solar_demanded(time()),
        ),
    )


@component.add(
    name="land use changes demanded",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "trends_of_land_use_changes": 1,
        "check_exogenous_land_use_demands": 1,
        "switch_law_exogenous_land_use_demands": 2,
        "land_use_changes_demanded_before_exogenous": 1,
    },
)
def land_use_changes_demanded():
    """
    Land use changes demanded by policies, by shortage signals and by trends, if exogenous values are selected (CHECK EXOGENOUS LAND USE DEMANDS =0) exogenous values substitute the calculated ones
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: trends_of_land_use_changes(),
        lambda: switch_law_exogenous_land_use_demands()
        * land_use_changes_demanded_before_exogenous()
        + (1 - switch_law_exogenous_land_use_demands())
        * check_exogenous_land_use_demands(),
    )


@component.add(
    name="land use changes demanded before exogenous",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "trends_of_land_use_changes": 6,
        "land_use_changes_driven_by_demands": 6,
    },
)
def land_use_changes_demanded_before_exogenous():
    """
    Land use changes demanded by policies, by shortage signals and by trends, before the exogenout values are added (if demanded)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        trends_of_land_use_changes()
        .loc[:, "CROPLAND IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST PRIMARY"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST PRIMARY"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        (
            trends_of_land_use_changes()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
            + land_use_changes_driven_by_demands()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = (
        trends_of_land_use_changes()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = (
        land_use_changes_driven_by_demands()
        .loc[:, "URBAN LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        land_use_changes_driven_by_demands()
        .loc[:, "SOLAR LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    return value


@component.add(
    name="land use changes driven by demands",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 6,
        "time_historical_data_land_module": 6,
        "increment_of_cropland_and_solar_limited": 3,
        "afforestation_due_to_policies": 1,
        "forest_plantations_growth_due_to_policies": 1,
        "increment_of_urban_land_demanded": 1,
    },
)
def land_use_changes_driven_by_demands():
    """
    Land use changes demanded by policies of by shortage signals that are latter added to the trends
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: afforestation_due_to_policies(),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = 0
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: forest_plantations_growth_due_to_policies(),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: increment_of_urban_land_demanded(),
        )
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: increment_of_cropland_and_solar_limited()
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    return value


@component.add(
    name="matrix of land use change demands",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_changes_demanded": 12,
        "share_of_land_use_change_from_others": 12,
    },
)
def matrix_of_land_use_change_demands():
    """
    Matrix of land use changes demanded. Demands might or might not be fulfilled due to limits and competition of other uses. From land use LANDS_I (down, first index) to land use LANDS_MAP_I (right, second index) WE take from land use LANDS_I the demand of LANDS_MAP_I * the % of the demand of LANDS_MAP_I from LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    value.loc[:, :, ["CROPLAND RAINFED"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "CROPLAND RAINFED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["CROPLAND RAINFED"]}, 2)
        .values
    )
    value.loc[:, :, ["CROPLAND IRRIGATED"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["CROPLAND IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST MANAGED"]] = (
        (
            land_use_changes_demanded().loc[:, "FOREST MANAGED"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST MANAGED"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST PRIMARY"]] = (
        (
            land_use_changes_demanded().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST PRIMARY"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST PLANTATIONS"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "SHRUBLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SHRUBLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "GRASSLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "GRASSLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        (
            land_use_changes_demanded().loc[:, "WETLAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "WETLAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "URBAN LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "URBAN LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["URBAN LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SOLAR LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "SOLAR LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SOLAR LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["SOLAR LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = (
        (
            land_use_changes_demanded()
            .loc[:, "SNOW ICE WATERBODIES"]
            .reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "SNOW ICE WATERBODIES"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["SNOW ICE WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER LAND"]] = (
        (
            land_use_changes_demanded().loc[:, "OTHER LAND"].reset_coords(drop=True)
            * share_of_land_use_change_from_others()
            .loc[:, :, "OTHER LAND"]
            .reset_coords(drop=True)
        )
        .expand_dims({"LANDS MAP I": ["OTHER LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="share of land use change from others",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 9,
        "time_historical_data_land_module": 9,
        "historical_share_of_land_use_changes_from_others": 9,
        "land_use_changes_demanded": 9,
        "share_of_land_use_changes_from_others_up": 9,
        "initial_share_of_land_use_changes_from_others_down": 9,
    },
)
def share_of_land_use_change_from_others():
    """
    Matrix of values that tells from whcih land use the land changes of a perticular use come from SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    value.loc[["EU27"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["EU27", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["EU27", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["EU27", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["EU27", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["UK", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["UK", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["UK", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["UK", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["CHINA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["CHINA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["CHINA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["CHINA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["EASOC", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["EASOC", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["EASOC", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["EASOC", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["INDIA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["INDIA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["INDIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["INDIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["LATAM", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["LATAM", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["LATAM", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["LATAM", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["RUSSIA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["RUSSIA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["RUSSIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["RUSSIA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["USMCA", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["USMCA", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["USMCA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["USMCA", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :, :] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_share_of_land_use_changes_from_others()
            .loc["LROW", :, :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                (
                    land_use_changes_demanded()
                    .loc["LROW", :]
                    .reset_coords(drop=True)
                    .rename({"LANDS I": "LANDS MAP I"})
                    > 0
                ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
                lambda: share_of_land_use_changes_from_others_up()
                .loc["LROW", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
                lambda: initial_share_of_land_use_changes_from_others_down()
                .loc["LROW", :, :]
                .reset_coords(drop=True)
                .transpose("LANDS MAP I", "LANDS I"),
            ).transpose("LANDS I", "LANDS MAP I"),
        )
        .expand_dims({"REGIONS 35 I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="share of land use changes from others up",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_share_of_land_use_changes_from_others_up": 12,
        "time": 1,
        "switch_solar_land_from_others_sp": 1,
        "year_initial_solar_land_from_others_sp": 1,
        "objective_solar_land_from_others_sp": 1,
    },
)
def share_of_land_use_changes_from_others_up():
    """
    Matrix of values that tells from whcih land use the land changes of a perticular use come from, constant except for solar land old and changed in march24 (noefer): IF_THEN_ELSE( SWITCH_SOLAR_LAND_FROM_OTHERS_SP[REGIONS_9_I]=1,share_of_solar_land_from_ot hers[REGIONS_9_I,LANDS_I], INITIAL_SHARE_OF_LAND_USE_CHANGES_FROM_OTHERS_UP[REGIONS_9_I,LANDS_I,SOLAR_ LAND])
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    value.loc[:, :, ["CROPLAND RAINFED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND RAINFED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["CROPLAND RAINFED"]}, 2)
        .values
    )
    value.loc[:, :, ["CROPLAND IRRIGATED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["CROPLAND IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST MANAGED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST MANAGED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST PRIMARY"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST PRIMARY"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST PLANTATIONS"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SHRUBLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "WETLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "URBAN LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["URBAN LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SOLAR LAND"]] = (
        if_then_else(
            np.logical_and(
                switch_solar_land_from_others_sp() == 1,
                time() > year_initial_solar_land_from_others_sp(),
            ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
            lambda: objective_solar_land_from_others_sp(),
            lambda: initial_share_of_land_use_changes_from_others_up()
            .loc[:, :, "SOLAR LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS MAP I": ["SOLAR LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["SNOW ICE WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "OTHER LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["OTHER LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="share of solar land from others",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_solar_land_from_others": 1},
    other_deps={
        "_integ_share_of_solar_land_from_others": {
            "initial": {"historical_share_of_land_use_changes_from_others": 1},
            "step": {"changes_of_share_of_solar_land": 1},
        }
    },
)
def share_of_solar_land_from_others():
    """
    Vector that tells from which land use the land for solar comes from. Initially equal to the observed shares, changed by policies.
    """
    return _integ_share_of_solar_land_from_others()


_integ_share_of_solar_land_from_others = Integ(
    lambda: changes_of_share_of_solar_land(),
    lambda: historical_share_of_land_use_changes_from_others()
    .loc[:, :, "SOLAR LAND"]
    .reset_coords(drop=True),
    "_integ_share_of_solar_land_from_others",
)


@component.add(
    name="share solar urban",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 2},
)
def share_solar_urban():
    """
    share of the area of solar land with respect to the area of urban land
    """
    return zidz(
        land_use_area_by_region().loc[:, "SOLAR LAND"].reset_coords(drop=True),
        land_use_area_by_region().loc[:, "URBAN LAND"].reset_coords(drop=True),
    )


@component.add(
    name="stress signal solar land",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_maximum_share_solar_urban_sp": 1,
        "policy_maximum_share_solar_urban_sp": 6,
        "share_solar_urban": 4,
    },
)
def stress_signal_solar_land():
    """
    Variable sending signal of stress of land for solar . If=1 no stress, from 0,5 to 1 the stress grows linearly, If =0 maximum stress
    """
    return if_then_else(
        switch_policy_maximum_share_solar_urban_sp() == 0,
        lambda: xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: if_then_else(
            share_solar_urban() < policy_maximum_share_solar_urban_sp() * 0.8,
            lambda: xr.DataArray(
                1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    share_solar_urban() >= policy_maximum_share_solar_urban_sp() * 0.8,
                    share_solar_urban() < policy_maximum_share_solar_urban_sp(),
                ),
                lambda: 1
                - (
                    1
                    / (
                        policy_maximum_share_solar_urban_sp()
                        - policy_maximum_share_solar_urban_sp() * 0.8
                    )
                )
                * (share_solar_urban() - policy_maximum_share_solar_urban_sp() * 0.8),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
        ),
    )


@component.add(
    name="SWITCH LAW EXOGENOUS LAND USE DEMANDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law_exogenous_land_use_demands"},
)
def switch_law_exogenous_land_use_demands():
    """
    If this parameter =1 the land use submodule works normally, If it is =0, exogenous land demands are taken.
    """
    return _ext_constant_switch_law_exogenous_land_use_demands()


_ext_constant_switch_law_exogenous_land_use_demands = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW_EXOGENOUS_LAND_USE_DEMANDS",
    {},
    _root,
    {},
    "_ext_constant_switch_law_exogenous_land_use_demands",
)


@component.add(
    name="trends of land use changes",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 8,
        "time_historical_data_land_module": 8,
        "historical_trends_of_land_use_demand": 8,
        "trends_of_land_use_demand": 8,
    },
)
def trends_of_land_use_changes():
    """
    land use changes demanded by trends calculated using historcal data
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = 0
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_trends_of_land_use_demand()
            .loc[:, "OTHER LAND"]
            .reset_coords(drop=True),
            lambda: trends_of_land_use_demand()
            .loc[:, "OTHER LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    return value
