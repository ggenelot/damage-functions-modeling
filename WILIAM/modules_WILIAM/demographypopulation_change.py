"""
Module demographypopulation_change
Translated using PySD version 3.14.0
"""

@component.add(
    name="aux population",
    units="person/Year",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_population": 1},
    other_deps={
        "_delayfixed_aux_population": {
            "initial": {"time_step": 1},
            "step": {"population_by_cohorts_each_five_years": 1},
        }
    },
)
def aux_population():
    return _delayfixed_aux_population()


_delayfixed_aux_population = DelayFixed(
    lambda: population_by_cohorts_each_five_years(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SEX I": _subscript_dict["SEX I"],
            "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
        },
        ["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    ),
    time_step,
    "_delayfixed_aux_population",
)


@component.add(
    name="births",
    units="people/Year",
    subscripts=["REGIONS 35 I", "SEX I", "AGE CHAIN YOUNG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "population_by_cohorts": 2,
        "fertility_rates": 2,
        "unit_conversion_kpeople_people": 2,
        "gender_birth": 2,
    },
)
def births():
    """
    Births, by region and gender. Historical births 2015-2020 are remained constant for scenarios. In case of smoothing births, gender births ratio HISTORICAL_FERTILITY_RATES_2015_2020 was included as constant ratio for historical period of time.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SEX I": _subscript_dict["SEX I"],
            "AGE CHAIN YOUNG I": _subscript_dict["AGE CHAIN YOUNG I"],
        },
        ["REGIONS 35 I", "SEX I", "AGE CHAIN YOUNG I"],
    )
    value.loc[:, ["FEMALE"], ["c0c4"]] = (
        (
            sum(
                population_by_cohorts()
                .loc[:, "FEMALE", _subscript_dict["FERTILITY AGES I"]]
                .reset_coords(drop=True)
                .rename({"AGE COHORTS I": "FERTILITY AGES I!"})
                * fertility_rates()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
                .rename({"FERTILITY AGES I": "FERTILITY AGES I!"})
                * unit_conversion_kpeople_people(),
                dim=["FERTILITY AGES I!"],
            )
            / 2
            * (2 - gender_birth())
        )
        .expand_dims({"SEX I": ["FEMALE"]}, 1)
        .expand_dims({"AGE CHAIN YOUNG I": ["c0c4"]}, 2)
        .values
    )
    value.loc[:, ["MALE"], ["c0c4"]] = (
        (
            sum(
                population_by_cohorts()
                .loc[:, "FEMALE", _subscript_dict["FERTILITY AGES I"]]
                .reset_coords(drop=True)
                .rename({"AGE COHORTS I": "FERTILITY AGES I!"})
                * fertility_rates()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
                .rename({"FERTILITY AGES I": "FERTILITY AGES I!"})
                * unit_conversion_kpeople_people(),
                dim=["FERTILITY AGES I!"],
            )
            / 2
            * gender_birth()
        )
        .expand_dims({"SEX I": ["MALE"]}, 1)
        .expand_dims({"AGE CHAIN YOUNG I": ["c0c4"]}, 2)
        .values
    )
    return value


@component.add(
    name="children under 15",
    units="person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts": 3},
)
def children_under_15():
    """
    Children under 15 years old
    """
    return (
        sum(
            population_by_cohorts()
            .loc[:, :, "c0c4"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        + sum(
            population_by_cohorts()
            .loc[:, :, "c5c9"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        + sum(
            population_by_cohorts()
            .loc[:, :, "c10c14"]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
    )


@component.add(
    name="deaths",
    units="people/Year",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "population_by_cohorts": 1,
        "mortality_rates_chain": 1,
        "unit_conversion_kpeople_people": 1,
    },
)
def deaths():
    """
    Deaths, by region, gender, and age cohort.
    """
    return (
        population_by_cohorts()
        * mortality_rates_chain()
        * unit_conversion_kpeople_people()
    )


@component.add(
    name="emigration distribution",
    units="person",
    subscripts=["REGIONS 35 I", "REGIONS 35 MAP I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "emigrations": 3,
        "historical_shares_migration": 2,
        "switch_migration_sp": 1,
        "start_year_migrations_sp": 1,
        "shares_emigration_sp": 1,
    },
)
def emigration_distribution():
    """
    Distribution of emigration into the regions (all with all)
    """
    return if_then_else(
        time() < 2020,
        lambda: emigrations() * historical_shares_migration(),
        lambda: if_then_else(
            switch_migration_sp() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SEX I": _subscript_dict["SEX I"],
                    "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
                    "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
                },
                ["REGIONS 35 I", "SEX I", "AGE COHORTS I", "REGIONS 35 MAP I"],
            ),
            lambda: if_then_else(
                time() < start_year_migrations_sp(),
                lambda: emigrations() * historical_shares_migration(),
                lambda: emigrations() * shares_emigration_sp(),
            ),
        ),
    ).transpose("REGIONS 35 I", "REGIONS 35 MAP I", "SEX I", "AGE COHORTS I")


@component.add(
    name="emigrations",
    units="person",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historic_emigrations_rate": 1,
        "population_by_cohorts": 2,
        "percentage_emigrations_sp": 1,
        "switch_migration_sp": 1,
        "start_year_migrations_sp": 1,
    },
)
def emigrations():
    """
    Estimated emigrations by region
    """
    return if_then_else(
        time() < 2020,
        lambda: population_by_cohorts() * historic_emigrations_rate(),
        lambda: if_then_else(
            switch_migration_sp() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SEX I": _subscript_dict["SEX I"],
                    "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
                },
                ["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
            ),
            lambda: if_then_else(
                time() < start_year_migrations_sp(),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SEX I": _subscript_dict["SEX I"],
                        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
                    },
                    ["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
                ),
                lambda: population_by_cohorts() * percentage_emigrations_sp(),
            ),
        ),
    )


@component.add(
    name="european births",
    units="people",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"births": 1},
)
def european_births():
    """
    Births in Europe-27
    """
    return sum(
        births()
        .loc[_subscript_dict["REGIONS EU27 I"], :, "c0c4"]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS EU27 I!", "SEX I": "SEX I!"}),
        dim=["REGIONS EU27 I!", "SEX I!"],
    )


@component.add(
    name="fertility rates",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "historical_fertility_rates_2005_2010": 1,
        "ramp_scenario_fertility_rates": 1,
        "historical_fertility_rates_2010_2015": 1,
        "historical_fertility_rates_2015_2020": 2,
    },
)
def fertility_rates():
    """
    Fertility rates
    """
    return if_then_else(
        time() < 2010,
        lambda: historical_fertility_rates_2005_2010()
        .loc[:, "FEMALE", :]
        .reset_coords(drop=True),
        lambda: if_then_else(
            time() < 2015,
            lambda: historical_fertility_rates_2010_2015()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True),
            lambda: if_then_else(
                time() < 2020,
                lambda: historical_fertility_rates_2015_2020()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True),
                lambda: historical_fertility_rates_2015_2020()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
                + ramp_scenario_fertility_rates()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True),
            ),
        ),
    ).expand_dims({"SEX I": ["FEMALE"]}, 1)


@component.add(
    name="gender birth",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historical_gender_birth_ratio_2005_2010": 1,
        "historical_gender_birth_ratio_2010_2015": 1,
        "historical_gender_birth_ratio_2015_2020": 1,
    },
)
def gender_birth():
    """
    The ratio of male to female births by region.
    """
    return if_then_else(
        time() < 2010,
        lambda: historical_gender_birth_ratio_2005_2010(),
        lambda: if_then_else(
            time() < 2015,
            lambda: historical_gender_birth_ratio_2010_2015(),
            lambda: historical_gender_birth_ratio_2015_2020(),
        ),
    )


@component.add(
    name="HISTORICAL SHARES MIGRATION",
    units="DMNL",
    subscripts=["REGIONS 35 I", "REGIONS 35 MAP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_shares_migration"},
)
def historical_shares_migration():
    """
    Historical shares of emigration (distribution across regions)
    """
    return _ext_constant_historical_shares_migration()


_ext_constant_historical_shares_migration = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_SHARES_MIGRATION",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
    },
    "_ext_constant_historical_shares_migration",
)


@component.add(
    name="immigrations",
    units="person",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"emigration_distribution": 1},
)
def immigrations():
    """
    Aggregation of immigration flows
    """
    return sum(
        emigration_distribution().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "REGIONS 35 MAP I": "REGIONS 35 I"}
        ),
        dim=["REGIONS 35 I!"],
    )


@component.add(
    name="mortality rates chain",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "a_exponential_leab_to_mr": 2,
        "b_exponential_leab_to_mr": 2,
        "life_expectancy_at_birth": 2,
        "min_historical_mortality_rate": 2,
    },
)
def mortality_rates_chain():
    """
    Units: people/kpeople = (people/(1000*people). Estimation of the mortality rates from the life expectancy at birth, by region, gender and age cohort.
    """
    return if_then_else(
        a_exponential_leab_to_mr()
        * np.exp(
            b_exponential_leab_to_mr()
            * life_expectancy_at_birth().transpose("SEX I", "REGIONS 35 I")
        )
        < min_historical_mortality_rate(),
        lambda: xr.DataArray(
            min_historical_mortality_rate(),
            {
                "SEX I": _subscript_dict["SEX I"],
                "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            },
            ["SEX I", "AGE COHORTS I", "REGIONS 35 I"],
        ),
        lambda: a_exponential_leab_to_mr()
        * np.exp(
            b_exponential_leab_to_mr()
            * life_expectancy_at_birth().transpose("SEX I", "REGIONS 35 I")
        ),
    ).transpose("REGIONS 35 I", "SEX I", "AGE COHORTS I")


@component.add(
    name="net migrations",
    units="people",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"immigrations": 1, "emigrations": 1},
)
def net_migrations():
    """
    Estimation net migrations by country
    """
    return immigrations() - emigrations()


@component.add(
    name="net migrations by country",
    units="person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_migrations": 1},
)
def net_migrations_by_country():
    return sum(
        net_migrations().rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )


@component.add(
    name="population 35 regions",
    units="people",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts": 1},
)
def population_35_regions():
    """
    Total regional population.
    """
    return sum(
        population_by_cohorts().rename(
            {"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}
        ),
        dim=["SEX I!", "AGE COHORTS I!"],
    )


@component.add(
    name="population 9 regions",
    units="people",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts": 9},
)
def population_9_regions():
    """
    Population with EU-27 aggregated, so 9 regions.
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[["EU27"]] = sum(
        population_by_cohorts()
        .loc[_subscript_dict["REGIONS EU27 I"], :, :]
        .rename(
            {
                "REGIONS 35 I": "REGIONS EU27 I!",
                "SEX I": "SEX I!",
                "AGE COHORTS I": "AGE COHORTS I!",
            }
        ),
        dim=["REGIONS EU27 I!", "SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["UK"]] = sum(
        population_by_cohorts()
        .loc["UK", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["CHINA"]] = sum(
        population_by_cohorts()
        .loc["CHINA", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["EASOC"]] = sum(
        population_by_cohorts()
        .loc["EASOC", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["INDIA"]] = sum(
        population_by_cohorts()
        .loc["INDIA", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["LATAM"]] = sum(
        population_by_cohorts()
        .loc["LATAM", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["RUSSIA"]] = sum(
        population_by_cohorts()
        .loc["RUSSIA", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["USMCA"]] = sum(
        population_by_cohorts()
        .loc["USMCA", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    value.loc[["LROW"]] = sum(
        population_by_cohorts()
        .loc["LROW", :, :]
        .reset_coords(drop=True)
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}),
        dim=["SEX I!", "AGE COHORTS I!"],
    )
    return value


@component.add(
    name="population by cohorts",
    units="people",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_population_by_cohorts": 1},
    other_deps={
        "_integ_population_by_cohorts": {
            "initial": {"population_2005": 1},
            "step": {"population_variation": 1, "emigrations": 1, "immigrations": 1},
        }
    },
)
def population_by_cohorts():
    """
    Population by region, sex, and age cohorts
    """
    return _integ_population_by_cohorts()


_integ_population_by_cohorts = Integ(
    lambda: population_variation() - emigrations() + immigrations(),
    lambda: population_2005(),
    "_integ_population_by_cohorts",
)


@component.add(
    name="population by cohorts each five years",
    units="person/Year",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "population_by_cohorts": 1, "aux_population": 1},
)
def population_by_cohorts_each_five_years():
    return if_then_else(
        modulo(time(), 5) == 0,
        lambda: population_by_cohorts(),
        lambda: aux_population(),
    )


@component.add(
    name="population variation",
    units="person/Year",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "births": 1,
        "deaths": 3,
        "population_by_cohorts_each_five_years": 4,
        "time_step": 2,
        "population_by_cohorts": 2,
    },
)
def population_variation():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SEX I": _subscript_dict["SEX I"],
            "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
        },
        ["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    )
    value.loc[:, :, ["c0c4"]] = (
        np.maximum(
            births().loc[:, :, "c0c4"].reset_coords(drop=True)
            - deaths().loc[:, :, "c0c4"].reset_coords(drop=True)
            - population_by_cohorts_each_five_years()
            .loc[:, :, "c0c4"]
            .reset_coords(drop=True)
            / 5,
            -population_by_cohorts().loc[:, :, "c0c4"].reset_coords(drop=True)
            / time_step(),
        )
        .expand_dims({"AGE CHAIN YOUNG I": ["c0c4"]}, 2)
        .values
    )
    value.loc[:, :, _subscript_dict["AGE CHAIN MIDDLE I"]] = np.maximum(
        -deaths()
        .loc[:, :, _subscript_dict["AGE CHAIN MIDDLE I"]]
        .rename({"AGE COHORTS I": "AGE CHAIN MIDDLE I"})
        + xr.DataArray(
            population_by_cohorts_each_five_years()
            .loc[:, :, _subscript_dict["AGE CHAIN YOUNG I"]]
            .rename({"AGE COHORTS I": "AGE CHAIN YOUNG I"})
            .values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SEX I": _subscript_dict["SEX I"],
                "AGE CHAIN MIDDLE I": _subscript_dict["AGE CHAIN MIDDLE I"],
            },
            ["REGIONS 35 I", "SEX I", "AGE CHAIN MIDDLE I"],
        )
        / 5
        - population_by_cohorts_each_five_years()
        .loc[:, :, _subscript_dict["AGE CHAIN MIDDLE I"]]
        .rename({"AGE COHORTS I": "AGE CHAIN MIDDLE I"})
        / 5,
        -population_by_cohorts()
        .loc[:, :, _subscript_dict["AGE CHAIN MIDDLE I"]]
        .rename({"AGE COHORTS I": "AGE CHAIN MIDDLE I"})
        / time_step(),
    ).values
    value.loc[:, :, ["cover80"]] = (
        (
            -deaths().loc[:, :, "cover80"].reset_coords(drop=True)
            + population_by_cohorts_each_five_years()
            .loc[:, :, "c75c79"]
            .reset_coords(drop=True)
            / 5
        )
        .expand_dims({"AGE CHAIN I": ["cover80"]}, 2)
        .values
    )
    return value


@component.add(
    name="ramp scenario fertility rates",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "time": 2,
        "target_year_fertility_rates_sp": 2,
        "slope_scenario_fertility_rates": 2,
    },
)
def ramp_scenario_fertility_rates():
    """
    Ramp of values to the future fertility rates (scenario)
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: ramp(
            __data["time"],
            slope_scenario_fertility_rates()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True),
            2020,
            target_year_fertility_rates_sp(),
        ),
        lambda: ramp(
            __data["time"],
            slope_scenario_fertility_rates()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True),
            2020,
            target_year_fertility_rates_sp(),
        ),
    ).expand_dims({"SEX I": ["FEMALE"]}, 1)


@component.add(
    name="retired population",
    units="person",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts": 1},
)
def retired_population():
    """
    Retired population in the world
    """
    return sum(
        population_by_cohorts()
        .loc[:, :, _subscript_dict["AGE RETIREMENT I"]]
        .rename({"AGE COHORTS I": "AGE RETIREMENT I!"}),
        dim=["AGE RETIREMENT I!"],
    )


@component.add(
    name="SLOPE SCENARIO FERTILITY RATES",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_fertility_rates": 1,
        "target_scenario_fertility_rates": 1,
        "target_year_fertility_rates_sp": 1,
        "historical_fertility_rates_2015_2020": 1,
    },
)
def slope_scenario_fertility_rates():
    """
    Slope of the ramp to create the scenario for the fertility rates. IF_THEN_ELSE(SWITCH_MODEL_EXPLORER=1, (model_explorer_fertility_rates[REGIONS_35_I,FEMALE,FERTILITY_AGES_I] - HISTORICAL_FERTILITY_RATES_2015_2020[REGIONS_35_I ,FEMALE,FERTILITY_AGES_I]) / (FINAL_YEAR_MODEL_EXPLORER - 2020) , (TARGET_SCENARIO_FERTILITY_RATES[REGIONS_35_I,FEMALE,FERTILITY_AGES_I] - HISTORICAL_FERTILITY_RATES_2015_2020[REGIONS_35_I ,FEMALE,FERTILITY_AGES_I]) / (TARGET_YEAR_FERTILITY_RATES_SP[REGIONS_35_I] - 2020))
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_fertility_rates()
        .loc[:, "FEMALE", :]
        .reset_coords(drop=True),
        lambda: (
            target_scenario_fertility_rates()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
            - historical_fertility_rates_2015_2020()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
        )
        / (target_year_fertility_rates_sp() - 2020),
    ).expand_dims({"SEX I": ["FEMALE"]}, 1)


@component.add(
    name="SWITCH MIGRATION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_migration_sp"},
)
def switch_migration_sp():
    """
    Switch to activare (1) / desactivate (0) the migration approach
    """
    return _ext_constant_switch_migration_sp()


_ext_constant_switch_migration_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "SWITCH_MIGRATION_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_migration_sp",
)


@component.add(
    name="TARGET SCENARIO FERTILITY RATES",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "objective_fertility_rates_sp": 2,
        "scenario_fertility_rate_minimum_sp": 1,
        "scenario_fertility_rate_maximum_sp": 1,
        "scenario_fertility_rate_average_sp": 1,
    },
)
def target_scenario_fertility_rates():
    """
    Selection of the scenario (low, medium or high)
    """
    return if_then_else(
        (objective_fertility_rates_sp() == 1).expand_dims(
            {"FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"]}, 1
        ),
        lambda: scenario_fertility_rate_minimum_sp()
        .loc[:, "FEMALE", :]
        .reset_coords(drop=True),
        lambda: if_then_else(
            (objective_fertility_rates_sp() == 2).expand_dims(
                {"FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"]}, 1
            ),
            lambda: scenario_fertility_rate_average_sp()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True),
            lambda: scenario_fertility_rate_maximum_sp()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True),
        ),
    ).expand_dims({"SEX I": ["FEMALE"]}, 1)


@component.add(
    name="total population over 15",
    units="people",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_by_cohorts": 1},
)
def total_population_over_15():
    """
    Population in working age (15 years old and older) by region.
    """
    return sum(
        population_by_cohorts()
        .loc[:, :, _subscript_dict["AGE WORKING I"]]
        .rename({"SEX I": "SEX I!", "AGE COHORTS I": "AGE WORKING I!"}),
        dim=["SEX I!", "AGE WORKING I!"],
    )


@component.add(
    name="world population",
    units="person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_9_regions": 1},
)
def world_population():
    """
    Population living in the Earth planet
    """
    return sum(
        population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
