"""
Module land_and_waterland.diets
Translated using PySD version 3.14.0
"""

@component.add(
    name="dairy obtained from grasslands",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_dairy_obtained_from_grasslands": 1,
        "initial_land_use_by_region": 1,
        "land_use_area_by_region": 1,
        "factor_of_grassland_production": 1,
    },
)
def dairy_obtained_from_grasslands():
    """
    Dairy obtained directly from grasslands and not from products obtained from crops,
    """
    return (
        initial_dairy_obtained_from_grasslands()
        * zidz(
            land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
            initial_land_use_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
        )
        * factor_of_grassland_production()
    )


@component.add(
    name="diet according to food shortage",
    units="kg/(person*Year)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gdppc_per_share_of_available_food": 9,
        "diet_patterns_data_by_gdppc_for_eu": 1,
        "diet_patterns_data_by_gdppc_for_uk": 1,
        "diet_patterns_data_by_gdppc_for_china": 1,
        "diet_patterns_data_by_gdppc_for_easoc": 1,
        "diet_patterns_data_by_gdppc_for_india": 1,
        "diet_patterns_data_by_gdppc_for_latam": 1,
        "diet_patterns_data_by_gdppc_for_russia": 1,
        "diet_patterns_data_by_gdppc_for_usmca": 1,
        "diet_patterns_data_by_gdppc_for_lrow": 1,
    },
)
def diet_according_to_food_shortage():
    """
    diet patterns according to GDPpc
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "FOODS I": _subscript_dict["FOODS I"],
        },
        ["REGIONS 9 I", "FOODS I"],
    )
    value.loc[["EU27"], :] = (
        diet_patterns_data_by_gdppc_for_eu(
            float(gdppc_per_share_of_available_food().loc["EU27"])
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :] = (
        diet_patterns_data_by_gdppc_for_uk(
            float(gdppc_per_share_of_available_food().loc["UK"])
        )
        .expand_dims({"REGIONS 35 I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :] = (
        diet_patterns_data_by_gdppc_for_china(
            float(gdppc_per_share_of_available_food().loc["CHINA"])
        )
        .expand_dims({"REGIONS 35 I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :] = (
        diet_patterns_data_by_gdppc_for_easoc(
            float(gdppc_per_share_of_available_food().loc["EASOC"])
        )
        .expand_dims({"REGIONS 35 I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :] = (
        diet_patterns_data_by_gdppc_for_india(
            float(gdppc_per_share_of_available_food().loc["INDIA"])
        )
        .expand_dims({"REGIONS 35 I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :] = (
        diet_patterns_data_by_gdppc_for_latam(
            float(gdppc_per_share_of_available_food().loc["LATAM"])
        )
        .expand_dims({"REGIONS 35 I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :] = (
        diet_patterns_data_by_gdppc_for_russia(
            float(gdppc_per_share_of_available_food().loc["RUSSIA"])
        )
        .expand_dims({"REGIONS 35 I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :] = (
        diet_patterns_data_by_gdppc_for_usmca(
            float(gdppc_per_share_of_available_food().loc["USMCA"])
        )
        .expand_dims({"REGIONS 35 I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :] = (
        diet_patterns_data_by_gdppc_for_lrow(
            float(gdppc_per_share_of_available_food().loc["LROW"])
        )
        .expand_dims({"REGIONS 35 I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="diet according to policies sp",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_diets": 1,
        "select_policy_diet_patterns_sp": 5,
        "plant_based_50_percent_diet_pattern_of_policy_diets_sp": 1,
        "willett_diet_patterns_of_policy_diets_sp": 1,
        "baseline_diet_pattern_of_policy_diets_sp": 1,
        "plant_based_100_diet_pattern_of_policy_diets_sp": 1,
        "flexitariana_diet_patterns_of_policy_diets_sp": 1,
    },
)
def diet_according_to_policies_sp():
    """
    Diet patterns according to the proposed policies
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_diets(),
        lambda: if_then_else(
            select_policy_diet_patterns_sp() == 0,
            lambda: flexitariana_diet_patterns_of_policy_diets_sp(),
            lambda: if_then_else(
                select_policy_diet_patterns_sp() == 1,
                lambda: willett_diet_patterns_of_policy_diets_sp(),
                lambda: if_then_else(
                    select_policy_diet_patterns_sp() == 2,
                    lambda: baseline_diet_pattern_of_policy_diets_sp(),
                    lambda: if_then_else(
                        select_policy_diet_patterns_sp() == 3,
                        lambda: plant_based_50_percent_diet_pattern_of_policy_diets_sp(),
                        lambda: if_then_else(
                            select_policy_diet_patterns_sp() == 4,
                            lambda: plant_based_100_diet_pattern_of_policy_diets_sp(),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                    "FOODS I": _subscript_dict["FOODS I"],
                                },
                                ["REGIONS 9 I", "FOODS I"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="diet available",
    units="kg/(Year*person)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "diet_demanded": 1,
        "select_policy_diet_patterns_sp": 1,
        "diet_according_to_food_shortage": 3,
        "diet_according_to_policies_sp": 1,
        "share_of_change_to_policy_diet": 2,
        "switch_model_explorer": 2,
        "efect_shortage_of_policy_diet": 1,
        "select_tipe_diets_me": 1,
    },
)
def diet_available():
    """
    Diet patterns of households it is the diet achievable with and without lack of crops production
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: diet_demanded(),
        lambda: if_then_else(
            np.logical_and(switch_model_explorer() == 1, select_tipe_diets_me() == 2),
            lambda: diet_according_to_food_shortage(),
            lambda: if_then_else(
                np.logical_and(
                    switch_model_explorer() == 0, select_policy_diet_patterns_sp() == 2
                ),
                lambda: diet_according_to_food_shortage(),
                lambda: diet_according_to_policies_sp()
                * share_of_change_to_policy_diet()
                * efect_shortage_of_policy_diet()
                + diet_according_to_food_shortage()
                * (1 - share_of_change_to_policy_diet()),
            ),
        ),
    )


@component.add(
    name="diet demanded",
    units="kg/(Year*person)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 2,
        "select_tipe_diets_me": 1,
        "diet_demanded_according_to_gdppc": 3,
        "select_policy_diet_patterns_sp": 1,
        "share_of_change_to_policy_diet": 2,
        "diet_according_to_policies_sp": 1,
    },
)
def diet_demanded():
    """
    Diet patterns of households according to GDPpc and policies, it is the diet demanded, that might not be achievable due to lack of crops production
    """
    return if_then_else(
        np.logical_and(switch_model_explorer() == 1, select_tipe_diets_me() == 2),
        lambda: diet_demanded_according_to_gdppc(),
        lambda: if_then_else(
            np.logical_and(
                switch_model_explorer() == 0, select_policy_diet_patterns_sp() == 2
            ),
            lambda: diet_demanded_according_to_gdppc(),
            lambda: diet_according_to_policies_sp() * share_of_change_to_policy_diet()
            + diet_demanded_according_to_gdppc()
            * (1 - share_of_change_to_policy_diet()),
        ),
    )


@component.add(
    name="diet demanded according to GDPpc",
    units="kg/(person*Year)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gdppc_9r_for_diets": 9,
        "diet_patterns_data_by_gdppc_for_eu": 1,
        "diet_patterns_data_by_gdppc_for_uk": 1,
        "diet_patterns_data_by_gdppc_for_china": 1,
        "diet_patterns_data_by_gdppc_for_easoc": 1,
        "diet_patterns_data_by_gdppc_for_india": 1,
        "diet_patterns_data_by_gdppc_for_latam": 1,
        "diet_patterns_data_by_gdppc_for_russia": 1,
        "diet_patterns_data_by_gdppc_for_usmca": 1,
        "diet_patterns_data_by_gdppc_for_lrow": 1,
    },
)
def diet_demanded_according_to_gdppc():
    """
    diet patterns according to GDPpc
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "FOODS I": _subscript_dict["FOODS I"],
        },
        ["REGIONS 9 I", "FOODS I"],
    )
    value.loc[["EU27"], :] = (
        diet_patterns_data_by_gdppc_for_eu(float(gdppc_9r_for_diets().loc["EU27"]))
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :] = (
        diet_patterns_data_by_gdppc_for_uk(float(gdppc_9r_for_diets().loc["UK"]))
        .expand_dims({"REGIONS 35 I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :] = (
        diet_patterns_data_by_gdppc_for_china(float(gdppc_9r_for_diets().loc["CHINA"]))
        .expand_dims({"REGIONS 35 I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :] = (
        diet_patterns_data_by_gdppc_for_easoc(float(gdppc_9r_for_diets().loc["EASOC"]))
        .expand_dims({"REGIONS 35 I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :] = (
        diet_patterns_data_by_gdppc_for_india(float(gdppc_9r_for_diets().loc["INDIA"]))
        .expand_dims({"REGIONS 35 I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :] = (
        diet_patterns_data_by_gdppc_for_latam(float(gdppc_9r_for_diets().loc["LATAM"]))
        .expand_dims({"REGIONS 35 I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :] = (
        diet_patterns_data_by_gdppc_for_russia(
            float(gdppc_9r_for_diets().loc["RUSSIA"])
        )
        .expand_dims({"REGIONS 35 I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :] = (
        diet_patterns_data_by_gdppc_for_usmca(float(gdppc_9r_for_diets().loc["USMCA"]))
        .expand_dims({"REGIONS 35 I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :] = (
        diet_patterns_data_by_gdppc_for_lrow(float(gdppc_9r_for_diets().loc["LROW"]))
        .expand_dims({"REGIONS 35 I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="efect shortage of policy diet",
    units="DMNL",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_available_crops_for_food": 33},
)
def efect_shortage_of_policy_diet():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "FOODS I": _subscript_dict["FOODS I"],
        },
        ["REGIONS 9 I", "FOODS I"],
    )
    value.loc[:, ["CEREALS DIET"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "RICE"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
            )
            / 3
        )
        .expand_dims({"FOODS I": ["CEREALS DIET"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS DIET"]] = (
        share_of_available_crops_for_food()
        .loc[:, "TUBERS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["TUBERS DIET"]}, 1)
        .values
    )
    value.loc[:, ["PULSES LEGUMES NUTS"]] = (
        share_of_available_crops_for_food()
        .loc[:, "PULSES NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["PULSES LEGUMES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES DIET"]] = (
        share_of_available_crops_for_food()
        .loc[:, "FRUITS VEGETABLES"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["FRUITS VEGETABLES DIET"]}, 1)
        .values
    )
    value.loc[:, ["FATS VEGETAL"]] = (
        share_of_available_crops_for_food()
        .loc[:, "OILCROPS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["FATS VEGETAL"]}, 1)
        .values
    )
    value.loc[:, ["FATS ANIMAL"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS I": ["FATS ANIMAL"]}, 1)
        .values
    )
    value.loc[:, ["DAIRY"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS I": ["DAIRY"]}, 1)
        .values
    )
    value.loc[:, ["EGGS"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS I": ["EGGS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT RUMINANTS"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS I": ["MEAT RUMINANTS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT MONOGASTRIC"]] = (
        (
            (
                share_of_available_crops_for_food()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
                + share_of_available_crops_for_food()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            / 5
        )
        .expand_dims({"FOODS I": ["MEAT MONOGASTRIC"]}, 1)
        .values
    )
    value.loc[:, ["FISH"]] = 1
    value.loc[:, ["SUGARS"]] = (
        share_of_available_crops_for_food()
        .loc[:, "SUGAR CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["SUGARS"]}, 1)
        .values
    )
    value.loc[:, ["BEVERAGES"]] = 1
    value.loc[:, ["STIMULANTS"]] = 1
    return value


@component.add(
    name="exo GDPpc 9R exogenous",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_exogenous_gdppc_9r": 1},
)
def exo_gdppc_9r_exogenous():
    """
    exogenous value of GDP per capita used when the Land and water module is disconnected from the rest of WILIAM model
    """
    return exo_exogenous_gdppc_9r(time())


@component.add(
    name="food demanded by households per region",
    units="t/Year",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded": 1,
        "population_9_regions_for_diets": 1,
        "unit_conversion_t_kg": 1,
    },
)
def food_demanded_by_households_per_region():
    """
    tonnes of food demanded by region
    """
    return diet_demanded() * population_9_regions_for_diets() * unit_conversion_t_kg()


@component.add(
    name="food demanded from land products",
    units="t/Year",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "food_demanded_by_households_per_region": 13,
        "dairy_obtained_from_grasslands": 1,
        "meat_obtained_from_grasslands": 1,
    },
)
def food_demanded_from_land_products():
    """
    diets of households by regions and without meat and dairy from grasslands and without fish
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "FOODS I": _subscript_dict["FOODS I"],
        },
        ["REGIONS 9 I", "FOODS I"],
    )
    value.loc[:, ["CEREALS DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "CEREALS DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["CEREALS DIET"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "TUBERS DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["TUBERS DIET"]}, 1)
        .values
    )
    value.loc[:, ["PULSES LEGUMES NUTS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "PULSES LEGUMES NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["PULSES LEGUMES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES DIET"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FRUITS VEGETABLES DIET"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["FRUITS VEGETABLES DIET"]}, 1)
        .values
    )
    value.loc[:, ["FATS VEGETAL"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FATS VEGETAL"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["FATS VEGETAL"]}, 1)
        .values
    )
    value.loc[:, ["FATS ANIMAL"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "FATS ANIMAL"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["FATS ANIMAL"]}, 1)
        .values
    )
    value.loc[:, ["DAIRY"]] = (
        np.maximum(
            0,
            food_demanded_by_households_per_region()
            .loc[:, "DAIRY"]
            .reset_coords(drop=True)
            - dairy_obtained_from_grasslands(),
        )
        .expand_dims({"FOODS I": ["DAIRY"]}, 1)
        .values
    )
    value.loc[:, ["EGGS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "EGGS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["EGGS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT RUMINANTS"]] = (
        np.maximum(
            0,
            food_demanded_by_households_per_region()
            .loc[:, "MEAT RUMINANTS"]
            .reset_coords(drop=True)
            - meat_obtained_from_grasslands(),
        )
        .expand_dims({"FOODS I": ["MEAT RUMINANTS"]}, 1)
        .values
    )
    value.loc[:, ["MEAT MONOGASTRIC"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "MEAT MONOGASTRIC"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["MEAT MONOGASTRIC"]}, 1)
        .values
    )
    value.loc[:, ["FISH"]] = 0
    value.loc[:, ["SUGARS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "SUGARS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["SUGARS"]}, 1)
        .values
    )
    value.loc[:, ["BEVERAGES"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "BEVERAGES"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["BEVERAGES"]}, 1)
        .values
    )
    value.loc[:, ["STIMULANTS"]] = (
        food_demanded_by_households_per_region()
        .loc[:, "STIMULANTS"]
        .reset_coords(drop=True)
        .expand_dims({"FOODS I": ["STIMULANTS"]}, 1)
        .values
    )
    return value


@component.add(
    name="food demanded world",
    units="t/Year",
    subscripts=["FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"food_demanded_by_households_per_region": 1},
)
def food_demanded_world():
    """
    Food products demanded all world
    """
    return sum(
        food_demanded_by_households_per_region().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="GDPpc 9R for diets",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "time": 1,
        "time_historical_data_land_module": 1,
        "exo_gdppc_9r_exogenous": 1,
        "gdppc_9r_real": 1,
    },
)
def gdppc_9r_for_diets():
    """
    GDP per capita used in the diets submodule
    """
    return if_then_else(
        np.logical_or(
            switch_landwater() == 0, time() < time_historical_data_land_module()
        ),
        lambda: exo_gdppc_9r_exogenous(),
        lambda: gdppc_9r_real(),
    )


@component.add(
    name="GDPpc per share of available food",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdppc_9r_for_diets": 1, "share_of_available_food": 1},
)
def gdppc_per_share_of_available_food():
    """
    Ratio of GDP according to food shortage
    """
    return gdppc_9r_for_diets() * share_of_available_food()


@component.add(
    name="increase of share of change to policy diet",
    units="1/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_objective_diets": 1,
        "year_final_diet_change_sp": 2,
        "switch_diet_change_sp": 2,
        "objective_diet_change_sp": 1,
        "time": 2,
        "year_initial_diet_change_sp": 2,
    },
)
def increase_of_share_of_change_to_policy_diet():
    """
    The variation of share of change to policy diet
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: xr.DataArray(
            model_explorer_objective_diets(),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: if_then_else(
            switch_diet_change_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_diet_change_sp() == 1,
                    np.logical_or(
                        time() < year_initial_diet_change_sp(),
                        time() > year_final_diet_change_sp(),
                    ),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: objective_diet_change_sp()
                / (year_final_diet_change_sp() - year_initial_diet_change_sp()),
            ),
        ),
    )


@component.add(
    name="land products demanded for food",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_for_food_before_losses": 1,
        "loss_factor_of_land_products": 1,
    },
)
def land_products_demanded_for_food():
    """
    Land prodcuts (crops mainly) demanded for food
    """
    return (
        land_products_demanded_for_food_before_losses() * loss_factor_of_land_products()
    )


@component.add(
    name="land products demanded for food before losses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "agrofood_transform_matrix": 14,
        "food_demanded_from_land_products": 14,
    },
)
def land_products_demanded_for_food_before_losses():
    """
    calculation of land products demanded for food by using the Agrofood matrix
    """
    return (
        agrofood_transform_matrix().loc["CEREALS DIET", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "CEREALS DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["TUBERS DIET", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "TUBERS DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix()
        .loc["PULSES LEGUMES NUTS", :]
        .reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "PULSES LEGUMES NUTS"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix()
        .loc["FRUITS VEGETABLES DIET", :]
        .reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FRUITS VEGETABLES DIET"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FATS VEGETAL", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FATS VEGETAL"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FATS ANIMAL", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "FATS ANIMAL"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["DAIRY", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "DAIRY"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["EGGS", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "EGGS"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["MEAT RUMINANTS", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "MEAT RUMINANTS"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["MEAT MONOGASTRIC", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "MEAT MONOGASTRIC"]
        .reset_coords(drop=True)
        + agrofood_transform_matrix().loc["FISH", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "FISH"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["SUGARS", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "SUGARS"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["BEVERAGES", :].reset_coords(drop=True)
        * food_demanded_from_land_products().loc[:, "BEVERAGES"].reset_coords(drop=True)
        + agrofood_transform_matrix().loc["STIMULANTS", :].reset_coords(drop=True)
        * food_demanded_from_land_products()
        .loc[:, "STIMULANTS"]
        .reset_coords(drop=True)
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="land products demanded for food delayed",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_land_products_demanded_for_food_delayed": 1},
    other_deps={
        "_delayfixed_land_products_demanded_for_food_delayed": {
            "initial": {"historical_land_products_production": 1},
            "step": {"land_products_demanded_for_food_before_losses": 1},
        }
    },
)
def land_products_demanded_for_food_delayed():
    """
    delayed variable of land products demanded for food
    """
    return _delayfixed_land_products_demanded_for_food_delayed()


_delayfixed_land_products_demanded_for_food_delayed = DelayFixed(
    lambda: land_products_demanded_for_food_before_losses(),
    lambda: 1,
    lambda: historical_land_products_production(),
    time_step,
    "_delayfixed_land_products_demanded_for_food_delayed",
)


@component.add(
    name="land products demanded for food world",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food": 1},
)
def land_products_demanded_for_food_world():
    """
    Land products demanded for food all world
    """
    return sum(
        land_products_demanded_for_food().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="meat obtained from grasslands",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_meat_obtained_from_grasslands": 1,
        "initial_land_use_by_region": 1,
        "land_use_area_by_region": 1,
        "factor_of_grassland_production": 1,
    },
)
def meat_obtained_from_grasslands():
    """
    Meat obtained directly from grasslands and not from products obtained from crops,
    """
    return (
        initial_meat_obtained_from_grasslands()
        * zidz(
            land_use_area_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
            initial_land_use_by_region().loc[:, "GRASSLAND"].reset_coords(drop=True),
        )
        * factor_of_grassland_production()
    )


@component.add(
    name="PLANT BASED 50 PERCENT DIET PATTERN OF POLICY DIETS SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp"
    },
)
def plant_based_50_percent_diet_pattern_of_policy_diets_sp():
    """
    50% plant based policy diet
    """
    return _ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp()


_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PLANT_BASED_50_PERCENT_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_plant_based_50_percent_diet_pattern_of_policy_diets_sp",
)


@component.add(
    name="population 9 regions for diets",
    units="people",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "time": 1,
        "exogenous_population_9r": 1,
        "population_9_regions": 1,
    },
)
def population_9_regions_for_diets():
    """
    Population constant values with variation during time for 9 regions
    """
    return if_then_else(
        switch_landwater() == 0,
        lambda: exogenous_population_9r(time()),
        lambda: population_9_regions(),
    )


@component.add(
    name="SELECT POLICY DIET PATTERNS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_policy_diet_patterns_sp"},
)
def select_policy_diet_patterns_sp():
    """
    0: APPLICATION OF FLEXITARIANA_DIET_PATTERNS 1: APPLICATION OF WILLET_DIET_PATTERNS 2: APPLICATION OF BASELINE_DIET_PATTERNS 3: APPLICATION OF PLANT_BASED_50_DIET_PATTERNS 4: APPLICATION OF PLANT_BASED_100_DIET_PATTERN
    """
    return _ext_constant_select_policy_diet_patterns_sp()


_ext_constant_select_policy_diet_patterns_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_DIET_PATTERNS_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_policy_diet_patterns_sp",
)


@component.add(
    name="share of available crops for food",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mask_essential_foods": 1,
        "land_products_demanded_for_food_delayed": 1,
        "crops_available_for_food": 1,
    },
)
def share_of_available_crops_for_food():
    """
    Auxiliar variable of food shortage feedback
    """
    return if_then_else(
        (mask_essential_foods() == 1).expand_dims(
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 1
        ),
        lambda: np.minimum(
            1,
            zidz(crops_available_for_food(), land_products_demanded_for_food_delayed()),
        ).transpose("LAND PRODUCTS I", "REGIONS 9 I"),
        lambda: xr.DataArray(
            0,
            {
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["LAND PRODUCTS I", "REGIONS 9 I"],
        ),
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="share of available food",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_available_crops_for_food": 1, "mask_essential_foods": 1},
)
def share_of_available_food():
    """
    >1 means food abundance, more that demanded
    """
    return sum(
        share_of_available_crops_for_food().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / sum(
        mask_essential_foods().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    )


@component.add(
    name="share of change to policy diet",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_change_to_policy_diet": 1},
    other_deps={
        "_integ_share_of_change_to_policy_diet": {
            "initial": {"share_of_change_to_policy_diet_initial_value_sp": 1},
            "step": {"increase_of_share_of_change_to_policy_diet": 1},
        }
    },
)
def share_of_change_to_policy_diet():
    """
    The share of change to policy diet =0 means that the diet is not influenced by policies of fiet change =1 the policy diet is fully implemented
    """
    return _integ_share_of_change_to_policy_diet()


_integ_share_of_change_to_policy_diet = Integ(
    lambda: increase_of_share_of_change_to_policy_diet(),
    lambda: share_of_change_to_policy_diet_initial_value_sp(),
    "_integ_share_of_change_to_policy_diet",
)
