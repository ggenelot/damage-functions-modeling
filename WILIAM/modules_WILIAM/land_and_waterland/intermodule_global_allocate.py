"""
Module land_and_waterland.intermodule_global_allocate
Translated using PySD version 3.14.0
"""

@component.add(
    name="availability of crops for energy",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_available_for_energy": 1, "crops_demanded_for_energy": 1},
)
def availability_of_crops_for_energy():
    """
    Signal to measure the abundance or shortage of crops for energy (biofuels) in each region. If demand can be met, availability of crops for energy =1, if it is 0.2, for example, 20% of the demand cannot be met. supply includes international trade
    """
    return zidz(
        sum(
            crops_available_for_energy().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        ),
        sum(
            crops_demanded_for_energy().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
            dim=["LAND PRODUCTS I!"],
        ),
    )


@component.add(
    name="availability of crops for food",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_available_for_food": 1, "land_products_demanded_for_food": 1},
)
def availability_of_crops_for_food():
    """
    Signal to measure the abundance or shortage of food in each region. If demand can be met, availability of crops for food=1, if it is 0.2, for example, 20% of the demand cannot be met.
    """
    return zidz(
        sum(
            crops_available_for_food().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
            dim=["LAND PRODUCTS I!"],
        ),
        sum(
            land_products_demanded_for_food().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        ),
    )


@component.add(
    name="availability of forestry products for energy",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
        "forestry_products_available_for_energy": 1,
    },
)
def availability_of_forestry_products_for_energy():
    """
    Signal to measure the abundance or shortage of wood for energy in each region. If demand can be met, availability of forestry products for energy =1, if it is 0.2, for example, 20% of the demand cannot be met. supply includes international trade
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: zidz(
            forestry_products_available_for_energy(),
            wood_demanded_for_energy_converted_to_tonnes(),
        ),
    )


@component.add(
    name="availability of forestry products for industry",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forestry_products_available_for_industry": 1,
        "wood_demanded_for_industry": 2,
    },
)
def availability_of_forestry_products_for_industry():
    """
    Signal to measure the abundance or shortage of wood for industry in each region. If demand can be met, availability of forestry products for industry =1, if it is 0.2, for example, 20% of the demand cannot be met. supply includes international trade
    """
    return zidz(
        forestry_products_available_for_industry() - wood_demanded_for_industry(),
        wood_demanded_for_industry(),
    )


@component.add(
    name="average availability of crops for energy world",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_crops_for_energy": 1},
)
def average_availability_of_crops_for_energy_world():
    """
    average availability of crops for energy, average of regions
    """
    return sum(
        availability_of_crops_for_energy().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    ) / len(
        xr.DataArray(
            np.arange(28, len(_subscript_dict["REGIONS 9 I"]) + 28),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        )
    )


@component.add(
    name="average availability of crops for food world",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_crops_for_food": 1},
)
def average_availability_of_crops_for_food_world():
    """
    average availability of crops feneor food, average of regions
    """
    return sum(
        availability_of_crops_for_food().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    ) / len(
        xr.DataArray(
            np.arange(28, len(_subscript_dict["REGIONS 9 I"]) + 28),
            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
            ["REGIONS 9 I"],
        )
    )


@component.add(
    name="change of the share of land products from smallholders",
    units="1/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_land_products_global_pool_sp": 1,
        "year_initial_land_products_global_pool_sp": 2,
        "time": 2,
        "year_final_land_products_global_pool_sp": 2,
        "initial_share_of_production_from_smallholders": 1,
        "objective_land_products_global_pool_sp": 1,
    },
)
def change_of_the_share_of_land_products_from_smallholders():
    """
    change of the share of land products protected from global pool "market"
    """
    return if_then_else(
        np.logical_and(
            switch_land_products_global_pool_sp() == 1,
            np.logical_and(
                time() > year_initial_land_products_global_pool_sp(),
                time() < year_final_land_products_global_pool_sp(),
            ),
        ),
        lambda: zidz(
            objective_land_products_global_pool_sp()
            - initial_share_of_production_from_smallholders(),
            year_final_land_products_global_pool_sp()
            - year_initial_land_products_global_pool_sp(),
        ),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="crops available for energy",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_available_for_energy():
    """
    crops allocated to energy
    """
    return (
        crops_distributed_to_uses()
        .loc[:, :, "LP ENERGY AGRICULTURAL"]
        .reset_coords(drop=True)
    )


@component.add(
    name="crops available for food",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_available_for_food():
    """
    Crops distributed to food per region
    """
    return crops_distributed_to_uses().loc[:, :, "LP FOOD"].reset_coords(drop=True)


@component.add(
    name="crops demanded to uses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "USES LP I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"land_products_demanded_for_food": 1, "crops_demanded_for_energy": 1},
)
def crops_demanded_to_uses():
    """
    Crops demanded for food (including feed) and energy (materials are considered constatn)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            "USES LP I": _subscript_dict["USES LP I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I", "USES LP I"],
    )
    value.loc[:, :, ["LP FOOD"]] = (
        land_products_demanded_for_food()
        .expand_dims({"USES LP I": ["LP FOOD"]}, 2)
        .values
    )
    value.loc[:, :, ["LP INDUSTRY"]] = 0
    value.loc[:, :, ["LP ENERGY FORESTRY"]] = 0
    value.loc[:, :, ["LP ENERGY AGRICULTURAL"]] = (
        crops_demanded_for_energy()
        .expand_dims({"USES LP I": ["LP ENERGY AGRICULTURAL"]}, 2)
        .values
    )
    return value


@component.add(
    name="crops distributed to uses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "USES LP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_demanded_to_uses": 1,
        "priorities_crops_among_uses": 1,
        "width_of_crops_distribution_among_uses_sp": 1,
        "land_products_available_to_each_region": 1,
    },
)
def crops_distributed_to_uses():
    """
    allocation of crops to uses in each region (energy, food)
    """
    return allocate_by_priority(
        crops_demanded_to_uses(),
        priorities_crops_among_uses(),
        width_of_crops_distribution_among_uses_sp().expand_dims(
            {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1
        ),
        land_products_available_to_each_region(),
    )


@component.add(
    name="crops distributed to uses world",
    units="t/Year",
    subscripts=["LAND PRODUCTS I", "USES LP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"crops_distributed_to_uses": 1},
)
def crops_distributed_to_uses_world():
    """
    crops distributed to uses, regions added
    """
    return sum(
        crops_distributed_to_uses().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="energy available from crops",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "crops_available_for_energy": 1,
        "energy_to_land_products_conversion_factor": 1,
    },
)
def energy_available_from_crops():
    """
    Energy available in each region for biofuels coming from crops
    """
    return (
        sum(
            crops_available_for_energy().rename(
                {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
            ),
            dim=["LAND PRODUCTS I!"],
        )
        * energy_to_land_products_conversion_factor()
    )


@component.add(
    name="energy available from crops world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_available_from_crops": 1},
)
def energy_available_from_crops_world():
    """
    Summ of all energy obtained from crops, world
    """
    return sum(
        energy_available_from_crops().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="energy available from forestry products",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forestry_products_available_for_energy": 1,
        "energy_to_wood_conversion_factor": 1,
    },
)
def energy_available_from_forestry_products():
    """
    Energy available from forestry products
    """
    return forestry_products_available_for_energy() * energy_to_wood_conversion_factor()


@component.add(
    name="forestry products available for energy",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forestry_products_distributed_to_uses": 1},
)
def forestry_products_available_for_energy():
    """
    forestry products allocated to energy
    """
    return (
        forestry_products_distributed_to_uses()
        .loc[:, "LP ENERGY FORESTRY"]
        .reset_coords(drop=True)
    )


@component.add(
    name="forestry products available for industry",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forestry_products_distributed_to_uses": 1},
)
def forestry_products_available_for_industry():
    """
    forestry products allocated to industry
    """
    return (
        forestry_products_distributed_to_uses()
        .loc[:, "LP INDUSTRY"]
        .reset_coords(drop=True)
    )


@component.add(
    name="forestry products distributed to uses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "USES LP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_to_uses": 1,
        "priorities_forestry_among_uses": 1,
        "width_of_forestry_products_distribution_among_uses_sp": 1,
        "land_products_available_to_each_region": 1,
    },
)
def forestry_products_distributed_to_uses():
    """
    allocation of frestry products to uses inside each region (energy , materials)
    """
    return allocate_by_priority(
        wood_demanded_to_uses(),
        priorities_forestry_among_uses(),
        width_of_forestry_products_distribution_among_uses_sp(),
        land_products_available_to_each_region().loc[:, "WOOD"].reset_coords(drop=True),
    )


@component.add(
    name="land products available",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"land_products_available_from_croplands": 11, "roundwood_extracted": 1},
)
def land_products_available():
    """
    Land products available (produced)
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
        land_products_available_from_croplands()
        .loc[:, "CORN"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"]] = (
        land_products_available_from_croplands()
        .loc[:, "RICE"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"]] = (
        land_products_available_from_croplands()
        .loc[:, "CEREALS OTHER"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"]] = (
        land_products_available_from_croplands()
        .loc[:, "TUBERS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"]] = (
        land_products_available_from_croplands()
        .loc[:, "SOY"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"]] = (
        land_products_available_from_croplands()
        .loc[:, "PULSES NUTS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "OILCROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "SUGAR CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"]] = (
        land_products_available_from_croplands()
        .loc[:, "FRUITS VEGETABLES"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"]] = (
        land_products_available_from_croplands()
        .loc[:, "BIOFUEL 2GCROP"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"]] = (
        land_products_available_from_croplands()
        .loc[:, "OTHER CROPS"]
        .reset_coords(drop=True)
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"]] = (
        roundwood_extracted().expand_dims({"LAND PRODUCTS I": ["WOOD"]}, 1).values
    )
    value.loc[:, ["RESIDUES"]] = 0
    return value


@component.add(
    name="land products available all regions",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_available": 1},
)
def land_products_available_all_regions():
    """
    Land products available, all regions added
    """
    return sum(
        land_products_available().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="land products available in global pool",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_available": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_available_in_global_pool():
    """
    La products that enter the global allocation. The allocation is considered to be a pool market where all the regions offer they production (ecxept the protected) and all ask to the pool according to its demand.
    """
    return np.maximum(
        0, land_products_available() - land_products_protected_from_global_pool()
    )


@component.add(
    name="land products available in global pool all regions",
    units="t/Year",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_products_available_in_global_pool": 1},
)
def land_products_available_in_global_pool_all_regions():
    """
    global land products available in global market
    """
    return sum(
        land_products_available_in_global_pool().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="land products available to each region",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_distributed_from_pool": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_available_to_each_region():
    """
    Land products available to each region
    """
    return (
        land_products_distributed_from_pool()
        + land_products_protected_from_global_pool().transpose(
            "LAND PRODUCTS I", "REGIONS 9 I"
        )
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="land products demanded to pool",
    units="t/Year",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded": 1,
        "land_products_protected_from_global_pool": 1,
    },
)
def land_products_demanded_to_pool():
    """
    Land products demanded in global pool distribution. The allocation is considered to be a pool market where all the regions offer they production (except the protected) and all ask to the pool according to its demand.
    """
    value = xr.DataArray(
        np.nan,
        {
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        },
        ["LAND PRODUCTS I", "REGIONS 9 I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["OTHER CROPS"], :] = False
    value.values[except_subs.values] = (
        np.maximum(
            0, land_products_demanded() - land_products_protected_from_global_pool()
        )
        .transpose("LAND PRODUCTS I", "REGIONS 9 I")
        .values[except_subs.values]
    )
    value.loc[["OTHER CROPS"], :] = 0
    return value


@component.add(
    name="land products distributed from pool",
    units="t/Year",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded_to_pool": 1,
        "priorities_of_land_products_distribution_among_regions_sp": 1,
        "width_of_land_products_distribution_among_regions_sp": 1,
        "land_products_available_in_global_pool_all_regions": 1,
    },
)
def land_products_distributed_from_pool():
    """
    Allocate by priority function to distribute he land products that participate the global pool distributed to each region. The allocation is considered to be a pool market where all the regions offer they production (ecxept the protected) and all ask to the pool according to its demand.
    """
    return allocate_by_priority(
        land_products_demanded_to_pool(),
        priorities_of_land_products_distribution_among_regions_sp(),
        width_of_land_products_distribution_among_regions_sp(),
        land_products_available_in_global_pool_all_regions(),
    )


@component.add(
    name="land products protected from global pool",
    units="t/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_products_demanded": 2,
        "land_products_available": 2,
        "share_of_land_products_from_smallholders": 2,
    },
)
def land_products_protected_from_global_pool():
    """
    Land prodcuts produced by small holders or protected by policies from interchange in global markets that do not enter the global pool distritucion
    """
    return if_then_else(
        land_products_demanded()
        > land_products_available() * share_of_land_products_from_smallholders(),
        lambda: land_products_available() * share_of_land_products_from_smallholders(),
        lambda: land_products_demanded(),
    )


@component.add(
    name="priorities crops among uses",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I", "USES LP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"priorities_of_crops_distribution_among_uses_sp": 13},
)
def priorities_crops_among_uses():
    """
    AUXILIAR priorities of crops among uses
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            "USES LP I": _subscript_dict["USES LP I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I", "USES LP I"],
    )
    value.loc[:, ["CORN"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["CORN"]}, 1)
        .values
    )
    value.loc[:, ["RICE"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["RICE"]}, 1)
        .values
    )
    value.loc[:, ["CEREALS OTHER"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["CEREALS OTHER"]}, 1)
        .values
    )
    value.loc[:, ["TUBERS"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["TUBERS"]}, 1)
        .values
    )
    value.loc[:, ["SOY"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["SOY"]}, 1)
        .values
    )
    value.loc[:, ["PULSES NUTS"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["PULSES NUTS"]}, 1)
        .values
    )
    value.loc[:, ["OILCROPS"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["OILCROPS"]}, 1)
        .values
    )
    value.loc[:, ["SUGAR CROPS"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["SUGAR CROPS"]}, 1)
        .values
    )
    value.loc[:, ["FRUITS VEGETABLES"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["FRUITS VEGETABLES"]}, 1)
        .values
    )
    value.loc[:, ["BIOFUEL 2GCROP"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["BIOFUEL 2GCROP"]}, 1)
        .values
    )
    value.loc[:, ["OTHER CROPS"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["OTHER CROPS"]}, 1)
        .values
    )
    value.loc[:, ["WOOD"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["WOOD"]}, 1)
        .values
    )
    value.loc[:, ["RESIDUES"], :] = (
        priorities_of_crops_distribution_among_uses_sp()
        .expand_dims({"LAND PRODUCTS I": ["RESIDUES"]}, 1)
        .values
    )
    return value


@component.add(
    name="priorities forestry among uses",
    units="DMNL",
    subscripts=["REGIONS 9 I", "USES LP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"priorities_of_forestry_products_distribution_among_uses_sp": 1},
)
def priorities_forestry_among_uses():
    """
    AUXILIAR priorities of forestry products among uses
    """
    return priorities_of_forestry_products_distribution_among_uses_sp()


@component.add(
    name="share of land products from smallholders",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_land_products_from_smallholders": 1},
    other_deps={
        "_integ_share_of_land_products_from_smallholders": {
            "initial": {"initial_share_of_production_from_smallholders": 1},
            "step": {"change_of_the_share_of_land_products_from_smallholders": 1},
        }
    },
)
def share_of_land_products_from_smallholders():
    """
    share of land products protected from global pool distribution, are those produced by small holders that do not interact with global markets or those protected by policies of trade restriction between regions
    """
    return _integ_share_of_land_products_from_smallholders()


_integ_share_of_land_products_from_smallholders = Integ(
    lambda: change_of_the_share_of_land_products_from_smallholders(),
    lambda: initial_share_of_production_from_smallholders(),
    "_integ_share_of_land_products_from_smallholders",
)


@component.add(
    name="shortage of forestry products for energy",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_forestry_products_for_energy": 2},
)
def shortage_of_forestry_products_for_energy():
    """
    Signal to measure the shortage of forestry products for energy in each region. If it is >0 there is a shortage
    """
    return if_then_else(
        availability_of_forestry_products_for_energy() > 1,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: -availability_of_forestry_products_for_energy(),
    )


@component.add(
    name="signal availability forestry products for energy",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"availability_of_forestry_products_for_energy": 1},
)
def signal_availability_forestry_products_for_energy():
    """
    If =1: available equals demanded (no scarcity), if =0 total scarcity Signal to measure the abundance or shortage of wood for energy in each region. If demand can be met, availability of forestry products for energy =1, if it is 0.2, for example, 20% of the demand cannot be met. supply includes international trade
    """
    return availability_of_forestry_products_for_energy()


@component.add(
    name="wood demanded to uses",
    units="t/Year",
    subscripts=["REGIONS 9 I", "USES LP I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_industry": 1,
        "wood_demanded_for_energy_converted_to_tonnes": 1,
    },
)
def wood_demanded_to_uses():
    """
    wood demanded for energy and materials
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "USES LP I": _subscript_dict["USES LP I"],
        },
        ["REGIONS 9 I", "USES LP I"],
    )
    value.loc[:, ["LP FOOD"]] = 0
    value.loc[:, ["LP INDUSTRY"]] = (
        wood_demanded_for_industry()
        .expand_dims({"USES LP I": ["LP INDUSTRY"]}, 1)
        .values
    )
    value.loc[:, ["LP ENERGY FORESTRY"]] = (
        wood_demanded_for_energy_converted_to_tonnes()
        .expand_dims({"USES LP I": ["LP ENERGY FORESTRY"]}, 1)
        .values
    )
    value.loc[:, ["LP ENERGY AGRICULTURAL"]] = 0
    return value
