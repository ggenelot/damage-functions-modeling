"""
Module damage_functions.general
Translated using PySD version 3.14.0
"""

@component.add(
    name='"FUND: TOT: EQ: fund total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_tot_eq_moneraty_impact": 1,
        "fund_mm1_eq_value_of_a_statistical_life": 1,
        "fund_tot_eq_total_deaths": 1,
    },
)
def fund_tot_eq_fund_total_impact():
    return (
        fund_tot_eq_moneraty_impact()
        + fund_mm1_eq_value_of_a_statistical_life() * fund_tot_eq_total_deaths()
    )


@component.add(
    name='"FUND: TOT: EQ moneraty impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_e1_eq_space_heating": 1,
        "fund_e1_eq_value_of_the_loss_of_the_ecosystems": 1,
        "fund_e2_eq_space_cooling": 1,
        "fund_ets1_eq_extratropical_storms": 1,
        "fund_f1_eq_forestry_change_in_consumer_and_producer_surplus": 1,
        "fund_ts1_eq_tropical_storms_damages": 1,
        "fund_w1_eq_change_in_water_resources": 1,
    },
)
def fund_tot_eq_moneraty_impact():
    return (
        fund_e1_eq_space_heating()
        + fund_e1_eq_value_of_the_loss_of_the_ecosystems()
        + fund_e2_eq_space_cooling()
        + fund_ets1_eq_extratropical_storms()
        + fund_f1_eq_forestry_change_in_consumer_and_producer_surplus()
        + fund_ts1_eq_tropical_storms_damages()
        + fund_w1_eq_change_in_water_resources()
    )


@component.add(
    name='"FUND: TOT: EQ total deaths"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_ets2_eq_mortality_from_extratropical_storm": 1,
        "fund_hd1_eq_additional_diarrhoea_deaths": 1,
        "fund_hv_eq_vectorborn_diseases": 1,
        "fund_ts2_eq_tropical_storms_mortality": 1,
    },
)
def fund_tot_eq_total_deaths():
    return (
        fund_ets2_eq_mortality_from_extratropical_storm()
        + fund_hd1_eq_additional_diarrhoea_deaths()
        + fund_hv_eq_vectorborn_diseases()
        + fund_ts2_eq_tropical_storms_mortality()
    )
