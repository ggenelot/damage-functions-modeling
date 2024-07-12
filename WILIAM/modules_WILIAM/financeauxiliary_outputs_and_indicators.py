"""
Module financeauxiliary_outputs_and_indicators
Translated using PySD version 3.13.4
"""

@component.add(
    name="INITIAL HOUSEHOLDS CAPITAL STOCK PER HOUSEHOLD",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_capital_stock_per_household": 1},
    other_deps={
        "_initial_initial_households_capital_stock_per_household": {
            "initial": {"households_capital_stock": 1},
            "step": {},
        }
    },
)
def initial_households_capital_stock_per_household():
    """
    Initial households capital stock by household type.
    """
    return _initial_initial_households_capital_stock_per_household()


_initial_initial_households_capital_stock_per_household = Initial(
    lambda: households_capital_stock(),
    "_initial_initial_households_capital_stock_per_household",
)


@component.add(
    name="INITIAL HOUSEHOLDS FINANCIAL ASSETS PER HOUSEHOLD",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_financial_assets_per_household": 1},
    other_deps={
        "_initial_initial_households_financial_assets_per_household": {
            "initial": {"households_financial_assets": 1},
            "step": {},
        }
    },
)
def initial_households_financial_assets_per_household():
    """
    Initial households financial assets by household type.
    """
    return _initial_initial_households_financial_assets_per_household()


_initial_initial_households_financial_assets_per_household = Initial(
    lambda: households_financial_assets(),
    "_initial_initial_households_financial_assets_per_household",
)


@component.add(
    name="INITIAL HOUSEHOLDS FINANCIAL LIABILITIES PER HOUSEHOLD",
    units="dollars/households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_households_financial_liabilities_per_household": 1},
    other_deps={
        "_initial_initial_households_financial_liabilities_per_household": {
            "initial": {"households_financial_liabilities": 1},
            "step": {},
        }
    },
)
def initial_households_financial_liabilities_per_household():
    """
    Initial households financial liabiliies by household type.
    """
    return _initial_initial_households_financial_liabilities_per_household()


_initial_initial_households_financial_liabilities_per_household = Initial(
    lambda: households_financial_liabilities(),
    "_initial_initial_households_financial_liabilities_per_household",
)


@component.add(
    name="INITIAL HOUSEHOLDS PROPERTY INCOME PAID",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_households_property_income_paid"
    },
)
def initial_households_property_income_paid():
    """
    Initial households property income paid by household type.
    """
    return _ext_constant_initial_households_property_income_paid()


_ext_constant_initial_households_property_income_paid = ExtConstant(
    "model_parameters/economy/Consumption.xlsx",
    "HH_Property_income_paid",
    "INITIAL_HOUSEHOLDS_PROPERTY_INCOME_PAID",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_households_property_income_paid",
)
