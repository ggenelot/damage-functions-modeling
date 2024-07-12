"""
Module financeexogenous_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="INITIAL HOUSEHOLDS ASSETS INTEREST RATE",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_assets_interest_rate"
    },
)
def initial_households_assets_interest_rate():
    """
    Households liabilities interest rate in 2015.
    """
    return _ext_constant_initial_households_assets_interest_rate()


_ext_constant_initial_households_assets_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "assets_yield",
    "HOUSEHOLDS_ASSETS_YIELD",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_assets_interest_rate",
)


@component.add(
    name="INITIAL HOUSEHOLDS CAPITAL STOCK",
    units="dollars",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_households_capital_stock"},
)
def initial_households_capital_stock():
    """
    Initial households capital stock.
    """
    return _ext_constant_initial_households_capital_stock()


_ext_constant_initial_households_capital_stock = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "non_financial_assets",
    "INITIAL_HOUSEHOLDS_CAPITAL_STOCK_MP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_capital_stock",
)


@component.add(
    name="INITIAL HOUSEHOLDS FINANCIAL ASSETS",
    units="$",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_households_financial_assets"},
)
def initial_households_financial_assets():
    """
    Initial total households financial assets.
    """
    return _ext_constant_initial_households_financial_assets()


_ext_constant_initial_households_financial_assets = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "financial_assets",
    "IMV_BASE_HOUSEHOLD_ASSETS",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_financial_assets",
)


@component.add(
    name="INITIAL HOUSEHOLDS FINANCIAL LIABILITIES",
    units="dollars",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_financial_liabilities"
    },
)
def initial_households_financial_liabilities():
    """
    Initial total households financial liabilities.
    """
    return _ext_constant_initial_households_financial_liabilities()


_ext_constant_initial_households_financial_liabilities = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "financial_liabilities",
    "IMV_BASE_HOUSEHOLDS_LIABILITIES",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_financial_liabilities",
)


@component.add(
    name="INITIAL HOUSEHOLDS LIABILITIES INTEREST RATE",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_liabilities_interest_rate"
    },
)
def initial_households_liabilities_interest_rate():
    """
    Households liabilities interest rate in 2015.
    """
    return _ext_constant_initial_households_liabilities_interest_rate()


_ext_constant_initial_households_liabilities_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "liabilities_yield",
    "HOUSEHOLDS_LIABILITIES_YIELD",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_liabilities_interest_rate",
)


@component.add(
    name="MINIMUM HOUSEHOLDS INTEREST RATE",
    units="DMNL/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_households_interest_rate"},
)
def minimum_households_interest_rate():
    """
    Minimum interest ratio that households will have on both their assets and their liabilities.
    """
    return _ext_constant_minimum_households_interest_rate()


_ext_constant_minimum_households_interest_rate = ExtConstant(
    "model_parameters/finance/finance.xlsx",
    "ratios",
    "MINIMUM_HOUSEHOLDS_INTEREST_RATE_MP",
    {},
    _root,
    {},
    "_ext_constant_minimum_households_interest_rate",
)
