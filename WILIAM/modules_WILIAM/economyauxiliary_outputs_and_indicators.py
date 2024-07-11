"""
Module economyauxiliary_outputs_and_indicators
Translated using PySD version 3.13.4
"""

@component.add(
    name="annual variation government expenditure",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_expenditure_by_cofog": 1,
        "delayed_government_expenditure_by_cofog": 2,
    },
)
def annual_variation_government_expenditure():
    """
    Percent of the annual variation in the government expenditure
    """
    return (
        (government_expenditure_by_cofog() - delayed_government_expenditure_by_cofog())
        / delayed_government_expenditure_by_cofog()
        * 100
    )


@component.add(
    name="aux GDP real 35R until 2019",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_gdp_real_35r_until_2019": 1},
    other_deps={
        "_delayfixed_aux_gdp_real_35r_until_2019": {
            "initial": {"time_step": 1},
            "step": {"gdp_real_35r_until_2019": 1},
        }
    },
)
def aux_gdp_real_35r_until_2019():
    return _delayfixed_aux_gdp_real_35r_until_2019()


_delayfixed_aux_gdp_real_35r_until_2019 = DelayFixed(
    lambda: gdp_real_35r_until_2019(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_aux_gdp_real_35r_until_2019",
)


@component.add(
    name="delayed government expenditure by COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_government_expenditure_by_cofog": 1},
    other_deps={
        "_delay_delayed_government_expenditure_by_cofog": {
            "initial": {"government_expenditure_by_cofog": 1},
            "step": {"government_expenditure_by_cofog": 1},
        }
    },
)
def delayed_government_expenditure_by_cofog():
    """
    Delay of one year to calculate the difference
    """
    return _delay_delayed_government_expenditure_by_cofog()


_delay_delayed_government_expenditure_by_cofog = Delay(
    lambda: government_expenditure_by_cofog(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COFOG I": _subscript_dict["COFOG I"],
        },
        ["REGIONS 35 I", "COFOG I"],
    ),
    lambda: government_expenditure_by_cofog(),
    lambda: 1,
    time_step,
    "_delay_delayed_government_expenditure_by_cofog",
)


@component.add(
    name="GDP real 35R until 2019",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "aux_gdp_real_35r_until_2019": 1,
        "gross_domestic_product_real_demand_side": 1,
    },
)
def gdp_real_35r_until_2019():
    return if_then_else(
        time() > 2019,
        lambda: aux_gdp_real_35r_until_2019(),
        lambda: gross_domestic_product_real_demand_side(),
    )


@component.add(
    name="government expenditure by COFOG",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "COFOG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_consumption_by_cofog": 1,
        "government_investment_by_cofog": 1,
    },
)
def government_expenditure_by_cofog():
    """
    Government expenditure by category (COFOG classification: Classification of the Functions of the Government).
    """
    return government_consumption_by_cofog() + government_investment_by_cofog()


@component.add(
    name="INITIAL GROSS SAVINGS",
    units="dollars/(Year*households)",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_gross_savings": 1},
    other_deps={
        "_initial_initial_gross_savings": {
            "initial": {"households_gross_savings": 1},
            "step": {},
        }
    },
)
def initial_gross_savings():
    return _initial_initial_gross_savings()


_initial_initial_gross_savings = Initial(
    lambda: households_gross_savings(), "_initial_initial_gross_savings"
)
