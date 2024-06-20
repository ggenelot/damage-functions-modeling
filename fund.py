"""
Module damage_functions.fund
Translated using PySD version 3.14.0
"""

@component.add(
    name='"FUND: A.2: agricultural impact of the rate of climate change"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_a2_alpha_parameter": 1,
        "fund_a2_beta_parameter": 1,
        "fund_a2_rate_of_temperature_change": 1,
        "fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change": 1,
        "fund_a2_rho_parameter": 1,
    },
)
def fund_a2_agricultural_impact_of_the_rate_of_climate_change():
    return (
        fund_a2_alpha_parameter()
        * (fund_a2_rate_of_temperature_change() / 0.04) ** fund_a2_beta_parameter()
        + (1 - 1 / fund_a2_rho_parameter())
        * fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change()
    )


@component.add(
    name='"FUND: A.2: alpha parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_a2_alpha_parameter"},
)
def fund_a2_alpha_parameter():
    return _ext_constant_fund_a2_alpha_parameter()


_ext_constant_fund_a2_alpha_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_a.xlsx",
    "Sheet1",
    "B2",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_a2_alpha_parameter",
)


@component.add(
    name='"FUND: A.2: beta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_a2_beta_parameter():
    return 2


@component.add(
    name='"FUND: A.2: DELAYED agricultural impact of the rate of climate change"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change": 1
    },
    other_deps={
        "_delayfixed_fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change": {
            "initial": {},
            "step": {"fund_a2_agricultural_impact_of_the_rate_of_climate_change": 1},
        }
    },
)
def fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change():
    return (
        _delayfixed_fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change()
    )


_delayfixed_fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change = (
    DelayFixed(
        lambda: fund_a2_agricultural_impact_of_the_rate_of_climate_change(),
        lambda: 1,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        time_step,
        "_delayfixed_fund_a2_delayed_agricultural_impact_of_the_rate_of_climate_change",
    )
)


@component.add(
    name='"FUND: A.2: rate of temperature change"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "temperature_change_in_35regions": 1,
        "fund_a2_temperature_change_delayed": 1,
    },
)
def fund_a2_rate_of_temperature_change():
    return temperature_change_in_35regions() - fund_a2_temperature_change_delayed()


@component.add(
    name='"FUND: A.2: rho parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_a2_rho_parameter():
    return 10


@component.add(
    name='"FUND: A.2: temperature change delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_a2_temperature_change_delayed": 1},
    other_deps={
        "_delayfixed_fund_a2_temperature_change_delayed": {
            "initial": {},
            "step": {"temperature_change_in_35regions": 1},
        }
    },
)
def fund_a2_temperature_change_delayed():
    return _delayfixed_fund_a2_temperature_change_delayed()


_delayfixed_fund_a2_temperature_change_delayed = DelayFixed(
    lambda: temperature_change_in_35regions(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_a2_temperature_change_delayed",
)


@component.add(
    name='"FUND: A.3: agricultural impact of the level of climate change"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_a3_delta_l_parameter": 1,
        "temperature_change_in_35regions": 3,
        "fund_a4_delta_q_parameter": 1,
    },
)
def fund_a3_agricultural_impact_of_the_level_of_climate_change():
    return (
        fund_a3_delta_l_parameter() * temperature_change_in_35regions()
        + fund_a4_delta_q_parameter()
        * temperature_change_in_35regions()
        * temperature_change_in_35regions()
    )


@component.add(
    name='"FUND: A.3: delta l parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_a3_delta_l_parameter"},
)
def fund_a3_delta_l_parameter():
    return _ext_constant_fund_a3_delta_l_parameter()


_ext_constant_fund_a3_delta_l_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_a.xlsx",
    "Sheet1",
    "B3",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_a3_delta_l_parameter",
)


@component.add(
    name='"FUND: A.4: delta q parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_a4_delta_q_parameter"},
)
def fund_a4_delta_q_parameter():
    return _ext_constant_fund_a4_delta_q_parameter()


_ext_constant_fund_a4_delta_q_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_a.xlsx",
    "Sheet1",
    "B4",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_a4_delta_q_parameter",
)


@component.add(
    name='"FUND: A.4: gamma parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_a4_gamma_parameter"},
)
def fund_a4_gamma_parameter():
    return _ext_constant_fund_a4_gamma_parameter()


_ext_constant_fund_a4_gamma_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_a.xlsx",
    "Sheet1",
    "B5",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_a4_gamma_parameter",
)


@component.add(
    name='"FUND: agricultural imact of the fertilisation"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fund_a4_gamma_parameter": 1, "atmospheric_concentrations_co2": 1},
)
def fund_agricultural_imact_of_the_fertilisation():
    return (
        fund_a4_gamma_parameter()
        / np.log(2)
        * np.log(atmospheric_concentrations_co2() / 275)
    )


@component.add(
    name='"FUND: E.1: alpha parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_e1_alpha_parameter"},
)
def fund_e1_alpha_parameter():
    """
    α is a parameter (in dollar per degree Celsius), that specifies the benchmark impact; see Table EFW, column 6-7
    """
    return _ext_constant_fund_e1_alpha_parameter()


_ext_constant_fund_e1_alpha_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_efw.xlsx",
    "Sheet1",
    "B4",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_e1_alpha_parameter",
)


@component.add(
    name='"FUND: E.1: epsilon parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_e1_epsilon_parameter():
    """
    ϵϵ is a parameter; it is the income elasticity of space heating demand; ϵϵ = 0.8 (0.1,&gt;0,&lt;1);
    """
    return 0.8


@component.add(
    name='"FUND: E.1: Space heating"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_e1_alpha_parameter": 1,
        "fund_extra_initial_gdp": 1,
        "temperature_change_in_35regions": 1,
        "fund_extra_initial_revenue": 1,
        "fund_e1_epsilon_parameter": 1,
        "average_disposable_income_per_capita": 1,
        "fund_extra_initial_population": 1,
        "population_35_regions": 1,
        "fund_e2_autonomous_energy_efficiency_improvement": 1,
    },
)
def fund_e1_space_heating():
    """
    SH denotes the decrease in expenditure on space heating (in 1995 US dollar) at time tt in region rr
    """
    return (
        fund_e1_alpha_parameter()
        * fund_extra_initial_gdp()
        * (np.arctan(temperature_change_in_35regions()) / np.arctan(1))
        * (average_disposable_income_per_capita() / fund_extra_initial_revenue())
        ** fund_e1_epsilon_parameter()
        * (population_35_regions() / fund_extra_initial_population())
    ) / fund_e2_autonomous_energy_efficiency_improvement()


@component.add(
    name='"FUND: E.2: alpha parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_e2_alpha_parameter"},
)
def fund_e2_alpha_parameter():
    """
    α is a parameter (in dollar per degree Celsius), that specifies the benchmark impact; see Table EFW, column 6-7
    """
    return _ext_constant_fund_e2_alpha_parameter()


_ext_constant_fund_e2_alpha_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_efw.xlsx",
    "Sheet1",
    "B5",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_e2_alpha_parameter",
)


@component.add(
    name='"FUND: E.2: Autonomous Energy Efficiency Improvement"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_e2_autonomous_energy_efficiency_improvement():
    """
    TODO trouver comment coder cette variable
    """
    return 1


@component.add(
    name='"FUND: E.2: beta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_e2_beta_parameter():
    """
    ββ is a parameter; ββ = 1.5 (1.0-2.0);
    """
    return 1.5


@component.add(
    name='"FUND: E.2: Space cooling"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_e2_alpha_parameter": 1,
        "fund_extra_initial_gdp": 1,
        "fund_e2_beta_parameter": 1,
        "temperature_change_in_35regions": 1,
        "fund_extra_initial_revenue": 1,
        "fund_e1_epsilon_parameter": 1,
        "average_disposable_income_per_capita": 1,
        "fund_extra_initial_population": 1,
        "population_35_regions": 1,
        "fund_e2_autonomous_energy_efficiency_improvement": 1,
    },
)
def fund_e2_space_cooling():
    """
    SC denotes the increase in expenditure on space cooling (1995 US dollar) at time tt in region rr;
    """
    return (
        fund_e2_alpha_parameter()
        * fund_extra_initial_gdp()
        * (temperature_change_in_35regions() / 1) ** fund_e2_beta_parameter()
        * (average_disposable_income_per_capita() / fund_extra_initial_revenue())
        ** fund_e1_epsilon_parameter()
        * (population_35_regions() / fund_extra_initial_population())
    ) / fund_e2_autonomous_energy_efficiency_improvement()


@component.add(
    name='"FUND: extra: initial GDP"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_fund_extra_initial_gdp": 1},
    other_deps={
        "_initial_fund_extra_initial_gdp": {
            "initial": {"gross_domestic_product_nominal": 1},
            "step": {},
        }
    },
)
def fund_extra_initial_gdp():
    return _initial_fund_extra_initial_gdp()


_initial_fund_extra_initial_gdp = Initial(
    lambda: gross_domestic_product_nominal(), "_initial_fund_extra_initial_gdp"
)


@component.add(
    name='"FUND: extra: initial population"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_fund_extra_initial_population": 1},
    other_deps={
        "_initial_fund_extra_initial_population": {
            "initial": {"population_35_regions": 1},
            "step": {},
        }
    },
)
def fund_extra_initial_population():
    return _initial_fund_extra_initial_population()


_initial_fund_extra_initial_population = Initial(
    lambda: population_35_regions(), "_initial_fund_extra_initial_population"
)


@component.add(
    name='"FUND: extra: Initial revenue"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_fund_extra_initial_revenue": 1},
    other_deps={
        "_initial_fund_extra_initial_revenue": {
            "initial": {"average_disposable_income_per_capita": 1},
            "step": {},
        }
    },
)
def fund_extra_initial_revenue():
    return _initial_fund_extra_initial_revenue()


_initial_fund_extra_initial_revenue = Initial(
    lambda: average_disposable_income_per_capita(),
    "_initial_fund_extra_initial_revenue",
)


@component.add(
    name='"FUND: F.1: alpha parameter on global warming economic impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_fund_f1_alpha_parameter_on_global_warming_economic_impact"
    },
)
def fund_f1_alpha_parameter_on_global_warming_economic_impact():
    """
    α is a parameter, that measures the impact of climate change of a 1ºC global warming on economic welfare; see Table EFW;
    """
    return _ext_constant_fund_f1_alpha_parameter_on_global_warming_economic_impact()


_ext_constant_fund_f1_alpha_parameter_on_global_warming_economic_impact = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_efw.xlsx",
    "Sheet1",
    "B2",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_f1_alpha_parameter_on_global_warming_economic_impact",
)


@component.add(
    name='"FUND: F.1: beta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_f1_beta_parameter():
    """
    β = 1 (0.5-1.5) is a parameter; this is an expert guess;
    """
    return 1


@component.add(
    name='"FUND: F.1: epsilon parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_f1_epsilon_parameter():
    """
    ϵ = 0.31 (0.11-0.51) is a parameter, and equals the income elasticity for agriculture;
    """
    return 0.31


@component.add(
    name='"FUND: F.1: Forestry change in consumer and producer surplus"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_f1_alpha_parameter_on_global_warming_economic_impact": 1,
        "fund_f1_epsilon_parameter": 1,
        "fund_extra_initial_revenue": 1,
        "average_disposable_income_per_capita": 1,
        "temperature_change_in_35regions": 1,
        "fund_f1_beta_parameter": 1,
        "atmospheric_concentrations_co2": 1,
        "fund_f1_gamma_parameter": 1,
    },
)
def fund_f1_forestry_change_in_consumer_and_producer_surplus():
    """
    FF denotes the change in forestry consumer and producer surplus (as a share of total income);
    """
    return (
        fund_f1_alpha_parameter_on_global_warming_economic_impact()
        * (average_disposable_income_per_capita() / fund_extra_initial_revenue())
        ** fund_f1_epsilon_parameter()
        * (
            0.5 * (temperature_change_in_35regions() / 1) ** fund_f1_beta_parameter()
            + 0.5
            * fund_f1_gamma_parameter()
            * np.log(atmospheric_concentrations_co2() / 275)
        )
    )


@component.add(
    name='"FUND: F.1: gamma parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_f1_gamma_parameter():
    """
    γ = 0.44 (0.29-0.87) is a parameter; γγ is such that a doubling of the atmospheric concentration of carbon dioxide would lead to a change of forest value of 15% (10-30%); this parameter is taken from Gitay et al., (2001).
    """
    return 0.44


@component.add(
    name='"FUND: SLR.10: annual unit cost of coastal protection"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_fund_slr10_annual_unit_cost_of_coastal_protection"
    },
)
def fund_slr10_annual_unit_cost_of_coastal_protection():
    """
    πr​ is the annual unit cost of coastal protection (in million dollar per vertical metre) in region rr; note that is assumed to be constant over time;
    """
    return _ext_constant_fund_slr10_annual_unit_cost_of_coastal_protection()


_ext_constant_fund_slr10_annual_unit_cost_of_coastal_protection = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B9",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr10_annual_unit_cost_of_coastal_protection",
)


@component.add(
    name='"FUND: SLR.10: delta SLR"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sea_level_rise": 1, "fund_slr10_slr_delayed": 1},
)
def fund_slr10_delta_slr():
    return sea_level_rise() - fund_slr10_slr_delayed()


@component.add(
    name='"FUND: SLR.10: epsilon parameter"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr10_epsilon_parameter():
    """
    ϵ is a parameter, the income elasticity of dryland value; ϵ=1.0ϵ=1.0, with a standard deviation of 0.2
    """
    return 1


@component.add(
    name='"FUND: SLR.10: eta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr10_eta_parameter():
    """
    η is a parameter, the consumption elasticity of marginal utility; ηη = 1
    """
    return 1


@component.add(
    name='"FUND: SLR.10: growth rate of per capita income"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "average_disposable_income_per_capita": 1,
        "delayed_ts_average_disposable_income_per_capita": 1,
    },
)
def fund_slr10_growth_rate_of_per_capita_income():
    return (
        average_disposable_income_per_capita()
        - delayed_ts_average_disposable_income_per_capita()
    )


@component.add(
    name='"FUND: SLR.10: NPVVP"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr10_rho_parameter": 2,
        "fund_slr10_eta_parameter": 2,
        "fund_slr10_growth_rate_of_per_capita_income": 2,
        "fund_slr10_annual_unit_cost_of_coastal_protection": 1,
        "fund_slr10_delta_slr": 1,
    },
)
def fund_slr10_npvvp():
    """
    NPVVPNPVVP is the net present costs of coastal protection at time tt in region rr; NPVVP is calculated assuming annual costs to be constant. This is based on the following. Firstly, the coastal protection decision makers anticipate a linear sea level rise. Secondly, coastal protection entails large infrastructural works which last for decades. Thirdly, the considered costs are direct investments only, and technologies for coastal protection are mature. Throughout the analysis, a pure rate of time preference, ρρ, of 1% per year is used. The actual discount rate lies thus 1% above the growth rate of the economy, gg. The net present costs of protection PCPC equal
    """
    return (
        (
            1
            + fund_slr10_rho_parameter()
            + fund_slr10_eta_parameter() * fund_slr10_growth_rate_of_per_capita_income()
        )
        * fund_slr10_annual_unit_cost_of_coastal_protection()
        * fund_slr10_delta_slr()
        / (
            fund_slr10_rho_parameter()
            + fund_slr10_eta_parameter() * fund_slr10_growth_rate_of_per_capita_income()
        )
    )


@component.add(
    name='"FUND: SLR.10: rho parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr10_rho_parameter():
    """
    ρ is a parameter, the rate of pure time preference; ρρ = 0.03;
    """
    return 0.03


@component.add(
    name='"FUND: SLR.10: SLR delayed"',
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr10_slr_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr10_slr_delayed": {
            "initial": {"time_step": 1},
            "step": {"sea_level_rise": 1},
        }
    },
)
def fund_slr10_slr_delayed():
    return _delayfixed_fund_slr10_slr_delayed()


_delayfixed_fund_slr10_slr_delayed = DelayFixed(
    lambda: sea_level_rise(),
    lambda: time_step(),
    lambda: 0,
    time_step,
    "_delayfixed_fund_slr10_slr_delayed",
)


@component.add(
    name='"FUND: SLR.11: annual unit wetland loss due to coastal protection"',
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection"
    },
)
def fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection():
    """
    ωr​ is the annual unit wetland loss due to full coastal protection (in square kilometre per metre sea level rise) in region rr; note that is assumed to be constant over time;
    """
    return _ext_constant_fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection()


_ext_constant_fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection = (
    ExtConstant(
        "df_parameters/FUND/output/wiliam_table_slr.xlsx",
        "Sheet1",
        "B5",
        {},
        _root,
        {},
        "_ext_constant_fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection",
    )
)


@component.add(
    name='"FUND: SLR.11: beta paramater"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr11_beta_paramater():
    """
    β is a parameter, the income elasticity of wetland value; ββ = 1.16 (0.46,&gt;0); this value is taken from Brander et al. (2006);
    """
    return 1.16


@component.add(
    name='"FUND: SLR.11: delta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr11_delta_parameter():
    """
    δ is a parameter, the size elasticity of wetland value; δδ = -0.11 (0.05,&gt;-1,&lt;0); this value is taken from Brander et al. (2006);
    """
    return -0.11


@component.add(
    name='"FUND: SLR.11: gamma parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr11_gamma_parameter():
    """
    γ is a parameter, the population density elasticity of wetland value; γγ = 0.47 (0.12,&gt;0,&lt;1); this value is taken from Brander et al. (2006);
    """
    return 0.47


@component.add(
    name='"FUND: SLR.11: NPVVW"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr6_wetland_loss": 1,
        "fund_slr8_wetland_value": 1,
        "fund_slr10_eta_parameter": 2,
        "fund_slr10_growth_rate_of_per_capita_income": 3,
        "fund_slr10_rho_parameter": 2,
        "fund_slr11_beta_paramater": 1,
        "fund_slr11_delta_parameter": 1,
        "fund_slr11_gamma_parameter": 1,
        "fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection": 1,
        "annual_population_growth_rate": 1,
    },
)
def fund_slr11_npvvw():
    """
    NPVVW denotes the net present value of wetland loss. at time tt in region rr;
    """
    return (
        fund_slr6_wetland_loss()
        * fund_slr8_wetland_value()
        * (
            1
            + fund_slr10_rho_parameter()
            + fund_slr10_growth_rate_of_per_capita_income() * fund_slr10_eta_parameter()
        )
        / (
            fund_slr10_rho_parameter()
            + fund_slr10_growth_rate_of_per_capita_income() * fund_slr10_eta_parameter()
            - fund_slr11_beta_paramater()
            * fund_slr10_growth_rate_of_per_capita_income()
            - fund_slr11_gamma_parameter() * annual_population_growth_rate()
            - fund_slr11_delta_parameter()
            * fund_slr11_annual_unit_wetland_loss_due_to_coastal_protection()
        )
    )


@component.add(
    name='"FUND: SLR.11: SLR.11 delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr11_slr11_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr11_slr11_delayed": {
            "initial": {"time_step": 1},
            "step": {"fund_slr11_npvvw": 1},
        }
    },
)
def fund_slr11_slr11_delayed():
    return _delayfixed_fund_slr11_slr11_delayed()


_delayfixed_fund_slr11_slr11_delayed = DelayFixed(
    lambda: fund_slr11_npvvw(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr11_slr11_delayed",
)


@component.add(
    name='"FUND: SLR.12: income density growth rate"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr12_income_density_growth_rate():
    return 1


@component.add(
    name='"FUND: SLR.12: NPVVD"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr3_actual_dryland_loss": 1,
        "fund_slr5_dryland_value": 1,
        "fund_slr10_eta_parameter": 2,
        "fund_slr10_growth_rate_of_per_capita_income": 2,
        "fund_slr10_epsilon_parameter": 1,
        "fund_slr12_income_density_growth_rate": 1,
        "fund_slr10_rho_parameter": 1,
    },
)
def fund_slr12_npvvd():
    return (
        fund_slr3_actual_dryland_loss()
        * fund_slr5_dryland_value()
        * fund_slr10_eta_parameter()
        * fund_slr10_growth_rate_of_per_capita_income()
        / (
            fund_slr10_rho_parameter()
            + fund_slr10_eta_parameter() * fund_slr10_growth_rate_of_per_capita_income()
            - fund_slr10_epsilon_parameter() * fund_slr12_income_density_growth_rate()
        )
    )


@component.add(
    name='"FUND: SLR.12: SLR.12 delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr12_slr12_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr12_slr12_delayed": {
            "initial": {"time_step": 1},
            "step": {"fund_slr12_npvvd": 1},
        }
    },
)
def fund_slr12_slr12_delayed():
    return _delayfixed_fund_slr12_slr12_delayed()


_delayfixed_fund_slr12_slr12_delayed = DelayFixed(
    lambda: fund_slr12_npvvd(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr12_slr12_delayed",
)


@component.add(
    name='"FUND: SLR.1: delta parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr1_delta_parameter"},
)
def fund_slr1_delta_parameter():
    """
    δr​ is the dryland loss due to one metre sea level rise (in square kilometre per metre) in region rr;
    """
    return _ext_constant_fund_slr1_delta_parameter()


_ext_constant_fund_slr1_delta_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B2",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr1_delta_parameter",
)


@component.add(
    name='"FUND: SLR.1: gamma parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr1_gamma_parameter"},
)
def fund_slr1_gamma_parameter():
    """
    γr​ is a parameter, calibrated to a digital elevation model;
    """
    return _ext_constant_fund_slr1_gamma_parameter()


_ext_constant_fund_slr1_gamma_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B3",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr1_gamma_parameter",
)


@component.add(
    name='"FUND: SLR.1: SLR dryland loss"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr1_delta_parameter": 1,
        "sea_level_rise": 1,
        "fund_slr1_gamma_parameter": 1,
        "fund_slr1_zeta_parameter": 1,
    },
)
def fund_slr1_slr_dryland_loss():
    """
    CDt,r​ is the potential cumulative dryland lost at time tt in region rr that would occur without protection;
    """
    return np.minimum(
        fund_slr1_delta_parameter() * sea_level_rise() ** fund_slr1_gamma_parameter(),
        fund_slr1_zeta_parameter(),
    )


@component.add(
    name='"FUND: SLR.1: zeta parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr1_zeta_parameter"},
)
def fund_slr1_zeta_parameter():
    """
    is the maximum dryland loss in region rr, which is equal to the area in the year 2000.
    """
    return _ext_constant_fund_slr1_zeta_parameter()


_ext_constant_fund_slr1_zeta_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B4",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr1_zeta_parameter",
)


@component.add(
    name='"FUND: SLR.2: CD delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr2_cd_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr2_cd_delayed": {
            "initial": {},
            "step": {"fund_slr4_actual_cumulative_dryland_lost": 1},
        }
    },
)
def fund_slr2_cd_delayed():
    return _delayfixed_fund_slr2_cd_delayed()


_delayfixed_fund_slr2_cd_delayed = DelayFixed(
    lambda: fund_slr4_actual_cumulative_dryland_lost(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr2_cd_delayed",
)


@component.add(
    name='"FUND: SLR.2: Potential dryland loss"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fund_slr1_slr_dryland_loss": 1, "fund_slr2_cd_delayed": 1},
)
def fund_slr2_potential_dryland_loss():
    """
    Dt,r​ is potential dryland loss in year tt and region rr without protection;
    """
    return fund_slr1_slr_dryland_loss() - fund_slr2_cd_delayed()


@component.add(
    name='"FUND: SLR.3: Actual dryland loss"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr9_fraction_of_the_coastline_protectd": 1,
        "fund_slr2_potential_dryland_loss": 1,
    },
)
def fund_slr3_actual_dryland_loss():
    """
    Dt,r​ is dryland loss in year tt and region rr;
    """
    return (
        1 - fund_slr9_fraction_of_the_coastline_protectd()
    ) * fund_slr2_potential_dryland_loss()


@component.add(
    name='"FUND: SLR.4: Actual cumulative dryland lost"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr3_actual_dryland_loss": 1,
        "fund_slr4_actual_cumulative_dryland_lost_delayed": 1,
    },
)
def fund_slr4_actual_cumulative_dryland_lost():
    """
    CDt,r​ is the actual cumulative dryland lost at time tt in region rr;
    """
    return (
        fund_slr3_actual_dryland_loss()
        + fund_slr4_actual_cumulative_dryland_lost_delayed()
    )


@component.add(
    name='"FUND: SLR.4: Actual cumulative dryland lost delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr4_actual_cumulative_dryland_lost_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr4_actual_cumulative_dryland_lost_delayed": {
            "initial": {"time_step": 1},
            "step": {"fund_slr4_actual_cumulative_dryland_lost": 1},
        }
    },
)
def fund_slr4_actual_cumulative_dryland_lost_delayed():
    """
    CDt,r​ is the actual cumulative dryland lost at time tt in region rr; - delayed
    """
    return _delayfixed_fund_slr4_actual_cumulative_dryland_lost_delayed()


_delayfixed_fund_slr4_actual_cumulative_dryland_lost_delayed = DelayFixed(
    lambda: fund_slr4_actual_cumulative_dryland_lost(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr4_actual_cumulative_dryland_lost_delayed",
)


@component.add(name='"FUND: SLR.5: area"', comp_type="Constant", comp_subtype="Normal")
def fund_slr5_area():
    """
    AA is the area (in square kilometre) at time tt of region rr;
    """
    return 500000


@component.add(
    name='"FUND: SLR.5: Dryland value"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr5_phi_parameter": 1,
        "fund_slr5_ya0": 1,
        "fund_slr5_epsilon_income_density_elasticity_of_land_value": 1,
        "fund_slr5_area": 1,
        "gross_domestic_product_nominal": 1,
    },
)
def fund_slr5_dryland_value():
    return (
        fund_slr5_phi_parameter()
        * ((gross_domestic_product_nominal() / fund_slr5_area()) / fund_slr5_ya0())
        ** fund_slr5_epsilon_income_density_elasticity_of_land_value()
    )


@component.add(
    name='"FUND: SLR.5: epsilon income density elasticity of land value"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr5_epsilon_income_density_elasticity_of_land_value():
    """
    ϵ is a parameter, the income density elasticity of land value; ϵϵ = 1 (0.25).
    """
    return 1


@component.add(
    name='"FUND: SLR.5: phi parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr5_phi_parameter():
    """
    φ is a parameter; φφ = 4 (2,&gt;0) million dollar per square kilometre (Darwin et al., 1995);
    """
    return 4


@component.add(name='"FUND: SLR.5: YA0"', comp_type="Constant", comp_subtype="Normal")
def fund_slr5_ya0():
    """
    YA0​ =0.635 (million dollar per square kilometre) is a normalisation constant, the average incomde density of the OECD in 1990;
    """
    return 0.635


@component.add(
    name='"FUND: SLR.6: omega M parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr6_omega_m_parameter"},
)
def fund_slr6_omega_m_parameter():
    """
    ωM is a parameter, the annual unit wetland loss due to coastal squeeze (in square kilometre per metre) in region rr; note that is assumed to be constant over time.
    """
    return _ext_constant_fund_slr6_omega_m_parameter()


_ext_constant_fund_slr6_omega_m_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B6",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr6_omega_m_parameter",
)


@component.add(
    name='"FUND: SLR.6: omega S parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr6_omega_s_parameter"},
)
def fund_slr6_omega_s_parameter():
    """
    ωS is a parameter, the annual unit wetland loss due to sea level rise (in square kilometre per metre) in region rr; note that is assumed to be constant over time;
    """
    return _ext_constant_fund_slr6_omega_s_parameter()


_ext_constant_fund_slr6_omega_s_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B5",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr6_omega_s_parameter",
)


@component.add(
    name='"FUND: SLR.6: Wetland loss"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr6_omega_s_parameter": 2,
        "fund_slr10_delta_slr": 1,
        "fund_slr6_omega_m_parameter": 1,
        "fund_slr9_fraction_of_the_coastline_protectd": 1,
    },
)
def fund_slr6_wetland_loss():
    return (
        fund_slr6_omega_s_parameter() * fund_slr10_delta_slr()
        + fund_slr6_omega_m_parameter()
        * fund_slr9_fraction_of_the_coastline_protectd()
        * fund_slr6_omega_s_parameter()
    )


@component.add(
    name='"FUND: SLR.7: Cumulative wetland loss"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr7_cumulative_wetland_loss_delayed": 1,
        "fund_slr7_wetland_loss_delayed": 1,
        "fund_slr7_wm_parameter": 1,
    },
)
def fund_slr7_cumulative_wetland_loss():
    return np.minimum(
        fund_slr7_cumulative_wetland_loss_delayed() + fund_slr7_wetland_loss_delayed(),
        fund_slr7_wm_parameter(),
    )


@component.add(
    name='"FUND: SLR.7: cumulative wetland loss delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr7_cumulative_wetland_loss_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr7_cumulative_wetland_loss_delayed": {
            "initial": {"time_step": 1},
            "step": {"fund_slr7_cumulative_wetland_loss": 1},
        }
    },
)
def fund_slr7_cumulative_wetland_loss_delayed():
    return _delayfixed_fund_slr7_cumulative_wetland_loss_delayed()


_delayfixed_fund_slr7_cumulative_wetland_loss_delayed = DelayFixed(
    lambda: fund_slr7_cumulative_wetland_loss(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr7_cumulative_wetland_loss_delayed",
)


@component.add(
    name='"FUND: SLR.7: wetland loss delayed"',
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_fund_slr7_wetland_loss_delayed": 1},
    other_deps={
        "_delayfixed_fund_slr7_wetland_loss_delayed": {
            "initial": {"time_step": 1},
            "step": {"fund_slr6_wetland_loss": 1},
        }
    },
)
def fund_slr7_wetland_loss_delayed():
    return _delayfixed_fund_slr7_wetland_loss_delayed()


_delayfixed_fund_slr7_wetland_loss_delayed = DelayFixed(
    lambda: fund_slr6_wetland_loss(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_fund_slr7_wetland_loss_delayed",
)


@component.add(
    name='"FUND: SLR.7: Wm parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr7_wm_parameter"},
)
def fund_slr7_wm_parameter():
    """
    WM is a parameter, the total amount of wetland that is exposed to sea level rise; this is assumed to be smaller than the total amount of wetlands in 1990.
    """
    return _ext_constant_fund_slr7_wm_parameter()


_ext_constant_fund_slr7_wm_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B7",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_slr7_wm_parameter",
)


@component.add(
    name='"FUND: SLR.8: alpha parameter"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fund_slr8_alpha_prime_parameter": 1},
)
def fund_slr8_alpha_parameter():
    return 21 * fund_slr8_alpha_prime_parameter()


@component.add(
    name='"FUND: SLR.8: alpha prime parameter"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr8_alpha_prime_parameter():
    return 280000


@component.add(
    name='"FUND: SLR.8: beta income elasticity of wetland value"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr8_beta_income_elasticity_of_wetland_value():
    return 1.16


@component.add(
    name='"FUND: SLR.8: d0 normalisation constant"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr8_d0_normalisation_constant():
    return 27.59


@component.add(
    name='"FUND: SLR.8: delta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr8_delta_parameter():
    return -0.11


@component.add(
    name='"FUND: SLR.8: gamme parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_slr8_gamme_parameter():
    return 0.47


@component.add(
    name='"FUND: SLR.8: population density"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr8_population_density():
    return 100


@component.add(
    name='"FUND: SLR.8: W1990 parameter"',
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_slr8_w1990_parameter"},
)
def fund_slr8_w1990_parameter():
    return _ext_constant_fund_slr8_w1990_parameter()


_ext_constant_fund_slr8_w1990_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_slr.xlsx",
    "Sheet1",
    "B8",
    {},
    _root,
    {},
    "_ext_constant_fund_slr8_w1990_parameter",
)


@component.add(
    name='"FUND: SLR.8: Wetland value"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr8_alpha_parameter": 1,
        "fund_slr8_beta_income_elasticity_of_wetland_value": 1,
        "fund_slr8_y0_normalisation_constant": 1,
        "average_disposable_income_per_capita": 1,
        "fund_slr8_d0_normalisation_constant": 1,
        "fund_slr8_population_density": 1,
        "fund_slr8_gamme_parameter": 1,
        "fund_slr8_w1990_parameter": 2,
        "fund_slr7_cumulative_wetland_loss": 1,
        "fund_slr8_delta_parameter": 1,
    },
)
def fund_slr8_wetland_value():
    return (
        fund_slr8_alpha_parameter()
        * (
            average_disposable_income_per_capita()
            / fund_slr8_y0_normalisation_constant()
        )
        ** fund_slr8_beta_income_elasticity_of_wetland_value()
        * (fund_slr8_population_density() / fund_slr8_d0_normalisation_constant())
        ** fund_slr8_gamme_parameter()
        * (
            (fund_slr8_w1990_parameter() - fund_slr7_cumulative_wetland_loss())
            / fund_slr8_w1990_parameter()
        )
        ** fund_slr8_delta_parameter()
    )


@component.add(
    name='"FUND: SLR.8: y0 normalisation constant"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def fund_slr8_y0_normalisation_constant():
    return 25000


@component.add(
    name='"FUND: SLR.9: fraction of the coastline protectd"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_slr10_npvvp": 1,
        "fund_slr11_slr11_delayed": 1,
        "fund_slr12_slr12_delayed": 1,
    },
)
def fund_slr9_fraction_of_the_coastline_protectd():
    """
    PP is the fraction of the coastline to be protected;
    """
    return np.minimum(
        0,
        1
        - 0.5
        * (
            (fund_slr10_npvvp() + fund_slr11_slr11_delayed())
            / fund_slr12_slr12_delayed()
        ),
    )


@component.add(
    name='"FUND: Total agricultural impact"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_agricultural_imact_of_the_fertilisation": 1,
        "fund_a3_agricultural_impact_of_the_level_of_climate_change": 1,
        "fund_a2_agricultural_impact_of_the_rate_of_climate_change": 1,
    },
)
def fund_total_agricultural_impact():
    return (
        fund_agricultural_imact_of_the_fertilisation()
        + fund_a3_agricultural_impact_of_the_level_of_climate_change()
        + fund_a2_agricultural_impact_of_the_rate_of_climate_change()
    )


@component.add(
    name='"FUND: W.1: alpha parameter"',
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fund_w1_alpha_parameter"},
)
def fund_w1_alpha_parameter():
    """
    α is a parameter (in percent of 1990 GDP per degree Celsius) that specifies the benchmark impact; see Table EFW;
    """
    return _ext_constant_fund_w1_alpha_parameter()


_ext_constant_fund_w1_alpha_parameter = ExtConstant(
    "df_parameters/FUND/output/wiliam_table_efw.xlsx",
    "Sheet1",
    "B3",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_fund_w1_alpha_parameter",
)


@component.add(
    name='"FUND: W.1: beta parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_w1_beta_parameter():
    """
    β = 0.85 (0.15, &gt;0) is a parameter, that specifies how impacts respond to economic growth;
    """
    return 0.85


@component.add(
    name='"FUND: W.1: Change in water resources"',
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fund_w1_alpha_parameter": 1,
        "fund_extra_initial_gdp": 1,
        "fund_w1_tau_parameter": 1,
        "time": 1,
        "fund_extra_initial_revenue": 1,
        "fund_w1_beta_parameter": 1,
        "average_disposable_income_per_capita": 1,
        "fund_extra_initial_population": 1,
        "fund_w1_mu_parameter": 1,
        "population_35_regions": 1,
        "fund_w1_gamma_parameter": 1,
        "temperature_change_in_35regions": 1,
        "gross_domestic_product_nominal": 1,
    },
)
def fund_w1_change_in_water_resources():
    """
    W denotes the change in water resources (in 1995 US dollar) at time tt in region rr; TODO même problème avec le revenue de reference 1990
    """
    return np.minimum(
        fund_w1_alpha_parameter()
        * fund_extra_initial_gdp()
        * (1 - fund_w1_tau_parameter()) ** (time() - 2000)
        * (average_disposable_income_per_capita() / fund_extra_initial_revenue())
        ** fund_w1_beta_parameter()
        * (population_35_regions() / fund_extra_initial_population())
        ** fund_w1_mu_parameter()
        * (temperature_change_in_35regions() / 1) ** fund_w1_gamma_parameter(),
        gross_domestic_product_nominal() / 10,
    )


@component.add(
    name='"FUND: W.1: gamma parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_w1_gamma_parameter():
    """
    γ = 1 (0.5,&gt;0) is a parameter, that determines the response of impact to warming;
    """
    return 1


@component.add(
    name='"FUND: W.1: mu parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_w1_mu_parameter():
    """
    η = 0.85 (0.15,&gt;0) is a parameter that specifies how impacts respond to population growth;
    """
    return 0.85


@component.add(
    name='"FUND: W.1: tau parameter"', comp_type="Constant", comp_subtype="Normal"
)
def fund_w1_tau_parameter():
    """
    τ = 0.005 (0.005, &gt;0) is a parameter, that measures technological progress in water supply and demand.
    """
    return 0.005