"""
Module energyvariability.storage.electricity
Translated using PySD version 3.14.0
"""

@component.add(
    name="ANNUAL VARIATION CAPACITY EXPANSION PROSTO DEDICATED SP",
    units="1/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp"
    },
)
def annual_variation_capacity_expansion_prosto_dedicated_sp():
    return _ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp()


_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    "_ext_constant_annual_variation_capacity_expansion_prosto_dedicated_sp",
)


@component.add(
    name="capacity charge vehicles with SC",
    units="TW*h/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "unit_conversion_hours_year": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def capacity_charge_vehicles_with_sc():
    """
    Energy to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
    ) * smart_charging_share_ev_vehicles()


@component.add(
    name="capacity charge vehicles without SC",
    units="TW*h/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "unit_conversion_hours_year": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def capacity_charge_vehicles_without_sc():
    """
    Energy to recharge normal vehicles
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I")
            * unit_conversion_hours_year(),
            dim=["EV BATTERIES I!"],
        )
    ) * (1 - smart_charging_share_ev_vehicles())


@component.add(
    name="CF max EV vehicle battery for elec storage",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cycles_max_for_elec_storage_ev_vehicles": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
        "cf_ev_vehicle_for_transport": 1,
        "v2g_share_ev_vehicles": 1,
    },
)
def cf_max_ev_vehicle_battery_for_elec_storage():
    """
    CF max of EV Household vehicle battery for electricity storage
    """
    return (
        zidz(
            cycles_max_for_elec_storage_ev_vehicles(),
            cycles_electrified_vehicles_for_mobility(),
        )
        * cf_ev_vehicle_for_transport().transpose(
            "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "EV BATTERIES I"
        )
        * v2g_share_ev_vehicles()
    ).transpose(
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    )


@component.add(
    name="CHARGING LOSSES SHARE BY PROSTO ELEC",
    units="DMNL",
    subscripts=["NRG PROSTO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "charging_losses_share_by_prosto_elec_dedicated": 1,
        "ev_charge_losses_share": 1,
    },
)
def charging_losses_share_by_prosto_elec():
    """
    Charging losses by storage utility-scale facility.
    """
    value = xr.DataArray(
        np.nan, {"NRG PROSTO I": _subscript_dict["NRG PROSTO I"]}, ["NRG PROSTO I"]
    )
    value.loc[_subscript_dict["PROSTO ELEC DEDICATED I"]] = (
        charging_losses_share_by_prosto_elec_dedicated().values
    )
    value.loc[["PROSTO V2G"]] = ev_charge_losses_share()
    return value


@component.add(
    name="CHARGING LOSSES SHARE BY PROSTO ELEC DEDICATED",
    units="DMNL",
    subscripts=["PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_charging_losses_share_by_prosto_elec_dedicated"
    },
)
def charging_losses_share_by_prosto_elec_dedicated():
    """
    Relative charging losses by storage utility-scale facility.
    """
    return _ext_constant_charging_losses_share_by_prosto_elec_dedicated()


_ext_constant_charging_losses_share_by_prosto_elec_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "CHARGING_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED*",
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    _root,
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    "_ext_constant_charging_losses_share_by_prosto_elec_dedicated",
)


@component.add(
    name="cycles electrified vehicles for mobility",
    units="cycle",
    subscripts=["TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mileage_vehicles": 2,
        "autonomy_ev_vehicles": 2,
        "battery_wear_factor": 1,
    },
)
def cycles_electrified_vehicles_for_mobility():
    return zidz(
        mileage_vehicles()
        .loc[:, _subscript_dict["BATTERY VEHICLES I"]]
        .rename({"TRANSPORT MODE I": "BATTERY VEHICLES I"}),
        autonomy_ev_vehicles(),
    ) + battery_wear_factor() * zidz(
        mileage_vehicles()
        .loc[:, _subscript_dict["BATTERY VEHICLES I"]]
        .rename({"TRANSPORT MODE I": "BATTERY VEHICLES I"}),
        autonomy_ev_vehicles(),
    )


@component.add(
    name="cycles for elec storage and supply the grid of EV battery",
    units="cycles",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_v2g_storage": 1,
        "cf_ev_vehicle_for_transport": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
    },
)
def cycles_for_elec_storage_and_supply_the_grid_of_ev_battery():
    """
    cycles used for storage and feed electrical energy for the system
    """
    return (
        zidz(
            cf_v2g_storage()
            .expand_dims({"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]}, 1)
            .expand_dims(
                {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]},
                2,
            )
            .expand_dims(
                {"BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"]}, 3
            ),
            cf_ev_vehicle_for_transport().expand_dims(
                {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0
            ),
        )
        * cycles_electrified_vehicles_for_mobility()
    )


@component.add(
    name="cycles max for elec storage EV vehicles",
    units="cycles",
    subscripts=["TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_cycles_batteries_ev": 1,
        "cycles_electrified_vehicles_for_mobility": 1,
    },
)
def cycles_max_for_elec_storage_ev_vehicles():
    """
    cycles max of EV Household vehicle battery for electricity storage
    """
    return np.maximum(
        0, max_cycles_batteries_ev() - cycles_electrified_vehicles_for_mobility()
    )


@component.add(
    name="DISCHARGE LOSSES SHARE BY PROSTO ELEC DEDICATED",
    units="DMNL",
    subscripts=["PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_discharge_losses_share_by_prosto_elec_dedicated"
    },
)
def discharge_losses_share_by_prosto_elec_dedicated():
    """
    Relative discharging losses by storage utility-scale facility.
    """
    return _ext_constant_discharge_losses_share_by_prosto_elec_dedicated()


_ext_constant_discharge_losses_share_by_prosto_elec_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "DISCHARGE_LOSSES_SHARE_BY_PROSTO_ELEC_DEDICATED*",
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    _root,
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    "_ext_constant_discharge_losses_share_by_prosto_elec_dedicated",
)


@component.add(
    name="DISCHARGING LOSSES SHARE BY PROSTO ELEC",
    units="DMNL",
    subscripts=["NRG PROSTO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "discharge_losses_share_by_prosto_elec_dedicated": 1,
        "ev_discharge_losses_share": 1,
    },
)
def discharging_losses_share_by_prosto_elec():
    """
    Discharging losses by storage utility-scale facility.
    """
    value = xr.DataArray(
        np.nan, {"NRG PROSTO I": _subscript_dict["NRG PROSTO I"]}, ["NRG PROSTO I"]
    )
    value.loc[_subscript_dict["PROSTO ELEC DEDICATED I"]] = (
        discharge_losses_share_by_prosto_elec_dedicated().values
    )
    value.loc[["PROSTO V2G"]] = ev_discharge_losses_share()
    return value


@component.add(
    name="elec transmission losses by PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_input_by_prosto": 1,
        "prosup_transmission_loss_shares": 1,
    },
)
def elec_transmission_losses_by_prosto():
    """
    Roundtrip storage losses and additional transmission losses by PROcess STOrage.
    """
    return stored_energy_input_by_prosto() * prosup_transmission_loss_shares().loc[
        :, "PROSUP transmission losses elec"
    ].reset_coords(drop=True)


@component.add(
    name="HISTORIC ANNUAL GROWTH CAPACITY EXPANSION PROSTO DEDICATED",
    units="1/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated"
    },
)
def historic_annual_growth_capacity_expansion_prosto_dedicated():
    """
    Historic annual growth capacity expansion of dedicated facilities to store energy at utility-scale level.
    """
    return _ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated()


_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "RELATIVE_HISTORIC_GROWTH_CAPACITY_EXPANSION_PROSTO_DEDICATED",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    "_ext_constant_historic_annual_growth_capacity_expansion_prosto_dedicated",
)


@component.add(
    name="HISTORIC CAPACITY EXPANSION STATIONARY BATERIES",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG PRO I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_historic_capacity_expansion_stationary_bateries",
        "__lookup__": "_ext_lookup_historic_capacity_expansion_stationary_bateries",
    },
)
def historic_capacity_expansion_stationary_bateries(x, final_subs=None):
    """
    Historic evolution of new capacity additions of stationary batteries per region.
    """
    return _ext_lookup_historic_capacity_expansion_stationary_bateries(x, final_subs)


_ext_lookup_historic_capacity_expansion_stationary_bateries = ExtLookup(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "Time_stationary_batteries",
    "HIST_CAPACITY_STATIONATY_BATTERIES_ADDITION",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PRO I": ["PROSTO STATIONARY BATTERIES"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PRO I": _subscript_dict["NRG PRO I"],
    },
    "_ext_lookup_historic_capacity_expansion_stationary_bateries",
)


@component.add(
    name="INITIAL PROSTO DEDICATED CAPACITY STOCK",
    units="MW",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_prosto_dedicated_capacity_stock"
    },
)
def initial_prosto_dedicated_capacity_stock():
    """
    Capacity stock of dedicated facilities to store energy at utility-scale level in the initial year of the simulation.
    """
    return _ext_constant_initial_prosto_dedicated_capacity_stock()


_ext_constant_initial_prosto_dedicated_capacity_stock = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "INITIAL_PROSTO_CAPACITY_STOCK",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
    },
    "_ext_constant_initial_prosto_dedicated_capacity_stock",
)


@component.add(
    name="INITIAL YEAR ANNUAL VARIATION CAPACITY EXPANSION PROSTO DEDICATED SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp"
    },
)
def initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp():
    return (
        _ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp()
    )


_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_ANNUAL_VARIATION_CAPACITY_EXPANSION_PROSTO_DEDICATED_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp",
)


@component.add(
    name="limited capacity expansion PROSTO dedicated",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp": 1,
        "historic_annual_growth_capacity_expansion_prosto_dedicated": 1,
        "annual_variation_capacity_expansion_prosto_dedicated_sp": 1,
        "remaining_potential_capacity_by_prosto": 1,
        "prosto_dedicated_capacity_stock": 1,
    },
)
def limited_capacity_expansion_prosto_dedicated():
    """
    Capacity expansion of dedicated storage utility-scale facilities taking into account scenario and techno-sustainable limits.
    """
    return (
        if_then_else(
            (
                time()
                < initial_year_annual_variation_capacity_expansion_prosto_dedicated_sp()
            ).expand_dims(
                {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
                1,
            ),
            lambda: historic_annual_growth_capacity_expansion_prosto_dedicated(),
            lambda: annual_variation_capacity_expansion_prosto_dedicated_sp(),
        )
        * remaining_potential_capacity_by_prosto()
        * prosto_dedicated_capacity_stock()
    )


@component.add(
    name="MAX capacity for elec storage of the EV batteries in one day",
    units="TW*h/cycle",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_capacity": 1,
        "v2g_share_ev_vehicles": 1,
    },
)
def max_capacity_for_elec_storage_of_the_ev_batteries_in_one_day():
    """
    max capacity in a day given by EV batteries for electricity storage
    """
    return (
        sum(
            transport_electrified_vehicle_batteries_capacity().rename(
                {
                    "EV BATTERIES I": "EV BATTERIES I!",
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["EV BATTERIES I!", "TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        * v2g_share_ev_vehicles()
    )


@component.add(
    name="MAX capacity for elec storage of the EV vehicles",
    units="TW*h/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_max_ev_vehicle_battery_for_elec_storage": 1,
        "transport_electrified_vehicle_batteries_power": 1,
        "unit_conversion_hours_year": 1,
    },
)
def max_capacity_for_elec_storage_of_the_ev_vehicles():
    """
    max capacity in a year given by EV batteries for electricity storage
    """
    return (
        sum(
            cf_max_ev_vehicle_battery_for_elec_storage().rename(
                {
                    "EV BATTERIES I": "EV BATTERIES I!",
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            )
            * transport_electrified_vehicle_batteries_power().rename(
                {
                    "EV BATTERIES I": "EV BATTERIES I!",
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["EV BATTERIES I!", "TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        * unit_conversion_hours_year()
    )


@component.add(
    name="MAX CYCLES BATTERIES EV",
    units="cycle",
    subscripts=["TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_cycles_batteries_ev"},
)
def max_cycles_batteries_ev():
    """
    Max cycles for a EV Battery
    """
    return _ext_constant_max_cycles_batteries_ev()


_ext_constant_max_cycles_batteries_ev = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "electric_battery_transport",
    "MAX_CYCLES_EV_VEHICLES",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
    },
    "_ext_constant_max_cycles_batteries_ev",
)


@component.add(
    name="MAX power for elec storage of the EV vehicles",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_max_ev_vehicle_battery_for_elec_storage": 1,
        "transport_electrified_vehicle_batteries_power": 1,
    },
)
def max_power_for_elec_storage_of_the_ev_vehicles():
    """
    max power given by EV batteries for electricity storage
    """
    return sum(
        cf_max_ev_vehicle_battery_for_elec_storage().rename(
            {
                "EV BATTERIES I": "EV BATTERIES I!",
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        )
        * transport_electrified_vehicle_batteries_power().rename(
            {
                "EV BATTERIES I": "EV BATTERIES I!",
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["EV BATTERIES I!", "TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="maximum PROSTO dedicated",
    units="TW",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_limited_res_potentials": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "unlimited_protra_res_parameter": 1,
        "phs_potential_sp": 1,
        "stationary_batteries_maximum_sp": 1,
    },
)
def maximum_prosto_dedicated():
    """
    Maximum annual capacity for stationary storage as defined in the scenario.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
        },
        ["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    )
    value.loc[:, ["PROSTO PHS"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 0,
            lambda: xr.DataArray(
                unlimited_protra_res_parameter() / unit_conversion_tw_per_ej_per_year(),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            lambda: phs_potential_sp(),
        )
        .expand_dims({"NRG PRO I": ["PROSTO PHS"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO STATIONARY BATTERIES"]] = (
        stationary_batteries_maximum_sp()
        .expand_dims({"NRG PRO I": ["PROSTO STATIONARY BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="PHS POTENTIAL SP",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_phs_potential_sp"},
)
def phs_potential_sp():
    """
    Techno-sustainable potential of PHS by region. Stylized approach based on MEDEAS method (1 * potential of hydropower to account for both open and closed loops).
    """
    return _ext_constant_phs_potential_sp()


_ext_constant_phs_potential_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PHS_POTENTIAL_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_phs_potential_sp",
)


@component.add(
    name="power charge vehicles with SC",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def power_charge_vehicles_with_sc():
    """
    Power to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
    ) * smart_charging_share_ev_vehicles()


@component.add(
    name="power charge vehicles without SC",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_ev_vehicle_for_transport": 4,
        "transport_electrified_vehicle_batteries_power": 4,
        "smart_charging_share_ev_vehicles": 1,
    },
)
def power_charge_vehicles_without_sc():
    """
    Power to recharge smart charging vehicles in a year
    """
    return (
        sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "LDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "MDV"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            cf_ev_vehicle_for_transport()
            .loc[:, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * transport_electrified_vehicle_batteries_power()
            .loc[:, :, "BEV", "BUS"]
            .reset_coords(drop=True)
            .rename({"EV BATTERIES I": "EV BATTERIES I!"})
            .transpose("EV BATTERIES I!", "REGIONS 35 I"),
            dim=["EV BATTERIES I!"],
        )
    ) * (1 - smart_charging_share_ev_vehicles())


@component.add(
    name="PROSTO capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I", "NRG PROSTO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosto_dedicated_capacity_stock": 1, "ev_batteries_power_v2g_9r": 1},
)
def prosto_capacity_stock():
    """
    Capacity stock by PROcess STOrage.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROSTO I": _subscript_dict["NRG PROSTO I"],
        },
        ["REGIONS 9 I", "NRG PROSTO I"],
    )
    value.loc[:, _subscript_dict["PROSTO ELEC DEDICATED I"]] = (
        prosto_dedicated_capacity_stock().values
    )
    value.loc[:, ["PROSTO V2G"]] = (
        ev_batteries_power_v2g_9r().expand_dims({"NRG PRO I": ["PROSTO V2G"]}, 1).values
    )
    return value


@component.add(
    name="PROSTO dedicated capacity decomissioning",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosto_dedicated_capacity_stock": 1, "prosto_dedicated_lifetime": 1},
)
def prosto_dedicated_capacity_decomissioning():
    """
    Capacity decommmissioning due to end of lifetime of dedicated storage utility-scale facilities.
    """
    return prosto_dedicated_capacity_stock() / prosto_dedicated_lifetime()


@component.add(
    name="PROSTO dedicated capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "limited_capacity_expansion_prosto_dedicated": 3,
        "prosto_dedicated_capacity_stock": 1,
        "switch_nrg_proflex_capacity_expansion_endogenous": 2,
        "prosto_dedicated_capacity_decomissioning": 2,
        "prosup_flexopt_elec_capacity_expansion": 2,
        "historic_capacity_expansion_stationary_bateries": 1,
    },
)
def prosto_dedicated_capacity_expansion():
    """
    Capacity expansion of dedicated storage utility-scale facilities.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"],
        },
        ["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    )
    value.loc[:, ["PROSTO PHS"]] = (
        if_then_else(
            time() < 2020,
            lambda: limited_capacity_expansion_prosto_dedicated()
            .loc[:, "PROSTO PHS"]
            .reset_coords(drop=True)
            * prosto_dedicated_capacity_stock()
            .loc[:, "PROSTO PHS"]
            .reset_coords(drop=True),
            lambda: prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO PHS"]
            .reset_coords(drop=True)
            + if_then_else(
                switch_nrg_proflex_capacity_expansion_endogenous() == 0,
                lambda: limited_capacity_expansion_prosto_dedicated()
                .loc[:, "PROSTO PHS"]
                .reset_coords(drop=True),
                lambda: prosup_flexopt_elec_capacity_expansion()
                .loc[:, "PROSTO PHS"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG PRO I": ["PROSTO PHS"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO STATIONARY BATTERIES"]] = (
        if_then_else(
            time() < 2020,
            lambda: historic_capacity_expansion_stationary_bateries(time())
            .loc[:, "PROSTO STATIONARY BATTERIES"]
            .reset_coords(drop=True),
            lambda: prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO STATIONARY BATTERIES"]
            .reset_coords(drop=True)
            + if_then_else(
                switch_nrg_proflex_capacity_expansion_endogenous() == 0,
                lambda: limited_capacity_expansion_prosto_dedicated()
                .loc[:, "PROSTO STATIONARY BATTERIES"]
                .reset_coords(drop=True),
                lambda: prosup_flexopt_elec_capacity_expansion()
                .loc[:, "PROSTO STATIONARY BATTERIES"]
                .reset_coords(drop=True),
            ),
        )
        .expand_dims({"NRG PRO I": ["PROSTO STATIONARY BATTERIES"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROSTO dedicated capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_prosto_dedicated_capacity_stock": 1},
    other_deps={
        "_integ_prosto_dedicated_capacity_stock": {
            "initial": {"initial_prosto_dedicated_capacity_stock": 1},
            "step": {
                "prosto_dedicated_capacity_expansion": 1,
                "prosto_dedicated_capacity_decomissioning": 1,
            },
        }
    },
)
def prosto_dedicated_capacity_stock():
    """
    Capacity stock of dedicated facilities to store energy at utility-scale level.
    """
    return _integ_prosto_dedicated_capacity_stock()


_integ_prosto_dedicated_capacity_stock = Integ(
    lambda: prosto_dedicated_capacity_expansion()
    - prosto_dedicated_capacity_decomissioning(),
    lambda: initial_prosto_dedicated_capacity_stock(),
    "_integ_prosto_dedicated_capacity_stock",
)


@component.add(
    name="PROSTO DEDICATED LIFETIME",
    units="Year",
    subscripts=["PROSTO ELEC DEDICATED I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prosto_dedicated_lifetime"},
)
def prosto_dedicated_lifetime():
    """
    Lifetime of dedicated facilities to store energy at utility-scale level.
    """
    return _ext_constant_prosto_dedicated_lifetime()


_ext_constant_prosto_dedicated_lifetime = ExtConstant(
    "model_parameters/energy/energy-storage.xlsx",
    "Dedicated_capacities",
    "PROSTO_LIFETIME",
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    _root,
    {"PROSTO ELEC DEDICATED I": _subscript_dict["PROSTO ELEC DEDICATED I"]},
    "_ext_constant_prosto_dedicated_lifetime",
)


@component.add(
    name="remaining potential capacity by PROSTO",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_prosto_dedicated": 2, "prosto_dedicated_capacity_stock": 1},
)
def remaining_potential_capacity_by_prosto():
    """
    Remaining potential taking into account scenario and techno-sustainable limits.
    """
    return zidz(
        maximum_prosto_dedicated() - prosto_dedicated_capacity_stock(),
        maximum_prosto_dedicated(),
    )


@component.add(
    name="roundtrip and transmission losses by PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_losses_roundtrip_by_prosto": 1,
        "elec_transmission_losses_by_prosto": 1,
    },
)
def roundtrip_and_transmission_losses_by_prosto():
    """
    Roundtrip storage losses and additional transmission losses by PROcess STOrage.
    """
    return (
        stored_energy_losses_roundtrip_by_prosto()
        + elec_transmission_losses_by_prosto()
    )


@component.add(
    name="smart charging share EV vehicles",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "v2g_share_ev_vehicles": 1,
        "initial_sc_sp": 4,
        "objective_sc_sp": 2,
        "year_final_sc_sp": 2,
        "year_initial_sc_sp": 3,
        "time": 4,
        "switch_sc_sp": 1,
    },
)
def smart_charging_share_ev_vehicles():
    """
    Smart charging factor.This factor indicates the percentage of EV vehicles that can be charged when there is excess power in the grid. Priority is given to V2G since together they cannot represent > 100%.
    """
    return (
        np.minimum(
            1 - v2g_share_ev_vehicles(),
            if_then_else(
                time() < 2015,
                lambda: initial_sc_sp(),
                lambda: if_then_else(
                    time() < year_initial_sc_sp(),
                    lambda: initial_sc_sp(),
                    lambda: if_then_else(
                        time() < year_final_sc_sp(),
                        lambda: initial_sc_sp()
                        + (objective_sc_sp() - initial_sc_sp())
                        * (time() - year_initial_sc_sp())
                        / (year_final_sc_sp() - year_initial_sc_sp()),
                        lambda: objective_sc_sp(),
                    ),
                ),
            ),
        )
        * switch_sc_sp()
    )


@component.add(
    name="STATIONARY BATTERIES MAXIMUM SP",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_stationary_batteries_maximum_sp"},
)
def stationary_batteries_maximum_sp():
    """
    Scenario-defined maximum capacity of stationary batteries.
    """
    return _ext_constant_stationary_batteries_maximum_sp()


_ext_constant_stationary_batteries_maximum_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "MAXIMUM_CAPACITY_STOCK_STATIONARY_BATTERIES_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_stationary_batteries_maximum_sp",
)


@component.add(
    name="stored energy input by PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_output_by_prosto": 1,
        "stored_energy_losses_roundtrip_by_prosto": 1,
    },
)
def stored_energy_input_by_prosto():
    """
    Total energy entering the storage device.
    """
    return stored_energy_output_by_prosto() + stored_energy_losses_roundtrip_by_prosto()


@component.add(
    name="stored energy losses roundtrip by PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stored_energy_output_by_prosto": 2,
        "charging_losses_share_by_prosto_elec": 1,
        "discharging_losses_share_by_prosto_elec": 1,
    },
)
def stored_energy_losses_roundtrip_by_prosto():
    """
    Energy losses associated to storage by PROcess STOrage.
    """
    return (
        stored_energy_output_by_prosto()
        / (
            (
                1
                - charging_losses_share_by_prosto_elec().rename(
                    {"NRG PROSTO I": "PROSTO ELEC I"}
                )
            )
            * (
                1
                - discharging_losses_share_by_prosto_elec().rename(
                    {"NRG PROSTO I": "PROSTO ELEC I"}
                )
            )
        )
        - stored_energy_output_by_prosto()
    )


@component.add(
    name="stored energy output by PROSTO",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSTO ELEC I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_prosto": 1,
        "prosto_capacity_stock": 1,
        "unit_conversion_hours_year": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def stored_energy_output_by_prosto():
    """
    Total energy exiting the storage device.
    """
    return (
        cf_prosto().rename({"NRG PROSTO I": "PROSTO ELEC I"})
        * prosto_capacity_stock().rename({"NRG PROSTO I": "PROSTO ELEC I"})
        * unit_conversion_hours_year()
        * unit_conversion_tw_per_ej_per_year()
    )


@component.add(
    name="SWITCH SC SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_sc_sp"},
)
def switch_sc_sp():
    """
    1: activate scenario parameter 0: deactivate scenario parameter
    """
    return _ext_constant_switch_sc_sp()


_ext_constant_switch_sc_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_SC_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_sc_sp",
)


@component.add(
    name="SWITCH V2G SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_v2g_sp"},
)
def switch_v2g_sp():
    """
    1: activate scenario parameter 0: deactivate scenario parameter
    """
    return _ext_constant_switch_v2g_sp()


_ext_constant_switch_v2g_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_V2G_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_v2g_sp",
)


@component.add(
    name="total PROSTO losses elec",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"roundtrip_and_transmission_losses_by_prosto": 1},
)
def total_prosto_losses_elec():
    """
    Storage losses including roundtrip storage and additional transmission losses.
    """
    return sum(
        roundtrip_and_transmission_losses_by_prosto().rename(
            {"PROSTO ELEC I": "NRG PROSTO I!"}
        ),
        dim=["NRG PROSTO I!"],
    )


@component.add(
    name="V2G share EV vehicles",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_v2g_sp": 4,
        "objective_v2g_sp": 2,
        "year_initial_v2g_sp": 3,
        "year_final_v2g_sp": 2,
        "switch_v2g_sp": 1,
    },
)
def v2g_share_ev_vehicles():
    """
    Vehicle to grid factor. This factor indicates the share of EV vehicles that can transfer electrical energy from their batteries to the grid.
    """
    return xr.DataArray(
        if_then_else(
            time() < 2015,
            lambda: initial_v2g_sp(),
            lambda: if_then_else(
                time() < year_initial_v2g_sp(),
                lambda: initial_v2g_sp(),
                lambda: if_then_else(
                    time() < year_final_v2g_sp(),
                    lambda: initial_v2g_sp()
                    + (objective_v2g_sp() - initial_v2g_sp())
                    * (time() - year_initial_v2g_sp())
                    / (year_final_v2g_sp() - year_initial_v2g_sp()),
                    lambda: objective_v2g_sp(),
                ),
            ),
        )
        * switch_v2g_sp(),
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    )
