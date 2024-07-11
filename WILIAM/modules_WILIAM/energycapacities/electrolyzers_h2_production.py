"""
Module energycapacities.electrolyzers_h2_production
Translated using PySD version 3.13.4
"""

@component.add(
    name="allocation pure hydrogen by process",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSUP H2 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
        "h2_production_from_flexible_electrolysers": 1,
        "share_electrolytic_h2_commodity_by_process": 1,
    },
)
def allocation_pure_hydrogen_by_process():
    """
    Distribution of electrolytic pure hydrogen (commodity) to different processes.
    """
    return (
        h2_production_from_stationary_electrolyzers_by_prosup_h2()
        + h2_production_from_flexible_electrolysers()
    ) * share_electrolytic_h2_commodity_by_process()


@component.add(
    name="CARBON DIOXIDE PER H2 GASES BASED FUEL INTENSITY",
    units="t/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_carbon_dioxide_per_h2_gases_based_fuel_intensity"
    },
)
def carbon_dioxide_per_h2_gases_based_fuel_intensity():
    """
    kg CO2 required to produce 1 kg CH4 in methanization plants (to produce methane from electrolytic hydrogen). Data based on (Hasan Mehrjerdi, 2019): "2.7 kg of CO2 is combined with H2 to make 1 kg of CH4" -> 2.7 kg CO2 / kg CH4 produced
    """
    return _ext_constant_carbon_dioxide_per_h2_gases_based_fuel_intensity()


_ext_constant_carbon_dioxide_per_h2_gases_based_fuel_intensity = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CARBON_DIOXIDE_PER_H2_GASES_BASED_FUEL_INTENSITY",
    {},
    _root,
    {},
    "_ext_constant_carbon_dioxide_per_h2_gases_based_fuel_intensity",
)


@component.add(
    name="CARBON DIOXIDE PER H2 LIQUIDS BASED FUEL INTENSITY",
    units="t/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_carbon_dioxide_per_h2_liquids_based_fuel_intensity"
    },
)
def carbon_dioxide_per_h2_liquids_based_fuel_intensity():
    """
    kg CO2 required to produce 1 kg CH3OH in methanol synthesis process (to produce methanol from electrolytic hydrogen). Data based on (D. Bellotti et al, 2017): according witch data from Table 4 -> 1.42 kg CO2 / kg methanol produced is required
    """
    return _ext_constant_carbon_dioxide_per_h2_liquids_based_fuel_intensity()


_ext_constant_carbon_dioxide_per_h2_liquids_based_fuel_intensity = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CARBON_DIOXIDE_PER_H2_LIQUIDS_BASED_FUEL_INTENSITY",
    {},
    _root,
    {},
    "_ext_constant_carbon_dioxide_per_h2_liquids_based_fuel_intensity",
)


@component.add(
    name="carbon dioxide used for H2 based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_dioxide_used_for_h2_gases_based_fuels": 1,
        "carbon_dioxide_used_for_h2_liquids_based_fuels": 1,
    },
)
def carbon_dioxide_used_for_h2_based_fuels():
    """
    Total CO2 used to produce methane (in methanization plants) and methanol (through methanol synthesis process) from electrolytic hydrogen
    """
    return (
        carbon_dioxide_used_for_h2_gases_based_fuels()
        + carbon_dioxide_used_for_h2_liquids_based_fuels()
    )


@component.add(
    name="carbon dioxide used for H2 gases based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_dioxide_per_h2_gases_based_fuel_intensity": 1,
        "to_commodities_electrolytic_h2": 1,
        "unit_conversion_mj_ej": 1,
        "lhv_hydrogen": 1,
    },
)
def carbon_dioxide_used_for_h2_gases_based_fuels():
    """
    CO2 used in methanization plants to produce methane from electrolytic hydrogen
    """
    return (
        carbon_dioxide_per_h2_gases_based_fuel_intensity()
        * to_commodities_electrolytic_h2().loc[:, "TO gas"].reset_coords(drop=True)
        * unit_conversion_mj_ej()
        / lhv_hydrogen()
    )


@component.add(
    name="carbon dioxide used for H2 liquids based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_dioxide_per_h2_liquids_based_fuel_intensity": 1,
        "to_commodities_electrolytic_h2": 1,
        "unit_conversion_mj_ej": 1,
        "lhv_hydrogen": 1,
    },
)
def carbon_dioxide_used_for_h2_liquids_based_fuels():
    """
    CO2 used in methanol synthesis process to produce methanol from electrolytic hydrogen
    """
    return (
        carbon_dioxide_per_h2_liquids_based_fuel_intensity()
        * to_commodities_electrolytic_h2().loc[:, "TO liquid"].reset_coords(drop=True)
        * unit_conversion_mj_ej()
        / lhv_hydrogen()
    )


@component.add(
    name="carbon used for H2 based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_used_for_h2_gases_based_fuels": 1,
        "carbon_used_for_h2_liquids_based_fuels": 1,
    },
)
def carbon_used_for_h2_based_fuels():
    """
    Total CO2 used to produce methane (in methanization plants) and methanol (through methanol synthesis process) from electrolytic hydrogen
    """
    return (
        carbon_used_for_h2_gases_based_fuels()
        + carbon_used_for_h2_liquids_based_fuels()
    )


@component.add(
    name="carbon used for H2 gases based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "unit_conversion_c_co2": 1,
        "carbon_dioxide_used_for_h2_gases_based_fuels": 1,
    },
)
def carbon_used_for_h2_gases_based_fuels():
    """
    C used in methanization plants to produce methane from electrolytic hydrogen
    """
    return unit_conversion_c_co2() * carbon_dioxide_used_for_h2_gases_based_fuels()


@component.add(
    name="carbon used for H2 liquids based fuels",
    units="tonnes/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "unit_conversion_c_co2": 1,
        "carbon_dioxide_used_for_h2_liquids_based_fuels": 1,
    },
)
def carbon_used_for_h2_liquids_based_fuels():
    """
    C used in methanol synthesis process to produce methanol from electrolytic hydrogen
    """
    return unit_conversion_c_co2() * carbon_dioxide_used_for_h2_liquids_based_fuels()


@component.add(
    name="CF EXOGENOUS FLEXIBLE ELECTROLYSERS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_exogenous_flexible_electrolysers"},
)
def cf_exogenous_flexible_electrolysers():
    """
    Exogenous capacity factor flexible electrolysers. A very low value similar to those of PHS currently is set as first approximation.
    """
    return _ext_constant_cf_exogenous_flexible_electrolysers()


_ext_constant_cf_exogenous_flexible_electrolysers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CF_FLEXIBLE_ELECTROLYSERS",
    {},
    _root,
    {},
    "_ext_constant_cf_exogenous_flexible_electrolysers",
)


@component.add(
    name="CF flexible electrolysers",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cf_exogenous_flexible_electrolysers": 1},
)
def cf_flexible_electrolysers():
    return xr.DataArray(
        cf_exogenous_flexible_electrolysers(),
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        ["REGIONS 9 I"],
    )


@component.add(
    name="CF STATIONARY ELECTROLYZERS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_stationary_electrolyzers"},
)
def cf_stationary_electrolyzers():
    return _ext_constant_cf_stationary_electrolyzers()


_ext_constant_cf_stationary_electrolyzers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "CF_STATIONARY_ELECTROLYZERS",
    {},
    _root,
    {},
    "_ext_constant_cf_stationary_electrolyzers",
)


@component.add(
    name="CORRESPONDENCE MATRIX TO INPUT OUTPUT PROSUP H2 PER COMMODITY",
    units="DMNL",
    subscripts=["PROSUP H2 I", "NRG TO I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity"
    },
)
def correspondence_matrix_to_input_output_prosup_h2_per_commodity():
    """
    Correspondence matrix (0s, 1s and -1s) relating TO inputs and outputs for each PROSUP. Note: negative values for output values fo the process (because the it reduces the amount of TO that needs to be coveres by other processes), positive values for process-inputs (mostly electricity - because it increases the amount of electricity needed to run these flexibility processes).
    """
    return _ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity()


_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity = (
    ExtConstant(
        "model_parameters/energy/energy-transformation.xlsm",
        "Common",
        "CORRESPONDENCE_MATRIX_TO_INPUT_OUTPUT_PROSUP_H2_PER_COMMODITY",
        {
            "PROSUP H2 I": _subscript_dict["PROSUP H2 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        _root,
        {
            "PROSUP H2 I": _subscript_dict["PROSUP H2 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        "_ext_constant_correspondence_matrix_to_input_output_prosup_h2_per_commodity",
    )
)


@component.add(
    name="EFFICIENCY GAS STORAGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_gas_storage"},
)
def efficiency_gas_storage():
    """
    This parameter represents the efficiency associated with the methane storage process; compression of methane for storage and losses due to self-discharge and standby (mainly caused by leaks).
    """
    return _ext_constant_efficiency_gas_storage()


_ext_constant_efficiency_gas_storage = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "EFFICIENCY_GAS_STORAGE",
    {},
    _root,
    {},
    "_ext_constant_efficiency_gas_storage",
)


@component.add(
    name="EFFICIENCY METHANIZATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_methanization"},
)
def efficiency_methanization():
    """
    Methane production, i.e. production of synthetic methane, takes place through the hydrogenation of carbon dioxide (Sabatier process), according to the following formula: CO_2+4H_2?CH_4+2H_2_O This parameter represents the amont of hydrogen energy required to produce synthetic methane (MJ methane produced per MJ hydrogen, in LHV basis).
    """
    return _ext_constant_efficiency_methanization()


_ext_constant_efficiency_methanization = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_METHANIZATION",
    {},
    _root,
    {},
    "_ext_constant_efficiency_methanization",
)


@component.add(
    name="EFFICIENCY METHANOL SYNTHESIS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_methanol_synthesis"},
)
def efficiency_methanol_synthesis():
    """
    This parameter represents the hydrogen energy required to produce methanol (MJ methanol produced per MJ hydrogen, in LHV basis).
    """
    return _ext_constant_efficiency_methanol_synthesis()


_ext_constant_efficiency_methanol_synthesis = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_METHANOL_SYNTHESIS",
    {},
    _root,
    {},
    "_ext_constant_efficiency_methanol_synthesis",
)


@component.add(
    name="EFFICIENCY STATIONARY ELECTROLYZER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_efficiency_stationary_electrolyzer"},
)
def efficiency_stationary_electrolyzer():
    """
    This variable gives an account of the efficiency of converting electrical energy into hydrogen for an electrolyzer (LHV basis), considering the auxiliary elements (pumps, heat exchangers, etc.) i.e. the efficiency of the system. Commercially available electrolyzer technologies include the alkaline electrolyzer (AEL) (mature technology) and the polymer exchange electrolyzer (PEM) (developing technology) and allow the production of hydrogen with a purity very close to 100 %.
    """
    return _ext_constant_efficiency_stationary_electrolyzer()


_ext_constant_efficiency_stationary_electrolyzer = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "EFFICIENCY_ELECTROLYZER",
    {},
    _root,
    {},
    "_ext_constant_efficiency_stationary_electrolyzer",
)


@component.add(
    name="electrolytic H2 required to satisfy H2 demand",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 3,
        "switch_nrg_hydrogen_industrial_demand": 1,
        "efficiency_methanol_synthesis": 1,
        "share_fe_liquid_substituted_by_h2_synthetic_liquid": 1,
        "efficiency_methanization": 1,
        "share_fe_gas_substituted_by_h2_synthetic_gas": 1,
        "h2_production_from_flexible_electrolysers": 1,
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
    },
)
def electrolytic_h2_required_to_satisfy_h2_demand():
    """
    Quantity of hydrogen demanded that is not supplied via stationary electrolysis. Note that hydrogen produced from "flexible_electrolysers_capacity_stock" is deducted from the required amount for satisfaction of TO demand. If this variable is <0 stop new stationary & flexible electrolyzers capacity installation.
    """
    return (
        total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
        * switch_nrg_hydrogen_industrial_demand()
        + share_fe_liquid_substituted_by_h2_synthetic_liquid()
        * total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
        / efficiency_methanol_synthesis()
        + share_fe_gas_substituted_by_h2_synthetic_gas()
        * total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
        / efficiency_methanization()
        - h2_production_from_flexible_electrolysers()
        - h2_production_from_stationary_electrolyzers_by_prosup_h2()
    )


@component.add(
    name="flexible electrolysers capacity decommissioning",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "flexible_electrolysers_capacity_stock": 1,
        "lifetime_electrolyzers": 1,
    },
)
def flexible_electrolysers_capacity_decommissioning():
    """
    Decommission of flexible electrolysers
    """
    return flexible_electrolysers_capacity_stock() / lifetime_electrolyzers()


@component.add(
    name="flexible electrolysers capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "electrolytic_h2_required_to_satisfy_h2_demand": 1,
        "switch_policy_flexible_electrolyzers_expansion_sp_0": 1,
        "year_final_flexible_electrolizers_expansion_sp_0": 2,
        "one_year": 1,
        "switch_nrg_proflex_capacity_expansion_endogenous": 1,
        "objective_flexible_electrolizers_expansion_sp": 1,
        "initial_year_flexible_electrolizers_expansion_sp_0": 2,
        "prosup_flexopt_elec_capacity_expansion": 1,
        "time": 1,
        "flexible_electrolysers_capacity_decommissioning": 1,
    },
)
def flexible_electrolysers_capacity_expansion():
    """
    New capacity of flexible electrolysers
    """
    return (
        if_then_else(
            electrolytic_h2_required_to_satisfy_h2_demand() < 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                switch_nrg_proflex_capacity_expansion_endogenous() == 1,
                lambda: prosup_flexopt_elec_capacity_expansion()
                .loc[:, "PROSUP elec 2 hydrogen"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    switch_policy_flexible_electrolyzers_expansion_sp_0() == 1,
                    lambda: ramp(
                        __data["time"],
                        objective_flexible_electrolizers_expansion_sp()
                        / (
                            year_final_flexible_electrolizers_expansion_sp_0()
                            - initial_year_flexible_electrolizers_expansion_sp_0()
                        ),
                        initial_year_flexible_electrolizers_expansion_sp_0(),
                        year_final_flexible_electrolizers_expansion_sp_0(),
                    )
                    / one_year(),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                        ["REGIONS 9 I"],
                    ),
                ),
            ),
        )
        + flexible_electrolysers_capacity_decommissioning()
    )


@component.add(
    name="flexible electrolysers capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_flexible_electrolysers_capacity_stock": 1},
    other_deps={
        "_integ_flexible_electrolysers_capacity_stock": {
            "initial": {},
            "step": {
                "flexible_electrolysers_capacity_expansion": 1,
                "flexible_electrolysers_capacity_decommissioning": 1,
            },
        }
    },
)
def flexible_electrolysers_capacity_stock():
    """
    Capacity of flexible electrolysers installed in the region
    """
    return _integ_flexible_electrolysers_capacity_stock()


_integ_flexible_electrolysers_capacity_stock = Integ(
    lambda: flexible_electrolysers_capacity_expansion()
    - flexible_electrolysers_capacity_decommissioning(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_flexible_electrolysers_capacity_stock",
)


@component.add(
    name="H2 maximum production via stationary electrolyzer",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def h2_maximum_production_via_stationary_electrolyzer():
    """
    Maximum amount of hydrogen that can be produced with stationary electrolyzers
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="H2 production from flexible electrolysers",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "flexible_electrolysers_capacity_stock": 1,
        "cf_flexible_electrolysers": 1,
        "unit_conversion_hours_year": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def h2_production_from_flexible_electrolysers():
    return (
        flexible_electrolysers_capacity_stock()
        * cf_flexible_electrolysers()
        * unit_conversion_hours_year()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="H2 production from stationary electrolyzers by PROSUP H2",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "unit_conversion_hours_year": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def h2_production_from_stationary_electrolyzers_by_prosup_h2():
    """
    Hydrogen produced by electrolysers ([PROSUP elec 2 hydrogen]).
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * unit_conversion_hours_year()
        * efficiency_stationary_electrolyzer()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="INITIAL STATIONARY ELECTROLYZER CAPACITY STOCK",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_stationary_electrolyzer_capacity_stock"
    },
)
def initial_stationary_electrolyzer_capacity_stock():
    """
    Capacity stock in the initial year of the simulation.
    """
    return _ext_constant_initial_stationary_electrolyzer_capacity_stock()


_ext_constant_initial_stationary_electrolyzer_capacity_stock = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "INITIAL_ELECTROLYZER_CAPACITY_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_stationary_electrolyzer_capacity_stock",
)


@component.add(
    name="INITIAL YEAR FLEXIBLE ELECTROLIZERS EXPANSION SP 0",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0"
    },
)
def initial_year_flexible_electrolizers_expansion_sp_0():
    """
    Initial year of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_initial_year_flexible_electrolizers_expansion_sp_0()


_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_year_flexible_electrolizers_expansion_sp_0",
)


@component.add(
    name="INITIAL YEAR SHARE FE LIQUID AND GAS SUBSTITUTED BY H2 SYNFUELS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Year from which the policies to replace liquids and gases with H2-based synthetic fuels begin
    """
    return (
        _ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)


@component.add(
    name="INITIAL YEAR STATIONARY ELECTROLYZERS EXPANSION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_stationary_electrolyzers_expansion_sp"
    },
)
def initial_year_stationary_electrolyzers_expansion_sp():
    """
    Initial year of the policy scenario for stationary electrolyzers.
    """
    return _ext_constant_initial_year_stationary_electrolyzers_expansion_sp()


_ext_constant_initial_year_stationary_electrolyzers_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_STATIONARY_ELECTROLYZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_year_stationary_electrolyzers_expansion_sp",
)


@component.add(
    name="LIFETIME ELECTROLYZERS",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_lifetime_electrolyzers"},
)
def lifetime_electrolyzers():
    """
    Lifetime of electrolyzers.
    """
    return _ext_constant_lifetime_electrolyzers()


_ext_constant_lifetime_electrolyzers = ExtConstant(
    "model_parameters/energy/energy-hydrogen.xlsx",
    "hydrogen_supply",
    "LIFETIME_ELECTROLYZERS",
    {},
    _root,
    {},
    "_ext_constant_lifetime_electrolyzers",
)


@component.add(
    name="maximum installed capacity electrolysers",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "h2_total_demand_lhv_basis": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "time_step": 1,
        "factor_backup_power_system": 1,
    },
)
def maximum_installed_capacity_electrolysers():
    """
    Assumption: 100% of the hydrogen demand may be electrified.
    """
    return (
        h2_total_demand_lhv_basis()
        / unit_conversion_tj_ej()
        / unit_conversion_hours_year()
        / unit_conversion_tw_per_ej_per_year()
        / time_step()
        * factor_backup_power_system()
    )


@component.add(
    name="OBJECTIVE FLEXIBLE ELECTROLIZERS EXPANSION SP",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_flexible_electrolizers_expansion_sp"
    },
)
def objective_flexible_electrolizers_expansion_sp():
    """
    Final installed capacity of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_objective_flexible_electrolizers_expansion_sp()


_ext_constant_objective_flexible_electrolizers_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_flexible_electrolizers_expansion_sp",
)


@component.add(
    name="OBJECTIVE SHARE FE GAS SUBSTITUTED BY H2 SYNTHETIC GAS SP",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp"
    },
)
def objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp():
    """
    Share of FE gas demand substituted by H2 synthetic gas
    """
    return _ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp()


_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_PERCENTAGE_FE_GAS_SUBSTITUTED_BY_H2_GASES_BASED_FUEL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp",
)


@component.add(
    name="OBJECTIVE SHARE FE LIQUID SUBSTITUTED BY H2 SYNTHETIC LIQUID SP",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp"
    },
)
def objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp():
    return (
        _ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp()
    )


_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "OBJECTIVE_PERCENTAGE_FE_LIQUID_SUBSTITUTED_BY_H2_LIQUIDS_BASED_FUEL_SP*",
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        _root,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        "_ext_constant_objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp",
    )
)


@component.add(
    name="OBJECTIVE STATIONARY ELECTROLYZERS EXPANSION SP",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_stationary_electrolyzers_expansion_sp"
    },
)
def objective_stationary_electrolyzers_expansion_sp():
    """
    Final installed capacity of the policy scenario for stationary electrolyzers.
    """
    return _ext_constant_objective_stationary_electrolyzers_expansion_sp()


_ext_constant_objective_stationary_electrolyzers_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_STATIONARY_ELECTROLYZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_stationary_electrolyzers_expansion_sp",
)


@component.add(
    name="SELECT STATIONARY ELECTROLYZERS EXPANSION PRIORITY SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_stationary_electrolyzers_expansion_priority_sp"
    },
)
def select_stationary_electrolyzers_expansion_priority_sp():
    """
    This switch can take two values: =0 model runs with exogenous capacity expansion for electrolyzers =1 model runs with endogenous capacity expansion for electrolyzers as a function of the energy shortage
    """
    return _ext_constant_select_stationary_electrolyzers_expansion_priority_sp()


_ext_constant_select_stationary_electrolyzers_expansion_priority_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_STATIONARY_ELECTROLYZERS_EXPANSION_PRIORITY_SP",
    {},
    _root,
    {},
    "_ext_constant_select_stationary_electrolyzers_expansion_priority_sp",
)


@component.add(
    name="share electrolytic H2 commodity by process",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSUP H2 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 12,
        "efficiency_methanol_synthesis": 4,
        "efficiency_methanization": 4,
        "share_fe_gas_substituted_by_h2_synthetic_gas": 4,
        "share_fe_liquid_substituted_by_h2_synthetic_liquid": 4,
    },
)
def share_electrolytic_h2_commodity_by_process():
    """
    Share of electrolytic pure hydrogen (commodity) to different processes.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROSUP H2 I": _subscript_dict["PROSUP H2 I"],
        },
        ["REGIONS 9 I", "PROSUP H2 I"],
    )
    value.loc[:, ["PROSUP elec 2 hydrogen"]] = (
        zidz(
            total_fe_including_net_trade()
            .loc[:, "FE hydrogen"]
            .reset_coords(drop=True),
            total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG PRO I": ["PROSUP elec 2 hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP hydrogen 2 liquid"]] = (
        zidz(
            share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis(),
            total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG PRO I": ["PROSUP hydrogen 2 liquid"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP hydrogen 2 gas"]] = (
        zidz(
            share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
            / efficiency_methanization(),
            total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
            + share_fe_liquid_substituted_by_h2_synthetic_liquid()
            * total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            / efficiency_methanol_synthesis()
            + share_fe_gas_substituted_by_h2_synthetic_gas()
            * total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
            / efficiency_methanization(),
        )
        .expand_dims({"NRG PRO I": ["PROSUP hydrogen 2 gas"]}, 1)
        .values
    )
    return value


@component.add(
    name="share FE gas substituted by H2 synthetic gas",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 1,
        "year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 3,
        "initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 4,
        "objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp": 3,
        "time": 3,
    },
)
def share_fe_gas_substituted_by_h2_synthetic_gas():
    return if_then_else(
        switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: if_then_else(
            time()
            < initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                time()
                > year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                lambda: objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp(),
                lambda: -objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp()
                * initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                / (
                    year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                )
                + time()
                * zidz(
                    objective_share_fe_gas_substituted_by_h2_synthetic_gas_sp(),
                    year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="share FE liquid substituted by H2 synthetic liquid",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid": 1,
        "objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp": 3,
        "year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 3,
        "switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 1,
        "initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp": 4,
        "time": 3,
    },
)
def share_fe_liquid_substituted_by_h2_synthetic_liquid():
    """
    Share of FE liquid demand substituted by H2 synthetic liquids
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_percentage_fe_liquid_substituted_by_h2_synthetic_liquid(),
        lambda: if_then_else(
            switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                time()
                < initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: if_then_else(
                    time()
                    > year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                    lambda: objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp(),
                    lambda: -objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp()
                    * initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    / (
                        year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                        - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                    )
                    + time()
                    * zidz(
                        objective_share_fe_liquid_substituted_by_h2_synthetic_liquid_sp(),
                        year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
                        - initial_year_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp(),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="stationary electrolyzer capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stationary_electrolyzer_capacity_stock": 1},
    other_deps={
        "_integ_stationary_electrolyzer_capacity_stock": {
            "initial": {"initial_stationary_electrolyzer_capacity_stock": 1},
            "step": {
                "stationary_electrolyzers_capacity_expansion": 1,
                "stationary_electrolyzers_capacity_decommissioning": 1,
            },
        }
    },
)
def stationary_electrolyzer_capacity_stock():
    """
    Operational capacity stock of electrolyzers.
    """
    return _integ_stationary_electrolyzer_capacity_stock()


_integ_stationary_electrolyzer_capacity_stock = Integ(
    lambda: stationary_electrolyzers_capacity_expansion()
    - stationary_electrolyzers_capacity_decommissioning(),
    lambda: initial_stationary_electrolyzer_capacity_stock(),
    "_integ_stationary_electrolyzer_capacity_stock",
)


@component.add(
    name="stationary electrolyzers capacity decommissioning",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "lifetime_electrolyzers": 1,
    },
)
def stationary_electrolyzers_capacity_decommissioning():
    """
    Decommissioning of electrolyzers capacity stock due to reaching the end of their lifetime.
    """
    return stationary_electrolyzer_capacity_stock() / lifetime_electrolyzers()


@component.add(
    name="stationary electrolyzers capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_availability_unmature_energy_technologies_sp": 2,
        "stationary_electrolyzers_capacity_expansion_required": 1,
        "electrolytic_h2_required_to_satisfy_h2_demand": 1,
        "objective_stationary_electrolyzers_expansion_sp": 1,
        "select_stationary_electrolyzers_expansion_priority_sp": 1,
        "year_final_stationary_electrolyzers_expansion_sp": 2,
        "initial_year_stationary_electrolyzers_expansion_sp": 2,
        "time": 1,
        "stationary_electrolyzers_capacity_decommissioning": 1,
    },
)
def stationary_electrolyzers_capacity_expansion():
    """
    New installed capacities of electrolyzers.
    """
    return (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 2,
            ),
            lambda: if_then_else(
                electrolytic_h2_required_to_satisfy_h2_demand() < 0,
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: if_then_else(
                    select_stationary_electrolyzers_expansion_priority_sp() == 0,
                    lambda: ramp(
                        __data["time"],
                        objective_stationary_electrolyzers_expansion_sp()
                        / (
                            year_final_stationary_electrolyzers_expansion_sp()
                            - initial_year_stationary_electrolyzers_expansion_sp()
                        ),
                        initial_year_stationary_electrolyzers_expansion_sp(),
                        year_final_stationary_electrolyzers_expansion_sp(),
                    ),
                    lambda: stationary_electrolyzers_capacity_expansion_required(),
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        )
        + stationary_electrolyzers_capacity_decommissioning()
    )


@component.add(
    name="stationary electrolyzers capacity expansion required",
    units="TW/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "electrolytic_h2_required_to_satisfy_h2_demand": 1,
        "cf_stationary_electrolyzers": 1,
        "efficiency_stationary_electrolyzer": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "one_year": 1,
    },
)
def stationary_electrolyzers_capacity_expansion_required():
    """
    Electrolyzers capacity expansion required annualy which would make it possible to cover the demand for hydrogen with stationary eletctrolyzers
    """
    return (
        electrolytic_h2_required_to_satisfy_h2_demand()
        / cf_stationary_electrolyzers()
        / efficiency_stationary_electrolyzer()
        / unit_conversion_hours_year()
        / unit_conversion_tw_per_ej_per_year()
        / one_year()
    )


@component.add(
    name="SWITCH NRG PROFLEX CAPACITY EXPANSION ENDOGENOUS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous"
    },
)
def switch_nrg_proflex_capacity_expansion_endogenous():
    """
    0: exogenous capacity expansion of PROFLEX based on scenario parameters inputs 1: endogenous capacity expansion of PROFLEX driven by the allocation of curtailement
    """
    return _ext_constant_switch_nrg_proflex_capacity_expansion_endogenous()


_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_PROFLEX_CAPACITY_EXPANSION_ENDOGENOUS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_proflex_capacity_expansion_endogenous",
)


@component.add(
    name="SWITCH POLICY FLEXIBLE ELECTROLYZERS EXPANSION SP 0",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0"
    },
)
def switch_policy_flexible_electrolyzers_expansion_sp_0():
    """
    Switch to activate and deactivate policy by country.
    """
    return _ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0()


_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_POLICY_FLEXIBLE_ELECTROLYZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_policy_flexible_electrolyzers_expansion_sp_0",
)


@component.add(
    name="SWITCH POLICY SHARE FE LIQUID AND GAS SUBSTITUTED BY H2 SYNFUELS SP",
    units="DMML",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Switch to activate and deactivate policy by country.
    """
    return (
        _ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_POLICY_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_policy_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)


@component.add(
    name="TO commodities electrolytic H2",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_elec_consumption_stationary_electrolyzers_by_prosup_h2": 1,
        "to_h2_gases_based_fuel": 1,
        "to_electrolytic_pure_h2": 1,
        "to_h2_liquids_based_fuel": 1,
    },
)
def to_commodities_electrolytic_h2():
    """
    Adjustment for the energy balance in the energy transformation chain. The amount of energy from TO_gas, TO_liquid and TO_hydrogen (produced from electrolyzers) substract what is already produced.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS 9 I", "NRG TO I"],
    )
    value.loc[:, ["TO elec"]] = (
        to_elec_consumption_stationary_electrolyzers_by_prosup_h2()
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        to_h2_gases_based_fuel()
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = 0
    value.loc[:, ["TO hydrogen"]] = (
        to_electrolytic_pure_h2()
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"]] = (
        to_h2_liquids_based_fuel()
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = 0
    value.loc[:, ["TO solid fossil"]] = 0
    return value


@component.add(
    name="TO elec consumption stationary electrolyzers by PROSUP H2",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzer_capacity_stock": 1,
        "cf_stationary_electrolyzers": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_ej": 1,
    },
)
def to_elec_consumption_stationary_electrolyzers_by_prosup_h2():
    """
    Consumption of electricity by electrolyzers to produce H2 and H2-derived fuels ([PROSUP_elec_2_hydrogen]).
    """
    return (
        stationary_electrolyzer_capacity_stock()
        * cf_stationary_electrolyzers()
        * unit_conversion_hours_year()
        * unit_conversion_w_tw()
        * unit_conversion_j_wh()
        / unit_conversion_j_ej()
    )


@component.add(
    name="TO electrolytic pure H2",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"allocation_pure_hydrogen_by_process": 1},
)
def to_electrolytic_pure_h2():
    """
    Pure electrolytic hydrogen usage in the economy. Actually, PROSUP_elec_2_hydrogen should be here substituted by other processes using pure hydrogen.
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP elec 2 hydrogen"]
        .reset_coords(drop=True)
    )


@component.add(
    name="TO H2 gases based fuel",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "allocation_pure_hydrogen_by_process": 1,
        "efficiency_methanization": 1,
    },
)
def to_h2_gases_based_fuel():
    """
    Gas produced in methanization plants (commodity based on electrolytic hydrogen)
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP hydrogen 2 gas"]
        .reset_coords(drop=True)
        * efficiency_methanization()
    )


@component.add(
    name="TO H2 liquids based fuel",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "allocation_pure_hydrogen_by_process": 1,
        "efficiency_methanol_synthesis": 1,
    },
)
def to_h2_liquids_based_fuel():
    """
    Liquid produced in methanol synthesis process (commodity based on electrolytic hydrogen)
    """
    return (
        allocation_pure_hydrogen_by_process()
        .loc[:, "PROSUP hydrogen 2 liquid"]
        .reset_coords(drop=True)
        * efficiency_methanol_synthesis()
    )


@component.add(
    name="TO PROSUP electrolytic H2 per commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSUP H2 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_elec_consumption_stationary_electrolyzers_by_prosup_h2": 1,
        "correspondence_matrix_to_input_output_prosup_h2_per_commodity": 4,
        "h2_production_from_stationary_electrolyzers_by_prosup_h2": 1,
    },
)
def to_prosup_electrolytic_h2_per_commodity():
    """
    Note: negative values for output values fo the process (because the it reduces the amount of TO that needs to be coveres by other processes), positive values for process-inputs (mostly electricity - because it increases the amount of electricity needed to run these flexibility processes).
    """
    return to_elec_consumption_stationary_electrolyzers_by_prosup_h2() * if_then_else(
        correspondence_matrix_to_input_output_prosup_h2_per_commodity() > 0,
        lambda: correspondence_matrix_to_input_output_prosup_h2_per_commodity(),
        lambda: xr.DataArray(
            0,
            {
                "PROSUP H2 I": _subscript_dict["PROSUP H2 I"],
                "NRG TO I": _subscript_dict["NRG TO I"],
            },
            ["PROSUP H2 I", "NRG TO I"],
        ),
    ) + h2_production_from_stationary_electrolyzers_by_prosup_h2() * if_then_else(
        correspondence_matrix_to_input_output_prosup_h2_per_commodity() > 0,
        lambda: xr.DataArray(
            0,
            {
                "PROSUP H2 I": _subscript_dict["PROSUP H2 I"],
                "NRG TO I": _subscript_dict["NRG TO I"],
            },
            ["PROSUP H2 I", "NRG TO I"],
        ),
        lambda: correspondence_matrix_to_input_output_prosup_h2_per_commodity(),
    )


@component.add(
    name="YEAR FINAL FLEXIBLE ELECTROLIZERS EXPANSION SP 0",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_flexible_electrolizers_expansion_sp_0"
    },
)
def year_final_flexible_electrolizers_expansion_sp_0():
    """
    Final year of the policy scenario for flexible electrolyzers.
    """
    return _ext_constant_year_final_flexible_electrolizers_expansion_sp_0()


_ext_constant_year_final_flexible_electrolizers_expansion_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_FLEXIBLE_ELECTROLIZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_flexible_electrolizers_expansion_sp_0",
)


@component.add(
    name="YEAR FINAL SHARE FE LIQUID AND GAS SUBSTITUTED BY H2 SYNFUELS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp"
    },
)
def year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp():
    """
    Target year of policies to replace liquids and gases with H2-based synthetic fuels
    """
    return (
        _ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp()
    )


_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_PERCENTAGE_FE_LIQUID_AND_GAS_SUBSTITUTED_BY_H2_LIQUIDS_AND_GASES_BASED_FUEL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_share_fe_liquid_and_gas_substituted_by_h2_synfuels_sp",
)


@component.add(
    name="YEAR FINAL STATIONARY ELECTROLYZERS EXPANSION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_stationary_electrolyzers_expansion_sp"
    },
)
def year_final_stationary_electrolyzers_expansion_sp():
    """
    Final year of the policy scenario for stationary electrolyzers.
    """
    return _ext_constant_year_final_stationary_electrolyzers_expansion_sp()


_ext_constant_year_final_stationary_electrolyzers_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_STATIONARY_ELECTROLYZERS_EXPANSION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_stationary_electrolyzers_expansion_sp",
)
