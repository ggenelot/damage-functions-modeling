"""
Module demographyhouseholds_composition
Translated using PySD version 3.14.0
"""

@component.add(
    name="adjustment factor households",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 1, "total_eu_population_in_households": 1},
)
def adjustment_factor_households():
    return zidz(
        population_35_regions()
        .loc[_subscript_dict["REGIONS EU27 I"]]
        .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
        total_eu_population_in_households(),
    )


@component.add(
    name="average people per household nonEU regions",
    units="person/household",
    subscripts=["REGIONS 8 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_average_people_per_household_noneu_regions": 1},
    other_deps={
        "_integ_average_people_per_household_noneu_regions": {
            "initial": {"initial_2015_average_people_per_household_noneu_regions": 1},
            "step": {"variation_average_people_per_household_noneu_regions": 1},
        }
    },
)
def average_people_per_household_noneu_regions():
    """
    Average people per household for non EU regions.
    """
    return _integ_average_people_per_household_noneu_regions()


_integ_average_people_per_household_noneu_regions = Integ(
    lambda: variation_average_people_per_household_noneu_regions(),
    lambda: initial_2015_average_people_per_household_noneu_regions(),
    "_integ_average_people_per_household_noneu_regions",
)


@component.add(
    name="average variation EU households per 100 people",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mean_variation_eu_households_per_100_people": 1,
        "buffering_parameter_for_eu_household_per_100_people_variation": 1,
    },
)
def average_variation_eu_households_per_100_people():
    """
    Average variation of European households per 100 inhabitants
    """
    return (
        mean_variation_eu_households_per_100_people()
        * buffering_parameter_for_eu_household_per_100_people_variation()
    )


@component.add(
    name="BUFFER EU HOUSEHOLDS SPEED OF CHANGE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_buffer_eu_households_speed_of_change_sp"
    },
)
def buffer_eu_households_speed_of_change_sp():
    """
    Parameter to modify the speed of the scenario assumption of the evolution of households composition in the EU.
    """
    return _ext_constant_buffer_eu_households_speed_of_change_sp()


_ext_constant_buffer_eu_households_speed_of_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "BUFFER_EU_HOUSEHOLDS_SPEED_OF_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_buffer_eu_households_speed_of_change_sp",
)


@component.add(
    name="buffering parameter for EU household per 100 people variation",
    units="DMNL",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buffer_eu_households_speed_of_change_sp": 1,
        "historical_min_eu_households_per_100_people": 2,
        "eu_households_per_100_people": 2,
        "historical_max_eu_households_per_100_people": 2,
    },
)
def buffering_parameter_for_eu_household_per_100_people_variation():
    """
    Parameter to buffer the changes in the households composition of Europe
    """
    return (
        buffer_eu_households_speed_of_change_sp()
        * np.maximum(
            np.minimum(
                historical_max_eu_households_per_100_people()
                - eu_households_per_100_people().transpose(
                    "HOUSEHOLDS DEMOGRAPHY I", "REGIONS EU27 I"
                ),
                (
                    eu_households_per_100_people()
                    - historical_min_eu_households_per_100_people()
                ).transpose("HOUSEHOLDS DEMOGRAPHY I", "REGIONS EU27 I"),
            ),
            0,
        )
        / (
            historical_max_eu_households_per_100_people()
            - historical_min_eu_households_per_100_people()
        )
    ).transpose("REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I")


@component.add(
    name="check people per hh EU",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_population_in_households": 1, "population_35_regions": 1},
)
def check_people_per_hh_eu():
    return sum(
        eu_population_in_households().rename(
            {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
        ),
        dim=["HOUSEHOLDS DEMOGRAPHY I!"],
    ) - population_35_regions().loc[_subscript_dict["REGIONS EU27 I"]].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    )


@component.add(
    name="check people per hh EU 2",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_population_in_households_2": 1, "population_35_regions": 1},
)
def check_people_per_hh_eu_2():
    return sum(
        eu_population_in_households_2().rename(
            {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
        ),
        dim=["HOUSEHOLDS DEMOGRAPHY I!"],
    ) - population_35_regions().loc[_subscript_dict["REGIONS EU27 I"]].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    )


@component.add(
    name="compensation between population and households",
    units="households/person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "demographic_ratio_compensation": 1,
        "eu_households_per_100_people": 2,
        "speed_for_demographic_fitting": 1,
        "surplus_persons_by_household": 1,
    },
)
def compensation_between_population_and_households():
    """
    Increase households to avoid negative values. There is a minimum number of households per type assured.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
                "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
            },
            ["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
        ),
        lambda: eu_households_per_100_people()
        * demographic_ratio_compensation()
        * speed_for_demographic_fitting()
        + surplus_persons_by_household() * eu_households_per_100_people(),
    )


@component.add(
    name="demographic ratio compensation",
    units="1",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"relative_variation_of_population_by_household": 2},
)
def demographic_ratio_compensation():
    """
    Ratio calculated to compensate imbalances between population across households
    """
    return (relative_variation_of_population_by_household() - 1) / (
        relative_variation_of_population_by_household() + 1
    )


@component.add(
    name="EU HOUSEHOLDS BY TYPE 2015",
    units="households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eu_households_by_type_2015"},
)
def eu_households_by_type_2015():
    """
    Number of people by household type in 2015. Exceptions (lack of data): Germany (data from 2014), Netherlands (same data than Belgium), Slovenia (same data than Croatia). Source: microdata of Eurostats.
    """
    return _ext_constant_eu_households_by_type_2015()


_ext_constant_eu_households_by_type_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "EU_HOUSEHOLDS_BY_TYPE_2015",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_eu_households_by_type_2015",
)


@component.add(
    name="EU households per 100 people",
    units="households/person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eu_households_per_100_people": 1},
    other_deps={
        "_integ_eu_households_per_100_people": {
            "initial": {"initial_ratio_eu_households_per_100_people": 1},
            "step": {
                "variation_eu_households_per_100_people": 1,
                "compensation_between_population_and_households": 1,
            },
        }
    },
)
def eu_households_per_100_people():
    """
    Dynamic ratio of European households per capita. Households per 100 people
    """
    return _integ_eu_households_per_100_people()


_integ_eu_households_per_100_people = Integ(
    lambda: variation_eu_households_per_100_people()
    + compensation_between_population_and_households(),
    lambda: initial_ratio_eu_households_per_100_people(),
    "_integ_eu_households_per_100_people",
)


@component.add(
    name="EU persons by household",
    units="person/households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eu_undefined_population_by_household": 1,
        "minimum_persons_by_household": 1,
    },
)
def eu_persons_by_household():
    """
    Persons by household in Europe
    """
    return eu_undefined_population_by_household() + minimum_persons_by_household()


@component.add(
    name="EU PERSONS BY HOUSEHOLD 2015",
    units="person/households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_eu_persons_by_household_2015"},
)
def eu_persons_by_household_2015():
    """
    Number of people by household type in 2015. Exceptions (lack of data): Germany (data from 2014), weighted values based on population size for Netherlands (similar than Belgium) and Croatia (similar than Croatia). Source: microdata of Eurostats.
    """
    return _ext_constant_eu_persons_by_household_2015()


_ext_constant_eu_persons_by_household_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "EU_PERSONS_BY_HOUSEHOLD_2015",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_eu_persons_by_household_2015",
)


@component.add(
    name="EU population in households",
    units="person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_households_by_type_eu27": 1, "eu_persons_by_household": 1},
)
def eu_population_in_households():
    """
    Population by household type in Europe
    """
    return number_households_by_type_eu27() * eu_persons_by_household()


@component.add(
    name="EU population in households 2",
    units="person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_households_by_type_eu27_adjusted": 1,
        "eu_persons_by_household": 1,
    },
)
def eu_population_in_households_2():
    """
    Population by household type in Europe
    """
    return number_households_by_type_eu27_adjusted() * eu_persons_by_household()


@component.add(
    name="EU undefined population by household",
    units="person/households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eu_undefined_population_by_household_2015": 1,
        "eu_undefined_population_in_households_2015": 1,
        "eu_households_by_type_2015": 1,
        "number_households_by_type_eu27": 1,
        "eu_undefined_population_in_households": 1,
    },
)
def eu_undefined_population_by_household():
    """
    People to place into different households (people over the minimum population living in European households)
    """
    return (
        eu_undefined_population_by_household_2015()
        * (eu_households_by_type_2015() / eu_undefined_population_in_households_2015())
        * (eu_undefined_population_in_households() / number_households_by_type_eu27())
    )


@component.add(
    name="EU undefined population by household 2015",
    units="person/households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_persons_by_household_2015": 1, "minimum_persons_by_household": 1},
)
def eu_undefined_population_by_household_2015():
    return eu_persons_by_household_2015() - minimum_persons_by_household()


@component.add(
    name="EU undefined population in households",
    units="person",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 1, "minimum_eu_population_in_households": 1},
)
def eu_undefined_population_in_households():
    """
    Rest of people to be allocated into different households
    """
    return population_35_regions().loc[_subscript_dict["REGIONS EU27 I"]].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    ) - sum(
        minimum_eu_population_in_households().rename(
            {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
        ),
        dim=["HOUSEHOLDS DEMOGRAPHY I!"],
    )


@component.add(
    name="EU undefined population in households 2015",
    units="person",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "population_2015_by_region": 1,
        "minimum_eu_population_in_households_2015": 1,
    },
)
def eu_undefined_population_in_households_2015():
    return population_2015_by_region().loc[_subscript_dict["REGIONS EU27 I"]].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    ) - sum(
        minimum_eu_population_in_households_2015().rename(
            {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
        ),
        dim=["HOUSEHOLDS DEMOGRAPHY I!"],
    )


@component.add(
    name="HISTORICAL MAX EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/person",
    subscripts=["HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_max_eu_households_per_100_people"
    },
)
def historical_max_eu_households_per_100_people():
    """
    Maximum historical values for the ratio of households per 100 people
    """
    return _ext_constant_historical_max_eu_households_per_100_people()


_ext_constant_historical_max_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MAX_HISTORICAL_HOUSEHOLDS_RATIO*",
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    _root,
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    "_ext_constant_historical_max_eu_households_per_100_people",
)


@component.add(
    name="HISTORICAL MIN EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/person",
    subscripts=["HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_min_eu_households_per_100_people"
    },
)
def historical_min_eu_households_per_100_people():
    """
    Minimum historical values for the ratio of households per 100 people
    """
    return _ext_constant_historical_min_eu_households_per_100_people()


_ext_constant_historical_min_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_HISTORICAL_HOUSEHOLDS_RATIO*",
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    _root,
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    "_ext_constant_historical_min_eu_households_per_100_people",
)


@component.add(
    name="INITIAL 2015 AVERAGE PEOPLE PER HOUSEHOLD NONEU REGIONS",
    units="people/household",
    subscripts=["REGIONS 8 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_2015_regions_8": 1, "base_number_of_households": 1},
)
def initial_2015_average_people_per_household_noneu_regions():
    """
    Average people per household in the year 2015 for non EU regions.
    """
    return population_2015_regions_8() / sum(
        base_number_of_households()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="MAXIMUM PERSONS BY HOUSEHOLD",
    units="people/household",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_persons_by_household"},
)
def maximum_persons_by_household():
    """
    Maximum number of people per household type
    """
    return _ext_constant_maximum_persons_by_household()


_ext_constant_maximum_persons_by_household = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MAXIMUM_PERSONS_BY_HH",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_maximum_persons_by_household",
)


@component.add(
    name="minimum EU population in households",
    units="person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_households_by_type_eu27": 1, "minimum_persons_by_household": 1},
)
def minimum_eu_population_in_households():
    """
    Minimum number of people in European households
    """
    return number_households_by_type_eu27() * minimum_persons_by_household()


@component.add(
    name="minimum EU population in households 2015",
    units="person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_households_by_type_2015": 1, "minimum_persons_by_household": 1},
)
def minimum_eu_population_in_households_2015():
    """
    Minimum number of people in European households in 2015
    """
    return eu_households_by_type_2015() * minimum_persons_by_household()


@component.add(
    name="MINIMUM PERSONS BY HOUSEHOLD",
    units="person/households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_persons_by_household"},
)
def minimum_persons_by_household():
    """
    Number of people by household type in 2015. Exceptions (lack of data): Germany (data from 2014), Netherlands (same data than Belgium), Sweden (same data than Finland). Source: microdata of Eurostats.
    """
    return _ext_constant_minimum_persons_by_household()


_ext_constant_minimum_persons_by_household = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MINIMUM_PERSONS_BY_HH",
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    _root,
    {
        "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
        "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"],
    },
    "_ext_constant_minimum_persons_by_household",
)


@component.add(
    name="number households by type EU27",
    units="households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_households_per_100_people": 1, "population_35_regions": 1},
)
def number_households_by_type_eu27():
    """
    Extrapolation of the number of households based on the regional population. The value "100" is used to translate from ratios (originally in households per 100 people) into households.
    """
    return np.maximum(
        eu_households_per_100_people()
        * (
            population_35_regions()
            .loc[_subscript_dict["REGIONS EU27 I"]]
            .rename({"REGIONS 35 I": "REGIONS EU27 I"})
            / 100
        ),
        1,
    )


@component.add(
    name="number households by type EU27 adjusted",
    units="households",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_households_by_type_eu27": 1, "adjustment_factor_households": 1},
)
def number_households_by_type_eu27_adjusted():
    """
    Extrapolation of the number of households based on the regional population. The value "100" is used to translate from ratios (originally in households per 100 people) into households.
    """
    return number_households_by_type_eu27() * adjustment_factor_households()


@component.add(
    name="number households nonEU",
    units="households",
    subscripts=["REGIONS 8 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "population_35_regions": 1,
        "average_people_per_household_noneu_regions": 1,
    },
)
def number_households_noneu():
    return (
        population_35_regions()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        / average_people_per_household_noneu_regions()
    )


@component.add(
    name="POPULATION 2015",
    units="people",
    subscripts=["REGIONS 35 I", "SEX I", "AGE COHORTS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2015"},
)
def population_2015():
    """
    Historical data of population by country (2015, United Nations Database)
    """
    return _ext_constant_population_2015()


_ext_constant_population_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_FEMALE_2015",
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
    "_ext_constant_population_2015",
)

_ext_constant_population_2015.add(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POP_MALE_2015",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SEX I": ["MALE"],
        "AGE COHORTS I": _subscript_dict["AGE COHORTS I"],
    },
)


@component.add(
    name="population 2015 by region",
    units="person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_2015": 1},
)
def population_2015_by_region():
    """
    Population by region
    """
    return sum(
        population_2015().rename(
            {"SEX I": "SEX I!", "AGE COHORTS I": "AGE COHORTS I!"}
        ),
        dim=["SEX I!", "AGE COHORTS I!"],
    )


@component.add(
    name="POPULATION 2015 REGIONS 8",
    units="people",
    subscripts=["REGIONS 8 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_population_2015_regions_8"},
)
def population_2015_regions_8():
    """
    Population in the year 2015 for the non EU regions.
    """
    return _ext_constant_population_2015_regions_8()


_ext_constant_population_2015_regions_8 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "POPULATION_2015_REGIONS_8*",
    {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]},
    _root,
    {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]},
    "_ext_constant_population_2015_regions_8",
)


@component.add(
    name="ratio urbanization EU27",
    units="1",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"urban_population_eu27": 1, "rural_population_eu27": 1},
)
def ratio_urbanization_eu27():
    """
    1 means equal population distributed between rural and urban areas. Greater than 1 means more population present in urban areas while less than one means more population present in rural areas
    """
    return urban_population_eu27() / rural_population_eu27()


@component.add(
    name="relative variation of population by household",
    units="1",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eu_undefined_population_by_household": 1,
        "eu_undefined_population_by_household_2015": 1,
    },
)
def relative_variation_of_population_by_household():
    """
    VRP = relative variation of the population by household type
    """
    return np.maximum(
        xidz(
            eu_undefined_population_by_household(),
            eu_undefined_population_by_household_2015(),
            1,
        ),
        0.001,
    )


@component.add(
    name="rural population EU27",
    units="person",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_persons_by_household": 6, "number_households_by_type_eu27": 6},
)
def rural_population_eu27():
    """
    Population in rural areas by European country
    """
    return (
        eu_persons_by_household().loc[:, "SPARSE SINGLE"].reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE SINGLE"]
        .reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "SPARSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        + eu_persons_by_household().loc[:, "SPARSE COUPLE"].reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE COUPLE"]
        .reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "SPARSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        + eu_persons_by_household().loc[:, "SPARSE OTHER"].reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE OTHER"]
        .reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "SPARSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "SPARSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
    )


@component.add(
    name="ruralization EU households per 100 people",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_variation_eu_households_per_100_people": 1,
        "final_time": 4,
        "time": 2,
        "mean_variation_eu_households_per_100_people": 1,
        "buffering_parameter_for_eu_household_per_100_people_variation": 1,
    },
)
def ruralization_eu_households_per_100_people():
    """
    Annual variation of ruralization in households composition of Europe
    """
    return (
        max_variation_eu_households_per_100_people()
        * ramp(__data["time"], 1 / (final_time() - 2015), 2015, final_time())
        - mean_variation_eu_households_per_100_people()
        * (1 - ramp(__data["time"], 1 / (final_time() - 2015), 2015, final_time()))
    ) * buffering_parameter_for_eu_household_per_100_people_variation()


@component.add(
    name="SELECT VARIATION OF AVERAGE PEOPLE PER HOUSEHOLD IN NON EU REGIONS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp"
    },
)
def select_variation_of_average_people_per_household_in_non_eu_regions_sp():
    """
    Select scenario parameter for seting the average people per household in the non EU regions.
    """
    return (
        _ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp()
    )


_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "demography",
    "SELECT_VARIATION_OF_AVERAGE_PEOPLE_PER_HOUSEHOLD_IN_NON_EU_REGIONS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_variation_of_average_people_per_household_in_non_eu_regions_sp",
)


@component.add(
    name="SPEED FOR DEMOGRAPHIC FITTING",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_speed_for_demographic_fitting"},
)
def speed_for_demographic_fitting():
    """
    Speed to adjust the compensation of unbalancing effects between the number of households and population. Range of the value: 0.01-1.
    """
    return _ext_constant_speed_for_demographic_fitting()


_ext_constant_speed_for_demographic_fitting = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "SPEED_FOR_DEMOGRAPHIC_FITTING",
    {},
    _root,
    {},
    "_ext_constant_speed_for_demographic_fitting",
)


@component.add(
    name="surplus persons by household",
    units="households/person",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eu_persons_by_household": 1,
        "maximum_persons_by_household": 1,
        "surplus_persons_by_household_base": 1,
    },
)
def surplus_persons_by_household():
    """
    People exceeding the maximum number of people per household. This variable should be always 0 in 2015
    """
    return (
        np.maximum(eu_persons_by_household() - maximum_persons_by_household(), 0)
        / surplus_persons_by_household_base()
    )


@component.add(
    name="SURPLUS PERSONS BY HOUSEHOLD BASE",
    units="households/person",
    comp_type="Constant",
    comp_subtype="Normal",
)
def surplus_persons_by_household_base():
    """
    Constant to change the units. In order to obtain a dmnl ratio, the original variable is divided by the reference value to invert the units
    """
    return 1


@component.add(
    name="total EU population in households",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_population_in_households": 1},
)
def total_eu_population_in_households():
    return sum(
        eu_population_in_households().rename(
            {"HOUSEHOLDS DEMOGRAPHY I": "HOUSEHOLDS DEMOGRAPHY I!"}
        ),
        dim=["HOUSEHOLDS DEMOGRAPHY I!"],
    )


@component.add(
    name="urban population EU27",
    units="person",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eu_persons_by_household": 6, "number_households_by_type_eu27": 6},
)
def urban_population_eu27():
    """
    Population in urban areas by European country
    """
    return (
        eu_persons_by_household().loc[:, "DENSE SINGLE"].reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "DENSE SINGLE"]
        .reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        + eu_persons_by_household().loc[:, "DENSE COUPLE"].reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "DENSE COUPLE"]
        .reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        + eu_persons_by_household().loc[:, "DENSE OTHER"].reset_coords(drop=True)
        * number_households_by_type_eu27().loc[:, "DENSE OTHER"].reset_coords(drop=True)
        + eu_persons_by_household()
        .loc[:, "DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        * number_households_by_type_eu27()
        .loc[:, "DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
    )


@component.add(
    name="urbanization EU households per 100 people",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "min_variation_eu_households_per_100_people": 1,
        "final_time": 4,
        "time": 2,
        "mean_variation_eu_households_per_100_people": 1,
        "buffering_parameter_for_eu_household_per_100_people_variation": 1,
    },
)
def urbanization_eu_households_per_100_people():
    """
    Annual variation of urbanization in households composition of Europe
    """
    return (
        min_variation_eu_households_per_100_people()
        * ramp(__data["time"], 1 / (final_time() - 2015), 2015, final_time())
        - mean_variation_eu_households_per_100_people()
        * (1 - ramp(__data["time"], 1 / (final_time() - 2015), 2015, final_time()))
    ) * buffering_parameter_for_eu_household_per_100_people_variation()


@component.add(
    name="variation average people per household nonEU regions",
    units="people/(household*Year)",
    subscripts=["REGIONS 8 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "select_variation_of_average_people_per_household_in_non_eu_regions_sp": 2,
        "average_people_per_household_non_eu_regions_timeseries_target_sp": 2,
    },
)
def variation_average_people_per_household_noneu_regions():
    """
    Variation over time of average number of people per household for non EU regions.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, ["REGIONS 8 I"]
        ),
        lambda: if_then_else(
            select_variation_of_average_people_per_household_in_non_eu_regions_sp()
            == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, ["REGIONS 8 I"]
            ),
            lambda: if_then_else(
                select_variation_of_average_people_per_household_in_non_eu_regions_sp()
                == 1,
                lambda: average_people_per_household_non_eu_regions_timeseries_target_sp(
                    time() + 1
                )
                - average_people_per_household_non_eu_regions_timeseries_target_sp(
                    time()
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, ["REGIONS 8 I"]
                ),
            ),
        ),
    )


@component.add(
    name="variation EU households per 100 people",
    units="households/(person*Year)",
    subscripts=["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "mean_variation_eu_households_per_100_people": 1,
        "average_variation_eu_households_per_100_people": 1,
        "select_slope_evolution_of_eu27_households_composition_sp": 3,
        "urbanization_eu_households_per_100_people": 1,
        "ruralization_eu_households_per_100_people": 1,
        "eu_households_per_100_people": 1,
    },
)
def variation_eu_households_per_100_people():
    """
    Slope in the ratio of households composition. Units: households per 100 people
    """
    return if_then_else(
        time() <= 2015,
        lambda: mean_variation_eu_households_per_100_people(),
        lambda: np.maximum(
            if_then_else(
                select_slope_evolution_of_eu27_households_composition_sp() == 1,
                lambda: average_variation_eu_households_per_100_people(),
                lambda: if_then_else(
                    select_slope_evolution_of_eu27_households_composition_sp() == 2,
                    lambda: urbanization_eu_households_per_100_people(),
                    lambda: if_then_else(
                        select_slope_evolution_of_eu27_households_composition_sp() == 3,
                        lambda: ruralization_eu_households_per_100_people(),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
                                "HOUSEHOLDS DEMOGRAPHY I": _subscript_dict[
                                    "HOUSEHOLDS DEMOGRAPHY I"
                                ],
                            },
                            ["REGIONS EU27 I", "HOUSEHOLDS DEMOGRAPHY I"],
                        ),
                    ),
                ),
            ),
            -eu_households_per_100_people(),
        ),
    )
