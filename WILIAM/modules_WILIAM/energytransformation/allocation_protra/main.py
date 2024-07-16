"""
Module energytransformation.allocation_protra.main
Translated using PySD version 3.14.0
"""

@component.add(
    name="aggregated TO production by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 1},
)
def aggregated_to_production_by_commodity():
    """
    Output from PROTRA (after allocation) aggregated
    """
    return sum(
        protra_to_allocated().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="CF nuclear after uranium scarcity",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "switch_mat2nrg_uranium_availability": 1,
        "uranium_extraction_rate": 1,
        "pe_global_demand_uranium": 1,
    },
)
def cf_nuclear_after_uranium_scarcity():
    """
    Capacity factor of nuclear power plants taking into account eventual uranium scarcity.
    """
    return if_then_else(
        np.logical_or(switch_energy() == 0, switch_mat2nrg_uranium_availability() == 0),
        lambda: 1,
        lambda: zidz(uranium_extraction_rate(), pe_global_demand_uranium()),
    )


@component.add(
    name="CF PROTRA",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "unit_conversion_hours_year": 1,
        "protra_operative_capacity_stock_selected": 1,
    },
)
def cf_protra():
    """
    Capacity factor of energy transformation processes.
    """
    return zidz(
        protra_to_allocated(),
        protra_operative_capacity_stock_selected()
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year(),
    )


@component.add(
    name="CF PROTRA FULL LOAD HOURS",
    units="1",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_max_full_load_hours": 1, "unit_conversion_hours_year": 1},
)
def cf_protra_full_load_hours():
    """
    Initial Capacity factor of energy transformation processes.
    """
    return protra_max_full_load_hours() / unit_conversion_hours_year()


@component.add(
    name="CF PROTRA full load hours after constraints",
    units="1",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_hours_year": 1,
    },
)
def cf_protra_full_load_hours_after_constraints():
    """
    Actual capacity factor of energy transformation processes.
    """
    return protra_max_full_load_hours_after_constraints() / unit_conversion_hours_year()


@component.add(
    name="CHP HEAT POWER RATIO 9R",
    subscripts=["REGIONS 9 I", "PROTRA CHP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_chp_heat_power_ratio_9r"},
)
def chp_heat_power_ratio_9r():
    """
    Heat to power ratio of CHPs; value < 1: more elec than heat value > 1: more heat than elec
    """
    return _ext_constant_chp_heat_power_ratio_9r()


_ext_constant_chp_heat_power_ratio_9r = ExtConstant(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "CHP-heat-to-power-ratio",
    "CHP_HEAT_POWER_RATIO_9R",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
    },
    "_ext_constant_chp_heat_power_ratio_9r",
)


@component.add(
    name="CHP production",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA CHP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_heat_allocation": 2,
        "chp_heat_power_ratio_9r": 1,
        "max_to_from_existing_stock_by_protra": 1,
    },
)
def chp_production():
    """
    Production of TO_heat and TO_elec from CHPs based on heat allocation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA CHP I"],
    )
    value.loc[:, ["TO heat"], :] = (
        protra_heat_allocation()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA CHP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], :] = (
        if_then_else(
            max_to_from_existing_stock_by_protra()
            .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA CHP I"})
            == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
                },
                ["REGIONS 9 I", "PROTRA CHP I"],
            ),
            lambda: protra_heat_allocation()
            .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA CHP I"})
            / chp_heat_power_ratio_9r(),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="delayed TS CF nuclear after uranium scarcity",
    units="1",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_cf_nuclear_after_uranium_scarcity": 1},
    other_deps={
        "_delayfixed_delayed_ts_cf_nuclear_after_uranium_scarcity": {
            "initial": {"time_step": 1},
            "step": {"cf_nuclear_after_uranium_scarcity": 1},
        }
    },
)
def delayed_ts_cf_nuclear_after_uranium_scarcity():
    """
    Delay to break simulataneous equations in the feedback demand nuclear -> demand uranium -> uranium availability -> demand nuclear.
    """
    return _delayfixed_delayed_ts_cf_nuclear_after_uranium_scarcity()


_delayfixed_delayed_ts_cf_nuclear_after_uranium_scarcity = DelayFixed(
    lambda: cf_nuclear_after_uranium_scarcity(),
    lambda: time_step(),
    lambda: 1,
    time_step,
    "_delayfixed_delayed_ts_cf_nuclear_after_uranium_scarcity",
)


@component.add(
    name="delayed TS PROTRA capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_protra_capacity_stock": 1},
    other_deps={
        "_delayfixed_delayed_ts_protra_capacity_stock": {
            "initial": {"initial_protra_capacity_stock": 1, "time_step": 1},
            "step": {"protra_operative_capacity_stock_selected": 1},
        }
    },
)
def delayed_ts_protra_capacity_stock():
    """
    Delay to break simulataneous equations in the feedback demand nuclear -> demand uranium -> uranium availability -> demand nuclear.
    """
    return _delayfixed_delayed_ts_protra_capacity_stock()


_delayfixed_delayed_ts_protra_capacity_stock = DelayFixed(
    lambda: protra_operative_capacity_stock_selected(),
    lambda: time_step(),
    lambda: initial_protra_capacity_stock()
    .loc[_subscript_dict["REGIONS 9 I"], :, :]
    .rename({"REGIONS 36 I": "REGIONS 9 I"}),
    time_step,
    "_delayfixed_delayed_ts_protra_capacity_stock",
)


@component.add(
    name="max TO from existing stock by PROTRA",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def max_to_from_existing_stock_by_protra():
    """
    maximum possible TO production volumes that could be produced from the existing transformation capacity (=powerplant, heatplant and CHP) stock
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    )
    value.loc[:, :, _subscript_dict["NRG PROTRA I"]] = np.maximum(
        0,
        protra_operative_capacity_stock_selected()
        * protra_max_full_load_hours_after_constraints()
        * unit_conversion_tw_per_ej_per_year(),
    ).values
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["NRG PROTRA I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="max TO from existing stock by PROTRA HP and CHP",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"max_to_from_existing_stock_by_protra": 1},
)
def max_to_from_existing_stock_by_protra_hp_and_chp():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    )
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP I"]] = (
        max_to_from_existing_stock_by_protra()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA CHP HP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO heat"], :] = True
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="max TO from existing stock by PROTRA PP",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"max_to_from_existing_stock_by_protra": 1},
)
def max_to_from_existing_stock_by_protra_pp():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = (
        max_to_from_existing_stock_by_protra()
        .loc[:, "TO elec", _subscript_dict["PROTRA PP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA PP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA actual full load hours",
    units="h/Year",
    subscripts=["REGIONS 9 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated_in_twh": 2,
        "protra_operative_capacity_stock_selected": 2,
    },
)
def protra_actual_full_load_hours():
    """
    PROTRA_TO_allocated_in_TWh[REGIONS_9_I,TO_elec,NRG_PROTRA_I]/ PROTRA_capacity_stock[REGIONS_9_I,TO_elec,NRG_PROTRA_I]/ UNIT_CONVERSION_HOURS_YEAR PROTRA_TO_allocated_in_TWh[REGIONS_9_I,TO_heat,NRG_PROTRA_I]/PROTRA_capacit y_stock[REGIONS_9_I,TO_heat,NRG_PROTRA_I]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"],
        },
        ["REGIONS 9 I", "PROTRA PP CHP HP I"],
    )
    value.loc[:, _subscript_dict["PROTRA CHP PP I"]] = zidz(
        protra_to_allocated_in_twh()
        .loc[:, "TO elec", _subscript_dict["PROTRA CHP PP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA CHP PP I"}),
        protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", _subscript_dict["PROTRA CHP PP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA CHP PP I"}),
    ).values
    value.loc[:, _subscript_dict["PROTRA HP I"]] = zidz(
        protra_to_allocated_in_twh()
        .loc[:, "TO heat", _subscript_dict["PROTRA HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA HP I"}),
        protra_operative_capacity_stock_selected()
        .loc[:, "TO heat", _subscript_dict["PROTRA HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA HP I"}),
    ).values
    return value


@component.add(
    name="PROTRA capacity utilization rate",
    units="1",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "protra_actual_full_load_hours": 1,
        "protra_max_full_load_hours_after_constraints": 1,
    },
)
def protra_capacity_utilization_rate():
    """
    Rate of utilization of existing PROTRA capacities after allocation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    )
    value.loc[:, _subscript_dict["PROTRA PP CHP HP I"]] = zidz(
        protra_actual_full_load_hours(),
        protra_max_full_load_hours_after_constraints()
        .loc[:, _subscript_dict["PROTRA PP CHP HP I"]]
        .rename({"NRG PROTRA I": "PROTRA PP CHP HP I"}),
    ).values
    value.loc[:, _subscript_dict["PROTRA NP I"]] = 1
    return value


@component.add(
    name="PROTRA elec allocation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_pp": 1,
        "protra_utilization_applied_priorities": 1,
        "remaining_to_to_be_allocated": 1,
    },
)
def protra_elec_allocation():
    """
    allocation of TO_elec to different Powerplant technologies (elec production from CHP has already been allocated in the previous step)
    """
    return allocate_available(
        max_to_from_existing_stock_by_protra_pp()
        .loc[:, "TO elec", :]
        .reset_coords(drop=True),
        protra_utilization_applied_priorities(),
        remaining_to_to_be_allocated().loc[:, "TO elec"].reset_coords(drop=True),
    ).expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)


@component.add(
    name="PROTRA heat allocation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra_hp_and_chp": 1,
        "protra_utilization_applied_priorities": 1,
        "to_by_commodity": 1,
    },
)
def protra_heat_allocation():
    """
    Allocation of (district-)heat demand to available genration technologies (PROTRA). (note: CHPs that treated as heat-demand driven: If they produce heat in the first allocation step, they will recieve highest priority in the second allocation for electricity).
    """
    return allocate_available(
        max_to_from_existing_stock_by_protra_hp_and_chp()
        .loc[:, "TO heat", :]
        .reset_coords(drop=True),
        protra_utilization_applied_priorities(),
        to_by_commodity().loc[:, "TO heat"].reset_coords(drop=True),
    ).expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)


@component.add(
    name="protra max full load hours after constraints",
    units="h/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_max_full_load_hours": 5,
        "variation_cf_nuclear_after_uranium_scarcity": 1,
        "protra_max_full_load_hours_curtailed": 1,
        "switch_law2nrg_hydropower_production": 2,
        "switch_climate_change_damage": 2,
        "variation_precipitation_evapotranspiration_36r": 2,
        "switch_energy": 2,
    },
)
def protra_max_full_load_hours_after_constraints():
    """
    Full load hours of plants taking into account biophysical limitations (uranium availability, RES variability, percipitation-changes impact on hydropower production etc.). For nuclear: maximum load hours from nuclear power plants given uranium extraction rate constraints; the eventual scarcity among regions is split proportionally to the nuclear capacity stock. For hydropower (dammed & run of river): maximum load hours limited by the ratio Precepitation/Evapotranspiration, as in (Calheiros et al, 2024) -> https://www.mdpi.com/2071-1050/16/4/1548
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    )
    value.loc[:, ["PROTRA PP nuclear"]] = (
        (
            protra_max_full_load_hours()
            .loc[:, "PROTRA PP nuclear"]
            .reset_coords(drop=True)
            * (1 - variation_cf_nuclear_after_uranium_scarcity())
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP nuclear"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA PP nuclear"]] = False
    except_subs.loc[:, ["PROTRA PP hydropower run of river"]] = False
    except_subs.loc[:, ["PROTRA PP hydropower dammed"]] = False
    value.values[except_subs.values] = protra_max_full_load_hours_curtailed().values[
        except_subs.values
    ]
    value.loc[:, ["PROTRA PP hydropower run of river"]] = (
        if_then_else(
            np.logical_or(
                switch_law2nrg_hydropower_production() == 0,
                np.logical_or(
                    switch_climate_change_damage() == 0, switch_energy() == 0
                ),
            ),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA PP hydropower run of river"]
            .reset_coords(drop=True),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA PP hydropower run of river"]
            .reset_coords(drop=True)
            * variation_precipitation_evapotranspiration_36r()
            .loc[_subscript_dict["REGIONS 9 I"]]
            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP hydropower run of river"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP hydropower dammed"]] = (
        if_then_else(
            np.logical_or(
                switch_law2nrg_hydropower_production() == 0,
                np.logical_or(
                    switch_climate_change_damage() == 0, switch_energy() == 0
                ),
            ),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA PP hydropower dammed"]
            .reset_coords(drop=True),
            lambda: protra_max_full_load_hours()
            .loc[:, "PROTRA PP hydropower dammed"]
            .reset_coords(drop=True)
            * variation_precipitation_evapotranspiration_36r()
            .loc[_subscript_dict["REGIONS 9 I"]]
            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP hydropower dammed"]}, 1)
        .values
    )
    return value


@component.add(
    name="protra max full load hours curtailed",
    units="h/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_variability_effects": 1,
        "protra_max_full_load_hours": 2,
        "variation_cf_curtailed_protra": 3,
    },
)
def protra_max_full_load_hours_curtailed():
    """
    Maximum full load hours taking into account curtailement due to energy variability (CEEP in EnergyPLAN).
    """
    return if_then_else(
        switch_nrg_variability_effects() == 1,
        lambda: protra_max_full_load_hours()
        * (
            1
            - if_then_else(
                variation_cf_curtailed_protra()
                .loc[:, "TO elec", :]
                .reset_coords(drop=True)
                < 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    },
                    ["REGIONS 9 I", "NRG PROTRA I"],
                ),
                lambda: if_then_else(
                    variation_cf_curtailed_protra()
                    .loc[:, "TO elec", :]
                    .reset_coords(drop=True)
                    > 1,
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                        },
                        ["REGIONS 9 I", "NRG PROTRA I"],
                    ),
                    lambda: variation_cf_curtailed_protra()
                    .loc[:, "TO elec", :]
                    .reset_coords(drop=True),
                ),
            )
        ),
        lambda: protra_max_full_load_hours(),
    )


@component.add(
    name="PROTRA other TO allocations",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "PROTRA NP I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"remaining_to_to_be_allocated": 5},
)
def protra_other_to_allocations():
    """
    allocation of blending and No-Process processes (mainly for accounting processes)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "PROTRA NP I": _subscript_dict["PROTRA NP I"],
        },
        ["REGIONS 9 I", "NRG TO I", "PROTRA NP I"],
    )
    value.loc[:, ["TO gas"], ["PROTRA blending gas fuels"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA blending gas fuels"]}, 2)
        .values
    )
    value.loc[:, ["TO liquid"], ["PROTRA blending liquid fuels"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO liquid"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA blending liquid fuels"]}, 2)
        .values
    )
    value.loc[:, ["TO hydrogen"], ["PROTRA no process TI hydrogen"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA no process TI hydrogen"]}, 2)
        .values
    )
    value.loc[:, ["TO solid bio"], ["PROTRA no process TI solid bio"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO solid bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA no process TI solid bio"]}, 2)
        .values
    )
    value.loc[:, ["TO solid fossil"], ["PROTRA no process TI solid fossil"]] = (
        remaining_to_to_be_allocated()
        .loc[:, "TO solid fossil"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA no process TI solid fossil"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO solid fossil"], ["PROTRA no process TI solid fossil"]] = (
        False
    )
    except_subs.loc[:, ["TO solid bio"], ["PROTRA no process TI solid bio"]] = False
    except_subs.loc[:, ["TO hydrogen"], ["PROTRA no process TI hydrogen"]] = False
    except_subs.loc[:, ["TO gas"], ["PROTRA blending gas fuels"]] = False
    except_subs.loc[:, ["TO liquid"], ["PROTRA blending liquid fuels"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA TO allocated",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "chp_production": 2,
        "protra_heat_allocation": 1,
        "protra_elec_allocation": 1,
        "protra_other_to_allocations": 1,
    },
)
def protra_to_allocated():
    """
    TO allocated to PROTRA technologies. Set together from stepwise-allocation approach (first heat, than elec)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP I"]] = (
        chp_production()
        .loc[:, "TO heat", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA CHP I"]] = (
        chp_production()
        .loc[:, "TO elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA HP I"]] = (
        protra_heat_allocation()
        .loc[:, "TO heat", _subscript_dict["PROTRA HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA HP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = (
        protra_elec_allocation()
        .loc[:, "TO elec", _subscript_dict["PROTRA PP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA PP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, :, _subscript_dict["PROTRA NP I"]] = (
        protra_other_to_allocations().values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA CHP I"]] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA CHP I"]] = False
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA HP I"]] = True
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA HP I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA PP I"]] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA TO allocated in TWh",
    units="TW*h/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 2,
        "unit_conversion_j_ej": 2,
        "unit_conversion_w_tw": 2,
        "unit_conversion_j_wh": 2,
    },
)
def protra_to_allocated_in_twh():
    """
    Output of heat and electricity from PROTRA in TWh
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    )
    value.loc[:, ["TO elec"], :] = (
        (
            protra_to_allocated().loc[:, "TO elec", :].reset_coords(drop=True)
            * unit_conversion_j_ej()
            / unit_conversion_w_tw()
            / unit_conversion_j_wh()
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"], :] = (
        (
            protra_to_allocated().loc[:, "TO heat", :].reset_coords(drop=True)
            * unit_conversion_j_ej()
            / unit_conversion_w_tw()
            / unit_conversion_j_wh()
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA utilization applied priorities",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PRO I", "pprofile"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "pwidth_protra_utilization_allocation_policy_priorities_sp": 1,
        "protra_utilization_priorities_policyweight_sp": 2,
        "protra_utilization_allocation_priorities_sp": 1,
        "protra_utilization_priorities_endogenous": 1,
    },
)
def protra_utilization_applied_priorities():
    """
    Applied allocation priorities for PROTRA energy transformation technology utilization, based on a mix of exogenous (policy) and endogeneous (OPEX, currently NOT ACTIVE) signals.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
            "pprofile": _subscript_dict["pprofile"],
        },
        ["REGIONS 9 I", "NRG PRO I", "pprofile"],
    )
    value.loc[:, :, ["ptype"]] = 3
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["NRG PROTRA I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["pwidth"]] = (
        pwidth_protra_utilization_allocation_policy_priorities_sp()
    )
    value.loc[:, :, ["pextra"]] = 0
    value.loc[:, _subscript_dict["NRG PROTRA I"], ["ppriority"]] = (
        (
            protra_utilization_allocation_priorities_sp()
            * protra_utilization_priorities_policyweight_sp()
            + protra_utilization_priorities_endogenous()
            * (1 - protra_utilization_priorities_policyweight_sp())
        )
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    return value


@component.add(
    name="PWIDTH PROTRA UTILIZATION ALLOCATION POLICY PRIORITIES SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp"
    },
)
def pwidth_protra_utilization_allocation_policy_priorities_sp():
    """
    One of the parameters of the Vensim ALLOCATE_AVAILABLE function used to specify the curves to be used for supply and demand. Note that the priorities and widths specified should all be of the same order of magnitude. For example, it does not make sense to have one priority be 20 and another 2e6 if width is 100.
    """
    return _ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp()


_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PWIDTH_PROTRA_UTILIZATION_ALLOCATION_POLICY_PRIORITIES_SP",
    {},
    _root,
    {},
    "_ext_constant_pwidth_protra_utilization_allocation_policy_priorities_sp",
)


@component.add(
    name="Remaining TO to be allocated",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 7, "chp_production": 2},
)
def remaining_to_to_be_allocated():
    """
    TO demand lesser the heat and elec produced from CHPs
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS 9 I", "NRG TO I"],
    )
    value.loc[:, ["TO elec"]] = (
        np.maximum(
            to_by_commodity().loc[:, "TO elec"].reset_coords(drop=True)
            - sum(
                chp_production()
                .loc[:, "TO elec", :]
                .reset_coords(drop=True)
                .rename({"PROTRA CHP I": "PROTRA CHP I!"}),
                dim=["PROTRA CHP I!"],
            ),
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO gas"].reset_coords(drop=True))
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        np.maximum(
            0,
            to_by_commodity().loc[:, "TO heat"].reset_coords(drop=True)
            - sum(
                chp_production()
                .loc[:, "TO heat", :]
                .reset_coords(drop=True)
                .rename({"PROTRA CHP I": "PROTRA CHP I!"}),
                dim=["PROTRA CHP I!"],
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO hydrogen"].reset_coords(drop=True))
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO liquid"].reset_coords(drop=True))
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = (
        np.maximum(0, to_by_commodity().loc[:, "TO solid bio"].reset_coords(drop=True))
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"]] = (
        np.maximum(
            0, to_by_commodity().loc[:, "TO solid fossil"].reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="SWITCH LAW2NRG HYDROPOWER PRODUCTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law2nrg_hydropower_production"},
)
def switch_law2nrg_hydropower_production():
    """
    =1: Climate Change Impact on Hydropower production activated =0: no change
    """
    return _ext_constant_switch_law2nrg_hydropower_production()


_ext_constant_switch_law2nrg_hydropower_production = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2NRG_HYDROPOWER_PRODUCTION",
    {},
    _root,
    {},
    "_ext_constant_switch_law2nrg_hydropower_production",
)


@component.add(
    name="SWITCH NRG VARIABILITY EFFECTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_variability_effects"},
)
def switch_nrg_variability_effects():
    """
    This switch can take two values: 0: the energy module does not see the effects variability in the generation of energy (RES would appear as fully dispatachable). 1: the energy module sees the effects of variability in utilization, capacity expansion, etc.
    """
    return _ext_constant_switch_nrg_variability_effects()


_ext_constant_switch_nrg_variability_effects = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_VARIABILITY_EFFECTS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_variability_effects",
)


@component.add(
    name="TO deficit",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "aggregated_to_production_by_commodity": 1},
)
def to_deficit():
    """
    Variable to detect if there is transformation output (FE) scarcity by region and TO type.
    """
    return to_by_commodity() - aggregated_to_production_by_commodity()


@component.add(
    name="TO deficit relative",
    units="1",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "aggregated_to_production_by_commodity": 1},
)
def to_deficit_relative():
    """
    Variable to detect if there is transformation output (FE) scarcity by region and TO type.
    """
    return -1 + zidz(to_by_commodity(), aggregated_to_production_by_commodity())


@component.add(
    name="variation CF nuclear after uranium scarcity",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_cf_nuclear_after_uranium_scarcity": 1},
)
def variation_cf_nuclear_after_uranium_scarcity():
    """
    Variation of the capacity factor (CF) of nuclear power plants as induced by uranium scarcity. If variation = 0 the CF corresponds to the maximum full load hours, if variation = 1 then the plant is running 0 hours/year.
    """
    return 1 - delayed_ts_cf_nuclear_after_uranium_scarcity()
