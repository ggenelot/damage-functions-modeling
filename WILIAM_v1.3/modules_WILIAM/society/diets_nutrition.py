"""
Module society.diets_nutrition
Translated using PySD version 3.14.0
"""

@component.add(
    name="daily nutritional energy intake",
    units="kcal/(person*day)",
    subscripts=["REGIONS 9 I", "NUTRITION I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"daily_nutritional_intake_energy_by_food_product": 1},
)
def daily_nutritional_energy_intake():
    """
    Daily nutritional energy intake by region and nutrion factor
    """
    return sum(
        daily_nutritional_intake_energy_by_food_product().rename(
            {"FOODS I": "FOODS I!"}
        ),
        dim=["FOODS I!"],
    ).expand_dims({"NUTRITION I": ["ENERGY"]}, 1)


@component.add(
    name="daily nutritional intake energy by food product",
    units="kcal/(person*day)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_after_food_losses": 1,
        "unit_conversion_g_kg": 1,
        "kcal_in_edible_portion_by_100_g": 1,
        "unit_conversion_days_year": 1,
        "food_composition_table_energy": 1,
    },
)
def daily_nutritional_intake_energy_by_food_product():
    """
    Nutritional intake of energy of nutritional assessment. Units are different across categories (1000/365/100) --> 1000 g per kg; 365 days per year; 100 g of reference in food composition table
    """
    return (
        diet_after_food_losses()
        * (
            unit_conversion_g_kg()
            / unit_conversion_days_year()
            / kcal_in_edible_portion_by_100_g()
        )
        * food_composition_table_energy()
    )


@component.add(
    name="daily nutritional intake mass by food product",
    units="g/(person*day)",
    subscripts=["REGIONS 9 I", "FOODS I", "NUTRITION MASS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_after_food_losses": 1,
        "unit_conversion_g_kg": 1,
        "unit_conversion_days_year": 1,
        "edible_portion_by_100_g": 1,
        "food_composition_table_mass": 1,
    },
)
def daily_nutritional_intake_mass_by_food_product():
    """
    Nutritional intake of mass by category of nutritional assessment. Units are different across categories (1000/365/100) --> 1000 g per kg; 365 days per year; 100 g of reference in food composition table
    """
    return (
        diet_after_food_losses()
        * (
            unit_conversion_g_kg()
            / unit_conversion_days_year()
            / edible_portion_by_100_g()
        )
        * food_composition_table_mass()
    )


@component.add(
    name="daily nutrutional mass intake",
    units="g/(person*day)",
    subscripts=["REGIONS 9 I", "NUTRITION MASS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"daily_nutritional_intake_mass_by_food_product": 1},
)
def daily_nutrutional_mass_intake():
    """
    Daily nutritional intake by region and nutrion factor
    """
    return sum(
        daily_nutritional_intake_mass_by_food_product().rename({"FOODS I": "FOODS I!"}),
        dim=["FOODS I!"],
    )


@component.add(
    name="diet after food losses",
    units="kg/(Year*person)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "diet_demanded": 3,
        "food_loss_parameters": 8,
        "unit_conversion_percent_share": 5,
    },
)
def diet_after_food_losses():
    """
    diet data after food losses
    """
    return (
        diet_demanded()
        * food_loss_parameters().loc[:, :, "cf"].reset_coords(drop=True)
        * (
            1
            - food_loss_parameters().loc[:, :, "wp cns"].reset_coords(drop=True)
            * unit_conversion_percent_share()
        )
        + diet_demanded()
        * food_loss_parameters().loc[:, :, "pct fresh"].reset_coords(drop=True)
        * unit_conversion_percent_share()
        * food_loss_parameters().loc[:, :, "cf fresh"].reset_coords(drop=True)
        * (
            1
            - food_loss_parameters().loc[:, :, "wp cns"].reset_coords(drop=True)
            * unit_conversion_percent_share()
        )
        + diet_demanded()
        * food_loss_parameters().loc[:, :, "pct prcd"].reset_coords(drop=True)
        * unit_conversion_percent_share()
        * food_loss_parameters().loc[:, :, "cf prcd"].reset_coords(drop=True)
        * (
            1
            - food_loss_parameters().loc[:, :, "wp cnsprcd"].reset_coords(drop=True)
            * unit_conversion_percent_share()
        )
    )


@component.add(
    name='"DN\\_fibre"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def dn_fibre():
    return (
        daily_nutrutional_mass_intake().loc[:, "FIBRE"].reset_coords(drop=True) * 1000
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_animal\\_protein"',
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutritional_intake_mass_by_food_product": 6,
        "daily_nutrutional_mass_intake": 1,
    },
)
def percentage_animal_protein():
    return (
        (
            daily_nutritional_intake_mass_by_food_product()
            .loc[:, "FATS ANIMAL", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "DAIRY", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "EGGS", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "MEAT RUMINANTS", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "MEAT MONOGASTRIC", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "FISH", "PROTEINS"]
            .reset_coords(drop=True)
        )
        * 100
    ) / daily_nutrutional_mass_intake().loc[:, "PROTEINS"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_CHO"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_cho():
    return (
        (
            daily_nutrutional_mass_intake()
            .loc[:, "CARBOHYDRATES"]
            .reset_coords(drop=True)
            * 4
        )
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_fats"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_fats():
    return (
        (daily_nutrutional_mass_intake().loc[:, "FATS"].reset_coords(drop=True) * 9)
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_MUFA"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_mufa():
    return (
        (
            daily_nutrutional_mass_intake().loc[:, "MUFA FATS"].reset_coords(drop=True)
            * 9
        )
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_protein"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_protein():
    return (
        (daily_nutrutional_mass_intake().loc[:, "PROTEINS"].reset_coords(drop=True) * 4)
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_PUFA"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_pufa():
    return (
        (
            daily_nutrutional_mass_intake().loc[:, "PUFA FATS"].reset_coords(drop=True)
            * 9
        )
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_SFA"',
    units="g/kcal",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutrutional_mass_intake": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_sfa():
    return (
        (daily_nutrutional_mass_intake().loc[:, "SFA FATS"].reset_coords(drop=True) * 9)
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_sugar"',
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutritional_intake_energy_by_food_product": 1,
        "daily_nutritional_energy_intake": 1,
    },
)
def percentage_sugar():
    return (
        daily_nutritional_intake_energy_by_food_product()
        .loc[:, "SUGARS"]
        .reset_coords(drop=True)
        * 100
    ) / daily_nutritional_energy_intake().loc[:, "ENERGY"].reset_coords(drop=True)


@component.add(
    name='"percentage\\_vegetal\\_protein"',
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "daily_nutritional_intake_mass_by_food_product": 6,
        "daily_nutrutional_mass_intake": 1,
    },
)
def percentage_vegetal_protein():
    return 100 - (
        (
            daily_nutritional_intake_mass_by_food_product()
            .loc[:, "FATS ANIMAL", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "DAIRY", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "EGGS", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "MEAT RUMINANTS", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "MEAT MONOGASTRIC", "PROTEINS"]
            .reset_coords(drop=True)
            + daily_nutritional_intake_mass_by_food_product()
            .loc[:, "FISH", "PROTEINS"]
            .reset_coords(drop=True)
        )
        * 100
    ) / daily_nutrutional_mass_intake().loc[:, "PROTEINS"].reset_coords(drop=True)
