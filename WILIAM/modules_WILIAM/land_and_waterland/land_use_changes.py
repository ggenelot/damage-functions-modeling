"""
Module land_and_waterland.land_use_changes
Translated using PySD version 3.14.0
"""

@component.add(
    name="aux land uses 2015",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_land_uses_2015": 1},
    other_deps={
        "_delayfixed_aux_land_uses_2015": {
            "initial": {"time_step": 1},
            "step": {"land_uses_until_2015": 1},
        }
    },
)
def aux_land_uses_2015():
    """
    Auxiliary variable to estimate the land uses in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_land_uses_2015()


_delayfixed_aux_land_uses_2015 = DelayFixed(
    lambda: land_uses_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    ),
    time_step,
    "_delayfixed_aux_land_uses_2015",
)


@component.add(
    name="cropland loss due to sea level rise by region",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate_change_damage": 1,
        "sea_level_rise_by_region": 1,
        "effective_percent_of_land_change_per_meter_of_sea_level_rise": 1,
        "unit_conversion_km2_ha": 1,
    },
)
def cropland_loss_due_to_sea_level_rise_by_region():
    """
    the agricultural land lost for the sea level rise in each country
    """
    return if_then_else(
        switch_climate_change_damage() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: sea_level_rise_by_region()
        * effective_percent_of_land_change_per_meter_of_sea_level_rise()
        * unit_conversion_km2_ha(),
    )


@component.add(
    name="factor of maximum land limit",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "matrix_of_accumulated_land_use_changes": 2,
        "matrix_of_maximum_land_changes": 2,
        "land_use_changes_demanded": 2,
        "initial_land_use_by_region_2015": 1,
        "land_use_area_by_region": 1,
        "maximum_land_uses_by_source": 1,
        "select_limits_land_uses_by_source_sp": 1,
    },
)
def factor_of_maximum_land_limit():
    """
    Factor of maximum land use changes by region, It becomes =0 when the land use change demanded surpasses the maximum land use allowed and the land use change demanded is not done
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
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CROPLAND RAINFED"]] = False
    value.values[except_subs.values] = if_then_else(
        np.logical_and(
            matrix_of_accumulated_land_use_changes()
            >= matrix_of_maximum_land_changes(),
            (land_use_changes_demanded().rename({"LANDS I": "LANDS MAP I"}) > 0),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
                "LANDS MAP I": _subscript_dict["LANDS MAP I"],
            },
            ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
                "LANDS MAP I": _subscript_dict["LANDS MAP I"],
            },
            ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
        ),
    ).values[except_subs.values]
    value.loc[:, :, ["CROPLAND RAINFED"]] = (
        if_then_else(
            select_limits_land_uses_by_source_sp() == 0,
            lambda: if_then_else(
                np.logical_and(
                    matrix_of_accumulated_land_use_changes()
                    .loc[:, :, "CROPLAND RAINFED"]
                    .reset_coords(drop=True)
                    >= matrix_of_maximum_land_changes()
                    .loc[:, :, "CROPLAND RAINFED"]
                    .reset_coords(drop=True),
                    (
                        land_use_changes_demanded()
                        .loc[:, "CROPLAND RAINFED"]
                        .reset_coords(drop=True)
                        > 0
                    ),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "LANDS I": _subscript_dict["LANDS I"],
                    },
                    ["REGIONS 9 I", "LANDS I"],
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "LANDS I": _subscript_dict["LANDS I"],
                    },
                    ["REGIONS 9 I", "LANDS I"],
                ),
            ),
            lambda: if_then_else(
                land_use_area_by_region()
                .loc[:, "CROPLAND RAINFED"]
                .reset_coords(drop=True)
                >= maximum_land_uses_by_source()
                .loc[:, "CROPLAND RAINFED"]
                .reset_coords(drop=True)
                * initial_land_use_by_region_2015()
                .loc[:, "CROPLAND RAINFED"]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: xr.DataArray(
                    1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
        )
        .expand_dims({"LANDS MAP I": ["CROPLAND RAINFED"]}, 2)
        .values
    )
    return value


@component.add(
    name="factor of minimum land limit",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 2,
        "minimum_land_uses_by_region": 1,
        "minimum_limit_land_use_by_policy": 1,
    },
)
def factor_of_minimum_land_limit():
    """
    factor of minimum use of land for each region. It bebomes =0 when the land use change demanded makes another use become less thatn the minumum allowed, and the land use change demanded is not done
    """
    return if_then_else(
        np.logical_or(
            land_use_area_by_region() <= minimum_land_uses_by_region(),
            land_use_area_by_region() <= minimum_limit_land_use_by_policy(),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
            },
            ["REGIONS 9 I", "LANDS I"],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
            },
            ["REGIONS 9 I", "LANDS I"],
        ),
    )


@component.add(
    name="factor of solar land limit",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_land_protection_from_solar_pv_sp": 1,
        "year_initial_land_protection_from_solar_pv_sp": 1,
        "time": 2,
        "year_final_land_protection_from_solar_pv_sp": 1,
        "policy_land_protection_from_solar_pv_sp": 1,
    },
)
def factor_of_solar_land_limit():
    """
    =1 solar land can increase, =0 solar land cannot increase in that land use because that use is protected but only for solar PV instalation
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
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["SOLAR LAND"]] = False
    value.values[except_subs.values] = 1
    value.loc[:, :, ["SOLAR LAND"]] = (
        if_then_else(
            np.logical_and(
                switch_policy_land_protection_from_solar_pv_sp() == 1,
                np.logical_and(
                    time() > year_initial_land_protection_from_solar_pv_sp(),
                    time() < year_final_land_protection_from_solar_pv_sp(),
                ),
            ).expand_dims({"LANDS I": _subscript_dict["LANDS I"]}, 1),
            lambda: policy_land_protection_from_solar_pv_sp(),
            lambda: xr.DataArray(
                1,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "LANDS I": _subscript_dict["LANDS I"],
                },
                ["REGIONS 9 I", "LANDS I"],
            ),
        )
        .expand_dims({"LANDS MAP I": ["SOLAR LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="global loss of agricultural land by sea level rise",
    units="km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cropland_loss_due_to_sea_level_rise_by_region": 1},
)
def global_loss_of_agricultural_land_by_sea_level_rise():
    """
    the global loss of agricultural land by sea level rise for world
    """
    return sum(
        cropland_loss_due_to_sea_level_rise_by_region().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="growth land uses vs 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "land_use_area_by_region": 1, "land_uses_until_2015": 1},
)
def growth_land_uses_vs_2015():
    """
    Growth in land uses with relation to the year 2015. Used to endogenize solar rooftop potential with urban land variation in the energy module.
    """
    return if_then_else(
        time() > 2015,
        lambda: zidz(land_use_area_by_region(), land_uses_until_2015()),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LANDS I": _subscript_dict["LANDS I"],
            },
            ["REGIONS 9 I", "LANDS I"],
        ),
    )


@component.add(
    name="historical land use by region t",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_land_use_by_region": 1},
)
def historical_land_use_by_region_t():
    """
    Historical data of land use by region
    """
    return historical_land_use_by_region(time())


@component.add(
    name="increase of matrix of land use changes",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_of_land_use_changes": 1},
)
def increase_of_matrix_of_land_use_changes():
    """
    matrix of acumulated land use changes by region, used to see if the accumulated changes are greater than the amount of land that can go from une use to another because of physical suitability
    """
    return matrix_of_land_use_changes()


@component.add(
    name="land protection by policy",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_land_production_policy": 1,
        "year_initial_land_protecion_policy": 1,
        "time": 2,
        "year_final_land_protection_policy": 1,
        "objective_land_protection_policy": 1,
    },
)
def land_protection_by_policy():
    """
    share of the initial land of each type in 2015 that is protected from changes to other uses
    """
    return if_then_else(
        np.logical_and(
            switch_land_production_policy() == 1,
            np.logical_and(
                time() > year_initial_land_protecion_policy(),
                time() < year_final_land_protection_policy(),
            ),
        ),
        lambda: objective_land_protection_policy(),
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
    name="land use area by region",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_productive_uses": 10,
        "snow_ice_and_waterbodies_area": 3,
        "wetland_area": 3,
        "share_of_shrubland": 2,
    },
)
def land_use_area_by_region():
    """
    land use area by region
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
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "FOREST PRIMARY"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = (
        np.maximum(
            0,
            (
                land_use_area_productive_uses()
                .loc[:, "OTHER LAND"]
                .reset_coords(drop=True)
                - wetland_area()
                - snow_ice_and_waterbodies_area()
            )
            * share_of_shrubland(),
        )
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses().loc[:, "GRASSLAND"].reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = (
        np.maximum(0, wetland_area()).expand_dims({"LANDS I": ["WETLAND"]}, 1).values
    )
    value.loc[:, ["URBAN LAND"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        np.maximum(
            0,
            land_use_area_productive_uses()
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = (
        np.maximum(0, snow_ice_and_waterbodies_area())
        .expand_dims({"LANDS I": ["SNOW ICE WATERBODIES"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        np.maximum(
            0,
            (
                land_use_area_productive_uses()
                .loc[:, "OTHER LAND"]
                .reset_coords(drop=True)
                - wetland_area()
                - snow_ice_and_waterbodies_area()
            )
            * (1 - share_of_shrubland()),
        )
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="land use area productive uses",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_land_use_area_productive_uses": 1,
        "_integ_land_use_area_productive_uses_1": 1,
        "_integ_land_use_area_productive_uses_2": 1,
        "_integ_land_use_area_productive_uses_3": 1,
        "_integ_land_use_area_productive_uses_4": 1,
        "_integ_land_use_area_productive_uses_5": 1,
        "_integ_land_use_area_productive_uses_6": 1,
        "_integ_land_use_area_productive_uses_7": 1,
        "_integ_land_use_area_productive_uses_8": 1,
        "_integ_land_use_area_productive_uses_9": 1,
        "_integ_land_use_area_productive_uses_10": 1,
        "_integ_land_use_area_productive_uses_11": 1,
    },
    other_deps={
        "_integ_land_use_area_productive_uses": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_1": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_2": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_3": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_4": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_5": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_6": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_7": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_8": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_9": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_10": {
            "initial": {},
            "step": {"land_use_changes_productive_uses": 1},
        },
        "_integ_land_use_area_productive_uses_11": {
            "initial": {"initial_land_use_by_region": 4},
            "step": {"land_use_changes_productive_uses": 4},
        },
    },
)
def land_use_area_productive_uses():
    """
    stock of land uses area productive uses by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = _integ_land_use_area_productive_uses().values
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        _integ_land_use_area_productive_uses_1().values
    )
    value.loc[:, ["FOREST MANAGED"]] = _integ_land_use_area_productive_uses_2().values
    value.loc[:, ["FOREST PRIMARY"]] = _integ_land_use_area_productive_uses_3().values
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        _integ_land_use_area_productive_uses_4().values
    )
    value.loc[:, ["SHRUBLAND"]] = _integ_land_use_area_productive_uses_5().values
    value.loc[:, ["GRASSLAND"]] = _integ_land_use_area_productive_uses_6().values
    value.loc[:, ["WETLAND"]] = _integ_land_use_area_productive_uses_7().values
    value.loc[:, ["URBAN LAND"]] = _integ_land_use_area_productive_uses_8().values
    value.loc[:, ["SOLAR LAND"]] = _integ_land_use_area_productive_uses_9().values
    value.loc[:, ["SNOW ICE WATERBODIES"]] = (
        _integ_land_use_area_productive_uses_10().values
    )
    value.loc[:, ["OTHER LAND"]] = _integ_land_use_area_productive_uses_11().values
    return value


_integ_land_use_area_productive_uses = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "CROPLAND RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1),
    "_integ_land_use_area_productive_uses",
)

_integ_land_use_area_productive_uses_1 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "CROPLAND IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1),
    "_integ_land_use_area_productive_uses_1",
)

_integ_land_use_area_productive_uses_2 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1),
    "_integ_land_use_area_productive_uses_2",
)

_integ_land_use_area_productive_uses_3 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1),
    "_integ_land_use_area_productive_uses_3",
)

_integ_land_use_area_productive_uses_4 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1),
    "_integ_land_use_area_productive_uses_4",
)

_integ_land_use_area_productive_uses_5 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SHRUBLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SHRUBLAND"]},
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_area_productive_uses_5",
)

_integ_land_use_area_productive_uses_6 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["GRASSLAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["GRASSLAND"]}, 1),
    "_integ_land_use_area_productive_uses_6",
)

_integ_land_use_area_productive_uses_7 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "WETLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["WETLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["WETLAND"]},
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_area_productive_uses_7",
)

_integ_land_use_area_productive_uses_8 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "URBAN LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["URBAN LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "URBAN LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["URBAN LAND"]}, 1),
    "_integ_land_use_area_productive_uses_8",
)

_integ_land_use_area_productive_uses_9 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SOLAR LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "SOLAR LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1),
    "_integ_land_use_area_productive_uses_9",
)

_integ_land_use_area_productive_uses_10 = Integ(
    lambda: land_use_changes_productive_uses()
    .loc[:, "SNOW ICE WATERBODIES"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SNOW ICE WATERBODIES"]}, 1),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": ["SNOW ICE WATERBODIES"],
        },
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_area_productive_uses_10",
)

_integ_land_use_area_productive_uses_11 = Integ(
    lambda: (
        land_use_changes_productive_uses().loc[:, "OTHER LAND"].reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses().loc[:, "WETLAND"].reset_coords(drop=True)
        + land_use_changes_productive_uses().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS I": ["OTHER LAND"]}, 1),
    lambda: (
        initial_land_use_by_region().loc[:, "OTHER LAND"].reset_coords(drop=True)
        + initial_land_use_by_region()
        .loc[:, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS I": ["OTHER LAND"]}, 1),
    "_integ_land_use_area_productive_uses_11",
)


@component.add(
    name="land use by region calibrated",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_land_use_by_region_calibrated": 1,
        "_integ_land_use_by_region_calibrated_1": 1,
        "_integ_land_use_by_region_calibrated_2": 1,
        "_integ_land_use_by_region_calibrated_3": 1,
        "_integ_land_use_by_region_calibrated_4": 1,
        "_integ_land_use_by_region_calibrated_5": 1,
        "_integ_land_use_by_region_calibrated_6": 1,
        "_integ_land_use_by_region_calibrated_7": 1,
        "_integ_land_use_by_region_calibrated_8": 1,
        "_integ_land_use_by_region_calibrated_9": 1,
        "_integ_land_use_by_region_calibrated_10": 1,
        "_integ_land_use_by_region_calibrated_11": 1,
    },
    other_deps={
        "_integ_land_use_by_region_calibrated": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_1": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_2": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_3": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_4": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_5": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_6": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_7": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_8": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_9": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_10": {
            "initial": {},
            "step": {"land_use_changes_by_region_calibrated": 1},
        },
        "_integ_land_use_by_region_calibrated_11": {
            "initial": {"initial_land_use_by_region": 4},
            "step": {"land_use_changes_by_region_calibrated": 4},
        },
    },
)
def land_use_by_region_calibrated():
    """
    stock of calibrated land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = _integ_land_use_by_region_calibrated().values
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        _integ_land_use_by_region_calibrated_1().values
    )
    value.loc[:, ["FOREST MANAGED"]] = _integ_land_use_by_region_calibrated_2().values
    value.loc[:, ["FOREST PRIMARY"]] = _integ_land_use_by_region_calibrated_3().values
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        _integ_land_use_by_region_calibrated_4().values
    )
    value.loc[:, ["SHRUBLAND"]] = _integ_land_use_by_region_calibrated_5().values
    value.loc[:, ["GRASSLAND"]] = _integ_land_use_by_region_calibrated_6().values
    value.loc[:, ["WETLAND"]] = _integ_land_use_by_region_calibrated_7().values
    value.loc[:, ["URBAN LAND"]] = _integ_land_use_by_region_calibrated_8().values
    value.loc[:, ["SOLAR LAND"]] = _integ_land_use_by_region_calibrated_9().values
    value.loc[:, ["SNOW ICE WATERBODIES"]] = (
        _integ_land_use_by_region_calibrated_10().values
    )
    value.loc[:, ["OTHER LAND"]] = _integ_land_use_by_region_calibrated_11().values
    return value


_integ_land_use_by_region_calibrated = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["CROPLAND RAINFED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND RAINFED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1),
    "_integ_land_use_by_region_calibrated",
)

_integ_land_use_by_region_calibrated_1 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["CROPLAND IRRIGATED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "CROPLAND IRRIGATED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1),
    "_integ_land_use_by_region_calibrated_1",
)

_integ_land_use_by_region_calibrated_2 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST MANAGED", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST MANAGED"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1),
    "_integ_land_use_by_region_calibrated_2",
)

_integ_land_use_by_region_calibrated_3 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST PRIMARY", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST PRIMARY"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1),
    "_integ_land_use_by_region_calibrated_3",
)

_integ_land_use_by_region_calibrated_4 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["FOREST PLANTATIONS", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "FOREST PLANTATIONS"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1),
    "_integ_land_use_by_region_calibrated_4",
)

_integ_land_use_by_region_calibrated_5 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SHRUBLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SHRUBLAND"]},
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_by_region_calibrated_5",
)

_integ_land_use_by_region_calibrated_6 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["GRASSLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["GRASSLAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "GRASSLAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["GRASSLAND"]}, 1),
    "_integ_land_use_by_region_calibrated_6",
)

_integ_land_use_by_region_calibrated_7 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["WETLAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["WETLAND"]}, 1),
    lambda: xr.DataArray(
        0,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["WETLAND"]},
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_by_region_calibrated_7",
)

_integ_land_use_by_region_calibrated_8 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["URBAN LAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["URBAN LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "URBAN LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["URBAN LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_8",
)

_integ_land_use_by_region_calibrated_9 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SOLAR LAND", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1),
    lambda: initial_land_use_by_region()
    .loc[:, "SOLAR LAND"]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_9",
)

_integ_land_use_by_region_calibrated_10 = Integ(
    lambda: land_use_changes_by_region_calibrated()
    .loc["SNOW ICE WATERBODIES", :]
    .reset_coords(drop=True)
    .expand_dims({"LANDS I": ["SNOW ICE WATERBODIES"]}, 1),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": ["SNOW ICE WATERBODIES"],
        },
        ["REGIONS 9 I", "LANDS I"],
    ),
    "_integ_land_use_by_region_calibrated_10",
)

_integ_land_use_by_region_calibrated_11 = Integ(
    lambda: (
        land_use_changes_by_region_calibrated()
        .loc["OTHER LAND", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["SNOW ICE WATERBODIES", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["WETLAND", :]
        .reset_coords(drop=True)
        + land_use_changes_by_region_calibrated()
        .loc["SHRUBLAND", :]
        .reset_coords(drop=True)
    ).expand_dims({"LANDS I": ["OTHER LAND"]}, 1),
    lambda: (
        initial_land_use_by_region().loc[:, "OTHER LAND"].reset_coords(drop=True)
        + initial_land_use_by_region()
        .loc[:, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True)
        + initial_land_use_by_region().loc[:, "SHRUBLAND"].reset_coords(drop=True)
    ).expand_dims({"LANDS I": ["OTHER LAND"]}, 1),
    "_integ_land_use_by_region_calibrated_11",
)


@component.add(
    name="land use changes by region calibrated",
    units="km2/Year",
    subscripts=["LANDS I", "REGIONS 9 I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"vector_of_land_use_changes": 13},
)
def land_use_changes_by_region_calibrated():
    """
    calibrated land use changes by region
    """
    value = xr.DataArray(
        np.nan,
        {
            "LANDS I": _subscript_dict["LANDS I"],
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        },
        ["LANDS I", "REGIONS 9 I"],
    )
    value.loc[["CROPLAND RAINFED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "CROPLAND RAINFED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 0)
        .values
    )
    value.loc[["CROPLAND IRRIGATED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "CROPLAND IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 0)
        .values
    )
    value.loc[["FOREST MANAGED"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST MANAGED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 0)
        .values
    )
    value.loc[["FOREST PRIMARY"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST PRIMARY"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 0)
        .values
    )
    value.loc[["FOREST PLANTATIONS"], :] = (
        vector_of_land_use_changes()
        .loc[:, "FOREST PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 0)
        .values
    )
    value.loc[["SHRUBLAND"], :] = 0
    value.loc[["GRASSLAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 0)
        .values
    )
    value.loc[["WETLAND"], :] = 0
    value.loc[["URBAN LAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "URBAN LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 0)
        .values
    )
    value.loc[["SOLAR LAND"], :] = (
        vector_of_land_use_changes()
        .loc[:, "SOLAR LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 0)
        .values
    )
    value.loc[["SNOW ICE WATERBODIES"], :] = (
        vector_of_land_use_changes()
        .loc[:, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS I": ["SNOW ICE WATERBODIES"]}, 0)
        .values
    )
    value.loc[["OTHER LAND"], :] = (
        (
            vector_of_land_use_changes().loc[:, "OTHER LAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "SOLAR LAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "WETLAND"].reset_coords(drop=True)
            + vector_of_land_use_changes().loc[:, "SHRUBLAND"].reset_coords(drop=True)
        )
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 0)
        .values
    )
    return value


@component.add(
    name="land use changes productive uses",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 21,
        "time_historical_data_land_module": 9,
        "historical_land_use_change_by_region": 12,
        "vector_of_land_use_changes": 12,
    },
)
def land_use_changes_productive_uses():
    """
    land use changes for productive uses by region, productive uses exclude snow ice and waterbodies, wetlands, shrublands and other lands that are in this vector added all to other lands
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
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "CROPLAND RAINFED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST PRIMARY"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "FOREST PRIMARY"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
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
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "GRASSLAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
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
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "URBAN LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        if_then_else(
            time() <= time_historical_data_land_module(),
            lambda: historical_land_use_change_by_region(time())
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
            lambda: vector_of_land_use_changes()
            .loc[:, "SOLAR LAND"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = (
        (
            if_then_else(
                time() <= time_historical_data_land_module(),
                lambda: historical_land_use_change_by_region(time())
                .loc[:, "OTHER LAND"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "SNOW ICE WATERBODIES"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "WETLAND"]
                .reset_coords(drop=True)
                + historical_land_use_change_by_region(time())
                .loc[:, "SHRUBLAND"]
                .reset_coords(drop=True),
                lambda: vector_of_land_use_changes()
                .loc[:, "OTHER LAND"]
                .reset_coords(drop=True)
                + vector_of_land_use_changes()
                .loc[:, "SNOW ICE WATERBODIES"]
                .reset_coords(drop=True)
                + vector_of_land_use_changes()
                .loc[:, "WETLAND"]
                .reset_coords(drop=True),
            )
            + vector_of_land_use_changes().loc[:, "SHRUBLAND"].reset_coords(drop=True)
        )
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="land uses until 2015",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "land_use_area_by_region": 1, "aux_land_uses_2015": 1},
)
def land_uses_until_2015():
    """
    Land uses fixed in the value of the year 2015 for the subsequent years of the simulation.
    """
    return if_then_else(
        time() < 2015, lambda: land_use_area_by_region(), lambda: aux_land_uses_2015()
    )


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_eroi_min_potential_wind_solar_sp": 5,
        "limits_to_solar_land_expansion_eroi_min_0": 1,
        "limits_to_solar_land_expansion_eroi_min_3": 1,
        "limits_to_solar_land_expansion_eroi_min_8": 1,
        "limits_to_solar_land_expansion_eroi_min_5": 1,
        "limits_to_solar_land_expansion_eroi_min_10": 1,
        "limits_to_solar_land_expansion_eroi_min_2": 1,
    },
)
def limits_to_solar_land_expansion_eroi_min():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return if_then_else(
        select_eroi_min_potential_wind_solar_sp() == 0,
        lambda: limits_to_solar_land_expansion_eroi_min_0(),
        lambda: if_then_else(
            select_eroi_min_potential_wind_solar_sp() == 2,
            lambda: limits_to_solar_land_expansion_eroi_min_2(),
            lambda: if_then_else(
                select_eroi_min_potential_wind_solar_sp() == 3,
                lambda: limits_to_solar_land_expansion_eroi_min_3(),
                lambda: if_then_else(
                    select_eroi_min_potential_wind_solar_sp() == 5,
                    lambda: limits_to_solar_land_expansion_eroi_min_5(),
                    lambda: if_then_else(
                        select_eroi_min_potential_wind_solar_sp() == 8,
                        lambda: limits_to_solar_land_expansion_eroi_min_8(),
                        lambda: limits_to_solar_land_expansion_eroi_min_10(),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="matrix of accumulated land use changes",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_matrix_of_accumulated_land_use_changes": 1},
    other_deps={
        "_integ_matrix_of_accumulated_land_use_changes": {
            "initial": {},
            "step": {"increase_of_matrix_of_land_use_changes": 1},
        }
    },
)
def matrix_of_accumulated_land_use_changes():
    """
    stock of matrix of accumulated land use changes by region
    """
    return _integ_matrix_of_accumulated_land_use_changes()


_integ_matrix_of_accumulated_land_use_changes = Integ(
    lambda: increase_of_matrix_of_land_use_changes(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    ),
    "_integ_matrix_of_accumulated_land_use_changes",
)


@component.add(
    name="matrix of land use changes",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "matrix_of_land_use_change_demands": 3,
        "factor_of_maximum_land_limit": 2,
        "factor_of_solar_land_limit": 2,
        "factor_of_minimum_land_limit": 2,
    },
)
def matrix_of_land_use_changes():
    """
    Matrix of land use changes from land use LANDS_I (down) to land use LANDS_MAP_I (right) multiplied by a factor that is 0 when the one that sends reaches its minimum limit and a factor that is 0 when the ose that sends reaches the limit of land suitable for that change
    """
    return if_then_else(
        matrix_of_land_use_change_demands() >= 0,
        lambda: factor_of_minimum_land_limit()
        * factor_of_maximum_land_limit()
        * factor_of_solar_land_limit()
        * matrix_of_land_use_change_demands(),
        lambda: (
            factor_of_minimum_land_limit().rename({"LANDS I": "LANDS MAP I"})
            * factor_of_maximum_land_limit().rename(
                {"LANDS I": "LANDS MAP I", "LANDS MAP I": "LANDS I"}
            )
            * factor_of_solar_land_limit().rename(
                {"LANDS I": "LANDS MAP I", "LANDS MAP I": "LANDS I"}
            )
            * matrix_of_land_use_change_demands().transpose(
                "REGIONS 9 I", "LANDS MAP I", "LANDS I"
            )
        ).transpose("REGIONS 9 I", "LANDS I", "LANDS MAP I"),
    )


@component.add(
    name="MATRIX OF MAXIMUM LAND CHANGES",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_land_use_by_region_2015": 2,
        "limits_to_land_use_changes_by_region": 1,
        "limits_to_solar_land_expansion_eroi_min": 1,
    },
)
def matrix_of_maximum_land_changes():
    """
    matrix of maximum land changes by region. FROM USE LANDS_I TO USE LANDS_MAP_I is the percent of use LANDS_I (related to the initial value) that can be converted to use LANDS_I
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
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["SOLAR LAND"]] = False
    value.values[except_subs.values] = (
        initial_land_use_by_region_2015() * limits_to_land_use_changes_by_region()
    ).values[except_subs.values]
    value.loc[:, :, ["SOLAR LAND"]] = (
        (initial_land_use_by_region_2015() * limits_to_solar_land_expansion_eroi_min())
        .expand_dims({"LANDS MAP I": ["SOLAR LAND"]}, 2)
        .values
    )
    return value


@component.add(
    name="minimum limit land use by policy",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "initial_land_use_by_region_2015": 2,
        "model_explorer_land_protection": 1,
        "land_protection_by_policy": 1,
    },
)
def minimum_limit_land_use_by_policy():
    """
    Minimum limit of land use by policy for each region
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_land_protection() * initial_land_use_by_region_2015(),
        lambda: land_protection_by_policy() * initial_land_use_by_region_2015(),
    )


@component.add(
    name="objective land protection policy",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "objective_cropland_protection_sp": 2,
        "objective_managed_forest_protection_sp": 1,
        "objective_primary_forest_protection_sp": 1,
        "objective_natural_land_protection_sp": 2,
        "objective_grassland_protection_sp": 1,
    },
)
def objective_land_protection_policy():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    value.loc[:, ["CROPLAND RAINFED"]] = (
        objective_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        objective_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        objective_managed_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        objective_primary_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        objective_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        objective_grassland_protection_sp()
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        objective_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


@component.add(
    name="SELECT LIMITS LAND USES BY SOURCE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_limits_land_uses_by_source_sp"},
)
def select_limits_land_uses_by_source_sp():
    """
    SELECT with two options (scenario hypothesis): =1 The limits to land expansion is drive by the land type that demands the land (activated only for cropland and aforestation+plantations) =0 limits given by the suitability of then land uses that are taken
    """
    return _ext_constant_select_limits_land_uses_by_source_sp()


_ext_constant_select_limits_land_uses_by_source_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SELECT_LIMITS_LAND_USES_BY_SOURCE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_limits_land_uses_by_source_sp",
)


@component.add(
    name="snow ice and waterbodies area",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_snow_ice_and_waterbodies_area": 1},
    other_deps={
        "_integ_snow_ice_and_waterbodies_area": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"variation_of_snow_ice_and_waterbodies_area": 1},
        }
    },
)
def snow_ice_and_waterbodies_area():
    """
    stock of snow ice and waterbodies area by region
    """
    return _integ_snow_ice_and_waterbodies_area()


_integ_snow_ice_and_waterbodies_area = Integ(
    lambda: variation_of_snow_ice_and_waterbodies_area(),
    lambda: initial_land_use_by_region()
    .loc[:, "SNOW ICE WATERBODIES"]
    .reset_coords(drop=True),
    "_integ_snow_ice_and_waterbodies_area",
)


@component.add(
    name="switch land production policy",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_cropland_protection_sp": 2,
        "switch_managed_forest_protection_sp": 1,
        "switch_primary_forest_protection_sp": 1,
        "switch_natural_land_protection_sp": 2,
        "switch_grassland_protection_sp": 1,
    },
)
def switch_land_production_policy():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
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
        switch_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        switch_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        switch_managed_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        switch_primary_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        switch_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        switch_grassland_protection_sp()
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        switch_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


@component.add(
    name="variation of snow ice and waterbodies area",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def variation_of_snow_ice_and_waterbodies_area():
    """
    variation of snow ice and waterbodies area by region
    """
    return xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="variation of wetland area",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def variation_of_wetland_area():
    """
    variation of wetland area by region
    """
    return xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="vector of land use changes",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cropland_loss_due_to_sea_level_rise_by_region": 1,
        "matrix_of_land_use_changes": 24,
    },
)
def vector_of_land_use_changes():
    """
    vector of land use changes by region
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
            cropland_loss_due_to_sea_level_rise_by_region()
            + sum(
                matrix_of_land_use_changes()
                .loc[:, :, "CROPLAND RAINFED"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "CROPLAND RAINFED", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "CROPLAND IRRIGATED"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "CROPLAND IRRIGATED", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST MANAGED"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST MANAGED", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST PRIMARY"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST PRIMARY", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "FOREST PLANTATIONS"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "FOREST PLANTATIONS", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 1)
        .values
    )
    value.loc[:, ["SHRUBLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SHRUBLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SHRUBLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "GRASSLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "GRASSLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "WETLAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "WETLAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["WETLAND"]}, 1)
        .values
    )
    value.loc[:, ["URBAN LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "URBAN LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "URBAN LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["URBAN LAND"]}, 1)
        .values
    )
    value.loc[:, ["SOLAR LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SOLAR LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SOLAR LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["SOLAR LAND"]}, 1)
        .values
    )
    value.loc[:, ["SNOW ICE WATERBODIES"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "SNOW ICE WATERBODIES"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "SNOW ICE WATERBODIES", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["SNOW ICE WATERBODIES"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        (
            sum(
                matrix_of_land_use_changes()
                .loc[:, :, "OTHER LAND"]
                .reset_coords(drop=True)
                .rename({"LANDS I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
            - sum(
                matrix_of_land_use_changes()
                .loc[:, "OTHER LAND", :]
                .reset_coords(drop=True)
                .rename({"LANDS MAP I": "LANDS I!"}),
                dim=["LANDS I!"],
            )
        )
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="wetland area",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_wetland_area": 1},
    other_deps={
        "_integ_wetland_area": {
            "initial": {"initial_land_use_by_region": 1},
            "step": {"variation_of_wetland_area": 1},
        }
    },
)
def wetland_area():
    """
    stock of wetland area by region
    """
    return _integ_wetland_area()


_integ_wetland_area = Integ(
    lambda: variation_of_wetland_area(),
    lambda: initial_land_use_by_region().loc[:, "WETLAND"].reset_coords(drop=True),
    "_integ_wetland_area",
)


@component.add(
    name="YEAR FINAL LAND PROTECTION FROM SOLAR PV SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_land_protection_from_solar_pv_sp"
    },
)
def year_final_land_protection_from_solar_pv_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_land_protection_from_solar_pv_sp()


_ext_constant_year_final_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_LAND_PROTECTION_FROM_SOLAR_PV_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_land_protection_from_solar_pv_sp",
)


@component.add(
    name="year final land protection policy",
    units="Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "year_final_cropland_protection_sp": 2,
        "year_final_managed_forest_protection_sp": 1,
        "year_final_primary_forest_protection_sp": 1,
        "year_final_natural_land_protection_sp": 2,
        "year_final_grassland_protection_sp": 1,
    },
)
def year_final_land_protection_policy():
    """
    final year of land protection policies
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
        year_final_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        year_final_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        year_final_managed_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        year_final_primary_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        year_final_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        year_final_grassland_protection_sp()
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        year_final_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


@component.add(
    name="year initial land protecion policy",
    units="Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "year_initial_cropland_protection_sp": 2,
        "year_initial_managed_forest_protection_sp": 1,
        "year_initial_primary_forest_protection_sp": 1,
        "year_initial_natural_land_protection_sp": 2,
        "year_initial_grassland_protection_sp": 1,
    },
)
def year_initial_land_protecion_policy():
    """
    initial year of land protection policies
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
        year_initial_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND RAINFED"]}, 1)
        .values
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = (
        year_initial_cropland_protection_sp()
        .expand_dims({"LANDS I": ["CROPLAND IRRIGATED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST MANAGED"]] = (
        year_initial_managed_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST MANAGED"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PRIMARY"]] = (
        year_initial_primary_forest_protection_sp()
        .expand_dims({"LANDS FOREST I": ["FOREST PRIMARY"]}, 1)
        .values
    )
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = (
        year_initial_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["SHRUBLAND"]}, 1)
        .values
    )
    value.loc[:, ["GRASSLAND"]] = (
        year_initial_grassland_protection_sp()
        .expand_dims({"LANDS I": ["GRASSLAND"]}, 1)
        .values
    )
    value.loc[:, ["OTHER LAND"]] = (
        year_initial_natural_land_protection_sp()
        .expand_dims({"LANDS I": ["OTHER LAND"]}, 1)
        .values
    )
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


@component.add(
    name="YEAR INITIAL LAND PROTECTION FROM SOLAR PV SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_land_protection_from_solar_pv_sp"
    },
)
def year_initial_land_protection_from_solar_pv_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_land_protection_from_solar_pv_sp()


_ext_constant_year_initial_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_LAND_PROTECTION_FROM_SOLAR_PV_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_land_protection_from_solar_pv_sp",
)
