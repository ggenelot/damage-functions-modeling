"""
Module societyauxiliary_outputs_and_indicators
Translated using PySD version 3.13.4
"""

@component.add(
    name="annual variation regional average schooling time",
    units="percent",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "regional_average_schooling_time": 1,
        "delayed_regional_average_schooling_time": 2,
    },
)
def annual_variation_regional_average_schooling_time():
    """
    Percentage in the variation of the regional average schooling time
    """
    return (
        (regional_average_schooling_time() - delayed_regional_average_schooling_time())
        / delayed_regional_average_schooling_time()
        * 100
    )


@component.add(
    name="delayed regional average schooling time",
    units="Year",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={"_delay_delayed_regional_average_schooling_time": 1},
    other_deps={
        "_delay_delayed_regional_average_schooling_time": {
            "initial": {"regional_average_schooling_time": 1},
            "step": {"regional_average_schooling_time": 1},
        }
    },
)
def delayed_regional_average_schooling_time():
    """
    Delay of one year in the regional average schooling time
    """
    return _delay_delayed_regional_average_schooling_time()


_delay_delayed_regional_average_schooling_time = Delay(
    lambda: regional_average_schooling_time(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SEX I": _subscript_dict["SEX I"],
        },
        ["REGIONS 35 I", "SEX I"],
    ),
    lambda: regional_average_schooling_time(),
    lambda: 1,
    time_step,
    "_delay_delayed_regional_average_schooling_time",
)
