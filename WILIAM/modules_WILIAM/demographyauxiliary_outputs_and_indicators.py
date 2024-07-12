"""
Module demographyauxiliary_outputs_and_indicators
Translated using PySD version 3.13.4
"""

@component.add(
    name="annual population growth rate",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 1, "delayed_population_35r": 1, "one_year": 1},
)
def annual_population_growth_rate():
    """
    Annual regional population growth rate.
    """
    return (-1 + zidz(population_35_regions(), delayed_population_35r())) / one_year()


@component.add(
    name="delayed population 35R",
    units="person",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_population_35r": 1},
    other_deps={
        "_delayfixed_delayed_population_35r": {
            "initial": {"population_35_regions": 1},
            "step": {"population_35_regions": 1},
        }
    },
)
def delayed_population_35r():
    """
    Population by region delayed 1 year.
    """
    return _delayfixed_delayed_population_35r()


_delayfixed_delayed_population_35r = DelayFixed(
    lambda: population_35_regions(),
    lambda: 1,
    lambda: population_35_regions(),
    time_step,
    "_delayfixed_delayed_population_35r",
)


@component.add(
    name="total population",
    units="person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 1},
)
def total_population():
    """
    Total world population.
    """
    return sum(
        population_35_regions().rename({"REGIONS 35 I": "REGIONS 35 I!"}),
        dim=["REGIONS 35 I!"],
    )
