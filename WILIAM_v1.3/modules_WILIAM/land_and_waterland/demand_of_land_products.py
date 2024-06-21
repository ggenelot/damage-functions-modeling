"""
Module land_and_waterland.demand_of_land_products
Translated using PySD version 3.14.0
"""

@component.add(
    name="ADJUSTMENT PE BY COMMODITY AGRICULTURAL",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_adjustment_pe_by_commodity_agricultural"
    },
)
def adjustment_pe_by_commodity_agricultural():
    """
    auxiliar jan 24 biofuels
    """
    return _ext_constant_adjustment_pe_by_commodity_agricultural()


_ext_constant_adjustment_pe_by_commodity_agricultural = ExtConstant(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "exogenous_inputs",
    "ADJUSTMENT_PE_BY_COMMODITY_AGRICULTURAL*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_adjustment_pe_by_commodity_agricultural",
)


@component.add(
    name="crops demanded for energy",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_for_energy_converted_to_tonnes": 1,
        "land_products_used_for_energy_percentages": 1,
    },
)
def crops_demanded_for_energy():
    """
    all the land products demanded and used for energy
    """
    return (
        crops_demanded_for_energy_converted_to_tonnes()
        * land_products_used_for_energy_percentages()
    )


@component.add(
    name="crops demanded for energy converted to tonnes",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_demanded_from_agriculture_products": 1,
        "energy_to_land_products_conversion_factor": 1,
    },
)
def crops_demanded_for_energy_converted_to_tonnes():
    """
    agriculture products demanded for energy with tonnes unit
    """
    return (
        energy_demanded_from_agriculture_products()
        / energy_to_land_products_conversion_factor()
    )


@component.add(
    name="crops demanded for energy world",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_demanded_for_energy": 1},
)
def crops_demanded_for_energy_world():
    """
    global quantity of land products used for energy
    """
    return sum(
        crops_demanded_for_energy().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="energy demanded from agriculture products",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "exo_pe_by_commodity_agriculture_products": 2,
        "switch_landwater": 1,
        "adjustment_pe_by_commodity_agricultural": 1,
        "pe_by_commodity_dem": 1,
    },
)
def energy_demanded_from_agriculture_products():
    """
    agriculture products demanded for energy in units of energy
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: exo_pe_by_commodity_agriculture_products(),
        lambda: if_then_else(
            switch_landwater() == 1,
            lambda: pe_by_commodity_dem()
            .loc[:, "PE agriculture products"]
            .reset_coords(drop=True)
            * adjustment_pe_by_commodity_agricultural(),
            lambda: exo_pe_by_commodity_agriculture_products(),
        ),
    )


@component.add(
    name="energy demanded from forestry products",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "pe_by_commodity": 1,
        "exo_pe_by_commodity_forestry_products": 1,
    },
)
def energy_demanded_from_forestry_products():
    """
    Energy demanded from forestry products
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: pe_by_commodity()
        .loc[:, "PE forestry products"]
        .reset_coords(drop=True),
        lambda: exo_pe_by_commodity_forestry_products(),
    )


@component.add(
    name="EXO PE by commodity agriculture products",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "imv_pe_by_commodity_agriculture_products": 1},
)
def exo_pe_by_commodity_agriculture_products():
    """
    PE by commidity agriculture products exogenous
    """
    return imv_pe_by_commodity_agriculture_products(time())


@component.add(
    name="EXO PE by commodity forestry products",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "imv_pe_by_commodity_forestry_products": 1},
)
def exo_pe_by_commodity_forestry_products():
    """
    exogenous valur of PE by commidity forestry products used when the Land and Water module is disconected from the rest of WILIAM
    """
    return imv_pe_by_commodity_forestry_products(time())


@component.add(
    name="exogenous output real 9R construction sector",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_construction_sector": 1},
)
def exogenous_output_real_9r_construction_sector():
    """
    Exogenous variable of output of construction sector. Only active if SWITCH_LANDWATER=0
    """
    return exo_output_real_for_construction_sector(time())


@component.add(
    name="exogenous output real 9R forrestry sector",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_forestry_sector": 1},
)
def exogenous_output_real_9r_forrestry_sector():
    """
    exogenous value of the economic output real for forestry sector to be used when the Land and Water module is disconected from the resto of WILIAM
    """
    return exo_output_real_for_forestry_sector(time())


@component.add(
    name="exogenous output real 9R manufacture wood sector",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_output_real_for_manufacture_wood_sector": 1},
)
def exogenous_output_real_9r_manufacture_wood_sector():
    """
    Exogenous variable of output of wood manufacturing sector. Only active if SWITCH_LANDWATER=0
    """
    return exo_output_real_for_manufacture_wood_sector(time())


@component.add(
    name="land products demanded",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_before_losses": 1,
        "loss_factor_of_land_products": 1,
    },
)
def land_products_demanded():
    """
    land_products_demanded
    """
    return land_products_demanded_before_losses() * loss_factor_of_land_products()


@component.add(
    name="land products demanded before losses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_for_energy": 11,
        "land_products_demanded_for_food_before_losses": 10,
        "percent_of_land_products_for_other_uses": 10,
        "roundwood_demanded_for_industry": 1,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
        "residues_of_forests_demanded_for_industry": 1,
    },
)
def land_products_demanded_before_losses():
    """
    land products demanded for food, energy, and industry by region and each type of land product
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    )
    value.loc[:, ["CORN"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "CORN"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "CORN"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "RICE"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "RICE"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "CEREALS OTHER"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "TUBERS"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "TUBERS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "SOY"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "SOY"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "PULSES NUTS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        (
            (
                crops_demanded_for_energy().loc[:, "OILCROPS"].reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "OILCROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "SUGAR CROPS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "SUGAR CROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "FRUITS VEGETABLES"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "FRUITS VEGETABLES"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = (
        crops_demanded_for_energy()
        .loc[:, "BIOFUEL 2GCROP"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"]] = (
        (
            (
                crops_demanded_for_energy()
                .loc[:, "OTHER CROPS"]
                .reset_coords(drop=True)
                + land_products_demanded_for_food_before_losses()
                .loc[:, "OTHER CROPS"]
                .reset_coords(drop=True)
            )
            * (1 + (1 - float(percent_of_land_products_for_other_uses().loc["CORN"])))
        )
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = (
        (
            roundwood_demanded_for_industry()
            + wood_demanded_for_energy_converted_to_tonnes()
        )
        .expand_dims({"LAND PRODUCTS I": ["WOOD"]}, 1)
        .values
    )
    value.loc[:, ["RESIDUES"]] = (
        residues_of_forests_demanded_for_industry()
        .expand_dims({"LAND PRODUCTS I": ["RESIDUES"]}, 1)
        .values
    )
    return value


@component.add(
    name="land products demanded world",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded": 1},
)
def land_products_demanded_world():
    """
    land products demanded for food and energy for all regions
    """
    return sum(
        land_products_demanded().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="land products demanded world before losses",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_before_losses": 1},
)
def land_products_demanded_world_before_losses():
    """
    Land products demanded -world, before losses, all uses
    """
    return sum(
        land_products_demanded_before_losses().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="output real 9R for forestry sector",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "output_real_9r": 1,
        "exogenous_output_real_9r_forrestry_sector": 1,
    },
)
def output_real_9r_for_forestry_sector():
    """
    Output real for forestry sector by region
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: output_real_9r().loc[:, "FORESTRY"].reset_coords(drop=True),
        lambda: exogenous_output_real_9r_forrestry_sector(),
    )


@component.add(
    name="output real of wood manufacturing and construction sectors",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_landwater": 1,
        "output_real_9r": 2,
        "exogenous_output_real_9r_construction_sector": 1,
        "exogenous_output_real_9r_manufacture_wood_sector": 1,
    },
)
def output_real_of_wood_manufacturing_and_construction_sectors():
    """
    Output real for construction and wood manufacturing, the main sectors that demand industrial wood
    """
    return if_then_else(
        switch_landwater() == 1,
        lambda: output_real_9r().loc[:, "MANUFACTURE WOOD"].reset_coords(drop=True)
        + output_real_9r().loc[:, "CONSTRUCTION"].reset_coords(drop=True),
        lambda: exogenous_output_real_9r_manufacture_wood_sector()
        + exogenous_output_real_9r_construction_sector(),
    )


@component.add(
    name="residues of forests demanded for industry",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_9r_for_forestry_sector": 1,
        "intensities_of_residues_for_industry": 1,
    },
)
def residues_of_forests_demanded_for_industry():
    """
    The global quantity of wood waste demanded for industry by region, not activated.
    """
    return output_real_9r_for_forestry_sector() * intensities_of_residues_for_industry()


@component.add(
    name="roundwood demanded for energy and industry",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_energy_converted_to_tonnes": 1,
        "wood_demanded_for_industry": 1,
    },
)
def roundwood_demanded_for_energy_and_industry():
    """
    wood demanded for energy and industry
    """
    return wood_demanded_for_energy_converted_to_tonnes() + wood_demanded_for_industry()


@component.add(
    name="roundwood demanded for industry",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "output_real_of_wood_manufacturing_and_construction_sectors": 1,
        "intensities_of_wood_for_industry": 1,
    },
)
def roundwood_demanded_for_industry():
    """
    The global quantity of wood demanded for industry by region
    """
    return (
        output_real_of_wood_manufacturing_and_construction_sectors()
        * intensities_of_wood_for_industry()
    )


@component.add(
    name="roundwood demanded world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_demanded_for_energy_and_industry": 1},
)
def roundwood_demanded_world():
    """
    global quantity of wood demanded for all regions
    """
    return sum(
        roundwood_demanded_for_energy_and_industry().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="wood demanded for energy converted to tonnes",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_demanded_from_forestry_products": 1,
        "energy_to_wood_conversion_factor": 1,
    },
)
def wood_demanded_for_energy_converted_to_tonnes():
    """
    forestry products demanded for energy with tonnes unit
    """
    return energy_demanded_from_forestry_products() / energy_to_wood_conversion_factor()


@component.add(
    name="wood demanded for energy world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wood_demanded_for_energy_converted_to_tonnes": 1},
)
def wood_demanded_for_energy_world():
    """
    wood demanded for energy for all regions
    """
    return sum(
        wood_demanded_for_energy_converted_to_tonnes().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="wood demanded for industry",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "residues_of_forests_demanded_for_industry": 1,
        "roundwood_demanded_for_industry": 1,
    },
)
def wood_demanded_for_industry():
    """
    global quantity of wood demand for industry
    """
    return (
        residues_of_forests_demanded_for_industry() + roundwood_demanded_for_industry()
    )


@component.add(
    name="wood demanded for industry world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wood_demanded_for_industry": 1},
)
def wood_demanded_for_industry_world():
    """
    wood demanded for industry for all regions
    """
    return sum(
        wood_demanded_for_industry().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
