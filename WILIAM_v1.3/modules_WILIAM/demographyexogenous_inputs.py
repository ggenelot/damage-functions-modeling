"""
Module demographyexogenous_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="A EXPONENTIAL LEAB TO MR",
    units="DMNL",
    subscripts=["SEX I", "AGE COHORTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_a_exponential_leab_to_mr"},
)
def a_exponential_leab_to_mr():
    """
    Parameter A of the equation that related the life expectancy at birth and the mortality rates (MR = A * exp(B * LEAB)
    """
    return _ext_constant_a_exponential_leab_to_mr()


_ext_constant_a_exponential_leab_to_mr = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "A_EXPONENTIAL_LEAB_TO_MR*",
    {
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    _root,
    {
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    "_ext_constant_a_exponential_leab_to_mr",
)


@component.add(
    name="AVERAGE PEOPLE PER HOUSEHOLD NON EU REGIONS TIMESERIES TARGET SP",
    units="people/household",
    subscripts=["REGIONS 8 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
        "__lookup__": "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
    },
)
def average_people_per_household_non_eu_regions_timeseries_target_sp(
    x, final_subs=None
):
    """
    Scenario parameter setting the number of people per household for the non EU regions through timeseries 2015-2100.
    """
    return _ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp(
        x, final_subs
    )


_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp = (
    ExtLookup(
        "scenario_parameters/scenario_parameters.xlsx",
        "demography",
        "time_index_2015_2100",
        "AVERAGE_PEOPLE_PER_HOUSEHOLD_NON_EU_REGIONS_TIMESERIES_TARGET_SP",
        {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]},
        _root,
        {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]},
        "_ext_lookup_average_people_per_household_non_eu_regions_timeseries_target_sp",
    )
)


@component.add(
    name="B EXPONENTIAL LEAB TO MR",
    units="DMNL",
    subscripts=["SEX I", "AGE COHORTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_b_exponential_leab_to_mr"},
)
def b_exponential_leab_to_mr():
    """
    Parameter B of the equation that related the life expectancy at birth and the mortality rates (MR = A * exp(B * LEAB)
    """
    return _ext_constant_b_exponential_leab_to_mr()


_ext_constant_b_exponential_leab_to_mr = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "B_EXPONENTIAL_LEAB_TO_MR*",
    {
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    _root,
    {
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    "_ext_constant_b_exponential_leab_to_mr",
)


@component.add(
    name="BASE NUMBER OF HOUSEHOLDS",
    units="households",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_number_of_households"},
)
def base_number_of_households():
    """
    Base number of households
    """
    return _ext_constant_base_number_of_households()


_ext_constant_base_number_of_households = ExtConstant(
    "model_parameters/economy/Consumption.xlsx",
    "BASE_Number_households",
    "IMV_BASE_NUMBER_OF_HOUSEHOLDS",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
    },
    "_ext_constant_base_number_of_households",
)


@component.add(
    name="CAL POPULATION",
    units="people",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_cal_population",
        "__data__": "_ext_data_cal_population",
        "time": 1,
    },
)
def cal_population():
    """
    Variable for calibration porpuses regional population by year
    """
    return _ext_data_cal_population(time())


_ext_data_cal_population = ExtData(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_TIME_POP_CAL",
    "CAL_POPULATION",
    None,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_cal_population",
)


@component.add(
    name="HISTORIC EMIGRATIONS RATE",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historic_emigrations_rate"},
)
def historic_emigrations_rate():
    """
    Share of population that emigrates per region
    """
    return _ext_constant_historic_emigrations_rate()


_ext_constant_historic_emigrations_rate = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORIC_EMIGRATIONS_RATE",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_historic_emigrations_rate",
)


@component.add(
    name="HISTORICAL FERTILITY RATES 2005 2010",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2005_2010"},
)
def historical_fertility_rates_2005_2010():
    """
    Exogenous data of the historical fertility rates in the period 2005-2010.
    """
    return _ext_constant_historical_fertility_rates_2005_2010()


_ext_constant_historical_fertility_rates_2005_2010 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2005_2010",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_historical_fertility_rates_2005_2010",
)


@component.add(
    name="HISTORICAL FERTILITY RATES 2010 2015",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2010_2015"},
)
def historical_fertility_rates_2010_2015():
    """
    Exogenous data of the historical fertility rates in the period 2010-2015.
    """
    return _ext_constant_historical_fertility_rates_2010_2015()


_ext_constant_historical_fertility_rates_2010_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2010_2015",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_historical_fertility_rates_2010_2015",
)


@component.add(
    name="HISTORICAL FERTILITY RATES 2015 2020",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_fertility_rates_2015_2020"},
)
def historical_fertility_rates_2015_2020():
    """
    Exogenous data of the historical fertility rates in the period 2015-2020.
    """
    return _ext_constant_historical_fertility_rates_2015_2020()


_ext_constant_historical_fertility_rates_2015_2020 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_FERTILITY_RATES_2015_2020",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_historical_fertility_rates_2015_2020",
)


@component.add(
    name="HISTORICAL GENDER BIRTH RATIO 2005 2010",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2005_2010"
    },
)
def historical_gender_birth_ratio_2005_2010():
    """
    Exogenous data of the historical gender rate in birth in the period 2005-2010.
    """
    return _ext_constant_historical_gender_birth_ratio_2005_2010()


_ext_constant_historical_gender_birth_ratio_2005_2010 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2005_2010",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_historical_gender_birth_ratio_2005_2010",
)


@component.add(
    name="HISTORICAL GENDER BIRTH RATIO 2010 2015",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2010_2015"
    },
)
def historical_gender_birth_ratio_2010_2015():
    """
    Exogenous data of the historical gender rate in birth in the period 2010-2015.
    """
    return _ext_constant_historical_gender_birth_ratio_2010_2015()


_ext_constant_historical_gender_birth_ratio_2010_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2010_2015",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_historical_gender_birth_ratio_2010_2015",
)


@component.add(
    name="HISTORICAL GENDER BIRTH RATIO 2015 2020",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_gender_birth_ratio_2015_2020"
    },
)
def historical_gender_birth_ratio_2015_2020():
    """
    Exogenous data of the historical gender rate in birth in the period 2015-2020.
    """
    return _ext_constant_historical_gender_birth_ratio_2015_2020()


_ext_constant_historical_gender_birth_ratio_2015_2020 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "HISTORICAL_GENDER_BIRTH_RATIO_2015_2020",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_historical_gender_birth_ratio_2015_2020",
)


@component.add(
    name="HISTORICAL LIFE EXPECTANCY AT BIRTH",
    units="Years",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_historical_life_expectancy_at_birth",
        "__data__": "_ext_data_historical_life_expectancy_at_birth",
        "time": 1,
    },
)
def historical_life_expectancy_at_birth():
    """
    Historical life expectancy at birth for regions and gender.
    """
    return _ext_data_historical_life_expectancy_at_birth(time())


_ext_data_historical_life_expectancy_at_birth = ExtData(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_AUSTRIA",
    "interpolate",
    {"REGIONS 35 I": ["AUSTRIA"], "SEX I": _subscript_dict["SEX I"]},
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    "_ext_data_historical_life_expectancy_at_birth",
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_BELGIUM",
    "interpolate",
    {"REGIONS 35 I": ["BELGIUM"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_BULGARIA",
    "interpolate",
    {"REGIONS 35 I": ["BULGARIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CROATIA",
    "interpolate",
    {"REGIONS 35 I": ["CROATIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CYPRUS",
    "interpolate",
    {"REGIONS 35 I": ["CYPRUS"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CZECH_REPUBLIC",
    "interpolate",
    {"REGIONS 35 I": ["CZECH REPUBLIC"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_DENMARK",
    "interpolate",
    {"REGIONS 35 I": ["DENMARK"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ESTONIA",
    "interpolate",
    {"REGIONS 35 I": ["ESTONIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_FINLAND",
    "interpolate",
    {"REGIONS 35 I": ["FINLAND"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_FRANCE",
    "interpolate",
    {"REGIONS 35 I": ["FRANCE"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_GERMANY",
    "interpolate",
    {"REGIONS 35 I": ["GERMANY"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_GREECE",
    "interpolate",
    {"REGIONS 35 I": ["GREECE"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_HUNGARY",
    "interpolate",
    {"REGIONS 35 I": ["HUNGARY"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_IRELAND",
    "interpolate",
    {"REGIONS 35 I": ["IRELAND"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ITALY",
    "interpolate",
    {"REGIONS 35 I": ["ITALY"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LATVIA",
    "interpolate",
    {"REGIONS 35 I": ["LATVIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LITHUANIA",
    "interpolate",
    {"REGIONS 35 I": ["LITHUANIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LUXEMBOURG",
    "interpolate",
    {"REGIONS 35 I": ["LUXEMBOURG"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_MALTA",
    "interpolate",
    {"REGIONS 35 I": ["MALTA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_NETHERLANDS",
    "interpolate",
    {"REGIONS 35 I": ["NETHERLANDS"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_POLAND",
    "interpolate",
    {"REGIONS 35 I": ["POLAND"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_PORTUGAL",
    "interpolate",
    {"REGIONS 35 I": ["PORTUGAL"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_ROMANIA",
    "interpolate",
    {"REGIONS 35 I": ["ROMANIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SLOVAKIA",
    "interpolate",
    {"REGIONS 35 I": ["SLOVAKIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SLOVENIA",
    "interpolate",
    {"REGIONS 35 I": ["SLOVENIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SPAIN",
    "interpolate",
    {"REGIONS 35 I": ["SPAIN"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_SWEDEN",
    "interpolate",
    {"REGIONS 35 I": ["SWEDEN"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_UK",
    "interpolate",
    {"REGIONS 35 I": ["UK"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_CHINA",
    "interpolate",
    {"REGIONS 35 I": ["CHINA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_EASOC",
    "interpolate",
    {"REGIONS 35 I": ["EASOC"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_INDIA",
    "interpolate",
    {"REGIONS 35 I": ["INDIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LATAM",
    "interpolate",
    {"REGIONS 35 I": ["LATAM"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_RUSSIA",
    "interpolate",
    {"REGIONS 35 I": ["RUSSIA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_USMCA",
    "interpolate",
    {"REGIONS 35 I": ["USMCA"], "SEX I": _subscript_dict["SEX I"]},
)

_ext_data_historical_life_expectancy_at_birth.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "historical_time",
    "historical_life_expectancy_at_birth_LROW",
    "interpolate",
    {"REGIONS 35 I": ["LROW"], "SEX I": _subscript_dict["SEX I"]},
)


@component.add(
    name="historical population regions lt",
    units="people",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historical_population_regions_lt",
        "__lookup__": "_ext_lookup_historical_population_regions_lt",
    },
)
def historical_population_regions_lt(x, final_subs=None):
    """
    Historical population in regions.
    """
    return _ext_lookup_historical_population_regions_lt(x, final_subs)


_ext_lookup_historical_population_regions_lt = ExtLookup(
    "model_parameters/demography/demography.xlsx",
    "World",
    "time_historicalPop",
    "HistPopLT",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_historical_population_regions_lt",
)


@component.add(
    name="INITIAL RATIO EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_ratio_eu_households_per_100_people"
    },
)
def initial_ratio_eu_households_per_100_people():
    """
    Initial ratio of households per 100 people
    """
    return _ext_constant_initial_ratio_eu_households_per_100_people()


_ext_constant_initial_ratio_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "INITIAL_RATIO_EU_HOUSEHOLDS_PER_100_PEOPLE*",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_initial_ratio_eu_households_per_100_people",
)


@component.add(
    name="LIFE EXPECTANCY AT BIRTH AVERAGES SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_averages_sp"},
)
def life_expectancy_at_birth_averages_sp():
    """
    Selection of the values for the high life expectancy at birth (historical average)
    """
    return _ext_constant_life_expectancy_at_birth_averages_sp()


_ext_constant_life_expectancy_at_birth_averages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_AVERAGES_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    "_ext_constant_life_expectancy_at_birth_averages_sp",
)


@component.add(
    name="LIFE EXPECTANCY AT BIRTH MAXIMUMS SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_maximums_sp"},
)
def life_expectancy_at_birth_maximums_sp():
    """
    Selection of the values for the high life expectancy at birth (historical maximum)
    """
    return _ext_constant_life_expectancy_at_birth_maximums_sp()


_ext_constant_life_expectancy_at_birth_maximums_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_MAXIMUMS_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    "_ext_constant_life_expectancy_at_birth_maximums_sp",
)


@component.add(
    name="LIFE EXPECTANCY AT BIRTH MINIMUMS SP",
    units="Years/(Years*Years)",
    subscripts=["REGIONS 35 I", "SEX I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_life_expectancy_at_birth_minimums_sp"},
)
def life_expectancy_at_birth_minimums_sp():
    """
    Selection of the values for the high life expectancy at birth (historical minimum)
    """
    return _ext_constant_life_expectancy_at_birth_minimums_sp()


_ext_constant_life_expectancy_at_birth_minimums_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "LEAB_MINIMUMS_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
    },
    "_ext_constant_life_expectancy_at_birth_minimums_sp",
)


@component.add(
    name="MAX VARIATION EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_max_variation_eu_households_per_100_people"
    },
)
def max_variation_eu_households_per_100_people():
    """
    Maximum annual variations in the ratio of households per 100 people.
    """
    return _ext_constant_max_variation_eu_households_per_100_people()


_ext_constant_max_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MAX_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_max_variation_eu_households_per_100_people",
)


@component.add(
    name="MAXIMUM LIFE EXPECTANCY AT BIRTH",
    units="Years",
    subscripts=["SEX I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_life_expectancy_at_birth"},
)
def maximum_life_expectancy_at_birth():
    """
    Maximum of the life expectancy at birth to human beings.
    """
    return _ext_constant_maximum_life_expectancy_at_birth()


_ext_constant_maximum_life_expectancy_at_birth = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "MAX_LIFE_EXPECTANCY_AT_BIRTH",
    {"SEX I": _subscript_dict["SEX I"]},
    _root,
    {"SEX I": _subscript_dict["SEX I"]},
    "_ext_constant_maximum_life_expectancy_at_birth",
)


@component.add(
    name="MEAN VARIATION EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_mean_variation_eu_households_per_100_people"
    },
)
def mean_variation_eu_households_per_100_people():
    """
    Average annual variations in the ratio of households per 100 people
    """
    return _ext_constant_mean_variation_eu_households_per_100_people()


_ext_constant_mean_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MEAN_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_mean_variation_eu_households_per_100_people",
)


@component.add(
    name="MIN HISTORICAL MORTALITY RATE",
    units="people/(Year*kpeople)",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_min_historical_mortality_rate"},
)
def min_historical_mortality_rate():
    """
    Minimum historical mortality rate to constraint the modelling of deaths.
    """
    return _ext_constant_min_historical_mortality_rate()


_ext_constant_min_historical_mortality_rate = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_HISTORICAL_MORTALITY_RATE",
    {},
    _root,
    {},
    "_ext_constant_min_historical_mortality_rate",
)


@component.add(
    name="MIN VARIATION EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_min_variation_eu_households_per_100_people"
    },
)
def min_variation_eu_households_per_100_people():
    """
    Minimum annual variations in the ratio of households per 100 people
    """
    return _ext_constant_min_variation_eu_households_per_100_people()


_ext_constant_min_variation_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_SLOPE_RATIO_HOUSEHOLDS*",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_min_variation_eu_households_per_100_people",
)


@component.add(
    name="OBJECTIVE FERTILITY RATES SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_fertility_rates_sp"},
)
def objective_fertility_rates_sp():
    """
    Selection of the qualitative scenario (minimum, average, maximum) for the fertility rates
    """
    return _ext_constant_objective_fertility_rates_sp()


_ext_constant_objective_fertility_rates_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "OBJECTIVE_FERTILITY_RATES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_objective_fertility_rates_sp",
)


@component.add(
    name="OBJECTIVE LIFE EXPECTANCY AT BIRTH SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_life_expectancy_at_birth_sp"},
)
def objective_life_expectancy_at_birth_sp():
    """
    Selection of the qualitative scenario (high, medium, low) for the life expectancy at birth
    """
    return _ext_constant_objective_life_expectancy_at_birth_sp()


_ext_constant_objective_life_expectancy_at_birth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "OBJECTIVE_LEAB_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_objective_life_expectancy_at_birth_sp",
)


@component.add(
    name="PERCENTAGE EMIGRATIONS SP",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_percentage_emigrations_sp"},
)
def percentage_emigrations_sp():
    return _ext_constant_percentage_emigrations_sp()


_ext_constant_percentage_emigrations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "PERCENTAGE_EMIGRATIONS_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_percentage_emigrations_sp",
)


@component.add(
    name="POPULATION 2004",
    units="people",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2004"},
)
def population_2004():
    """
    Snapshot of the population in the year before the simulation (2004) to do the delays of the population.
    """
    return _ext_constant_population_2004()


_ext_constant_population_2004 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_FEMALE_2004",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    "_ext_constant_population_2004",
)

_ext_constant_population_2004.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_MALE_2004",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["MALE"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
)


@component.add(
    name="POPULATION 2005",
    units="people",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2005"},
)
def population_2005():
    """
    Snapshot of the population in the first year of simulation (2005) to initialize the stock of population.
    """
    return _ext_constant_population_2005()


_ext_constant_population_2005 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_FEMALE_2005",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
    "_ext_constant_population_2005",
)

_ext_constant_population_2005.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_MALE_2005",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["MALE"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
)


@component.add(
    name="SCENARIO FERTILITY RATE AVERAGE SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_average_sp"},
)
def scenario_fertility_rate_average_sp():
    """
    Selection of the values for the medium fertility rates (historical average)
    """
    return _ext_constant_scenario_fertility_rate_average_sp()


_ext_constant_scenario_fertility_rate_average_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_AVERAGE",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rate_average_sp",
)


@component.add(
    name="SCENARIO FERTILITY RATE MAXIMUM SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_maximum_sp"},
)
def scenario_fertility_rate_maximum_sp():
    """
    Selection of the values for the high fertility rates (historical maximum)
    """
    return _ext_constant_scenario_fertility_rate_maximum_sp()


_ext_constant_scenario_fertility_rate_maximum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_MAXIMUM",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rate_maximum_sp",
)


@component.add(
    name="SCENARIO FERTILITY RATE MINIMUM SP",
    units="people/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SEX I", "FERTILITY AGES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_scenario_fertility_rate_minimum_sp"},
)
def scenario_fertility_rate_minimum_sp():
    """
    Selection of the values for the low fertility rates (historical minimum)
    """
    return _ext_constant_scenario_fertility_rate_minimum_sp()


_ext_constant_scenario_fertility_rate_minimum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SCEN_FERTILITY_MINIMUM",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["FEMALE"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": _subscript_dict["SEX I"],
        "FERTILITY AGES I": _subscript_dict["FERTILITY AGES I"],
    },
    "_ext_constant_scenario_fertility_rate_minimum_sp",
)


@component.add(
    name="SELECT SLOPE EVOLUTION OF EU27 HOUSEHOLDS COMPOSITION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_slope_evolution_of_eu27_households_composition_sp"
    },
)
def select_slope_evolution_of_eu27_households_composition_sp():
    """
    Value for the switch scenario for households composition for EU27 countries. 4 options for the evolution of the ratio of households per 100 people over time available from the statistical analysis of past data: 0: Constant 2015 values 1: Mean values for future trend 2: Minimum values for future trend 3: Maximum values for future trend
    """
    return _ext_constant_select_slope_evolution_of_eu27_households_composition_sp()


_ext_constant_select_slope_evolution_of_eu27_households_composition_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "SLOPE_EU_HOUSEHOLDS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_slope_evolution_of_eu27_households_composition_sp",
)


@component.add(
    name="SHARES EMIGRATION SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "REGIONS 35 MAP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_shares_emigration_sp"},
)
def shares_emigration_sp():
    """
    Shares to distribute each regional emigration into the rest of regions
    """
    return _ext_constant_shares_emigration_sp()


_ext_constant_shares_emigration_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography_data",
    "SHARES_MIGRATION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
    },
    "_ext_constant_shares_emigration_sp",
)


@component.add(
    name="START YEAR MIGRATIONS SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_migrations_sp"},
)
def start_year_migrations_sp():
    return _ext_constant_start_year_migrations_sp()


_ext_constant_start_year_migrations_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "START_YEAR_MIGRATIONS_SP",
    {},
    _root,
    {},
    "_ext_constant_start_year_migrations_sp",
)


@component.add(
    name="TARGET YEAR FERTILITY RATES SP",
    units="Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_year_fertility_rates_sp"},
)
def target_year_fertility_rates_sp():
    """
    Final year of policy/scenario of fertility rates
    """
    return _ext_constant_target_year_fertility_rates_sp()


_ext_constant_target_year_fertility_rates_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "YEAR_FINAL_FERTILITY_RATES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_target_year_fertility_rates_sp",
)


@component.add(
    name="TARGET YEAR LIFE EXPECTANCY AT BIRTH SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_year_life_expectancy_at_birth_sp"
    },
)
def target_year_life_expectancy_at_birth_sp():
    """
    Final year of policy/scenario of life expectancy at birth
    """
    return _ext_constant_target_year_life_expectancy_at_birth_sp()


_ext_constant_target_year_life_expectancy_at_birth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "LEAB_YEAR_FINAL_LEAB_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_target_year_life_expectancy_at_birth_sp",
)
