"""
Module financehouseholds
Translated using PySD version 3.14.0
"""

@component.add(
    name="AUX BASIC INCOME TAX PAYERS SP",
    units="DMNL",
    subscripts=["HOUSEHOLDS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"basic_income_tax_payers_sp": 1},
)
def aux_basic_income_tax_payers_sp():
    value = xr.DataArray(
        np.nan, {"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, ["HOUSEHOLDS I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["HOUSEHOLDS EU27 I"]] = False
    except_subs.loc[["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    value.loc[_subscript_dict["HOUSEHOLDS EU27 I"]] = (
        basic_income_tax_payers_sp().values
    )
    value.loc[["REPRESENTATIVE HOUSEHOLD"]] = 0
    return value


@component.add(
    name="average households real net wealth 9R",
    units="dollars 2015/households",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_net_wealth": 1,
        "consumer_price_index": 1,
        "dollars_per_dollars_2015": 1,
        "average_households_real_net_wealth_eu27": 1,
    },
)
def average_households_real_net_wealth_9r():
    """
    average_households_real_net_wealth_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = sum(
        households_net_wealth()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"})
        * zidz(
            xr.DataArray(
                100, {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, ["REGIONS 8 I"]
            ),
            consumer_price_index()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 35 I": "REGIONS 8 I"}),
        )
        / dollars_per_dollars_2015(),
        dim=["HOUSEHOLDS I!"],
    ).values
    value.loc[["EU27"]] = average_households_real_net_wealth_eu27()
    return value


@component.add(
    name="average households real net wealth EU27",
    units="dollars 2015/households",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "number_of_households_by_income_and_type": 3,
        "base_number_of_households": 1,
        "households_net_wealth": 2,
        "dollars_per_dollars_2015": 2,
        "consumer_price_index": 2,
    },
)
def average_households_real_net_wealth_eu27():
    """
    ZIDZ(SUM(households_net_wealth[REGIONS_EU27_I!,HOUSEHOLDS_I!]*ZIDZ(100,consumer_price _index[REGIONS_EU27_I!])*number_of_households_by_income_and_type[REGIONS_EU 27_I!,HOUSEHOLDS_I !]),SUM(number_of_households_by_income_and_type[REGIONS_EU27_I!,HOUSEHOLDS_ I!]))
    """
    return if_then_else(
        time() < 2015,
        lambda: zidz(
            sum(
                households_net_wealth()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                )
                * zidz(
                    xr.DataArray(
                        100,
                        {
                            "REGIONS EU27 I!": [
                                "AUSTRIA",
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
                                "ITALY",
                                "LATVIA",
                                "LITHUANIA",
                                "LUXEMBOURG",
                                "MALTA",
                                "NETHERLANDS",
                                "POLAND",
                                "PORTUGAL",
                                "ROMANIA",
                                "SLOVAKIA",
                                "SLOVENIA",
                                "SPAIN",
                                "SWEDEN",
                            ]
                        },
                        ["REGIONS EU27 I!"],
                    ),
                    consumer_price_index()
                    .loc[_subscript_dict["REGIONS EU27 I"]]
                    .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                )
                / dollars_per_dollars_2015()
                * number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
            ),
            sum(
                base_number_of_households()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
            ),
        ),
        lambda: zidz(
            sum(
                households_net_wealth()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                )
                * zidz(
                    xr.DataArray(
                        100,
                        {
                            "REGIONS EU27 I!": [
                                "AUSTRIA",
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
                                "ITALY",
                                "LATVIA",
                                "LITHUANIA",
                                "LUXEMBOURG",
                                "MALTA",
                                "NETHERLANDS",
                                "POLAND",
                                "PORTUGAL",
                                "ROMANIA",
                                "SLOVAKIA",
                                "SLOVENIA",
                                "SPAIN",
                                "SWEDEN",
                            ]
                        },
                        ["REGIONS EU27 I!"],
                    ),
                    consumer_price_index()
                    .loc[_subscript_dict["REGIONS EU27 I"]]
                    .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                )
                / dollars_per_dollars_2015()
                * number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
            ),
            sum(
                number_of_households_by_income_and_type()
                .loc[_subscript_dict["REGIONS EU27 I"], :]
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
            ),
        ),
    )


@component.add(
    name="BASIC INCOME TAX PAYERS SP",
    units="DMNL",
    subscripts=["HOUSEHOLDS EU27 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_basic_income_tax_payers_sp"},
)
def basic_income_tax_payers_sp():
    """
    Vector of ones for selecting those households paying taxed to finance basic income
    """
    return _ext_constant_basic_income_tax_payers_sp()


_ext_constant_basic_income_tax_payers_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "BASIC_INCOME_TAX_PAYERS_SP*",
    {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]},
    _root,
    {"HOUSEHOLDS EU27 I": _subscript_dict["HOUSEHOLDS EU27 I"]},
    "_ext_constant_basic_income_tax_payers_sp",
)


@component.add(
    name="decrease in households capital stock due to depreciation",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"depreciation_rate": 1, "households_capital_stock": 1},
)
def decrease_in_households_capital_stock_due_to_depreciation():
    """
    Decrease in households capital stock due to depreciation.
    """
    return (
        depreciation_rate().loc[:, "REAL ESTATE"].reset_coords(drop=True)
        * households_capital_stock()
    )


@component.add(
    name="delayed TS households financial assets",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_financial_assets": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_financial_assets": {
            "initial": {"time_step": 1},
            "step": {"households_financial_assets": 1},
        }
    },
)
def delayed_ts_households_financial_assets():
    """
    Delayed (Time step) households financial assets
    """
    return _delayfixed_delayed_ts_households_financial_assets()


_delayfixed_delayed_ts_households_financial_assets = DelayFixed(
    lambda: households_financial_assets(),
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
    "_delayfixed_delayed_ts_households_financial_assets",
)


@component.add(
    name="delayed TS households net lending",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_net_lending": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_net_lending": {
            "initial": {"time_step": 1},
            "step": {"households_net_lending": 1},
        }
    },
)
def delayed_ts_households_net_lending():
    return _delayfixed_delayed_ts_households_net_lending()


_delayfixed_delayed_ts_households_net_lending = DelayFixed(
    lambda: households_net_lending(),
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
    "_delayfixed_delayed_ts_households_net_lending",
)


@component.add(
    name="delayed TS households net wealth",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_households_net_wealth": 1},
    other_deps={
        "_delayfixed_delayed_ts_households_net_wealth": {
            "initial": {"initial_households_net_wealth": 1, "time_step": 1},
            "step": {"households_net_wealth": 1},
        }
    },
)
def delayed_ts_households_net_wealth():
    """
    Delayed (time step) households net wealth
    """
    return _delayfixed_delayed_ts_households_net_wealth()


_delayfixed_delayed_ts_households_net_wealth = DelayFixed(
    lambda: households_net_wealth(),
    lambda: time_step(),
    lambda: initial_households_net_wealth(),
    time_step,
    "_delayfixed_delayed_ts_households_net_wealth",
)


@component.add(
    name="households capital stock",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_capital_stock": 1},
    other_deps={
        "_integ_households_capital_stock": {
            "initial": {
                "initial_households_capital_stock": 1,
                "base_number_of_households": 1,
            },
            "step": {
                "time": 1,
                "decrease_in_households_capital_stock_due_to_depreciation": 1,
                "increase_in_households_capital_stock_due_to_investments": 1,
                "variation_in_households_capital_stock_due_to_revalorizations": 1,
            },
        }
    },
)
def households_capital_stock():
    """
    Households capital stock, mainly housing.
    """
    return _integ_households_capital_stock()


_integ_households_capital_stock = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: increase_in_households_capital_stock_due_to_investments()
        + variation_in_households_capital_stock_due_to_revalorizations()
        - decrease_in_households_capital_stock_due_to_depreciation(),
    ),
    lambda: zidz(initial_households_capital_stock(), base_number_of_households()),
    "_integ_households_capital_stock",
)


@component.add(
    name="households financial assets",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_financial_assets": 1},
    other_deps={
        "_integ_households_financial_assets": {
            "initial": {
                "initial_households_financial_assets": 1,
                "base_number_of_households": 1,
            },
            "step": {
                "time": 1,
                "variation_in_households_financial_assets_due_to_net_lending": 1,
            },
        }
    },
)
def households_financial_assets():
    """
    Total households financial assets.
    """
    return _integ_households_financial_assets()


_integ_households_financial_assets = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: variation_in_households_financial_assets_due_to_net_lending(),
    ),
    lambda: zidz(initial_households_financial_assets(), base_number_of_households()),
    "_integ_households_financial_assets",
)


@component.add(
    name="households financial liabilities",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_households_financial_liabilities": 1},
    other_deps={
        "_integ_households_financial_liabilities": {
            "initial": {
                "initial_households_financial_liabilities": 1,
                "base_number_of_households": 1,
            },
            "step": {"time": 1, "variation_in_households_financial_liabilities": 1},
        }
    },
)
def households_financial_liabilities():
    """
    Total households financial liabilities.
    """
    return _integ_households_financial_liabilities()


_integ_households_financial_liabilities = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: variation_in_households_financial_liabilities(),
    ),
    lambda: zidz(
        initial_households_financial_liabilities(), base_number_of_households()
    ),
    "_integ_households_financial_liabilities",
)


@component.add(
    name="households net lending",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_finance": 1,
        "initial_gross_savings": 1,
        "increase_in_households_capital_stock_due_to_investments": 2,
        "households_gross_savings": 1,
    },
)
def households_net_lending():
    """
    Amount of money that households can use to buy financial assets or cancel their liabilities.
    """
    return if_then_else(
        switch_finance() == 0,
        lambda: initial_gross_savings()
        - increase_in_households_capital_stock_due_to_investments(),
        lambda: households_gross_savings()
        - increase_in_households_capital_stock_due_to_investments(),
    )


@component.add(
    name="households net wealth",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_capital_stock": 1,
        "households_financial_assets": 1,
        "households_financial_liabilities": 1,
    },
)
def households_net_wealth():
    """
    Total assets minus total liabilities of households.
    """
    return (
        households_capital_stock()
        + households_financial_assets()
        - households_financial_liabilities()
    )


@component.add(
    name="households property income paid",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_liabilities": 1,
        "interest_rate_for_households_liabilities": 1,
    },
)
def households_property_income_paid():
    """
    Households property income paid by household type.
    """
    return (
        households_financial_liabilities() * interest_rate_for_households_liabilities()
    )


@component.add(
    name="households property income received",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_assets": 1,
        "households_capital_stock": 1,
        "interest_rate_for_households_assets": 1,
    },
)
def households_property_income_received():
    """
    Households property income received by household type.
    """
    return (
        households_financial_assets() + households_capital_stock()
    ) * interest_rate_for_households_assets()


@component.add(
    name="households taxes on assets to finance basic income",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_on_assets_to_finance_basic_income_by_household_group": 1,
        "unit_conversion_dollars_mdollars": 1,
        "number_of_households_by_income_and_type": 1,
    },
)
def households_taxes_on_assets_to_finance_basic_income():
    """
    Taxes on financial assets to finance basic income paid by each household
    """
    return zidz(
        taxes_on_assets_to_finance_basic_income_by_household_group()
        * unit_conversion_dollars_mdollars(),
        number_of_households_by_income_and_type(),
    )


@component.add(
    name="implicit tax rate to finance basic income",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_taxes_on_assets_to_finance_basic_income": 1,
        "households_financial_assets": 1,
    },
)
def implicit_tax_rate_to_finance_basic_income():
    """
    Implicit tax rate on financial assets to finace basic income.
    """
    return zidz(
        households_taxes_on_assets_to_finance_basic_income(),
        households_financial_assets(),
    )


@component.add(
    name="increase in households capital stock due to investments",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "gross_fixed_capital_formation_real": 2,
        "households_financial_assets": 4,
        "mdollars_per_mdollars_2015": 2,
        "price_gfcf": 2,
        "base_number_of_households": 3,
        "unit_conversion_dollars_mdollars": 2,
        "price_transformation": 2,
        "number_of_households_by_income_and_type": 3,
    },
)
def increase_in_households_capital_stock_due_to_investments():
    """
    Household investments to increase their capital stock, mainly housing. The initial values are used to maintain certain ratios throughout the simulation.
    """
    return if_then_else(
        time() < 2015,
        lambda: zidz(
            gross_fixed_capital_formation_real()
            .loc[:, "REAL ESTATE"]
            .reset_coords(drop=True)
            * price_gfcf().loc[:, "REAL ESTATE"].reset_coords(drop=True)
            / price_transformation()
            * mdollars_per_mdollars_2015()
            * unit_conversion_dollars_mdollars()
            * zidz(
                households_financial_assets() * base_number_of_households(),
                sum(
                    households_financial_assets().rename(
                        {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                    )
                    * base_number_of_households().rename(
                        {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                    ),
                    dim=["HOUSEHOLDS I!"],
                ).expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1),
            ),
            base_number_of_households(),
        ),
        lambda: zidz(
            gross_fixed_capital_formation_real()
            .loc[:, "REAL ESTATE"]
            .reset_coords(drop=True)
            * price_gfcf().loc[:, "REAL ESTATE"].reset_coords(drop=True)
            / price_transformation()
            * mdollars_per_mdollars_2015()
            * unit_conversion_dollars_mdollars()
            * zidz(
                households_financial_assets()
                * number_of_households_by_income_and_type(),
                sum(
                    households_financial_assets().rename(
                        {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                    )
                    * number_of_households_by_income_and_type().rename(
                        {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                    ),
                    dim=["HOUSEHOLDS I!"],
                ).expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1),
            ),
            number_of_households_by_income_and_type(),
        ),
    )


@component.add(
    name="INITIAL HOUSEHOLD TAXES ON ASSETS TO FINANCE BASIC INCOME",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={
        "_initial_initial_household_taxes_on_assets_to_finance_basic_income": 1
    },
    other_deps={
        "_initial_initial_household_taxes_on_assets_to_finance_basic_income": {
            "initial": {"households_taxes_on_assets_to_finance_basic_income": 1},
            "step": {},
        }
    },
)
def initial_household_taxes_on_assets_to_finance_basic_income():
    """
    This variable is the initial value of the variable contained in it, to generate a variable to modularize.
    """
    return _initial_initial_household_taxes_on_assets_to_finance_basic_income()


_initial_initial_household_taxes_on_assets_to_finance_basic_income = Initial(
    lambda: households_taxes_on_assets_to_finance_basic_income(),
    "_initial_initial_household_taxes_on_assets_to_finance_basic_income",
)


@component.add(
    name="INITIAL HOUSEHOLDS NET WEALTH",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_net_wealth": 1},
    other_deps={
        "_initial_initial_households_net_wealth": {
            "initial": {"households_net_wealth": 1},
            "step": {},
        }
    },
)
def initial_households_net_wealth():
    """
    Initial households net wealth
    """
    return _initial_initial_households_net_wealth()


_initial_initial_households_net_wealth = Initial(
    lambda: households_net_wealth(), "_initial_initial_households_net_wealth"
)


@component.add(
    name="interest rate for households assets",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "debt_interest_rate": 1,
        "mark_up_for_households_assets": 1,
        "minimum_households_interest_rate": 1,
    },
)
def interest_rate_for_households_assets():
    """
    Interest rate for households assets.
    """
    return np.maximum(
        debt_interest_rate() + mark_up_for_households_assets(),
        minimum_households_interest_rate(),
    )


@component.add(
    name="interest rate for households liabilities",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "debt_interest_rate": 1,
        "mark_up_for_households_liabilities": 1,
        "minimum_households_interest_rate": 1,
    },
)
def interest_rate_for_households_liabilities():
    """
    Interest rate for households liabilities.
    """
    return np.maximum(
        debt_interest_rate() + mark_up_for_households_liabilities(),
        minimum_households_interest_rate(),
    )


@component.add(
    name="mark up for households assets",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_assets_interest_rate": 1,
        "debt_interest_rate_default": 1,
    },
)
def mark_up_for_households_assets():
    """
    Increase in the interest rate on household assets with respect to the base interest rate.
    """
    return initial_households_assets_interest_rate() - debt_interest_rate_default()


@component.add(
    name="mark up for households liabilities",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_liabilities_interest_rate": 1,
        "debt_interest_rate_default": 1,
    },
)
def mark_up_for_households_liabilities():
    """
    Increase in the interest rate on household liabilities with respect to the base interest rate.
    """
    return initial_households_liabilities_interest_rate() - debt_interest_rate_default()


@component.add(
    name="ratio liabilties to disposable income",
    units="DMNL",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_households_financial_liabilities_per_household": 1,
        "initial_households_disposable_income": 1,
    },
)
def ratio_liabilties_to_disposable_income():
    """
    Ratio liabilities to disposable income
    """
    return zidz(
        initial_households_financial_liabilities_per_household(),
        initial_households_disposable_income(),
    )


@component.add(
    name="SELECT POLICY FINANCE BASIC INCOME SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_policy_finance_basic_income_sp"},
)
def select_policy_finance_basic_income_sp():
    """
    Select policy to finance basic income 0: New tax on wealth to finance basic income 1: New tax on operating surplus of corporations to finance basic income 2: New tax on wealth combined with a tax on CO2 to finance basic income
    """
    return _ext_constant_select_policy_finance_basic_income_sp()


_ext_constant_select_policy_finance_basic_income_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_POLICY_FINANCE_BASIC_INCOME_SP*",
    {},
    _root,
    {},
    "_ext_constant_select_policy_finance_basic_income_sp",
)


@component.add(
    name="share of total financial assets households paying taxes finance basic income",
    units="DMNL",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_financial_assets_by_houshold_group": 1,
        "aux_basic_income_tax_payers_sp": 1,
        "total_financial_assets_households_paying_taxes_finance_basic_income": 1,
    },
)
def share_of_total_financial_assets_households_paying_taxes_finance_basic_income():
    """
    Share of the total finacial assets in a country owned by each household
    """
    return zidz(
        total_financial_assets_by_houshold_group() * aux_basic_income_tax_payers_sp(),
        total_financial_assets_households_paying_taxes_finance_basic_income().expand_dims(
            {"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1
        ),
    )


@component.add(
    name="SWITCH FINANCE",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_finance"},
)
def switch_finance():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_finance()


_ext_constant_switch_finance = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_FINANCE",
    {},
    _root,
    {},
    "_ext_constant_switch_finance",
)


@component.add(
    name="taxes on assets to finance basic income",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_basic_income_sp": 1,
        "select_policy_finance_basic_income_sp": 2,
        "ghg_tax_revenues_used_to_finance_basic_income": 1,
        "government_basic_income_expenditure": 2,
    },
)
def taxes_on_assets_to_finance_basic_income():
    """
    Taxes on financial assets to fiance basic income
    """
    return if_then_else(
        switch_policy_basic_income_sp() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: if_then_else(
            select_policy_finance_basic_income_sp() == 0,
            lambda: government_basic_income_expenditure(),
            lambda: if_then_else(
                select_policy_finance_basic_income_sp() == 2,
                lambda: government_basic_income_expenditure()
                - ghg_tax_revenues_used_to_finance_basic_income(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
        ),
    )


@component.add(
    name="taxes on assets to finance basic income by household group",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_policy_finance_basic_income_sp": 2,
        "share_of_total_financial_assets_households_paying_taxes_finance_basic_income": 1,
        "taxes_on_assets_to_finance_basic_income": 1,
    },
)
def taxes_on_assets_to_finance_basic_income_by_household_group():
    """
    Taxes on financial assets to finance basic income paid by each household group
    """
    return if_then_else(
        np.logical_or(
            select_policy_finance_basic_income_sp() == 0,
            select_policy_finance_basic_income_sp() == 2,
        ),
        lambda: taxes_on_assets_to_finance_basic_income()
        * share_of_total_financial_assets_households_paying_taxes_finance_basic_income(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
    )


@component.add(
    name="total financial assets by houshold group",
    units="Mdollars",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_financial_assets": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def total_financial_assets_by_houshold_group():
    """
    Total finacial assets by type of household
    """
    return (
        households_financial_assets()
        * number_of_households_by_income_and_type()
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="total financial assets households paying taxes finance basic income",
    units="Mdollars",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_financial_assets_by_houshold_group": 1,
        "aux_basic_income_tax_payers_sp": 1,
    },
)
def total_financial_assets_households_paying_taxes_finance_basic_income():
    """
    Total finacial assets
    """
    return sum(
        total_financial_assets_by_houshold_group().rename(
            {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
        )
        * aux_basic_income_tax_payers_sp().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="variation in households capital stock due to revalorizations",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_finance": 1,
        "delayed_ts_price_gfcf": 1,
        "households_capital_stock": 1,
        "price_gfcf": 1,
    },
)
def variation_in_households_capital_stock_due_to_revalorizations():
    """
    Variation in households capital stock due to revalorizations.
    """
    return if_then_else(
        switch_finance() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: np.minimum(
            zidz(
                price_gfcf().loc[:, "REAL ESTATE"].reset_coords(drop=True),
                delayed_ts_price_gfcf().loc[:, "REAL ESTATE"].reset_coords(drop=True),
            )
            - 1,
            0.05,
        )
        * households_capital_stock(),
    )


@component.add(
    name="variation in households financial assets due to net lending",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_net_lending": 3,
        "variation_in_households_financial_liabilities": 3,
        "households_financial_assets": 1,
    },
)
def variation_in_households_financial_assets_due_to_net_lending():
    """
    Variation in households financial assets due to net lending IF_THEN_ELSE(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I]<0 :AND: ABS(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I])>households_financial _assets[REGIONS_35_I,HOUSEHOLDS_I],-households_financial_assets[REGIONS_35_ I,HOUSEHOLDS_I],households_net_lending[REGIONS_35_I,HOUSEHOLDS_I])
    """
    return if_then_else(
        np.logical_and(
            households_net_lending() + variation_in_households_financial_liabilities()
            < 0,
            np.abs(
                households_net_lending()
                + variation_in_households_financial_liabilities()
            )
            > households_financial_assets(),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: households_net_lending()
        + variation_in_households_financial_liabilities(),
    )


@component.add(
    name="variation in households financial liabilities",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "households_financial_liabilities": 3,
        "households_financial_assets": 1,
        "households_net_lending": 3,
        "ratio_liabilties_to_disposable_income": 3,
        "delayed_ts_households_disposable_income": 3,
    },
)
def variation_in_households_financial_liabilities():
    """
    Variation in households financial liabilities. IF_THEN_ELSE(Time < 2015, 0, IF_THEN_ELSE(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I]< 0 :AND: ABS(households_net_lending[REGIONS_35_I,HOUSEHOLDS_I ])>households_financial_assets[REGIONS_35_I,HOUSEHOLDS_I],-households_net_lending[REG IONS_35_I,HOUSEHOLDS_I], ratio_liabilities_to_assets[REGIONS_35_I,HOUSEHOLDS_I]*(households_capital_stock[REGI ONS_35_I ,HOUSEHOLDS_I]+households_financial_assets[REGIONS_35_I,HOUSEHOLDS_I])-households_fin ancial_liabilities[REGIONS_35_I,HOUSEHOLDS_I ]) )
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            ["REGIONS 35 I", "HOUSEHOLDS I"],
        ),
        lambda: if_then_else(
            np.logical_and(
                households_net_lending()
                + ratio_liabilties_to_disposable_income()
                * delayed_ts_households_disposable_income()
                - households_financial_liabilities()
                < 0,
                np.abs(
                    households_net_lending()
                    + ratio_liabilties_to_disposable_income()
                    * delayed_ts_households_disposable_income()
                    - households_financial_liabilities()
                )
                > households_financial_assets(),
            ),
            lambda: -households_net_lending(),
            lambda: ratio_liabilties_to_disposable_income()
            * delayed_ts_households_disposable_income()
            - households_financial_liabilities(),
        ),
    )
