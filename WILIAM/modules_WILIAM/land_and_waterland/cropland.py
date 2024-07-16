"""
Module land_and_waterland.cropland
Translated using PySD version 3.14.0
"""

@component.add(
    name="area of crops all managements",
    units="km2",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 2,
        "shares_of_crops_all_managements": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_crops_all_managements():
    """
    Area of each crop, rainfed and irrigated added
    """
    return (
        (
            land_use_area_by_region().loc[:, "CROPLAND RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True)
        )
        * shares_of_crops_all_managements()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="area of irrigated crops",
    units="km2",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "shares_of_irrigated_crops": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_irrigated_crops():
    """
    irrigated crops area by crop and region. Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return (
        land_use_area_by_region().loc[:, "CROPLAND IRRIGATED"].reset_coords(drop=True)
        * shares_of_irrigated_crops()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="area of rainfed crops",
    units="km2",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "shares_of_rainfed_crops": 1,
        "land_area_adjust_coefficient": 1,
    },
)
def area_of_rainfed_crops():
    """
    Area of each rainfed crop in each region. Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return (
        land_use_area_by_region().loc[:, "CROPLAND RAINFED"].reset_coords(drop=True)
        * shares_of_rainfed_crops()
        * land_area_adjust_coefficient()
    )


@component.add(
    name="aux shortage crops",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ratio_shortage_of_crops": 1},
)
def aux_shortage_crops():
    """
    auxiliar check of crop shortage
    """
    return np.maximum(ratio_shortage_of_crops(), 1) - 1


@component.add(
    name="availability of crops",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "mask_crops": 2,
        "land_products_available_all_regions": 2,
        "land_products_demanded_world": 2,
    },
)
def availability_of_crops():
    """
    indicator available/demanded, if =1 all demanded is available, 0.5 menas 50% of demanded is available
    """
    value = xr.DataArray(
        np.nan,
        {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
        ["LAND PRODUCTS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["RESIDUES"]] = False
    except_subs.loc[["OTHER CROPS"]] = False
    except_subs.loc[["BIOFUEL 2GCROP"]] = False
    except_subs.loc[["WOOD"]] = False
    value.values[except_subs.values] = if_then_else(
        time() < time_historical_data_land_module(),
        lambda: mask_crops()
        * zidz(land_products_available_all_regions(), land_products_demanded_world()),
        lambda: mask_crops()
        * zidz(land_products_available_all_regions(), land_products_demanded_world()),
    ).values[except_subs.values]
    value.loc[["RESIDUES"]] = 1
    value.loc[["WOOD"]] = 1
    value.loc[["OTHER CROPS"]] = 1
    value.loc[["BIOFUEL 2GCROP"]] = 1
    return value


@component.add(
    name="crops available all managements",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_of_crops_all_managements": 1,
        "yields_of_crops_all_managements": 1,
    },
)
def crops_available_all_managements():
    """
    Crops available. Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=1
    """
    return area_of_crops_all_managements() * yields_of_crops_all_managements()


@component.add(
    name="factor maximum irrigated",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_irrigated_crops": 1, "maximum_irrigated_crops_shares": 1},
)
def factor_maximum_irrigated():
    """
    factor to avoid changes of shares of crops that would lead to negative area assigned to a crop
    """
    return if_then_else(
        shares_of_irrigated_crops() < maximum_irrigated_crops_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="factor maximum rainfed crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_rainfed_crops": 1, "maximum_rainfed_crops_shares": 1},
)
def factor_maximum_rainfed_crops():
    """
    factor to avoid changes of shares of crops that would lead to negative area assigned to a crop
    """
    return if_then_else(
        shares_of_rainfed_crops() < maximum_rainfed_crops_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="factor minimum irrigated",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_irrigated_crops": 1},
)
def factor_minimum_irrigated():
    """
    factor to avoid changes of shares of crops that would lead to negative area assigned to a crop
    """
    return if_then_else(
        shares_of_irrigated_crops() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="factor minimum rainfed",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_rainfed_crops": 1},
)
def factor_minimum_rainfed():
    """
    factor to avoid changes of shares of crops that would lead to negative area assigned to a crop
    """
    return if_then_else(
        shares_of_rainfed_crops() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="factor of maximum crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_crops_all_managements": 1, "maximum_crop_shares": 1},
)
def factor_of_maximum_crops():
    """
    factor to avoid the share of crops to become greater than 1 or to avoid crops to expand avobe the suitable area for those crops that requiere high quality lands. This limit is not activated except for =1.
    """
    return if_then_else(
        shares_of_crops_all_managements() < maximum_crop_shares(),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="factor of minimum crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"shares_of_crops_all_managements": 1},
)
def factor_of_minimum_crops():
    """
    factor to avoid changes of shares of crops that would lead to negative area assigned to a crop
    """
    return if_then_else(
        shares_of_crops_all_managements() > 0,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="gap availability of crops",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "mask_crops": 2,
        "land_products_available_all_regions": 2,
        "land_products_demanded_world": 4,
    },
)
def gap_availability_of_crops():
    """
    if it is greater than 0 excess of crops production, lower than zero, shortage
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: mask_crops()
        * zidz(
            land_products_available_all_regions() - land_products_demanded_world(),
            land_products_demanded_world(),
        ),
        lambda: mask_crops()
        * zidz(
            land_products_available_all_regions() - land_products_demanded_world(),
            land_products_demanded_world(),
        ),
    )


@component.add(
    name="gap global availability of crops",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "_smooth_gap_global_availability_of_crops": 1,
        "gap_availability_of_crops": 1,
    },
    other_deps={
        "_smooth_gap_global_availability_of_crops": {
            "initial": {"gap_availability_of_crops": 1},
            "step": {"gap_availability_of_crops": 1},
        }
    },
)
def gap_global_availability_of_crops():
    """
    Signal of crops availability at global level, all crops agregated. If it is greater than 0 excess of crops production
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: _smooth_gap_global_availability_of_crops(),
        lambda: sum(
            gap_availability_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
            dim=["LAND PRODUCTS I!"],
        )
        / len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        ),
    )


_smooth_gap_global_availability_of_crops = Smooth(
    lambda: sum(
        gap_availability_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    )
    / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
            ["LAND PRODUCTS I"],
        )
    ),
    lambda: 5,
    lambda: sum(
        gap_availability_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    )
    / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
            ["LAND PRODUCTS I"],
        )
    ),
    lambda: 1,
    "_smooth_gap_global_availability_of_crops",
)


@component.add(
    name="global availability of crops",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_global_availability_of_crops": 1},
    other_deps={
        "_smooth_global_availability_of_crops": {
            "initial": {
                "time": 1,
                "time_historical_data_land_module": 1,
                "availability_of_crops": 1,
            },
            "step": {
                "time": 1,
                "time_historical_data_land_module": 1,
                "availability_of_crops": 1,
            },
        }
    },
)
def global_availability_of_crops():
    """
    available/demanded equal to 1 means no shortage, less than one shortage
    """
    return _smooth_global_availability_of_crops()


_smooth_global_availability_of_crops = Smooth(
    lambda: if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: 1,
        lambda: sum(
            availability_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
            dim=["LAND PRODUCTS I!"],
        )
        / len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        ),
    ),
    lambda: 3,
    lambda: if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: 1,
        lambda: sum(
            availability_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
            dim=["LAND PRODUCTS I!"],
        )
        / len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        ),
    ),
    lambda: 1,
    "_smooth_global_availability_of_crops",
)


@component.add(
    name="global shortage of crops",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_global_shortage_of_crops": 1},
    other_deps={
        "_smooth_global_shortage_of_crops": {
            "initial": {"shortage_of_crops": 1},
            "step": {"shortage_of_crops": 1},
        }
    },
)
def global_shortage_of_crops():
    """
    indicator of shortage of all crops world level
    """
    return _smooth_global_shortage_of_crops()


_smooth_global_shortage_of_crops = Smooth(
    lambda: sum(
        shortage_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    )
    / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 4
    ),
    lambda: 4,
    lambda: sum(
        shortage_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    )
    / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 4
    ),
    lambda: 1,
    "_smooth_global_shortage_of_crops",
)


@component.add(
    name="historical area of crops all managements",
    units="km2",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_shares_of_crops_all_management": 1,
        "land_use_area_by_region": 2,
        "land_area_adjust_coefficient": 1,
    },
)
def historical_area_of_crops_all_managements():
    """
    historical area, FAO data only per region mixing irrigated and rainfed
    """
    return (
        historical_shares_of_crops_all_management(time())
        * (
            land_use_area_by_region().loc[:, "CROPLAND RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True)
        )
        * land_area_adjust_coefficient()
    )


@component.add(
    name="historical area of irrigated crops",
    units="km2",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_area_of_crops_all_management": 1,
        "share_of_irrigation_per_crop": 1,
    },
)
def historical_area_of_irrigated_crops():
    """
    Historical value of the area of each crop cultivated in irrigated land
    """
    return (
        historical_area_of_crops_all_management(time())
        * share_of_irrigation_per_crop().transpose("LAND PRODUCTS I", "REGIONS 9 I")
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="historical area of rainfed crops",
    units="km2",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_area_of_crops_all_management": 1,
        "share_of_irrigation_per_crop": 1,
    },
)
def historical_area_of_rainfed_crops():
    """
    Historical value of the area of each crop cultivated in rainfed cropland
    """
    return (
        historical_area_of_crops_all_management(time())
        * (1 - share_of_irrigation_per_crop()).transpose(
            "LAND PRODUCTS I", "REGIONS 9 I"
        )
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="historical change of shares of irrigated crops",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_share_of_irrigated_crops": 1,
        "historical_shares_irrigated_delayed": 1,
    },
)
def historical_change_of_shares_of_irrigated_crops():
    """
    historical change of crop area irrigated
    """
    return historical_share_of_irrigated_crops() - historical_shares_irrigated_delayed()


@component.add(
    name="historical change of shares rainfed crops",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_share_of_rainfed_crops": 1,
        "historical_shares_rainfed_delayed": 1,
    },
)
def historical_change_of_shares_rainfed_crops():
    """
    historical change of crop area rainfed
    """
    return historical_share_of_rainfed_crops() - historical_shares_rainfed_delayed()


@component.add(
    name="historical increase of shares of crops all managements",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_shares_of_crops_all_management": 1,
        "historical_shares_of_crops_delayed_all_managements": 1,
    },
)
def historical_increase_of_shares_of_crops_all_managements():
    """
    historical change of share of crop area
    """
    return (
        historical_shares_of_crops_all_management(time())
        - historical_shares_of_crops_delayed_all_managements().transpose(
            "LAND PRODUCTS I", "REGIONS 9 I"
        )
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="historical share of irrigated crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_area_of_irrigated_crops": 2},
)
def historical_share_of_irrigated_crops():
    """
    historical values of shares of irrigated crops
    """
    return zidz(
        historical_area_of_irrigated_crops(),
        sum(
            historical_area_of_irrigated_crops().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        ).expand_dims({"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1),
    )


@component.add(
    name="historical share of rainfed crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_area_of_rainfed_crops": 2},
)
def historical_share_of_rainfed_crops():
    """
    historical values of shares of rainfed crops
    """
    return zidz(
        historical_area_of_rainfed_crops(),
        sum(
            historical_area_of_rainfed_crops().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        ).expand_dims({"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1),
    )


@component.add(
    name="historical shares irrigated delayed",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_irrigated_delayed": 1},
    other_deps={
        "_delayfixed_historical_shares_irrigated_delayed": {
            "initial": {"initial_shares_of_irrigated_crops": 1},
            "step": {"historical_share_of_irrigated_crops": 1},
        }
    },
)
def historical_shares_irrigated_delayed():
    """
    aux historical values of shares of irrigated crops
    """
    return _delayfixed_historical_shares_irrigated_delayed()


_delayfixed_historical_shares_irrigated_delayed = DelayFixed(
    lambda: historical_share_of_irrigated_crops(),
    lambda: 1,
    lambda: initial_shares_of_irrigated_crops(),
    time_step,
    "_delayfixed_historical_shares_irrigated_delayed",
)


@component.add(
    name="historical shares of crops delayed all managements",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_of_crops_delayed_all_managements": 1},
    other_deps={
        "_delayfixed_historical_shares_of_crops_delayed_all_managements": {
            "initial": {"initial_shares_of_crops_all_managements": 1},
            "step": {"time": 1, "historical_shares_of_crops_all_management": 1},
        }
    },
)
def historical_shares_of_crops_delayed_all_managements():
    """
    aux historical shares of crops
    """
    return _delayfixed_historical_shares_of_crops_delayed_all_managements()


_delayfixed_historical_shares_of_crops_delayed_all_managements = DelayFixed(
    lambda: historical_shares_of_crops_all_management(time()).transpose(
        "REGIONS 9 I", "LAND PRODUCTS I"
    ),
    lambda: 1,
    lambda: initial_shares_of_crops_all_managements(),
    time_step,
    "_delayfixed_historical_shares_of_crops_delayed_all_managements",
)


@component.add(
    name="historical shares rainfed delayed",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_shares_rainfed_delayed": 1},
    other_deps={
        "_delayfixed_historical_shares_rainfed_delayed": {
            "initial": {"initial_shares_of_rainfed_crops": 1},
            "step": {"historical_share_of_rainfed_crops": 1},
        }
    },
)
def historical_shares_rainfed_delayed():
    """
    auxiliar, historical shares rainfed crops
    """
    return _delayfixed_historical_shares_rainfed_delayed()


_delayfixed_historical_shares_rainfed_delayed = DelayFixed(
    lambda: historical_share_of_rainfed_crops(),
    lambda: 1,
    lambda: initial_shares_of_rainfed_crops(),
    time_step,
    "_delayfixed_historical_shares_rainfed_delayed",
)


@component.add(
    name="increase of shares of crops all managements",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 10,
        "time_historical_data_land_module": 10,
        "historical_increase_of_shares_of_crops_all_managements": 10,
        "matrix_of_changes_of_crops_all_managements": 20,
    },
)
def increase_of_shares_of_crops_all_managements():
    """
    increase shares all managements
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "CEREALS OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "CEREALS OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "PULSES NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "PULSES NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "SUGAR CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "SUGAR CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "FRUITS VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "FRUITS VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = 0
    value.loc[:, ["OTHER CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_increase_of_shares_of_crops_all_managements()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, :, "OTHER CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_crops_all_managements()
                .loc[:, "OTHER CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="increase of shares of irrigated crops",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "historical_change_of_shares_of_irrigated_crops": 1,
        "increase_of_shares_of_irrigated_crops_aux": 1,
    },
)
def increase_of_shares_of_irrigated_crops():
    """
    increase of shares of irrigated crops
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: historical_change_of_shares_of_irrigated_crops(),
        lambda: increase_of_shares_of_irrigated_crops_aux(),
    )


@component.add(
    name="increase of shares of irrigated crops aux",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 11,
        "time_historical_data_land_module": 11,
        "historical_change_of_shares_of_irrigated_crops": 11,
        "matrix_of_changes_of_irrigated_crops": 22,
    },
)
def increase_of_shares_of_irrigated_crops_aux():
    """
    the matrix goes from taking share of LAND_PRODUCTS_I and sending it to LAND_PRODUCTS_MAP_I the ones that give to that use minus the ones that go from that use to others
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "CEREALS OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "CEREALS OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "PULSES NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "PULSES NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "SUGAR CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "SUGAR CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "FRUITS VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "FRUITS VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "BIOFUEL 2GCROP"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "BIOFUEL 2GCROP"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "BIOFUEL 2GCROP", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_of_irrigated_crops()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, :, "OTHER CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_irrigated_crops()
                .loc[:, "OTHER CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="increase of shares of rainfed crops",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"increase_of_shares_of_rainfed_crops_aux": 1},
)
def increase_of_shares_of_rainfed_crops():
    """
    increase of shares of rainfed crops
    """
    return increase_of_shares_of_rainfed_crops_aux()


@component.add(
    name="increase of shares of rainfed crops aux",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 11,
        "time_historical_data_land_module": 11,
        "historical_change_of_shares_rainfed_crops": 11,
        "matrix_of_changes_of_rainfed_crops": 22,
    },
)
def increase_of_shares_of_rainfed_crops_aux():
    """
    the matrix goes from taking share of LAND_PRODUCTS_I and sending it to LAND_PRODUCTS_MAP_I the ones that give to that use minus the ones that go from that use to others
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "CORN"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "CORN", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "RICE"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "RICE", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "CEREALS OTHER"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "CEREALS OTHER", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "TUBERS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "TUBERS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "SOY"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "SOY", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "PULSES NUTS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "PULSES NUTS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "OILCROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "OILCROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "SUGAR CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "SUGAR CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "FRUITS VEGETABLES"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "FRUITS VEGETABLES", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "BIOFUEL 2GCROP"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "BIOFUEL 2GCROP"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "BIOFUEL 2GCROP", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"]] = (
        if_then_else(
            time() < time_historical_data_land_module(),
            lambda: historical_change_of_shares_rainfed_crops()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True),
            lambda: sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, :, "OTHER CROPS"]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
                dim=["LAND PRODUCTS I!"],
            )
            - sum(
                matrix_of_changes_of_rainfed_crops()
                .loc[:, "OTHER CROPS", :]
                .reset_coords(drop=True)
                .rename({"LAND PRODUCTS MAP I": "LAND PRODUCTS MAP I!"}),
                dim=["LAND PRODUCTS MAP I!"],
            ),
        )
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="irrigated crops available by region",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_irrigated_crops": 1, "yields_of_irrigated_crops": 1},
)
def irrigated_crops_available_by_region():
    """
    Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return area_of_irrigated_crops() * yields_of_irrigated_crops()


@component.add(
    name="land products available from croplands",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_separate_irrigated_rainfed": 11,
        "crops_available_all_managements": 11,
        "irrigated_crops_available_by_region": 11,
        "rainfed_crops_available_by_region": 11,
        "residues_available_from_crops": 1,
    },
)
def land_products_available_from_croplands():
    """
    Land products produced from all croplands
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    value.loc[:, ["CORN"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "CORN"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "CORN"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "RICE"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "RICE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "CEREALS OTHER"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "TUBERS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "SOY"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "SOY"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region().loc[:, "SOY"].reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "PULSES NUTS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "OILCROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "SUGAR CROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "FRUITS VEGETABLES"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "BIOFUEL 2GCROP"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "BIOFUEL 2GCROP"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "BIOFUEL 2GCROP"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"]] = (
        if_then_else(
            switch_separate_irrigated_rainfed() == 1,
            lambda: crops_available_all_managements()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True),
            lambda: irrigated_crops_available_by_region()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True)
            + rainfed_crops_available_by_region()
            .loc[:, "OTHER CROPS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = (
        residues_available_from_crops()
        .expand_dims({"LAND PRODUCTS I": ["RESIDUES"]}, 1)
        .values
    )
    return value


@component.add(
    name="matrix of changes of crops all managements",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_of_minimum_crops": 1,
        "parameter_of_crop_share_change": 1,
        "factor_of_maximum_crops": 1,
    },
)
def matrix_of_changes_of_crops_all_managements():
    """
    matrix that governs the changes of share of existing cropland from one crop to another driven by relative deamnd of each crop. Crops area adjusts in each time interval to match demand
    """
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND PRODUCTS I": "LAND PRODUCTS MAP I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND PRODUCTS I", "LAND PRODUCTS MAP I")
            * factor_of_minimum_crops().transpose("LAND PRODUCTS I", "REGIONS 9 I")
            * factor_of_maximum_crops()
            .rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            .transpose("LAND PRODUCTS MAP I", "REGIONS 9 I")
        ).transpose("LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND PRODUCTS MAP I": _subscript_dict["LAND PRODUCTS MAP I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"],
        ),
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I")


@component.add(
    name="matrix of changes of irrigated crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_maximum_irrigated": 1,
        "parameter_of_crop_share_change": 1,
        "factor_minimum_irrigated": 1,
    },
)
def matrix_of_changes_of_irrigated_crops():
    """
    atrix that governs the changes of share of existing irrigated cropland from one crop to another driven by relative deamnd of each crop
    """
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND PRODUCTS I": "LAND PRODUCTS MAP I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND PRODUCTS I", "LAND PRODUCTS MAP I")
            * factor_minimum_irrigated().transpose("LAND PRODUCTS I", "REGIONS 9 I")
            * factor_maximum_irrigated()
            .rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            .transpose("LAND PRODUCTS MAP I", "REGIONS 9 I")
        ).transpose("LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND PRODUCTS MAP I": _subscript_dict["LAND PRODUCTS MAP I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"],
        ),
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I")


@component.add(
    name="matrix of changes of rainfed crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ratio_shortage_of_crops": 4,
        "factor_minimum_rainfed": 1,
        "parameter_of_crop_share_change": 1,
        "factor_maximum_rainfed_crops": 1,
    },
)
def matrix_of_changes_of_rainfed_crops():
    """
    matrix that governs the changes of share of existing rainfed cropland from one crop to another driven by relative deamnd of each crop IF_THEN_ELSE( ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]>ratio_availability_of_crop s[LAND_PRODUCTS_I], PARAMETER_OF_CROP_SHARE_CHANGE*(ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]-rati o_availability_of_crops[LAND_PRODUCTS_I ])*factor_minimum_rainfed[REGIONS_9_I,LAND_PRODUCTS_I]*(factor_maximum_rainfed_crops[ REGIONS_9_I,LAND_PRODUCTS_MAP_I]), PARAMETER_OF_CROP_SHARE_CHANGE*(-ratio_availability_of_crops[LAND_PRODUCTS_MAP_I]+rat io_availability_of_crops[LAND_PRODUCTS_I ])*factor_minimum_rainfed[REGIONS_9_I,LAND_PRODUCTS_MAP_I]*(factor_maximum_ rainfed_crops[REGIONS_9_I,LAND_PRODUCTS_I]) )
    """
    return if_then_else(
        (
            ratio_shortage_of_crops().rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            > ratio_shortage_of_crops()
        ).expand_dims({"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 2),
        lambda: (
            parameter_of_crop_share_change()
            * (
                ratio_shortage_of_crops().rename(
                    {"LAND PRODUCTS I": "LAND PRODUCTS MAP I"}
                )
                - ratio_shortage_of_crops()
            ).transpose("LAND PRODUCTS I", "LAND PRODUCTS MAP I")
            * factor_minimum_rainfed().transpose("LAND PRODUCTS I", "REGIONS 9 I")
            * factor_maximum_rainfed_crops()
            .rename({"LAND PRODUCTS I": "LAND PRODUCTS MAP I"})
            .transpose("LAND PRODUCTS MAP I", "REGIONS 9 I")
        ).transpose("LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND PRODUCTS MAP I": _subscript_dict["LAND PRODUCTS MAP I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["LAND PRODUCTS MAP I", "LAND PRODUCTS I", "REGIONS 9 I"],
        ),
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I", "LAND PRODUCTS MAP I")


@component.add(
    name="parameter of crop share change",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"mask_crops": 1},
)
def parameter_of_crop_share_change():
    return 0.01 * mask_crops()


@component.add(
    name="rainfed crops available by region",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_of_rainfed_crops": 1, "yields_of_rainfed_crops": 1},
)
def rainfed_crops_available_by_region():
    """
    Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return area_of_rainfed_crops() * yields_of_rainfed_crops()


@component.add(
    name="ratio shortage of crops",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mask_crops": 1,
        "land_products_demanded_world": 2,
        "land_products_available_all_regions": 1,
    },
)
def ratio_shortage_of_crops():
    """
    If =1 demand of land product equals production >1 shortage <1 excess of production
    """
    return if_then_else(
        np.logical_and(mask_crops() == 1, land_products_demanded_world() > 20),
        lambda: zidz(
            land_products_demanded_world(), land_products_available_all_regions()
        ),
        lambda: xr.DataArray(
            0,
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
            ["LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="residues available from crops",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_separate_irrigated_rainfed": 1,
        "share_of_residuals_from_crops": 2,
        "crops_available_all_managements": 1,
        "irrigated_crops_available_by_region": 1,
        "rainfed_crops_available_by_region": 1,
    },
)
def residues_available_from_crops():
    """
    not active
    """
    return if_then_else(
        switch_separate_irrigated_rainfed() == 1,
        lambda: sum(
            crops_available_all_managements().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        )
        * share_of_residuals_from_crops(),
        lambda: (
            sum(
                rainfed_crops_available_by_region().rename(
                    {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
                ),
                dim=["LAND PRODUCTS I!"],
            )
            + sum(
                irrigated_crops_available_by_region().rename(
                    {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
                ),
                dim=["LAND PRODUCTS I!"],
            )
        )
        * share_of_residuals_from_crops(),
    )


@component.add(
    name="share of irrigation per crop",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "initial_share_of_irrigation": 1},
)
def share_of_irrigation_per_crop():
    """
    Share of area of each crop that is cultivated in irrigated area. Value obtained from historical data.
    """
    return initial_share_of_irrigation(time()).transpose(
        "REGIONS 9 I", "LAND PRODUCTS I"
    )


@component.add(
    name="shares of crops all managements",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_crops_all_managements": 1},
    other_deps={
        "_integ_shares_of_crops_all_managements": {
            "initial": {"initial_shares_of_crops_all_managements": 1},
            "step": {"increase_of_shares_of_crops_all_managements": 1},
        }
    },
)
def shares_of_crops_all_managements():
    """
    shares of crops relative to existing rainfed+irrigated cropland area. Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=1
    """
    return _integ_shares_of_crops_all_managements()


_integ_shares_of_crops_all_managements = Integ(
    lambda: increase_of_shares_of_crops_all_managements(),
    lambda: initial_shares_of_crops_all_managements(),
    "_integ_shares_of_crops_all_managements",
)


@component.add(
    name="shares of irrigated crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_irrigated_crops": 1},
    other_deps={
        "_integ_shares_of_irrigated_crops": {
            "initial": {"initial_shares_of_irrigated_crops": 1},
            "step": {"increase_of_shares_of_irrigated_crops": 1},
        }
    },
)
def shares_of_irrigated_crops():
    """
    shares of irrigated crops relative to existing irrigated cropland area . Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return _integ_shares_of_irrigated_crops()


_integ_shares_of_irrigated_crops = Integ(
    lambda: increase_of_shares_of_irrigated_crops(),
    lambda: initial_shares_of_irrigated_crops(),
    "_integ_shares_of_irrigated_crops",
)


@component.add(
    name="shares of rainfed crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_shares_of_rainfed_crops": 1},
    other_deps={
        "_integ_shares_of_rainfed_crops": {
            "initial": {"initial_shares_of_rainfed_crops": 1},
            "step": {"increase_of_shares_of_rainfed_crops": 1},
        }
    },
)
def shares_of_rainfed_crops():
    """
    shares of rainfed crops relative to existing rainfed cropland area. Only valid if SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return _integ_shares_of_rainfed_crops()


_integ_shares_of_rainfed_crops = Integ(
    lambda: increase_of_shares_of_rainfed_crops(),
    lambda: initial_shares_of_rainfed_crops(),
    "_integ_shares_of_rainfed_crops",
)


@component.add(
    name="shortage of crops",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_shortage_of_crops": 1},
    other_deps={
        "_smooth_shortage_of_crops": {
            "initial": {"time": 1, "aux_shortage_crops": 1},
            "step": {"time": 1, "aux_shortage_crops": 1},
        }
    },
)
def shortage_of_crops():
    """
    shortage_of_crops
    """
    return _smooth_shortage_of_crops()


_smooth_shortage_of_crops = Smooth(
    lambda: if_then_else(
        time() > 2020,
        lambda: aux_shortage_crops(),
        lambda: xr.DataArray(
            0,
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
            ["LAND PRODUCTS I"],
        ),
    ),
    lambda: xr.DataArray(
        3, {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, ["LAND PRODUCTS I"]
    ),
    lambda: if_then_else(
        time() > 2020,
        lambda: aux_shortage_crops(),
        lambda: xr.DataArray(
            0,
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
            ["LAND PRODUCTS I"],
        ),
    ),
    lambda: 1,
    "_smooth_shortage_of_crops",
)


@component.add(
    name="SWITCH SEPARATE IRRIGATED RAINFED",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_separate_irrigated_rainfed"},
)
def switch_separate_irrigated_rainfed():
    """
    =1: crops production and yields are calculated NOT separating irrigated and rainfed crops =0: crops production and yields are calculated separating irrigated and rainfed crops, in this case irrigated and rainfed yields are stimated
    """
    return _ext_constant_switch_separate_irrigated_rainfed()


_ext_constant_switch_separate_irrigated_rainfed = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_SEPARATE_IRRIGATED_RAINFED",
    {},
    _root,
    {},
    "_ext_constant_switch_separate_irrigated_rainfed",
)
