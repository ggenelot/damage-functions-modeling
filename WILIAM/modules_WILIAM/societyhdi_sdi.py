"""
Module societyhdi_sdi
Translated using PySD version 3.14.0
"""

@component.add(
    name="AO SDI",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_material_footprint": 2,
        "pb_material_footprint": 2,
        "pb_co2": 2,
        "sdi_co2_emissions": 2,
    },
)
def ao_sdi():
    """
    AO parameter of the sustainable development index
    """
    return np.sqrt(
        if_then_else(
            world_material_footprint() / pb_material_footprint() < 1,
            lambda: 1,
            lambda: world_material_footprint() / pb_material_footprint(),
        )
        * if_then_else(
            sdi_co2_emissions() / pb_co2() < 1,
            lambda: 1,
            lambda: sdi_co2_emissions() / pb_co2(),
        )
    )


@component.add(
    name="ecological impact index",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ao_sdi": 3},
)
def ecological_impact_index():
    """
    Ecological impact index used to calculate the sustainable development index https://www.sustainabledevelopmentindex.org/methods
    """
    return if_then_else(
        ao_sdi() > 4,
        lambda: ao_sdi() - 2,
        lambda: 1 + (np.exp(ao_sdi()) - np.exp(1)) / (np.exp(4) - np.exp(1)),
    )


@component.add(
    name="gdp per capital real purchasing parity power",
    units="dollars 2017PPP/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "population_35_regions": 1,
        "conversion_to_purchasing_parity_power_mp": 1,
        "matrix_unit_prefixes": 1,
    },
)
def gdp_per_capital_real_purchasing_parity_power():
    """
    The transformation has been done maintaining the ratio between real gdp (2015) and real gdp ppp (2017) of 2015.
    """
    return (
        zidz(gross_domestic_product_real_supply_side(), population_35_regions())
        * conversion_to_purchasing_parity_power_mp()
        * float(matrix_unit_prefixes().loc["mega", "BASE UNIT"])
    )


@component.add(
    name="HDI",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "knowledge_index": 1,
        "long_and_healthy_life_index": 1,
        "standard_of_living_index": 1,
    },
)
def hdi():
    """
    Human Development Index. Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return (
        knowledge_index() * long_and_healthy_life_index() * standard_of_living_index()
    ) ** (1 / 3)


@component.add(
    name="HDI 9R",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi": 1, "hdi_eu_27": 1},
)
def hdi_9r():
    """
    HDI_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        hdi()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"]] = hdi_eu_27()
    return value


@component.add(
    name="HDI EU 27",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi": 1, "population_35_regions": 2},
)
def hdi_eu_27():
    return zidz(
        sum(
            hdi()
            .loc[_subscript_dict["REGIONS EU27 I"]]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"})
            * population_35_regions()
            .loc[_subscript_dict["REGIONS EU27 I"]]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
        sum(
            population_35_regions()
            .loc[_subscript_dict["REGIONS EU27 I"]]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
    )


@component.add(
    name="HDI world",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi_9r": 1, "population_9_regions": 2},
)
def hdi_world():
    """
    Human development index (HDI) of the world
    """
    return zidz(
        sum(
            hdi_9r().rename({"REGIONS 9 I": "REGIONS 9 I!"})
            * population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
        sum(
            population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )


@component.add(
    name="knowledge index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"means_years_of_schooling": 1, "schooling_life_expectancy": 1},
)
def knowledge_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(means_years_of_schooling() / 15 + schooling_life_expectancy() / 18, 2)


@component.add(
    name="long and healthy life index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"life_expectancy_at_birth": 2},
)
def long_and_healthy_life_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(
        (
            life_expectancy_at_birth().loc[:, "FEMALE"].reset_coords(drop=True)
            + life_expectancy_at_birth().loc[:, "MALE"].reset_coords(drop=True)
        )
        / 2
        - 20,
        85 - 20,
    )


@component.add(
    name="means years of schooling",
    units="Years",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "percentage_of_workforce_in_each_educational_level": 3,
        "years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp": 3,
    },
)
def means_years_of_schooling():
    """
    The years for calculating mean years of schooling are different from the years for calculating schooling life expectancy because in general the levels for reaching certain levels of schooling were lower in the past than they are today. It should be noted that the mean years of schooling takes data from the working age population (there is a population that studied decades ago), while schooling life expectancy takes current enrollments, which in the model is approximated by the percentages of the population that becomes part of the working age population.
    """
    return (
        sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "LOW EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "LOW EDUCATION"
            ]
        )
        + sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "MEDIUM EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "MEDIUM EDUCATION"
            ]
        )
        + sum(
            percentage_of_workforce_in_each_educational_level()
            .loc[:, "HIGH EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_means_years_of_schooling_mp().loc[
                "HIGH EDUCATION"
            ]
        )
    ) / 200


@component.add(
    name="PB CO2", units="t/(Year*person)", comp_type="Constant", comp_subtype="Normal"
)
def pb_co2():
    """
    Reference: 2015. Jason Hickel, The sustainable development index: Measuring the ecological efficiency of human development in the anthropocene, Ecological Economics, Volume 167, 2020, 106331, ISSN 0921-8009, https://doi.org/10.1016/j.ecolecon.2019.05.011.
    """
    return 7.91


@component.add(
    name="PB MATERIAL FOOTPRINT",
    units="t/(Year*person)",
    comp_type="Constant",
    comp_subtype="Normal",
)
def pb_material_footprint():
    """
    Reference: 2015. Jason Hickel, The sustainable development index: Measuring the ecological efficiency of human development in the anthropocene, Ecological Economics, Volume 167, 2020, 106331, ISSN 0921-8009, https://doi.org/10.1016/j.ecolecon.2019.05.011.
    """
    return 5.09


@component.add(
    name="schooling life expectancy",
    units="Years",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "percentage_of_new_workforce_in_each_educational_level": 3,
        "years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp": 3,
    },
)
def schooling_life_expectancy():
    """
    The years for calculating mean years of schooling are different from the years for calculating schooling life expectancy because in general the levels for reaching certain levels of schooling were lower in the past than they are today. It should be noted that the mean years of schooling takes data from the working age population (there is a population that studied decades ago), while schooling life expectancy takes current enrollments, which in the model is approximated by the percentages of the population that becomes part of the working age population.
    """
    return (
        sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "LOW EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "LOW EDUCATION"
            ]
        )
        + sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "MEDIUM EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "MEDIUM EDUCATION"
            ]
        )
        + sum(
            percentage_of_new_workforce_in_each_educational_level()
            .loc[:, "HIGH EDUCATION", :]
            .reset_coords(drop=True)
            .rename({"SEX I": "SEX I!"}),
            dim=["SEX I!"],
        )
        * float(
            years_of_education_corresponding_to_each_level_for_schooling_life_expectancy_mp().loc[
                "HIGH EDUCATION"
            ]
        )
    ) / 200


@component.add(
    name="SDI",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hdi_world": 1, "ecological_impact_index": 1},
)
def sdi():
    """
    Sustainable development index (SDI). Source: https://www.sustainabledevelopmentindex.org/
    """
    return hdi_world() / ecological_impact_index()


@component.add(
    name="SDI CO2 emissions",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_co2_energy_emissions_9r": 1,
        "world_population": 1,
        "unit_conversion_t_gt": 1,
    },
)
def sdi_co2_emissions():
    """
    Proxy of CO2 emissions to calculate the sustainable development index (SDI)
    """
    return (
        sum(
            total_co2_energy_emissions_9r().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        / world_population()
        * unit_conversion_t_gt()
    )


@component.add(
    name="standard of living index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_per_capital_real_purchasing_parity_power": 2},
)
def standard_of_living_index():
    """
    Formula proposed by UNDP and revisable in technical-notes-calculating-human-development-indices.pdf (undp.org)
    """
    return zidz(
        np.log(gdp_per_capital_real_purchasing_parity_power()) - np.log(100),
        np.maximum(
            np.log(
                vmax(
                    gdp_per_capital_real_purchasing_parity_power().rename(
                        {"REGIONS 35 I": "REGIONS 35 I!"}
                    ),
                    dim=["REGIONS 35 I!"],
                )
            ),
            np.log(75000),
        )
        - np.log(100),
    )


@component.add(
    name="world material footprint",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "al_market_sales": 1,
        "cu_market_sales": 1,
        "fe_market_sales": 1,
        "ni_market_sales": 1,
        "world_pe_by_commodity": 6,
        "unit_conversion_mj_ej": 6,
        "unit_conversion_kg_mt": 6,
        "pe_energy_density_mj_kg": 6,
        "world_population": 1,
        "unit_conversion_t_mt": 1,
    },
)
def world_material_footprint():
    """
    Proxy of the global material footprint
    """
    return (
        (
            al_market_sales()
            + cu_market_sales()
            + fe_market_sales()
            + ni_market_sales()
            + float(world_pe_by_commodity().loc["PE agriculture products"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE agriculture products"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE coal"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE coal"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE oil"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE oil"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE natural gas"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE natural gas"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE forestry products"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE forestry products"])
            / unit_conversion_kg_mt()
            + float(world_pe_by_commodity().loc["PE waste"])
            * unit_conversion_mj_ej()
            / float(pe_energy_density_mj_kg().loc["PE waste"])
            / unit_conversion_kg_mt()
        )
        / world_population()
        * unit_conversion_t_mt()
    )
