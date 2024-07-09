"""
Module economygovernment
Translated using PySD version 3.14.0
"""

@component.add(
    name="ANNUAL GROWTH GOVERNMENT EXPENDITURE DEFAULT",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_annual_growth_government_expenditure_default"
    },
)
def annual_growth_government_expenditure_default():
    """
    Limit to annual growth in government expenditure
    """
    return _ext_constant_annual_growth_government_expenditure_default()


_ext_constant_annual_growth_government_expenditure_default = ExtConstant(
    "model_parameters/economy/Government.xlsx",
    "EXO_limit_growth_gov_exp_def",
    "ANNUAL_GROWTH_GOVERNMENT_EXPENDITURE_DEFAULT",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_annual_growth_government_expenditure_default",
)


@component.add(
    name="average disposable income per capita",
    units="dollars/(Year*person)",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "people_per_household_by_income_and_type": 2,
        "number_of_households_by_income_and_type_until_2015": 2,
        "households_disposable_income_until_2015": 1,
        "households_disposable_income": 1,
        "number_of_households_by_income_and_type": 2,
    },
)
def average_disposable_income_per_capita():
    """
    Average disposable income per household.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: zidz(
            sum(
                households_disposable_income_until_2015().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                )
                * number_of_households_by_income_and_type_until_2015().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            ),
            sum(
                number_of_households_by_income_and_type_until_2015().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                )
                * people_per_household_by_income_and_type().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            ),
        ),
        lambda: zidz(
            sum(
                households_disposable_income().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
                * number_of_households_by_income_and_type().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            ),
            sum(
                number_of_households_by_income_and_type().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                )
                * people_per_household_by_income_and_type().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            ),
        ),
    )


@component.add(
    name="average people per household nonEU regions until 2015",
    units="person/household",
    subscripts=["REGIONS 8 I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={
        "_sampleiftrue_average_people_per_household_noneu_regions_until_2015": 1
    },
    other_deps={
        "_sampleiftrue_average_people_per_household_noneu_regions_until_2015": {
            "initial": {"average_people_per_household_noneu_regions": 1},
            "step": {"time": 1, "average_people_per_household_noneu_regions": 1},
        }
    },
)
def average_people_per_household_noneu_regions_until_2015():
    """
    This variable is the value contained in it until 2015 and further on, where its value remains a constant of the 2015 level. Its used to isolate the economic module when the switch economy is deactivated.
    """
    return _sampleiftrue_average_people_per_household_noneu_regions_until_2015()


_sampleiftrue_average_people_per_household_noneu_regions_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015, {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, ["REGIONS 8 I"]
    ),
    lambda: average_people_per_household_noneu_regions(),
    lambda: average_people_per_household_noneu_regions(),
    "_sampleiftrue_average_people_per_household_noneu_regions_until_2015",
)


@component.add(
    name="base delayed GDP",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_gross_domestic_product": 1},
)
def base_delayed_gdp():
    """
    Delayed Gross Domestic Product (GDP). ZIDZ( BASE GDP[REGIONS 35 I] , 1+INITIAL_DELAYED_GDP_GROWTH[REGIONS 35 I])
    """
    return initial_gross_domestic_product() / (1 + 0.0005)


@component.add(
    name="basic income per capita",
    units="dollars/(Year*person)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "delayed_ts_basic_income_per_capita": 2,
        "initial_year_basic_income_sp": 4,
        "delayed_ts_average_disposable_income_per_capita": 2,
        "time": 4,
        "switch_policy_basic_income_sp": 4,
        "initial_delayed_2_consumer_price_index": 1,
        "ratio_basic_income_to_average_disposable_income_sp": 2,
        "initial_delayed_consumer_price_index": 1,
        "delayed_2_ts_consumer_price_index": 1,
        "delayed_ts_consumer_price_index": 1,
    },
)
def basic_income_per_capita():
    """
    Basic income per capita. In the initial year the basic income is defined as a share of the average disposable income per capita. This value is updated with the consumer price index, except when the submodule runs isolated, when it takes the initial consumer price index.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS NON DISAGGREGATED HH I"], :] = False
    except_subs.loc[
        _subscript_dict["REGIONS DISAGGREGATED HH I"], ["REPRESENTATIVE HOUSEHOLD"]
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS DISAGGREGATED HH I"],
        _subscript_dict["HOUSEHOLDS EU27 I"],
    ] = False
    value.values[except_subs.values] = 0
    value.loc[_subscript_dict["REGIONS NON DISAGGREGATED HH I"], :] = 0
    value.loc[
        _subscript_dict["REGIONS DISAGGREGATED HH I"], ["REPRESENTATIVE HOUSEHOLD"]
    ] = 0
    value.loc[
        _subscript_dict["REGIONS DISAGGREGATED HH I"],
        _subscript_dict["HOUSEHOLDS EU27 I"],
    ] = if_then_else(
        switch_eco_government() == 0,
        lambda: if_then_else(
            np.logical_and(
                switch_policy_basic_income_sp()
                .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                == 1,
                time() == initial_year_basic_income_sp(),
            ).expand_dims(
                {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
            ),
            lambda: (
                delayed_ts_average_disposable_income_per_capita()
                .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                * ratio_basic_income_to_average_disposable_income_sp()
            ).expand_dims(
                {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_policy_basic_income_sp()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                    == 1,
                    time() > initial_year_basic_income_sp(),
                ).expand_dims(
                    {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
                ),
                lambda: delayed_ts_basic_income_per_capita()
                .loc[
                    _subscript_dict["REGIONS DISAGGREGATED HH I"],
                    _subscript_dict["HOUSEHOLDS EU27 I"],
                ]
                .rename(
                    {
                        "REGIONS 35 I": "REGIONS DISAGGREGATED HH I",
                        "HOUSEHOLDS I": "HOUSEHOLDS EU27 I",
                    }
                )
                * zidz(
                    initial_delayed_consumer_price_index()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"}),
                    initial_delayed_2_consumer_price_index()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"}),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS DISAGGREGATED HH I": _subscript_dict[
                            "REGIONS DISAGGREGATED HH I"
                        ],
                        "HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"],
                    },
                    ["REGIONS DISAGGREGATED HH I", "HOUSEHOLDS EU27 I"],
                ),
            ),
        ),
        lambda: if_then_else(
            np.logical_and(
                switch_policy_basic_income_sp()
                .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                == 1,
                time() == initial_year_basic_income_sp(),
            ).expand_dims(
                {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
            ),
            lambda: (
                delayed_ts_average_disposable_income_per_capita()
                .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                * ratio_basic_income_to_average_disposable_income_sp()
            ).expand_dims(
                {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_policy_basic_income_sp()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"})
                    == 1,
                    time() > initial_year_basic_income_sp(),
                ).expand_dims(
                    {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]}, 1
                ),
                lambda: delayed_ts_basic_income_per_capita()
                .loc[
                    _subscript_dict["REGIONS DISAGGREGATED HH I"],
                    _subscript_dict["HOUSEHOLDS EU27 I"],
                ]
                .rename(
                    {
                        "REGIONS 35 I": "REGIONS DISAGGREGATED HH I",
                        "HOUSEHOLDS I": "HOUSEHOLDS EU27 I",
                    }
                )
                * zidz(
                    delayed_ts_consumer_price_index()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"}),
                    delayed_2_ts_consumer_price_index()
                    .loc[_subscript_dict["REGIONS DISAGGREGATED HH I"]]
                    .rename({"REGIONS 35 I": "REGIONS DISAGGREGATED HH I"}),
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS DISAGGREGATED HH I": _subscript_dict[
                            "REGIONS DISAGGREGATED HH I"
                        ],
                        "HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"],
                    },
                    ["REGIONS DISAGGREGATED HH I", "HOUSEHOLDS EU27 I"],
                ),
            ),
        ),
    ).values
    return value


@component.add(
    name="change in government debt",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_government_assets_net_adquisition": 1,
        "statistical_difference_government_debt": 1,
        "government_budget_balance": 2,
        "ghg_tax_revenues_to_reduce_government_debt": 1,
    },
)
def change_in_government_debt():
    """
    Change in the stock gross of debt.
    """
    return if_then_else(
        time() <= 2015,
        lambda: -government_budget_balance()
        + statistical_difference_government_debt()
        + initial_government_assets_net_adquisition(),
        lambda: -government_budget_balance()
        - ghg_tax_revenues_to_reduce_government_debt(),
    )


@component.add(
    name="debt interest",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_government_debt": 1, "debt_interest_rate": 1},
)
def debt_interest():
    """
    Interests paid by the government to the owners of public debt.
    """
    return delayed_ts_government_debt() * debt_interest_rate()


@component.add(
    name="debt interest rate",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_debt_interest_rate_target": 1,
        "initial_year_debt_interest_rate_sp": 1,
        "select_debt_interest_rate_sp": 1,
        "debt_interest_rate_default": 1,
        "time": 1,
        "debt_interest_rate_sp": 1,
    },
)
def debt_interest_rate():
    """
    Debt interest rate.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_debt_interest_rate_target(),
        lambda: if_then_else(
            np.logical_and(
                select_debt_interest_rate_sp() == 1,
                initial_year_debt_interest_rate_sp() <= time(),
            ),
            lambda: debt_interest_rate_sp(),
            lambda: debt_interest_rate_default(),
        ),
    )


@component.add(
    name="DEBT INTEREST RATE SP",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_debt_interest_rate_sp",
        "__data__": "_ext_data_debt_interest_rate_sp",
        "time": 1,
    },
)
def debt_interest_rate_sp():
    """
    Debt interest rate.
    """
    return _ext_data_debt_interest_rate_sp(time())


_ext_data_debt_interest_rate_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "TIME_DEBT_INTEREST",
    "DEBT_INTEREST_RATE_SP",
    "interpolate",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_debt_interest_rate_sp",
)


@component.add(
    name="delayed 2 TS consumer price index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_2_ts_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_2_ts_consumer_price_index": {
            "initial": {"initial_delayed_consumer_price_index": 1, "time_step": 1},
            "step": {"delayed_ts_consumer_price_index": 1},
        }
    },
)
def delayed_2_ts_consumer_price_index():
    """
    Delayed (2 time step) consumer price index.
    """
    return _delayfixed_delayed_2_ts_consumer_price_index()


_delayfixed_delayed_2_ts_consumer_price_index = DelayFixed(
    lambda: delayed_ts_consumer_price_index(),
    lambda: time_step(),
    lambda: initial_delayed_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_2_ts_consumer_price_index",
)


@component.add(
    name="delayed gdp growth",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdp_growth": 1},
    other_deps={
        "_delayfixed_delayed_gdp_growth": {
            "initial": {"initial_initial_delayed_gdp_growth": 1},
            "step": {
                "time": 1,
                "initial_initial_delayed_gdp_growth": 1,
                "gross_domestic_product_nominal_growth": 1,
            },
        }
    },
)
def delayed_gdp_growth():
    """
    Delayed GDP growth
    """
    return _delayfixed_delayed_gdp_growth()


_delayfixed_delayed_gdp_growth = DelayFixed(
    lambda: if_then_else(
        time() <= 2016,
        lambda: initial_initial_delayed_gdp_growth(),
        lambda: gross_domestic_product_nominal_growth(),
    ),
    lambda: 1,
    lambda: initial_initial_delayed_gdp_growth(),
    time_step,
    "_delayfixed_delayed_gdp_growth",
)


@component.add(
    name="delayed government revenue to GDP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_government_revenue_to_gdp": 1},
    other_deps={
        "_delayfixed_delayed_government_revenue_to_gdp": {
            "initial": {"initial_delayed_government_revenue_to_gdp": 1},
            "step": {
                "time": 1,
                "initial_delayed_government_revenue_to_gdp": 1,
                "government_revenue_to_gdp": 1,
            },
        }
    },
)
def delayed_government_revenue_to_gdp():
    """
    Delayed government revenue to GDP.
    """
    return _delayfixed_delayed_government_revenue_to_gdp()


_delayfixed_delayed_government_revenue_to_gdp = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_government_revenue_to_gdp(),
        lambda: government_revenue_to_gdp(),
    ),
    lambda: 1,
    lambda: initial_delayed_government_revenue_to_gdp(),
    time_step,
    "_delayfixed_delayed_government_revenue_to_gdp",
)


@component.add(
    name="delayed gross domestic product nominal",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gross_domestic_product_nominal": 1},
    other_deps={
        "_delayfixed_delayed_gross_domestic_product_nominal": {
            "initial": {"initial_delayed_gdp": 1},
            "step": {
                "time": 1,
                "initial_delayed_gdp": 1,
                "gross_domestic_product_nominal": 1,
            },
        }
    },
)
def delayed_gross_domestic_product_nominal():
    """
    Delayed GDP nominal
    """
    return _delayfixed_delayed_gross_domestic_product_nominal()


_delayfixed_delayed_gross_domestic_product_nominal = DelayFixed(
    lambda: if_then_else(
        time() <= 2014,
        lambda: initial_delayed_gdp(),
        lambda: gross_domestic_product_nominal(),
    ),
    lambda: 1,
    lambda: initial_delayed_gdp(),
    time_step,
    "_delayfixed_delayed_gross_domestic_product_nominal",
)


@component.add(
    name="delayed TS average disposable income per capita",
    units="dollars/(Year*person)",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_average_disposable_income_per_capita": 1},
    other_deps={
        "_delayfixed_delayed_ts_average_disposable_income_per_capita": {
            "initial": {"time_step": 1},
            "step": {"average_disposable_income_per_capita": 1},
        }
    },
)
def delayed_ts_average_disposable_income_per_capita():
    """
    Delayed average disposable income
    """
    return _delayfixed_delayed_ts_average_disposable_income_per_capita()


_delayfixed_delayed_ts_average_disposable_income_per_capita = DelayFixed(
    lambda: average_disposable_income_per_capita(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_average_disposable_income_per_capita",
)


@component.add(
    name="delayed TS basic income per capita",
    units="dollars/(Year*person)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_basic_income_per_capita": 1},
    other_deps={
        "_delayfixed_delayed_ts_basic_income_per_capita": {
            "initial": {"time_step": 1},
            "step": {"basic_income_per_capita": 1},
        }
    },
)
def delayed_ts_basic_income_per_capita():
    """
    Delayed basic income per capita
    """
    return _delayfixed_delayed_ts_basic_income_per_capita()


_delayfixed_delayed_ts_basic_income_per_capita = DelayFixed(
    lambda: basic_income_per_capita(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_basic_income_per_capita",
)


@component.add(
    name="delayed TS government debt",
    units="Mdollars",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_government_debt": 1},
    other_deps={
        "_delayfixed_delayed_ts_government_debt": {
            "initial": {"initial_delayed_government_debt": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_government_debt": 1,
                "government_debt": 1,
            },
        }
    },
)
def delayed_ts_government_debt():
    """
    Delayed government debt.
    """
    return _delayfixed_delayed_ts_government_debt()


_delayfixed_delayed_ts_government_debt = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_government_debt(),
        lambda: government_debt(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_government_debt(),
    time_step,
    "_delayfixed_delayed_ts_government_debt",
)


@component.add(
    name="delayed TS government expenditure rest",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_government_expenditure_rest": 1},
    other_deps={
        "_delayfixed_delayed_ts_government_expenditure_rest": {
            "initial": {"time_step": 1},
            "step": {"government_expenditure_rest": 1},
        }
    },
)
def delayed_ts_government_expenditure_rest():
    """
    Government expenditure objective excluding debt interests, investments to replace climate damages and basic income.
    """
    return _delayfixed_delayed_ts_government_expenditure_rest()


_delayfixed_delayed_ts_government_expenditure_rest = DelayFixed(
    lambda: government_expenditure_rest(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_government_expenditure_rest",
)


@component.add(
    name="delayed TS gross value added",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_value_added": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_value_added": {
            "initial": {"initial_gross_value_added": 1, "time_step": 1},
            "step": {"time": 1, "initial_gross_value_added": 1, "gross_value_added": 1},
        }
    },
)
def delayed_ts_gross_value_added():
    """
    Delayed gross value added in current prices.
    """
    return _delayfixed_delayed_ts_gross_value_added()


_delayfixed_delayed_ts_gross_value_added = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_gross_value_added(),
        lambda: gross_value_added().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        ),
    ),
    lambda: time_step(),
    lambda: initial_gross_value_added(),
    time_step,
    "_delayfixed_delayed_ts_gross_value_added",
)


@component.add(
    name="delayed TS non adjusted government expenditure objective rest",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_non_adjusted_government_expenditure_objective_rest": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_non_adjusted_government_expenditure_objective_rest": {
            "initial": {"time_step": 1},
            "step": {"non_adjusted_government_expenditure_objective_rest": 1},
        }
    },
)
def delayed_ts_non_adjusted_government_expenditure_objective_rest():
    """
    Delayed non adjusted Government expenditure desired taking into account some specific expenditures.
    """
    return _delayfixed_delayed_ts_non_adjusted_government_expenditure_objective_rest()


_delayfixed_delayed_ts_non_adjusted_government_expenditure_objective_rest = DelayFixed(
    lambda: non_adjusted_government_expenditure_objective_rest(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_non_adjusted_government_expenditure_objective_rest",
)


@component.add(
    name="delayed TS taxes on resources",
    units="Mdollars/Year",
    subscripts=["MATERIALS W I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_on_resources": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_on_resources": {
            "initial": {"taxes_on_resources": 1, "time_step": 1},
            "step": {"taxes_on_resources": 1},
        }
    },
)
def delayed_ts_taxes_on_resources():
    """
    Delayed taxes on resources Tax Revenue from metals/ resources Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    return _delayfixed_delayed_ts_taxes_on_resources()


_delayfixed_delayed_ts_taxes_on_resources = DelayFixed(
    lambda: taxes_on_resources(),
    lambda: time_step(),
    lambda: taxes_on_resources(),
    time_step,
    "_delayfixed_delayed_ts_taxes_on_resources",
)


@component.add(
    name="delayed TS taxes on resources until 2015",
    units="Mdollars/Year",
    subscripts=["MATERIALS W I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_delayed_ts_taxes_on_resources_until_2015": 1},
    other_deps={
        "_sampleiftrue_delayed_ts_taxes_on_resources_until_2015": {
            "initial": {"delayed_ts_taxes_on_resources": 1},
            "step": {"time": 1, "delayed_ts_taxes_on_resources": 1},
        }
    },
)
def delayed_ts_taxes_on_resources_until_2015():
    """
    This variable is used to isolate the government module. When it reaches 2015 it stays at a constant value, that of the 2015 level of delayed TS taxes on resources.
    """
    return _sampleiftrue_delayed_ts_taxes_on_resources_until_2015()


_sampleiftrue_delayed_ts_taxes_on_resources_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {"MATERIALS W I": _subscript_dict["MATERIALS W I"]},
        ["MATERIALS W I"],
    ),
    lambda: delayed_ts_taxes_on_resources(),
    lambda: delayed_ts_taxes_on_resources(),
    "_sampleiftrue_delayed_ts_taxes_on_resources_until_2015",
)


@component.add(
    name="delayed TS taxes production",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_production": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_production": {
            "initial": {"initial_taxes_production": 1, "time_step": 1},
            "step": {"time": 1, "initial_taxes_production": 1, "taxes_production": 1},
        }
    },
)
def delayed_ts_taxes_production():
    """
    Delayed taxes on production.
    """
    return _delayfixed_delayed_ts_taxes_production()


_delayfixed_delayed_ts_taxes_production = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: initial_taxes_production(), lambda: taxes_production()
    ),
    lambda: time_step(),
    lambda: initial_taxes_production(),
    time_step,
    "_delayfixed_delayed_ts_taxes_production",
)


@component.add(
    name="delayed TS taxes products by sector",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_products_by_sector": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_products_by_sector": {
            "initial": {"initial_taxes_products_by_sector": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_taxes_products_by_sector": 1,
                "taxes_products_by_sector": 1,
            },
        }
    },
)
def delayed_ts_taxes_products_by_sector():
    """
    Delayed taxes on products by sector.
    """
    return _delayfixed_delayed_ts_taxes_products_by_sector()


_delayfixed_delayed_ts_taxes_products_by_sector = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_taxes_products_by_sector(),
        lambda: taxes_products_by_sector().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        ),
    ),
    lambda: time_step(),
    lambda: initial_taxes_products_by_sector(),
    time_step,
    "_delayfixed_delayed_ts_taxes_products_by_sector",
)


@component.add(
    name="delayed TS taxes products final demand",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_taxes_products_final_demand": 1},
    other_deps={
        "_delayfixed_delayed_ts_taxes_products_final_demand": {
            "initial": {"initial_taxes_products_final_demand": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_taxes_products_final_demand": 1,
                "taxes_products_final_demand": 1,
            },
        }
    },
)
def delayed_ts_taxes_products_final_demand():
    """
    Delayed taxes products final demand.
    """
    return _delayfixed_delayed_ts_taxes_products_final_demand()


_delayfixed_delayed_ts_taxes_products_final_demand = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_taxes_products_final_demand(),
        lambda: taxes_products_final_demand().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I"}
        ),
    ),
    lambda: time_step(),
    lambda: initial_taxes_products_final_demand(),
    time_step,
    "_delayfixed_delayed_ts_taxes_products_final_demand",
)


@component.add(
    name="GDP objective government budget",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_initial_delayed_gdp_growth": 1,
        "base_delayed_gdp": 1,
        "delayed_gross_domestic_product_nominal": 1,
        "delayed_gdp_growth": 1,
    },
)
def gdp_objective_government_budget():
    """
    Expected GDP by the government.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: base_delayed_gdp() * (1 + initial_initial_delayed_gdp_growth()),
        lambda: delayed_gross_domestic_product_nominal() * (1 + delayed_gdp_growth()),
    )


@component.add(
    name="GHG tax revenues to reduce government debt",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"revenues_ghg_taxes": 1, "share_ghg_revenues_to_reduce_debt_sp": 1},
)
def ghg_tax_revenues_to_reduce_government_debt():
    """
    GHG tax revenues used to reduce government debt
    """
    return revenues_ghg_taxes() * share_ghg_revenues_to_reduce_debt_sp()


@component.add(
    name="GHG tax revenues used to finance basic income",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "revenues_ghg_taxes": 1,
        "share_ghg_revenues_to_finance_basic_income_sp": 1,
    },
)
def ghg_tax_revenues_used_to_finance_basic_income():
    """
    GHG tax revenues used to fiance a universal basic income
    """
    return revenues_ghg_taxes() * share_ghg_revenues_to_finance_basic_income_sp()


@component.add(
    name="GHG tax revenues used to increase social benefits",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "revenues_ghg_taxes": 1,
        "share_ghg_revenues_to_increase_social_benefits_sp": 1,
    },
)
def ghg_tax_revenues_used_to_increase_social_benefits():
    """
    GHG tax revenues used to increase social benefits
    """
    return revenues_ghg_taxes() * share_ghg_revenues_to_increase_social_benefits_sp()


@component.add(
    name="GHG tax revenues used to reduce income tax",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"revenues_ghg_taxes": 1, "share_ghg_revenues_to_income_tax_sp": 1},
)
def ghg_tax_revenues_used_to_reduce_income_tax():
    """
    GHG tax revenues used to reduce income taxes
    """
    return revenues_ghg_taxes() * share_ghg_revenues_to_income_tax_sp()


@component.add(
    name="government basic income expenditure",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "household_basic_income": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def government_basic_income_expenditure():
    """
    Government basic income expenditure.
    """
    return (
        sum(
            household_basic_income().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        )
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="government budget balance",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_revenue": 1, "government_expenditure": 1},
)
def government_budget_balance():
    """
    Government deficit or surplus (difference between revenue and expenditure).
    """
    return government_revenue() - government_expenditure()


@component.add(
    name="government budget balance objective",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_budget_balance_to_gdp_objective": 1,
        "gdp_objective_government_budget": 1,
    },
)
def government_budget_balance_objective():
    """
    Government deficit or surplus objective.
    """
    return (
        government_budget_balance_to_gdp_objective() * gdp_objective_government_budget()
    )


@component.add(
    name="government budget balance to GDP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_budget_balance": 1, "gross_domestic_product_nominal": 1},
)
def government_budget_balance_to_gdp():
    """
    Government budget balance to GDP
    """
    return zidz(government_budget_balance(), gross_domestic_product_nominal())


@component.add(
    name="government budget balance to GDP objective",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "initial_government_budget_balance_to_gdp_objective": 1,
        "government_budget_balance_to_gdp_objective_sp": 2,
        "model_explorer_government_to_gdp_objetive": 1,
        "initial_year_government_budget_balance_to_gdp_objective_sp": 1,
        "switch_model_explorer": 1,
        "government_budget_balance_to_gdp_objective_default_sp": 1,
        "select_government_budget_balance_to_gdp_objective_sp": 1,
    },
)
def government_budget_balance_to_gdp_objective():
    """
    Government deficit or surplus to GDP objective. Deficit or surplus of the government measured as a % of the GDP. When the variable is positive, it means that the government has a surplus, and the expenditure is less than the revenue in that year, so the accumulated debt decreases. On the other hand, when the variable is negative, there is a deficit, and the government public expenditure is higher than the revenue, so the debt increases. IF_THEN_ELSE(Time<=2015,GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_DEFAULT [REGIONS_35_I], IF_THEN_ELSE(SWITCH_MODEL_EXPLORER=1, model_explorer_government_to_GDP_objetive[REGIONS_35_I] +GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_SP [REGIONS_35_I], GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_TARGET_SP[REGIONS_35_I]))
    """
    return if_then_else(
        time() <= 2015,
        lambda: initial_government_budget_balance_to_gdp_objective(),
        lambda: if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_government_to_gdp_objetive()
            + government_budget_balance_to_gdp_objective_sp(),
            lambda: if_then_else(
                np.logical_and(
                    select_government_budget_balance_to_gdp_objective_sp() == 1,
                    initial_year_government_budget_balance_to_gdp_objective_sp()
                    <= time(),
                ),
                lambda: government_budget_balance_to_gdp_objective_sp(),
                lambda: government_budget_balance_to_gdp_objective_default_sp(),
            ),
        ),
    )


@component.add(
    name="GOVERNMENT BUDGET BALANCE TO GDP OBJECTIVE DEFAULT SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_government_budget_balance_to_gdp_objective_default_sp",
        "__data__": "_ext_data_government_budget_balance_to_gdp_objective_default_sp",
        "time": 1,
    },
)
def government_budget_balance_to_gdp_objective_default_sp():
    """
    Goverment deficit or surplus to GDP objetive target. Deficit or surplus of the government measured as a % of the GDP. When the variable is positive, it means that the government has a surplus, and the expenditure is less than the revenue in that year, so the accumulated debt decreases. On the other hand, when the variable is negative, there is a deficit, and the government public expenditure is higher than the revenue, so the debt increases.Deficit or surplus of the government measured as a % of the GDP. When the variable is positive, it means that the government has a surplus, and the expenditure is less than the revenue in that year, so the accumulated debt decreases. On the other hand, when the variable is negative, there is a deficit, and the government public expenditure is higher than the revenue, so the debt increases.
    """
    return _ext_data_government_budget_balance_to_gdp_objective_default_sp(time())


_ext_data_government_budget_balance_to_gdp_objective_default_sp = ExtData(
    "model_parameters/economy/Government.xlsx",
    "EXO_Gov_DefSrup_to_GDP_obj_def",
    "TIME_GOV_BALANCE",
    "GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_DEFAULT_SP",
    "interpolate",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_government_budget_balance_to_gdp_objective_default_sp",
)


@component.add(
    name="GOVERNMENT BUDGET BALANCE TO GDP OBJECTIVE SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_government_budget_balance_to_gdp_objective_sp",
        "__data__": "_ext_data_government_budget_balance_to_gdp_objective_sp",
        "time": 1,
    },
)
def government_budget_balance_to_gdp_objective_sp():
    """
    Goverment deficit or surplus to GDP objetive target. Deficit or surplus of the government measured as a % of the GDP. When the variable is positive, it means that the government has a surplus, and the expenditure is less than the revenue in that year, so the accumulated debt decreases. On the other hand, when the variable is negative, there is a deficit, and the government public expenditure is higher than the revenue, so the debt increases.Deficit or surplus of the government measured as a % of the GDP. When the variable is positive, it means that the government has a surplus, and the expenditure is less than the revenue in that year, so the accumulated debt decreases. On the other hand, when the variable is negative, there is a deficit, and the government public expenditure is higher than the revenue, so the debt increases.
    """
    return _ext_data_government_budget_balance_to_gdp_objective_sp(time())


_ext_data_government_budget_balance_to_gdp_objective_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "TIME_GOV_BALANCE",
    "GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_SP",
    "interpolate",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_government_budget_balance_to_gdp_objective_sp",
)


@component.add(
    name="government consumption",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_rest": 1,
        "structure_government_expenditure": 1,
    },
)
def government_consumption():
    """
    Total government consumption of goods and services.
    """
    return government_expenditure_rest() * structure_government_expenditure().loc[
        :, "GOV CONSUMPTION"
    ].reset_coords(drop=True)


@component.add(
    name="government consumption by COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption": 1,
        "structure_government_consumption": 1,
        "statistical_difference_government_consumption": 1,
    },
)
def government_consumption_by_cofog():
    """
    Government consumption by category (COFOG classification: Classification of the Functions of the Government).
    """
    return (
        government_consumption()
        * structure_government_consumption()
        * statistical_difference_government_consumption()
    )


@component.add(
    name="government consumption purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "bridge_government_consumption_products": 1,
        "government_consumption_by_cofog": 1,
    },
)
def government_consumption_purchaser_prices():
    """
    Government consumption in purchaser prices and nominal terms.
    """
    return sum(
        bridge_government_consumption_products().rename({"COFOG I": "COFOG I!"})
        * government_consumption_by_cofog().rename({"COFOG I": "COFOG I!"}),
        dim=["COFOG I!"],
    )


@component.add(
    name="government debt",
    units="Mdollars",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_government_debt": 1},
    other_deps={
        "_integ_government_debt": {
            "initial": {"initial_government_debt": 1},
            "step": {"time": 1, "change_in_government_debt": 1},
        }
    },
)
def government_debt():
    """
    Total government debt (accumulated deficit or surplus).
    """
    return _integ_government_debt()


_integ_government_debt = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: change_in_government_debt(),
    ),
    lambda: initial_government_debt(),
    "_integ_government_debt",
)


@component.add(
    name="government debt to GDP ratio",
    units="Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_debt": 1, "gross_domestic_product_nominal": 1},
)
def government_debt_to_gdp_ratio():
    """
    Ratio government debt to GDP.
    """
    return zidz(government_debt(), gross_domestic_product_nominal())


@component.add(
    name="government expenditure",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption": 1,
        "debt_interest": 1,
        "government_investment": 1,
        "government_other_expenditures": 1,
        "government_transferences": 1,
        "social_benefits": 1,
        "government_basic_income_expenditure": 1,
        "ghg_tax_revenues_to_reduce_government_debt": 1,
    },
)
def government_expenditure():
    """
    Total government expenditure.
    """
    return (
        government_consumption()
        + debt_interest()
        + government_investment()
        + government_other_expenditures()
        + government_transferences()
        + social_benefits()
        + government_basic_income_expenditure()
        + ghg_tax_revenues_to_reduce_government_debt()
    )


@component.add(
    name="government expenditure objective",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_revenue_objective": 1,
        "government_budget_balance_objective": 1,
    },
)
def government_expenditure_objective():
    """
    Government expenditure objective.
    """
    return government_revenue_objective() - government_budget_balance_objective()


@component.add(
    name="government expenditure rest",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "non_adjusted_government_expenditure_objective_rest": 1,
        "delayed_ts_government_expenditure_rest": 2,
        "maximun_growth_government_expenditure_rest": 2,
        "growth_government_expenditure_objective_rest": 2,
        "limit_annual_growth_government_expenditure_sp": 1,
    },
)
def government_expenditure_rest():
    """
    Government expenditure excluding debt interests, investments to replace climate damages and basic income.
    """
    return if_then_else(
        time() <= 2015,
        lambda: non_adjusted_government_expenditure_objective_rest(),
        lambda: if_then_else(
            np.logical_and(
                limit_annual_growth_government_expenditure_sp() == 1,
                growth_government_expenditure_objective_rest()
                > maximun_growth_government_expenditure_rest(),
            ),
            lambda: delayed_ts_government_expenditure_rest()
            * (1 + maximun_growth_government_expenditure_rest()),
            lambda: delayed_ts_government_expenditure_rest()
            * (1 + growth_government_expenditure_objective_rest()),
        ),
    )


@component.add(
    name="government investment",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "government_expenditure_rest": 2,
        "structure_government_expenditure": 2,
        "public_gfcf_to_replace_climate_change_until_2015": 1,
        "public_gfcf_to_replace_climate_damage": 1,
    },
)
def government_investment():
    """
    Government purchase of investment goods. When the submodule runs isolated it takes the value of 2015 for the variable of public GFCF to replace climate change damage.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: government_expenditure_rest()
        * structure_government_expenditure()
        .loc[:, "GOV INVESTMENT"]
        .reset_coords(drop=True)
        + public_gfcf_to_replace_climate_change_until_2015(),
        lambda: government_expenditure_rest()
        * structure_government_expenditure()
        .loc[:, "GOV INVESTMENT"]
        .reset_coords(drop=True)
        + public_gfcf_to_replace_climate_damage(),
    )


@component.add(
    name="government investment by COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_investment": 1, "structure_government_investment": 1},
)
def government_investment_by_cofog():
    """
    Government investment by category (COFOG classification: Classification of the Functions of the Government).
    """
    return government_investment() * structure_government_investment()


@component.add(
    name="government other expenditures",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_rest": 1,
        "structure_government_expenditure": 1,
    },
)
def government_other_expenditures():
    """
    Other government expendutires
    """
    return government_expenditure_rest() * structure_government_expenditure().loc[
        :, "GOV OTHER EXPENDITURES"
    ].reset_coords(drop=True)


@component.add(
    name="government other revenue",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_gross_value_added": 1,
        "rate_government_other_revenue_to_value_added_default": 2,
        "delayed_ts_gross_value_added": 1,
    },
)
def government_other_revenue():
    """
    Other government revenue.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: rate_government_other_revenue_to_value_added_default()
        * sum(
            initial_gross_value_added().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
        lambda: rate_government_other_revenue_to_value_added_default()
        * sum(
            delayed_ts_gross_value_added().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="government property income",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_gross_value_added": 1,
        "rate_government_property_income_to_value_added_default": 2,
        "delayed_ts_gross_value_added": 1,
    },
)
def government_property_income():
    """
    Government revenue received from property income.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            initial_gross_value_added().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        * rate_government_property_income_to_value_added_default(),
        lambda: sum(
            delayed_ts_gross_value_added().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        * rate_government_property_income_to_value_added_default(),
    )


@component.add(
    name="government revenue",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_other_revenue": 1,
        "government_property_income": 1,
        "social_security": 1,
        "taxes_on_income_and_wealth": 1,
        "taxes_on_production": 1,
        "taxes_products": 1,
        "taxes_on_resources_paid_by_extraction_sectors": 1,
        "revenues_ghg_taxes": 1,
    },
)
def government_revenue():
    """
    Total government revenue.
    """
    return (
        government_other_revenue()
        + government_property_income()
        + social_security()
        + taxes_on_income_and_wealth()
        + taxes_on_production()
        + taxes_products()
        + sum(
            taxes_on_resources_paid_by_extraction_sectors().rename(
                {"SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + revenues_ghg_taxes()
    )


@component.add(
    name="government revenue objective",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_government_revenue_to_gdp": 1,
        "gdp_objective_government_budget": 1,
    },
)
def government_revenue_objective():
    """
    Government revenue objective.
    """
    return delayed_government_revenue_to_gdp() * gdp_objective_government_budget()


@component.add(
    name="government revenue to GDP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_revenue": 1,
        "government_basic_income_expenditure": 1,
        "ghg_tax_revenues_to_reduce_government_debt": 1,
        "ghg_tax_revenues_used_to_increase_social_benefits": 1,
        "switch_eco_government": 1,
        "initial_gross_domestic_product": 1,
        "gross_domestic_product_nominal": 1,
    },
)
def government_revenue_to_gdp():
    """
    Ratio government revenue to GDP.
    """
    return zidz(
        government_revenue()
        - government_basic_income_expenditure()
        - ghg_tax_revenues_to_reduce_government_debt()
        - ghg_tax_revenues_used_to_increase_social_benefits(),
        if_then_else(
            switch_eco_government() == 0,
            lambda: initial_gross_domestic_product(),
            lambda: gross_domestic_product_nominal(),
        ),
    )


@component.add(
    name="government transferences",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_rest": 1,
        "structure_government_expenditure": 1,
    },
)
def government_transferences():
    """
    Government expenditures for tranferences (such as income distribution, etc.)
    """
    return government_expenditure_rest() * structure_government_expenditure().loc[
        :, "GOV TRANSFERENCES"
    ].reset_coords(drop=True)


@component.add(
    name="gross domestic product nominal growth",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "delayed_gross_domestic_product_nominal": 2,
    },
)
def gross_domestic_product_nominal_growth():
    """
    GDP growth in nominal terms.
    """
    return (
        gross_domestic_product_nominal() - delayed_gross_domestic_product_nominal()
    ) / delayed_gross_domestic_product_nominal()


@component.add(
    name="growth government expenditure objective rest",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "non_adjusted_government_expenditure_objective_rest": 1,
        "delayed_ts_non_adjusted_government_expenditure_objective_rest": 1,
    },
)
def growth_government_expenditure_objective_rest():
    """
    Growth non adjusted Government expenditure objective excluding debt interests, investments to replace climate damages and basic income.
    """
    return (
        zidz(
            non_adjusted_government_expenditure_objective_rest(),
            delayed_ts_non_adjusted_government_expenditure_objective_rest(),
        )
        - 1
    )


@component.add(
    name="household basic income",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "basic_income_per_capita": 1,
        "people_per_household_by_income_and_type": 1,
    },
)
def household_basic_income():
    """
    Basic income per household
    """
    return basic_income_per_capita() * people_per_household_by_income_and_type()


@component.add(
    name="households disposable income until 2015",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_households_disposable_income_until_2015": 1},
    other_deps={
        "_sampleiftrue_households_disposable_income_until_2015": {
            "initial": {"households_disposable_income": 1},
            "step": {"time": 1, "households_disposable_income": 1},
        }
    },
)
def households_disposable_income_until_2015():
    """
    This variable is created to isolate the Government submodule when the eco-government switch is zero and the submodule runs isolated. It takes the historic data of the variable contained in it until 2015, when it stays becomes a constant at the level of that year.
    """
    return _sampleiftrue_households_disposable_income_until_2015()


_sampleiftrue_households_disposable_income_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    ),
    lambda: households_disposable_income(),
    lambda: households_disposable_income(),
    "_sampleiftrue_households_disposable_income_until_2015",
)


@component.add(
    name="implicit tax income corportations to finance basic income",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tax_income_corportations_to_finance_basic_income": 1,
        "delayed_ts_net_operating_surplus_total": 1,
    },
)
def implicit_tax_income_corportations_to_finance_basic_income():
    """
    Implicit tax on profits of corporations to finance basic income.
    """
    return zidz(
        tax_income_corportations_to_finance_basic_income(),
        delayed_ts_net_operating_surplus_total(),
    )


@component.add(
    name="INITIAL YEAR BASIC INCOME SP",
    units="Year",
    subscripts=["REGIONS DISAGGREGATED HH I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_basic_income_sp"},
)
def initial_year_basic_income_sp():
    """
    Initial year basic income
    """
    return _ext_constant_initial_year_basic_income_sp()


_ext_constant_initial_year_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_BASIC_INCOME_SP*",
    {"REGIONS DISAGGREGATED HH I": _subscript_dict["REGIONS DISAGGREGATED HH I"]},
    _root,
    {"REGIONS DISAGGREGATED HH I": _subscript_dict["REGIONS DISAGGREGATED HH I"]},
    "_ext_constant_initial_year_basic_income_sp",
)


@component.add(
    name="INITIAL YEAR DEBT INTEREST RATE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_debt_interest_rate_sp"},
)
def initial_year_debt_interest_rate_sp():
    """
    Initial year debt interest rate.
    """
    return _ext_constant_initial_year_debt_interest_rate_sp()


_ext_constant_initial_year_debt_interest_rate_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_DEBT_INTEREST_RATE_SP*",
    {},
    _root,
    {},
    "_ext_constant_initial_year_debt_interest_rate_sp",
)


@component.add(
    name="INITIAL YEAR GOVERNMENT BUDGET BALANCE TO GDP OBJECTIVE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_government_budget_balance_to_gdp_objective_sp"
    },
)
def initial_year_government_budget_balance_to_gdp_objective_sp():
    """
    Initial year goverment deficit or surplus to GDP objetive scenario
    """
    return _ext_constant_initial_year_government_budget_balance_to_gdp_objective_sp()


_ext_constant_initial_year_government_budget_balance_to_gdp_objective_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_SP*",
    {},
    _root,
    {},
    "_ext_constant_initial_year_government_budget_balance_to_gdp_objective_sp",
)


@component.add(
    name="INITIAL YEAR MAXIMUN GROWTH GOVERNMENT EXPENDITURE",
    units="Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_maximun_growth_government_expenditure"
    },
)
def initial_year_maximun_growth_government_expenditure():
    """
    Inital year maximum growth government expenditure
    """
    return _ext_constant_initial_year_maximun_growth_government_expenditure()


_ext_constant_initial_year_maximun_growth_government_expenditure = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_LIMIT_ANNUAL_GROWTH_GOVERNMENT_EXPENDITURE_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_year_maximun_growth_government_expenditure",
)


@component.add(
    name="INITIAL YEAR STRUCTURE GOVERNMENT CONSUMPTION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_structure_government_consumption_sp"
    },
)
def initial_year_structure_government_consumption_sp():
    return _ext_constant_initial_year_structure_government_consumption_sp()


_ext_constant_initial_year_structure_government_consumption_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_STRUCTURE_GOVERNMENT_CONSUMPTION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_structure_government_consumption_sp",
)


@component.add(
    name="INITIAL YEAR STRUCTURE GOVERNMENT EXPENDITURE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_structure_government_expenditure_sp"
    },
)
def initial_year_structure_government_expenditure_sp():
    """
    Initial year government expenditure structure.
    """
    return _ext_constant_initial_year_structure_government_expenditure_sp()


_ext_constant_initial_year_structure_government_expenditure_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_STRUCTURE_GOVERNMENT_EXPENDITURE_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_structure_government_expenditure_sp",
)


@component.add(
    name="INITIAL YEAR STRUCTURE GOVERNMENT INVESTMENT SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_structure_government_investment_sp"
    },
)
def initial_year_structure_government_investment_sp():
    return _ext_constant_initial_year_structure_government_investment_sp()


_ext_constant_initial_year_structure_government_investment_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_STRUCTURE_GOVERNMENT_INVESTMENT_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_structure_government_investment_sp",
)


@component.add(
    name="INITIAL YEAR TAX RATE PROFITS SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_tax_rate_profits_sp"},
)
def initial_year_tax_rate_profits_sp():
    """
    Initla year taxa rate of profits of corporations.
    """
    return _ext_constant_initial_year_tax_rate_profits_sp()


_ext_constant_initial_year_tax_rate_profits_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_TAX_RATE_PROFITS_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_tax_rate_profits_sp",
)


@component.add(
    name="LIMIT ANNUAL GROWTH GOVERNMENT EXPENDITURE SP",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limit_annual_growth_government_expenditure_sp"
    },
)
def limit_annual_growth_government_expenditure_sp():
    """
    Limit to annual growth in government expenditure
    """
    return _ext_constant_limit_annual_growth_government_expenditure_sp()


_ext_constant_limit_annual_growth_government_expenditure_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LIMIT_ANNUAL_GROWTH_GOVERNMENT_EXPENDITURE_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_limit_annual_growth_government_expenditure_sp",
)


@component.add(
    name="MAXIMUN GROWTH GOVERNMENT EXPENDITURE REST",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_maximun_growth_government_expenditure": 1,
        "select_limit_annual_growth_government_expenditure_sp": 1,
        "time_step": 2,
        "limit_annual_growth_government_expenditure_sp": 1,
        "annual_growth_government_expenditure_default": 1,
    },
)
def maximun_growth_government_expenditure_rest():
    """
    Maximum growth government expenditure excluding debt interests, investments to replace climate damages and basic income.
    """
    return if_then_else(
        np.logical_and(
            time() >= initial_year_maximun_growth_government_expenditure(),
            select_limit_annual_growth_government_expenditure_sp() == 1,
        ),
        lambda: limit_annual_growth_government_expenditure_sp() * time_step(),
        lambda: annual_growth_government_expenditure_default() * time_step(),
    )


@component.add(
    name="non adjusted government expenditure objective rest",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "government_expenditure_objective": 2,
        "debt_interest": 2,
        "public_gfcf_to_replace_climate_change_until_2015": 1,
        "public_gfcf_to_replace_climate_damage": 1,
    },
)
def non_adjusted_government_expenditure_objective_rest():
    """
    Non adjusted Government expenditure desired taking into account some specific expenditures. When the submodule runs isolated the variable takes the values of 2015 value of public GFCF... (which is zero, but should be isolated anyway, for future changes).
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: government_expenditure_objective()
        - debt_interest()
        - public_gfcf_to_replace_climate_change_until_2015(),
        lambda: government_expenditure_objective()
        - debt_interest()
        - public_gfcf_to_replace_climate_damage(),
    )


@component.add(
    name="number of households by income and type until 2015",
    units="households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_number_of_households_by_income_and_type_until_2015": 1},
    other_deps={
        "_sampleiftrue_number_of_households_by_income_and_type_until_2015": {
            "initial": {"number_of_households_by_income_and_type": 1},
            "step": {"time": 1, "number_of_households_by_income_and_type": 1},
        }
    },
)
def number_of_households_by_income_and_type_until_2015():
    """
    This variable is used to isolate the subgovernment module when its switch is zero. The variable takes the historic data of the variable contained inside it, until 2015 when it becomes a constant at that level.
    """
    return _sampleiftrue_number_of_households_by_income_and_type_until_2015()


_sampleiftrue_number_of_households_by_income_and_type_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    ),
    lambda: number_of_households_by_income_and_type(),
    lambda: number_of_households_by_income_and_type(),
    "_sampleiftrue_number_of_households_by_income_and_type_until_2015",
)


@component.add(
    name="people per household by income and type",
    units="person/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 2,
        "switch_eco_government": 1,
        "eu_persons_by_household_2015": 1,
        "households_correspondance_12_to_60": 2,
        "eu_persons_by_household": 1,
        "average_people_per_household_noneu_regions_until_2015": 1,
        "average_people_per_household_noneu_regions": 1,
    },
)
def people_per_household_by_income_and_type():
    """
    People per household by income and type. When the Economy or Government modules run isolated (switch economy = 0, switch eco government = 0) this variable takes data from the 2015 year as a constant for the whole period.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], :] = if_then_else(
        np.logical_or(switch_economy() == 0, switch_eco_government() == 0),
        lambda: sum(
            eu_persons_by_household_2015().rename(
                {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
            )
            * households_correspondance_12_to_60()
            .rename({"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"})
            .transpose("HOUSEHOLDS DEMOGRAPHY I!", "HOUSEHOLDS I"),
            dim=["HOUSEHOLDS DEMOGRAPHY I!"],
        ),
        lambda: sum(
            eu_persons_by_household().rename(
                {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
            )
            * households_correspondance_12_to_60()
            .rename({"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"})
            .transpose("HOUSEHOLDS DEMOGRAPHY I!", "HOUSEHOLDS I"),
            dim=["HOUSEHOLDS DEMOGRAPHY I!"],
        ),
    ).values
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        if_then_else(
            switch_economy() == 0,
            lambda: average_people_per_household_noneu_regions_until_2015(),
            lambda: average_people_per_household_noneu_regions(),
        )
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1)
        .values
    )
    return value


@component.add(
    name="public GFCF to replace climate change until 2015",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_public_gfcf_to_replace_climate_change_until_2015": 1},
    other_deps={
        "_sampleiftrue_public_gfcf_to_replace_climate_change_until_2015": {
            "initial": {"public_gfcf_to_replace_climate_damage": 1},
            "step": {"time": 1, "public_gfcf_to_replace_climate_damage": 1},
        }
    },
)
def public_gfcf_to_replace_climate_change_until_2015():
    """
    This variable is used to isolate the government submodule when it runs isolated. This function generates a variable that takes historic data from the variable contained in it until 2015, when it stays constant at the level of that year.
    """
    return _sampleiftrue_public_gfcf_to_replace_climate_change_until_2015()


_sampleiftrue_public_gfcf_to_replace_climate_change_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    ),
    lambda: public_gfcf_to_replace_climate_damage(),
    lambda: public_gfcf_to_replace_climate_damage(),
    "_sampleiftrue_public_gfcf_to_replace_climate_change_until_2015",
)


@component.add(
    name="RATIO BASIC INCOME TO AVERAGE DISPOSABLE INCOME SP",
    units="DMNL",
    subscripts=["REGIONS DISAGGREGATED HH I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_ratio_basic_income_to_average_disposable_income_sp"
    },
)
def ratio_basic_income_to_average_disposable_income_sp():
    """
    Ratio of basic income to average disposable income per capita.
    """
    return _ext_constant_ratio_basic_income_to_average_disposable_income_sp()


_ext_constant_ratio_basic_income_to_average_disposable_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "RATIO_BASIC_INCOME_TO_AVERAGE_DISPOSABLE_INCOME_SP*",
    {"REGIONS DISAGGREGATED HH I": _subscript_dict["REGIONS DISAGGREGATED HH I"]},
    _root,
    {"REGIONS DISAGGREGATED HH I": _subscript_dict["REGIONS DISAGGREGATED HH I"]},
    "_ext_constant_ratio_basic_income_to_average_disposable_income_sp",
)


@component.add(
    name="revenues GHG taxes",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "tax_ghg_sectors_until_2015": 1,
        "tax_ghg_households_until_2015": 1,
        "tax_ghg_sectors": 1,
        "tax_ghg_households": 1,
    },
)
def revenues_ghg_taxes():
    """
    Government revenues from GHG taxes.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: tax_ghg_households_until_2015() + tax_ghg_sectors_until_2015(),
        lambda: tax_ghg_households() + tax_ghg_sectors(),
    )


@component.add(
    name="SELECT DEBT INTEREST RATE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_debt_interest_rate_sp"},
)
def select_debt_interest_rate_sp():
    """
    Initial year debt interest rate.
    """
    return _ext_constant_select_debt_interest_rate_sp()


_ext_constant_select_debt_interest_rate_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_DEBT_INTEREST_RATE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_debt_interest_rate_sp",
)


@component.add(
    name="SELECT GOVERNMENT BUDGET BALANCE TO GDP OBJECTIVE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_government_budget_balance_to_gdp_objective_sp"
    },
)
def select_government_budget_balance_to_gdp_objective_sp():
    """
    Goverment deficit or surplus to GDP objetive scenario 0: Default 1: User defined
    """
    return _ext_constant_select_government_budget_balance_to_gdp_objective_sp()


_ext_constant_select_government_budget_balance_to_gdp_objective_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_GOVERNMENT_BUDGET_BALANCE_TO_GDP_OBJECTIVE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_government_budget_balance_to_gdp_objective_sp",
)


@component.add(
    name="SELECT LIMIT ANNUAL GROWTH GOVERNMENT EXPENDITURE SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_limit_annual_growth_government_expenditure_sp"
    },
)
def select_limit_annual_growth_government_expenditure_sp():
    """
    Select maximum growth government expenditure: 0: No limit 1: Limit
    """
    return _ext_constant_select_limit_annual_growth_government_expenditure_sp()


_ext_constant_select_limit_annual_growth_government_expenditure_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_LIMIT_ANNUAL_GROWTH_GOVERNMENT_EXPENDITURE_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_select_limit_annual_growth_government_expenditure_sp",
)


@component.add(
    name="SELECT STRUCTURE GOVERNMENT CONSUMPTION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_structure_government_consumption_sp"
    },
)
def select_structure_government_consumption_sp():
    """
    Government consumption structure 0: Default 1: User defined
    """
    return _ext_constant_select_structure_government_consumption_sp()


_ext_constant_select_structure_government_consumption_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_STRUCTURE_GOVERNMENT_CONSUMPTION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_structure_government_consumption_sp",
)


@component.add(
    name="SELECT STRUCTURE GOVERNMENT EXPENDITURE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_structure_government_expenditure_sp"
    },
)
def select_structure_government_expenditure_sp():
    """
    Government expenditure structure 0: Default 1: User defined
    """
    return _ext_constant_select_structure_government_expenditure_sp()


_ext_constant_select_structure_government_expenditure_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_STRUCTURE_GOVERNMENT_EXPENDITURE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_structure_government_expenditure_sp",
)


@component.add(
    name="SELECT STRUCTURE GOVERNMENT INVESTMENT SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_structure_government_investment_sp"
    },
)
def select_structure_government_investment_sp():
    """
    Government investment structure 0: Default 1: User defined
    """
    return _ext_constant_select_structure_government_investment_sp()


_ext_constant_select_structure_government_investment_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_STRUCTURE_GOVERNMENT_INVESTMENT_SP",
    {},
    _root,
    {},
    "_ext_constant_select_structure_government_investment_sp",
)


@component.add(
    name="SELECT TAX RATE PROFITS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_tax_rate_profits_sp"},
)
def select_tax_rate_profits_sp():
    """
    Tax rate profits 0: Default 1: User defined
    """
    return _ext_constant_select_tax_rate_profits_sp()


_ext_constant_select_tax_rate_profits_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_TAX_RATE_PROFITS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_tax_rate_profits_sp",
)


@component.add(
    name="SHARE GHG REVENUES TO FINANCE BASIC INCOME SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_ghg_revenues_to_finance_basic_income_sp"
    },
)
def share_ghg_revenues_to_finance_basic_income_sp():
    """
    Share GHG tax revenues used to fiance a universal basic income
    """
    return _ext_constant_share_ghg_revenues_to_finance_basic_income_sp()


_ext_constant_share_ghg_revenues_to_finance_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SHARE_GHG_REVENUES_TO_FINANCE_BASIC_INCOME_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_share_ghg_revenues_to_finance_basic_income_sp",
)


@component.add(
    name="SHARE GHG REVENUES TO INCOME TAX SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_ghg_revenues_to_income_tax_sp"},
)
def share_ghg_revenues_to_income_tax_sp():
    """
    Share GHG tax revenues used to reduce income taxes
    """
    return _ext_constant_share_ghg_revenues_to_income_tax_sp()


_ext_constant_share_ghg_revenues_to_income_tax_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SHARE_GHG_REVENUES_TO_INCOME_TAX_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_share_ghg_revenues_to_income_tax_sp",
)


@component.add(
    name="SHARE GHG REVENUES TO INCREASE SOCIAL BENEFITS SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_ghg_revenues_to_increase_social_benefits_sp"
    },
)
def share_ghg_revenues_to_increase_social_benefits_sp():
    """
    Share GHG tax revenues used to increase social benefits
    """
    return _ext_constant_share_ghg_revenues_to_increase_social_benefits_sp()


_ext_constant_share_ghg_revenues_to_increase_social_benefits_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SHARE_GHG_REVENUES_TO_INCOME_TAX_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_share_ghg_revenues_to_increase_social_benefits_sp",
)


@component.add(
    name="SHARE GHG REVENUES TO REDUCE DEBT SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_ghg_revenues_to_reduce_debt_sp"},
)
def share_ghg_revenues_to_reduce_debt_sp():
    """
    Share GHG tax revenues used to reduce government debt
    """
    return _ext_constant_share_ghg_revenues_to_reduce_debt_sp()


_ext_constant_share_ghg_revenues_to_reduce_debt_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SHARE_GHG_REVENUES_TO_REDUCE_DEBT_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_share_ghg_revenues_to_reduce_debt_sp",
)


@component.add(
    name="social benefits",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_rest": 1,
        "structure_government_expenditure": 1,
        "ghg_tax_revenues_used_to_increase_social_benefits": 1,
    },
)
def social_benefits():
    """
    Social benefits paid by the government (such as pensions and payments to unemployed people). THIS SHOULD BE LINKED TO THE LABORU AND DEMOGRAPHIC MODULES.
    """
    return (
        government_expenditure_rest()
        * structure_government_expenditure()
        .loc[:, "GOV SOCIAL BENEFITS"]
        .reset_coords(drop=True)
        + ghg_tax_revenues_used_to_increase_social_benefits()
    )


@component.add(
    name="social security",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "tax_rate_social_security_default": 1,
        "initial_labour_compensation": 1,
        "number_of_households_by_income_and_type": 1,
        "households_social_security": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def social_security():
    """
    Social security contributions.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: tax_rate_social_security_default()
        * sum(
            initial_labour_compensation().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
        lambda: sum(
            households_social_security().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            )
            / unit_conversion_dollars_mdollars(),
            dim=["HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="structure government consumption",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "structure_government_consumption_default": 2,
        "select_structure_government_consumption_sp": 1,
        "structure_government_consumption_sp": 1,
        "initial_year_structure_government_consumption_sp": 1,
    },
)
def structure_government_consumption():
    """
    Structure of government consumption by category (COFOG classification: Classification of the Functions of the Government).
    """
    return if_then_else(
        time() <= 2015,
        lambda: structure_government_consumption_default(),
        lambda: if_then_else(
            np.logical_and(
                select_structure_government_consumption_sp() == 1,
                initial_year_structure_government_consumption_sp() >= time(),
            ),
            lambda: structure_government_consumption_sp(),
            lambda: structure_government_consumption_default(),
        ),
    )


@component.add(
    name="STRUCTURE GOVERNMENT CONSUMPTION SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_structure_government_consumption_sp"},
)
def structure_government_consumption_sp():
    """
    Structure government consumption by category (COFOG classification: Classification of the Functions of the Government).
    """
    return _ext_constant_structure_government_consumption_sp()


_ext_constant_structure_government_consumption_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "STRUCTURE_GOVERNMENT_CONSUMPTION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "COFOG I": _subscript_dict["COFOG I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "COFOG I": _subscript_dict["COFOG I"],
    },
    "_ext_constant_structure_government_consumption_sp",
)


@component.add(
    name="structure government expenditure",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GOVERNMENT EXPENDITURE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 10,
        "share_government_expenditure_consumption_default": 2,
        "initial_year_structure_government_expenditure_sp": 5,
        "structure_government_expenditure_sp": 5,
        "select_structure_government_expenditure_sp": 5,
        "share_government_expenditure_investment_default": 2,
        "share_government_expenditure_social_benefits_default": 2,
        "share_government_expenditure_transferences_default": 2,
        "share_government_expenditure_other_expenditures_default": 2,
    },
)
def structure_government_expenditure():
    """
    Structure of government expenditure
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "GOVERNMENT EXPENDITURE I": _subscript_dict["GOVERNMENT EXPENDITURE I"],
        },
        ["REGIONS 35 I", "GOVERNMENT EXPENDITURE I"],
    )
    value.loc[:, ["GOV CONSUMPTION"]] = (
        if_then_else(
            time() <= 2015,
            lambda: share_government_expenditure_consumption_default(),
            lambda: if_then_else(
                np.logical_and(
                    select_structure_government_expenditure_sp() == 1,
                    initial_year_structure_government_expenditure_sp() >= time(),
                ),
                lambda: structure_government_expenditure_sp()
                .loc[:, "GOV CONSUMPTION"]
                .reset_coords(drop=True),
                lambda: share_government_expenditure_consumption_default(),
            ),
        )
        .expand_dims({"GOVERNMENT EXPENDITURE I": ["GOV CONSUMPTION"]}, 1)
        .values
    )
    value.loc[:, ["GOV INVESTMENT"]] = (
        if_then_else(
            time() <= 2015,
            lambda: share_government_expenditure_investment_default(),
            lambda: if_then_else(
                np.logical_and(
                    select_structure_government_expenditure_sp() == 1,
                    initial_year_structure_government_expenditure_sp() >= time(),
                ),
                lambda: structure_government_expenditure_sp()
                .loc[:, "GOV INVESTMENT"]
                .reset_coords(drop=True),
                lambda: share_government_expenditure_investment_default(),
            ),
        )
        .expand_dims({"GOVERNMENT EXPENDITURE I": ["GOV INVESTMENT"]}, 1)
        .values
    )
    value.loc[:, ["GOV SOCIAL BENEFITS"]] = (
        if_then_else(
            time() <= 2015,
            lambda: share_government_expenditure_social_benefits_default(),
            lambda: if_then_else(
                np.logical_and(
                    select_structure_government_expenditure_sp() == 1,
                    initial_year_structure_government_expenditure_sp() >= time(),
                ),
                lambda: structure_government_expenditure_sp()
                .loc[:, "GOV SOCIAL BENEFITS"]
                .reset_coords(drop=True),
                lambda: share_government_expenditure_social_benefits_default(),
            ),
        )
        .expand_dims({"GOVERNMENT EXPENDITURE I": ["GOV SOCIAL BENEFITS"]}, 1)
        .values
    )
    value.loc[:, ["GOV TRANSFERENCES"]] = (
        if_then_else(
            time() <= 2015,
            lambda: share_government_expenditure_transferences_default(),
            lambda: if_then_else(
                np.logical_and(
                    select_structure_government_expenditure_sp() == 1,
                    initial_year_structure_government_expenditure_sp() >= time(),
                ),
                lambda: structure_government_expenditure_sp()
                .loc[:, "GOV TRANSFERENCES"]
                .reset_coords(drop=True),
                lambda: share_government_expenditure_transferences_default(),
            ),
        )
        .expand_dims({"GOVERNMENT EXPENDITURE I": ["GOV TRANSFERENCES"]}, 1)
        .values
    )
    value.loc[:, ["GOV OTHER EXPENDITURES"]] = (
        if_then_else(
            time() <= 2015,
            lambda: share_government_expenditure_other_expenditures_default(),
            lambda: if_then_else(
                np.logical_and(
                    select_structure_government_expenditure_sp() == 1,
                    initial_year_structure_government_expenditure_sp() >= time(),
                ),
                lambda: structure_government_expenditure_sp()
                .loc[:, "GOV OTHER EXPENDITURES"]
                .reset_coords(drop=True),
                lambda: share_government_expenditure_other_expenditures_default(),
            ),
        )
        .expand_dims({"GOVERNMENT EXPENDITURE I": ["GOV OTHER EXPENDITURES"]}, 1)
        .values
    )
    return value


@component.add(
    name="STRUCTURE GOVERNMENT EXPENDITURE SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GOVERNMENT EXPENDITURE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_structure_government_expenditure_sp"},
)
def structure_government_expenditure_sp():
    """
    Structure government expenditure
    """
    return _ext_constant_structure_government_expenditure_sp()


_ext_constant_structure_government_expenditure_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "STRUCTURE_GOVERNMENT_EXPENDITURE_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "GOVERNMENT EXPENDITURE I": _subscript_dict["GOVERNMENT EXPENDITURE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "GOVERNMENT EXPENDITURE I": _subscript_dict["GOVERNMENT EXPENDITURE I"],
    },
    "_ext_constant_structure_government_expenditure_sp",
)


@component.add(
    name="structure government investment",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "structure_government_investment_default": 2,
        "select_structure_government_investment_sp": 1,
        "structure_government_investment_sp": 1,
        "initial_year_structure_government_investment_sp": 1,
    },
)
def structure_government_investment():
    """
    Structure of government investment by category (COFOG classification: Classification of the Functions of the Government).
    """
    return if_then_else(
        time() <= 2015,
        lambda: structure_government_investment_default(),
        lambda: if_then_else(
            np.logical_and(
                select_structure_government_investment_sp() == 1,
                initial_year_structure_government_investment_sp() >= time(),
            ),
            lambda: structure_government_investment_sp(),
            lambda: structure_government_investment_default(),
        ),
    )


@component.add(
    name="STRUCTURE GOVERNMENT INVESTMENT SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_structure_government_investment_sp"},
)
def structure_government_investment_sp():
    """
    Structure government investment by category (COFOG classification: Classification of the Functions of the Government).
    """
    return _ext_constant_structure_government_investment_sp()


_ext_constant_structure_government_investment_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "STRUCTURE_GOVERNMENT_INVESTMENT_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "COFOG I": _subscript_dict["COFOG I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "COFOG I": _subscript_dict["COFOG I"],
    },
    "_ext_constant_structure_government_investment_sp",
)


@component.add(
    name="SWITCH ECO GOVERNMENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_government"},
)
def switch_eco_government():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_government()


_ext_constant_switch_eco_government = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_GOVERNMENT",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_government",
)


@component.add(
    name="SWITCH POLICY BASIC INCOME SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_switch_policy_basic_income_sp"},
)
def switch_policy_basic_income_sp():
    """
    Basic income policy 0: No Policy 1: Basic income
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        [
            "BELGIUM",
            "BULGARIA",
            "CROATIA",
            "CYPRUS",
            "CZECH REPUBLIC",
            "DENMARK",
            "ESTONIA",
            "FINLAND",
            "FRANCE",
            "GERMANY",
            "GREECE",
            "HUNGARY",
            "IRELAND",
            "LATVIA",
            "LITHUANIA",
            "LUXEMBOURG",
            "POLAND",
            "PORTUGAL",
            "SLOVAKIA",
            "SPAIN",
            "SWEDEN",
        ]
    ] = True
    value.values[def_subs.values] = (
        _ext_constant_switch_policy_basic_income_sp().values[def_subs.values]
    )
    value.loc[_subscript_dict["REGIONS NON DISAGGREGATED HH I"]] = 0
    return value


_ext_constant_switch_policy_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SWITCH_POLICY_BASIC_INCOME_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS DISAGGREGATED HH I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_switch_policy_basic_income_sp",
)


@component.add(
    name="tax GHG households until 2015",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_tax_ghg_households_until_2015": 1},
    other_deps={
        "_sampleiftrue_tax_ghg_households_until_2015": {
            "initial": {"tax_ghg_households": 1},
            "step": {"time": 1, "tax_ghg_households": 1},
        }
    },
)
def tax_ghg_households_until_2015():
    """
    This variable is created to isolate the government module. When 2015 is reached it stops taking the historic value of the variable contained in it and stays constant at the 2015 level of this variable.
    """
    return _sampleiftrue_tax_ghg_households_until_2015()


_sampleiftrue_tax_ghg_households_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    ),
    lambda: tax_ghg_households(),
    lambda: tax_ghg_households(),
    "_sampleiftrue_tax_ghg_households_until_2015",
)


@component.add(
    name="tax GHG sectors until 2015",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_tax_ghg_sectors_until_2015": 1},
    other_deps={
        "_sampleiftrue_tax_ghg_sectors_until_2015": {
            "initial": {"tax_ghg_sectors": 1},
            "step": {"time": 1, "tax_ghg_sectors": 1},
        }
    },
)
def tax_ghg_sectors_until_2015():
    """
    This variable is used to isolate the government submodule when it runs isolated. It takes the historic data of the variable contained in it until 2015, when it stays constant at that level for the rest of the time.
    """
    return _sampleiftrue_tax_ghg_sectors_until_2015()


_sampleiftrue_tax_ghg_sectors_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    ),
    lambda: tax_ghg_sectors(),
    lambda: tax_ghg_sectors(),
    "_sampleiftrue_tax_ghg_sectors_until_2015",
)


@component.add(
    name="tax income corporations",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_delayed_net_operating_surplus": 1,
        "tax_rate_on_profits_default": 1,
        "tax_income_corportations_to_finance_basic_income": 1,
        "select_policy_finance_basic_income_sp": 1,
        "delayed_ts_net_operating_surplus_total": 2,
        "tax_rate_on_profits": 2,
    },
)
def tax_income_corporations():
    """
    Total taxes on corporations profits.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: sum(
            initial_delayed_net_operating_surplus().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        * tax_rate_on_profits_default(),
        lambda: if_then_else(
            select_policy_finance_basic_income_sp() == 1,
            lambda: delayed_ts_net_operating_surplus_total() * tax_rate_on_profits()
            + tax_income_corportations_to_finance_basic_income(),
            lambda: delayed_ts_net_operating_surplus_total() * tax_rate_on_profits(),
        ),
    )


@component.add(
    name="tax income corportations to finance basic income",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"government_basic_income_expenditure": 1},
)
def tax_income_corportations_to_finance_basic_income():
    """
    Tax on profits of corporations to finance universal basic income
    """
    return government_basic_income_expenditure()


@component.add(
    name="tax rate on profits",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "tax_rate_on_profits_default": 2,
        "initial_year_tax_rate_profits_sp": 1,
        "tax_rate_profits_sp": 1,
        "select_tax_rate_profits_sp": 1,
    },
)
def tax_rate_on_profits():
    """
    Tax rate on taxes on the income or profits of corporations
    """
    return if_then_else(
        time() <= 2015,
        lambda: tax_rate_on_profits_default(),
        lambda: if_then_else(
            np.logical_and(
                select_tax_rate_profits_sp() == 1,
                initial_year_tax_rate_profits_sp() >= time(),
            ),
            lambda: tax_rate_profits_sp(),
            lambda: tax_rate_on_profits_default(),
        ),
    )


@component.add(
    name="TAX RATE PROFITS SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tax_rate_profits_sp"},
)
def tax_rate_profits_sp():
    """
    Tax rate on taxes on the income or profits of corporations.
    """
    return _ext_constant_tax_rate_profits_sp()


_ext_constant_tax_rate_profits_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "TAX_RATE_PROFITS_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_tax_rate_profits_sp",
)


@component.add(
    name="taxes on income",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_taxes_on_income_hh": 1,
        "number_of_households_by_income_and_type": 1,
        "households_income_tax": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def taxes_on_income():
    """
    Total of taxes on income.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: initial_taxes_on_income_hh(),
        lambda: sum(
            households_income_tax().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="taxes on income and wealth",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tax_income_corporations": 1,
        "taxes_on_income": 1,
        "taxes_on_wealth": 1,
    },
)
def taxes_on_income_and_wealth():
    """
    Total of taxes on income and wealth.
    """
    return tax_income_corporations() + taxes_on_income() + taxes_on_wealth()


@component.add(
    name="taxes on production",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_eco_government": 1,
        "statistical_difference_net_taxes_production": 1,
        "initial_taxes_production": 1,
        "delayed_ts_taxes_production": 1,
    },
)
def taxes_on_production():
    """
    Net taxes on production.
    """
    return if_then_else(
        np.logical_or(time() <= 2015, switch_eco_government() == 0),
        lambda: sum(
            initial_taxes_production().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        + statistical_difference_net_taxes_production(),
        lambda: sum(
            delayed_ts_taxes_production().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="taxes on resources paid by extraction sectors",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 7,
        "delayed_ts_taxes_on_resources_until_2015": 7,
        "delayed_ts_output_real_until_2015": 14,
        "delayed_ts_output_real": 14,
        "delayed_ts_taxes_on_resources": 7,
    },
)
def taxes_on_resources_paid_by_extraction_sectors():
    """
    Taxes on resources split into the different regions according to their output share. Tax Revenue from metals/ resources Tax. The tax revenue is collected by the countries that are extracting these materials. It is a policy variable. The idea is with increasing prices for resource extraction by imposing a tax the demand for the taxed resources will decrease
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["EXTRACTION GAS"]] = False
    except_subs.loc[:, ["MINING COAL"]] = False
    except_subs.loc[:, ["MINING AND MANUFACTURING COPPER"]] = False
    except_subs.loc[:, ["MINING AND MANUFACTURING ALUMINIUM"]] = False
    except_subs.loc[:, ["MINING AND MANUFACTURING IRON"]] = False
    except_subs.loc[:, ["MINING AND MANUFACTURING NICKEL"]] = False
    except_subs.loc[:, ["EXTRACTION OIL"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["EXTRACTION GAS"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Gas W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "EXTRACTION GAS"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "EXTRACTION GAS"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Gas W"])
            * delayed_ts_output_real().loc[:, "EXTRACTION GAS"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "EXTRACTION GAS"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Coal W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "MINING COAL"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "MINING COAL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Coal W"])
            * delayed_ts_output_real().loc[:, "MINING COAL"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING COAL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["MINING AND MANUFACTURING COPPER"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Cu W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "MINING AND MANUFACTURING COPPER"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "MINING AND MANUFACTURING COPPER"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Cu W"])
            * delayed_ts_output_real()
            .loc[:, "MINING AND MANUFACTURING COPPER"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING AND MANUFACTURING COPPER"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER MINNING": ["MINING AND MANUFACTURING COPPER"]}, 1)
        .values
    )
    value.loc[:, ["MINING AND MANUFACTURING ALUMINIUM"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Al W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "MINING AND MANUFACTURING ALUMINIUM"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "MINING AND MANUFACTURING ALUMINIUM"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Al W"])
            * delayed_ts_output_real()
            .loc[:, "MINING AND MANUFACTURING ALUMINIUM"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING AND MANUFACTURING ALUMINIUM"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER MINNING": ["MINING AND MANUFACTURING ALUMINIUM"]}, 1)
        .values
    )
    value.loc[:, ["MINING AND MANUFACTURING IRON"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Fe W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "MINING AND MANUFACTURING IRON"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "MINING AND MANUFACTURING IRON"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Fe W"])
            * delayed_ts_output_real()
            .loc[:, "MINING AND MANUFACTURING IRON"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING AND MANUFACTURING IRON"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER MINNING": ["MINING AND MANUFACTURING IRON"]}, 1)
        .values
    )
    value.loc[:, ["MINING AND MANUFACTURING NICKEL"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Ni W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "MINING AND MANUFACTURING NICKEL"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "MINING AND MANUFACTURING NICKEL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Ni W"])
            * delayed_ts_output_real()
            .loc[:, "MINING AND MANUFACTURING NICKEL"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "MINING AND MANUFACTURING NICKEL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER MINNING": ["MINING AND MANUFACTURING NICKEL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION OIL"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: float(delayed_ts_taxes_on_resources_until_2015().loc["Oil W"])
            * delayed_ts_output_real_until_2015()
            .loc[:, "EXTRACTION OIL"]
            .reset_coords(drop=True)
            / sum(
                delayed_ts_output_real_until_2015()
                .loc[:, "EXTRACTION OIL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
            lambda: float(delayed_ts_taxes_on_resources().loc["Oil W"])
            * delayed_ts_output_real().loc[:, "EXTRACTION OIL"].reset_coords(drop=True)
            / sum(
                delayed_ts_output_real()
                .loc[:, "EXTRACTION OIL"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 35 I!"}),
                dim=["REGIONS 35 I!"],
            ),
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION OIL"]}, 1)
        .values
    )
    return value


@component.add(
    name="taxes on wealth",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_government": 1,
        "initial_taxes_on_wealth": 1,
        "households_wealth_tax": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def taxes_on_wealth():
    """
    Total of taxes on wealth.
    """
    return if_then_else(
        switch_eco_government() == 0,
        lambda: initial_taxes_on_wealth(),
        lambda: sum(
            households_wealth_tax().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        )
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="taxes products",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_eco_government": 1,
        "initial_taxes_products_final_demand": 1,
        "initial_taxes_products_by_sector": 1,
        "statistical_difference_net_taxes_products": 2,
        "delayed_ts_taxes_products_by_sector": 1,
        "delayed_ts_taxes_products_final_demand": 1,
    },
)
def taxes_products():
    """
    Net taxes on products.
    """
    return if_then_else(
        np.logical_or(time() <= 2015, switch_eco_government() == 0),
        lambda: sum(
            initial_taxes_products_final_demand().rename(
                {"FINAL DEMAND I": "FINAL DEMAND I!"}
            ),
            dim=["FINAL DEMAND I!"],
        )
        + sum(
            initial_taxes_products_by_sector().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        + statistical_difference_net_taxes_products(),
        lambda: sum(
            delayed_ts_taxes_products_final_demand().rename(
                {"FINAL DEMAND I": "FINAL DEMAND I!"}
            ),
            dim=["FINAL DEMAND I!"],
        )
        + sum(
            delayed_ts_taxes_products_by_sector().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        + statistical_difference_net_taxes_products(),
    )
