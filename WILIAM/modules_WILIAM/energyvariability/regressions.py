"""
Module energyvariability.regressions
Translated using PySD version 3.13.4
"""

@component.add(
    name="CF PHS storage",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_phs_storage():
    """
    capacity factor of pumped hydro storage - constant for now might change with new regression approach
    """
    return xr.DataArray(
        0.1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="CF PROSTO",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROSTO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_v2g_storage_9r": 1,
        "cf_phs_storage": 1,
        "cf_stationary_batteries": 1,
    },
)
def cf_prosto():
    """
    Capacity factor of utility-scale storage facilities.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROSTO I": _subscript_dict["NRG PROSTO I"],
        },
        ["REGIONS 9 I", "NRG PROSTO I"],
    )
    value.loc[:, ["PROSTO V2G"]] = (
        cf_v2g_storage_9r().expand_dims({"NRG PRO I": ["PROSTO V2G"]}, 1).values
    )
    value.loc[:, ["PROSTO PHS"]] = (
        cf_phs_storage().expand_dims({"NRG PRO I": ["PROSTO PHS"]}, 1).values
    )
    value.loc[:, ["PROSTO STATIONARY BATTERIES"]] = (
        cf_stationary_batteries()
        .expand_dims({"NRG PRO I": ["PROSTO STATIONARY BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="CF stationary batteries",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_stationary_batteries():
    """
    capacity factor of staitonary batteries - constant for now
    """
    return xr.DataArray(
        0.1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="CF V2G storage",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def cf_v2g_storage():
    """
    Capacity factor of V2G, defined as output from storage (after the charger) divided by the power of V2G.
    """
    return xr.DataArray(
        0.01, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    )


@component.add(
    name="CF V2G storage 9R",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cf_v2g_storage": 2},
)
def cf_v2g_storage_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        cf_v2g_storage()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"]] = sum(
        cf_v2g_storage()
        .loc[_subscript_dict["REGIONS EU27 I"]]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    ) / len(
        xr.DataArray(
            np.arange(1, len(_subscript_dict["REGIONS EU27 I"]) + 1),
            {"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]},
            ["REGIONS EU27 I"],
        )
    )
    return value


@component.add(
    name="check ranges",
    units="DMNL",
    subscripts=["REGIONS 9 I", "BASIC PREDICTORS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 2,
        "minimum_predictors_variability_regression": 1,
        "maximum_predictors_variability_regression": 1,
    },
)
def check_ranges():
    """
    Check if predictors are within the range (0) or not (1)
    """
    return if_then_else(
        np.logical_or(
            predictors_all()
            .loc[:, _subscript_dict["BASIC PREDICTORS NGR VARIABILITY I"]]
            .rename(
                {"PREDICTORS NGR VARIABILITY I": "BASIC PREDICTORS NGR VARIABILITY I"}
            )
            < minimum_predictors_variability_regression(),
            predictors_all()
            .loc[:, _subscript_dict["BASIC PREDICTORS NGR VARIABILITY I"]]
            .rename(
                {"PREDICTORS NGR VARIABILITY I": "BASIC PREDICTORS NGR VARIABILITY I"}
            )
            > maximum_predictors_variability_regression(),
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
                    "BASIC PREDICTORS NGR VARIABILITY I"
                ],
            },
            ["REGIONS 9 I", "BASIC PREDICTORS NGR VARIABILITY I"],
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
                    "BASIC PREDICTORS NGR VARIABILITY I"
                ],
            },
            ["REGIONS 9 I", "BASIC PREDICTORS NGR VARIABILITY I"],
        ),
    )


@component.add(
    name="checking linear regression models energy variability",
    units="DMNL",
    subscripts=["REGIONS 9 I", "OUTPUTS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_variability_linear_regression_intercept": 3,
        "individual_linear_regression_terms_energy_variability": 3,
    },
)
def checking_linear_regression_models_energy_variability():
    """
    Calculation of the regression model (independent term + sum(Coefficients * predictors)) to consider the variability of renewable energy. For linear functions, it is assumed a range to be between [0, 1], in order to avoid errors.
    """
    return if_then_else(
        energy_variability_linear_regression_intercept()
        + sum(
            individual_linear_regression_terms_energy_variability().rename(
                {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
            ),
            dim=["PREDICTORS NGR VARIABILITY I!"],
        ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I")
        > 1,
        lambda: xr.DataArray(
            1,
            {
                "OUTPUTS NGR VARIABILITY I": _subscript_dict[
                    "OUTPUTS NGR VARIABILITY I"
                ],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"],
        ),
        lambda: if_then_else(
            energy_variability_linear_regression_intercept()
            + sum(
                individual_linear_regression_terms_energy_variability().rename(
                    {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
                ),
                dim=["PREDICTORS NGR VARIABILITY I!"],
            ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I")
            < 0,
            lambda: xr.DataArray(
                0,
                {
                    "OUTPUTS NGR VARIABILITY I": _subscript_dict[
                        "OUTPUTS NGR VARIABILITY I"
                    ],
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                },
                ["OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"],
            ),
            lambda: energy_variability_linear_regression_intercept()
            + sum(
                individual_linear_regression_terms_energy_variability().rename(
                    {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
                ),
                dim=["PREDICTORS NGR VARIABILITY I!"],
            ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"),
        ),
    ).transpose("REGIONS 9 I", "OUTPUTS NGR VARIABILITY I")


@component.add(
    name="checking logistic regression models energy variability",
    units="DMNL",
    subscripts=["REGIONS 9 I", "OUTPUTS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_variability_logistic_regression_intercept": 3,
        "individual_logistic_regression_terms_energy_variability": 3,
    },
)
def checking_logistic_regression_models_energy_variability():
    """
    Calculation of the regression model (independent term + sum(Coefficients * predictors)) to consider the variability of renewable energy. For logistic functions, it is assumed a range to be between [-10, 10], in order to avoid errors.
    """
    return if_then_else(
        energy_variability_logistic_regression_intercept()
        + sum(
            individual_logistic_regression_terms_energy_variability().rename(
                {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
            ),
            dim=["PREDICTORS NGR VARIABILITY I!"],
        ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I")
        > 10,
        lambda: xr.DataArray(
            10,
            {
                "OUTPUTS NGR VARIABILITY I": _subscript_dict[
                    "OUTPUTS NGR VARIABILITY I"
                ],
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            },
            ["OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"],
        ),
        lambda: if_then_else(
            energy_variability_logistic_regression_intercept()
            + sum(
                individual_logistic_regression_terms_energy_variability().rename(
                    {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
                ),
                dim=["PREDICTORS NGR VARIABILITY I!"],
            ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I")
            < -10,
            lambda: xr.DataArray(
                -10,
                {
                    "OUTPUTS NGR VARIABILITY I": _subscript_dict[
                        "OUTPUTS NGR VARIABILITY I"
                    ],
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                },
                ["OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"],
            ),
            lambda: energy_variability_logistic_regression_intercept()
            + sum(
                individual_logistic_regression_terms_energy_variability().rename(
                    {"PREDICTORS NGR VARIABILITY I": "PREDICTORS NGR VARIABILITY I!"}
                ),
                dim=["PREDICTORS NGR VARIABILITY I!"],
            ).transpose("OUTPUTS NGR VARIABILITY I", "REGIONS 9 I"),
        ),
    ).transpose("REGIONS 9 I", "OUTPUTS NGR VARIABILITY I")


@component.add(
    name="EXOGENOUS PREDICTORS ENERGY VARIABILITY REGRESSIONS",
    units="DMNL",
    subscripts=["BASIC PREDICTORS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_exogenous_predictors_energy_variability_regressions"
    },
)
def exogenous_predictors_energy_variability_regressions():
    """
    INPUTS_ENERGY_VARIABILITY_REGRESSION
    """
    return _ext_constant_exogenous_predictors_energy_variability_regressions()


_ext_constant_exogenous_predictors_energy_variability_regressions = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INPUTS_ENERGY_VARIABILITY_REGRESSION",
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    _root,
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    "_ext_constant_exogenous_predictors_energy_variability_regressions",
)


@component.add(
    name="hourly average power elec demand",
    units="MW*TWh/(TW*h)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "legacy_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_hours_year": 1,
    },
)
def hourly_average_power_elec_demand():
    """
    1 year = 8760 hours
    """
    return legacy_elec_demand() * unit_conversion_mw_tw() / unit_conversion_hours_year()


@component.add(
    name="HOURLY AVERAGE POWER ELEC DEMAND EnergyPLAN",
    units="MW*TWh/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_hours_year": 1,
    },
)
def hourly_average_power_elec_demand_energyplan():
    return (
        legacy_elec_demand_energyplan()
        * unit_conversion_mw_tw()
        / unit_conversion_hours_year()
    )


@component.add(
    name="individual linear regression terms energy variability",
    units="DMNL",
    subscripts=[
        "REGIONS 9 I",
        "OUTPUTS NGR VARIABILITY I",
        "PREDICTORS NGR VARIABILITY I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 1,
        "energy_variability_linear_regression_coefficients": 1,
    },
)
def individual_linear_regression_terms_energy_variability():
    """
    Calculation of individual terms in the multiple linear regression models to consider the variability of renewable energy
    """
    return (
        predictors_all()
        * energy_variability_linear_regression_coefficients().transpose(
            "PREDICTORS NGR VARIABILITY I", "OUTPUTS NGR VARIABILITY I"
        )
    ).transpose(
        "REGIONS 9 I", "OUTPUTS NGR VARIABILITY I", "PREDICTORS NGR VARIABILITY I"
    )


@component.add(
    name="individual logistic regression terms energy variability",
    units="DMNL",
    subscripts=[
        "REGIONS 9 I",
        "OUTPUTS NGR VARIABILITY I",
        "PREDICTORS NGR VARIABILITY I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictors_all": 1,
        "energy_variability_logistic_regression_coefficients": 1,
    },
)
def individual_logistic_regression_terms_energy_variability():
    """
    Calculation of individual terms in the regression models to consider the variability of renewable energy
    """
    return (
        predictors_all()
        * energy_variability_logistic_regression_coefficients().transpose(
            "PREDICTORS NGR VARIABILITY I", "OUTPUTS NGR VARIABILITY I"
        )
    ).transpose(
        "REGIONS 9 I", "OUTPUTS NGR VARIABILITY I", "PREDICTORS NGR VARIABILITY I"
    )


@component.add(
    name="legacy elec demand",
    units="TWh/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "legacy_elec_demand_energyplan": 1,
        "fe_excluding_trade": 1,
        "unit_conversion_twh_ej": 1,
    },
)
def legacy_elec_demand():
    """
    Reference of legacy demand for the regression models for the renewable variability management
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            legacy_elec_demand_energyplan(),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE elec"].reset_coords(drop=True)
        * unit_conversion_twh_ej(),
    )


@component.add(
    name="LEGACY ELEC DEMAND EnergyPLAN",
    units="TWh/Year",
    comp_type="Constant",
    comp_subtype="Normal",
)
def legacy_elec_demand_energyplan():
    """
    Base value of the EnergyPLAN experimental design
    """
    return 100


@component.add(
    name="outputs linear regression",
    units="DMNL",
    subscripts=["REGIONS 9 I", "OUTPUTS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"checking_linear_regression_models_energy_variability": 1},
)
def outputs_linear_regression():
    """
    Outputs of the linear regression models taking into account variable renewable energies
    """
    return checking_linear_regression_models_energy_variability()


@component.add(
    name="outputs logistic regression",
    units="Dnml",
    subscripts=["REGIONS 9 I", "OUTPUTS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"checking_logistic_regression_models_energy_variability": 1},
)
def outputs_logistic_regression():
    """
    Outputs of the logistic regression models taking into account variable renewable energies
    """
    return 1 / (1 + np.exp(-checking_logistic_regression_models_energy_variability()))


@component.add(
    name="predictor 10 v2g",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "ev_batteries_power_v2g_9r": 1,
    },
)
def predictor_10_v2g():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR V2G"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: ev_batteries_power_v2g_9r()
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 11 hydrogen FE demand",
    units="TWh/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "fe_excluding_trade": 1,
        "legacy_elec_demand": 1,
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_twh_ej": 1,
    },
)
def predictor_11_hydrogen_fe_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR HYDROGEN DEMAND"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / legacy_elec_demand(),
    )


@component.add(
    name="predictor 12 hydrogen supply",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "flexible_electrolysers_capacity_stock": 1,
    },
)
def predictor_12_hydrogen_supply():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR HYDROGEN SUPPLY"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: flexible_electrolysers_capacity_stock()
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 13 flexible demand",
    units="TWh/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "switch_flex_elec_demand_sp": 3,
        "initial_year_flex_elec_demand_sp": 3,
        "objective_flex_elec_demand_sp": 2,
        "year_final_flex_elec_demand_sp": 3,
        "time": 3,
    },
)
def predictor_13_flexible_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR FLEX DEMAND"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: if_then_else(
            switch_flex_elec_demand_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_flex_elec_demand_sp() == 1,
                    time() < initial_year_flex_elec_demand_sp(),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: if_then_else(
                    np.logical_and(
                        switch_flex_elec_demand_sp() == 1,
                        time() > year_final_flex_elec_demand_sp(),
                    ),
                    lambda: objective_flex_elec_demand_sp(),
                    lambda: ramp(
                        __data["time"],
                        objective_flex_elec_demand_sp()
                        / (
                            year_final_flex_elec_demand_sp()
                            - initial_year_flex_elec_demand_sp()
                        ),
                        initial_year_flex_elec_demand_sp(),
                        year_final_flex_elec_demand_sp(),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="predictor 1 PROTRA PP solar",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "protra_operative_capacity_stock_selected": 2,
    },
)
def predictor_1_protra_pp_solar():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR SOLAR"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: (
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP solar CSP"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 2 PROTRA PP wind",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "protra_operative_capacity_stock_selected": 2,
    },
)
def predictor_2_protra_pp_wind():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR WIND"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: (
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP wind offshore"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP wind onshore"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 3 capacity zero ghg semiflex",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "protra_operative_capacity_stock_selected": 4,
    },
)
def predictor_3_capacity_zero_ghg_semiflex():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR ZERO GHG SEMIFLEX"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: (
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP nuclear"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP geothermal"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP hydropower run of river"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA PP hydropower dammed"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 4 stationary storage",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand_energyplan": 2,
        "prosto_capacity_stock": 2,
        "ev_batteries_power_sc": 2,
        "ev_batteries_power_v2g": 2,
        "hourly_average_power_elec_demand": 2,
        "unit_conversion_mw_tw": 2,
    },
)
def predictor_4_stationary_storage():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_nrg_variability() == 0,
        lambda: float(
            exogenous_predictors_energy_variability_regressions().loc[
                "PREDICTOR STATIONARY STORAGE"
            ]
        ),
        lambda: (
            sum(
                ev_batteries_power_v2g()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            )
            + sum(
                ev_batteries_power_sc()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            )
            + sum(
                prosto_capacity_stock()
                .loc["EU27", _subscript_dict["PROSTO ELEC DEDICATED I"]]
                .reset_coords(drop=True)
                .rename({"NRG PROSTO I": "PROSTO ELEC DEDICATED I!"}),
                dim=["PROSTO ELEC DEDICATED I!"],
            )
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / float(hourly_average_power_elec_demand().loc["EU27"]),
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        + ev_batteries_power_sc()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        + sum(
            prosto_capacity_stock()
            .loc[
                _subscript_dict["REGIONS 8 I"],
                _subscript_dict["PROSTO ELEC DEDICATED I"],
            ]
            .rename(
                {
                    "REGIONS 9 I": "REGIONS 8 I",
                    "NRG PROSTO I": "PROSTO ELEC DEDICATED I!",
                }
            ),
            dim=["PROSTO ELEC DEDICATED I!"],
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
    ).values
    return value


@component.add(
    name="predictor 5 heat demand",
    units="TWh/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "fe_excluding_trade": 1,
        "legacy_elec_demand": 1,
        "legacy_elec_demand_energyplan": 1,
        "unit_conversion_twh_ej": 1,
    },
)
def predictor_5_heat_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR HEAT DEMAND"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: fe_excluding_trade().loc[:, "FE heat"].reset_coords(drop=True)
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / legacy_elec_demand(),
    )


@component.add(
    name="predictor 6 chp",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "protra_operative_capacity_stock_selected": 10,
    },
)
def predictor_6_chp():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return if_then_else(
        switch_nrg_variability() == 0,
        lambda: xr.DataArray(
            float(
                exogenous_predictors_energy_variability_regressions().loc[
                    "PREDICTOR CHP"
                ]
            ),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        ),
        lambda: (
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP gas fuels"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP gas fuels CCS"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP geothermal DEACTIVATED"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP liquid fuels"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP liquid fuels CCS"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP solid fossil"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP solid fossil CCS"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP waste"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP solid bio"]
            .reset_coords(drop=True)
            + protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", "PROTRA CHP solid bio CCS"]
            .reset_coords(drop=True)
        )
        * unit_conversion_mw_tw()
        * hourly_average_power_elec_demand_energyplan()
        / hourly_average_power_elec_demand(),
    )


@component.add(
    name="predictor 7 heat pumps",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "prosup_p2h_capacity_stock": 1,
        "switch_test_nrg_activate_p2h_regressions": 1,
    },
)
def predictor_7_heat_pumps():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return (
        if_then_else(
            switch_nrg_variability() == 0,
            lambda: xr.DataArray(
                float(
                    exogenous_predictors_energy_variability_regressions().loc[
                        "PREDICTOR HEAT PUMPS"
                    ]
                ),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H heat pump"]
            .reset_coords(drop=True)
            * unit_conversion_mw_tw()
            * hourly_average_power_elec_demand_energyplan()
            / hourly_average_power_elec_demand(),
        )
        * switch_test_nrg_activate_p2h_regressions()
    )


@component.add(
    name="predictor 8 electric boilers",
    units="MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "hourly_average_power_elec_demand": 1,
        "unit_conversion_mw_tw": 1,
        "hourly_average_power_elec_demand_energyplan": 1,
        "prosup_p2h_capacity_stock": 1,
        "switch_test_nrg_activate_p2h_regressions": 1,
    },
)
def predictor_8_electric_boilers():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    return (
        if_then_else(
            switch_nrg_variability() == 0,
            lambda: xr.DataArray(
                float(
                    exogenous_predictors_energy_variability_regressions().loc[
                        "PREDICTOR ELEC BOILERS"
                    ]
                ),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H electric boiler"]
            .reset_coords(drop=True)
            * unit_conversion_mw_tw()
            * hourly_average_power_elec_demand_energyplan()
            / hourly_average_power_elec_demand(),
        )
        * switch_test_nrg_activate_p2h_regressions()
    )


@component.add(
    name="predictor 9 electric vehicle demand",
    units="TWh",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability": 1,
        "exogenous_predictors_energy_variability_regressions": 1,
        "energy_passenger_transport_consumption_by_fe_35r": 9,
        "legacy_elec_demand_energyplan": 9,
        "unit_conversion_twh_ej": 9,
        "unit_conversion_mj_ej": 9,
        "legacy_elec_demand": 9,
    },
)
def predictor_9_electric_vehicle_demand():
    """
    Value of the cluster. The input is re-scaled according to the design of the experiment
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[["EU27"]] = if_then_else(
        switch_nrg_variability() == 0,
        lambda: float(
            exogenous_predictors_energy_variability_regressions().loc[
                "PREDICTOR EV DEMAND"
            ]
        ),
        lambda: sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "REGIONS 35 I": "REGIONS EU27 I!",
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["REGIONS EU27 I!", "PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["EU27"]),
    )
    value.loc[["UK"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["UK", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["UK"])
    )
    value.loc[["CHINA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["CHINA", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["CHINA"])
    )
    value.loc[["EASOC"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["EASOC", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["EASOC"])
    )
    value.loc[["INDIA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["INDIA", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["INDIA"])
    )
    value.loc[["LATAM"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["LATAM", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["LATAM"])
    )
    value.loc[["RUSSIA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["RUSSIA", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["RUSSIA"])
    )
    value.loc[["USMCA"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["USMCA", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["USMCA"])
    )
    value.loc[["LROW"]] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc["LROW", "FE elec", :, :]
            .reset_coords(drop=True)
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
        * unit_conversion_twh_ej()
        * legacy_elec_demand_energyplan()
        / float(legacy_elec_demand().loc["LROW"])
    )
    return value


@component.add(
    name="predictors all",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PREDICTORS NGR VARIABILITY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "predictor_6_chp": 15,
        "predictor_8_electric_boilers": 15,
        "predictor_9_electric_vehicle_demand": 15,
        "predictor_13_flexible_demand": 15,
        "predictor_7_heat_pumps": 15,
        "predictor_11_hydrogen_fe_demand": 15,
        "predictor_12_hydrogen_supply": 15,
        "predictor_10_v2g": 15,
        "predictor_5_heat_demand": 15,
        "predictor_1_protra_pp_solar": 15,
        "predictor_4_stationary_storage": 15,
        "predictor_2_protra_pp_wind": 15,
        "predictor_3_capacity_zero_ghg_semiflex": 15,
    },
)
def predictors_all():
    """
    Inputs of the regression analysis in the energy variability submodule
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PREDICTORS NGR VARIABILITY I": _subscript_dict[
                "PREDICTORS NGR VARIABILITY I"
            ],
        },
        ["REGIONS 9 I", "PREDICTORS NGR VARIABILITY I"],
    )
    value.loc[:, ["PREDICTOR CHP"]] = (
        predictor_6_chp()
        .expand_dims({"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR CHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoELEC BOILERS"]] = (
        (predictor_6_chp() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoEV DEMAND"]] = (
        (predictor_6_chp() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoFLEX DEMAND"]] = (
        (predictor_6_chp() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoHEAT PUMPS"]] = (
        (predictor_6_chp() * predictor_7_heat_pumps())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoHEAT PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoHYDROGEN DEMAND"]] = (
        (predictor_6_chp() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoHYDROGEN SUPPLY"]] = (
        (predictor_6_chp() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoV2G"]] = (
        (predictor_6_chp() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERS"]] = (
        predictor_8_electric_boilers()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR ELEC BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoEV DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoFLEX DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoHYDROGEN DEMAND"]] = (
        (predictor_8_electric_boilers() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoHYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoHYDROGEN SUPPLY"]] = (
        (predictor_8_electric_boilers() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoV2G"]] = (
        (predictor_8_electric_boilers() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMAND"]] = (
        predictor_9_electric_vehicle_demand()
        .expand_dims({"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR EV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMANDoFLEX DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR EV DEMANDoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMANDoHYDROGEN DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR EV DEMANDoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMANDoHYDROGEN SUPPLY"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR EV DEMANDoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMANDoV2G"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR EV DEMANDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR FLEX DEMAND"]] = (
        predictor_13_flexible_demand()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR FLEX DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMAND"]] = (
        predictor_5_heat_demand()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR HEAT DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoCHP"]] = (
        (predictor_5_heat_demand() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoELEC BOILERS"]] = (
        (predictor_5_heat_demand() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoEV DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoFLEX DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoHEAT PUMPS"]] = (
        (predictor_5_heat_demand() * predictor_7_heat_pumps())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoHEAT PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoHYDROGEN DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoHYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoHYDROGEN SUPPLY"]] = (
        (predictor_5_heat_demand() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoV2G"]] = (
        (predictor_5_heat_demand() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPS"]] = (
        predictor_7_heat_pumps()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR HEAT PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoELEC BOILERS"]] = (
        (predictor_7_heat_pumps() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoEV DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoFLEX DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoHYDROGEN DEMAND"]] = (
        (predictor_7_heat_pumps() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoHYDROGEN SUPPLY"]] = (
        (predictor_7_heat_pumps() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoV2G"]] = (
        (predictor_7_heat_pumps() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN DEMAND"]] = (
        predictor_11_hydrogen_fe_demand()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR HYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN DEMANDoFLEX DEMAND"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HYDROGEN DEMANDoFLEX DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN DEMANDoHYDROGEN SUPPLY"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HYDROGEN DEMANDoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN SUPPLY"]] = (
        predictor_12_hydrogen_supply()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR HYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN SUPPLYoFLEX DEMAND"]] = (
        (predictor_12_hydrogen_supply() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HYDROGEN SUPPLYoFLEX DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR SOLAR"]] = (
        predictor_1_protra_pp_solar()
        .expand_dims({"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR SOLAR"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoCHP"]] = (
        (predictor_1_protra_pp_solar() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoELEC BOILERS"]] = (
        (predictor_1_protra_pp_solar() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoEV DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoFLEX DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoHEAT DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_5_heat_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoHEAT DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoHEAT PUMPS"]] = (
        (predictor_1_protra_pp_solar() * predictor_7_heat_pumps())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoHEAT PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoHYDROGEN DEMAND"]] = (
        (predictor_1_protra_pp_solar() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoHYDROGEN SUPPLY"]] = (
        (predictor_1_protra_pp_solar() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoSTATIONARY STORAGE"]] = (
        (predictor_1_protra_pp_solar() * predictor_4_stationary_storage())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoSTATIONARY STORAGE"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoV2G"]] = (
        (predictor_1_protra_pp_solar() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoWIND"]] = (
        (predictor_1_protra_pp_solar() * predictor_2_protra_pp_wind())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoWIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoZERO GHG SEMIFLEX"]] = (
        (predictor_1_protra_pp_solar() * predictor_3_capacity_zero_ghg_semiflex())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoZERO GHG SEMIFLEX"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGE"]] = (
        predictor_4_stationary_storage()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR STATIONARY STORAGE"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoCHP"]] = (
        (predictor_4_stationary_storage() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoELEC BOILERS"]] = (
        (predictor_4_stationary_storage() * predictor_8_electric_boilers())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoELEC BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoEV DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_9_electric_vehicle_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoEV DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoFLEX DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoFLEX DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoHEAT DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_5_heat_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoHEAT DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoHEAT PUMPS"]] = (
        (predictor_4_stationary_storage() * predictor_7_heat_pumps())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoHEAT PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoHYDROGEN DEMAND"]] = (
        (predictor_4_stationary_storage() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoHYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoHYDROGEN SUPPLY"]] = (
        (predictor_4_stationary_storage() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoV2G"]] = (
        (predictor_4_stationary_storage() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR V2G"]] = (
        predictor_10_v2g()
        .expand_dims({"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR V2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR V2GoFLEX DEMAND"]] = (
        (predictor_10_v2g() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR V2GoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR V2GoHYDROGEN DEMAND"]] = (
        (predictor_10_v2g() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR V2GoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR V2GoHYDROGEN SUPPLY"]] = (
        (predictor_10_v2g() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR V2GoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WIND"]] = (
        predictor_2_protra_pp_wind()
        .expand_dims({"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR WIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoCHP"]] = (
        (predictor_2_protra_pp_wind() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoELEC BOILERS"]] = (
        (predictor_2_protra_pp_wind() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoEV DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoFLEX DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoFLEX DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoHEAT DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_5_heat_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoHEAT DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoHEAT PUMPS"]] = (
        (predictor_2_protra_pp_wind() * predictor_7_heat_pumps())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoHEAT PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoHYDROGEN DEMAND"]] = (
        (predictor_2_protra_pp_wind() * predictor_11_hydrogen_fe_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoHYDROGEN DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoHYDROGEN SUPPLY"]] = (
        (predictor_2_protra_pp_wind() * predictor_12_hydrogen_supply())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoHYDROGEN SUPPLY"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoSTATIONARY STORAGE"]] = (
        (predictor_2_protra_pp_wind() * predictor_4_stationary_storage())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoSTATIONARY STORAGE"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoV2G"]] = (
        (predictor_2_protra_pp_wind() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoZERO GHG SEMIFLEX"]] = (
        (predictor_2_protra_pp_wind() * predictor_3_capacity_zero_ghg_semiflex())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoZERO GHG SEMIFLEX"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEX"]] = (
        predictor_3_capacity_zero_ghg_semiflex()
        .expand_dims(
            {"BASIC PREDICTORS NGR VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEX"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoCHP"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoELEC BOILERS"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_8_electric_boilers())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoELEC BOILERS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoEV DEMAND"]] = (
        (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_9_electric_vehicle_demand()
        )
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoEV DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoFLEX DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_13_flexible_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoFLEX DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoHEAT DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_5_heat_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoHEAT DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoHEAT PUMPS"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_7_heat_pumps())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoHEAT PUMPS"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoHYDROGEN DEMAND"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoHYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoHYDROGEN SUPPLY"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoSTATIONARY STORAGE"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_4_stationary_storage())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoSTATIONARY STORAGE"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoV2G"]] = (
        (predictor_3_capacity_zero_ghg_semiflex() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR SOLARoSOLAR"]] = (
        (predictor_1_protra_pp_solar() * predictor_1_protra_pp_solar())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR SOLARoSOLAR"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR WINDoWIND"]] = (
        (predictor_2_protra_pp_wind() * predictor_2_protra_pp_wind())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR WINDoWIND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ZERO GHG SEMIFLEXoZERO GHG SEMIFLEX"]] = (
        (
            predictor_3_capacity_zero_ghg_semiflex()
            * predictor_3_capacity_zero_ghg_semiflex()
        )
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR ZERO GHG SEMIFLEXoZERO GHG SEMIFLEX"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR STATIONARY STORAGEoSTATIONARY STORAGE"]] = (
        (predictor_4_stationary_storage() * predictor_4_stationary_storage())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR STATIONARY STORAGEoSTATIONARY STORAGE"]},
            1,
        )
        .values
    )
    value.loc[:, ["PREDICTOR HEAT DEMANDoHEAT DEMAND"]] = (
        (predictor_5_heat_demand() * predictor_5_heat_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT DEMANDoHEAT DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR CHPoCHP"]] = (
        (predictor_6_chp() * predictor_6_chp())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR CHPoCHP"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HEAT PUMPSoHEAT PUMPS"]] = (
        (predictor_7_heat_pumps() * predictor_7_heat_pumps())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR HEAT PUMPSoHEAT PUMPS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR ELEC BOILERSoELEC BOILERS"]] = (
        (predictor_8_electric_boilers() * predictor_8_electric_boilers())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR ELEC BOILERSoELEC BOILERS"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR EV DEMANDoEV DEMAND"]] = (
        (predictor_9_electric_vehicle_demand() * predictor_9_electric_vehicle_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR EV DEMANDoEV DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR V2GoV2G"]] = (
        (predictor_10_v2g() * predictor_10_v2g())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR V2GoV2G"]}, 1)
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN DEMANDoHYDROGEN DEMAND"]] = (
        (predictor_11_hydrogen_fe_demand() * predictor_11_hydrogen_fe_demand())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HYDROGEN DEMANDoHYDROGEN DEMAND"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR HYDROGEN SUPPLYoHYDROGEN SUPPLY"]] = (
        (predictor_12_hydrogen_supply() * predictor_12_hydrogen_supply())
        .expand_dims(
            {"NRG VARIABILITY I": ["PREDICTOR HYDROGEN SUPPLYoHYDROGEN SUPPLY"]}, 1
        )
        .values
    )
    value.loc[:, ["PREDICTOR FLEX DEMANDoFLEX DEMAND"]] = (
        (predictor_13_flexible_demand() * predictor_13_flexible_demand())
        .expand_dims({"NRG VARIABILITY I": ["PREDICTOR FLEX DEMANDoFLEX DEMAND"]}, 1)
        .values
    )
    return value


@component.add(
    name="SELECT NRG VARIABILITY TYPE REGRESSION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_nrg_variability_type_regression"},
)
def select_nrg_variability_type_regression():
    """
    Selection of the type of regresssion to consider the variability of renewable energy sources 0: multiple linear regression models 1: multiple logistic regression models
    """
    return _ext_constant_select_nrg_variability_type_regression()


_ext_constant_select_nrg_variability_type_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "SELECT_regression_method",
    "SELECT_NRG_VARIABILITY_TYPE_REGRESSION",
    {},
    _root,
    {},
    "_ext_constant_select_nrg_variability_type_regression",
)


@component.add(
    name="SWITCH NRG VARIABILITY",
    units="DMNL/per year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_variability"},
)
def switch_nrg_variability():
    """
    This switch can take two values: 1: the energy variability equations are activated and the (sub)module runs integrated with the rest of WILIAM. 0: the (sub)module imports exogenous constants, i.e., WILIAM does not see the energy variability in the generation of energy (RES would appear as fully dispatachable).
    """
    return _ext_constant_switch_nrg_variability()


_ext_constant_switch_nrg_variability = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_VARIABILITY",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_variability",
)


@component.add(
    name="SWITCH TEST NRG ACTIVATE P2H REGRESSIONS",
    units="DMML",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_test_nrg_activate_p2h_regressions"
    },
)
def switch_test_nrg_activate_p2h_regressions():
    """
    0: P2H technologies are not considered in the energy variability submodule. 1: P2H technologies are considered in the energy variability submodule.
    """
    return _ext_constant_switch_test_nrg_activate_p2h_regressions()


_ext_constant_switch_test_nrg_activate_p2h_regressions = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_TEST_NRG_ACTIVATE_P2H_REGRESSIONS",
    {},
    _root,
    {},
    "_ext_constant_switch_test_nrg_activate_p2h_regressions",
)


@component.add(
    name="variation CF curtailed PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_nrg_variability_type_regression": 3,
        "outputs_linear_regression": 3,
        "outputs_logistic_regression": 3,
    },
)
def variation_cf_curtailed_protra():
    """
    Variation from the maximum capacity factor of PROTRA technologies. This indicator ranges 0-1 (0 means CF=0% and 1 means CF= maximum possible CF without curtailment).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar CSP"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT WIND CF DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT WIND CF DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"PROTRA WIND I": _subscript_dict["PROTRA WIND I"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar CSP"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT SOLAR CF DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT SOLAR CF DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = (
        if_then_else(
            select_nrg_variability_type_regression() == 0,
            lambda: outputs_linear_regression()
            .loc[:, "OUTPUT SOLAR CF DECLINE"]
            .reset_coords(drop=True),
            lambda: outputs_logistic_regression()
            .loc[:, "OUTPUT SOLAR CF DECLINE"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    return value
