"""
Module damage_functions.general
Translated using PySD version 3.14.0
"""

@component.add(
    name='"DEFINE: TOT: EQ DEFINE total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "define_46_eq_damage_function": 1,
        "gross_domestic_product_nominal": 1,
        "extra_extra_gdp_modifyer": 1,
    },
)
def define_tot_eq_define_total_impact():
    return (
        define_46_eq_damage_function()
        * gross_domestic_product_nominal()
        * extra_extra_gdp_modifyer()
    )


@component.add(
    name='"DICE: TOT: EQ DICE total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "dice_5_eq_damage_function": 1,
        "extra_extra_gdp_modifyer": 1,
    },
)
def dice_tot_eq_dice_total_impact():
    return (
        gross_domestic_product_nominal()
        * dice_5_eq_damage_function()
        * extra_extra_gdp_modifyer()
    )


@component.add(
    name='"DSK: TOT: EQ DSK total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dsk_a128_eq_shock_from_climate_change": 1,
        "gross_domestic_product_nominal": 1,
        "extra_extra_gdp_modifyer": 1,
    },
)
def dsk_tot_eq_dsk_total_impact():
    return (
        dsk_a128_eq_shock_from_climate_change()
        * gross_domestic_product_nominal()
        * extra_extra_gdp_modifyer()
    )


@component.add(
    name='"EXTRA: EXTRA: exponent"', comp_type="Constant", comp_subtype="Normal"
)
def extra_extra_exponent():
    """
    Same as in FUND
    """
    return 1


@component.add(
    name='"EXTRA: EXTRA: GDP modifyer"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "average_disposable_income_per_capita": 1,
        "extra_extra_normalisation_constant": 1,
        "extra_extra_exponent": 1,
    },
)
def extra_extra_gdp_modifyer():
    return (
        average_disposable_income_per_capita() / extra_extra_normalisation_constant()
    ) ** extra_extra_exponent()


@component.add(
    name='"EXTRA: EXTRA: normalisation constant"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def extra_extra_normalisation_constant():
    """
    Same as in FUND
    """
    return 25000


@component.add(
    name='"FUND: EXTRA: EQ SWITCH deaths"', comp_type="Constant", comp_subtype="Normal"
)
def fund_extra_eq_switch_deaths():
    return 0


@component.add(
    name='"FUND: TOT: EQ: fund total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_tot_eq_monetary_impact": 1,
        "fund_extra_eq_switch_deaths": 1,
        "fund_tot_eq_total_deaths": 1,
        "fund_mm1_eq_value_of_a_statistical_life": 1,
    },
)
def fund_tot_eq_fund_total_impact():
    return (
        fund_tot_eq_monetary_impact()
        + fund_mm1_eq_value_of_a_statistical_life()
        * fund_tot_eq_total_deaths()
        * fund_extra_eq_switch_deaths()
    )


@component.add(
    name='"FUND: TOT: EQ monetary impact"',
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
def fund_tot_eq_monetary_impact():
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


@component.add(
    name='"WITNESS: TOT: EQ WITNESS total impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "witness_dicelike_damage_eq_dicelike_damage": 1,
        "witness_tipping_point_damage_eq_tipping_point_damge": 1,
        "gross_domestic_product_nominal": 1,
        "extra_extra_gdp_modifyer": 1,
    },
)
def witness_tot_eq_witness_total_impact():
    return (
        (
            witness_dicelike_damage_eq_dicelike_damage()
            + witness_tipping_point_damage_eq_tipping_point_damge()
        )
        * gross_domestic_product_nominal()
        * extra_extra_gdp_modifyer()
    )
