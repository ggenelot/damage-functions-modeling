"""
Module constantsexogenous_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="BILLONperson PER MILLONperson units",
    units="Billon persons/Million persons",
    comp_type="Constant",
    comp_subtype="Normal",
)
def billonperson_per_millonperson_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="dollars 2015 per Mdollar 2015",
    units="dollars 2015/Mdollars 2015",
    comp_type="Constant",
    comp_subtype="Normal",
)
def dollars_2015_per_mdollar_2015():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="dollars per dollars 2015",
    units="dollars/dollars 2015",
    comp_type="Constant",
    comp_subtype="Normal",
)
def dollars_per_dollars_2015():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="dollars per Mdollar",
    units="dollars/Mdollars",
    comp_type="Constant",
    comp_subtype="Normal",
)
def dollars_per_mdollar():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="g per kg units", units="g/kg", comp_type="Constant", comp_subtype="Normal"
)
def g_per_kg_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="g per Mt units", units="g/Mt", comp_type="Constant", comp_subtype="Normal"
)
def g_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="g per t units", units="g/t", comp_type="Constant", comp_subtype="Normal"
)
def g_per_t_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="GHG VOLUME TO MASS CONVERSION FACTOR",
    units="Mt/m3",
    subscripts=["GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ghg_volume_to_mass_conversion_factor"},
)
def ghg_volume_to_mass_conversion_factor():
    return _ext_constant_ghg_volume_to_mass_conversion_factor()


_ext_constant_ghg_volume_to_mass_conversion_factor = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MINING",
    "GHG_VOLUME_TO_MASS_CONVERSION_FACTOR*",
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    _root,
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    "_ext_constant_ghg_volume_to_mass_conversion_factor",
)


@component.add(
    name="GJ per EJ units", units="GJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def gj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="GW per TW units", units="GW/TW", comp_type="Constant", comp_subtype="Normal"
)
def gw_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="ha per Mha units", units="ha/MHa", comp_type="Constant", comp_subtype="Normal"
)
def ha_per_mha_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="hours per Mhour",
    units="dollars/Mdollars",
    comp_type="Constant",
    comp_subtype="Normal",
)
def hours_per_mhour():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="INITIAL SIMULATION YEAR",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_simulation_year"},
)
def initial_simulation_year():
    """
    Initial simulation year.
    """
    return _ext_constant_initial_simulation_year()


_ext_constant_initial_simulation_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "INITIAL_SIMULATION_YEAR",
    {},
    _root,
    {},
    "_ext_constant_initial_simulation_year",
)


@component.add(
    name="J per EJ units", units="J/EJ", comp_type="Constant", comp_subtype="Normal"
)
def j_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="J per MJ units", units="J/MJ", comp_type="Constant", comp_subtype="Normal"
)
def j_per_mj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="J per TJ units", units="TJ/J", comp_type="Constant", comp_subtype="Normal"
)
def j_per_tj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kg per Mt units", units="kg/Mt", comp_type="Constant", comp_subtype="Normal"
)
def kg_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km2 per ha units", units="km2/ha", comp_type="Constant", comp_subtype="Normal"
)
def km2_per_ha_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km3 per hm3 units",
    units="km3/hm3",
    comp_type="Constant",
    comp_subtype="Normal",
)
def km3_per_hm3_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="km per m units", units="km/m", comp_type="Constant", comp_subtype="Normal"
)
def km_per_m_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kpeople per people units",
    units="kpeople/people",
    comp_type="Constant",
    comp_subtype="Normal",
)
def kpeople_per_people_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kt per Gt units", units="Kt/Gt", comp_type="Constant", comp_subtype="Normal"
)
def kt_per_gt_units():
    return 1


@component.add(
    name="kW per MW units", units="kW/MW", comp_type="Constant", comp_subtype="Normal"
)
def kw_per_mw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="kWh per TWh units",
    units="kWh/TWh",
    comp_type="Constant",
    comp_subtype="Normal",
)
def kwh_per_twh_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="m2 per km2 units", units="m2/km2", comp_type="Constant", comp_subtype="Normal"
)
def m2_per_km2_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="m per mm units", units="m/mm", comp_type="Constant", comp_subtype="Normal"
)
def m_per_mm_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="MATRIX UNIT PREFIXES",
    units="DMNL",
    subscripts=["UNIT PREFIXES I", "UNIT PREFIXES1 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_matrix_unit_prefixes"},
)
def matrix_unit_prefixes():
    """
    Conversion from Matrix unit prefixes[tera,BASE UNIT] (1 T$ = 1e12 $).
    """
    return _ext_constant_matrix_unit_prefixes()


_ext_constant_matrix_unit_prefixes = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "MATRIX_UNIT_PREFIXES",
    {
        "UNIT PREFIXES I": _subscript_dict["UNIT PREFIXES I"],
        "UNIT PREFIXES1 I": _subscript_dict["UNIT PREFIXES1 I"],
    },
    _root,
    {
        "UNIT PREFIXES I": _subscript_dict["UNIT PREFIXES I"],
        "UNIT PREFIXES1 I": _subscript_dict["UNIT PREFIXES1 I"],
    },
    "_ext_constant_matrix_unit_prefixes",
)


@component.add(
    name="Mdollars per Mdollars 2015",
    units="Mdollars/Mdollars 2015",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mdollars_per_mdollars_2015():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="MJ per EJ units", units="MJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def mj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mm3 per m3 units", units="Mm3/m3", comp_type="Constant", comp_subtype="Normal"
)
def mm3_per_m3_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mt per Bt units", units="Mt/Bt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_bt_units():
    return 1


@component.add(
    name="Mt per Gt units", units="Mt/Gt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_gt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mt per kt units", units="Mt/Kt", comp_type="Constant", comp_subtype="Normal"
)
def mt_per_kt_units():
    return 1


@component.add(
    name="MtCO2eq per GtCO2eq units",
    units="MtCO2eq/GtCO2eq",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mtco2eq_per_gtco2eq_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Mvehicles per vehicles units",
    units="Mvehicles/vehicles",
    comp_type="Constant",
    comp_subtype="Normal",
)
def mvehicles_per_vehicles_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="MW 1 YEAR TO MJ",
    units="MJ/(Year*MW)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mw_1_year_to_mj"},
)
def mw_1_year_to_mj():
    """
    Conversion factor MW in 1 year to MJ.
    """
    return _ext_constant_mw_1_year_to_mj()


_ext_constant_mw_1_year_to_mj = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "MW_in_1_year_to_MJ",
    {},
    _root,
    {},
    "_ext_constant_mw_1_year_to_mj",
)


@component.add(
    name="MW per TW units", units="MW/TW", comp_type="Constant", comp_subtype="Normal"
)
def mw_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="NUMBER OF REGIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_number_of_regions"},
)
def number_of_regions():
    """
    **DO NOT MODIFY THIS PARAMETER** Auxiliary variable to prorate world data to 9 regions weighting equally each one (World/9). Each module should take care of adapting the inputs received from other modules so they are correctly calibrated with historical data. As versions of the model are progressively built, all the variables which are provided by other modules should come endogenously regionalized.
    """
    return _ext_constant_number_of_regions()


_ext_constant_number_of_regions = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "NUMBER_OF_REGIONS",
    {},
    _root,
    {},
    "_ext_constant_number_of_regions",
)


@component.add(
    name="ONE YEAR", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def one_year():
    return 1


@component.add(
    name="PE ENERGY DENSITY MJ kg",
    units="MJ/kg",
    subscripts=["NRG PE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pe_energy_density_mj_kg"},
)
def pe_energy_density_mj_kg():
    """
    Energy density of primary energy sources (commodities). This indicator assumes constant quantities of energy per kilogram of mass.
    """
    return _ext_constant_pe_energy_density_mj_kg()


_ext_constant_pe_energy_density_mj_kg = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "PE_ENERGY_DENSITY_MJ_kg*",
    {"NRG PE I": _subscript_dict["NRG PE I"]},
    _root,
    {"NRG PE I": _subscript_dict["NRG PE I"]},
    "_ext_constant_pe_energy_density_mj_kg",
)


@component.add(
    name="PJ per EJ units", units="PJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def pj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="RADIANS PER ARCDEGREE",
    units="radians/arcdegree",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_radians_per_arcdegree"},
)
def radians_per_arcdegree():
    """
    x PI/180°.
    """
    return _ext_constant_radians_per_arcdegree()


_ext_constant_radians_per_arcdegree = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "RADIANS_PER_ARCDEGREE",
    {},
    _root,
    {},
    "_ext_constant_radians_per_arcdegree",
)


@component.add(
    name="SPECIFIC HEAT CAPACITY WATER",
    units="J/kg/DegreesC",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_specific_heat_capacity_water"},
)
def specific_heat_capacity_water():
    """
    Specific heat of water, i.e., amount of heat in Joules per kg water required to raise the temperature by one degree Celsius.
    """
    return _ext_constant_specific_heat_capacity_water()


_ext_constant_specific_heat_capacity_water = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "SPECIFIC_HEAT_CAPACITY_WATER",
    {},
    _root,
    {},
    "_ext_constant_specific_heat_capacity_water",
)


@component.add(
    name="t per Gt units", units="t/Gt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_gt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="t per kg units", units="t/kg", comp_type="Constant", comp_subtype="Normal"
)
def t_per_kg_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="t per kt units", units="t/Kt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_kt_units():
    return 1


@component.add(
    name="t per Mt units", units="t/Mt", comp_type="Constant", comp_subtype="Normal"
)
def t_per_mt_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="tCO2eq per GtCO2eq units",
    units="tCO2eq/GtCO2eq",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tco2eq_per_gtco2eq_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="tCO2eq per MtCO2eq",
    units="tCO2eq/MtCO2eq",
    comp_type="Constant",
    comp_subtype="Normal",
)
def tco2eq_per_mtco2eq():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TJ per EJ units", units="TJ/EJ", comp_type="Constant", comp_subtype="Normal"
)
def tj_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TJ per MJ units", units="TJ/MJ", comp_type="Constant", comp_subtype="Normal"
)
def tj_per_mj_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TW per kW units", units="TW/kW", comp_type="Constant", comp_subtype="Normal"
)
def tw_per_kw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="TWh per EJ units", units="TWh/EJ", comp_type="Constant", comp_subtype="Normal"
)
def twh_per_ej_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="UNIT CONVERISON Wh kWh",
    units="w*h/(kW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "wh_per_kwh_units": 1},
)
def unit_converison_wh_kwh():
    """
    Unit conversion Wh per kWh.
    """
    return float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"]) * wh_per_kwh_units()


@component.add(
    name="UNIT CONVERSION C CO2",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_c_co2"},
)
def unit_conversion_c_co2():
    """
    1 g of CO2 contains 3/11 of carbon.
    """
    return _ext_constant_unit_conversion_c_co2()


_ext_constant_unit_conversion_c_co2 = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_C_CO2",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_c_co2",
)


@component.add(
    name="UNIT CONVERSION CH4 C",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ch4_c"},
)
def unit_conversion_ch4_c():
    """
    Molar mass ratio of CH4 to C, 16/12
    """
    return _ext_constant_unit_conversion_ch4_c()


_ext_constant_unit_conversion_ch4_c = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_CH4_C",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ch4_c",
)


@component.add(
    name="UNIT CONVERSION DAYS YEAR",
    units="days/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_days_year"},
)
def unit_conversion_days_year():
    """
    Constant: 365 days in a year.
    """
    return _ext_constant_unit_conversion_days_year()


_ext_constant_unit_conversion_days_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_DAYS_YEAR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_days_year",
)


@component.add(
    name="UNIT CONVERSION dollars 2015 Mdollars 2015",
    units="dollars 2015/Mdollars 2015",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "dollars_2015_per_mdollar_2015": 1},
)
def unit_conversion_dollars_2015_mdollars_2015():
    """
    Unit conversion dollars per Mdollar.
    """
    return (
        float(matrix_unit_prefixes().loc["mega", "BASE UNIT"])
        * dollars_2015_per_mdollar_2015()
    )


@component.add(
    name="UNIT CONVERSION dollars Mdollars",
    units="dollars/Mdollars",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "dollars_per_mdollar": 1},
)
def unit_conversion_dollars_mdollars():
    """
    Unit conversion dollars per Mdollar.
    """
    return (
        float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * dollars_per_mdollar()
    )


@component.add(
    name="UNIT CONVERSION g kg",
    units="g/kg",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "g_per_kg_units": 1},
)
def unit_conversion_g_kg():
    """
    Unit conversion g per kg.
    """
    return float(matrix_unit_prefixes().loc["mega", "kilo"]) * g_per_kg_units()


@component.add(
    name="UNIT CONVERSION g Mt",
    units="g/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "g_per_mt_units": 1},
)
def unit_conversion_g_mt():
    """
    Unit conversion g per Mt.
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE UNIT"]) * g_per_mt_units()


@component.add(
    name="UNIT CONVERSION g t",
    units="g/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "g_per_t_units": 1},
)
def unit_conversion_g_t():
    """
    Unit conversion g per t
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * g_per_t_units()


@component.add(
    name="UNIT CONVERSION GJ EJ",
    units="GJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "gj_per_ej_units": 1},
)
def unit_conversion_gj_ej():
    """
    Unit conversion GJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "giga"]) * gj_per_ej_units()


@component.add(
    name="UNIT CONVERSION GtC ppm",
    units="Gt/ppm",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_gtc_ppm"},
)
def unit_conversion_gtc_ppm():
    """
    Conversion from ppm to GtC (1 ppm by volume of atmosphere CO2 = 2.13 Gt C (Uses atmospheric mass (Ma) = 5.137 × 10^18 kg)) CDIAC: http://cdiac.ornl.gov/pns/convert.html
    """
    return _ext_constant_unit_conversion_gtc_ppm()


_ext_constant_unit_conversion_gtc_ppm = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_GtC_ppm",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_gtc_ppm",
)


@component.add(
    name="UNIT CONVERSION GtCO2eq MtCO2eq",
    units="MtCO2eq/GtCO2eq",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mtco2eq_per_gtco2eq_units": 1},
)
def unit_conversion_gtco2eq_mtco2eq():
    """
    Unit conversion MCO2eq per GtCO2eq.
    """
    return (
        float(matrix_unit_prefixes().loc["giga", "mega"]) * mtco2eq_per_gtco2eq_units()
    )


@component.add(
    name="UNIT CONVERSION GW TW",
    units="GW/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "gw_per_tw_units": 1},
)
def unit_conversion_gw_tw():
    """
    Unit conversion GW per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "giga"]) * gw_per_tw_units()


@component.add(
    name="UNIT CONVERSION ha Mha",
    units="ha/MHa",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "ha_per_mha_units": 1},
)
def unit_conversion_ha_mha():
    """
    Unit conversion ha per MHa.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * ha_per_mha_units()


@component.add(
    name="UNIT CONVERSION hours Mhours",
    units="Hours/Mhours",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "hours_per_mhour": 1},
)
def unit_conversion_hours_mhours():
    """
    Unit conversion hours per Mhour.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * hours_per_mhour()


@component.add(
    name="UNIT CONVERSION HOURS YEAR",
    units="h/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_hours_year"},
)
def unit_conversion_hours_year():
    """
    Constant: 8760 hours in a year.
    """
    return _ext_constant_unit_conversion_hours_year()


_ext_constant_unit_conversion_hours_year = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_HOURS_YEAR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_hours_year",
)


@component.add(
    name="UNIT CONVERSION J boe",
    units="J/boe",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_boe"},
)
def unit_conversion_j_boe():
    """
    Constant: 5711869031,31802 jules in a barrel of oil equivalent.
    """
    return _ext_constant_unit_conversion_j_boe()


_ext_constant_unit_conversion_j_boe = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_boe",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_boe",
)


@component.add(
    name="UNIT CONVERSION J EJ",
    units="J/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_ej_units": 1},
)
def unit_conversion_j_ej():
    """
    Unit conversion J per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "BASE UNIT"]) * j_per_ej_units()


@component.add(
    name="UNIT CONVERSION J MJ",
    units="J/MJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_mj_units": 1},
)
def unit_conversion_j_mj():
    """
    Unit conversion J per MJ.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * j_per_mj_units()


@component.add(
    name="UNIT CONVERSION J TJ",
    units="TJ/J",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "j_per_tj_units": 1},
)
def unit_conversion_j_tj():
    """
    Unit conversion J per TJ
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE UNIT"]) * j_per_tj_units()


@component.add(
    name="UNIT CONVERSION J toe",
    units="J/toe",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_toe"},
)
def unit_conversion_j_toe():
    """
    Constant: 41867999999,5611 jules in a tonne of oil equivalent.
    """
    return _ext_constant_unit_conversion_j_toe()


_ext_constant_unit_conversion_j_toe = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_toe",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_toe",
)


@component.add(
    name="UNIT CONVERSION J Wh",
    units="J/(w*h)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_wh"},
)
def unit_conversion_j_wh():
    """
    Constant: 3600 joules per watt hour.
    """
    return _ext_constant_unit_conversion_j_wh()


_ext_constant_unit_conversion_j_wh = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_Wh",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_wh",
)


@component.add(
    name="UNIT CONVERSION kg Mt",
    units="kg/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kg_per_mt_units": 1},
)
def unit_conversion_kg_mt():
    """
    Unit conversion kg per Mt
    """
    return float(matrix_unit_prefixes().loc["tera", "kilo"]) * kg_per_mt_units()


@component.add(
    name="UNIT CONVERSION km2 ha",
    units="km2/ha",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km2_per_ha_units": 1},
)
def unit_conversion_km2_ha():
    """
    Unit conversion ha per km2
    """
    return float(matrix_unit_prefixes().loc["centi", "BASE UNIT"]) * km2_per_ha_units()


@component.add(
    name="UNIT CONVERSION km3 hm3",
    units="km3/hm3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km3_per_hm3_units": 1},
)
def unit_conversion_km3_hm3():
    """
    Unit conversion km3 per hm3.
    """
    return float(matrix_unit_prefixes().loc["hecto", "kilo"]) ** 3 * km3_per_hm3_units()


@component.add(
    name="UNIT CONVERSION km m",
    units="km/m",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "km_per_m_units": 1},
)
def unit_conversion_km_m():
    """
    Unit conversion km per m.
    """
    return float(matrix_unit_prefixes().loc["BASE UNIT", "kilo"]) * km_per_m_units()


@component.add(
    name="UNIT CONVERSION KPEOPLE PEOPLE",
    units="kpeople/people",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kpeople_per_people_units": 1},
)
def unit_conversion_kpeople_people():
    """
    Conversion unit for demography to fertility (births/1000people) and mortality rates (deaths/1000people)
    """
    return (
        float(matrix_unit_prefixes().loc["BASE UNIT", "kilo"])
        * kpeople_per_people_units()
    )


@component.add(
    name="UNIT CONVERSION kt Gt",
    units="Kt/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kt_per_gt_units": 1},
)
def unit_conversion_kt_gt():
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * kt_per_gt_units()


@component.add(
    name="UNIT CONVERSION kt URANIUM EJ",
    units="Kt/EJ",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_kt_uranium_ej"},
)
def unit_conversion_kt_uranium_ej():
    """
    Unit conversion (1 EJ thermal = 2.3866). See EWG (2006).
    """
    return _ext_constant_unit_conversion_kt_uranium_ej()


_ext_constant_unit_conversion_kt_uranium_ej = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_kt_URANIUM_EJ",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_kt_uranium_ej",
)


@component.add(
    name="UNIT CONVERSION kW MW",
    units="kW/MW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kw_per_mw_units": 1},
)
def unit_conversion_kw_mw():
    """
    Unit conversion kW per MW.
    """
    return float(matrix_unit_prefixes().loc["mega", "kilo"]) * kw_per_mw_units()


@component.add(
    name="UNIT CONVERSION kWh TWh",
    units="kW*h/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "kwh_per_twh_units": 1},
)
def unit_conversion_kwh_twh():
    """
    Unit conversion kWh per TWh.
    """
    return float(matrix_unit_prefixes().loc["tera", "kilo"]) * kwh_per_twh_units()


@component.add(
    name="UNIT CONVERSION m2 km2",
    units="m2/km2",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "m2_per_km2_units": 1},
)
def unit_conversion_m2_km2():
    """
    Unit conversion m2 per km2.
    """
    return (
        float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"]) ** 2 * m2_per_km2_units()
    )


@component.add(
    name="UNIT CONVERSION m mm",
    units="m/mm",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "m_per_mm_units": 1},
)
def unit_conversion_m_mm():
    return float(matrix_unit_prefixes().loc["BASE UNIT", "kilo"]) * m_per_mm_units()


@component.add(
    name="UNIT CONVERSION MILLION BILLION",
    units="Million persons/Billon persons",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "billonperson_per_millonperson_units": 1},
)
def unit_conversion_million_billion():
    """
    Converting from billion people to billion people.
    """
    return (
        float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"])
        * billonperson_per_millonperson_units()
    )


@component.add(
    name="UNIT CONVERSION MJ EJ",
    units="MJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mj_per_ej_units": 1},
)
def unit_conversion_mj_ej():
    """
    Unit conversion MJ per EJ
    """
    return float(matrix_unit_prefixes().loc["exa", "mega"]) * mj_per_ej_units()


@component.add(
    name="UNIT CONVERSION Mm3 m3",
    units="Mm3/m3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mm3_per_m3_units": 1},
)
def unit_conversion_mm3_m3():
    """
    Unit conversion Mm3 per m3.
    """
    return float(matrix_unit_prefixes().loc["BASE UNIT", "mega"]) * mm3_per_m3_units()


@component.add(
    name="UNIT CONVERSION Mt Bt",
    units="Mt/Bt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_bt_units": 1},
)
def unit_conversion_mt_bt():
    return float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"]) * mt_per_bt_units()


@component.add(
    name="UNIT CONVERSION Mt Gt",
    units="Mt/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_gt_units": 1},
)
def unit_conversion_mt_gt():
    """
    Unit conversion Mt per Gt
    """
    return float(matrix_unit_prefixes().loc["giga", "mega"]) * mt_per_gt_units()


@component.add(
    name="UNIT CONVERSION Mt kt",
    units="Mt/Kt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mt_per_kt_units": 1},
)
def unit_conversion_mt_kt():
    """
    Unit conversion Mt per kt.
    """
    return float(matrix_unit_prefixes().loc["kilo", "mega"]) * mt_per_kt_units()


@component.add(
    name="UNIT CONVERSION Mt t",
    units="Mt/t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"unit_conversion_t_mt": 1},
)
def unit_conversion_mt_t():
    """
    ton to mega ton
    """
    return 1 / unit_conversion_t_mt()


@component.add(
    name="UNIT CONVERSION Mvehicles vehicles",
    units="Mvehicles/vehicles",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mvehicles_per_vehicles_units": 1},
)
def unit_conversion_mvehicles_vehicles():
    """
    Unit conversion Mvehicles per vehicles
    """
    return (
        float(matrix_unit_prefixes().loc["BASE UNIT", "mega"])
        * mvehicles_per_vehicles_units()
    )


@component.add(
    name="UNIT CONVERSION MW TW",
    units="MW/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "mw_per_tw_units": 1},
)
def unit_conversion_mw_tw():
    """
    Unit conversion MW per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "mega"]) * mw_per_tw_units()


@component.add(
    name="UNIT CONVERSION N2ON N2O",
    units="N2O/N2ON",
    comp_type="Constant",
    comp_subtype="Normal",
)
def unit_conversion_n2on_n2o():
    """
    N2O-N_TO_N2O N2O = N2O-N ? 44/28 (IPCC)
    """
    return 44 / 28


@component.add(
    name="UNIT CONVERSION PERCENT SHARE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_percent_share"},
)
def unit_conversion_percent_share():
    """
    Conversion of percent to share.
    """
    return _ext_constant_unit_conversion_percent_share()


_ext_constant_unit_conversion_percent_share = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_PERCENT_SHARE",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_percent_share",
)


@component.add(
    name="UNIT CONVERSION PJ EJ",
    units="PJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "pj_per_ej_units": 1},
)
def unit_conversion_pj_ej():
    """
    Unit conversion PJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "peta"]) * pj_per_ej_units()


@component.add(
    name="UNIT CONVERSION ppt MOL",
    units="ppt/mol",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ppt_mol"},
)
def unit_conversion_ppt_mol():
    """
    Parts per trillion per mol.
    """
    return _ext_constant_unit_conversion_ppt_mol()


_ext_constant_unit_conversion_ppt_mol = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_ppt_MOL",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ppt_mol",
)


@component.add(
    name="UNIT CONVERSION ppt ppb",
    units="ppt/ppb",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_ppt_ppb"},
)
def unit_conversion_ppt_ppb():
    """
    Parts-per-trillion per parts-per-billion.
    """
    return _ext_constant_unit_conversion_ppt_ppb()


_ext_constant_unit_conversion_ppt_ppb = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_ppt_ppb",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_ppt_ppb",
)


@component.add(
    name="UNIT CONVERSION SECONDS DAY",
    units="s/day",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_seconds_day"},
)
def unit_conversion_seconds_day():
    """
    Constant: 86400 seconds in a day.
    """
    return _ext_constant_unit_conversion_seconds_day()


_ext_constant_unit_conversion_seconds_day = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_SECONDS_DAY",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_seconds_day",
)


@component.add(
    name="UNIT CONVERSION SECONDS HOUR",
    units="s/Hours",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_seconds_hour"},
)
def unit_conversion_seconds_hour():
    """
    Constant: 3600 seconds in a hour.
    """
    return _ext_constant_unit_conversion_seconds_hour()


_ext_constant_unit_conversion_seconds_hour = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_SECONDS_HOUR",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_seconds_hour",
)


@component.add(
    name="UNIT CONVERSION t Gt",
    units="t/Gt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_gt_units": 1},
)
def unit_conversion_t_gt():
    """
    Unit conversion t per Gt
    """
    return float(matrix_unit_prefixes().loc["giga", "BASE UNIT"]) * t_per_gt_units()


@component.add(
    name="UNIT CONVERSION t kg",
    units="t/kg",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_kg_units": 1},
)
def unit_conversion_t_kg():
    """
    Unit conversion t per kg.
    """
    return float(matrix_unit_prefixes().loc["kilo", "mega"]) * t_per_kg_units()


@component.add(
    name="UNIT CONVERSION t kt",
    units="t/Kt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_kt_units": 1},
)
def unit_conversion_t_kt():
    return float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"]) * t_per_kt_units()


@component.add(
    name="UNIT CONVERSION t Mt",
    units="t/Mt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "t_per_mt_units": 1},
)
def unit_conversion_t_mt():
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * t_per_mt_units()


@component.add(
    name="UNIT CONVERSION tCO2eq GtCO2eq",
    units="tCO2eq/GtCO2eq",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tco2eq_per_gtco2eq_units": 1},
)
def unit_conversion_tco2eq_gtco2eq():
    """
    Unit conversion tCO2eq per GtCO2eq.
    """
    return (
        float(matrix_unit_prefixes().loc["giga", "BASE UNIT"])
        * tco2eq_per_gtco2eq_units()
    )


@component.add(
    name="UNIT CONVERSION tCO2eq MtCO2eq",
    units="tCO2eq/MtCO2eq",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tco2eq_per_mtco2eq": 1},
)
def unit_conversion_tco2eq_mtco2eq():
    """
    Unit conversion tCO2eq per MtCO2eq.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * tco2eq_per_mtco2eq()


@component.add(
    name="UNIT CONVERSION TJ EJ",
    units="TJ/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tj_per_ej_units": 1},
)
def unit_conversion_tj_ej():
    """
    Unit conversion TJ per EJ.
    """
    return float(matrix_unit_prefixes().loc["exa", "tera"]) * tj_per_ej_units()


@component.add(
    name="UNIT CONVERSION TJ MJ",
    units="TJ/MJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tj_per_mj_units": 1},
)
def unit_conversion_tj_mj():
    """
    Unit conversion TJ per MJ.
    """
    return float(matrix_unit_prefixes().loc["mega", "tera"]) * tj_per_mj_units()


@component.add(
    name="UNIT CONVERSION toe m3",
    units="toe/m3",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_toe_m3"},
)
def unit_conversion_toe_m3():
    return _ext_constant_unit_conversion_toe_m3()


_ext_constant_unit_conversion_toe_m3 = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_toe_m3",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_toe_m3",
)


@component.add(
    name="UNIT CONVERSION TW kW",
    units="TW/kW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "tw_per_kw_units": 1},
)
def unit_conversion_tw_kw():
    """
    Unit conversion TW per kW.
    """
    return float(matrix_unit_prefixes().loc["kilo", "tera"]) * tw_per_kw_units()


@component.add(
    name="UNIT CONVERSION TW PER EJ PER YEAR",
    units="EJ/(TW*h)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "unit_conversion_j_wh": 1,
        "unit_conversion_w_tw": 1,
        "unit_conversion_j_ej": 1,
    },
)
def unit_conversion_tw_per_ej_per_year():
    return unit_conversion_j_wh() * unit_conversion_w_tw() / unit_conversion_j_ej()


@component.add(
    name="UNIT CONVERSION TWh EJ",
    units="TWh/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"twh_per_ej_units": 1, "matrix_unit_prefixes": 1},
)
def unit_conversion_twh_ej():
    """
    1 EJ = 1 EJ * (10^6 TJ) * (second/second) = 10^6 TW * s * (1 hour / 3600 seconds) = TWh
    """
    return twh_per_ej_units() * float(matrix_unit_prefixes().loc["exa", "tera"]) / 3600


@component.add(
    name="UNIT CONVERSION W J s",
    units="w/(J/s)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_w_j_s"},
)
def unit_conversion_w_j_s():
    """
    Constant: 1 watt in a jules/second.
    """
    return _ext_constant_unit_conversion_w_j_s()


_ext_constant_unit_conversion_w_j_s = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "UNIT_CONVERSION_W_J_s",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_w_j_s",
)


@component.add(
    name="UNIT CONVERSION W kW",
    units="w/kW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_kw_units": 1},
)
def unit_conversion_w_kw():
    """
    Unit conversion W per kW.
    """
    return float(matrix_unit_prefixes().loc["kilo", "BASE UNIT"]) * w_per_kw_units()


@component.add(
    name="UNIT CONVERSION W MW",
    units="w/MW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_mw_units": 1},
)
def unit_conversion_w_mw():
    """
    Unit conversion W per MW.
    """
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * w_per_mw_units()


@component.add(
    name="UNIT CONVERSION W TW",
    units="w/TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "w_per_tw_units": 1},
)
def unit_conversion_w_tw():
    """
    Unit conversion W per TW.
    """
    return float(matrix_unit_prefixes().loc["tera", "BASE UNIT"]) * w_per_tw_units()


@component.add(
    name="UNIT CONVERSION Wh MWh",
    units="w*h/MW/h",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"matrix_unit_prefixes": 1, "wh_per_mwh_units": 1},
)
def unit_conversion_wh_mwh():
    return float(matrix_unit_prefixes().loc["mega", "BASE UNIT"]) * wh_per_mwh_units()


@component.add(
    name="UNIT CONVERSION Wh We",
    units="Wh/We",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_wh_we"},
)
def unit_conversion_wh_we():
    """
    Constant: 8760 watt hour in a electric watt.
    """
    return _ext_constant_unit_conversion_wh_we()


_ext_constant_unit_conversion_wh_we = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_Wh_We",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_wh_we",
)


@component.add(
    name="W per kW units", units="w/kW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_kw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="W per MW units", units="w/TW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_mw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="W per TW units", units="w/TW", comp_type="Constant", comp_subtype="Normal"
)
def w_per_tw_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="WATER DENSITY",
    units="kg/(m*m*m)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_water_density"},
)
def water_density():
    """
    Density of water, i.e., mass per volume of water.
    """
    return _ext_constant_water_density()


_ext_constant_water_density = ExtConstant(
    "model_parameters/constants.xlsx",
    "constants",
    "WATER_DENSITY",
    {},
    _root,
    {},
    "_ext_constant_water_density",
)


@component.add(
    name="Wh per kWh units", units="Wh/kWh", comp_type="Constant", comp_subtype="Normal"
)
def wh_per_kwh_units():
    """
    Units for unit conversion.
    """
    return 1


@component.add(
    name="Wh per MWh units",
    units="w*h/MW*h",
    comp_type="Constant",
    comp_subtype="Normal",
)
def wh_per_mwh_units():
    return 1
