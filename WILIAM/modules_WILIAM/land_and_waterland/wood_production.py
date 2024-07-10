"""
Module land_and_waterland.wood_production
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual growth rate of forest M and P",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficient_of_growth_forest_plantations": 1,
        "proportion_of_plantations_in_forest_m_and_p": 2,
        "coefficient_of_growth_forest_managed": 1,
        "maximum_forest_stock_per_area": 1,
        "volume_stock_per_area_forest_m_and_p": 1,
    },
)
def annual_growth_rate_of_forest_m_and_p():
    """
    annual growth rate of forest stocks,
    """
    return (
        coefficient_of_growth_forest_plantations()
        * proportion_of_plantations_in_forest_m_and_p()
        + coefficient_of_growth_forest_managed()
        * (1 - proportion_of_plantations_in_forest_m_and_p())
    ) * (
        1
        - zidz(volume_stock_per_area_forest_m_and_p(), maximum_forest_stock_per_area())
    )


@component.add(
    name="area forest M and P",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 5},
)
def area_forest_m_and_p():
    """
    total forest area
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = (
        land_use_area_by_region().loc[:, "FOREST MANAGED"].reset_coords(drop=True)
        + land_use_area_by_region().loc[:, "FOREST PLANTATIONS"].reset_coords(drop=True)
    ).values[except_subs.values]
    value.loc[["INDIA"]] = (
        float(land_use_area_by_region().loc["INDIA", "FOREST MANAGED"])
        + float(land_use_area_by_region().loc["INDIA", "FOREST PRIMARY"])
        + float(land_use_area_by_region().loc["INDIA", "FOREST PLANTATIONS"])
    )
    return value


@component.add(
    name="area gain of forests M and P",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Delay",
    depends_on={
        "land_use_changes_productive_uses": 2,
        "_delay_area_gain_of_forests_m_and_p": 1,
    },
    other_deps={
        "_delay_area_gain_of_forests_m_and_p": {
            "initial": {
                "land_use_changes_productive_uses": 2,
                "time_of_forest_maturation": 1,
            },
            "step": {
                "land_use_changes_productive_uses": 2,
                "time_of_forest_maturation": 1,
            },
        }
    },
)
def area_gain_of_forests_m_and_p():
    """
    gain of area of forests, aforestation
    """
    return if_then_else(
        land_use_changes_productive_uses()
        .loc[:, "FOREST MANAGED"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST PLANTATIONS"]
        .reset_coords(drop=True)
        >= 0,
        lambda: _delay_area_gain_of_forests_m_and_p(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


_delay_area_gain_of_forests_m_and_p = Delay(
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST MANAGED"]
    .reset_coords(drop=True)
    + land_use_changes_productive_uses()
    .loc[:, "FOREST PLANTATIONS"]
    .reset_coords(drop=True),
    lambda: time_of_forest_maturation(),
    lambda: land_use_changes_productive_uses()
    .loc[:, "FOREST MANAGED"]
    .reset_coords(drop=True)
    + land_use_changes_productive_uses()
    .loc[:, "FOREST PLANTATIONS"]
    .reset_coords(drop=True),
    lambda: 3,
    time_step,
    "_delay_area_gain_of_forests_m_and_p",
)


@component.add(
    name="area loss of forest M and P",
    units="km2/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_changes_productive_uses": 4},
)
def area_loss_of_forest_m_and_p():
    """
    Are of managed forests and plantations lost
    """
    return if_then_else(
        land_use_changes_productive_uses()
        .loc[:, "FOREST MANAGED"]
        .reset_coords(drop=True)
        + land_use_changes_productive_uses()
        .loc[:, "FOREST PLANTATIONS"]
        .reset_coords(drop=True)
        < 0,
        lambda: -(
            land_use_changes_productive_uses()
            .loc[:, "FOREST MANAGED"]
            .reset_coords(drop=True)
            + land_use_changes_productive_uses()
            .loc[:, "FOREST PLANTATIONS"]
            .reset_coords(drop=True)
        ),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="biomass stock of managed forest and plantations",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_biomass_stock_of_managed_forest_and_plantations": 1},
    other_deps={
        "_integ_biomass_stock_of_managed_forest_and_plantations": {
            "initial": {
                "initial_time": 1,
                "historical_forest_volume_stock_all_forests": 1,
                "initial_land_use_by_region": 1,
                "coefficient_max_stock_primary": 1,
                "maximum_forest_stock_per_area": 1,
            },
            "step": {"change_of_stock_forest_m_and_p": 1},
        }
    },
)
def biomass_stock_of_managed_forest_and_plantations():
    """
    forest volume stock of avobe ground biomass of managed forest and plantations,
    """
    return _integ_biomass_stock_of_managed_forest_and_plantations()


_integ_biomass_stock_of_managed_forest_and_plantations = Integ(
    lambda: change_of_stock_forest_m_and_p(),
    lambda: historical_forest_volume_stock_all_forests(initial_time())
    - initial_land_use_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
    * maximum_forest_stock_per_area()
    * coefficient_max_stock_primary(),
    "_integ_biomass_stock_of_managed_forest_and_plantations",
)


@component.add(
    name="change of stock forest M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful, Auxiliary",
    comp_subtype="Normal, Smooth",
    depends_on={
        "biomass_stock_of_managed_forest_and_plantations": 1,
        "initial_volume_stock_of_forest_m_and_p": 1,
        "volume_stock_changes_forest_m_and_p": 1,
        "_smooth_change_of_stock_forest_m_and_p": 1,
    },
    other_deps={
        "_smooth_change_of_stock_forest_m_and_p": {
            "initial": {
                "biomass_stock_of_managed_forest_and_plantations": 1,
                "initial_volume_stock_of_forest_m_and_p": 1,
                "volume_stock_changes_forest_m_and_p": 1,
            },
            "step": {
                "biomass_stock_of_managed_forest_and_plantations": 1,
                "initial_volume_stock_of_forest_m_and_p": 1,
                "volume_stock_changes_forest_m_and_p": 1,
            },
        }
    },
)
def change_of_stock_forest_m_and_p():
    """
    increase of forest volume stock. If the stock of forest is less than 1% of initial valur, extraction stops to avoid negative stock.
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = if_then_else(
        biomass_stock_of_managed_forest_and_plantations()
        > 0.055 * initial_volume_stock_of_forest_m_and_p(),
        lambda: volume_stock_changes_forest_m_and_p(),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    ).values[except_subs.values]
    value.loc[["INDIA"]] = _smooth_change_of_stock_forest_m_and_p().values
    return value


_smooth_change_of_stock_forest_m_and_p = Smooth(
    lambda: xr.DataArray(
        if_then_else(
            float(biomass_stock_of_managed_forest_and_plantations().loc["INDIA"])
            > 0.055 * float(initial_volume_stock_of_forest_m_and_p().loc["INDIA"]),
            lambda: float(volume_stock_changes_forest_m_and_p().loc["INDIA"]),
            lambda: 0,
        ),
        {"REGIONS 35 I": ["INDIA"]},
        ["REGIONS 35 I"],
    ),
    lambda: xr.DataArray(5, {"REGIONS 35 I": ["INDIA"]}, ["REGIONS 35 I"]),
    lambda: xr.DataArray(
        if_then_else(
            float(biomass_stock_of_managed_forest_and_plantations().loc["INDIA"])
            > 0.055 * float(initial_volume_stock_of_forest_m_and_p().loc["INDIA"]),
            lambda: float(volume_stock_changes_forest_m_and_p().loc["INDIA"]),
            lambda: 0,
        ),
        {"REGIONS 35 I": ["INDIA"]},
        ["REGIONS 35 I"],
    ),
    lambda: 1,
    "_smooth_change_of_stock_forest_m_and_p",
)


@component.add(
    name="global availability of biomass",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "roundwood_available_world": 1,
        "roundwood_demanded_world": 1,
        "historical_roundwood_harvested": 1,
        "initial_time": 1,
    },
)
def global_availability_of_biomass():
    """
    difference between demanded and available biomass (=0 meand no shortage) This should be always zero since there are no restrictions set to wood extraction, until all the forests are cut!
    """
    return zidz(
        roundwood_available_world() - roundwood_demanded_world(),
        sum(
            historical_roundwood_harvested(initial_time()).rename(
                {"REGIONS 9 I": "REGIONS 9 I!"}
            ),
            dim=["REGIONS 9 I!"],
        ),
    )


@component.add(
    name="global roundwood demand distributed as trends",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_roundwood_for_energy_distributed": 1,
        "global_roundwood_for_industry_distributed": 1,
    },
)
def global_roundwood_demand_distributed_as_trends():
    """
    Demand of roundwood to producing regions acording to present shares of distribution (global market of wood)
    """
    return (
        global_roundwood_for_energy_distributed()
        + global_roundwood_for_industry_distributed()
    )


@component.add(
    name="global roundwood demand distributed to regions",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_roundwood_demand_distributed_as_trends": 1,
        "share_of_self_suficiency_of_forestry_products": 2,
        "global_roundwood_demand_self_suficiency": 1,
        "limit_to_forest_extraction": 1,
    },
)
def global_roundwood_demand_distributed_to_regions():
    """
    Demand of roundwood distributed to regions is a compbination of the one destributed as present and the one by policy of self suficiency.Share of self suficiency =1 --> all regions produce their wood
    """
    return (
        global_roundwood_demand_distributed_as_trends()
        * (1 - share_of_self_suficiency_of_forestry_products())
        + global_roundwood_demand_self_suficiency()
        * share_of_self_suficiency_of_forestry_products()
    ) * limit_to_forest_extraction()


@component.add(
    name="global roundwood demand self suficiency",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_demanded_for_energy_and_industry": 1},
)
def global_roundwood_demand_self_suficiency():
    """
    In 100% self suficiency each regions produces the wood that demands
    """
    return roundwood_demanded_for_energy_and_industry()


@component.add(
    name="global roundwood for energy distributed",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_energy_world": 1,
        "share_of_wood_for_energy_extraction_by_region": 1,
    },
)
def global_roundwood_for_energy_distributed():
    """
    Demand of wood for energy to producing regions acording to present shares of distribution (global market of wood)
    """
    return (
        wood_demanded_for_energy_world()
        * share_of_wood_for_energy_extraction_by_region()
    )


@component.add(
    name="global roundwood for industry distributed",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "wood_demanded_for_industry_world": 1,
        "share_of_wood_for_industry_extraction_by_region": 1,
    },
)
def global_roundwood_for_industry_distributed():
    """
    Demand of wood for industry to producing regions acording to present shares of distribution (global market of wood)
    """
    return (
        wood_demanded_for_industry_world()
        * share_of_wood_for_industry_extraction_by_region()
    )


@component.add(
    name="growth forest M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "biomass_stock_of_managed_forest_and_plantations": 1,
        "annual_growth_rate_of_forest_m_and_p": 1,
    },
)
def growth_forest_m_and_p():
    """
    forest stock increment
    """
    return (
        biomass_stock_of_managed_forest_and_plantations()
        * annual_growth_rate_of_forest_m_and_p()
    )


@component.add(
    name="historical roundwood extracted world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"historical_wood_extracted": 1},
)
def historical_roundwood_extracted_world():
    """
    historical wood extracted, world
    """
    return sum(
        historical_wood_extracted().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="historical vol stock change forest M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_volume_stock_forest_m_and_p": 1,
        "historical_volume_stock_forest_m_and_p_delayed": 1,
    },
)
def historical_vol_stock_change_forest_m_and_p():
    """
    estimation of historical change volume of managed forests and plantations
    """
    return (
        historical_volume_stock_forest_m_and_p()
        - historical_volume_stock_forest_m_and_p_delayed()
    )


@component.add(
    name="historical volume stock forest M and P",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historical_forest_volume_stock_all_forests": 1,
        "historical_volume_stock_forest_primary": 1,
    },
)
def historical_volume_stock_forest_m_and_p():
    """
    historical estimated volume stock of forest managed and plantations
    """
    return (
        historical_forest_volume_stock_all_forests(time())
        - historical_volume_stock_forest_primary()
    )


@component.add(
    name="historical volume stock forest M and P delayed",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_historical_volume_stock_forest_m_and_p_delayed": 1},
    other_deps={
        "_delayfixed_historical_volume_stock_forest_m_and_p_delayed": {
            "initial": {"intial_stock_m_and_p": 1},
            "step": {"historical_volume_stock_forest_m_and_p": 1},
        }
    },
)
def historical_volume_stock_forest_m_and_p_delayed():
    """
    auxiliar
    """
    return _delayfixed_historical_volume_stock_forest_m_and_p_delayed()


_delayfixed_historical_volume_stock_forest_m_and_p_delayed = DelayFixed(
    lambda: historical_volume_stock_forest_m_and_p(),
    lambda: 1,
    lambda: intial_stock_m_and_p(),
    time_step,
    "_delayfixed_historical_volume_stock_forest_m_and_p_delayed",
)


@component.add(
    name="historical volume stock forest primary",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1, "maximum_forest_stock_per_area": 1},
)
def historical_volume_stock_forest_primary():
    """
    Volume stock of biomass in primary forests, we assume primary forests are close to their maximum stock per area as in Roebroeck et. al 2022
    """
    return (
        land_use_area_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
        * maximum_forest_stock_per_area()
    )


@component.add(
    name="historical wood extracted",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "historical_roundwood_harvested": 2},
)
def historical_wood_extracted():
    """
    Exogenous wood extration. Only active if SWITCH_LANDWATER=0
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = historical_roundwood_harvested(time()).values[
        except_subs.values
    ]
    value.loc[["INDIA"]] = float(historical_roundwood_harvested(time()).loc["INDIA"])
    return value


@component.add(
    name="increase of self suficiency forestry",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_forestry_self_sufficiency": 1,
        "time": 2,
        "objective_forestry_self_sufficiency_sp": 1,
        "switch_forestry_self_sufficiency_sp": 1,
        "year_final_forestry_self_sufficiency_sp": 2,
        "year_initial_forestry_self_sufficiency_sp": 2,
    },
)
def increase_of_self_suficiency_forestry():
    """
    Increase of the self suficiency of regions in wood production, =1 means that each region produces its wood demanded
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_forestry_self_sufficiency(),
        lambda: if_then_else(
            np.logical_and(
                switch_forestry_self_sufficiency_sp() == 1,
                np.logical_and(
                    time() > year_initial_forestry_self_sufficiency_sp(),
                    time() < year_final_forestry_self_sufficiency_sp(),
                ),
            ),
            lambda: objective_forestry_self_sufficiency_sp()
            / (
                year_final_forestry_self_sufficiency_sp()
                - year_initial_forestry_self_sufficiency_sp()
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        ),
    )


@component.add(
    name="intial stock M and P",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_time": 1,
        "historical_forest_volume_stock_all_forests": 1,
        "initial_land_use_by_region": 1,
        "maximum_forest_stock_per_area": 1,
    },
)
def intial_stock_m_and_p():
    return (
        historical_forest_volume_stock_all_forests(initial_time())
        - initial_land_use_by_region().loc[:, "FOREST PRIMARY"].reset_coords(drop=True)
        * maximum_forest_stock_per_area()
    )


@component.add(
    name="limit to forest extraction",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful, Auxiliary",
    comp_subtype="Normal, Smooth",
    depends_on={
        "biomass_stock_all_forests": 3,
        "stock_of_forest_volume_protected": 4,
        "_smooth_limit_to_forest_extraction": 1,
    },
    other_deps={
        "_smooth_limit_to_forest_extraction": {
            "initial": {
                "biomass_stock_all_forests": 3,
                "stock_of_forest_volume_protected": 4,
            },
            "step": {
                "biomass_stock_all_forests": 3,
                "stock_of_forest_volume_protected": 4,
            },
        }
    },
)
def limit_to_forest_extraction():
    """
    =1 no limit =0 extraction is set to zero
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = if_then_else(
        biomass_stock_all_forests() >= stock_of_forest_volume_protected() * 1.05,
        lambda: xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: if_then_else(
            biomass_stock_all_forests() <= stock_of_forest_volume_protected(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: (biomass_stock_all_forests() - stock_of_forest_volume_protected())
            / (0.05 * stock_of_forest_volume_protected()),
        ),
    ).values[except_subs.values]
    value.loc[["INDIA"]] = _smooth_limit_to_forest_extraction().values
    return value


_smooth_limit_to_forest_extraction = Smooth(
    lambda: xr.DataArray(
        if_then_else(
            float(biomass_stock_all_forests().loc["INDIA"])
            >= float(stock_of_forest_volume_protected().loc["INDIA"]) * 1.05,
            lambda: 1,
            lambda: if_then_else(
                float(biomass_stock_all_forests().loc["INDIA"])
                <= float(stock_of_forest_volume_protected().loc["INDIA"]),
                lambda: 0,
                lambda: (
                    float(biomass_stock_all_forests().loc["INDIA"])
                    - float(stock_of_forest_volume_protected().loc["INDIA"])
                )
                / (0.05 * float(stock_of_forest_volume_protected().loc["INDIA"])),
            ),
        ),
        {"REGIONS 35 I": ["INDIA"]},
        ["REGIONS 35 I"],
    ),
    lambda: xr.DataArray(7, {"REGIONS 35 I": ["INDIA"]}, ["REGIONS 35 I"]),
    lambda: xr.DataArray(
        if_then_else(
            float(biomass_stock_all_forests().loc["INDIA"])
            >= float(stock_of_forest_volume_protected().loc["INDIA"]) * 1.05,
            lambda: 1,
            lambda: if_then_else(
                float(biomass_stock_all_forests().loc["INDIA"])
                <= float(stock_of_forest_volume_protected().loc["INDIA"]),
                lambda: 0,
                lambda: (
                    float(biomass_stock_all_forests().loc["INDIA"])
                    - float(stock_of_forest_volume_protected().loc["INDIA"])
                )
                / (0.05 * float(stock_of_forest_volume_protected().loc["INDIA"])),
            ),
        ),
        {"REGIONS 35 I": ["INDIA"]},
        ["REGIONS 35 I"],
    ),
    lambda: 1,
    "_smooth_limit_to_forest_extraction",
)


@component.add(
    name="loss of forest stock M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"change_of_stock_forest_m_and_p": 1},
)
def loss_of_forest_stock_m_and_p():
    """
    If stock is loss this is positive,
    """
    return -change_of_stock_forest_m_and_p()


@component.add(
    name="maximum stock forest M and P",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"area_forest_m_and_p": 1, "maximum_forest_stock_per_area": 1},
)
def maximum_stock_forest_m_and_p():
    return area_forest_m_and_p() * maximum_forest_stock_per_area()


@component.add(
    name="natural disturbance forests M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "coefficient_of_forest_distrurbance": 1,
        "biomass_stock_of_managed_forest_and_plantations": 1,
    },
)
def natural_disturbance_forests_m_and_p():
    """
    Loss of forest stock due to natural causes with no human intervention
    """
    return (
        coefficient_of_forest_distrurbance()
        * biomass_stock_of_managed_forest_and_plantations()
    )


@component.add(
    name="OBJECTIVE FOREST LOSS LIMIT SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_forest_loss_limit_sp"},
)
def objective_forest_loss_limit_sp():
    """
    IF =1 the policy that limits the volume of forest that can be loss per region is limited between initial and final time, relative to 2019 value of forest volume stock
    """
    return _ext_constant_objective_forest_loss_limit_sp()


_ext_constant_objective_forest_loss_limit_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "OBJECTIVE_FOREST_LOSS_LIMIT_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_forest_loss_limit_sp",
)


@component.add(
    name="proportion of plantations in forest M and P",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"land_use_area_by_region": 1, "area_forest_m_and_p": 1},
)
def proportion_of_plantations_in_forest_m_and_p():
    """
    proportion of plantations in the total forest area
    """
    return (
        land_use_area_by_region().loc[:, "FOREST PLANTATIONS"].reset_coords(drop=True)
        / area_forest_m_and_p()
    )


@component.add(
    name="roundwood available world",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_extracted": 1},
)
def roundwood_available_world():
    """
    Available wood
    """
    return sum(
        roundwood_extracted().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="roundwood extracted",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "historical_wood_extracted": 1,
        "biomass_stock_of_managed_forest_and_plantations": 1,
        "initial_volume_stock_of_forest_m_and_p": 1,
        "global_roundwood_demand_distributed_to_regions": 1,
    },
)
def roundwood_extracted():
    """
    All the roundwood that is demanded is extracted, no limits to extraction (as long as there is forest area) IF_THEN_ELSE(Time<=TIME_HISTORICAL_DATA_LAND_MODULE, historical_wood_extracted[REGIONS 9 I], IF_THEN_ELSE( stock_of_managed_forest_and_plantations[REGIONS 9 I]> 0.01*INITIAL_VOLUME_STOCK_OF_FOREST_M_AND_P[REGIONS 9 I ] , global_roundwood_demand_distributed_to_regions[REGIONS 9 I],0))
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_wood_extracted(),
        lambda: if_then_else(
            biomass_stock_of_managed_forest_and_plantations()
            > 0.01 * initial_volume_stock_of_forest_m_and_p(),
            lambda: global_roundwood_demand_distributed_to_regions(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        ),
    )


@component.add(
    name="roundwood from deforestation",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundwood_volumme_from_deforestation": 1, "wood_density_by_region": 1},
)
def roundwood_from_deforestation():
    """
    This is not added to the wood available to meet demand
    """
    return roundwood_volumme_from_deforestation() * wood_density_by_region()


@component.add(
    name="roundwood volumme extracted from forest M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "roundwood_extracted": 2,
        "wood_density_by_region": 2,
        "outturn_of_wood_extraction": 2,
    },
)
def roundwood_volumme_extracted_from_forest_m_and_p():
    """
    roundwood harvested from managed forests and plantations (we assume that primary forest have zero extraction, therefore this is all the wood extracted) INDIA data adjusted, no reasonable data found in literatura
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["INDIA"]] = False
    value.values[except_subs.values] = (
        roundwood_extracted()
        / (wood_density_by_region() * outturn_of_wood_extraction())
    ).values[except_subs.values]
    value.loc[["INDIA"]] = float(roundwood_extracted().loc["INDIA"]) / (
        3
        * float(wood_density_by_region().loc["INDIA"])
        * float(outturn_of_wood_extraction().loc["INDIA"])
    )
    return value


@component.add(
    name="roundwood volumme from deforestation",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_roundwood_volumme_from_deforestation": 1},
    other_deps={
        "_delayfixed_roundwood_volumme_from_deforestation": {
            "initial": {},
            "step": {
                "volume_stock_change_net_afforestation_m_and_p": 1,
                "outturn_of_wood_extraction": 1,
            },
        }
    },
)
def roundwood_volumme_from_deforestation():
    """
    wood obtained from the complete deforestation of forests
    """
    return _delayfixed_roundwood_volumme_from_deforestation()


_delayfixed_roundwood_volumme_from_deforestation = DelayFixed(
    lambda: volume_stock_change_net_afforestation_m_and_p()
    * outturn_of_wood_extraction(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_roundwood_volumme_from_deforestation",
)


@component.add(
    name="share of forest stock loss",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "loss_of_forest_stock_m_and_p": 1,
        "biomass_stock_of_managed_forest_and_plantations": 1,
    },
)
def share_of_forest_stock_loss():
    """
    Indicator of forest sustainability. It shows the percent of forest stock loss per year, >0 means loss of forest
    """
    return zidz(
        np.maximum(0, loss_of_forest_stock_m_and_p()),
        biomass_stock_of_managed_forest_and_plantations(),
    )


@component.add(
    name="share of self suficiency of forestry products",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_self_suficiency_of_forestry_products": 1},
    other_deps={
        "_integ_share_of_self_suficiency_of_forestry_products": {
            "initial": {},
            "step": {"increase_of_self_suficiency_forestry": 1},
        }
    },
)
def share_of_self_suficiency_of_forestry_products():
    """
    Share of wood production that is extracted in the same country that demands it
    """
    return _integ_share_of_self_suficiency_of_forestry_products()


_integ_share_of_self_suficiency_of_forestry_products = Integ(
    lambda: increase_of_self_suficiency_forestry(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_share_of_self_suficiency_of_forestry_products",
)


@component.add(
    name="stock of forest volume protected",
    units="m3",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_forest_loss_limit_sp": 1,
        "time": 2,
        "year_initial_forest_loss_limit_sp": 1,
        "year_final_forest_loss_limit_sp": 1,
        "objective_forest_loss_limit_sp": 1,
        "time_historical_data_land_module": 1,
        "historical_forest_volume_stock_all_forests": 1,
    },
)
def stock_of_forest_volume_protected():
    """
    share of forest volume relative to 2019 value that is the limit of extraction
    """
    return if_then_else(
        np.logical_and(
            switch_forest_loss_limit_sp() == 1,
            np.logical_and(
                time() >= year_initial_forest_loss_limit_sp(),
                time() <= year_final_forest_loss_limit_sp(),
            ),
        ),
        lambda: objective_forest_loss_limit_sp()
        * historical_forest_volume_stock_all_forests(
            time_historical_data_land_module()
        ),
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
    )


@component.add(
    name="SWITCH FOREST LOSS LIMIT SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_forest_loss_limit_sp"},
)
def switch_forest_loss_limit_sp():
    """
    IF =1 the policy that limits the volume of forest that can be loss per region is limited between initial and final time, relative to 2019 value of forest volume stock
    """
    return _ext_constant_switch_forest_loss_limit_sp()


_ext_constant_switch_forest_loss_limit_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "SWITCH_FOREST_LOSS_LIMIT_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_forest_loss_limit_sp",
)


@component.add(
    name="volume stock change net afforestation M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "area_gain_of_forests_m_and_p": 1,
        "area_loss_of_forest_m_and_p": 1,
        "volume_stock_per_area_forest_m_and_p": 1,
    },
)
def volume_stock_change_net_afforestation_m_and_p():
    """
    volume of biomass net afforetation
    """
    return (
        area_gain_of_forests_m_and_p() - area_loss_of_forest_m_and_p()
    ) * volume_stock_per_area_forest_m_and_p()


@component.add(
    name="volume stock changes forest M and P",
    units="m3/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "historical_vol_stock_change_forest_m_and_p": 1,
        "natural_disturbance_forests_m_and_p": 1,
        "growth_forest_m_and_p": 1,
        "roundwood_volumme_extracted_from_forest_m_and_p": 1,
        "volume_stock_change_net_afforestation_m_and_p": 1,
    },
)
def volume_stock_changes_forest_m_and_p():
    """
    forest volume stock changes, managed forest and plantations
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: historical_vol_stock_change_forest_m_and_p(),
        lambda: growth_forest_m_and_p()
        - roundwood_volumme_extracted_from_forest_m_and_p()
        + volume_stock_change_net_afforestation_m_and_p()
        - natural_disturbance_forests_m_and_p(),
    )


@component.add(
    name="volume stock per area forest M and P",
    units="m3/km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "biomass_stock_of_managed_forest_and_plantations": 1,
        "area_forest_m_and_p": 1,
    },
)
def volume_stock_per_area_forest_m_and_p():
    """
    forest volume stock per unit area of managed forests and plantations
    """
    return zidz(
        biomass_stock_of_managed_forest_and_plantations(), area_forest_m_and_p()
    )


@component.add(
    name="YEAR FINAL FOREST LOSS LIMIT SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_forest_loss_limit_sp"},
)
def year_final_forest_loss_limit_sp():
    """
    initial year policy forest loss limit
    """
    return _ext_constant_year_final_forest_loss_limit_sp()


_ext_constant_year_final_forest_loss_limit_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_FINAL_FOREST_LOSS_LIMIT_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_forest_loss_limit_sp",
)


@component.add(
    name="YEAR INITIAL FOREST LOSS LIMIT SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_forest_loss_limit_sp"},
)
def year_initial_forest_loss_limit_sp():
    """
    final year policy forest loss limit
    """
    return _ext_constant_year_initial_forest_loss_limit_sp()


_ext_constant_year_initial_forest_loss_limit_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "land_and_water",
    "YEAR_INITIAL_FOREST_LOSS_LIMIT_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_forest_loss_limit_sp",
)
