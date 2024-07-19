"""
Module energyexogenous_inputs
Translated using PySD version 3.13.4
"""

@component.add(
    name="BATTERIES PER EV VEHICLE",
    units="batteries/vehicle",
    comp_type="Constant",
    comp_subtype="Normal",
)
def batteries_per_ev_vehicle():
    return 1


@component.add(
    name="CF EV batteries for Transp",
    units="DMNL",
    subscripts=["EV BATTERIES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_ev_batteries_for_transp"},
)
def cf_ev_batteries_for_transp():
    """
    CF of EV batteries for Transportation use.
    """
    return _ext_constant_cf_ev_batteries_for_transp()


_ext_constant_cf_ev_batteries_for_transp = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV BATTERIES I": ["LMO"]},
    _root,
    {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]},
    "_ext_constant_cf_ev_batteries_for_transp",
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV BATTERIES I": ["NMC622"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV BATTERIES I": ["NMC811"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV BATTERIES I": ["NCA"]},
)

_ext_constant_cf_ev_batteries_for_transp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "CF_EV_batteries",
    {"EV BATTERIES I": ["LFP"]},
)


@component.add(
    name="ENERGY VARIABILITY LINEAR REGRESSION COEFFICIENTS",
    units="DMNL",
    subscripts=["OUTPUTS NGR VARIABILITY I", "PREDICTORS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_linear_regression_coefficients"
    },
)
def energy_variability_linear_regression_coefficients():
    """
    Coefficients of the multiple linear regression models
    """
    return _ext_constant_energy_variability_linear_regression_coefficients()


_ext_constant_energy_variability_linear_regression_coefficients = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "COEFFICIENTS_LINEAR",
    {
        "OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"],
        "PREDICTORS NGR VARIABILITY I": _subscript_dict["PREDICTORS NGR VARIABILITY I"],
    },
    _root,
    {
        "OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"],
        "PREDICTORS NGR VARIABILITY I": _subscript_dict["PREDICTORS NGR VARIABILITY I"],
    },
    "_ext_constant_energy_variability_linear_regression_coefficients",
)


@component.add(
    name="ENERGY VARIABILITY LINEAR REGRESSION INTERCEPT",
    units="DMNL",
    subscripts=["OUTPUTS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_linear_regression_intercept"
    },
)
def energy_variability_linear_regression_intercept():
    """
    Independent term of the multiple logistic regression equations in the energy variability submodule
    """
    return _ext_constant_energy_variability_linear_regression_intercept()


_ext_constant_energy_variability_linear_regression_intercept = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "INTERCEPT_LINEAR*",
    {"OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"]},
    _root,
    {"OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"]},
    "_ext_constant_energy_variability_linear_regression_intercept",
)


@component.add(
    name="ENERGY VARIABILITY LOGISTIC REGRESSION COEFFICIENTS",
    units="DMNL",
    subscripts=["OUTPUTS NGR VARIABILITY I", "PREDICTORS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_logistic_regression_coefficients"
    },
)
def energy_variability_logistic_regression_coefficients():
    """
    Coefficients of the multiple logistic regression models
    """
    return _ext_constant_energy_variability_logistic_regression_coefficients()


_ext_constant_energy_variability_logistic_regression_coefficients = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "COEFFICIENTS_LOGISTIC",
    {
        "OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"],
        "PREDICTORS NGR VARIABILITY I": _subscript_dict["PREDICTORS NGR VARIABILITY I"],
    },
    _root,
    {
        "OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"],
        "PREDICTORS NGR VARIABILITY I": _subscript_dict["PREDICTORS NGR VARIABILITY I"],
    },
    "_ext_constant_energy_variability_logistic_regression_coefficients",
)


@component.add(
    name="ENERGY VARIABILITY LOGISTIC REGRESSION INTERCEPT",
    units="DMNL",
    subscripts=["OUTPUTS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_variability_logistic_regression_intercept"
    },
)
def energy_variability_logistic_regression_intercept():
    """
    Independent term of the multiple logistic regression equations in the energy variability submodule
    """
    return _ext_constant_energy_variability_logistic_regression_intercept()


_ext_constant_energy_variability_logistic_regression_intercept = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "COEFFICIENTS",
    "INTERCEPT_LOGISTIC*",
    {"OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"]},
    _root,
    {"OUTPUTS NGR VARIABILITY I": _subscript_dict["OUTPUTS NGR VARIABILITY I"]},
    "_ext_constant_energy_variability_logistic_regression_intercept",
)


@component.add(
    name="EROIst ini hydro 2015",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eroist_ini_hydro_2015"},
)
def eroist_ini_hydro_2015():
    return _ext_constant_eroist_ini_hydro_2015()


_ext_constant_eroist_ini_hydro_2015 = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "EROIst_ini_hydro_2015",
    {},
    _root,
    {},
    "_ext_constant_eroist_ini_hydro_2015",
)


@component.add(
    name="EXO TOTAL TRANSPORT DEMAND BY REGION AND TYPE OF HH",
    units="persons*km",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh"
    },
)
def exo_total_transport_demand_by_region_and_type_of_hh():
    return _ext_constant_exo_total_transport_demand_by_region_and_type_of_hh()


_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "transport_demand_2015",
    "TOTAL_TRANSPORT_DEMAND_BY_REGION_AND_TYPE_OF_HH",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_exo_total_transport_demand_by_region_and_type_of_hh",
)


@component.add(
    name="FACTOR BACKUP POWER SYSTEM",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_backup_power_system"},
)
def factor_backup_power_system():
    """
    Factor of overcapacity to represent the reserves in the power system (related to the stability and reliability of the power grid)
    """
    return _ext_constant_factor_backup_power_system()


_ext_constant_factor_backup_power_system = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "FACTOR_BACKUP_POWER_SYSTEM",
    {},
    _root,
    {},
    "_ext_constant_factor_backup_power_system",
)


@component.add(
    name="FINAL ENERGY CONSUMPTION INITIAL",
    units="MJ/(km*vehicle)",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_energy_consumption_initial"},
)
def final_energy_consumption_initial():
    """
    Energy vehicle consumption by region, power train and transport mode in MJ/(vehicle*km)
    """
    return _ext_constant_final_energy_consumption_initial()


_ext_constant_final_energy_consumption_initial = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_final_energy_consumption_initial",
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_final_energy_consumption_initial.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FINAL_ENERGY_CONSUMPTION_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="HISTORIC CO2 EMISSIONS ENERGY AND WASTE",
    units="Mt/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historic_co2_emissions_energy_and_waste",
        "__data__": "_ext_data_historic_co2_emissions_energy_and_waste",
        "time": 1,
    },
)
def historic_co2_emissions_energy_and_waste():
    """
    Historic CO2 emissions from energy and waste (IPCC categories).
    """
    return _ext_data_historic_co2_emissions_energy_and_waste(time())


_ext_data_historic_co2_emissions_energy_and_waste = ExtData(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "historic_GHG_emissions",
    "historic_time_index",
    "HISTORIC_CO2_EMISSIONS_FROM_ENERGY_AND_WASTE",
    "interpolate",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_historic_co2_emissions_energy_and_waste",
)


@component.add(
    name="HISTORICAL ENERGY INTENSITIES TOP DOWN BY SECTOR AND FE",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe"
    },
)
def historical_energy_intensities_top_down_by_sector_and_fe():
    """
    Initial final energy intensities by sector and final energy obtained from EXIOBASE only for year 2015. 0 values are avoided and instead 0.00001 to avoid error given that if the initial value of Energy Intensity stocks are 0, the variation being dependent on itself, and thus the value can never change.
    """
    return _ext_constant_historical_energy_intensities_top_down_by_sector_and_fe()


_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "AUSTRIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe",
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "BELGIUM_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "BULGARIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "CROATIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CROATIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "CYPRUS_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "CZECH_REPUBLIC_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "DENMARK_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["DENMARK"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "ESTONIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "FINLAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["FINLAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "FRANCE_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "GERMANY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["GERMANY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "GREECE_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["GREECE"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "HUNGARY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "IRELAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["IRELAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "ITALY_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ITALY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "LATVIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LATVIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "LITHUANIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "LUXEMBOURG_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "MALTA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["MALTA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "NETHERLANDS_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "POLAND_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["POLAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "PORTUGAL_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "ROMANIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "SLOVAKIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "SLOVENIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "SPAIN_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SPAIN"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "SWEDEN_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "UK_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["UK"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "CHINA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CHINA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "EASOC_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["EASOC"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "INDIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["INDIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "LATAM_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LATAM"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "RUSSIA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "USMCA_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["USMCA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_energy_intensities_top_down_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Energy_intensities_by_sector",
    "LROW_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LROW"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)


@component.add(
    name="HISTORICAL NON ENERGY USE INTENSITIES BY SECTOR AND FE",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe"
    },
)
def historical_non_energy_use_intensities_by_sector_and_fe():
    """
    Energy intensities of non energy sectors obtained from EXIOBASE for 2015
    """
    return _ext_constant_historical_non_energy_use_intensities_by_sector_and_fe()


_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "AUSTRIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe",
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "BELGIUM_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "BULGARIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "CROATIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CROATIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "CYPRUS_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "CZECH_REPUBLIC_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "DENMARK_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["DENMARK"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "ESTONIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "FINLAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["FINLAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "FRANCE_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "GERMANY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["GERMANY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "GREECE_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["GREECE"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "HUNGARY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "IRELAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["IRELAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "ITALY_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ITALY"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "LATVIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LATVIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "LITHUANIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "LUXEMBOURG_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "MALTA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["MALTA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "NETHERLANDS_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "POLAND_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["POLAND"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "PORTUGAL_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "ROMANIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "SLOVAKIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "SLOVENIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "SPAIN_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SPAIN"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "SWEDEN_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "UK_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["UK"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "CHINA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["CHINA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "EASOC_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["EASOC"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "INDIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["INDIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "LATAM_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LATAM"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "RUSSIA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "USMCA_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["USMCA"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)

_ext_constant_historical_non_energy_use_intensities_by_sector_and_fe.add(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Non-energy-use_intensities_by_s",
    "LROW_NON_ENERGY_INTENSITIES_BY_SECTOR_AND_FE",
    {
        "REGIONS 35 I": ["LROW"],
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
)


@component.add(
    name="IEA GDC BY COMMODITY EMPIRICAL",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PE I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_iea_gdc_by_commodity_empirical",
        "__data__": "_ext_data_iea_gdc_by_commodity_empirical",
        "time": 1,
    },
)
def iea_gdc_by_commodity_empirical():
    """
    Empirical primary energy demand (=GDC, Gross Domestic Demand) + Exports / - Imports by PE-commodity and region. Source: IEA Energy balances.
    """
    return _ext_data_iea_gdc_by_commodity_empirical(time())


_ext_data_iea_gdc_by_commodity_empirical = ExtData(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "EU27_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["EU27"], "NRG PE I": _subscript_dict["NRG PE I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
    "_ext_data_iea_gdc_by_commodity_empirical",
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "UK_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["UK"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "EASOC_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["EASOC"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "INDIA_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["INDIA"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "LATAM_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["LATAM"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "RUSSIA_PE_IEA",
    "interpolate",
    {"REGIONS 9 I": ["RUSSIA"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "USMCA_PE_IEA",
    None,
    {"REGIONS 9 I": ["USMCA"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "LROW_PE_IEA",
    None,
    {"REGIONS 9 I": ["LROW"], "NRG PE I": _subscript_dict["NRG PE I"]},
)

_ext_data_iea_gdc_by_commodity_empirical.add(
    "model_parameters/energy/IEA_energy_balance_vensim_import.xlsx",
    "IEA_GDC",
    "GDC_TIME",
    "CHINA_PE_IEA",
    None,
    {"REGIONS 9 I": ["CHINA"], "NRG PE I": _subscript_dict["NRG PE I"]},
)


@component.add(
    name="IMV PROSUP STORAGE LOSSES",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSUP STORAGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_imv_prosup_storage_losses"},
)
def imv_prosup_storage_losses():
    """
    Storage Losses for elec, gas and (district-)heat --> TO BE ENDOGENIZED
    """
    return _ext_constant_imv_prosup_storage_losses()


_ext_constant_imv_prosup_storage_losses = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["CHINA"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
    "_ext_constant_imv_prosup_storage_losses",
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["EASOC"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["EU27"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["INDIA"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["LATAM"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["LROW"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "storage_losses_required_per_process*",
    {"REGIONS 9 I": ["UK"], "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"]},
)

_ext_constant_imv_prosup_storage_losses.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "storage_losses_required_per_process*",
    {
        "REGIONS 9 I": ["USMCA"],
        "PROSUP STORAGES I": _subscript_dict["PROSUP STORAGES I"],
    },
)


@component.add(
    name="INITIAL 2W 3W FLEET",
    units="vehicle",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_2w_3w_fleet"},
)
def initial_2w_3w_fleet():
    """
    Initial LDV fleet by type of household in 2015.
    """
    return _ext_constant_initial_2w_3w_fleet()


_ext_constant_initial_2w_3w_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_AUSTRIA_FLEET",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_2w_3w_fleet",
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_BELGIUM_FLEET",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_BULGARIA_FLEET",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_CROATIA_FLEET",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_CYPRUS_FLEET",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_CZECH_REPUBLIC_FLEET",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_DENMARK_FLEET",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_ESTONIA_FLEET",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_FINLAND_FLEET",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_FRANCE_FLEET",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_GERMANY_FLEET",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_GREECE_FLEET",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_HUNGARY_FLEET",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_IRELAND_FLEET",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_ITALY_FLEET",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_LATVIA_FLEET",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_LITHUANIA_FLEET",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_LUXEMBOURG_FLEET",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_MALTA_FLEET",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_NETHERLANDS_FLEET",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_POLAND_FLEET",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_PORTUGAL_FLEET",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_ROMANIA_FLEET",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_SLOVAKIA_FLEET",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_SLOVENIA_FLEET",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_SPAIN_FLEET",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_SWEDEN_FLEET",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_UK_FLEET",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_CHINA_FLEET",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_EASOC_FLEET",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_INDIA_FLEET",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_LATAM_FLEET",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_RUSSIA_FLEET",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_USMCA_FLEET",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_2w_3w_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "2W_3W_fleet_by_household",
    "INITIAL_2W_3W_LROW_FLEET",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)


@component.add(
    name="INITIAL LDV FLEET",
    units="vehicle",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_ldv_fleet"},
)
def initial_ldv_fleet():
    """
    Initial LDV fleet by type of household in 2015.
    """
    return _ext_constant_initial_ldv_fleet()


_ext_constant_initial_ldv_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_AUSTRIA_FLEET",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_initial_ldv_fleet",
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_BELGIUM_FLEET",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_BULGARIA_FLEET",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_CROATIA_FLEET",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_CYPRUS_FLEET",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_CZECH_REPUBLIC_FLEET",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_DENMARK_FLEET",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_ESTONIA_FLEET",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_FINLAND_FLEET",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_FRANCE_FLEET",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_GERMANY_FLEET",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_GREECE_FLEET",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_HUNGARY_FLEET",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_IRELAND_FLEET",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_ITALY_FLEET",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_LATVIA_FLEET",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_LITHUANIA_FLEET",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_LUXEMBOURG_FLEET",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_MALTA_FLEET",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_NETHERLANDS_FLEET",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_POLAND_FLEET",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_PORTUGAL_FLEET",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_ROMANIA_FLEET",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_SLOVAKIA_FLEET",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_SLOVENIA_FLEET",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_SPAIN_FLEET",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_SWEDEN_FLEET",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_UK_FLEET",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_CHINA_FLEET",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_EASOC_FLEET",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_INDIA_FLEET",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_LATAM_FLEET",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_RUSSIA_FLEET",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_USMCA_FLEET",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)

_ext_constant_initial_ldv_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "LDV_fleet_by_household",
    "INITIAL_LDV_LROW_FLEET",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
)


@component.add(
    name="INITIAL LOAD FACTOR PASSENGERS VEHICLES",
    units="persons/vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_load_factor_passengers_vehicles"
    },
)
def initial_load_factor_passengers_vehicles():
    """
    Capacity of vehicles in passengers per vehicle in the initial year.
    """
    return _ext_constant_initial_load_factor_passengers_vehicles()


_ext_constant_initial_load_factor_passengers_vehicles = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_initial_load_factor_passengers_vehicles",
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_load_factor_passengers_vehicles.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "LOAD_FACTOR_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="INITIAL PASSENGER TRANSPORT DEMAND SHARE",
    units="DMML",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_passenger_transport_modal_share_by_region": 1,
        "initial_power_train_share_by_passenger_transport_mode": 1,
    },
)
def initial_passenger_transport_demand_share():
    return (
        initial_passenger_transport_modal_share_by_region()
        * initial_power_train_share_by_passenger_transport_mode().transpose(
            "REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "TRANSPORT POWER TRAIN I"
        )
    ).transpose(
        "REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"
    )


@component.add(
    name="INITIAL PASSENGERS PRIVATE FLEET",
    units="vehicle",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_private_fleet"},
)
def initial_passengers_private_fleet():
    """
    Initial private vehicle fleet in 2015.
    """
    return _ext_constant_initial_passengers_private_fleet()


_ext_constant_initial_passengers_private_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
    "_ext_constant_initial_passengers_private_fleet",
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_private_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PRIVATE_FLEET_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
)


@component.add(
    name="INITIAL PASSENGERS PUBLIC FLEET",
    units="vehicle",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_public_fleet"},
)
def initial_passengers_public_fleet():
    """
    Initial public vehicle fleet in 2015.
    """
    return _ext_constant_initial_passengers_public_fleet()


_ext_constant_initial_passengers_public_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
    "_ext_constant_initial_passengers_public_fleet",
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)

_ext_constant_initial_passengers_public_fleet.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PUBLIC_FLEET_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
    },
)


@component.add(
    name="INITIAL PASSENGERS VEHICLE DISTANCE",
    units="km",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_passengers_vehicle_distance"},
)
def initial_passengers_vehicle_distance():
    """
    Annual vehicle distance travelled by type of transport mode and power train in 2015 year in km.
    """
    return _ext_constant_initial_passengers_vehicle_distance()


_ext_constant_initial_passengers_vehicle_distance = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_initial_passengers_vehicle_distance",
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passengers_vehicle_distance.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "VEHICLE_DISTANCE_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="kW per battery EV",
    units="kW/battery",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_kw_per_battery_ev"},
)
def kw_per_battery_ev():
    """
    Average kW per battery of electrical vehicle.
    """
    return _ext_constant_kw_per_battery_ev()


_ext_constant_kw_per_battery_ev = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Wattios_per_battery_EV",
    {},
    _root,
    {},
    "_ext_constant_kw_per_battery_ev",
)


@component.add(
    name="MAX LIFETIME EV BATTERIES",
    units="Years",
    subscripts=["EV BATTERIES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_lifetime_ev_batteries"},
)
def max_lifetime_ev_batteries():
    """
    Maximum lifetime of the batteries for electric vehicles if used solely for mobility.
    """
    return _ext_constant_max_lifetime_ev_batteries()


_ext_constant_max_lifetime_ev_batteries = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV BATTERIES I": ["LMO"]},
    _root,
    {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]},
    "_ext_constant_max_lifetime_ev_batteries",
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NMC622"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NMC811"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NCA"]},
)

_ext_constant_max_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "max_lifetime_EV_batteries",
    {"EV BATTERIES I": ["LFP"]},
)


@component.add(
    name="MAXIMUM PREDICTORS VARIABILITY REGRESSION",
    units="DMNL",
    subscripts=["BASIC PREDICTORS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_maximum_predictors_variability_regression"
    },
)
def maximum_predictors_variability_regression():
    """
    Maximum value in the range of regression models for the energy variability submodule
    """
    return _ext_constant_maximum_predictors_variability_regression()


_ext_constant_maximum_predictors_variability_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "RANGES",
    "MAXIMUM_RANGE_VARIABILITY*",
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    _root,
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    "_ext_constant_maximum_predictors_variability_regression",
)


@component.add(
    name="MILEAGE VEHICLES",
    units="km",
    subscripts=["TRANSPORT POWER TRAIN I", "TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mileage_vehicles"},
)
def mileage_vehicles():
    return _ext_constant_mileage_vehicles()


_ext_constant_mileage_vehicles = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "MILEAGE_VEHICLES",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "TRANSPORT MODE I": _subscript_dict["TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "TRANSPORT MODE I": _subscript_dict["TRANSPORT MODE I"],
    },
    "_ext_constant_mileage_vehicles",
)


@component.add(
    name="min lifetime EV batteries",
    units="Years",
    subscripts=["EV BATTERIES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_min_lifetime_ev_batteries"},
)
def min_lifetime_ev_batteries():
    """
    Minimum lifetime of the batteries for electric vehicles. When used for electricity storage for back-up to the system besides its use for mobility we assume that the lifetime of the battery decreases proportionally to the number of additional cycles.
    """
    return _ext_constant_min_lifetime_ev_batteries()


_ext_constant_min_lifetime_ev_batteries = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV BATTERIES I": ["LMO"]},
    _root,
    {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]},
    "_ext_constant_min_lifetime_ev_batteries",
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NMC622"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NMC811"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV BATTERIES I": ["NCA"]},
)

_ext_constant_min_lifetime_ev_batteries.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "min_lifetime_EV_batteries",
    {"EV BATTERIES I": ["LFP"]},
)


@component.add(
    name="MINIMUM PREDICTORS VARIABILITY REGRESSION",
    units="DMNL",
    subscripts=["BASIC PREDICTORS NGR VARIABILITY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_minimum_predictors_variability_regression"
    },
)
def minimum_predictors_variability_regression():
    """
    Minimum value in the range of regression models for the energy variability submodule
    """
    return _ext_constant_minimum_predictors_variability_regression()


_ext_constant_minimum_predictors_variability_regression = ExtConstant(
    "model_parameters/energy/intermittency_coefficients.xlsx",
    "RANGES",
    "MINIMUM_RANGE_VARIABILITY*",
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    _root,
    {
        "BASIC PREDICTORS NGR VARIABILITY I": _subscript_dict[
            "BASIC PREDICTORS NGR VARIABILITY I"
        ]
    },
    "_ext_constant_minimum_predictors_variability_regression",
)


@component.add(
    name="Net stored energy EV battery over lifetime",
    units="MJ",
    subscripts=["EV BATTERIES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_net_stored_energy_ev_battery_over_lifetime"
    },
)
def net_stored_energy_ev_battery_over_lifetime():
    """
    Net stored energy EV battery in whole lifetime.
    """
    return _ext_constant_net_stored_energy_ev_battery_over_lifetime()


_ext_constant_net_stored_energy_ev_battery_over_lifetime = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV BATTERIES I": ["LMO"]},
    _root,
    {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]},
    "_ext_constant_net_stored_energy_ev_battery_over_lifetime",
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV BATTERIES I": ["NMC622"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV BATTERIES I": ["NMC811"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV BATTERIES I": ["NCA"]},
)

_ext_constant_net_stored_energy_ev_battery_over_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Net_stored_energy_EV_battery_over_lifetime",
    {"EV BATTERIES I": ["LFP"]},
)


@component.add(
    name="PROREF CONVERSION FACTORS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROREF I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_conversion_factors"},
)
def proref_conversion_factors():
    """
    refinery process transformation efficiencies (oil refinery, coal refinery, bio refinery, gas2hydrogen)
    """
    return _ext_constant_proref_conversion_factors()


_ext_constant_proref_conversion_factors = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["CHINA"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
    "_ext_constant_proref_conversion_factors",
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["EASOC"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["EU27"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["INDIA"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["LATAM"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["LROW"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["RUSSIA"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["USMCA"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)

_ext_constant_proref_conversion_factors.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "conversion_efficiency_per_refinery_process*",
    {"REGIONS 9 I": ["UK"], "NRG PROREF I": _subscript_dict["NRG PROREF I"]},
)


@component.add(
    name="PROREF INPUT SHARES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROREF I", "NRG PE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_input_shares_sp"},
)
def proref_input_shares_sp():
    """
    Input-split of the refineration process
    """
    return _ext_constant_proref_input_shares_sp()


_ext_constant_proref_input_shares_sp = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["CHINA"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
    "_ext_constant_proref_input_shares_sp",
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["EASOC"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["EU27"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["INDIA"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["LATAM"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["LROW"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["UK"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)

_ext_constant_proref_input_shares_sp.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "primary_energy_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["USMCA"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
        "NRG PE I": _subscript_dict["NRG PE I"],
    },
)


@component.add(
    name="PROREF OUTPUT SHARES",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TI I", "NRG PROREF I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_proref_output_shares"},
)
def proref_output_shares():
    """
    How much individual processes contribute to total TI.
    """
    return _ext_constant_proref_output_shares()


_ext_constant_proref_output_shares = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["CHINA"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
    "_ext_constant_proref_output_shares",
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["EASOC"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["EU27"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["INDIA"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["LATAM"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["LROW"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["UK"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)

_ext_constant_proref_output_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "process_refinery_required_shares_of_process_and_commodity_max",
    {
        "REGIONS 9 I": ["USMCA"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "NRG PROREF I": _subscript_dict["NRG PROREF I"],
    },
)


@component.add(
    name="PROSUP ENERGY SECTOR OWN CONSUMPTION SHARE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSUP SECTOR OWN CONSUMPTION I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_energy_sector_own_consumption_share"
    },
)
def prosup_energy_sector_own_consumption_share():
    """
    Energy sector own consumption excluding storage losses (to avoid double counting!) as share of Final Energy
    """
    return _ext_constant_prosup_energy_sector_own_consumption_share()


_ext_constant_prosup_energy_sector_own_consumption_share = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["CHINA"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
    "_ext_constant_prosup_energy_sector_own_consumption_share",
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["EASOC"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["EU27"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["INDIA"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["LATAM"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["LROW"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["UK"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)

_ext_constant_prosup_energy_sector_own_consumption_share.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "sector_own_consumption_required_per_process*",
    {
        "REGIONS 9 I": ["USMCA"],
        "PROSUP SECTOR OWN CONSUMPTION I": _subscript_dict[
            "PROSUP SECTOR OWN CONSUMPTION I"
        ],
    },
)


@component.add(
    name="PROSUP TRANSMISSION LOSS SHARES",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSUP TRANSMISSION I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prosup_transmission_loss_shares"},
)
def prosup_transmission_loss_shares():
    """
    Transmission losses as share of Final Energy (including distribution and transportation losses). Exogeneous input calculated from energy balances.
    """
    return _ext_constant_prosup_transmission_loss_shares()


_ext_constant_prosup_transmission_loss_shares = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["CHINA"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
    "_ext_constant_prosup_transmission_loss_shares",
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["EASOC"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["EU27"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["INDIA"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["LATAM"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["LROW"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["UK"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)

_ext_constant_prosup_transmission_loss_shares.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "transmission_losses_required_shares*",
    {
        "REGIONS 9 I": ["USMCA"],
        "PROSUP TRANSMISSION I": _subscript_dict["PROSUP TRANSMISSION I"],
    },
)


@component.add(
    name="PROTRA CAPACITY EXPANSION MAX GROWTH RATE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_max_growth_rate"
    },
)
def protra_capacity_expansion_max_growth_rate():
    """
    exogeneous limit for max. capacity growth per year (expresed in relative terms, capacity-addition per year).
    """
    return _ext_constant_protra_capacity_expansion_max_growth_rate()


_ext_constant_protra_capacity_expansion_max_growth_rate = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["CHINA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_capacity_expansion_max_growth_rate",
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["EASOC"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["EU27"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["INDIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["LATAM"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["LROW"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["RUSSIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["UK"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_capacity_expansion_max_growth_rate.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "capacity_expansion_limits_relative_per_transformation_process*",
    {"REGIONS 9 I": ["USMCA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)


@component.add(
    name="PROTRA INPUT SHARES EMPIRIC",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_input_shares_empiric"},
)
def protra_input_shares_empiric():
    """
    Empiric input fuel shares for the year 2015 (some transformation processes can take more than one fuel, e.g. gas plants can be driven with biogas or fossil gas).
    """
    return _ext_constant_protra_input_shares_empiric()


_ext_constant_protra_input_shares_empiric = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["CHINA"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
    "_ext_constant_protra_input_shares_empiric",
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["EASOC"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["EU27"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["INDIA"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["LATAM"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["LROW"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["UK"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)

_ext_constant_protra_input_shares_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "transformation_input_required_shares_of_process_and_commodity",
    {
        "REGIONS 9 I": ["USMCA"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
)


@component.add(
    name="PROTRA MAX FULL LOAD HOURS",
    units="Hours/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_max_full_load_hours"},
)
def protra_max_full_load_hours():
    """
    operating hours of capacity stock
    """
    return _ext_constant_protra_max_full_load_hours()


_ext_constant_protra_max_full_load_hours = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["CHINA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_max_full_load_hours",
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["EASOC"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["EU27"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["INDIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["LATAM"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["LROW"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["RUSSIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["UK"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_max_full_load_hours.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "IMV_annual_operating_hours_maximum_per_transformation_process*",
    {"REGIONS 9 I": ["USMCA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)


@component.add(
    name="PROTRA UTILIZATION ALLOCATION PRIORITIES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_utilization_allocation_priorities_sp"
    },
)
def protra_utilization_allocation_priorities_sp():
    """
    Exogenous allocation priorities for energy transformation technologies (PROTRA). Note: In Technology Utilization Heat is allcoated first to determin CHP-Utilization (and related electricity production), than electricity is allocated in a second step to all PP technologies.
    """
    return _ext_constant_protra_utilization_allocation_priorities_sp()


_ext_constant_protra_utilization_allocation_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_UTILIZATION_ALLOCATION_PRIORITIES_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_utilization_allocation_priorities_sp",
)


@component.add(
    name="PROTRA UTILIZATION PRIORITIES POLICYWEIGHT SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_utilization_priorities_policyweight_sp"
    },
)
def protra_utilization_priorities_policyweight_sp():
    """
    Weight of the (exogeneous) policy allocation priority. The missing quantity to 1 is the weight of the endogeneous allocation factors. If this parameter = 1 then the endogenous component is omitted.
    """
    return _ext_constant_protra_utilization_priorities_policyweight_sp()


_ext_constant_protra_utilization_priorities_policyweight_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_UTILIZATION_PRIORITIES_POLICYWEIGHT_SP",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_protra_utilization_priorities_policyweight_sp",
)


@component.add(
    name="RT STORAGE EFFICIENCY EV BATTERIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_rt_storage_efficiency_ev_batteries"},
)
def rt_storage_efficiency_ev_batteries():
    """
    Round-trip storage efficiency of electric batteries frome electric vehicles.
    """
    return _ext_constant_rt_storage_efficiency_ev_batteries()


_ext_constant_rt_storage_efficiency_ev_batteries = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Round_trip_storage_efficiency_EV_batteries",
    {},
    _root,
    {},
    "_ext_constant_rt_storage_efficiency_ev_batteries",
)


@component.add(
    name="RT STORAGE EFFICIENCY PHS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_rt_storage_efficiency_phs"},
)
def rt_storage_efficiency_phs():
    """
    Round-trip storage efficiency.
    """
    return _ext_constant_rt_storage_efficiency_phs()


_ext_constant_rt_storage_efficiency_phs = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "World",
    "Round_trip_storage_efficiency_PHS",
    {},
    _root,
    {},
    "_ext_constant_rt_storage_efficiency_phs",
)


@component.add(
    name="SHARE ELEC IN PHEV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_elec_in_phev"},
)
def share_elec_in_phev():
    """
    Share of electricity consumption in PHEV power trains.
    """
    return _ext_constant_share_elec_in_phev()


_ext_constant_share_elec_in_phev = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "SHARE_ELEC_IN_PHEV",
    {},
    _root,
    {},
    "_ext_constant_share_elec_in_phev",
)


@component.add(
    name="SWITCH NRG DYNAMIC EROIst",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_dynamic_eroist"},
)
def switch_nrg_dynamic_eroist():
    """
    This variable activates the computation of the 'static' EROIst by technology: 1. 'Dynamic' EROI calculation (endogenous) 0. 'Static' EROIst calculation: - recycling rate of minerals constant at 2015 levels, - "Take into account of RES variability?"=0, - do not include material requirements for overgrids, - all VRES technologies are considered to be fully dispachtable (so storage is not required)
    """
    return _ext_constant_switch_nrg_dynamic_eroist()


_ext_constant_switch_nrg_dynamic_eroist = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_DYNAMIC_EROIst",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_dynamic_eroist",
)
