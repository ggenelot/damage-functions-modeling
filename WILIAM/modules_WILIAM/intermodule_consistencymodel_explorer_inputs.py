"""
Module intermodule_consistencymodel_explorer_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="FINAL YEAR MODEL EXPLORER",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_year_model_explorer"},
)
def final_year_model_explorer():
    """
    FINAL_YEAR_MODEL_EXPLORER
    """
    return _ext_constant_final_year_model_explorer()


_ext_constant_final_year_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "FINAL_YEAR_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_final_year_model_explorer",
)


@component.add(
    name="FINAL YEAR WORKING TIME",
    units="Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def final_year_working_time():
    """
    FINAL_YEAR_WORKING_TIME
    """
    return 2030


@component.add(
    name="INITIAL YEAR MODEL EXPLORER",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_model_explorer"},
)
def initial_year_model_explorer():
    """
    INITIAL_YEAR_MODEL_EXPLORER
    """
    return _ext_constant_initial_year_model_explorer()


_ext_constant_initial_year_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "INITIAL_YEAR_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_initial_year_model_explorer",
)


@component.add(
    name="model explorer change to regenerative agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_change_to_regenerative_agriculture_me": 3,
        "final_year_model_explorer": 5,
        "scenario_select_change_to_regenerative_agriculture_option_1_me": 1,
        "initial_year_model_explorer": 5,
        "time": 6,
        "scenario_select_change_to_regenerative_agriculture_option_2_me": 1,
        "initial_share_of_regenerative_agriculture": 2,
        "scenario_select_change_to_regenerative_agriculture_option_3_me": 1,
    },
)
def model_explorer_change_to_regenerative_agriculture():
    """
    Policy Change to Regenerative Agriculture for model explorer.
    """
    return if_then_else(
        select_change_to_regenerative_agriculture_me() == 1,
        lambda: if_then_else(
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() < final_year_model_explorer(),
            ),
            lambda: scenario_select_change_to_regenerative_agriculture_option_1_me(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        ).expand_dims({"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1),
        lambda: if_then_else(
            select_change_to_regenerative_agriculture_me() == 2,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() < final_year_model_explorer(),
                ),
                lambda: (
                    scenario_select_change_to_regenerative_agriculture_option_2_me()
                    - initial_share_of_regenerative_agriculture()
                )
                / (final_year_model_explorer() - initial_year_model_explorer()),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                    },
                    ["REGIONS 9 I", "LAND PRODUCTS I"],
                ),
            ),
            lambda: if_then_else(
                select_change_to_regenerative_agriculture_me() == 3,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() < final_year_model_explorer(),
                    ),
                    lambda: (
                        scenario_select_change_to_regenerative_agriculture_option_3_me()
                        - initial_share_of_regenerative_agriculture()
                    )
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                        },
                        ["REGIONS 9 I", "LAND PRODUCTS I"],
                    ),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                    },
                    ["REGIONS 9 I", "LAND PRODUCTS I"],
                ),
            ),
        ),
    )


@component.add(
    name="model explorer climate sensitivity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "scenario_climate_sensitivity_option_2_me": 2,
        "select_climate_sensitivity_me": 3,
        "scenario_climate_sensitivity_option_3_me": 1,
        "scenario_climate_sensitivity_option_1_me": 1,
    },
)
def model_explorer_climate_sensitivity():
    """
    Hypothesis climate sensitivity for model explorer.
    """
    return if_then_else(
        time() < 2015,
        lambda: scenario_climate_sensitivity_option_2_me(),
        lambda: if_then_else(
            select_climate_sensitivity_me() == 1,
            lambda: scenario_climate_sensitivity_option_1_me(),
            lambda: if_then_else(
                select_climate_sensitivity_me() == 2,
                lambda: scenario_climate_sensitivity_option_2_me(),
                lambda: if_then_else(
                    select_climate_sensitivity_me() == 3,
                    lambda: scenario_climate_sensitivity_option_3_me(),
                    lambda: 0,
                ),
            ),
        ),
    )


@component.add(
    name="model explorer debt interest rate target",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_debt_interest_rate_target_me": 3,
        "debt_interest_rate_default": 6,
        "initial_year_model_explorer": 3,
        "time": 3,
        "scenario_debt_interest_rate_target_option_1_me": 1,
        "scenario_debt_interest_rate_target_option_3_me": 1,
        "scenario_debt_interest_rate_target_option_2_me": 1,
    },
)
def model_explorer_debt_interest_rate_target():
    """
    Policy debt interest rate target for model explorer.
    """
    return if_then_else(
        select_debt_interest_rate_target_me() == 1,
        lambda: if_then_else(
            time() < initial_year_model_explorer(),
            lambda: debt_interest_rate_default(),
            lambda: scenario_debt_interest_rate_target_option_1_me()
            + debt_interest_rate_default(),
        ),
        lambda: if_then_else(
            select_debt_interest_rate_target_me() == 2,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: debt_interest_rate_default(),
                lambda: scenario_debt_interest_rate_target_option_2_me()
                + debt_interest_rate_default(),
            ),
            lambda: if_then_else(
                select_debt_interest_rate_target_me() == 3,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: debt_interest_rate_default(),
                    lambda: scenario_debt_interest_rate_target_option_3_me()
                    + debt_interest_rate_default(),
                ),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
        ),
    )


@component.add(
    name="model explorer diets",
    units="kg/(Year*person)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_tipe_diets_me": 3,
        "scenario_flexitariana_option_1_me": 1,
        "scenario_plant_based_100_option_3_me": 1,
        "scenario_baseline_option_2_me": 1,
    },
)
def model_explorer_diets():
    """
    Policy diets for model explorer.
    """
    return if_then_else(
        select_tipe_diets_me() == 1,
        lambda: scenario_flexitariana_option_1_me(),
        lambda: if_then_else(
            select_tipe_diets_me() == 2,
            lambda: scenario_baseline_option_2_me(),
            lambda: if_then_else(
                select_tipe_diets_me() == 3,
                lambda: scenario_plant_based_100_option_3_me(),
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
    )


@component.add(
    name="model explorer energy efficiency anual improvement",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_model_explorer": 1,
        "historical_energy_efficiency_annual_improvement": 1,
        "select_energy_efficiency_annual_improvement_me": 3,
        "scenario_energy_efficiency_option_3_me": 1,
        "scenario_energy_efficiency_option_1_me": 1,
        "scenario_energy_efficiency_option_2_me": 1,
    },
)
def model_explorer_energy_efficiency_anual_improvement():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: historical_energy_efficiency_annual_improvement(),
        lambda: if_then_else(
            select_energy_efficiency_annual_improvement_me() == 1,
            lambda: scenario_energy_efficiency_option_1_me(),
            lambda: if_then_else(
                select_energy_efficiency_annual_improvement_me() == 2,
                lambda: scenario_energy_efficiency_option_2_me(),
                lambda: if_then_else(
                    select_energy_efficiency_annual_improvement_me() == 3,
                    lambda: scenario_energy_efficiency_option_3_me(),
                    lambda: xr.DataArray(
                        1,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model explorer fertility rates",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_fertility_rates_me": 3,
        "final_year_model_explorer": 3,
        "scenario_fertility_rates_option_1_me": 1,
        "historical_fertility_rates_2015_2020": 3,
        "scenario_fertility_rates_option_3_me": 1,
        "scenario_fertility_rates_option_2_me": 1,
    },
)
def model_explorer_fertility_rates():
    """
    Policy fertility rates for model explorer.
    """
    return if_then_else(
        select_fertility_rates_me() == 1,
        lambda: (
            scenario_fertility_rates_option_1_me()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
            - historical_fertility_rates_2015_2020()
            .loc[:, "FEMALE", :]
            .reset_coords(drop=True)
        )
        / (final_year_model_explorer() - 2020),
        lambda: if_then_else(
            select_fertility_rates_me() == 2,
            lambda: (
                scenario_fertility_rates_option_2_me()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
                - historical_fertility_rates_2015_2020()
                .loc[:, "FEMALE", :]
                .reset_coords(drop=True)
            )
            / (final_year_model_explorer() - 2020),
            lambda: if_then_else(
                select_fertility_rates_me() == 3,
                lambda: (
                    scenario_fertility_rates_option_3_me()
                    .loc[:, "FEMALE", :]
                    .reset_coords(drop=True)
                    - historical_fertility_rates_2015_2020()
                    .loc[:, "FEMALE", :]
                    .reset_coords(drop=True)
                )
                / (final_year_model_explorer() - 2020),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
                    },
                    ["REGIONS 35 I", "FERTILITY AGES I"],
                ),
            ),
        ),
    ).expand_dims({"SEX I": ["FEMALE"]}, 1)


@component.add(
    name="model explorer final gender parity index",
    units="1/Year",
    subscripts=["REGIONS 35 I", "EDUCATIONAL LEVEL I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_final_gender_parity_index_me": 6,
        "initial_gender_parity_index": 6,
        "final_year_model_explorer": 12,
        "initial_year_model_explorer": 12,
        "time": 12,
        "scenario_final_gender_parity_index_option_1_me": 2,
        "scenario_final_gender_parity_index_option_2_me": 2,
        "scenario_final_gender_parity_index_option_3_me": 2,
    },
)
def model_explorer_final_gender_parity_index():
    """
    Policy gender parity in education for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "EDUCATIONAL LEVEL I": _subscript_dict["EDUCATIONAL LEVEL I"],
        },
        ["REGIONS 35 I", "EDUCATIONAL LEVEL I"],
    )
    value.loc[:, ["HIGH EDUCATION"]] = (
        if_then_else(
            select_final_gender_parity_index_me() == 1,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: zidz(
                        scenario_final_gender_parity_index_option_1_me()
                        .loc[:, "HIGH EDUCATION"]
                        .reset_coords(drop=True)
                        - initial_gender_parity_index()
                        .loc[:, "HIGH EDUCATION"]
                        .reset_coords(drop=True),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
            lambda: if_then_else(
                select_final_gender_parity_index_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_final_gender_parity_index_option_2_me()
                            .loc[:, "HIGH EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "HIGH EDUCATION"]
                            .reset_coords(drop=True),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                            ["REGIONS 35 I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_final_gender_parity_index_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                            ["REGIONS 35 I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_final_gender_parity_index_option_3_me()
                                .loc[:, "HIGH EDUCATION"]
                                .reset_coords(drop=True)
                                - initial_gender_parity_index()
                                .loc[:, "HIGH EDUCATION"]
                                .reset_coords(drop=True),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                                ["REGIONS 35 I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL LEVEL I": ["HIGH EDUCATION"]}, 1)
        .values
    )
    value.loc[:, ["MEDIUM EDUCATION"]] = (
        if_then_else(
            select_final_gender_parity_index_me() == 1,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: zidz(
                        scenario_final_gender_parity_index_option_1_me()
                        .loc[:, "MEDIUM EDUCATION"]
                        .reset_coords(drop=True)
                        - initial_gender_parity_index()
                        .loc[:, "MEDIUM EDUCATION"]
                        .reset_coords(drop=True),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
            lambda: if_then_else(
                select_final_gender_parity_index_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_final_gender_parity_index_option_2_me()
                            .loc[:, "MEDIUM EDUCATION"]
                            .reset_coords(drop=True)
                            - initial_gender_parity_index()
                            .loc[:, "MEDIUM EDUCATION"]
                            .reset_coords(drop=True),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                            ["REGIONS 35 I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_final_gender_parity_index_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                            ["REGIONS 35 I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_final_gender_parity_index_option_3_me()
                                .loc[:, "MEDIUM EDUCATION"]
                                .reset_coords(drop=True)
                                - initial_gender_parity_index()
                                .loc[:, "MEDIUM EDUCATION"]
                                .reset_coords(drop=True),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                                ["REGIONS 35 I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
        )
        .expand_dims({"EDUCATIONAL LEVEL I": ["MEDIUM EDUCATION"]}, 1)
        .values
    )
    return value


@component.add(
    name="model explorer forestry self sufficiency",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_forestry_self_sufficiency": 3,
        "initial_year_model_explorer": 6,
        "time": 6,
        "final_year_model_explorer": 6,
        "scenario_forestry_self_sufficiency_option_1_me": 1,
        "scenario_forestry_self_sufficiency_option_2_me": 1,
        "scenario_forestry_self_sufficiency_option_3_me": 1,
    },
)
def model_explorer_forestry_self_sufficiency():
    """
    Policy Forestry self sufficiency policy for model explorer.
    """
    return if_then_else(
        np.logical_and(
            select_forestry_self_sufficiency() == 1,
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() <= final_year_model_explorer(),
            ),
        ),
        lambda: scenario_forestry_self_sufficiency_option_1_me()
        / (final_year_model_explorer() - initial_year_model_explorer()),
        lambda: if_then_else(
            np.logical_and(
                select_forestry_self_sufficiency() == 2,
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
            ),
            lambda: scenario_forestry_self_sufficiency_option_2_me()
            / (final_year_model_explorer() - initial_year_model_explorer()),
            lambda: if_then_else(
                np.logical_and(
                    select_forestry_self_sufficiency() == 3,
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                ),
                lambda: scenario_forestry_self_sufficiency_option_3_me()
                / (final_year_model_explorer() - initial_year_model_explorer()),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
        ),
    )


@component.add(
    name="model explorer government to GDP objetive",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_model_explorer": 1,
        "scenario_goverment_option_2_me": 1,
        "scenario_goverment_option_3_me": 1,
        "scenario_goverment_option_1_me": 1,
        "select_government_budget_balance_to_gdp_objective_target_me": 3,
    },
)
def model_explorer_government_to_gdp_objetive():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: if_then_else(
            select_government_budget_balance_to_gdp_objective_target_me() == 1,
            lambda: scenario_goverment_option_1_me(),
            lambda: if_then_else(
                select_government_budget_balance_to_gdp_objective_target_me() == 2,
                lambda: scenario_goverment_option_2_me(),
                lambda: if_then_else(
                    select_government_budget_balance_to_gdp_objective_target_me() == 3,
                    lambda: scenario_goverment_option_3_me(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                        ["REGIONS 35 I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model explorer land protection",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_land_protection_by_policy_me": 3,
        "initial_year_model_explorer": 3,
        "time": 6,
        "final_year_model_explorer": 3,
        "scenario_land_protection_by_policy_option_1_me": 1,
        "scenario_land_protection_by_policy_option_3_me": 1,
        "scenario_land_protection_by_policy_option_2_me": 1,
    },
)
def model_explorer_land_protection():
    """
    Policy Protection of Primary Forest Policy for model explorer.
    """
    return if_then_else(
        np.logical_and(
            select_land_protection_by_policy_me() == 1,
            np.logical_and(
                time() > initial_year_model_explorer(),
                time() < final_year_model_explorer(),
            ),
        ),
        lambda: scenario_land_protection_by_policy_option_1_me(),
        lambda: if_then_else(
            np.logical_and(
                select_land_protection_by_policy_me() == 2,
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() < final_year_model_explorer(),
                ),
            ),
            lambda: scenario_land_protection_by_policy_option_2_me(),
            lambda: if_then_else(
                np.logical_and(
                    select_land_protection_by_policy_me() == 3,
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() < final_year_model_explorer(),
                    ),
                ),
                lambda: scenario_land_protection_by_policy_option_3_me(),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "LANDS I": _subscript_dict["LANDS I"],
                    },
                    ["REGIONS 9 I", "LANDS I"],
                ),
            ),
        ),
    )


@component.add(
    name="model explorer manure management system",
    units="kg/(number animals*Year)",
    subscripts=["ANIMALS TYPES I", "REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_manure_management_system_me": 12,
        "methane_conversion_factor_by_system": 24,
        "scenario_manure_management_system_option_1_me": 4,
        "dairy_cattle_manure_system": 3,
        "final_year_model_explorer": 12,
        "initial_year_model_explorer": 12,
        "time": 24,
        "scenario_manure_management_system_option_3_me": 4,
        "scenario_manure_management_system_option_2_me": 4,
        "other_cattle_manure_system": 3,
        "buffalo_manure_system": 3,
        "swine_manure_system": 3,
    },
)
def model_explorer_manure_management_system():
    """
    Policy manure management system policy for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "ANIMALS TYPES I": _subscript_dict["ANIMALS TYPES I"],
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
        },
        ["ANIMALS TYPES I", "REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
    )
    value.loc[["DAIRY CATTLE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["DAIRY CATTLE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system()
                * dairy_cattle_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["DAIRY CATTLE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * dairy_cattle_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["DAIRY CATTLE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * dairy_cattle_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "MANURE MANAGEMENT SYSTEM I": _subscript_dict[
                                "MANURE MANAGEMENT SYSTEM I"
                            ],
                        },
                        ["REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS TYPES I": ["DAIRY CATTLE"]}, 0)
        .values
    )
    value.loc[["OTHER CATTLE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["OTHER CATTLE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system()
                * other_cattle_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["OTHER CATTLE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * other_cattle_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["OTHER CATTLE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * other_cattle_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "MANURE MANAGEMENT SYSTEM I": _subscript_dict[
                                "MANURE MANAGEMENT SYSTEM I"
                            ],
                        },
                        ["REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS TYPES I": ["OTHER CATTLE"]}, 0)
        .values
    )
    value.loc[["BUFFALO"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["BUFFALO", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system() * buffalo_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["BUFFALO", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * buffalo_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["BUFFALO", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * buffalo_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "MANURE MANAGEMENT SYSTEM I": _subscript_dict[
                                "MANURE MANAGEMENT SYSTEM I"
                            ],
                        },
                        ["REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS TYPES I": ["BUFFALO"]}, 0)
        .values
    )
    value.loc[["SWINE"], :, :] = (
        if_then_else(
            select_manure_management_system_me() == 1,
            lambda: if_then_else(
                np.logical_and(
                    time() > initial_year_model_explorer(),
                    time() <= final_year_model_explorer(),
                ),
                lambda: methane_conversion_factor_by_system()
                * scenario_manure_management_system_option_1_me()
                .loc["SWINE", :, :]
                .reset_coords(drop=True),
                lambda: methane_conversion_factor_by_system() * swine_manure_system(),
            ),
            lambda: if_then_else(
                select_manure_management_system_me() == 2,
                lambda: if_then_else(
                    np.logical_and(
                        time() > initial_year_model_explorer(),
                        time() <= final_year_model_explorer(),
                    ),
                    lambda: methane_conversion_factor_by_system()
                    * scenario_manure_management_system_option_2_me()
                    .loc["SWINE", :, :]
                    .reset_coords(drop=True),
                    lambda: methane_conversion_factor_by_system()
                    * swine_manure_system(),
                ),
                lambda: if_then_else(
                    select_manure_management_system_me() == 3,
                    lambda: if_then_else(
                        np.logical_and(
                            time() > initial_year_model_explorer(),
                            time() <= final_year_model_explorer(),
                        ),
                        lambda: methane_conversion_factor_by_system()
                        * scenario_manure_management_system_option_3_me()
                        .loc["SWINE", :, :]
                        .reset_coords(drop=True),
                        lambda: methane_conversion_factor_by_system()
                        * swine_manure_system(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "MANURE MANAGEMENT SYSTEM I": _subscript_dict[
                                "MANURE MANAGEMENT SYSTEM I"
                            ],
                        },
                        ["REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
                    ),
                ),
            ),
        )
        .expand_dims({"ANIMALS TYPES I": ["SWINE"]}, 0)
        .values
    )
    return value


@component.add(
    name="model explorer objective diets",
    units="1/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "initial_year_model_explorer": 2,
        "final_year_model_explorer": 2,
        "scenario_share_diets_me": 1,
    },
)
def model_explorer_objective_diets():
    """
    Policy diets for model explorer.
    """
    return if_then_else(
        np.logical_or(
            time() < initial_year_model_explorer(), time() > final_year_model_explorer()
        ),
        lambda: 0,
        lambda: scenario_share_diets_me()
        / (final_year_model_explorer() - initial_year_model_explorer()),
    )


@component.add(
    name="model explorer oil resource",
    units="bbl",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_oil_resource_me": 3,
        "scenario_oil_resource_option_1_me": 1,
        "scenario_oil_resource_option_3_me": 1,
        "scenario_oil_resource_option_2_me": 1,
    },
)
def model_explorer_oil_resource():
    """
    Selection of different resource estimation in the model explorer.
    """
    return if_then_else(
        select_oil_resource_me() == 1,
        lambda: scenario_oil_resource_option_1_me(),
        lambda: if_then_else(
            select_oil_resource_me() == 2,
            lambda: scenario_oil_resource_option_2_me(),
            lambda: if_then_else(
                select_oil_resource_me() == 3,
                lambda: scenario_oil_resource_option_3_me(),
                lambda: 1,
            ),
        ),
    )


@component.add(
    name="model explorer percentage FE liquid substituted by H2 synthetic liquid",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me": 3,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me": 1,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me": 3,
        "final_year_model_explorer": 6,
        "initial_year_model_explorer": 8,
        "time": 6,
        "scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me": 3,
    },
)
def model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid():
    """
    Policy share of FE gas substituted by H2 gases based fuel for model explorer.
    """
    return if_then_else(
        select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me() == 1,
        lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me(),
        lambda: if_then_else(
            select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me() == 2,
            lambda: if_then_else(
                time() < initial_year_model_explorer(),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: if_then_else(
                    time() < final_year_model_explorer(),
                    lambda: -scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me()
                    * initial_year_model_explorer()
                    / (final_year_model_explorer() - initial_year_model_explorer())
                    + time()
                    * zidz(
                        scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me(),
                        final_year_model_explorer() - initial_year_model_explorer(),
                    ),
                    lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me(),
                ),
            ),
            lambda: if_then_else(
                select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me()
                == 3,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                        ["REGIONS 9 I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: -scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me()
                        * initial_year_model_explorer()
                        / (final_year_model_explorer() - initial_year_model_explorer())
                        + time()
                        * zidz(
                            scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me(),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me(),
                    ),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
        ),
    )


@component.add(
    name="model explorer protra capacity expansion",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_protra_capacity_expansion_priorities_vector_me": 3,
        "scenario_protra_expansion_option_1_me": 1,
        "scenario_protra_expansion_option_3_me": 1,
        "scenario_protra_expansion_option_2_me": 1,
    },
)
def model_explorer_protra_capacity_expansion():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        select_protra_capacity_expansion_priorities_vector_me() == 1,
        lambda: scenario_protra_expansion_option_1_me(),
        lambda: if_then_else(
            select_protra_capacity_expansion_priorities_vector_me() == 2,
            lambda: scenario_protra_expansion_option_2_me(),
            lambda: if_then_else(
                select_protra_capacity_expansion_priorities_vector_me() == 3,
                lambda: scenario_protra_expansion_option_3_me(),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    },
                    ["REGIONS 9 I", "NRG PROTRA I"],
                ),
            ),
        ),
    )


@component.add(
    name="model explorer RCP GHG emissions",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"select_rcp_ghg_emissions_me": 1},
)
def model_explorer_rcp_ghg_emissions():
    """
    Hypothesis RCP for setting the GHG emissions of those gases not being modelled endogenously for model explorer.
    """
    return select_rcp_ghg_emissions_me()


@component.add(
    name="model explorer target share bioenergy in fossil liquids and gases",
    units="1/Year",
    subscripts=["REGIONS 9 I", "NRG PRO I", "NRG COMMODITIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_target_share_bioenergy_in_fossil_liquids_and_gases_me": 12,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me": 4,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me": 4,
        "scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me": 4,
        "final_year_model_explorer": 16,
        "initial_year_model_explorer": 16,
        "time": 16,
        "protra_input_shares_empiric": 8,
    },
)
def model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases():
    """
    Policy share of bioenergy fossil liquids and gases for model explorer.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
        },
        ["REGIONS 9 I", "NRG PRO I", "NRG COMMODITIES I"],
    )
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                - protra_input_shares_empiric()
                                .loc[
                                    :, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                    "PROTRA TI GAS I": _subscript_dict[
                                        "PROTRA TI GAS I"
                                    ],
                                },
                                ["REGIONS 9 I", "PROTRA TI GAS I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas fossil"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            (
                                1
                                - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            )
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas fossil"]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                (
                                    1
                                    - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                )
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA TI GAS I"],
                                    "TI gas fossil",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                    "PROTRA TI GAS I": _subscript_dict[
                                        "PROTRA TI GAS I"
                                    ],
                                },
                                ["REGIONS 9 I", "PROTRA TI GAS I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA TI LIQUIDS I"],
                                "TI liquid bio",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA TI LIQUIDS I"],
                                    "TI liquid bio",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                    "PROTRA TI LIQUIDS I": _subscript_dict[
                                        "PROTRA TI LIQUIDS I"
                                    ],
                                },
                                ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid fossil"]] = (
        if_then_else(
            select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 1,
            lambda: scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me().expand_dims(
                {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]}, 1
            ),
            lambda: if_then_else(
                select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 2,
                lambda: if_then_else(
                    time() < initial_year_model_explorer(),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                    lambda: if_then_else(
                        time() < final_year_model_explorer(),
                        lambda: zidz(
                            (
                                1
                                - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
                            )
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA TI LIQUIDS I"],
                                "TI liquid fossil",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                            final_year_model_explorer() - initial_year_model_explorer(),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                    ),
                ),
                lambda: if_then_else(
                    select_target_share_bioenergy_in_fossil_liquids_and_gases_me() == 3,
                    lambda: if_then_else(
                        time() < initial_year_model_explorer(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                        lambda: if_then_else(
                            time() < final_year_model_explorer(),
                            lambda: zidz(
                                (
                                    1
                                    - scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
                                )
                                - protra_input_shares_empiric()
                                .loc[
                                    :,
                                    _subscript_dict["PROTRA TI LIQUIDS I"],
                                    "TI liquid fossil",
                                ]
                                .reset_coords(drop=True)
                                .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                                final_year_model_explorer()
                                - initial_year_model_explorer(),
                            ),
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                    "PROTRA TI LIQUIDS I": _subscript_dict[
                                        "PROTRA TI LIQUIDS I"
                                    ],
                                },
                                ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                            ),
                        ),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="model explorer uranium maximum supply curve",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_uranium_maximum_supply_curve_me": 3,
        "scenario_uranium_maximum_supply_curve_option_1_me": 1,
        "scenario_uranium_maximum_supply_curve_option_2_me": 1,
        "scenario_uranium_maximum_supply_curve_option_3_me": 1,
    },
)
def model_explorer_uranium_maximum_supply_curve():
    return if_then_else(
        select_uranium_maximum_supply_curve_me() == 1,
        lambda: scenario_uranium_maximum_supply_curve_option_1_me(),
        lambda: if_then_else(
            select_uranium_maximum_supply_curve_me() == 2,
            lambda: scenario_uranium_maximum_supply_curve_option_2_me(),
            lambda: if_then_else(
                select_uranium_maximum_supply_curve_me() == 3,
                lambda: scenario_uranium_maximum_supply_curve_option_3_me(),
                lambda: 0,
            ),
        ),
    )


@component.add(
    name="model explorer working time variation",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
        "initial_hours_per_worker": 7,
        "scenario_working_time_option_1_me": 1,
        "select_working_time_variation_me": 3,
        "final_year_working_time": 6,
        "scenario_working_time_option_3_me": 1,
        "scenario_working_time_option_2_me": 1,
    },
)
def model_explorer_working_time_variation():
    """
    Policy working time variation for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: initial_hours_per_worker(),
        lambda: if_then_else(
            select_working_time_variation_me() == 1,
            lambda: initial_hours_per_worker()
            + ramp(
                __data["time"],
                (scenario_working_time_option_1_me() * initial_hours_per_worker())
                / (final_year_working_time() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_working_time(),
            ),
            lambda: if_then_else(
                select_working_time_variation_me() == 2,
                lambda: initial_hours_per_worker()
                + ramp(
                    __data["time"],
                    (scenario_working_time_option_2_me() * initial_hours_per_worker())
                    / (final_year_working_time() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_working_time(),
                ),
                lambda: if_then_else(
                    select_working_time_variation_me() == 3,
                    lambda: initial_hours_per_worker()
                    + ramp(
                        __data["time"],
                        (
                            scenario_working_time_option_3_me()
                            * initial_hours_per_worker()
                        )
                        / (final_year_working_time() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_working_time(),
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "SECTORS I": _subscript_dict["SECTORS I"],
                        },
                        ["REGIONS 35 I", "SECTORS I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="SCENARIO BASELINE OPTION 2 ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_baseline_option_2_me"},
)
def scenario_baseline_option_2_me():
    """
    SCENARIO_BASELINE_OPTION_2_ME
    """
    return _ext_constant_scenario_baseline_option_2_me()


_ext_constant_scenario_baseline_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BASELINE_OPTION_2_ME",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_scenario_baseline_option_2_me",
)


@component.add(
    name="SCENARIO CLIMATE SENSITIVITY OPTION 1 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_1_me"
    },
)
def scenario_climate_sensitivity_option_1_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_1_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_1_me()


_ext_constant_scenario_climate_sensitivity_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_1_me",
)


@component.add(
    name="SCENARIO CLIMATE SENSITIVITY OPTION 2 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_2_me"
    },
)
def scenario_climate_sensitivity_option_2_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_2_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_2_me()


_ext_constant_scenario_climate_sensitivity_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_2_me",
)


@component.add(
    name="SCENARIO CLIMATE SENSITIVITY OPTION 3 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_climate_sensitivity_option_3_me"
    },
)
def scenario_climate_sensitivity_option_3_me():
    """
    SCENARIO_CLIMATE_SENSITIVITY_OPTION_3_ME
    """
    return _ext_constant_scenario_climate_sensitivity_option_3_me()


_ext_constant_scenario_climate_sensitivity_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_CLIMATE_SENSITIVITY_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_climate_sensitivity_option_3_me",
)


@component.add(
    name="SCENARIO DEBT INTEREST RATE TARGET OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_1_me"
    },
)
def scenario_debt_interest_rate_target_option_1_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_1_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_1_me()


_ext_constant_scenario_debt_interest_rate_target_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_1_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_1_me",
)


@component.add(
    name="SCENARIO DEBT INTEREST RATE TARGET OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_2_me"
    },
)
def scenario_debt_interest_rate_target_option_2_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_2_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_2_me()


_ext_constant_scenario_debt_interest_rate_target_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_2_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_2_me",
)


@component.add(
    name="SCENARIO DEBT INTEREST RATE TARGET OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_debt_interest_rate_target_option_3_me"
    },
)
def scenario_debt_interest_rate_target_option_3_me():
    """
    SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_3_ME
    """
    return _ext_constant_scenario_debt_interest_rate_target_option_3_me()


_ext_constant_scenario_debt_interest_rate_target_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DEBT_INTEREST_RATE_TARGET_OPTION_3_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_debt_interest_rate_target_option_3_me",
)


@component.add(
    name="SCENARIO ENERGY EFFICIENCY OPTION 1 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_1_me"},
)
def scenario_energy_efficiency_option_1_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_1_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_1_me()


_ext_constant_scenario_energy_efficiency_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_1_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_energy_efficiency_option_1_me",
)


@component.add(
    name="SCENARIO ENERGY EFFICIENCY OPTION 2 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_2_me"},
)
def scenario_energy_efficiency_option_2_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_2_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_2_me()


_ext_constant_scenario_energy_efficiency_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_2_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_energy_efficiency_option_2_me",
)


@component.add(
    name="SCENARIO ENERGY EFFICIENCY OPTION 3 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_energy_efficiency_option_3_me"},
)
def scenario_energy_efficiency_option_3_me():
    """
    SCENARIO_ENERGY_EFFICIENCY_OPTION_3_ME
    """
    return _ext_constant_scenario_energy_efficiency_option_3_me()


_ext_constant_scenario_energy_efficiency_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_ENERGY_EFFICIENCY_OPTION_3_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_energy_efficiency_option_3_me",
)


@component.add(
    name="SCENARIO FERTILITY RATES OPTION 1 ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_1_me"},
)
def scenario_fertility_rates_option_1_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_1_ME
    """
    return _ext_constant_scenario_fertility_rates_option_1_me()


_ext_constant_scenario_fertility_rates_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_1_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rates_option_1_me",
)


@component.add(
    name="SCENARIO FERTILITY RATES OPTION 2 ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_2_me"},
)
def scenario_fertility_rates_option_2_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_2_ME
    """
    return _ext_constant_scenario_fertility_rates_option_2_me()


_ext_constant_scenario_fertility_rates_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_2_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rates_option_2_me",
)


@component.add(
    name="SCENARIO FERTILITY RATES OPTION 3 ME",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rates_option_3_me"},
)
def scenario_fertility_rates_option_3_me():
    """
    SCENARIO_FERTILITY_RATES_OPTION_3_ME
    """
    return _ext_constant_scenario_fertility_rates_option_3_me()


_ext_constant_scenario_fertility_rates_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FERTILITY_RATES_OPTION_3_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rates_option_3_me",
)


@component.add(
    name="SCENARIO FINAL GENDER PARITY INDEX OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I", "EDUCATIONAL LEVEL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_1_me"
    },
)
def scenario_final_gender_parity_index_option_1_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_1_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_1_me()


_ext_constant_scenario_final_gender_parity_index_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_1_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["HIGH EDUCATION"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": _subscript_dict["EDUCATIONAL LEVEL I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_1_me",
)

_ext_constant_scenario_final_gender_parity_index_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_1_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["MEDIUM EDUCATION"],
    },
)


@component.add(
    name="SCENARIO FINAL GENDER PARITY INDEX OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I", "EDUCATIONAL LEVEL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_2_me"
    },
)
def scenario_final_gender_parity_index_option_2_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_2_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_2_me()


_ext_constant_scenario_final_gender_parity_index_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_2_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["HIGH EDUCATION"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": _subscript_dict["EDUCATIONAL LEVEL I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_2_me",
)

_ext_constant_scenario_final_gender_parity_index_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_2_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["MEDIUM EDUCATION"],
    },
)


@component.add(
    name="SCENARIO FINAL GENDER PARITY INDEX OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 35 I", "EDUCATIONAL LEVEL I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_final_gender_parity_index_option_3_me"
    },
)
def scenario_final_gender_parity_index_option_3_me():
    """
    SCENARIO_FINAL_GENDER_PARITY_INDEX_OPTION_3_ME
    """
    return _ext_constant_scenario_final_gender_parity_index_option_3_me()


_ext_constant_scenario_final_gender_parity_index_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_HIGH_OPTION_3_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["HIGH EDUCATION"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": _subscript_dict["EDUCATIONAL LEVEL I"],
    },
    "_ext_constant_scenario_final_gender_parity_index_option_3_me",
)

_ext_constant_scenario_final_gender_parity_index_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FINAL_GENDER_PARITY_INDEX_MEDIUM_OPTION_3_ME*",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "EDUCATIONAL LEVEL I": ["MEDIUM EDUCATION"],
    },
)


@component.add(
    name="SCENARIO FLEXITARIANA OPTION 1 ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_flexitariana_option_1_me"},
)
def scenario_flexitariana_option_1_me():
    """
    SCENARIO_FLEXITARIANA_OPTION_1_ME
    """
    return _ext_constant_scenario_flexitariana_option_1_me()


_ext_constant_scenario_flexitariana_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FLEXITARIANA_OPTION_1_ME",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_scenario_flexitariana_option_1_me",
)


@component.add(
    name="SCENARIO FORESTRY SELF SUFFICIENCY OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_1_me"
    },
)
def scenario_forestry_self_sufficiency_option_1_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_1_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_1_me()


_ext_constant_scenario_forestry_self_sufficiency_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_1_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_1_me",
)


@component.add(
    name="SCENARIO FORESTRY SELF SUFFICIENCY OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_2_me"
    },
)
def scenario_forestry_self_sufficiency_option_2_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_2_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_2_me()


_ext_constant_scenario_forestry_self_sufficiency_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_2_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_2_me",
)


@component.add(
    name="SCENARIO FORESTRY SELF SUFFICIENCY OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_forestry_self_sufficiency_option_3_me"
    },
)
def scenario_forestry_self_sufficiency_option_3_me():
    """
    SCENARIO_FOREST_OVEREXPLOITATION_OPTION_3_ME
    """
    return _ext_constant_scenario_forestry_self_sufficiency_option_3_me()


_ext_constant_scenario_forestry_self_sufficiency_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_FOREST_OVEREXPLOITATION_OPTION_3_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_forestry_self_sufficiency_option_3_me",
)


@component.add(
    name="SCENARIO GOVERMENT OPTION 1 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_1_me"},
)
def scenario_goverment_option_1_me():
    """
    SCENARIO_GOVERMENT_OPTION_1_ME
    """
    return _ext_constant_scenario_goverment_option_1_me()


_ext_constant_scenario_goverment_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_1_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_goverment_option_1_me",
)


@component.add(
    name="SCENARIO GOVERMENT OPTION 2 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_2_me"},
)
def scenario_goverment_option_2_me():
    """
    SCENARIO_GOVERMENT_OPTION_2_ME
    """
    return _ext_constant_scenario_goverment_option_2_me()


_ext_constant_scenario_goverment_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_2_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_goverment_option_2_me",
)


@component.add(
    name="SCENARIO GOVERMENT OPTION 3 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_goverment_option_3_me"},
)
def scenario_goverment_option_3_me():
    """
    SCENARIO_GOVERMENT_OPTION_3_ME
    """
    return _ext_constant_scenario_goverment_option_3_me()


_ext_constant_scenario_goverment_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_GOVERMENT_OPTION_3_ME*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_scenario_goverment_option_3_me",
)


@component.add(
    name="SCENARIO LAND PROTECTION BY POLICY OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_1_me"
    },
)
def scenario_land_protection_by_policy_option_1_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_1_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST MANAGED"]] = True
    def_subs.loc[:, ["FOREST PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_1_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_1_me",
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_1_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PRIMARY"]},
)


@component.add(
    name="SCENARIO LAND PROTECTION BY POLICY OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_2_me"
    },
)
def scenario_land_protection_by_policy_option_2_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_2_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST MANAGED"]] = True
    def_subs.loc[:, ["FOREST PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_2_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_2_me",
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_2_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PRIMARY"]},
)


@component.add(
    name="SCENARIO LAND PROTECTION BY POLICY OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_scenario_land_protection_by_policy_option_3_me"
    },
)
def scenario_land_protection_by_policy_option_3_me():
    """
    SCENARIO_LAND_PROTECTION_BY_POLICY_OPTION_3_ME
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, ["FOREST MANAGED"]] = True
    def_subs.loc[:, ["FOREST PRIMARY"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_scenario_land_protection_by_policy_option_3_me().values[
        def_subs.values
    ]
    value.loc[:, ["FOREST PLANTATIONS"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SOLAR LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    return value


_ext_constant_scenario_land_protection_by_policy_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_scenario_land_protection_by_policy_option_3_me",
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_CROPLAND_PROTECTION_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND IRRIGATED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_constant_scenario_land_protection_by_policy_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OPTION_3_POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PRIMARY"]},
)


@component.add(
    name="SCENARIO MANURE MANAGEMENT SYSTEM OPTION 1 ME",
    units="DMNL",
    subscripts=["ANIMALS TYPES I", "REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_1_me"
    },
)
def scenario_manure_management_system_option_1_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME
    """
    return _ext_constant_scenario_manure_management_system_option_1_me()


_ext_constant_scenario_manure_management_system_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEMS_OPTION_1_ME",
    {
        "ANIMALS TYPES I": ["DAIRY CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    _root,
    {
        "ANIMALS TYPES I": _subscript_dict["ANIMALS TYPES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    "_ext_constant_scenario_manure_management_system_option_1_me",
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS TYPES I": ["OTHER CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS TYPES I": ["BUFFALO"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_1_ME",
    {
        "ANIMALS TYPES I": ["SWINE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)


@component.add(
    name="SCENARIO MANURE MANAGEMENT SYSTEM OPTION 2 ME",
    units="DMNL",
    subscripts=["ANIMALS TYPES I", "REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_2_me"
    },
)
def scenario_manure_management_system_option_2_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME
    """
    return _ext_constant_scenario_manure_management_system_option_2_me()


_ext_constant_scenario_manure_management_system_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS TYPES I": ["DAIRY CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    _root,
    {
        "ANIMALS TYPES I": _subscript_dict["ANIMALS TYPES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    "_ext_constant_scenario_manure_management_system_option_2_me",
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS TYPES I": ["OTHER CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS TYPES I": ["BUFFALO"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_2_ME",
    {
        "ANIMALS TYPES I": ["SWINE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)


@component.add(
    name="SCENARIO MANURE MANAGEMENT SYSTEM OPTION 3 ME",
    units="DMNL",
    subscripts=["ANIMALS TYPES I", "REGIONS 9 I", "MANURE MANAGEMENT SYSTEM I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_manure_management_system_option_3_me"
    },
)
def scenario_manure_management_system_option_3_me():
    """
    SCENARIO_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME
    """
    return _ext_constant_scenario_manure_management_system_option_3_me()


_ext_constant_scenario_manure_management_system_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_DAIRY_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS TYPES I": ["DAIRY CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    _root,
    {
        "ANIMALS TYPES I": _subscript_dict["ANIMALS TYPES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
    "_ext_constant_scenario_manure_management_system_option_3_me",
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OTHER_CATTLE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS TYPES I": ["OTHER CATTLE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_BUFFALO_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS TYPES I": ["BUFFALO"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)

_ext_constant_scenario_manure_management_system_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SWINE_MANURE_MANAGEMENT_SYSTEM_OPTION_3_ME",
    {
        "ANIMALS TYPES I": ["SWINE"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "MANURE MANAGEMENT SYSTEM I": _subscript_dict["MANURE MANAGEMENT SYSTEM I"],
    },
)


@component.add(
    name="SCENARIO OBJECTIVE PERCENTAGE FE LIQUID SUBSTITUTED BY H2 SYNTHETIC LIQUID OPTION 1 ME",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_1_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_1_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_1_me",
)


@component.add(
    name="SCENARIO OBJECTIVE PERCENTAGE FE LIQUID SUBSTITUTED BY H2 SYNTHETIC LIQUID OPTION 2 ME",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_2_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_2_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_2_me",
)


@component.add(
    name="SCENARIO OBJECTIVE PERCENTAGE FE LIQUID SUBSTITUTED BY H2 SYNTHETIC LIQUID OPTION 3 ME",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me"
    },
)
def scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me():
    """
    SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ OPTION_3_ME
    """
    return (
        _ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me()
    )


_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_OPTION_3_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_objective_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_option_3_me",
)


@component.add(
    name="SCENARIO OIL RESOURCE OPTION 1 ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_1_me"},
)
def scenario_oil_resource_option_1_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_1_ME
    """
    return _ext_constant_scenario_oil_resource_option_1_me()


_ext_constant_scenario_oil_resource_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_1_me",
)


@component.add(
    name="SCENARIO OIL RESOURCE OPTION 2 ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_2_me"},
)
def scenario_oil_resource_option_2_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_2_ME
    """
    return _ext_constant_scenario_oil_resource_option_2_me()


_ext_constant_scenario_oil_resource_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_2_me",
)


@component.add(
    name="SCENARIO OIL RESOURCE OPTION 3 ME",
    units="bbl",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_oil_resource_option_3_me"},
)
def scenario_oil_resource_option_3_me():
    """
    SCENARIO_OIL_RESOURCE_OPTION_3_ME
    """
    return _ext_constant_scenario_oil_resource_option_3_me()


_ext_constant_scenario_oil_resource_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_OIL_RESOURCE_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_oil_resource_option_3_me",
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND MODAL SHARE OPTION 1 ME",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_1_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_1_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_1_ME",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_1_ME",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBILC_OPTION_1_ME",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_1_ME",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_1_ME",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_1_ME",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_1_ME",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_1_ME",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_1_ME",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_1_ME",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_1_ME",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_1_ME",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NEHTERLANDS_OPTION_1_ME",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_1_ME",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_1_ME",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_1_ME",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_1_ME",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_1_ME",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_1_ME",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_1_ME",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_1_ME",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_1_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_1_ME",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND MODAL SHARE OPTION 2 ME",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_2_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_2_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_2_ME",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_2_ME",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBLIC_OPTION_2_ME",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_2_ME",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_2_ME",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_2_ME",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_2_ME",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_2_ME",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_2_ME",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_2_ME",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_2_ME",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_2_ME",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NETHERLANDS_OPTION_2_ME",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_2_ME",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_2_ME",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_2_ME",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_2_ME",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_2_ME",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_2_ME",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_2_ME",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_2_ME",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_2_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_2_ME",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND MODAL SHARE OPTION 3 ME",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me"
    },
)
def scenario_passenger_transport_demand_modal_share_option_3_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_OPTION_3_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me()


_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_AUSTRIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me",
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BELGIUM_OPTION_3_ME",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_BULGARIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CROATIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CYPRUS_OPTION_3_ME",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CZECH_REPUBLIC_OPTION_3_ME",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_DENMARK_OPTION_3_ME",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ESTONIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FINLAND_OPTION_3_ME",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_FRANCE_OPTION_3_ME",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GERMANY_OPTION_3_ME",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_GREECE_OPTION_3_ME",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_HUNGARY_OPTION_3_ME",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_IRELAND_OPTION_3_ME",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ITALY_OPTION_3_ME",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATVIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LITHUANIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LUXEMBOURG_OPTION_3_ME",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_MALTA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_NETHERLANDS_OPTION_3_ME",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_POLAND_OPTION_3_ME",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_PORTUGAL_OPTION_3_ME",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_ROMANIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVAKIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SLOVENIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SPAIN_OPTION_3_ME",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_SWEDEN_OPTION_3_ME",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_UK_OPTION_3_ME",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_CHINA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_EASOC_OPTION_3_ME",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_INDIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LATAM_OPTION_3_ME",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_RUSSIA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_USMCA_OPTION_3_ME",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_scenario_passenger_transport_demand_modal_share_option_3_me.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "OBJECTIVE_PASSENGER_DEMAND_SHARE_LROW_OPTION_3_ME",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND OPTION 1 ME",
    units="DMNL",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_1_me"
    },
)
def scenario_passenger_transport_demand_option_1_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_1_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_1_me()


_ext_constant_scenario_passenger_transport_demand_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_1_ME",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_1_me",
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND OPTION 2 ME",
    units="DMNL",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_2_me"
    },
)
def scenario_passenger_transport_demand_option_2_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_2_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_2_me()


_ext_constant_scenario_passenger_transport_demand_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_2_ME",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_2_me",
)


@component.add(
    name="SCENARIO PASSENGER TRANSPORT DEMAND OPTION 3 ME",
    units="DMNL",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_passenger_transport_demand_option_3_me"
    },
)
def scenario_passenger_transport_demand_option_3_me():
    """
    SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_3_ME
    """
    return _ext_constant_scenario_passenger_transport_demand_option_3_me()


_ext_constant_scenario_passenger_transport_demand_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PASSENGER_TRANSPORT_DEMAND_OPTION_3_ME",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_scenario_passenger_transport_demand_option_3_me",
)


@component.add(
    name="SCENARIO PLANT BASED 100 OPTION 3 ME",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_plant_based_100_option_3_me"},
)
def scenario_plant_based_100_option_3_me():
    """
    SCENARIO_PLANT_BASED_100_OPTION_3_ME
    """
    return _ext_constant_scenario_plant_based_100_option_3_me()


_ext_constant_scenario_plant_based_100_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PLANT_BASED_100_OPTION_3_ME",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_scenario_plant_based_100_option_3_me",
)


@component.add(
    name="SCENARIO PROTRA EXPANSION OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_1_me"},
)
def scenario_protra_expansion_option_1_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_1_ME
    """
    return _ext_constant_scenario_protra_expansion_option_1_me()


_ext_constant_scenario_protra_expansion_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_1_ME*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_scenario_protra_expansion_option_1_me",
)


@component.add(
    name="SCENARIO PROTRA EXPANSION OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_2_me"},
)
def scenario_protra_expansion_option_2_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_2_ME
    """
    return _ext_constant_scenario_protra_expansion_option_2_me()


_ext_constant_scenario_protra_expansion_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_2_ME*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_scenario_protra_expansion_option_2_me",
)


@component.add(
    name="SCENARIO PROTRA EXPANSION OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_protra_expansion_option_3_me"},
)
def scenario_protra_expansion_option_3_me():
    """
    SCENARIO_PROTRA_EXPANSION_OPTION_3_ME
    """
    return _ext_constant_scenario_protra_expansion_option_3_me()


_ext_constant_scenario_protra_expansion_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_PROTRA_EXPANSION_OPTION_3_ME*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_scenario_protra_expansion_option_3_me",
)


@component.add(
    name="SCENARIO SELECT CHANGE TO REGENERATIVE AGRICULTURE OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_1_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_1_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_1_ME*",
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        _root,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_1_me",
    )
)


@component.add(
    name="SCENARIO SELECT CHANGE TO REGENERATIVE AGRICULTURE OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_2_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_2_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_2_ME*",
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        _root,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_2_me",
    )
)


@component.add(
    name="SCENARIO SELECT CHANGE TO REGENERATIVE AGRICULTURE OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me"
    },
)
def scenario_select_change_to_regenerative_agriculture_option_3_me():
    """
    SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_3_ME
    """
    return (
        _ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me()
    )


_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "data_model_explorer",
        "SCENARIO_SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_OPTION_3_ME*",
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        _root,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        "_ext_constant_scenario_select_change_to_regenerative_agriculture_option_3_me",
    )
)


@component.add(
    name="SCENARIO SHARE DIETS ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_share_diets_me"},
)
def scenario_share_diets_me():
    """
    Percent of population
    """
    return _ext_constant_scenario_share_diets_me()


_ext_constant_scenario_share_diets_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_SHARE_DIETS_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_share_diets_me",
)


@component.add(
    name="SCENARIO TARGET SHARE BIOENERGY IN FOSSIL LIQUIDS AND GASES OPTION 1 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_1_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_1_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_1_me",
)


@component.add(
    name="SCENARIO TARGET SHARE BIOENERGY IN FOSSIL LIQUIDS AND GASES OPTION 2 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_2_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_2_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_2_me",
)


@component.add(
    name="SCENARIO TARGET SHARE BIOENERGY IN FOSSIL LIQUIDS AND GASES OPTION 3 ME",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me"
    },
)
def scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me():
    """
    SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_3_ME
    """
    return (
        _ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me()
    )


_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_OPTION_3_ME*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_scenario_target_share_bioenergy_in_fossil_liquids_and_gases_option_3_me",
)


@component.add(
    name="SCENARIO URANIUM MAXIMUM SUPPLY CURVE OPTION 1 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_1_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_1_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_1_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_1_me",
)


@component.add(
    name="SCENARIO URANIUM MAXIMUM SUPPLY CURVE OPTION 2 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_2_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_2_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_2_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_2_me",
)


@component.add(
    name="SCENARIO URANIUM MAXIMUM SUPPLY CURVE OPTION 3 ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me"
    },
)
def scenario_uranium_maximum_supply_curve_option_3_me():
    return _ext_constant_scenario_uranium_maximum_supply_curve_option_3_me()


_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_URANIUM_MAXIMUM_SUPPLY_CURVE_OPTION_3_ME",
    {},
    _root,
    {},
    "_ext_constant_scenario_uranium_maximum_supply_curve_option_3_me",
)


@component.add(
    name="SCENARIO WORKING TIME OPTION 1 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_1_me"},
)
def scenario_working_time_option_1_me():
    """
    SCENARIO_WORKING_TIME_OPTION_1_ME
    """
    return _ext_constant_scenario_working_time_option_1_me()


_ext_constant_scenario_working_time_option_1_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_1_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_scenario_working_time_option_1_me",
)


@component.add(
    name="SCENARIO WORKING TIME OPTION 2 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_2_me"},
)
def scenario_working_time_option_2_me():
    """
    SCENARIO_WORKING_TIME_OPTION_2_ME
    """
    return _ext_constant_scenario_working_time_option_2_me()


_ext_constant_scenario_working_time_option_2_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_2_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_scenario_working_time_option_2_me",
)


@component.add(
    name="SCENARIO WORKING TIME OPTION 3 ME",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_working_time_option_3_me"},
)
def scenario_working_time_option_3_me():
    """
    SCENARIO_WORKING_TIME_OPTION_3_ME
    """
    return _ext_constant_scenario_working_time_option_3_me()


_ext_constant_scenario_working_time_option_3_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "data_model_explorer",
    "SCENARIO_WORKING_TIME_OPTION_3_ME",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_scenario_working_time_option_3_me",
)


@component.add(
    name="SELECT CHANGE TO REGENERATIVE AGRICULTURE ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_change_to_regenerative_agriculture_me"
    },
)
def select_change_to_regenerative_agriculture_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_change_to_regenerative_agriculture_me()


_ext_constant_select_change_to_regenerative_agriculture_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_CHANGE_TO_REGENERATIVE_AGRICULTURE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_change_to_regenerative_agriculture_me",
)


@component.add(
    name="SELECT CLIMATE SENSITIVITY ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_climate_sensitivity_me"},
)
def select_climate_sensitivity_me():
    """
    1: Application of 2.5 as climate sensitivity value 2: Application of 3 as climate sensitivity value 3: Application of 4 as climate sensitivity value
    """
    return _ext_constant_select_climate_sensitivity_me()


_ext_constant_select_climate_sensitivity_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_CLIMATE_SENSITIVITY_ME",
    {},
    _root,
    {},
    "_ext_constant_select_climate_sensitivity_me",
)


@component.add(
    name="SELECT DEBT INTEREST RATE TARGET ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_debt_interest_rate_target_me"},
)
def select_debt_interest_rate_target_me():
    """
    1: Less than current debt interest rate 2: Current debt interest rate 3: More than current debt interest rate
    """
    return _ext_constant_select_debt_interest_rate_target_me()


_ext_constant_select_debt_interest_rate_target_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_DEBT_INTEREST_RATE_TARGET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_debt_interest_rate_target_me",
)


@component.add(
    name="SELECT ENERGY EFFICIENCY ANNUAL IMPROVEMENT ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_energy_efficiency_annual_improvement_me"
    },
)
def select_energy_efficiency_annual_improvement_me():
    """
    1: Less than current energy efficiency improvement 2: Current trends energy efficiency improvement 3: More than current energy efficiency improvement
    """
    return _ext_constant_select_energy_efficiency_annual_improvement_me()


_ext_constant_select_energy_efficiency_annual_improvement_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_ENERGY_EFFICIENCY_ANNUAL_IMPROVEMENT_ME",
    {},
    _root,
    {},
    "_ext_constant_select_energy_efficiency_annual_improvement_me",
)


@component.add(
    name="SELECT FERTILITY RATES ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_fertility_rates_me"},
)
def select_fertility_rates_me():
    """
    1: LOW FERTILITY RATES 2: MEDIUM FERTILITY RATES 3: HIGH FERTILITY RATES
    """
    return _ext_constant_select_fertility_rates_me()


_ext_constant_select_fertility_rates_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FERTILITY_RATES_ME",
    {},
    _root,
    {},
    "_ext_constant_select_fertility_rates_me",
)


@component.add(
    name="SELECT FINAL GENDER PARITY INDEX ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_final_gender_parity_index_me"},
)
def select_final_gender_parity_index_me():
    """
    1: No policy (current trends) 2: Medium level of policy implementation 3: Total gender parity in education
    """
    return _ext_constant_select_final_gender_parity_index_me()


_ext_constant_select_final_gender_parity_index_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FINAL_GENDER_PARITY_INDEX_ME",
    {},
    _root,
    {},
    "_ext_constant_select_final_gender_parity_index_me",
)


@component.add(
    name="SELECT FORESTRY SELF SUFFICIENCY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_forestry_self_sufficiency"},
)
def select_forestry_self_sufficiency():
    """
    1: Forestry explotation for other regions allowed 2: Only 50% of explotation for other regions allowed 3: Self-Suficient forestrexplotation
    """
    return _ext_constant_select_forestry_self_sufficiency()


_ext_constant_select_forestry_self_sufficiency = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_FORESTRY_SELF_SUFFICIENCY",
    {},
    _root,
    {},
    "_ext_constant_select_forestry_self_sufficiency",
)


@component.add(
    name="SELECT GOVERNMENT BUDGET BALANCE TO GDP OBJECTIVE TARGET ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_government_budget_balance_to_gdp_objective_target_me"
    },
)
def select_government_budget_balance_to_gdp_objective_target_me():
    """
    1: Less than current GDP objetive 2: Current GDP objetive 3: More than current GDP objetive
    """
    return _ext_constant_select_government_budget_balance_to_gdp_objective_target_me()


_ext_constant_select_government_budget_balance_to_gdp_objective_target_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_government_budget_balance_to_gdp_objective_target_me",
)


@component.add(
    name="SELECT LAND PROTECTION BY POLICY ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_land_protection_by_policy_me"},
)
def select_land_protection_by_policy_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_land_protection_by_policy_me()


_ext_constant_select_land_protection_by_policy_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_LAND_PROTECTION_BY_POLICY_ME",
    {},
    _root,
    {},
    "_ext_constant_select_land_protection_by_policy_me",
)


@component.add(
    name="SELECT MANURE MANAGEMENT SYSTEM ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_manure_management_system_me"},
)
def select_manure_management_system_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_manure_management_system_me()


_ext_constant_select_manure_management_system_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_MANURE_MANAGEMENT_SYSTEM_ME",
    {},
    _root,
    {},
    "_ext_constant_select_manure_management_system_me",
)


@component.add(
    name="SELECT OIL RESOURCE ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_oil_resource_me"},
)
def select_oil_resource_me():
    """
    1: Low level of oil resources 2: Medium level of oil resources 3: High level of oil resources
    """
    return _ext_constant_select_oil_resource_me()


_ext_constant_select_oil_resource_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_OIL_RESOURCE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_oil_resource_me",
)


@component.add(
    name="SELECT PASSENGER TRANSPORT DEMAND MODAL SHARE ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_passenger_transport_demand_modal_share_me"
    },
)
def select_passenger_transport_demand_modal_share_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_passenger_transport_demand_modal_share_me()


_ext_constant_select_passenger_transport_demand_modal_share_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_ME",
    {},
    _root,
    {},
    "_ext_constant_select_passenger_transport_demand_modal_share_me",
)


@component.add(
    name="SELECT PERCENTAGE FE LIQUID SUBSTITUTED BY H2 SYNTHETIC LIQUID ME",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me"
    },
)
def select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me():
    """
    1: LOW LEVEL OF POLICY IMPLEMENTATION 2: MEEDIUM LEVEL OF POLICY IMPLEMENTATION 3: HIGH LEVEL OF POLICY IMPLEMENTATION
    """
    return (
        _ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me()
    )


_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_SYNTHETIC_LIQUID_ME",
    {},
    _root,
    {},
    "_ext_constant_select_percentage_fe_liquid_substituted_by_h2_synthetic_liquid_me",
)


@component.add(
    name="SELECT PROTRA CAPACITY EXPANSION PRIORITIES VECTOR ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_protra_capacity_expansion_priorities_vector_me"
    },
)
def select_protra_capacity_expansion_priorities_vector_me():
    """
    1: Back to fossil and uranium energies 2: Current trends 3: Rapid implementaion of renewable energies
    """
    return _ext_constant_select_protra_capacity_expansion_priorities_vector_me()


_ext_constant_select_protra_capacity_expansion_priorities_vector_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_ME",
    {},
    _root,
    {},
    "_ext_constant_select_protra_capacity_expansion_priorities_vector_me",
)


@component.add(
    name="SELECT RCP GHG EMISSIONS ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_rcp_ghg_emissions_me"},
)
def select_rcp_ghg_emissions_me():
    """
    1: APPLICATION OF RCP 2.6 2: APPLICATION OF RCP 4.5 3: APPLICATION OF RCP 6 4: APPLICATION OF RCP 8.5
    """
    return _ext_constant_select_rcp_ghg_emissions_me()


_ext_constant_select_rcp_ghg_emissions_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_RCP_GHG_EMISSIONS_ME",
    {},
    _root,
    {},
    "_ext_constant_select_rcp_ghg_emissions_me",
)


@component.add(
    name="SELECT REDUCTION PASSENGER TRANSPORT DEMAND ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_reduction_passenger_transport_demand_me"
    },
)
def select_reduction_passenger_transport_demand_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_reduction_passenger_transport_demand_me()


_ext_constant_select_reduction_passenger_transport_demand_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_REDUCTION_PASSENGER_TRANSPORT_DEMAND_ME",
    {},
    _root,
    {},
    "_ext_constant_select_reduction_passenger_transport_demand_me",
)


@component.add(
    name="SELECT TARGET SHARE BIOENERGY IN FOSSIL LIQUIDS AND GASES ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me"
    },
)
def select_target_share_bioenergy_in_fossil_liquids_and_gases_me():
    """
    1: No policy 2: Medium level of policy implementation 3: High level of policy implementation
    """
    return _ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me()


_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "inputs_model_explorer",
        "SELECT_TARGET_SHARE_BIOENERGY_IN_FOSSIL_LIQUIDS_AND_GASES_ME",
        {},
        _root,
        {},
        "_ext_constant_select_target_share_bioenergy_in_fossil_liquids_and_gases_me",
    )
)


@component.add(
    name="SELECT TIPE DIETS ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_tipe_diets_me"},
)
def select_tipe_diets_me():
    """
    1: 30% of population with flexitarian diet 2: Baseline diet patterns 3: 30% of population with 100% plant based diet
    """
    return _ext_constant_select_tipe_diets_me()


_ext_constant_select_tipe_diets_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_SHARE_OF_CHANGE_TO_POLICY_DIET_ME",
    {},
    _root,
    {},
    "_ext_constant_select_tipe_diets_me",
)


@component.add(
    name="SELECT WORKING TIME VARIATION ME",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_working_time_variation_me"},
)
def select_working_time_variation_me():
    """
    1: Less than current working time 2: Current working time 3: More than current working time
    """
    return _ext_constant_select_working_time_variation_me()


_ext_constant_select_working_time_variation_me = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SELECT_WORKING_TIME_VARIATION_ME",
    {},
    _root,
    {},
    "_ext_constant_select_working_time_variation_me",
)
