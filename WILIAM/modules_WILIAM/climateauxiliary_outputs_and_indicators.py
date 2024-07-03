"""
Module climateauxiliary_outputs_and_indicators
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual variation CO2 emissions",
    units="Gt/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emissions": 2, "delayed_total_co2_emissions": 4},
)
def annual_variation_co2_emissions():
    """
    Annual variation of the CO2 emissions. Europe has the same variation in all the countries to account for the same effect
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        (
            total_co2_emissions()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            - delayed_total_co2_emissions()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
        )
        / delayed_total_co2_emissions()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        * 100
    ).values
    value.loc[_subscript_dict["REGIONS EU27 I"]] = (
        (
            float(total_co2_emissions().loc["EU27"])
            - float(delayed_total_co2_emissions().loc["EU27"])
        )
        / float(delayed_total_co2_emissions().loc["EU27"])
        * 100
    )
    return value


@component.add(
    name="delayed total CO2 emissions",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_total_co2_emissions": 1},
    other_deps={
        "_delay_delayed_total_co2_emissions": {
            "initial": {"total_co2_emissions": 1},
            "step": {"total_co2_emissions": 1},
        }
    },
)
def delayed_total_co2_emissions():
    """
    Delayed one year the total carbon emissions
    """
    return _delay_delayed_total_co2_emissions()


_delay_delayed_total_co2_emissions = Delay(
    lambda: total_co2_emissions(),
    lambda: xr.DataArray(
        1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    lambda: total_co2_emissions(),
    lambda: 1,
    time_step,
    "_delay_delayed_total_co2_emissions",
)
