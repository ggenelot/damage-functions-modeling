"""
Module energycapacities_protra.lcoe
Translated using PySD version 3.14.0
"""

@component.add(
    name="LCOE by PROTRA priority signal",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1, "min_lcoe": 1, "max_lcoe": 1},
)
def lcoe_by_protra_priority_signal():
    """
    approximation of levelized cost of electricity, NOT taking into account capital cost, discount rate etc.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    )
    value.loc[:, _subscript_dict["PROTRA PP CHP HP I"]] = (
        1
        - zidz(
            lcoe_protra() - min_lcoe(),
            max_lcoe().expand_dims(
                {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]}, 1
            ),
        )
    ).values
    value.loc[:, _subscript_dict["PROTRA NP I"]] = 1
    return value


@component.add(
    name="LCOE PROTRA",
    units="$/MWh",
    subscripts=["REGIONS 9 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynamic_capacity_investment_cost_protra_development_36r": 1,
        "unit_conversion_dollars_mdollars": 1,
        "protra_max_full_load_hours_after_constraints": 2,
        "protra_lifetime": 2,
        "opex_in_usd_per_mwh": 1,
    },
)
def lcoe_protra():
    """
    Levelized cost of electricity for transformation processes (technologies). A minimum for 'protra_max_full_load_hours_after_constraints' of 1h is set ad hoc to avoid potential issues dividing by 0 when curtailement is 100%.
    """
    return (
        dynamic_capacity_investment_cost_protra_development_36r()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * unit_conversion_dollars_mdollars()
        + opex_in_usd_per_mwh()
        .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
        .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"})
        * np.maximum(
            protra_max_full_load_hours_after_constraints()
            .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
            .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"}),
            1,
        )
        * protra_lifetime()
        .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
        .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"})
    ) / (
        np.maximum(
            protra_max_full_load_hours_after_constraints()
            .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
            .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"}),
            1,
        )
        * protra_lifetime()
        .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
        .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"})
    )


@component.add(
    name="max LCOE",
    units="$/MWh",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1},
)
def max_lcoe():
    return vmax(
        lcoe_protra().rename({"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}),
        dim=["PROTRA PP CHP HP I!"],
    )


@component.add(
    name="min LCOE",
    units="$/MWh",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lcoe_protra": 1},
)
def min_lcoe():
    return vmin(
        lcoe_protra().rename({"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}),
        dim=["PROTRA PP CHP HP I!"],
    )


@component.add(
    name="OPEX in USD per MWh",
    units="$/MWh",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "opex_by_protra_and_region": 1,
        "unit_conversion_dollars_mdollars": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_wh_mwh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def opex_in_usd_per_mwh():
    """
    OPEX_by_PROTRA_and_region[REGIONS 9 I,NRG PROTRA I]*0.0036
    """
    return (
        opex_by_protra_and_region()
        * unit_conversion_dollars_mdollars()
        * unit_conversion_j_wh()
        * unit_conversion_wh_mwh()
        / unit_conversion_j_ej()
    )
