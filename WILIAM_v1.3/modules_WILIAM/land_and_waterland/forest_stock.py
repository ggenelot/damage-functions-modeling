"""
Module land_and_waterland.forest_stock
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual growth rate of primary forests",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficient_of_growth_forest_primary": 1,
        "primary_forest_volumen_per_area": 1,
        "maximum_stock_per_area_forest_primary": 1,
    },
)
def annual_growth_rate_of_primary_forests():
    """
    annual growth rate of forest stocks
    """
    return coefficient_of_growth_forest_primary() * (
        1
        - zidz(
            primary_forest_volumen_per_area(), maximum_stock_per_area_forest_primary()
        )
    )


@component.add(
    name="biomass stock all forests",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_biomass_stock_all_forests": 1},
    other_deps={
        "_integ_biomass_stock_all_forests": {
            "initial": {
                "initial_time": 1,
                "historical_forest_volume_stock_all_forests": 1,
            },
            "step": {"change_of_all_forests_stock": 1},
        }
    },
)
def biomass_stock_all_forests():
    """
    forest volume stock
    """
    return _integ_biomass_stock_all_forests()


_integ_biomass_stock_all_forests = Integ(
    lambda: change_of_all_forests_stock(),
    lambda: historical_forest_volume_stock_all_forests(initial_time()),
    "_integ_biomass_stock_all_forests",
)


@component.add(
    name="biomass stock forest primay",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "land_use_area_by_region": 1,
        "maximum_stock_per_area_forest_primary": 1,
    },
)
def biomass_stock_forest_primay():
    """
    biomass above ground stock of primary forests
    """
    return (
        land_use_area_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
        * maximum_stock_per_area_forest_primary()
    )


@component.add(
    name="change of all forests stock",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "biomass_stock_all_forests": 1,
        "historical_forest_volume_stock_all_forests": 1,
        "initial_time": 1,
        "forest_volume_stock_changes": 1,
    },
)
def change_of_all_forests_stock():
    """
    increase of forest volume stock
    """
    return if_then_else(
        biomass_stock_all_forests()
        <= 0.08 * historical_forest_volume_stock_all_forests(initial_time()),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: forest_volume_stock_changes(),
    )


@component.add(
    name="forest planetary boundary volume",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def forest_planetary_boundary_volume():
    """
    forestry planetary boundary, not implemented
    """
    return xr.DataArray(
        1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="forest planetary boundary weight",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forest_planetary_boundary_volume": 1, "wood_density_by_region": 1},
)
def forest_planetary_boundary_weight():
    """
    not implemented
    """
    return forest_planetary_boundary_volume() * wood_density_by_region()


@component.add(
    name="forest primary area lost",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_changes_productive_uses": 2},
)
def forest_primary_area_lost():
    """
    forest area lost primary forests, >0 means forest are is lost
    """
    return if_then_else(
        land_use_changes_productive_uses()
        .loc[:, "FOREST PRIMARY"]
        .reset_coords(drop=True)
        < 0,
        lambda: -land_use_changes_productive_uses()
        .loc[:, "FOREST PRIMARY"]
        .reset_coords(drop=True),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="forest stock change net afforestation",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "volume_stock_change_net_afforestation_m_and_p": 1,
        "forest_primary_area_lost": 1,
        "maximum_forest_stock_per_area": 1,
    },
)
def forest_stock_change_net_afforestation():
    """
    total change of forest biomass due to net afforestation all forests
    """
    return (
        volume_stock_change_net_afforestation_m_and_p()
        - forest_primary_area_lost() * maximum_forest_stock_per_area()
    )


@component.add(
    name="forest volume stock changes",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "time_historical_data_land_module": 1,
        "historical_forest_volume_stock_change_all_forests": 1,
        "roundwood_volumme_extracted_from_forest_m_and_p": 1,
        "growth_forest_all": 1,
        "forest_stock_change_net_afforestation": 1,
        "natural_disturbance_all_forest": 1,
    },
)
def forest_volume_stock_changes():
    """
    forest volume stock changes.
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_forest_volume_stock_change_all_forests(time()),
        lambda: growth_forest_all()
        - roundwood_volumme_extracted_from_forest_m_and_p()
        + forest_stock_change_net_afforestation()
        - natural_disturbance_all_forest(),
    )


@component.add(
    name="forest volume stock per unit area",
    units="m3/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"biomass_stock_all_forests": 1, "total_forest_area": 1},
)
def forest_volume_stock_per_unit_area():
    """
    forest volume stock per unit area
    """
    return biomass_stock_all_forests() / total_forest_area()


@component.add(
    name="forestry sustainability index by region",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def forestry_sustainability_index_by_region():
    """
    forestry sustainability index by region. nOT CHECKED.
    """
    return xr.DataArray(
        1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )


@component.add(
    name="forests stock all forests global",
    units="m3",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"biomass_stock_all_forests": 1},
)
def forests_stock_all_forests_global():
    """
    forests_stock_all_forests_global
    """
    return sum(
        biomass_stock_all_forests().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="growth forest all",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "growth_forest_m_and_p": 1,
        "annual_growth_rate_of_primary_forests": 1,
        "biomass_stock_forest_primay": 1,
    },
)
def growth_forest_all():
    """
    forest stock increment
    """
    return (
        growth_forest_m_and_p()
        + biomass_stock_forest_primay() * annual_growth_rate_of_primary_forests()
    )


@component.add(
    name="historical stock all forests",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_forest_volume_stock_all_forests": 1},
)
def historical_stock_all_forests():
    """
    biomass volume avobe ground all forests, historical data
    """
    return historical_forest_volume_stock_all_forests(time())


@component.add(
    name="maximum forest stock all forests",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_forest_stock_per_area": 1, "total_forest_area": 1},
)
def maximum_forest_stock_all_forests():
    """
    maximum achievable biomass stock all forests
    """
    return maximum_forest_stock_per_area() * total_forest_area()


@component.add(
    name="maximum stock per area forest primary",
    units="m3/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_forest_stock_per_area": 1, "coefficient_max_stock_primary": 1},
)
def maximum_stock_per_area_forest_primary():
    """
    maximum stock of biomass of primary forests
    """
    return maximum_forest_stock_per_area() * coefficient_max_stock_primary()


@component.add(
    name="natural disturbance all forest",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"natural_disturbance_forests_m_and_p": 1},
)
def natural_disturbance_all_forest():
    """
    loss of stock due to natural causes
    """
    return natural_disturbance_forests_m_and_p()


@component.add(
    name="primary forest volumen per area",
    units="m3/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"biomass_stock_forest_primay": 1, "land_use_area_by_region": 1},
)
def primary_forest_volumen_per_area():
    """
    maximim volume per area forest primary
    """
    return zidz(
        biomass_stock_forest_primay(),
        land_use_area_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True),
    )


@component.add(
    name="total forest area",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 3},
)
def total_forest_area():
    """
    total forest area
    """
    return (
        land_use_area_by_region().loc[:, "FOREST MANAGED"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST PLANTATIONS"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
    )
