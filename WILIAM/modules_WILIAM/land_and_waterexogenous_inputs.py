"""
Module land_and_waterexogenous_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="AGROFOOD TRANSFORM MATRIX",
    units="DMNL",
    subscripts=["FOODS I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_agrofood_transform_matrix"},
)
def agrofood_transform_matrix():
    """
    Agrofood matrix to convert diet patterns to land products
    """
    return _ext_constant_agrofood_transform_matrix()


_ext_constant_agrofood_transform_matrix = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "AGROFOOD_TRANSFORM_MATRIX",
    {
        "FOODS I": _subscript_dict["FOODS I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "FOODS I": _subscript_dict["FOODS I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_agrofood_transform_matrix",
)


@component.add(
    name="BASELINE DIET PATTERN OF POLICY DIETS SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_baseline_diet_pattern_of_policy_diets_sp"
    },
)
def baseline_diet_pattern_of_policy_diets_sp():
    """
    Baseline policy diet
    """
    return _ext_constant_baseline_diet_pattern_of_policy_diets_sp()


_ext_constant_baseline_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "BASELINE_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_baseline_diet_pattern_of_policy_diets_sp",
)


@component.add(
    name="CARBON FRACTION OF DRY MATTER FOREST",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_carbon_fraction_of_dry_matter_forest"},
)
def carbon_fraction_of_dry_matter_forest():
    """
    carbon fraction of dry matter forest
    """
    return _ext_constant_carbon_fraction_of_dry_matter_forest()


_ext_constant_carbon_fraction_of_dry_matter_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "CARBON_FRACTION_OF_DRY_MATTER_FOREST*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_carbon_fraction_of_dry_matter_forest",
)


@component.add(
    name="CHECK EXOGENOUS LAND USE DEMANDS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_check_exogenous_land_use_demands"},
)
def check_exogenous_land_use_demands():
    """
    Exogenous values of land use changes demanded, used only when the SWITCH_LAW_EXOGENOUS_LAND_USE_DEMANDS =0
    """
    return _ext_constant_check_exogenous_land_use_demands()


_ext_constant_check_exogenous_land_use_demands = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "EXOGENOUS_LAND_USE_DEMANDS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_check_exogenous_land_use_demands",
)


@component.add(
    name="CHEMICAL FERTILIZERS PER CROPLAND AREA",
    units="t/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_chemical_fertilizers_per_cropland_area"},
)
def chemical_fertilizers_per_cropland_area():
    """
    chemical fertilizers used per area
    """
    return _ext_constant_chemical_fertilizers_per_cropland_area()


_ext_constant_chemical_fertilizers_per_cropland_area = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "CHEMICAL_FERTILIZERS_PER_CROPLAND_AREA",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_chemical_fertilizers_per_cropland_area",
)


@component.add(
    name="COEFFICIENT MAX STOCK PRIMARY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_max_stock_primary"},
)
def coefficient_max_stock_primary():
    """
    PERCENT OF THE maximum stock per area that primary forest have once substracted natural disturbance
    """
    return _ext_constant_coefficient_max_stock_primary()


_ext_constant_coefficient_max_stock_primary = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "COEFFICIENT_MAX_STOCK_PRIMARY",
    {},
    _root,
    {},
    "_ext_constant_coefficient_max_stock_primary",
)


@component.add(
    name="COEFFICIENT OF FOREST DISTRURBANCE",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_of_forest_distrurbance"},
)
def coefficient_of_forest_distrurbance():
    """
    coefficient of loss of forest stock due to natural causes with no human intervention
    """
    return _ext_constant_coefficient_of_forest_distrurbance()


_ext_constant_coefficient_of_forest_distrurbance = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "COEFFICIENT_OF_FOREST_DISTRURBANCE*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_coefficient_of_forest_distrurbance",
)


@component.add(
    name="COEFFICIENT OF GROWTH FOREST MANAGED",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_of_growth_forest_managed"},
)
def coefficient_of_growth_forest_managed():
    """
    annual growth rate of forest stocks coefficient 1 GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'forest' , 'ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_1*' )
    """
    return _ext_constant_coefficient_of_growth_forest_managed()


_ext_constant_coefficient_of_growth_forest_managed = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "COEFFICIENT_OF_GROWTH_FOREST_MANAGED*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_coefficient_of_growth_forest_managed",
)


@component.add(
    name="COEFFICIENT OF GROWTH FOREST PLANTATIONS",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_coefficient_of_growth_forest_plantations"
    },
)
def coefficient_of_growth_forest_plantations():
    """
    annual growth rate of forest stocks coefficient 0 GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water.xlsx', 'forest' , 'ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_0*' )
    """
    return _ext_constant_coefficient_of_growth_forest_plantations()


_ext_constant_coefficient_of_growth_forest_plantations = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ANNUAL_GROWTH_RATE_OF_FOREST_STOCKS_COEFFICIENT_0*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_coefficient_of_growth_forest_plantations",
)


@component.add(
    name="COEFFICIENT OF GROWTH FOREST PRIMARY",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_coefficient_of_growth_forest_primary"},
)
def coefficient_of_growth_forest_primary():
    """
    annual growth rate of forest primary
    """
    return _ext_constant_coefficient_of_growth_forest_primary()


_ext_constant_coefficient_of_growth_forest_primary = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "COEFFICIENT_OF_GROWTH_FOREST_PRIMARY*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_coefficient_of_growth_forest_primary",
)


@component.add(
    name="CONTROL PARAMETER OF LAND USE CHANGES",
    units="1/Year",
    subscripts=["LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_control_parameter_of_land_use_changes"},
)
def control_parameter_of_land_use_changes():
    """
    Constant of the proprotional control of the feedback loop of land changes drive by shortage. It is multiplied by the initial value of land uses in order to be proportional to the land area of each region and to the PRIORITIES OF LAND USE CHANGE to speed up those uses with highest priority.
    """
    return _ext_constant_control_parameter_of_land_use_changes()


_ext_constant_control_parameter_of_land_use_changes = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "CONTROL_PARAMETER_OF_LAND_USE_CHANGES",
    {"LANDS I": _subscript_dict["LANDS I"]},
    _root,
    {"LANDS I": _subscript_dict["LANDS I"]},
    "_ext_constant_control_parameter_of_land_use_changes",
)


@component.add(
    name="DELAY TIME LANDUSE TO LANDUSE2 SOIL",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_delay_time_landuse_to_landuse2_soil"},
)
def delay_time_landuse_to_landuse2_soil():
    """
    Time period to reach equilibrium of the soil carbon stock when grassland is changed to cropland. Source: IPPC Guidelines 2006 A value of 20 for the time period of equilibrimm corresponds to a delay time (for the delay function) of 5 years.If the value is of 0 the emissions are produced instantaenosly (inmediate)--> time period of equilibrium of 1 year
    """
    return _ext_constant_delay_time_landuse_to_landuse2_soil()


_ext_constant_delay_time_landuse_to_landuse2_soil = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DELAY_TIME_LANDUSE_TO_LANDUSE2_SOIL",
    {},
    _root,
    {},
    "_ext_constant_delay_time_landuse_to_landuse2_soil",
)


@component.add(
    name="DELAY TIME SOIL EMISSIONS MANAGEMENT",
    units="Years",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_delay_time_soil_emissions_management"},
)
def delay_time_soil_emissions_management():
    """
    Time to reach equilibrium of soil carbon stock equal to 20 years (by default, provided by IPCC 2006 guidelines this is the time dependence of the stock change factors). This corresponds to a constant time/delay time (first order) of 20/4 = 5 years.
    """
    return _ext_constant_delay_time_soil_emissions_management()


_ext_constant_delay_time_soil_emissions_management = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DELAY_TIME_SOIL_EMISSIONS_MANAGEMENT",
    {},
    _root,
    {},
    "_ext_constant_delay_time_soil_emissions_management",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR CHINA",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
    },
)
def diet_patterns_data_by_gdppc_for_china(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP China
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_china(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_china = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_CHINA",
    "DIET_PATTERNS_CHINA",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_china",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR EASOC",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
    },
)
def diet_patterns_data_by_gdppc_for_easoc(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP EASOC
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_easoc(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_easoc = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_EASOC",
    "DIET_PATTERNS_EASOC",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_easoc",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR EU",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
    },
)
def diet_patterns_data_by_gdppc_for_eu(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP EU
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_eu(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_eu = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_EU",
    "DIET_PATTERNS_EU",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_eu",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR INDIA",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
    },
)
def diet_patterns_data_by_gdppc_for_india(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP India
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_india(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_india = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_INDIA",
    "DIET_PATTERNS_INDIA",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_india",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR LATAM",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
    },
)
def diet_patterns_data_by_gdppc_for_latam(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP LATAM
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_latam(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_latam = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_LATAM",
    "DIET_PATTERNS_LATAM",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_latam",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR LROW",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
    },
)
def diet_patterns_data_by_gdppc_for_lrow(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP ROW
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_lrow(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_lrow = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_LROW",
    "DIET_PATTERNS_LROW",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_lrow",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR RUSSIA",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
    },
)
def diet_patterns_data_by_gdppc_for_russia(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP Russia
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_russia(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_russia = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_RUSSIA",
    "DIET_PATTERNS_RUSSIA",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_russia",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR UK",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
    },
)
def diet_patterns_data_by_gdppc_for_uk(x, final_subs=None):
    """
    Historical patterns of diet evolution with GDP UK
    """
    return _ext_lookup_diet_patterns_data_by_gdppc_for_uk(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_uk = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_UK",
    "DIET_PATTERNS_UK",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_uk",
)


@component.add(
    name="DIET PATTERNS DATA BY GDPpc FOR USMCA",
    units="kg/(Year*people)",
    subscripts=["FOODS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
        "__lookup__": "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
    },
)
def diet_patterns_data_by_gdppc_for_usmca(x, final_subs=None):
    return _ext_lookup_diet_patterns_data_by_gdppc_for_usmca(x, final_subs)


_ext_lookup_diet_patterns_data_by_gdppc_for_usmca = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "GDPpc_USMCA",
    "DIET_PATTERNS_USMCA",
    {"FOODS I": _subscript_dict["FOODS I"]},
    _root,
    {"FOODS I": _subscript_dict["FOODS I"]},
    "_ext_lookup_diet_patterns_data_by_gdppc_for_usmca",
)


@component.add(
    name="EFFECT OF IRRIGATION ON YIELDS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_irrigation_on_yields"},
)
def effect_of_irrigation_on_yields():
    """
    Effect of irrigation of crop yields, MapSpam data
    """
    return _ext_constant_effect_of_irrigation_on_yields()


_ext_constant_effect_of_irrigation_on_yields = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_IRRIGATION_ON_YIELDS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_effect_of_irrigation_on_yields",
)


@component.add(
    name="EFFECT OF LOW INPUT AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_low_input_agriculture"},
)
def effect_of_low_input_agriculture():
    """
    Factor to estimated the yields of low input agricultura compared to industrial ones
    """
    return _ext_constant_effect_of_low_input_agriculture()


_ext_constant_effect_of_low_input_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_LOW_INPUT_ON_YIELDS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_effect_of_low_input_agriculture",
)


@component.add(
    name="EFFECT OF REGENERATIVE AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_effect_of_regenerative_agriculture"},
)
def effect_of_regenerative_agriculture():
    """
    Factor to estimated the yields of regenerative agricultura compared to industrial ones
    """
    return _ext_constant_effect_of_regenerative_agriculture()


_ext_constant_effect_of_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "EFFECT_OF_REGENERATIVE_ON_YIELDS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_effect_of_regenerative_agriculture",
)


@component.add(
    name="EFFECTIVE PERCENT OF LAND CHANGE PER METER OF SEA LEVEL RISE",
    units="ha/m",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise"
    },
)
def effective_percent_of_land_change_per_meter_of_sea_level_rise():
    """
    the effective percent of land change per meter of sea level rise
    """
    return _ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise()


_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise = (
    ExtConstant(
        "model_parameters/land_and_water/land_and_water.xlsx",
        "land_uses",
        "LOST_CROPLAND*",
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        _root,
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        "_ext_constant_effective_percent_of_land_change_per_meter_of_sea_level_rise",
    )
)


@component.add(
    name="ENERGY TO LAND PRODUCTS CONVERSION FACTOR",
    units="EJ/t",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_energy_to_land_products_conversion_factor"
    },
)
def energy_to_land_products_conversion_factor():
    """
    conversion factor (from EJ to tonnes )
    """
    return _ext_constant_energy_to_land_products_conversion_factor()


_ext_constant_energy_to_land_products_conversion_factor = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "ENERGY_TO_LAND_PRODUCTS_CONVERSION_FACTOR",
    {},
    _root,
    {},
    "_ext_constant_energy_to_land_products_conversion_factor",
)


@component.add(
    name="ENERGY TO WOOD CONVERSION FACTOR",
    units="EJ/t",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_energy_to_wood_conversion_factor"},
)
def energy_to_wood_conversion_factor():
    """
    conversion factor (from TJ to tonnes or from tonnes to TJ)
    """
    return _ext_constant_energy_to_wood_conversion_factor()


_ext_constant_energy_to_wood_conversion_factor = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "ENERGY_TO_WOOD_CONVERSION_FACTOR*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_energy_to_wood_conversion_factor",
)


@component.add(
    name="EXO EXOGENOUS GDPpc 9R",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_exogenous_gdppc_9r",
        "__lookup__": "_ext_lookup_exo_exogenous_gdppc_9r",
    },
)
def exo_exogenous_gdppc_9r(x, final_subs=None):
    """
    GDPpc real constant values for 9 regions
    """
    return _ext_lookup_exo_exogenous_gdppc_9r(x, final_subs)


_ext_lookup_exo_exogenous_gdppc_9r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_GDPPC",
    "EXOGENOUS_GDPPC_CONSTANT",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_exogenous_gdppc_9r",
)


@component.add(
    name="EXO LAND FOR SOLAR DEMANDED",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_land_for_solar_demanded",
        "__lookup__": "_ext_lookup_exo_land_for_solar_demanded",
    },
)
def exo_land_for_solar_demanded(x, final_subs=None):
    """
    Exogenous demand of land for solar. Only used when LAND module disconected from the rest of the model (SWITCH_LANDWATER=0)
    """
    return _ext_lookup_exo_land_for_solar_demanded(x, final_subs)


_ext_lookup_exo_land_for_solar_demanded = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_LAND_FOR_SOLAR_DEMANDED",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_land_for_solar_demanded",
)


@component.add(
    name="EXO LAND USE AREA PRODUCTIVE USES",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_land_use_area_productive_uses",
        "__lookup__": "_ext_lookup_exo_land_use_area_productive_uses",
    },
)
def exo_land_use_area_productive_uses(x, final_subs=None):
    """
    Exogenous information from simulation- stock of land uses area productive uses by region
    """
    return _ext_lookup_exo_land_use_area_productive_uses(x, final_subs)


_ext_lookup_exo_land_use_area_productive_uses = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_EU27",
    {"REGIONS 9 I": ["EU27"], "LANDS I": _subscript_dict["LANDS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_lookup_exo_land_use_area_productive_uses",
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_UK",
    {"REGIONS 9 I": ["UK"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LANDS I": _subscript_dict["LANDS I"]},
)

_ext_lookup_exo_land_use_area_productive_uses.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_land_use_area_productive_uses_LROW",
    {"REGIONS 9 I": ["LROW"], "LANDS I": _subscript_dict["LANDS I"]},
)


@component.add(
    name="EXO OUTPUT REAL FOR CONSTRUCTION SECTOR",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_construction_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_construction_sector",
    },
)
def exo_output_real_for_construction_sector(x, final_subs=None):
    """
    Exogenous variable of output of construction sector. Only active if SWITCH_LANDWATER=0
    """
    return _ext_lookup_exo_output_real_for_construction_sector(x, final_subs)


_ext_lookup_exo_output_real_for_construction_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "OUTPUT_CONSTRUCTION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_output_real_for_construction_sector",
)


@component.add(
    name="EXO OUTPUT REAL FOR FORESTRY SECTOR",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_forestry_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_forestry_sector",
    },
)
def exo_output_real_for_forestry_sector(x, final_subs=None):
    """
    Output real for forestry sector constant values for 9 regions
    """
    return _ext_lookup_exo_output_real_for_forestry_sector(x, final_subs)


_ext_lookup_exo_output_real_for_forestry_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_OUTPUT_REAL_FORESTRY",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_output_real_for_forestry_sector",
)


@component.add(
    name="EXO OUTPUT REAL FOR MANUFACTURE WOOD SECTOR",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
        "__lookup__": "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
    },
)
def exo_output_real_for_manufacture_wood_sector(x, final_subs=None):
    """
    Exogenous variable of output of wood manufacturing sector. Only active if SWITCH_LANDWATER=0
    """
    return _ext_lookup_exo_output_real_for_manufacture_wood_sector(x, final_subs)


_ext_lookup_exo_output_real_for_manufacture_wood_sector = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "OUTPUT_MANU_WOOD",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_output_real_for_manufacture_wood_sector",
)


@component.add(
    name="EXO POPULATION 35R",
    units="people",
    subscripts=["REGIONS 35 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_population_35r",
        "__lookup__": "_ext_lookup_exo_population_35r",
    },
)
def exo_population_35r(x, final_subs=None):
    return _ext_lookup_exo_population_35r(x, final_subs)


_ext_lookup_exo_population_35r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_POPULATION_35R",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_lookup_exo_population_35r",
)


@component.add(
    name="EXO PV LAND OCCUPATION RATIO",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_pv_land_occupation_ratio",
        "__lookup__": "_ext_lookup_exo_pv_land_occupation_ratio",
    },
)
def exo_pv_land_occupation_ratio(x, final_subs=None):
    """
    Exogenous information from simulation- stock of PV land occupation ratio
    """
    return _ext_lookup_exo_pv_land_occupation_ratio(x, final_subs)


_ext_lookup_exo_pv_land_occupation_ratio = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_PV_LAND_OCCUPATION_RATIO",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_pv_land_occupation_ratio",
)


@component.add(
    name="EXOGENOUS POPULATION 9R",
    units="people",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exogenous_population_9r",
        "__lookup__": "_ext_lookup_exogenous_population_9r",
    },
)
def exogenous_population_9r(x, final_subs=None):
    """
    population historical data by rehion
    """
    return _ext_lookup_exogenous_population_9r(x, final_subs)


_ext_lookup_exogenous_population_9r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_POPULATION_9R",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exogenous_population_9r",
)


@component.add(
    name="FACTOR INPUT HIGH WITH MANURE CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_high_with_manure_crops"},
)
def factor_input_high_with_manure_crops():
    """
    Stock change factor input (FI) High with manure
    """
    return _ext_constant_factor_input_high_with_manure_crops()


_ext_constant_factor_input_high_with_manure_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_HIGHWMANURE_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_input_high_with_manure_crops",
)


@component.add(
    name="FACTOR INPUT HIGH WITHOUT MANURE CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_high_without_manure_crops"},
)
def factor_input_high_without_manure_crops():
    """
    Stock change factor input (FI) High with-out manure
    """
    return _ext_constant_factor_input_high_without_manure_crops()


_ext_constant_factor_input_high_without_manure_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_HIGHWOUTMANURE_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_input_high_without_manure_crops",
)


@component.add(
    name="FACTOR INPUT LOW CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_low_crops"},
)
def factor_input_low_crops():
    """
    Stock change factor input (FI) low
    """
    return _ext_constant_factor_input_low_crops()


_ext_constant_factor_input_low_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_LOW_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_input_low_crops",
)


@component.add(
    name="FACTOR INPUT MEDIUM CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_input_medium_crops"},
)
def factor_input_medium_crops():
    """
    Stock change factor input (FI) medium
    """
    return _ext_constant_factor_input_medium_crops()


_ext_constant_factor_input_medium_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_INPUT_MEDIUM_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_input_medium_crops",
)


@component.add(
    name="FACTOR LANDUSE LONGTERM CULTIVATED CROP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_landuse_longterm_cultivated_crop"
    },
)
def factor_landuse_longterm_cultivated_crop():
    """
    Stock change factor land use (FLU) Long-term cultivated
    """
    return _ext_constant_factor_landuse_longterm_cultivated_crop()


_ext_constant_factor_landuse_longterm_cultivated_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_LONGTERMCULT",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_landuse_longterm_cultivated_crop",
)


@component.add(
    name="FACTOR LANDUSE PADDY RICE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_paddy_rice"},
)
def factor_landuse_paddy_rice():
    """
    Stock change factor land use (FLU) paddy rice
    """
    return _ext_constant_factor_landuse_paddy_rice()


_ext_constant_factor_landuse_paddy_rice = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_PADDY_RICE",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_landuse_paddy_rice",
)


@component.add(
    name="FACTOR LANDUSE PERENNIAL TREE CROP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_perennial_tree_crop"},
)
def factor_landuse_perennial_tree_crop():
    """
    Stock change factor land use (FLU) Perennial/tree crop
    """
    return _ext_constant_factor_landuse_perennial_tree_crop()


_ext_constant_factor_landuse_perennial_tree_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_PERENIAL_TREECROP",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_landuse_perennial_tree_crop",
)


@component.add(
    name="FACTOR LANDUSE SET ASSIDE CROP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_landuse_set_asside_crop"},
)
def factor_landuse_set_asside_crop():
    """
    Stock change factor land use (FLU) SET ASSIDE
    """
    return _ext_constant_factor_landuse_set_asside_crop()


_ext_constant_factor_landuse_set_asside_crop = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_LANDUSE_SET_ASSIDE",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_landuse_set_asside_crop",
)


@component.add(
    name="FACTOR MANAGEMENT FULL TILLAGE CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_full_tillage_crops"},
)
def factor_management_full_tillage_crops():
    """
    Stock change factor management (FMG) full tillage
    """
    return _ext_constant_factor_management_full_tillage_crops()


_ext_constant_factor_management_full_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_FULL_TILLAGE_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_full_tillage_crops",
)


@component.add(
    name="FACTOR MANAGEMENT IMPROVED HIGH GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_improved_high_grassland"
    },
)
def factor_management_improved_high_grassland():
    """
    Stock change factor management IMPROVED_HIGH_ inputs grassland
    """
    return _ext_constant_factor_management_improved_high_grassland()


_ext_constant_factor_management_improved_high_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_IMPROVED_HIGH_GRASSLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_improved_high_grassland",
)


@component.add(
    name="FACTOR MANAGEMENT IMPROVED MEDIUM GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_improved_medium_grassland"
    },
)
def factor_management_improved_medium_grassland():
    """
    Stock change factor management MPROVED with MEDIUM inputs grassland
    """
    return _ext_constant_factor_management_improved_medium_grassland()


_ext_constant_factor_management_improved_medium_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_IMPROVED_MEDIUM_GRASSLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_improved_medium_grassland",
)


@component.add(
    name="FACTOR MANAGEMENT MODERATELY DEGRADED GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_moderately_degraded_grassland"
    },
)
def factor_management_moderately_degraded_grassland():
    """
    Stock change factor management MODERATELY_DEGRADED grassland
    """
    return _ext_constant_factor_management_moderately_degraded_grassland()


_ext_constant_factor_management_moderately_degraded_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_MODERATELY_DEGRADED_GRASSLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_moderately_degraded_grassland",
)


@component.add(
    name="FACTOR MANAGEMENT NOMINALLY MANAGED GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_nominally_managed_grassland"
    },
)
def factor_management_nominally_managed_grassland():
    """
    Stock change factor management nominally managed grassland
    """
    return _ext_constant_factor_management_nominally_managed_grassland()


_ext_constant_factor_management_nominally_managed_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_NOMINALLY_MANAGED_GRASSLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_nominally_managed_grassland",
)


@component.add(
    name="FACTOR MANAGEMENT NOTILL TILLAGE CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_notill_tillage_crops"},
)
def factor_management_notill_tillage_crops():
    """
    Stock change factor management (FMG) no till
    """
    return _ext_constant_factor_management_notill_tillage_crops()


_ext_constant_factor_management_notill_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_NO_TILL_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_notill_tillage_crops",
)


@component.add(
    name="FACTOR MANAGEMENT REDUCE TILLAGE CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_management_reduce_tillage_crops"},
)
def factor_management_reduce_tillage_crops():
    """
    Stock change factor management (FMG) reduced tillage
    """
    return _ext_constant_factor_management_reduce_tillage_crops()


_ext_constant_factor_management_reduce_tillage_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_REDUCED_TILLAGE_CROPS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_reduce_tillage_crops",
)


@component.add(
    name="FACTOR MANAGEMENT SEVERELY DEGRADED GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_management_severely_degraded_grassland"
    },
)
def factor_management_severely_degraded_grassland():
    """
    Stock change factor management SEVERELY_DEGRADED grassland
    """
    return _ext_constant_factor_management_severely_degraded_grassland()


_ext_constant_factor_management_severely_degraded_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "FACTOR_MANAGEMENT_SEVERELY_DEGRADED_GRASSLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_management_severely_degraded_grassland",
)


@component.add(
    name="FACTOR OF CARBON CAPTURE OF GRASSLANDS",
    units="tC/km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_of_carbon_capture_of_grasslands"},
)
def factor_of_carbon_capture_of_grasslands():
    """
    carbon capture per year and area of patures , not activated
    """
    return _ext_constant_factor_of_carbon_capture_of_grasslands()


_ext_constant_factor_of_carbon_capture_of_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "grasslands",
    "FACTOR_OF_CARBON_CAPTURE_OF_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_of_carbon_capture_of_grasslands",
)


@component.add(
    name="FACTOR OF CARBON CAPTURE OF REGENERATIVE GRASSLANDS",
    units="tC/Year/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_factor_of_carbon_capture_of_regenerative_grasslands"
    },
)
def factor_of_carbon_capture_of_regenerative_grasslands():
    """
    carbon capture per year and area of patures under regenerative management, not activated
    """
    return _ext_constant_factor_of_carbon_capture_of_regenerative_grasslands()


_ext_constant_factor_of_carbon_capture_of_regenerative_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "grasslands",
    "FACTOR_OF_CARBON_CAPTURE_OF_REGENERATIVE_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_of_carbon_capture_of_regenerative_grasslands",
)


@component.add(
    name="FACTOR OF GAIN REGENERATIVE GRAZING",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_of_gain_regenerative_grazing"},
)
def factor_of_gain_regenerative_grazing():
    """
    Increment of pasture's ability to rise cattle fue to regenerative management
    """
    return _ext_constant_factor_of_gain_regenerative_grazing()


_ext_constant_factor_of_gain_regenerative_grazing = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "grasslands",
    "GAIN_OF_REGENERATIVE_GRAZING*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_factor_of_gain_regenerative_grazing",
)


@component.add(
    name="FEEDBACK PARAMETER CROPS KI", comp_type="Constant", comp_subtype="Normal"
)
def feedback_parameter_crops_ki():
    return 0.006


@component.add(
    name="FEEDBACK PARAMETER CROPS KP", comp_type="Constant", comp_subtype="Normal"
)
def feedback_parameter_crops_kp():
    return 0.03


@component.add(
    name="FIRST FACTOR WATER EQUATION",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_first_factor_water_equation"},
)
def first_factor_water_equation():
    return _ext_constant_first_factor_water_equation()


_ext_constant_first_factor_water_equation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "WA_Projections_Eq_Factor_1*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_first_factor_water_equation",
)


@component.add(
    name="FLEXITARIANA DIET PATTERNS OF POLICY DIETS SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp"
    },
)
def flexitariana_diet_patterns_of_policy_diets_sp():
    """
    Flexitariana policy diet
    """
    return _ext_constant_flexitariana_diet_patterns_of_policy_diets_sp()


_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "FLEXITARIANA_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_flexitariana_diet_patterns_of_policy_diets_sp",
)


@component.add(
    name="FOOD LOSS PARAMETERS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "FOODS I", "FOOD LOSSES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_food_loss_parameters"},
)
def food_loss_parameters():
    """
    food loss parameters
    """
    return _ext_constant_food_loss_parameters()


_ext_constant_food_loss_parameters = ExtConstant(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_EU27",
    {
        "REGIONS 9 I": ["EU27"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
    "_ext_constant_food_loss_parameters",
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_UK",
    {
        "REGIONS 9 I": ["UK"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_CHINA",
    {
        "REGIONS 9 I": ["CHINA"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_EASOC",
    {
        "REGIONS 9 I": ["EASOC"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_INDIA",
    {
        "REGIONS 9 I": ["INDIA"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_LATAM",
    {
        "REGIONS 9 I": ["LATAM"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_RUSSIA",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_USMCA",
    {
        "REGIONS 9 I": ["USMCA"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)

_ext_constant_food_loss_parameters.add(
    "model_parameters/society/nutrition.xlsx",
    "2020",
    "FOOD_LOSS_PARAMETERS_LROW",
    {
        "REGIONS 9 I": ["LROW"],
        "FOODS I": _subscript_dict["FOODS I"],
        "FOOD LOSSES I": _subscript_dict["FOOD LOSSES I"],
    },
)


@component.add(
    name="GDP OEKSTRA 2019",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_oekstra_2019"},
)
def gdp_oekstra_2019():
    return _ext_constant_gdp_oekstra_2019()


_ext_constant_gdp_oekstra_2019 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDP_BY_OEKSTRA_2019*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_gdp_oekstra_2019",
)


@component.add(
    name="GDP OEKSTRA INITIAL",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_oekstra_initial"},
)
def gdp_oekstra_initial():
    return _ext_constant_gdp_oekstra_initial()


_ext_constant_gdp_oekstra_initial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDPw_B2*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_gdp_oekstra_initial",
)


@component.add(
    name="GDP VARIATION BY OEKSTRA",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_gdp_variation_by_oekstra"},
)
def gdp_variation_by_oekstra():
    """
    Put here the output of each sector and region by Oekstra estimations
    """
    return _ext_constant_gdp_variation_by_oekstra()


_ext_constant_gdp_variation_by_oekstra = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "GDPw_var_B2*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_gdp_variation_by_oekstra",
)


@component.add(
    name="HISTORICAL AFFORESTATION BY REGION",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_afforestation_by_region",
        "__lookup__": "_ext_lookup_historical_afforestation_by_region",
    },
)
def historical_afforestation_by_region(x, final_subs=None):
    """
    Historical data of land uses change to afforestation by region
    """
    return _ext_lookup_historical_afforestation_by_region(x, final_subs)


_ext_lookup_historical_afforestation_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_AFFORESTATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_afforestation_by_region",
)


@component.add(
    name="HISTORICAL AREA OF CROPS ALL MANAGEMENT",
    units="km2",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_area_of_crops_all_management",
        "__lookup__": "_ext_lookup_historical_area_of_crops_all_management",
    },
)
def historical_area_of_crops_all_management(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_area_of_crops_all_management(x, final_subs)


_ext_lookup_historical_area_of_crops_all_management = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_area_of_crops_all_management",
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_area_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_AREA_OF_CROPS_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="HISTORICAL AVERAGE FOREST STOCK LOSS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_average_forest_stock_loss"},
)
def historical_average_forest_stock_loss():
    """
    Average share of forest stock loss during historical period
    """
    return _ext_constant_historical_average_forest_stock_loss()


_ext_constant_historical_average_forest_stock_loss = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "HISTORICAL_FOREST_STOCK_LOSS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_historical_average_forest_stock_loss",
)


@component.add(
    name="HISTORICAL CROPS PRODUCTION FAO",
    units="t/Year",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_crops_production_fao",
        "__lookup__": "_ext_lookup_historical_crops_production_fao",
    },
)
def historical_crops_production_fao(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_crops_production_fao(x, final_subs)


_ext_lookup_historical_crops_production_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_crops_production_fao",
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_crops_production_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_CROPS_FAO_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="HISTORICAL FOREST VOLUME STOCK ALL FORESTS",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_forest_volume_stock_all_forests",
        "__lookup__": "_ext_lookup_historical_forest_volume_stock_all_forests",
    },
)
def historical_forest_volume_stock_all_forests(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_forest_volume_stock_all_forests(x, final_subs)


_ext_lookup_historical_forest_volume_stock_all_forests = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_FOREST_VOLUME_STOCK_ALL_FORESTS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_forest_volume_stock_all_forests",
)


@component.add(
    name="HISTORICAL FOREST VOLUME STOCK CHANGE ALL FORESTS",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_forest_volume_stock_change_all_forests",
        "__lookup__": "_ext_lookup_historical_forest_volume_stock_change_all_forests",
    },
)
def historical_forest_volume_stock_change_all_forests(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_forest_volume_stock_change_all_forests(x, final_subs)


_ext_lookup_historical_forest_volume_stock_change_all_forests = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_FOREST_VOLUME_STOCK_CHANGE_ALL_FORESTS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_forest_volume_stock_change_all_forests",
)


@component.add(
    name="HISTORICAL LAND PRODUCTS PRODUCTION",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_land_products_production",
        "__data__": "_ext_data_historical_land_products_production",
        "time": 1,
    },
)
def historical_land_products_production():
    """
    land products production (FAO data)
    """
    return _ext_data_historical_land_products_production(time())


_ext_data_historical_land_products_production = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "CORN",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["CORN"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_data_historical_land_products_production",
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "RICE",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["RICE"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "CEREALS",
    None,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": ["CEREALS OTHER"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "TUBERS",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["TUBERS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "SOY",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["SOY"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "PULSES_NUTS",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["PULSES NUTS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "OILCROPS",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["OILCROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "SUGARS",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["SUGAR CROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "VEGETABLES_FRUITS",
    None,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": ["FRUITS VEGETABLES"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "BIOFUEL",
    None,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": ["BIOFUEL 2GCROP"],
    },
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "OTHER_CROPS",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["OTHER CROPS"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "WOOD",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["WOOD"]},
)

_ext_data_historical_land_products_production.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_LP",
    "RESIDUES",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["RESIDUES"]},
)


@component.add(
    name="HISTORICAL LAND USE BY REGION",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_land_use_by_region",
        "__lookup__": "_ext_lookup_historical_land_use_by_region",
    },
)
def historical_land_use_by_region(x, final_subs=None):
    """
    HISTORICAL_LAND_USE_BY_REGION
    """
    return _ext_lookup_historical_land_use_by_region(x, final_subs)


_ext_lookup_historical_land_use_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_RAINFED_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_lookup_historical_land_use_by_region",
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_IRRIGATED_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND IRRIGATED"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_MANAGED_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PRIMARY_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PRIMARY"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PLANTATIONS_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PLANTATIONS"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SHRUBLAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SHRUBLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_GRASSLAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["GRASSLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_WETLAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["WETLAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["URBAN LAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SOLAR LAND"]},
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SNOW_ICE_WATERBODIES_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["SNOW ICE WATERBODIES"],
    },
)

_ext_lookup_historical_land_use_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_OTHER_LAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["OTHER LAND"]},
)


@component.add(
    name="HISTORICAL LAND USE CHANGE BY REGION",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_land_use_change_by_region",
        "__lookup__": "_ext_lookup_historical_land_use_change_by_region",
    },
)
def historical_land_use_change_by_region(x, final_subs=None):
    """
    Past trends of land-use change by region. The spike in EASOC for the year 2018 is related with fires. The forest data from India must be revised!
    """
    return _ext_lookup_historical_land_use_change_by_region(x, final_subs)


_ext_lookup_historical_land_use_change_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_RAINFED_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_lookup_historical_land_use_change_by_region",
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_CROPLAND_IRRIGATED_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND IRRIGATED"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_MANAGED_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PRIMARY_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PRIMARY"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_FOREST_PLANTATIONS_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PLANTATIONS"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SHRUBLAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SHRUBLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_GRASSLAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["GRASSLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_WETLAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["WETLAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["URBAN LAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SOLAR LAND"]},
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SNOW_ICE_WATERBODIES_VARIATION_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["SNOW ICE WATERBODIES"],
    },
)

_ext_lookup_historical_land_use_change_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_OTHER_LAND_VARIATION_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["OTHER LAND"]},
)


@component.add(
    name="HISTORICAL ROUNDWOOD HARVESTED",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_roundwood_harvested",
        "__lookup__": "_ext_lookup_historical_roundwood_harvested",
    },
)
def historical_roundwood_harvested(x, final_subs=None):
    """
    historical roundwood harvested
    """
    return _ext_lookup_historical_roundwood_harvested(x, final_subs)


_ext_lookup_historical_roundwood_harvested = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ROUNDWOOD_TIME",
    "HISTORICAL_ROUNDWOOD_HARVESTED",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_roundwood_harvested",
)


@component.add(
    name="HISTORICAL SHARE OF LAND USE CHANGES FROM OTHERS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_historical_share_of_land_use_changes_from_others"
    },
)
def historical_share_of_land_use_changes_from_others():
    """
    SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST PLANTATIONS"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    def_subs.loc[:, :, ["URBAN LAND"]] = True
    def_subs.loc[:, :, ["SOLAR LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_historical_share_of_land_use_changes_from_others().values[
        def_subs.values
    ]
    value.loc[:, :, ["FOREST PRIMARY"]] = 0
    value.loc[:, :, ["SHRUBLAND"]] = 0
    value.loc[:, :, ["WETLAND"]] = 0
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, :, ["OTHER LAND"]] = 0
    return value


_ext_constant_historical_share_of_land_use_changes_from_others = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["CROPLAND RAINFED"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    "_ext_constant_historical_share_of_land_use_changes_from_others",
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_IRRIGATED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["CROPLAND IRRIGATED"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST MANAGED"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_FOREST_PLANTATIONS_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST PLANTATIONS"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_SHARE_OF_GRASSLAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["GRASSLAND"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["URBAN LAND"],
    },
)

_ext_constant_historical_share_of_land_use_changes_from_others.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["SOLAR LAND"],
    },
)


@component.add(
    name="HISTORICAL SHARES OF CROPS ALL MANAGEMENT",
    units="DMNL",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_shares_of_crops_all_management",
        "__lookup__": "_ext_lookup_historical_shares_of_crops_all_management",
    },
)
def historical_shares_of_crops_all_management(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_shares_of_crops_all_management(x, final_subs)


_ext_lookup_historical_shares_of_crops_all_management = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_shares_of_crops_all_management",
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_shares_of_crops_all_management.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_SHARES_ALL_MANAGEMENT_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="HISTORICAL SHARES OF RAINFED CROPS EU",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_shares_of_rainfed_crops_eu",
        "__lookup__": "_ext_lookup_historical_shares_of_rainfed_crops_eu",
    },
)
def historical_shares_of_rainfed_crops_eu(x, final_subs=None):
    """
    GET_DIRECT_LOOKUPS('model_parameters/land_and_water/land_and_water_parameters.xlsx', 'croplands' , 'TIME_CROPLANDS', 'HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_UK') GET_DIRECT_LOOKUPS('model_parameters/land_and_water/land_and_water_paramete rs.xlsx', 'croplands' , 'TIME_CROPLANDS', 'HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_CHINA')
    """
    return _ext_lookup_historical_shares_of_rainfed_crops_eu(x, final_subs)


_ext_lookup_historical_shares_of_rainfed_crops_eu = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_RAINFED_CROP_SHARES_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    "_ext_lookup_historical_shares_of_rainfed_crops_eu",
)


@component.add(
    name="HISTORICAL SOLAR LAND BY REGION",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_solar_land_by_region",
        "__lookup__": "_ext_lookup_historical_solar_land_by_region",
    },
)
def historical_solar_land_by_region(x, final_subs=None):
    return _ext_lookup_historical_solar_land_by_region(x, final_subs)


_ext_lookup_historical_solar_land_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_SOLAR_LAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_solar_land_by_region",
)


@component.add(
    name="HISTORICAL TRENDS OF LAND USE DEMAND",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_trends_of_land_use_demand"},
)
def historical_trends_of_land_use_demand():
    """
    Trends of land use demand got from historical data (lineal approximation)
    """
    return _ext_constant_historical_trends_of_land_use_demand()


_ext_constant_historical_trends_of_land_use_demand = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "HISTORICAL_TRENDS_OF_LAND_USE_CHANGE_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_historical_trends_of_land_use_demand",
)


@component.add(
    name="HISTORICAL URBAN LAND BY REGION",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_urban_land_by_region",
        "__lookup__": "_ext_lookup_historical_urban_land_by_region",
    },
)
def historical_urban_land_by_region(x, final_subs=None):
    return _ext_lookup_historical_urban_land_by_region(x, final_subs)


_ext_lookup_historical_urban_land_by_region = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_LAND_USE",
    "HISTORICAL_URBAN_LAND_BY_REGION",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_urban_land_by_region",
)


@component.add(
    name="HISTORICAL VARIATION OF SHARES OF IRRIGATED CROPS",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
        "__lookup__": "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
    },
)
def historical_variation_of_shares_of_irrigated_crops(x, final_subs=None):
    return _ext_lookup_historical_variation_of_shares_of_irrigated_crops(x, final_subs)


_ext_lookup_historical_variation_of_shares_of_irrigated_crops = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_variation_of_shares_of_irrigated_crops",
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_variation_of_shares_of_irrigated_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_IRRIGATED_CROP_SHARES_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="HISTORICAL VARIATION OF SHARES OF RAINFED CROPS",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
        "__lookup__": "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
    },
)
def historical_variation_of_shares_of_rainfed_crops(x, final_subs=None):
    return _ext_lookup_historical_variation_of_shares_of_rainfed_crops(x, final_subs)


_ext_lookup_historical_variation_of_shares_of_rainfed_crops = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_variation_of_shares_of_rainfed_crops",
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_variation_of_shares_of_rainfed_crops.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_VARIATION_OF_RAINFED_CROP_SHARES_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="HISTORICAL VOLUME STOCK CHANGE FOREST M AND P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
        "__lookup__": "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
    },
)
def historical_volume_stock_change_forest_m_and_p(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_volume_stock_change_forest_m_and_p(x, final_subs)


_ext_lookup_historical_volume_stock_change_forest_m_and_p = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_CHANGE_OF_STOCK_MANAGED_FORESTS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_volume_stock_change_forest_m_and_p",
)


@component.add(
    name="HISTORICAL VOLUME STOCK OF FOREST M AND P",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
        "__lookup__": "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
    },
)
def historical_volume_stock_of_forest_m_and_p(x, final_subs=None):
    """
    historical forest volume stock change by region
    """
    return _ext_lookup_historical_volume_stock_of_forest_m_and_p(x, final_subs)


_ext_lookup_historical_volume_stock_of_forest_m_and_p = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_FORESTS",
    "HISTORICAL_STOCK_OF_MANAGED_FORESTS",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_volume_stock_of_forest_m_and_p",
)


@component.add(
    name="HISTORICAL WATER AVAILABLE 35R",
    units="hm3",
    subscripts=["REGIONS 35 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_water_available_35r",
        "__lookup__": "_ext_lookup_historical_water_available_35r",
    },
)
def historical_water_available_35r(x, final_subs=None):
    return _ext_lookup_historical_water_available_35r(x, final_subs)


_ext_lookup_historical_water_available_35r = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "water",
    "TIME_WATER",
    "HISTORICAL_WATER_AVAILABLE_35R",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_lookup_historical_water_available_35r",
)


@component.add(
    name="HISTORICAL WATER USE FAO",
    units="hm3",
    subscripts=["REGIONS 35 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_water_use_fao",
        "__lookup__": "_ext_lookup_historical_water_use_fao",
    },
)
def historical_water_use_fao(x, final_subs=None):
    """
    historical WATER use from FAO accounts
    """
    return _ext_lookup_historical_water_use_fao(x, final_subs)


_ext_lookup_historical_water_use_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "water",
    "TIME_WATER_USE",
    "HISTORICAL_BLUE_WATER_USE",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_lookup_historical_water_use_fao",
)


@component.add(
    name="HISTORICAL YIELDS FAO",
    units="t/(km2*Year)",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_yields_fao",
        "__lookup__": "_ext_lookup_historical_yields_fao",
    },
)
def historical_yields_fao(x, final_subs=None):
    """
    FAO data only per region mixing irrigated and rainfed
    """
    return _ext_lookup_historical_yields_fao(x, final_subs)


_ext_lookup_historical_yields_fao = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_historical_yields_fao",
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_historical_yields_fao.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "HISTORICAL_YIELDS_FAO_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="IMV EXOGENOUS POPULATION VARIATION",
    units="people/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_exogenous_population_variation",
        "__lookup__": "_ext_lookup_imv_exogenous_population_variation",
    },
)
def imv_exogenous_population_variation(x, final_subs=None):
    """
    to be removed when integrating with Demography module
    """
    return _ext_lookup_imv_exogenous_population_variation(x, final_subs)


_ext_lookup_imv_exogenous_population_variation = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_VARIATION_OF_POPULATION_9R",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_imv_exogenous_population_variation",
)


@component.add(
    name="IMV PE BY COMMODITY AGRICULTURE PRODUCTS",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_pe_by_commodity_agriculture_products",
        "__lookup__": "_ext_lookup_imv_pe_by_commodity_agriculture_products",
    },
)
def imv_pe_by_commodity_agriculture_products(x, final_subs=None):
    """
    exogenour value of PE by commodity agriculture products used when the Land and Water module is disconected from the rest fo WILIAM model
    """
    return _ext_lookup_imv_pe_by_commodity_agriculture_products(x, final_subs)


_ext_lookup_imv_pe_by_commodity_agriculture_products = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_PE_BY_COMMODITY_AGRICULTURE",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_imv_pe_by_commodity_agriculture_products",
)


@component.add(
    name="IMV PE BY COMMODITY FORESTRY PRODUCTS",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_imv_pe_by_commodity_forestry_products",
        "__lookup__": "_ext_lookup_imv_pe_by_commodity_forestry_products",
    },
)
def imv_pe_by_commodity_forestry_products(x, final_subs=None):
    """
    PE by commodity forestry products constant values for 9 regions
    """
    return _ext_lookup_imv_pe_by_commodity_forestry_products(x, final_subs)


_ext_lookup_imv_pe_by_commodity_forestry_products = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "TIME_EXOGENOUS_POPULATION",
    "EXOGENOUS_PE_BY_COMMODITY_FORESTRY",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_imv_pe_by_commodity_forestry_products",
)


@component.add(
    name="INITIAL BLUE WATER REGION HOUSEHOLDS",
    units="hm3",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_blue_water_region_households"},
)
def initial_blue_water_region_households():
    """
    Load the initial (2005) values of the Blue Water for the Households, for the 35 Regions, per capita.
    """
    return _ext_constant_initial_blue_water_region_households()


_ext_constant_initial_blue_water_region_households = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "Blue2005h*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_blue_water_region_households",
)


@component.add(
    name="INITIAL DAIRY OBTAINED FROM GRASSLANDS",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_dairy_obtained_from_grasslands"},
)
def initial_dairy_obtained_from_grasslands():
    """
    dairy quantity produced by grasslands
    """
    return _ext_constant_initial_dairy_obtained_from_grasslands()


_ext_constant_initial_dairy_obtained_from_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "DAIRY_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_dairy_obtained_from_grasslands",
)


@component.add(
    name="INITIAL FOREST ABOVE GROUND BIOMASS STOCK",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_above_ground_biomass_stock"
    },
)
def initial_forest_above_ground_biomass_stock():
    """
    Initial forest above ground biomass stock
    """
    return _ext_constant_initial_forest_above_ground_biomass_stock()


_ext_constant_initial_forest_above_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_ABOVE_GROUND_BIOMASS_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_forest_above_ground_biomass_stock",
)


@component.add(
    name="INITIAL FOREST BELOW GROUND BIOMASS STOCK",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_below_ground_biomass_stock"
    },
)
def initial_forest_below_ground_biomass_stock():
    """
    initial forest below ground biomass stock
    """
    return _ext_constant_initial_forest_below_ground_biomass_stock()


_ext_constant_initial_forest_below_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_BELOW_GROUND_BIOMASS_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_forest_below_ground_biomass_stock",
)


@component.add(
    name="INITIAL FOREST CARBON IN ABOVE GROUND BIOMASS STOCK",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock"
    },
)
def initial_forest_carbon_in_above_ground_biomass_stock():
    """
    Initial forest carbon in above ground biomass stock
    """
    return _ext_constant_initial_forest_carbon_in_above_ground_biomass_stock()


_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_CARBON_IN_ABOVE_GROUND_BIOMASS_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_forest_carbon_in_above_ground_biomass_stock",
)


@component.add(
    name="INITIAL FOREST CARBON IN BELOW GROUND BIOMASS STOCK",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock"
    },
)
def initial_forest_carbon_in_below_ground_biomass_stock():
    """
    initial forest carbon in below ground biomass stock
    """
    return _ext_constant_initial_forest_carbon_in_below_ground_biomass_stock()


_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_FOREST_CARBON_IN_BELOW_GROUND_BIOMASS_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_forest_carbon_in_below_ground_biomass_stock",
)


@component.add(
    name="INITIAL GREEN WATER REGION SECT",
    units="hm3",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_green_water_region_sect"},
)
def initial_green_water_region_sect():
    """
    Load the initial (2005) values of the Green Water, for the 35 Regions and 62 Sectors.
    """
    return _ext_constant_initial_green_water_region_sect()


_ext_constant_initial_green_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "Green2005",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_initial_green_water_region_sect",
)


@component.add(
    name="INITIAL LAND USE BY REGION",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_land_use_by_region"},
)
def initial_land_use_by_region():
    """
    Initial area of land uses
    """
    return _ext_constant_initial_land_use_by_region()


_ext_constant_initial_land_use_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_LAND_BY_REGION_2005*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_initial_land_use_by_region",
)


@component.add(
    name="INITIAL LAND USE BY REGION 2015",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_land_use_by_region_2015"},
)
def initial_land_use_by_region_2015():
    """
    Initial land area in year 2015
    """
    return _ext_constant_initial_land_use_by_region_2015()


_ext_constant_initial_land_use_by_region_2015 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_LAND_BY_REGION_2015*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_initial_land_use_by_region_2015",
)


@component.add(
    name="INITIAL MEAT OBTAINED FROM GRASSLANDS",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_meat_obtained_from_grasslands"},
)
def initial_meat_obtained_from_grasslands():
    """
    meat quantity produced by grasslands
    """
    return _ext_constant_initial_meat_obtained_from_grasslands()


_ext_constant_initial_meat_obtained_from_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "MEAT_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_meat_obtained_from_grasslands",
)


@component.add(
    name="INITIAL PRECIPITATION EVAPOTRANSPIRATION BY REGION",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_precipitation_evapotranspiration_by_region"
    },
)
def initial_precipitation_evapotranspiration_by_region():
    """
    GET_DIRECT_CONSTANTS( 'water', 'WaPPET' , 'B2' ) initial water availability from FAO
    """
    return _ext_constant_initial_precipitation_evapotranspiration_by_region()


_ext_constant_initial_precipitation_evapotranspiration_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "PE_presente*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_precipitation_evapotranspiration_by_region",
)


@component.add(
    name="INITIAL SHARE OF IRRIGATION",
    units="DMNL",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_initial_share_of_irrigation",
        "__lookup__": "_ext_lookup_initial_share_of_irrigation",
    },
)
def initial_share_of_irrigation(x, final_subs=None):
    """
    initial percent of each crop that is irrigated
    """
    return _ext_lookup_initial_share_of_irrigation(x, final_subs)


_ext_lookup_initial_share_of_irrigation = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_EU27",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EU27"]},
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_lookup_initial_share_of_irrigation",
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_UK",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["UK"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_CHINA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["CHINA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_EASOC",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["EASOC"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_INDIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["INDIA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_LATAM",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LATAM"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_RUSSIA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["RUSSIA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_USMCA",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["USMCA"]},
)

_ext_lookup_initial_share_of_irrigation.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_CROPLANDS",
    "SHARE_OF_IRRIGATION_LROW",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"], "REGIONS 9 I": ["LROW"]},
)


@component.add(
    name="INITIAL SHARE OF LAND USE CHANGES FROM OTHERS DOWN",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_land_use_changes_from_others_down",
        "initial_share_of_land_use_changes_from_others_up": 8,
    },
)
def initial_share_of_land_use_changes_from_others_down():
    """
    Matrix of values that tells from whcih land use the land changes of a perticular use come from. Historical values. SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I now is set equal to the shares when the demands go up, EXCEPT FOR FOREST AND CROPLAND IRRIGATED because in some ocasions shares are different when land is released instead of taken.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, :, ["FOREST MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST PRIMARY"]] = True
    def_subs.loc[:, :, ["SOLAR LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_land_use_changes_from_others_down().values[
        def_subs.values
    ]
    value.loc[:, :, ["CROPLAND IRRIGATED"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "CROPLAND IRRIGATED"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["CROPLAND IRRIGATED"]}, 2)
        .values
    )
    value.loc[:, :, ["FOREST PLANTATIONS"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "FOREST PLANTATIONS"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS FOREST I": ["FOREST PLANTATIONS"]}, 2)
        .values
    )
    value.loc[:, :, ["SHRUBLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SHRUBLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["SHRUBLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["GRASSLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "GRASSLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["GRASSLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["WETLAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "WETLAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["WETLAND"]}, 2)
        .values
    )
    value.loc[:, :, ["URBAN LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "URBAN LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["URBAN LAND"]}, 2)
        .values
    )
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "SNOW ICE WATERBODIES"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["SNOW ICE WATERBODIES"]}, 2)
        .values
    )
    value.loc[:, :, ["OTHER LAND"]] = (
        initial_share_of_land_use_changes_from_others_up()
        .loc[:, :, "OTHER LAND"]
        .reset_coords(drop=True)
        .expand_dims({"LANDS MAP I": ["OTHER LAND"]}, 2)
        .values
    )
    return value


_ext_constant_initial_share_of_land_use_changes_from_others_down = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_DOWN",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["CROPLAND RAINFED"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    "_ext_constant_initial_share_of_land_use_changes_from_others_down",
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_DOWN",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST MANAGED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_DOWN",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST PRIMARY"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_down.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_DOWN",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["SOLAR LAND"],
    },
)


@component.add(
    name="INITIAL SHARE OF LAND USE CHANGES FROM OTHERS UP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_land_use_changes_from_others_up"
    },
)
def initial_share_of_land_use_changes_from_others_up():
    """
    Matrix of values that tells from whcih land use the land changes of a perticular use come from. Historical values. SHARES (LANDS_I,LANDS_MAP_I)=demand of use LANDS_MAP_I taken from LANDS_I these are the shares when the demands go up
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST PLANTATIONS"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    def_subs.loc[:, :, ["URBAN LAND"]] = True
    def_subs.loc[:, :, ["SOLAR LAND"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_land_use_changes_from_others_up().values[
        def_subs.values
    ]
    value.loc[:, :, ["FOREST PRIMARY"]] = 0
    value.loc[:, :, ["SHRUBLAND"]] = 0
    value.loc[:, :, ["WETLAND"]] = 0
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, :, ["OTHER LAND"]] = 0
    return value


_ext_constant_initial_share_of_land_use_changes_from_others_up = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_RAINFED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["CROPLAND RAINFED"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    "_ext_constant_initial_share_of_land_use_changes_from_others_up",
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_CROPLAND_IRRIGATED_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["CROPLAND IRRIGATED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_AFFORESTATION_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST MANAGED"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_FOREST_PLANTATIONS_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["FOREST PLANTATIONS"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_GRASSLAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["GRASSLAND"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["URBAN LAND"],
    },
)

_ext_constant_initial_share_of_land_use_changes_from_others_up.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["SOLAR LAND"],
    },
)


@component.add(
    name="INITIAL SHARE OF LOW INPUT AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_share_of_low_input_agriculture():
    """
    Share of agriculture under management based on low input of fertilizers and agrochemicals. It is used to simulate oil and gas shortage effects on agriculture. Its yields are similar to traditional agriculture.
    """
    return xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )


@component.add(
    name="INITIAL SHARE OF PRODUCTION FROM SMALLHOLDERS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_production_from_smallholders"
    },
)
def initial_share_of_production_from_smallholders():
    """
    INICIAL PERCENTAGES OF FOOD PRODUCTION FROM SMALLHOLDERS
    """
    return _ext_constant_initial_share_of_production_from_smallholders()


_ext_constant_initial_share_of_production_from_smallholders = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "INITIAL_PERCENTAGES_OF_PRODUCTION_SMALLHOLDERS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_share_of_production_from_smallholders",
)


@component.add(
    name="INITIAL SHARE OF REGENERATIVE AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_regenerative_agriculture"
    },
)
def initial_share_of_regenerative_agriculture():
    """
    INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE, regenerative is the land under advanced agroecological methods with no use of agrochemical inputs
    """
    return _ext_constant_initial_share_of_regenerative_agriculture()


_ext_constant_initial_share_of_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_share_of_regenerative_agriculture",
)


@component.add(
    name="INITIAL SHARE OF TRADITIONAL AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_traditional_agriculture"
    },
)
def initial_share_of_traditional_agriculture():
    """
    Share of agriculture under traditional agricultural methods with low input of fertilizers and agrochemicals, low yields and labor intensive.
    """
    return _ext_constant_initial_share_of_traditional_agriculture()


_ext_constant_initial_share_of_traditional_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARE_OF_TRADITIONAL_AGRICULTURE",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_share_of_traditional_agriculture",
)


@component.add(
    name="INITIAL SHARE OF URBAN AND SOLAR FROM OTHER LANDS BY REGION",
    units="DMNL",
    subscripts=["REGIONS 36 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region"
    },
)
def initial_share_of_urban_and_solar_from_other_lands_by_region():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "LANDS I": _subscript_dict["LANDS I"],
            "LANDS MAP I": _subscript_dict["LANDS MAP I"],
        },
        ["REGIONS 36 I", "LANDS I", "LANDS MAP I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        ["EU27", "UK", "CHINA", "EASOC", "INDIA", "LATAM", "RUSSIA", "USMCA", "LROW"],
        :,
        ["URBAN LAND"],
    ] = True
    def_subs.loc[
        ["EU27", "UK", "CHINA", "EASOC", "INDIA", "LATAM", "RUSSIA", "USMCA", "LROW"],
        :,
        ["SOLAR LAND"],
    ] = True
    value.values[
        def_subs.values
    ] = _ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region().values[
        def_subs.values
    ]
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["CROPLAND RAINFED"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["CROPLAND IRRIGATED"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["FOREST MANAGED"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["FOREST PRIMARY"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["FOREST PLANTATIONS"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["SHRUBLAND"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["WETLAND"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["SNOW ICE WATERBODIES"]] = 1
    value.loc[_subscript_dict["REGIONS 9 I"], :, ["OTHER LAND"]] = 1
    value.loc[:, :, ["GRASSLAND"]] = 1
    return value


_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_URBAN_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["URBAN LAND"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    "_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region",
)

_ext_constant_initial_share_of_urban_and_solar_from_other_lands_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "INITIAL_SHARE_OF_SOLAR_LAND_FROM_OTHERS_BY_REGION",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": ["SOLAR LAND"],
    },
)


@component.add(
    name="INITIAL SHARES OF CROPS ALL MANAGEMENTS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_shares_of_crops_all_managements"
    },
)
def initial_shares_of_crops_all_managements():
    """
    initial shares of cropland with each crops
    """
    return _ext_constant_initial_shares_of_crops_all_managements()


_ext_constant_initial_shares_of_crops_all_managements = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_shares_of_crops_all_managements",
)


@component.add(
    name="INITIAL SHARES OF IRRIGATED CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_shares_of_irrigated_crops"},
)
def initial_shares_of_irrigated_crops():
    """
    initial shares of irrigated cropland with each crops
    """
    return _ext_constant_initial_shares_of_irrigated_crops()


_ext_constant_initial_shares_of_irrigated_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_IRRIGATED_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_shares_of_irrigated_crops",
)


@component.add(
    name="INITIAL SHARES OF RAINFED CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_shares_of_rainfed_crops"},
)
def initial_shares_of_rainfed_crops():
    """
    initial shares of rainfed cropland with each crop
    """
    return _ext_constant_initial_shares_of_rainfed_crops()


_ext_constant_initial_shares_of_rainfed_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_SHARES_OF_RAINFED_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_shares_of_rainfed_crops",
)


@component.add(
    name="INITIAL TOTAL RENEWABLE WATER BY REGION",
    units="km3",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_total_renewable_water_by_region"
    },
)
def initial_total_renewable_water_by_region():
    """
    GET_DIRECT_CONSTANTS('water','WaPPET' , 'C2' )
    """
    return _ext_constant_initial_total_renewable_water_by_region()


_ext_constant_initial_total_renewable_water_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dams*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_total_renewable_water_by_region",
)


@component.add(
    name="INITIAL VALUE OF LAND PRODUCTS DEMANDED FOR FOOD",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_value_of_land_products_demanded_for_food"
    },
)
def initial_value_of_land_products_demanded_for_food():
    """
    INITIAL DELAY FOR LAND PRODUCTS DEMANDED FOR FOOD
    """
    return _ext_constant_initial_value_of_land_products_demanded_for_food()


_ext_constant_initial_value_of_land_products_demanded_for_food = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INITIAL_DELAY",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_value_of_land_products_demanded_for_food",
)


@component.add(
    name="INITIAL VOLUME STOCK OF FOREST M AND P",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_volume_stock_of_forest_m_and_p"},
)
def initial_volume_stock_of_forest_m_and_p():
    """
    INITIAL_VALUE_OF_MANAGED_STOCK
    """
    return _ext_constant_initial_volume_stock_of_forest_m_and_p()


_ext_constant_initial_volume_stock_of_forest_m_and_p = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "INITIAL_VALUE_OF_MANAGED_STOCK*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_volume_stock_of_forest_m_and_p",
)


@component.add(
    name="INITIAL WATER EFFICIENCY",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_water_efficiency"},
)
def initial_water_efficiency():
    return _ext_constant_initial_water_efficiency()


_ext_constant_initial_water_efficiency = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "INITIAL_WATER_EFFICIENCY*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_water_efficiency",
)


@component.add(
    name="INITIAL YIELDS ALL MANAGEMENTS",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_yields_all_managements"},
)
def initial_yields_all_managements():
    """
    initial agricultura yields all managemens , historical FAO data
    """
    return _ext_constant_initial_yields_all_managements()


_ext_constant_initial_yields_all_managements = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "INITIAL_YIELDS_ALL_MANAGEMENTS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_initial_yields_all_managements",
)


@component.add(
    name="INTENSITIES OF RESIDUES FOR INDUSTRY",
    units="t/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_intensities_of_residues_for_industry"},
)
def intensities_of_residues_for_industry():
    """
    Calculated intensities for residues wood demanded for industry
    """
    return _ext_constant_intensities_of_residues_for_industry()


_ext_constant_intensities_of_residues_for_industry = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INTENSITIES_OF_RESIDUES_FOR_INDUSTRY*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_intensities_of_residues_for_industry",
)


@component.add(
    name="INTENSITIES OF WOOD FOR INDUSTRY",
    units="t/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_intensities_of_wood_for_industry"},
)
def intensities_of_wood_for_industry():
    """
    Calculated intensities for wood demanded for industry
    """
    return _ext_constant_intensities_of_wood_for_industry()


_ext_constant_intensities_of_wood_for_industry = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "INTENSITIES_OF_WOOD_FOR_INDUSTRY*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_intensities_of_wood_for_industry",
)


@component.add(
    name="KI SOLAR FEEDBACK", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def ki_solar_feedback():
    """
    Parameter used for the integral feedback control of solar land adjustment
    """
    return 0.03


@component.add(
    name="KP SOLAR FEEDBACK", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def kp_solar_feedback():
    """
    Parameter used for the proportional feedback control of solar land adjustment
    """
    return 2


@component.add(
    name="LAND AREA ADJUST COEFFICIENT",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_land_area_adjust_coefficient"},
)
def land_area_adjust_coefficient():
    """
    coefficient to take into account fallow and multiple crops in a year (FAO average)
    """
    return _ext_constant_land_area_adjust_coefficient()


_ext_constant_land_area_adjust_coefficient = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "LAND_AREA_ADJUST_COEFFICIENT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_land_area_adjust_coefficient",
)


@component.add(
    name="LAND PRODUCTS HISTORICAL CONSUMPTION",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Data",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_data_land_products_historical_consumption",
        "__data__": "_ext_data_land_products_historical_consumption",
        "time": 1,
    },
)
def land_products_historical_consumption():
    """
    land products consumption historical, net consumption production + imports - exports
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CORN"]] = True
    def_subs.loc[:, ["RICE"]] = True
    def_subs.loc[:, ["CEREALS OTHER"]] = True
    def_subs.loc[:, ["TUBERS"]] = True
    def_subs.loc[:, ["SOY"]] = True
    def_subs.loc[:, ["PULSES NUTS"]] = True
    def_subs.loc[:, ["OILCROPS"]] = True
    def_subs.loc[:, ["SUGAR CROPS"]] = True
    def_subs.loc[:, ["FRUITS VEGETABLES"]] = True
    def_subs.loc[:, ["OTHER CROPS"]] = True
    value.values[def_subs.values] = _ext_data_land_products_historical_consumption(
        time()
    ).values[def_subs.values]
    value.loc[:, ["BIOFUEL 2GCROP"]] = 0
    value.loc[:, ["WOOD"]] = 0
    value.loc[:, ["RESIDUES"]] = 0
    return value


_ext_data_land_products_historical_consumption = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_CORN",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["CORN"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_data_land_products_historical_consumption",
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_RICE",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["RICE"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_CEREALS_OTHER",
    "interpolate",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": ["CEREALS OTHER"],
    },
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_TUBERS",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["TUBERS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_SOY",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["SOY"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_PULSES_NUTS",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["PULSES NUTS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_OILCROPS",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["OILCROPS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_SUGAR_CROPS",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["SUGAR CROPS"]},
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_FRUITS_VEGETABLES",
    "interpolate",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": ["FRUITS VEGETABLES"],
    },
)

_ext_data_land_products_historical_consumption.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "TIME_INTERMODULE",
    "HISTORICAL_CONSUMPTION_OTHER_CROPS",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LAND PRODUCTS I": ["OTHER CROPS"]},
)


@component.add(
    name="LAND PRODUCTS USED FOR ENERGY PERCENTAGES",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_land_products_used_for_energy_percentages"
    },
)
def land_products_used_for_energy_percentages():
    """
    percentage of each land product used for energy
    """
    return _ext_constant_land_products_used_for_energy_percentages()


_ext_constant_land_products_used_for_energy_percentages = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "LAND_PRODUCTS_USED_FOR_ENERGY_PERCENTAGES*",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    "_ext_constant_land_products_used_for_energy_percentages",
)


@component.add(
    name="LIMITS TO LAND USE CHANGES BY REGION",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I", "LANDS MAP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_limits_to_land_use_changes_by_region"},
)
def limits_to_land_use_changes_by_region():
    """
    Maximum land use change allowed from use LANDS_I to use LANDS_I_MAP in percent of the initial land of the use that gives (LANDS_I)
    """
    return _ext_constant_limits_to_land_use_changes_by_region()


_ext_constant_limits_to_land_use_changes_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_EU27",
    {
        "REGIONS 9 I": ["EU27"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
    "_ext_constant_limits_to_land_use_changes_by_region",
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_UK",
    {
        "REGIONS 9 I": ["UK"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_CHINA",
    {
        "REGIONS 9 I": ["CHINA"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_EASOC",
    {
        "REGIONS 9 I": ["EASOC"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_INDIA",
    {
        "REGIONS 9 I": ["INDIA"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_LATAM",
    {
        "REGIONS 9 I": ["LATAM"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_RUSSIA",
    {
        "REGIONS 9 I": ["RUSSIA"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_USMCA",
    {
        "REGIONS 9 I": ["USMCA"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)

_ext_constant_limits_to_land_use_changes_by_region.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_LAND_USE_CHANGES_LROW",
    {
        "REGIONS 9 I": ["LROW"],
        "LANDS I": _subscript_dict["LANDS I"],
        "LANDS MAP I": _subscript_dict["LANDS MAP I"],
    },
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 0",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_0"
    },
)
def limits_to_solar_land_expansion_eroi_min_0():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_0()


_ext_constant_limits_to_solar_land_expansion_eroi_min_0 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_0",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_0",
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 10",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_10"
    },
)
def limits_to_solar_land_expansion_eroi_min_10():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_10()


_ext_constant_limits_to_solar_land_expansion_eroi_min_10 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_10",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_10",
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 2",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_2"
    },
)
def limits_to_solar_land_expansion_eroi_min_2():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_2()


_ext_constant_limits_to_solar_land_expansion_eroi_min_2 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_2",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_2",
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 3",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_3"
    },
)
def limits_to_solar_land_expansion_eroi_min_3():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_3()


_ext_constant_limits_to_solar_land_expansion_eroi_min_3 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_3",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_3",
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 5",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_5"
    },
)
def limits_to_solar_land_expansion_eroi_min_5():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_5()


_ext_constant_limits_to_solar_land_expansion_eroi_min_5 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_5",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_5",
)


@component.add(
    name="LIMITS TO SOLAR LAND EXPANSION EROI MIN 8",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limits_to_solar_land_expansion_eroi_min_8"
    },
)
def limits_to_solar_land_expansion_eroi_min_8():
    """
    Share of are of each land use in 2015 that can be used for solar.
    """
    return _ext_constant_limits_to_solar_land_expansion_eroi_min_8()


_ext_constant_limits_to_solar_land_expansion_eroi_min_8 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "LIMITS_TO_SOLAR_LAND_EXPANSION_EROI_MIN_8",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_limits_to_solar_land_expansion_eroi_min_8",
)


@component.add(
    name="LOSS FACTOR OF LAND PRODUCTS",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_loss_factor_of_land_products"},
)
def loss_factor_of_land_products():
    """
    Factor of losses in food production
    """
    return _ext_constant_loss_factor_of_land_products()


_ext_constant_loss_factor_of_land_products = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "intermodule_global_allocate",
    "LOSS_FACTOR_LAND_PRODUCTS*",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    "_ext_constant_loss_factor_of_land_products",
)


@component.add(
    name="MANAGEMENT STOCK CHANGE FACTOR DEFAULT CROPLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_management_stock_change_factor_default_cropland"
    },
)
def management_stock_change_factor_default_cropland():
    """
    Factors for "Cbefore". Soil database (regionally average C stocks) corresponds to Cbef (default values) assuming full tillage (FMG), Input is medium (FI) and long-term cultivated (FLU).
    """
    return _ext_constant_management_stock_change_factor_default_cropland()


_ext_constant_management_stock_change_factor_default_cropland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DEFAULT_MANAGEMENT_STOCK_FACTOR_CROPS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_management_stock_change_factor_default_cropland",
)


@component.add(
    name="MANAGEMENT STOCK CHANGE FACTOR DEFAULT GRASSLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_management_stock_change_factor_default_grassland"
    },
)
def management_stock_change_factor_default_grassland():
    """
    Factors for "Cbefore". Soil database (regionally average C stocks) corresponds to Cbef (default values) For grasslands (Plevin et al 2014) ,assume a value of 1 for all three: LU (following the IPCC recommendation for all grassland); MG, assuming the land is nominally managed (non-degraded); and I, assuming medium inputs .
    """
    return _ext_constant_management_stock_change_factor_default_grassland()


_ext_constant_management_stock_change_factor_default_grassland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "DEFAULT_MANAGEMENT_STOCK_FACTOR_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_management_stock_change_factor_default_grassland",
)


@component.add(
    name="MASK CROPS",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mask_crops():
    """
    =1 if land product is a crop , 0 for wood and residues and for other crops because its demand is not given by the diets module
    """
    return xr.DataArray(
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
        ["LAND PRODUCTS I"],
    )


@component.add(
    name="MASK ESSENTIAL FOODS",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def mask_essential_foods():
    """
    Variable to select the land products that influence food shortage
    """
    return xr.DataArray(
        [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
        ["LAND PRODUCTS I"],
    )


@component.add(
    name="MATRIX COUNTRY REGION",
    subscripts=["REGIONS 35 I", "REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_matrix_country_region"},
)
def matrix_country_region():
    """
    GET_DIRECT_CONSTANTS( 'model_parameters/constants.xlsx', 'constants', 'D76' )
    """
    return _ext_constant_matrix_country_region()


_ext_constant_matrix_country_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "water_matrix",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_constant_matrix_country_region",
)


@component.add(
    name="MAXIMUM ANNUAL LAND USE CHANGE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_annual_land_use_change"},
)
def maximum_annual_land_use_change():
    """
    Maximum land use changes observed in historical period relative to the initial land area of each type
    """
    return _ext_constant_maximum_annual_land_use_change()


_ext_constant_maximum_annual_land_use_change = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "MAXIMUM_ANNUAL_LAND_USE_CHANGE",
    {},
    _root,
    {},
    "_ext_constant_maximum_annual_land_use_change",
)


@component.add(
    name="MAXIMUM CROP SHARES",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_crop_shares"},
)
def maximum_crop_shares():
    """
    maximum shares than highly exigent crops can achieve. Not activated.
    """
    return _ext_constant_maximum_crop_shares()


_ext_constant_maximum_crop_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_maximum_crop_shares",
)


@component.add(
    name="MAXIMUM EXPLOITATION WATER COEFFICIENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def maximum_exploitation_water_coefficient():
    """
    max exploitable to preserve envirn systems (from Amandine) Could change with policies, we can put in the excel: scenario_parameters, add in water explotation. 0.3 and 0.2.
    """
    return 0.4


@component.add(
    name="MAXIMUM FOREST STOCK PER AREA",
    units="m3/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_forest_stock_per_area"},
)
def maximum_forest_stock_per_area():
    """
    maximum forest avobe ground per area not including distirbance for natural causes
    """
    return _ext_constant_maximum_forest_stock_per_area()


_ext_constant_maximum_forest_stock_per_area = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "MAXIMUM_FOREST_STOCK_PER_AREA*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_maximum_forest_stock_per_area",
)


@component.add(
    name="MAXIMUM IRRIGATED CROPS SHARES",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_irrigated_crops_shares"},
)
def maximum_irrigated_crops_shares():
    """
    maximum shares that crops can achieve, not activated.
    """
    return _ext_constant_maximum_irrigated_crops_shares()


_ext_constant_maximum_irrigated_crops_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_IRRIGATED_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_maximum_irrigated_crops_shares",
)


@component.add(
    name="MAXIMUM LAND USES BY SOURCE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_land_uses_by_source"},
)
def maximum_land_uses_by_source():
    """
    Used when the limits to expansion in the case of forest plantations adn rainfed cropland is drive by the land type that demands the land ( SELECT_LIMITS_LAND_BY_SOURCE_SP=1). It gives the share of land that can be increased relative to the area in the initial year. =1 means no increase allowed.
    """
    return _ext_constant_maximum_land_uses_by_source()


_ext_constant_maximum_land_uses_by_source = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "MAXIMUM_INCREASE_OF_LAND_BY_SOURCE",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_maximum_land_uses_by_source",
)


@component.add(
    name="MAXIMUM RAINFED CROPS SHARES",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_rainfed_crops_shares"},
)
def maximum_rainfed_crops_shares():
    """
    maximum shares that crops can achieve, not activated.
    """
    return _ext_constant_maximum_rainfed_crops_shares()


_ext_constant_maximum_rainfed_crops_shares = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_SHARES_OF_RAINFED_CROPS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_maximum_rainfed_crops_shares",
)


@component.add(
    name="MAXIMUM YIELDS R AND I INDUSTRIAL",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_yields_r_and_i_industrial"},
)
def maximum_yields_r_and_i_industrial():
    """
    maximum yiedls possible in the future for industrial management, irrigated and rainfed mixed
    """
    return _ext_constant_maximum_yields_r_and_i_industrial()


_ext_constant_maximum_yields_r_and_i_industrial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_YIELDS_R_AND_I",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_maximum_yields_r_and_i_industrial",
)


@component.add(
    name="MAXIMUM YIELDS RAINFED INDUSTRIAL",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_yields_rainfed_industrial"},
)
def maximum_yields_rainfed_industrial():
    """
    maximum yiedls possible in the future for industrial management, rainfed
    """
    return _ext_constant_maximum_yields_rainfed_industrial()


_ext_constant_maximum_yields_rainfed_industrial = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "MAXIMUM_YIELDS_RAINFED_INDUSTRIAL",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_maximum_yields_rainfed_industrial",
)


@component.add(
    name="MINIMUM LAND USES BY REGION",
    units="km2",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_land_uses_by_region"},
)
def minimum_land_uses_by_region():
    """
    Minimum limit of land use for each region
    """
    return _ext_constant_minimum_land_uses_by_region()


_ext_constant_minimum_land_uses_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "MINIMUM_LAND_USES_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_minimum_land_uses_by_region",
)


@component.add(
    name="OBJECTIVE AFFORESTATION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_afforestation_sp"},
)
def objective_afforestation_sp():
    """
    -Policy of increase of managed forest. -This is an increase of the hihg biodiversity forest (not the increase of tree plantations) -The OBJECTIVE area of forest is achieved in the FINAL TIME with a lineal evolution. -OBJECTIVE of this policy is expressed as a % of the historical value of the area of forest of 2015 (0=0%, means that there is no increse of forest; 1=100%, means that the area reforested equals forest area in 2015). -This policy competes with the rest of land uses, therefore, the forest area objective might not be achiven in the final year due to land use changes from forest to other uses.
    """
    return _ext_constant_objective_afforestation_sp()


_ext_constant_objective_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_AFFORESTATION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_afforestation_sp",
)


@component.add(
    name="OBJECTIVE CROPLAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_cropland_protection_sp"},
)
def objective_cropland_protection_sp():
    """
    -If this policy is applied, the cropland (Sum of irrigated and rainfed cropland) is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If cropland area in INITIAL YEAR is lower than OBJECTIVE*cropland area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of cropland in 2015 (from 0 to 1; =1 means that an area equal to the cropland we had in 2015 is protected, =0 means that there are no limits to cropland loss).
    """
    return _ext_constant_objective_cropland_protection_sp()


_ext_constant_objective_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_CROPLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_cropland_protection_sp",
)


@component.add(
    name="OBJECTIVE DIET CHANGE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_diet_change_sp"},
)
def objective_diet_change_sp():
    """
    -If this policy is applied, the population starts a cultural-driven change of diet to the policy diets that starts in INITIAL YEAR and ends in FINAL YEAR. -OBJECTIVE of this policy is expressed as a share of the population that has adopted the policy diet in FINAL YEAR. -OBJECTIVE varies between 0 and 1 (0= means that there no dietary change, 1= means that all the population adopts the policy diet).
    """
    return _ext_constant_objective_diet_change_sp()


_ext_constant_objective_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_DIET_CHANGE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_diet_change_sp",
)


@component.add(
    name="OBJECTIVE EFFECT OF OIL AND GAS ON AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def objective_effect_of_oil_and_gas_on_agriculture_sp():
    """
    Share of agricultura area in final year that can no loger be cultivated with industrialized methods based on high use of agrochemical inputs
    """
    return _ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="OBJECTIVE FOREST PLANTATIONS SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_forest_plantations_sp"},
)
def objective_forest_plantations_sp():
    """
    -This is an increase of tree plantations. -The OBJECTIVE area of forest is achieved in the FINAL TIME with a lineal evolution. -OBJECTIVE of this policy is expressed as a % of the historical value of the area of PLANTATIONS of 2015 (0=0%, means that there is no increse of plantations; 1=100%, means that the area planted equals plantations area in 2015). -This policy competes with the rest of land uses, therefore, the area objective might not be achiven in the final year due to land use changes to other uses.
    """
    return _ext_constant_objective_forest_plantations_sp()


_ext_constant_objective_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_FOREST_PLANTATIONS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_forest_plantations_sp",
)


@component.add(
    name="OBJECTIVE FORESTRY SELF SUFFICIENCY SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_forestry_self_sufficiency_sp"},
)
def objective_forestry_self_sufficiency_sp():
    """
    FORESTRY_SELF_SUFFICIENCY policy objective
    """
    return _ext_constant_objective_forestry_self_sufficiency_sp()


_ext_constant_objective_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_forestry_self_sufficiency_sp",
)


@component.add(
    name="OBJECTIVE GRASSLAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_grassland_protection_sp"},
)
def objective_grassland_protection_sp():
    """
    -If this policy is applied, the grassland is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If grassland area in INITIAL YEAR is lower than OBJECTIVE*grassland area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of grassland in 2015 (from 0 to 1; =1 means that an area equal to the grassland we had in 2015 is protected, =0 means that there are no limits to grassland loss).
    """
    return _ext_constant_objective_grassland_protection_sp()


_ext_constant_objective_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_GRASSLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_grassland_protection_sp",
)


@component.add(
    name="OBJECTIVE INDUSTRIAL AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_industrial_agriculture_sp"},
)
def objective_industrial_agriculture_sp():
    """
    policy objective
    """
    return _ext_constant_objective_industrial_agriculture_sp()


_ext_constant_objective_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_industrial_agriculture_sp",
)


@component.add(
    name="OBJECTIVE LAND PRODUCTS GLOBAL POOL SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_land_products_global_pool_sp"},
)
def objective_land_products_global_pool_sp():
    """
    -Policy of protection of land products from global trade. Share of the production in final policy year that does not interact with global allocation of products
    """
    return _ext_constant_objective_land_products_global_pool_sp()


_ext_constant_objective_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_land_products_global_pool_sp",
)


@component.add(
    name="OBJECTIVE MANAGED FOREST PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_managed_forest_protection_sp"},
)
def objective_managed_forest_protection_sp():
    """
    -If this policy is applied, the managed forest is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If managed forest area in INITIAL YEAR is lower than OBJECTIVE*forest area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of managed forest in 2015 (from 0 to 1; =1 means that an area equal to the managed forest we had in 2015 is protected, =0 means that there are no limits to deforestation).
    """
    return _ext_constant_objective_managed_forest_protection_sp()


_ext_constant_objective_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_managed_forest_protection_sp",
)


@component.add(
    name="OBJECTIVE NATURAL LAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_natural_land_protection_sp"},
)
def objective_natural_land_protection_sp():
    """
    -If this policy is applied, the natural land is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If natural land area in INITIAL YEAR is lower than OBJECTIVE*natural land area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of natural land in 2015 (from 0 to 1; =1 means that an area equal to the land natural we had in 2015 is protected, =0 means that there are no limits to natural land loss).
    """
    return _ext_constant_objective_natural_land_protection_sp()


_ext_constant_objective_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_natural_land_protection_sp",
)


@component.add(
    name="OBJECTIVE PRIMARY FOREST PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_primary_forest_protection_sp"},
)
def objective_primary_forest_protection_sp():
    """
    -If this policy is applied, the primary forest is protected and its area does not go down the value given in OBJECTIVE. -The protection starts in INITIAL YEAR and ends in FINAL YEAR. -If primary forest area in INITIAL YEAR is lower than OBJECTIVE*forest area in 2015 (TIME HISTORICAL DATA LAND MODULE), the area in INITIAL YEAR is maintained. -OBJECTIVE of policy is expressed as a share of the initial area of primary forest in 2015 (from 0 to 1; =1 means that an area equal to the primary forest we had in 2015 is protected, =0 means that there are no limits to deforestation).
    """
    return _ext_constant_objective_primary_forest_protection_sp()


_ext_constant_objective_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_primary_forest_protection_sp",
)


@component.add(
    name="OBJECTIVE REGENERATIVE AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_regenerative_agriculture_sp"},
)
def objective_regenerative_agriculture_sp():
    """
    policy objective
    """
    return _ext_constant_objective_regenerative_agriculture_sp()


_ext_constant_objective_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OBJECTIVE_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_regenerative_agriculture_sp",
)


@component.add(
    name="OBJECTIVE SOIL MANAGEMENT IN GRASSLANDS SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_soil_management_in_grasslands_sp"
    },
)
def objective_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy objective
    """
    return _ext_constant_objective_soil_management_in_grasslands_sp()


_ext_constant_objective_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_SOIL_MANAGEMENT_IN_GRASSLANDS_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_soil_management_in_grasslands_sp",
)


@component.add(
    name="OBJECTIVE SOLAR LAND FROM OTHERS SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_solar_land_from_others_sp"},
)
def objective_solar_land_from_others_sp():
    """
    solar land from others objective. vector that tells from which land use the land for solar comes from in the YEAR FINAL SOLAR LAND FROM OTHERS
    """
    return _ext_constant_objective_solar_land_from_others_sp()


_ext_constant_objective_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_SOLAR_LAND_FROM_OTHERS",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_objective_solar_land_from_others_sp",
)


@component.add(
    name="OBJECTIVE URBAN LAND DENSITY SP",
    units="m2/person",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_urban_land_density_sp"},
)
def objective_urban_land_density_sp():
    """
    Policy objective to set urban land dispertion ratio (m2 per person) in final year of policy.
    """
    return _ext_constant_objective_urban_land_density_sp()


_ext_constant_objective_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_URBAN_LAND_DENSITY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_urban_land_density_sp",
)


@component.add(
    name="OBJECTIVE WATER EFFICIENCY SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_water_efficiency_sp"},
)
def objective_water_efficiency_sp():
    """
    OBJECTIVE_WATER_EFFICIENCY_SP
    """
    return _ext_constant_objective_water_efficiency_sp()


_ext_constant_objective_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_objective_water_efficiency_sp",
)


@component.add(
    name="OUTTURN OF WOOD EXTRACTION",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_outturn_of_wood_extraction"},
)
def outturn_of_wood_extraction():
    """
    efficiency of wood extraction
    """
    return _ext_constant_outturn_of_wood_extraction()


_ext_constant_outturn_of_wood_extraction = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "OUTTURN_OF_WOOD_EXTRACTION*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_outturn_of_wood_extraction",
)


@component.add(
    name="PAST TRENDS GLOBAL CO2 LAND USE CHANGE EMISSIONS",
    units="GtCO2/Year",
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_past_trends_global_co2_land_use_change_emissions",
        "__data__": "_ext_data_past_trends_global_co2_land_use_change_emissions",
        "time": 1,
    },
)
def past_trends_global_co2_land_use_change_emissions():
    """
    [DICE-2013R] Land-use change emissions. Cte at 2010 level for the period 1990-2100 as first approximation. Also aligned with Houghton Et al 2017--> Global and regional fluxes of carbon from land use and land cover change 1850–2015 (total cumulative = 145,5 / (2015-1850)= 0.88 GtC/año (in DICE = 0,9 GtC/año)
    """
    return _ext_data_past_trends_global_co2_land_use_change_emissions(time())


_ext_data_past_trends_global_co2_land_use_change_emissions = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_OTHER_GHG_EMISSIONS",
    "LAND_USE_CHANGE_EMISSIONS",
    "interpolate",
    {},
    _root,
    {},
    "_ext_data_past_trends_global_co2_land_use_change_emissions",
)


@component.add(
    name="PERCENT OF LAND PRODUCTS FOR OTHER USES",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_percent_of_land_products_for_other_uses"
    },
)
def percent_of_land_products_for_other_uses():
    """
    Percentages of food + feed + energy - other uses
    """
    return _ext_constant_percent_of_land_products_for_other_uses()


_ext_constant_percent_of_land_products_for_other_uses = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Diet",
    "LAND_PRODUCTS_DISTRIBUTION_PERCENTAGES*",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    "_ext_constant_percent_of_land_products_for_other_uses",
)


@component.add(
    name="PLANT BASED 100 DIET PATTERN OF POLICY DIETS SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp"
    },
)
def plant_based_100_diet_pattern_of_policy_diets_sp():
    """
    100% plant based policy diet
    """
    return _ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp()


_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PLANT_BASED_100_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_plant_based_100_diet_pattern_of_policy_diets_sp",
)


@component.add(
    name="POLICIES OF LAND USE CHANGE FROM OTHERS AT REGIONAL LEVEL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def policies_of_land_use_change_from_others_at_regional_level():
    """
    EQUATION NOT SET esto seria par ahacer que la demanda de tierras de solar y de urban no se tomase de un tipo de tierras sino de otras,cambios poco a poco en os hsares
    """
    return 0


@component.add(
    name="POLICY LAND PROTECTION FROM SOLAR PV SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_policy_land_protection_from_solar_pv_sp"
    },
)
def policy_land_protection_from_solar_pv_sp():
    """
    Policies of land protected from solar PV deployment. if =1 the policy allows to deploy solar PV in that land use type if =0 the policy protect that type of land use to be occupied for solar PV
    """
    return _ext_constant_policy_land_protection_from_solar_pv_sp()


_ext_constant_policy_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_policy_land_protection_from_solar_pv_sp",
)


@component.add(
    name="POLICY MAXIMUM SHARE SOLAR URBAN SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_policy_maximum_share_solar_urban_sp"},
)
def policy_maximum_share_solar_urban_sp():
    """
    Policy defining the maximum value for the share of urban and solar, --> land use solar/ land use urban - To set this value considering the relation to cropland (example: solar land/cropland compared to urban_land/cropland).
    """
    return _ext_constant_policy_maximum_share_solar_urban_sp()


_ext_constant_policy_maximum_share_solar_urban_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_MAXIMUM_SHARE_SOLAR_URBAN_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_policy_maximum_share_solar_urban_sp",
)


@component.add(
    name="PREINDUSTRIAL C",
    units="Gt",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_preindustrial_c"},
)
def preindustrial_c():
    """
    Preindustrial C content of atmosphere.
    """
    return _ext_constant_preindustrial_c()


_ext_constant_preindustrial_c = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "preindustrial_C",
    {},
    _root,
    {},
    "_ext_constant_preindustrial_c",
)


@component.add(
    name="PRIORITIES OF CROPS DISTRIBUTION AMONG USES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "USES LP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_priorities_of_crops_distribution_among_uses_sp"
    },
)
def priorities_of_crops_distribution_among_uses_sp():
    """
    PRIORITIES_OF_CROPS_DISTRIBUTION_AMONG_USES, constant for all land products
    """
    return _ext_constant_priorities_of_crops_distribution_among_uses_sp()


_ext_constant_priorities_of_crops_distribution_among_uses_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_CROPS_DISTRIBUTION_USES",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "USES LP I": _subscript_dict["USES LP I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "USES LP I": _subscript_dict["USES LP I"],
    },
    "_ext_constant_priorities_of_crops_distribution_among_uses_sp",
)


@component.add(
    name="PRIORITIES OF FORESTRY PRODUCTS DISTRIBUTION AMONG USES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "USES LP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_priorities_of_forestry_products_distribution_among_uses_sp"
    },
)
def priorities_of_forestry_products_distribution_among_uses_sp():
    """
    PRIORITIES_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES,
    """
    return _ext_constant_priorities_of_forestry_products_distribution_among_uses_sp()


_ext_constant_priorities_of_forestry_products_distribution_among_uses_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_FORESTRY_DISTRIBUTION_USES",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "USES LP I": _subscript_dict["USES LP I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "USES LP I": _subscript_dict["USES LP I"],
    },
    "_ext_constant_priorities_of_forestry_products_distribution_among_uses_sp",
)


@component.add(
    name="PRIORITIES OF LAND PRODUCTS DISTRIBUTION AMONG REGIONS SP",
    units="DMNL",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_priorities_of_land_products_distribution_among_regions_sp"
    },
)
def priorities_of_land_products_distribution_among_regions_sp():
    """
    PRIORITIES_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS_
    """
    return _ext_constant_priorities_of_land_products_distribution_among_regions_sp()


_ext_constant_priorities_of_land_products_distribution_among_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_PRODUCTS_DISTRIBUTION_REGIONS*",
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    _root,
    {
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
    },
    "_ext_constant_priorities_of_land_products_distribution_among_regions_sp",
)


@component.add(
    name="PRIORITIES OF LAND USE CHANGE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={"__external__": "_ext_constant_priorities_of_land_use_change_sp"},
)
def priorities_of_land_use_change_sp():
    """
    priorities of land use change policy, only valid to speed up the change to solar and cropland. Not fully implemented
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, ["FOREST MANAGED"]] = True
    def_subs.loc[:, ["FOREST PLANTATIONS"]] = True
    def_subs.loc[:, ["SOLAR LAND"]] = True
    value.values[def_subs.values] = (
        _ext_constant_priorities_of_land_use_change_sp().values[def_subs.values]
    )
    value.loc[:, ["CROPLAND IRRIGATED"]] = 0
    value.loc[:, ["FOREST PRIMARY"]] = 0
    value.loc[:, ["SHRUBLAND"]] = 0
    value.loc[:, ["GRASSLAND"]] = 0
    value.loc[:, ["WETLAND"]] = 0
    value.loc[:, ["URBAN LAND"]] = 0
    value.loc[:, ["SNOW ICE WATERBODIES"]] = 0
    value.loc[:, ["OTHER LAND"]] = 0
    return value


_ext_constant_priorities_of_land_use_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_CROPLAND_RAINFED*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["CROPLAND RAINFED"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_priorities_of_land_use_change_sp",
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_FOREST_MANAGED*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST MANAGED"]},
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_FOREST_PLANTATIONS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["FOREST PLANTATIONS"]},
)

_ext_constant_priorities_of_land_use_change_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "PRIORITIES_OF_LAND_USE_SOLAR_LAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "LANDS I": ["SOLAR LAND"]},
)


@component.add(
    name="ROOT TO SHOOT RATIO FOREST",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_root_to_shoot_ratio_forest"},
)
def root_to_shoot_ratio_forest():
    """
    root to shoot ratio forest
    """
    return _ext_constant_root_to_shoot_ratio_forest()


_ext_constant_root_to_shoot_ratio_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "ROOT_TO_SHOOT_RATIO_FOREST*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_root_to_shoot_ratio_forest",
)


@component.add(
    name="SATURATION TIME OF REGENERATIVE GRASSLANDS",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_saturation_time_of_regenerative_grasslands"
    },
)
def saturation_time_of_regenerative_grasslands():
    """
    Years that takes the soil of pastures to became saturated of C
    """
    return _ext_constant_saturation_time_of_regenerative_grasslands()


_ext_constant_saturation_time_of_regenerative_grasslands = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "grasslands",
    "SATURATION_TIME_OF_REGENERATIVE_GRASSLANDS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_saturation_time_of_regenerative_grasslands",
)


@component.add(
    name="SEA LEVEL RISE PARAMETER ALPHA",
    units="m/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sea_level_rise_parameter_alpha"},
)
def sea_level_rise_parameter_alpha():
    """
    parameter alpha is part of the "Roson and Sartori 2016b" equation that assumes a positive relationship between sea level rise and the increase in global mean surface temperature. 〖SLR〗_i=(α+β∆t-V_i )(T-2000)
    """
    return _ext_constant_sea_level_rise_parameter_alpha()


_ext_constant_sea_level_rise_parameter_alpha = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "ALPHA_CONSTANT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_sea_level_rise_parameter_alpha",
)


@component.add(
    name="SEA LEVEL RISE PARAMETER BETA",
    units="m/(Year*DegreesC)",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sea_level_rise_parameter_beta"},
)
def sea_level_rise_parameter_beta():
    """
    parameter beta is part of the "Roson and Sartori 2016b" equation that assumes a positive relationship between sea level rise and the increase in global mean surface temperature. 〖SLR〗_i=(α+β∆t-V_i )(T-2000)
    """
    return _ext_constant_sea_level_rise_parameter_beta()


_ext_constant_sea_level_rise_parameter_beta = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "BETA_CONSTANT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_sea_level_rise_parameter_beta",
)


@component.add(
    name="SECOND FACTOR WATER EQUATION",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_second_factor_water_equation"},
)
def second_factor_water_equation():
    return _ext_constant_second_factor_water_equation()


_ext_constant_second_factor_water_equation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "WA_Projections_Eq_Factor_2*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_second_factor_water_equation",
)


@component.add(
    name="SELECT EROI MIN POTENTIAL WIND SOLAR SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_eroi_min_potential_wind_solar_sp"
    },
)
def select_eroi_min_potential_wind_solar_sp():
    """
    Threshold of EROImin selected by the user for the solar and wind potential.
    """
    return _ext_constant_select_eroi_min_potential_wind_solar_sp()


_ext_constant_select_eroi_min_potential_wind_solar_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_EROI_MIN_POTENTIAL_WIND_SOLAR_SP",
    {},
    _root,
    {},
    "_ext_constant_select_eroi_min_potential_wind_solar_sp",
)


@component.add(
    name="SELECT SELECTION MANAGEMENT GRASSLAND SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_selection_management_grassland_sp"
    },
)
def select_selection_management_grassland_sp():
    """
    Based on IPCC Table 6.2 (soil stock change factor for different management activities on grassland). 0. Nominally managed (non-degraded). No new policies. Keep present trends/default assumption (Plevin et al. 2014). Sustainably managed grassland, but without significant management improvements. 1. Moderately degraded grassland. Overgrazed or moderately degraded grassland, with somewhat reduced productivity and receiving no management inputs. 2. Severely degraded. Implies major long-term loss of productivity and vegetation cover, due to severe mechanical damage to the vegetation and/or severe soil erosion. 3. Improved grassland medium inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). No additional management inputs have been used. 4. Improved grassland high inputs. Sustainably managed with moderate grazing pressure and that receive at least one improvement (e.g., fertilization, species improvement, irrigation). One or more additional management inputs/improvements have been used (beyond that is required to be classified as improved grassland)
    """
    return _ext_constant_select_selection_management_grassland_sp()


_ext_constant_select_selection_management_grassland_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_GRASSLAND_MANAGEMENT_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_selection_management_grassland_sp",
)


@component.add(
    name="SELECT SELECTION MANAGEMENT SOLARLAND SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_selection_management_solarland_sp"
    },
)
def select_selection_management_solarland_sp():
    """
    Based on article from Dirk (Suplementary information: Table S8), Capellán et al 2021 https://www.nature.com/articles/s41598-021-82042-5#author-information 0. Permanently clearing land vegetation 1. Maintain /restore previous vegetation (up to 30 cm) 2. Seeding and management as pastures GET_DIRECT_CONSTANTS('scenario_parameters/scenario_parameters.xlsx', 'land_and_water', 'XXXXX')
    """
    return _ext_constant_select_selection_management_solarland_sp()


_ext_constant_select_selection_management_solarland_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_OF_SOLARLAND_MANAGEMENT_SELECTED",
    {},
    _root,
    {},
    "_ext_constant_select_selection_management_solarland_sp",
)


@component.add(
    name="SHARE OF CHANGE TO POLICY DIET INITIAL VALUE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_change_to_policy_diet_initial_value_sp"
    },
)
def share_of_change_to_policy_diet_initial_value_sp():
    """
    initial value of share of change to policy diet and must be 0.
    """
    return _ext_constant_share_of_change_to_policy_diet_initial_value_sp()


_ext_constant_share_of_change_to_policy_diet_initial_value_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SHARE_OF_CHANGE_TO_POLICY_DIET_INICIAL_VALUE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_share_of_change_to_policy_diet_initial_value_sp",
)


@component.add(
    name="SHARE OF RESIDUALS FROM CROPS",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_residuals_from_crops"},
)
def share_of_residuals_from_crops():
    """
    share of residuals for energy use obtained from crops. Not activated.
    """
    return _ext_constant_share_of_residuals_from_crops()


_ext_constant_share_of_residuals_from_crops = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "SHARE_OF_RESIDUALS_FROM_CROPS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_share_of_residuals_from_crops",
)


@component.add(
    name="SHARE OF SHRUBLAND",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_share_of_shrubland"},
)
def share_of_shrubland():
    """
    Share of shrubland relative to the summ of shrubland+other_land, is kept constant and equal to historical average per region
    """
    return _ext_constant_share_of_shrubland()


_ext_constant_share_of_shrubland = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "SHARE_OF_SHRUBLAND*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_share_of_shrubland",
)


@component.add(
    name="SHARE OF WOOD FOR ENERGY EXTRACTION BY REGION",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_wood_for_energy_extraction_by_region"
    },
)
def share_of_wood_for_energy_extraction_by_region():
    """
    share of the world demand for wood for energy that comes from each region
    """
    return _ext_constant_share_of_wood_for_energy_extraction_by_region()


_ext_constant_share_of_wood_for_energy_extraction_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "SHARE_OF_WOOD_FOR_ENERGY_EXTRACTION_BY_REGION*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_share_of_wood_for_energy_extraction_by_region",
)


@component.add(
    name="SHARE OF WOOD FOR INDUSTRY EXTRACTION BY REGION",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_share_of_wood_for_industry_extraction_by_region"
    },
)
def share_of_wood_for_industry_extraction_by_region():
    """
    share of the world demand for wood for industry that comes from each region
    """
    return _ext_constant_share_of_wood_for_industry_extraction_by_region()


_ext_constant_share_of_wood_for_industry_extraction_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "SHARE_OF_WOOD_FOR_INDUSTRY_EXTRACTION_BY_REGION*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_share_of_wood_for_industry_extraction_by_region",
)


@component.add(
    name="SOIL CARBON DENSITY DATA BY LAND USE",
    units="tC/ha",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_soil_carbon_density_data_by_land_use"},
)
def soil_carbon_density_data_by_land_use():
    """
    SOC before: Soil carbon stock density data (soil carbon database) before conversion, and based also in assumptions for "land use factors" (current trends). Source: Assumed carbon stock in GCAM land use module. Van de Ven et al. 2021,.The potential land requirements and related land use change emissions of solar energy Notes: Vegetation in cropland, wetland and snow-ice-waterbodies data should be reviewed and improved. In the case of waterbodies soil carbon stock, and wetland carbon data, the numbers should be corrected in the future. For this version their area is cte so this information is not used.
    """
    return _ext_constant_soil_carbon_density_data_by_land_use()


_ext_constant_soil_carbon_density_data_by_land_use = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "SOIL_CARBON_DATA_REGIONSXLAND",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_soil_carbon_density_data_by_land_use",
)


@component.add(
    name="SWITCH AFFORESTATION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_afforestation_sp"},
)
def switch_afforestation_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_afforestation_sp()


_ext_constant_switch_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_AFFORESTATION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_afforestation_sp",
)


@component.add(
    name="SWITCH CROPLAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_cropland_protection_sp"},
)
def switch_cropland_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_cropland_protection_sp()


_ext_constant_switch_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_CROPLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_cropland_protection_sp",
)


@component.add(
    name="SWITCH DIET CHANGE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_diet_change_sp"},
)
def switch_diet_change_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_diet_change_sp()


_ext_constant_switch_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_DIET_CHANGE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_diet_change_sp",
)


@component.add(
    name="SWITCH EFFECT OIL AND GAS ON AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp"
    },
)
def switch_effect_oil_and_gas_on_agriculture_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter Policy to simulate the effect of gas and oil shortage on agriculture, the high input industrial agriculture goes to an agriculture of low inputs and low yields
    """
    return _ext_constant_switch_effect_oil_and_gas_on_agriculture_sp()


_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_effect_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="SWITCH FOREST PLANTATIONS SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_forest_plantations_sp"},
)
def switch_forest_plantations_sp():
    """
    0: deactivate policy the scenario parameter , increase of plantations land driven only by trends 1: Activate the scenario parameter
    """
    return _ext_constant_switch_forest_plantations_sp()


_ext_constant_switch_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_FOREST_PLANTATIONS_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_forest_plantations_sp",
)


@component.add(
    name="SWITCH FORESTRY SELF SUFFICIENCY SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_forestry_self_sufficiency_sp"},
)
def switch_forestry_self_sufficiency_sp():
    """
    IF =1 the policy of forest suficiency starts, regions increase the share of self consumption of wood
    """
    return _ext_constant_switch_forestry_self_sufficiency_sp()


_ext_constant_switch_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_forestry_self_sufficiency_sp",
)


@component.add(
    name="SWITCH GRASSLAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_grassland_protection_sp"},
)
def switch_grassland_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_grassland_protection_sp()


_ext_constant_switch_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_GRASSLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_grassland_protection_sp",
)


@component.add(
    name="SWITCH INDUSTRIAL AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_industrial_agriculture_sp"},
)
def switch_industrial_agriculture_sp():
    """
    policy on or off
    """
    return _ext_constant_switch_industrial_agriculture_sp()


_ext_constant_switch_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_industrial_agriculture_sp",
)


@component.add(
    name="SWITCH LAND PRODUCTS GLOBAL POOL SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_land_products_global_pool_sp"},
)
def switch_land_products_global_pool_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_land_products_global_pool_sp()


_ext_constant_switch_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_land_products_global_pool_sp",
)


@component.add(
    name="SWITCH MANAGED FOREST PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_managed_forest_protection_sp"},
)
def switch_managed_forest_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_managed_forest_protection_sp()


_ext_constant_switch_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_managed_forest_protection_sp",
)


@component.add(
    name="SWITCH NATURAL LAND PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_natural_land_protection_sp"},
)
def switch_natural_land_protection_sp():
    """
    Switch to activate the protection of all kind of land with potential ecological value: forests + grasslands + shrubland + other land 0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_natural_land_protection_sp()


_ext_constant_switch_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_natural_land_protection_sp",
)


@component.add(
    name="SWITCH POLICY LAND PROTECTION FROM SOLAR PV SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_land_protection_from_solar_pv_sp"
    },
)
def switch_policy_land_protection_from_solar_pv_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_policy_land_protection_from_solar_pv_sp()


_ext_constant_switch_policy_land_protection_from_solar_pv_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_POLICY_LAND_PROTECTION_FROM_SOLAR_PV_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_policy_land_protection_from_solar_pv_sp",
)


@component.add(
    name="SWITCH POLICY MAXIMUM SHARE SOLAR URBAN SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_maximum_share_solar_urban_sp"
    },
)
def switch_policy_maximum_share_solar_urban_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_policy_maximum_share_solar_urban_sp()


_ext_constant_switch_policy_maximum_share_solar_urban_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_POLICY_MAXIMUM_SHARE_SOLAR_URBAN_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_policy_maximum_share_solar_urban_sp",
)


@component.add(
    name="SWITCH PRIMARY FOREST PROTECTION SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_primary_forest_protection_sp"},
)
def switch_primary_forest_protection_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_primary_forest_protection_sp()


_ext_constant_switch_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_primary_forest_protection_sp",
)


@component.add(
    name="SWITCH REGENERATIVE AGRICULTURE SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_regenerative_agriculture_sp"},
)
def switch_regenerative_agriculture_sp():
    """
    policy on or off
    """
    return _ext_constant_switch_regenerative_agriculture_sp()


_ext_constant_switch_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_SWITCH_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_regenerative_agriculture_sp",
)


@component.add(
    name="SWITCH SOIL MANAGEMENT IN GRASSLANDS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_soil_management_in_grasslands_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> soil management in grasslands policy is applied IF switch_between_wiliam_and_constant_outreal=0---> soil management in grasslands policy is not applied
    """
    return 0


@component.add(
    name="SWITCH SOLAR LAND FROM OTHERS SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_solar_land_from_others_sp"},
)
def switch_solar_land_from_others_sp():
    """
    0: deactivate policy the scenario parameter 1: Activate the scenario parameter
    """
    return _ext_constant_switch_solar_land_from_others_sp()


_ext_constant_switch_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_solar_land_from_others_sp",
)


@component.add(
    name="SWITCH URBAN LAND DENSITY SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_urban_land_density_sp"},
)
def switch_urban_land_density_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> urban land density policy is applied IF switch_between_wiliam_and_constant_outreal=0---> urban land density policy is not applied
    """
    return _ext_constant_switch_urban_land_density_sp()


_ext_constant_switch_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_URBAN_LAND_DENSITY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_urban_land_density_sp",
)


@component.add(
    name="SWITCH WATER EFFICIENCY SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def switch_water_efficiency_sp():
    """
    IF switch_between_wiliam_and_constant_outreal=1---> water efficiency policy is applied IF switch_between_wiliam_and_constant_outreal=0---> water efficiency policy is not applied
    """
    return 1


@component.add(
    name="TIME HISTORICAL DATA LAND MODULE",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_historical_data_land_module"},
)
def time_historical_data_land_module():
    """
    time of historical data of Land and Water module (2019). Previous to this year historical values are used as results.
    """
    return _ext_constant_time_historical_data_land_module()


_ext_constant_time_historical_data_land_module = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TIME_HISTORICAL_DATA_LAND_MODULE",
    {},
    _root,
    {},
    "_ext_constant_time_historical_data_land_module",
)


@component.add(
    name="TIME OF FOREST MATURATION",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_time_of_forest_maturation"},
)
def time_of_forest_maturation():
    """
    average time of forest maturation
    """
    return _ext_constant_time_of_forest_maturation()


_ext_constant_time_of_forest_maturation = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "TIME_OF_FOREST_MATURATION*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_time_of_forest_maturation",
)


@component.add(
    name="TIME OF TRANSITION TO REGENERATIVE AGRICULTURE",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_time_of_transition_to_regenerative_agriculture"
    },
)
def time_of_transition_to_regenerative_agriculture():
    """
    Time to achieve a fully productive regenerative agriculture
    """
    return _ext_constant_time_of_transition_to_regenerative_agriculture()


_ext_constant_time_of_transition_to_regenerative_agriculture = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TIME_OF_TRANSITION_TO_REGENERATIVE_AGRICULTURE*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_time_of_transition_to_regenerative_agriculture",
)


@component.add(
    name="TRANSFORMATION MATRICES REGIONS TO ZONES",
    subscripts=["REGIONS 9 I", "CLIMATIC ZONES I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_transformation_matrices_regions_to_zones"
    },
)
def transformation_matrices_regions_to_zones():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'transformation_matrices' , 'MATRIX_REGIONS_TO_ZONES_SNOW_ICE_WATERBODIES_9_R' )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["REGIONS 9 I", "CLIMATIC ZONES I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST PRIMARY"]] = True
    def_subs.loc[:, :, ["FOREST PLANTATIONS"]] = True
    def_subs.loc[:, :, ["SHRUBLAND"]] = True
    def_subs.loc[:, :, ["WETLAND"]] = True
    def_subs.loc[:, :, ["URBAN LAND"]] = True
    def_subs.loc[:, :, ["SOLAR LAND"]] = True
    def_subs.loc[:, :, ["OTHER LAND"]] = True
    def_subs.loc[:, :, ["GRASSLAND"]] = True
    value.values[def_subs.values] = (
        _ext_constant_transformation_matrices_regions_to_zones().values[def_subs.values]
    )
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = 0
    return value


_ext_constant_transformation_matrices_regions_to_zones = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_CROPLAND_RAINFED_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["CROPLAND RAINFED"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_transformation_matrices_regions_to_zones",
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_CROPLAND_IRRIGATED_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["CROPLAND IRRIGATED"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_MANAGED_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["FOREST MANAGED"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_PRIMARY_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["FOREST PRIMARY"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_FOREST_PLANTATIONS_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["FOREST PLANTATIONS"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_SHRUBLAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["SHRUBLAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_WETLAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["WETLAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_URBAN_LAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["URBAN LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_SOLAR_LAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["SOLAR LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_OTHER_LAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["OTHER LAND"],
    },
)

_ext_constant_transformation_matrices_regions_to_zones.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_REGIONS_TO_ZONES_GRASSLAND_9_R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "LANDS I": ["GRASSLAND"],
    },
)


@component.add(
    name="TRANSFORMATION MATRICES ZONES TO REGIONS",
    subscripts=["CLIMATIC ZONES I", "REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="Normal, External",
    depends_on={
        "__external__": "_ext_constant_transformation_matrices_zones_to_regions"
    },
)
def transformation_matrices_zones_to_regions():
    """
    GET_DIRECT_CONSTANTS('model_parameters/land_and_water/land_and_water_parame ters.xlsx', 'transformation_matrices' , 'MATRIX_REGIONS_TO_ZONES_SNOW_ICE_WATERBODIES_9_R' )
    """
    value = xr.DataArray(
        np.nan,
        {
            "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LANDS I": _subscript_dict["LANDS I"],
        },
        ["CLIMATIC ZONES I", "REGIONS 9 I", "LANDS I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CROPLAND RAINFED"]] = True
    def_subs.loc[:, :, ["CROPLAND IRRIGATED"]] = True
    def_subs.loc[:, :, ["FOREST MANAGED"]] = True
    def_subs.loc[:, :, ["FOREST PRIMARY"]] = True
    def_subs.loc[:, :, ["FOREST PLANTATIONS"]] = True
    def_subs.loc[:, :, ["SHRUBLAND"]] = True
    def_subs.loc[:, :, ["WETLAND"]] = True
    def_subs.loc[:, :, ["URBAN LAND"]] = True
    def_subs.loc[:, :, ["SOLAR LAND"]] = True
    def_subs.loc[:, :, ["OTHER LAND"]] = True
    value.values[def_subs.values] = (
        _ext_constant_transformation_matrices_zones_to_regions().values[def_subs.values]
    )
    value.loc[:, :, ["SNOW ICE WATERBODIES"]] = 0
    return value


_ext_constant_transformation_matrices_zones_to_regions = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_CROPLAND_RAINFED_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["CROPLAND RAINFED"],
    },
    _root,
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_transformation_matrices_zones_to_regions",
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_CROPLAND_IRRIGATED_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["CROPLAND IRRIGATED"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_MANAGED_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["FOREST MANAGED"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_PRIMARY_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["FOREST PRIMARY"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_FOREST_PLANTATIONS_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["FOREST PLANTATIONS"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_SHRUBLAND_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["SHRUBLAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_WETLAND_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["WETLAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_URBAN_LAND_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["URBAN LAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_SOLAR_LAND_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["SOLAR LAND"],
    },
)

_ext_constant_transformation_matrices_zones_to_regions.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "transformation_matrices",
    "MATRIX_ZONES_TO_REGIONS_OTHER_LAND_8_Z",
    {
        "CLIMATIC ZONES I": _subscript_dict["CLIMATIC ZONES I"],
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": ["OTHER LAND"],
    },
)


@component.add(
    name="TRENDS OF LAND USE DEMAND",
    units="km2/Year",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_trends_of_land_use_demand"},
)
def trends_of_land_use_demand():
    """
    Trends of land use demand got from historical data (lineal approximation), some values are corrected from the historical ones because the trends do not seem to stand fo the future
    """
    return _ext_constant_trends_of_land_use_demand()


_ext_constant_trends_of_land_use_demand = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "TRENDS_OF_LAND_USE_DEMAND_BY_REGION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_trends_of_land_use_demand",
)


@component.add(
    name="TRENDS OF YIELD CHANGE R AND I",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_trends_of_yield_change_r_and_i"},
)
def trends_of_yield_change_r_and_i():
    return _ext_constant_trends_of_yield_change_r_and_i()


_ext_constant_trends_of_yield_change_r_and_i = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "TRENDS_OF_YIELD_CHANGE_R_AND_I",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_trends_of_yield_change_r_and_i",
)


@component.add(
    name="VARIATION LINEAR BLUE WATER REGION SECT",
    units="hm3",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_variation_linear_blue_water_region_sect"
    },
)
def variation_linear_blue_water_region_sect():
    """
    Load the variation of the Blue Water values, for the 35 Regions and 62 Sectors. Data from Ercin and Hoekstra (2014): Water footprint scenarios for 2050: A global analysis.Table 7, Scenario S4.
    """
    return _ext_constant_variation_linear_blue_water_region_sect()


_ext_constant_variation_linear_blue_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dBlue",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_variation_linear_blue_water_region_sect",
)


@component.add(
    name="VARIATION LINEAR GREEN WATER REGION SECT",
    units="hm3",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_variation_linear_green_water_region_sect"
    },
)
def variation_linear_green_water_region_sect():
    """
    Load the variation of the Green Water values, for the 35 Regions and 62 Sectors. Data from Ercin and Hoekstra (2014): Water footprint scenarios for 2050: A global analysis.Table 7, Scenario S4.
    """
    return _ext_constant_variation_linear_green_water_region_sect()


_ext_constant_variation_linear_green_water_region_sect = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Water",
    "dGreen",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_variation_linear_green_water_region_sect",
)


@component.add(
    name="VEGETATION CARBON DENSITY DATA BY LAND USE",
    units="tC/ha",
    subscripts=["REGIONS 9 I", "LANDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_vegetation_carbon_density_data_by_land_use"
    },
)
def vegetation_carbon_density_data_by_land_use():
    """
    Vegetation carbon stock data (vegetation carbon database) SOC before: Soil carbon stock density data (soil carbon database) before conversion, and based also in assumptions for "land use factors" (current trends). Source: Assumed carbon stock in GCAM land use module. Van de Ven et al. 2021,.The potential land requirements and related land use change emissions of solar energy Notes: Vegetation in cropland, wetland and snow-ice-waterbodies data should be reviewed and improved. In the case of waterbodies soil carbon stock, and wetland carbon data, the numbers should be corrected in the future. For this version their area is cte so this information is not used.
    """
    return _ext_constant_vegetation_carbon_density_data_by_land_use()


_ext_constant_vegetation_carbon_density_data_by_land_use = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "VEGETATION_CARBON_DATA_REGIONSXLAND",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LANDS I": _subscript_dict["LANDS I"],
    },
    "_ext_constant_vegetation_carbon_density_data_by_land_use",
)


@component.add(
    name="VERTICAL LAND MOVEMENT",
    units="m/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_vertical_land_movement"},
)
def vertical_land_movement():
    """
    the vertical land movement is a generic term used to describe several processes affecting the elevation at a given location (tectonic movements, subsidence, ground water extraction) that cause the land to move up or down.
    """
    return _ext_constant_vertical_land_movement()


_ext_constant_vertical_land_movement = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "land_uses",
    "VI_CONSTANT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_vertical_land_movement",
)


@component.add(
    name="WBS PLUS BIOMASS EXANSION FACTOR FOREST",
    units="t/m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_wbs_plus_biomass_exansion_factor_forest"
    },
)
def wbs_plus_biomass_exansion_factor_forest():
    """
    wbs plus biomass exansion factor forest
    """
    return _ext_constant_wbs_plus_biomass_exansion_factor_forest()


_ext_constant_wbs_plus_biomass_exansion_factor_forest = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "WBS_PLUS_BIOMASS_EXANSION_FACTOR_FOREST*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_wbs_plus_biomass_exansion_factor_forest",
)


@component.add(
    name="WIDTH OF CROPS DISTRIBUTION AMONG USES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_width_of_crops_distribution_among_uses_sp"
    },
)
def width_of_crops_distribution_among_uses_sp():
    """
    WIDTH_OF_CROPS_DISTRIBUTION_AMONG_USES. width specifies how big a gap in priority is required to have the allocation go first to higher priority with only leftovers going to lower priority. When the distance between any two priorities exceeds width and the higher priority does not receive its full request the lower priority will receive nothing.
    """
    return _ext_constant_width_of_crops_distribution_among_uses_sp()


_ext_constant_width_of_crops_distribution_among_uses_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WIDTH_OF_CROPS_DISTRIBUTION_USES*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_width_of_crops_distribution_among_uses_sp",
)


@component.add(
    name="WIDTH OF FORESTRY PRODUCTS DISTRIBUTION AMONG USES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_width_of_forestry_products_distribution_among_uses_sp"
    },
)
def width_of_forestry_products_distribution_among_uses_sp():
    """
    WIDTH_OF_FORESTRY_PRODUCTS_DISTRIBUTION_AMONG_USES. width specifies how big a gap in priority is required to have the allocation go first to higher priority with only leftovers going to lower priority. When the distance between any two priorities exceeds width and the higher priority does not receive its full request the lower priority will receive nothing.
    """
    return _ext_constant_width_of_forestry_products_distribution_among_uses_sp()


_ext_constant_width_of_forestry_products_distribution_among_uses_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WIDTH_OF_FORESTRY_DISTRIBUTION_USES*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_width_of_forestry_products_distribution_among_uses_sp",
)


@component.add(
    name="WIDTH OF LAND PRODUCTS DISTRIBUTION AMONG REGIONS SP",
    units="DMNL",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_width_of_land_products_distribution_among_regions_sp"
    },
)
def width_of_land_products_distribution_among_regions_sp():
    """
    WIDTH_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS. Parameter to make the priorities of the allocation to be more or less sharp. width specifies how big a gap in priority is required to have the allocation go first to higher priority with only leftovers going to lower priority. When the distance between any two priorities exceeds width and the higher priority does not receive its full request the lower priority will receive nothing.
    """
    return _ext_constant_width_of_land_products_distribution_among_regions_sp()


_ext_constant_width_of_land_products_distribution_among_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WIDTH_OF_LAND_PRODUCTS_DISTRIBUTION_AMONG_REGIONS",
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    "_ext_constant_width_of_land_products_distribution_among_regions_sp",
)


@component.add(
    name="WILLETT DIET PATTERNS OF POLICY DIETS SP",
    units="kg/(Year*people)",
    subscripts=["REGIONS 9 I", "FOODS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_willett_diet_patterns_of_policy_diets_sp"
    },
)
def willett_diet_patterns_of_policy_diets_sp():
    """
    Willett policy diet
    """
    return _ext_constant_willett_diet_patterns_of_policy_diets_sp()


_ext_constant_willett_diet_patterns_of_policy_diets_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "WILLET_DIET_PATTERN_OF_POLICY_DIETS_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "FOODS I": _subscript_dict["FOODS I"],
    },
    "_ext_constant_willett_diet_patterns_of_policy_diets_sp",
)


@component.add(
    name="WOOD DENSITY BY REGION",
    units="t/m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_wood_density_by_region"},
)
def wood_density_by_region():
    """
    wood density by region
    """
    return _ext_constant_wood_density_by_region()


_ext_constant_wood_density_by_region = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "forest",
    "WOOD_DENSITY_BY_REGION*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_wood_density_by_region",
)


@component.add(
    name="WOOD FUEL PRODUCTION",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_wood_fuel_production",
        "__data__": "_ext_data_wood_fuel_production",
        "time": 1,
    },
)
def wood_fuel_production():
    """
    wood fuel production for energy by region
    """
    return _ext_data_wood_fuel_production(time())


_ext_data_wood_fuel_production = ExtData(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "diet",
    "TIME_WOOD",
    "WOOD_FUEL",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_data_wood_fuel_production",
)


@component.add(
    name="YEAR FINAL AFFORESTATION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_afforestation_sp"},
)
def year_final_afforestation_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_afforestation_sp()


_ext_constant_year_final_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_AFFORESTATION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_afforestation_sp",
)


@component.add(
    name="YEAR FINAL CROPLAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_cropland_protection_sp"},
)
def year_final_cropland_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_cropland_protection_sp()


_ext_constant_year_final_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_CROPLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_cropland_protection_sp",
)


@component.add(
    name="YEAR FINAL DIET CHANGE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_diet_change_sp"},
)
def year_final_diet_change_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_diet_change_sp()


_ext_constant_year_final_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_DIET_CHANGE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_diet_change_sp",
)


@component.add(
    name="YEAR FINAL EFFECT OF OIL AND GAS ON AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def year_final_effect_of_oil_and_gas_on_agriculture_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="YEAR FINAL FOREST PLANTATIONS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_forest_plantations_sp"},
)
def year_final_forest_plantations_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_forest_plantations_sp()


_ext_constant_year_final_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_FOREST_PLANTATIONS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_forest_plantations_sp",
)


@component.add(
    name="YEAR FINAL FORESTRY SELF SUFFICIENCY SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_forestry_self_sufficiency_sp"
    },
)
def year_final_forestry_self_sufficiency_sp():
    """
    FORESTRY_SELF_SUFFICIENCY policy final year
    """
    return _ext_constant_year_final_forestry_self_sufficiency_sp()


_ext_constant_year_final_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_forestry_self_sufficiency_sp",
)


@component.add(
    name="YEAR FINAL GRASSLAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_grassland_protection_sp"},
)
def year_final_grassland_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_grassland_protection_sp()


_ext_constant_year_final_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_GRASSLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_grassland_protection_sp",
)


@component.add(
    name="YEAR FINAL INDUSTRIAL AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_industrial_agriculture_sp"},
)
def year_final_industrial_agriculture_sp():
    """
    policy final year
    """
    return _ext_constant_year_final_industrial_agriculture_sp()


_ext_constant_year_final_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_industrial_agriculture_sp",
)


@component.add(
    name="YEAR FINAL LAND PRODUCTS GLOBAL POOL SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_land_products_global_pool_sp"
    },
)
def year_final_land_products_global_pool_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_land_products_global_pool_sp()


_ext_constant_year_final_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_land_products_global_pool_sp",
)


@component.add(
    name="YEAR FINAL MANAGED FOREST PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_managed_forest_protection_sp"
    },
)
def year_final_managed_forest_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_managed_forest_protection_sp()


_ext_constant_year_final_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_managed_forest_protection_sp",
)


@component.add(
    name="YEAR FINAL NATURAL LAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_natural_land_protection_sp"},
)
def year_final_natural_land_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_natural_land_protection_sp()


_ext_constant_year_final_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_natural_land_protection_sp",
)


@component.add(
    name="YEAR FINAL PRIMARY FOREST PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_primary_forest_protection_sp"
    },
)
def year_final_primary_forest_protection_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_primary_forest_protection_sp()


_ext_constant_year_final_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_primary_forest_protection_sp",
)


@component.add(
    name="YEAR FINAL REGENERATIVE AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_regenerative_agriculture_sp"},
)
def year_final_regenerative_agriculture_sp():
    """
    policy final year
    """
    return _ext_constant_year_final_regenerative_agriculture_sp()


_ext_constant_year_final_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_FINAL_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_regenerative_agriculture_sp",
)


@component.add(
    name="YEAR FINAL SOIL MANAGEMENT IN GRASSLANDS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_soil_management_in_grasslands_sp"
    },
)
def year_final_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy final year
    """
    return _ext_constant_year_final_soil_management_in_grasslands_sp()


_ext_constant_year_final_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_SOIL_MANAGEMENT_GRASSLANDS_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_soil_management_in_grasslands_sp",
)


@component.add(
    name="YEAR FINAL SOLAR LAND FROM OTHERS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_solar_land_from_others_sp"},
)
def year_final_solar_land_from_others_sp():
    """
    Scenario parameter final year
    """
    return _ext_constant_year_final_solar_land_from_others_sp()


_ext_constant_year_final_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_solar_land_from_others_sp",
)


@component.add(
    name="YEAR FINAL URBAN LAND DENSITY SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_urban_land_density_sp"},
)
def year_final_urban_land_density_sp():
    """
    urban land density policy final year
    """
    return _ext_constant_year_final_urban_land_density_sp()


_ext_constant_year_final_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_URBAN_LAND_DENSITY_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_urban_land_density_sp",
)


@component.add(
    name="YEAR FINAL WATER EFFICIENCY SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_water_efficiency_sp"},
)
def year_final_water_efficiency_sp():
    """
    YEAR_FINAL_WATER_EFFICIENCY_SP
    """
    return _ext_constant_year_final_water_efficiency_sp()


_ext_constant_year_final_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_year_final_water_efficiency_sp",
)


@component.add(
    name="YEAR INITIAL AFFORESTATION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_afforestation_sp"},
)
def year_initial_afforestation_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_afforestation_sp()


_ext_constant_year_initial_afforestation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_AFFORESTATION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_afforestation_sp",
)


@component.add(
    name="YEAR INITIAL CROPLAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_cropland_protection_sp"},
)
def year_initial_cropland_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_cropland_protection_sp()


_ext_constant_year_initial_cropland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_CROPLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_cropland_protection_sp",
)


@component.add(
    name="YEAR INITIAL DIET CHANGE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_diet_change_sp"},
)
def year_initial_diet_change_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_diet_change_sp()


_ext_constant_year_initial_diet_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_DIET_CHANGE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_diet_change_sp",
)


@component.add(
    name="YEAR INITIAL EFFECT OF OIL AND GAS ON AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp"
    },
)
def year_initial_effect_of_oil_and_gas_on_agriculture_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp()


_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_EFFECT_OIL_AND_GAS_ON_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_effect_of_oil_and_gas_on_agriculture_sp",
)


@component.add(
    name="YEAR INITIAL FOREST PLANTATIONS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_forest_plantations_sp"},
)
def year_initial_forest_plantations_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_forest_plantations_sp()


_ext_constant_year_initial_forest_plantations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_FOREST_PLANTATIONS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_forest_plantations_sp",
)


@component.add(
    name="YEAR INITIAL FORESTRY SELF SUFFICIENCY SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_forestry_self_sufficiency_sp"
    },
)
def year_initial_forestry_self_sufficiency_sp():
    """
    FORESTRY_SELF_SUFFICIENCY policy initial year
    """
    return _ext_constant_year_initial_forestry_self_sufficiency_sp()


_ext_constant_year_initial_forestry_self_sufficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_FORESTRY_SELF_SUFFICIENCY_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_forestry_self_sufficiency_sp",
)


@component.add(
    name="YEAR INITIAL GRASSLAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_grassland_protection_sp"},
)
def year_initial_grassland_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_grassland_protection_sp()


_ext_constant_year_initial_grassland_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_GRASSLAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_grassland_protection_sp",
)


@component.add(
    name="YEAR INITIAL INDUSTRIAL AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_industrial_agriculture_sp"},
)
def year_initial_industrial_agriculture_sp():
    """
    policy intial year
    """
    return _ext_constant_year_initial_industrial_agriculture_sp()


_ext_constant_year_initial_industrial_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_INDUSTRIAL_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_industrial_agriculture_sp",
)


@component.add(
    name="YEAR INITIAL LAND PRODUCTS GLOBAL POOL SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_land_products_global_pool_sp"
    },
)
def year_initial_land_products_global_pool_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_land_products_global_pool_sp()


_ext_constant_year_initial_land_products_global_pool_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_LAND_PRODUCTS_GLOBAL_POOL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_land_products_global_pool_sp",
)


@component.add(
    name="YEAR INITIAL MANAGED FOREST PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_managed_forest_protection_sp"
    },
)
def year_initial_managed_forest_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_managed_forest_protection_sp()


_ext_constant_year_initial_managed_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_MANAGED_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_managed_forest_protection_sp",
)


@component.add(
    name="YEAR INITIAL NATURAL LAND PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_natural_land_protection_sp"
    },
)
def year_initial_natural_land_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_natural_land_protection_sp()


_ext_constant_year_initial_natural_land_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_NATURAL_LAND_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_natural_land_protection_sp",
)


@component.add(
    name="YEAR INITIAL PRIMARY FOREST PROTECTION SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_primary_forest_protection_sp"
    },
)
def year_initial_primary_forest_protection_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_primary_forest_protection_sp()


_ext_constant_year_initial_primary_forest_protection_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_PRIMARY_FOREST_PROTECTION_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_primary_forest_protection_sp",
)


@component.add(
    name="YEAR INITIAL REGENERATIVE AGRICULTURE SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_regenerative_agriculture_sp"
    },
)
def year_initial_regenerative_agriculture_sp():
    """
    policy initial year
    """
    return _ext_constant_year_initial_regenerative_agriculture_sp()


_ext_constant_year_initial_regenerative_agriculture_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "POLICY_YEAR_INITIAL_REGENERATIVE_AGRICULTURE_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_regenerative_agriculture_sp",
)


@component.add(
    name="YEAR INITIAL SOIL MANAGEMENT IN GRASSLANDS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_soil_management_in_grasslands_sp"
    },
)
def year_initial_soil_management_in_grasslands_sp():
    """
    soil management in grasslands policy initial year
    """
    return _ext_constant_year_initial_soil_management_in_grasslands_sp()


_ext_constant_year_initial_soil_management_in_grasslands_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_SOIL_MANAGEMENT_GRASSLANDS_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_soil_management_in_grasslands_sp",
)


@component.add(
    name="YEAR INITIAL SOLAR LAND FROM OTHERS SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_solar_land_from_others_sp"},
)
def year_initial_solar_land_from_others_sp():
    """
    Scenario parameter intial year
    """
    return _ext_constant_year_initial_solar_land_from_others_sp()


_ext_constant_year_initial_solar_land_from_others_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_SOLAR_LAND_FROM_OTHERS*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_solar_land_from_others_sp",
)


@component.add(
    name="YEAR INITIAL URBAN LAND DENSITY SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_urban_land_density_sp"},
)
def year_initial_urban_land_density_sp():
    """
    urban land density policy initial year
    """
    return _ext_constant_year_initial_urban_land_density_sp()


_ext_constant_year_initial_urban_land_density_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_URBAN_LAND_DENSITY_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_urban_land_density_sp",
)


@component.add(
    name="YEAR INITIAL WATER EFFICIENCY SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_water_efficiency_sp"},
)
def year_initial_water_efficiency_sp():
    """
    YEAR_INITIAL_WATER_EFFICIENCY_SP
    """
    return _ext_constant_year_initial_water_efficiency_sp()


_ext_constant_year_initial_water_efficiency_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_WATER_EFFICIENCY_SP*",
    {},
    _root,
    {},
    "_ext_constant_year_initial_water_efficiency_sp",
)


@component.add(
    name="YIELDS ALL MANAGEMENT 2019",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_yields_all_management_2019"},
)
def yields_all_management_2019():
    return _ext_constant_yields_all_management_2019()


_ext_constant_yields_all_management_2019 = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "croplands",
    "YIELDS_ALL_MANAGEMENTS_2019",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_constant_yields_all_management_2019",
)
