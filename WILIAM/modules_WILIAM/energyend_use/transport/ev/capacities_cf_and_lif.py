"""
Module energyend_use.transport.ev.capacities_cf_and_lif
Translated using PySD version 3.14.0
"""

@component.add(
    name="average power electrified vehicle used",
    units="w/batteries",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_electrified_vehicles_battery_lifetime": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_hours_year": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def average_power_electrified_vehicle_used():
    """
    Average power delivered by the electrified vehicles battery over its lifetime
    """
    return (
        energy_delivered_by_electrified_vehicles_battery_lifetime()
        * unit_conversion_j_mj()
        / unit_conversion_j_wh()
        / (max_lifetime_ev_batteries() * unit_conversion_hours_year())
    )


@component.add(
    name="average power EV vehicle used for transport",
    units="w/batteries",
    subscripts=["EV BATTERIES I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_ev_battery_for_transport": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_hours_year": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def average_power_ev_vehicle_used_for_transport():
    """
    Average power delivered by the electric household vehicle battery over its lifetime only for transport
    """
    return (
        energy_delivered_by_ev_battery_for_transport()
        * unit_conversion_j_mj()
        / unit_conversion_j_wh()
        / (max_lifetime_ev_batteries() * unit_conversion_hours_year())
    ).transpose("EV BATTERIES I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I")


@component.add(
    name="CAPACITY EV",
    units="kW*h/(cycle*vehicle)",
    subscripts=["TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_capacity_ev"},
)
def capacity_ev():
    """
    Capacity storage of EV batteries by vehicle.
    """
    return _ext_constant_capacity_ev()


_ext_constant_capacity_ev = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "electric_battery_transport",
    "VEHICLE_ELECTRIC_CAPACITY",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
    },
    "_ext_constant_capacity_ev",
)


@component.add(
    name="CF electrified vehicle",
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
        "average_power_electrified_vehicle_used": 1,
        "unit_conversion_w_kw": 1,
        "vehicle_electric_power": 1,
    },
)
def cf_electrified_vehicle():
    """
    capacity factor of a electrified vehicle battery
    """
    return zidz(
        zidz(average_power_electrified_vehicle_used(), unit_conversion_w_kw()),
        vehicle_electric_power()
        .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)
        .expand_dims({"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]}, 1),
    )


@component.add(
    name="CF EV vehicle for transport",
    units="DMNL",
    subscripts=["EV BATTERIES I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "average_power_ev_vehicle_used_for_transport": 1,
        "unit_conversion_w_kw": 1,
        "vehicle_electric_power": 1,
    },
)
def cf_ev_vehicle_for_transport():
    """
    capacity factor of a electric household vehicle battery only for transport
    """
    return zidz(
        zidz(average_power_ev_vehicle_used_for_transport(), unit_conversion_w_kw()),
        vehicle_electric_power().expand_dims(
            {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]}, 0
        ),
    )


@component.add(
    name="discarded transport electrified vehicle batteries capacity",
    units="TW*h/(Year*cycle)",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_capacity": 1,
        "lifetime_electrified_vehicle_batteries": 1,
    },
)
def discarded_transport_electrified_vehicle_batteries_capacity():
    """
    Electrical capacity discarded from the transport system by electrified vehicles by battery type
    """
    return np.maximum(
        0,
        zidz(
            transport_electrified_vehicle_batteries_capacity(),
            lifetime_electrified_vehicle_batteries(),
        ),
    )


@component.add(
    name="discarded transport electrified vehicle batteries power",
    units="TW/Year",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_electrified_vehicle_batteries_power": 1,
        "lifetime_electrified_vehicle_batteries": 1,
    },
)
def discarded_transport_electrified_vehicle_batteries_power():
    """
    Electrical power discarded from the transport system by electrified vehicles by battery type
    """
    return np.maximum(
        0,
        zidz(
            transport_electrified_vehicle_batteries_power(),
            lifetime_electrified_vehicle_batteries(),
        ),
    )


@component.add(
    name="electrified vehicles power by battery type",
    units="TW",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_power": 1},
)
def electrified_vehicles_power_by_battery_type():
    """
    Total electrified vehicles (Ebike + EV + Hyb vehicle) power per type of battery.
    """
    return sum(
        transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="energy delivered by electrified vehicles battery lifetime",
    units="MJ/batteries",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cycles_electrified_vehicles_for_mobility": 1,
        "cycles_for_elec_storage_and_supply_the_grid_of_ev_battery": 1,
        "battery_wear_factor": 1,
        "capacity_ev": 1,
        "batteries_per_ev_vehicle": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_mj": 1,
    },
)
def energy_delivered_by_electrified_vehicles_battery_lifetime():
    """
    Energy delivered by the electrified vehicles battery over its lifetime
    """
    return (
        (
            cycles_electrified_vehicles_for_mobility()
            + cycles_for_elec_storage_and_supply_the_grid_of_ev_battery().transpose(
                "TRANSPORT POWER TRAIN I",
                "BATTERY VEHICLES I",
                "REGIONS 35 I",
                "EV BATTERIES I",
            )
        )
        / (1 + battery_wear_factor())
        * capacity_ev()
        / batteries_per_ev_vehicle()
        * unit_converison_wh_kwh()
        * unit_conversion_j_wh()
        / unit_conversion_j_mj()
    ).transpose(
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    )


@component.add(
    name="energy delivered by EV battery for transport",
    units="MJ/batteries",
    subscripts=["TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cycles_electrified_vehicles_for_mobility": 1,
        "battery_wear_factor": 1,
        "capacity_ev": 1,
        "batteries_per_ev_vehicle": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_j_wh": 1,
        "unit_conversion_j_mj": 1,
    },
)
def energy_delivered_by_ev_battery_for_transport():
    """
    Energy delivered by the electric household vehicle battery over its lifetime only for transport
    """
    return (
        cycles_electrified_vehicles_for_mobility()
        / (1 + battery_wear_factor())
        * capacity_ev()
        / batteries_per_ev_vehicle()
        * unit_converison_wh_kwh()
        * unit_conversion_j_wh()
        / unit_conversion_j_mj()
    )


@component.add(
    name="EV batteries capacity required",
    units="TW*h/cycle",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_ev_vehicles": 1,
        "capacity_ev": 1,
        "unit_conversion_kwh_twh": 1,
    },
)
def ev_batteries_capacity_required():
    """
    Total battery capacity required for the Electric vehicles over the years
    """
    return (
        sum(
            total_number_ev_vehicles().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            )
            * capacity_ev().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        / unit_conversion_kwh_twh()
    )


@component.add(
    name="EV batteries power",
    units="TW",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_power": 1},
)
def ev_batteries_power():
    """
    Electric batteries from electric vehicles, expresed in terms of power available (TW)
    """
    return sum(
        transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="EV batteries power SC",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "smart_charging_share_ev_vehicles": 1},
)
def ev_batteries_power_sc():
    """
    EV batteries power for Smart Charging (ebike are assumed not to be available due to their small battery size).
    """
    return (
        sum(
            ev_batteries_power().rename({"EV BATTERIES I": "EV BATTERIES I!"}),
            dim=["EV BATTERIES I!"],
        )
        * smart_charging_share_ev_vehicles()
    )


@component.add(
    name="EV batteries power V2G",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "v2g_share_ev_vehicles": 1},
)
def ev_batteries_power_v2g():
    """
    EV batteries power for V2G (ebike are assumed not to be available due to their small battery size).
    """
    return (
        sum(
            ev_batteries_power().rename({"EV BATTERIES I": "EV BATTERIES I!"}),
            dim=["EV BATTERIES I!"],
        )
        * v2g_share_ev_vehicles()
    )


@component.add(
    name="EV batteries power V2G 9R",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power_v2g": 2},
)
def ev_batteries_power_v2g_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[["EU27"]] = sum(
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS EU27 I"]]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        ev_batteries_power_v2g()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    return value


@component.add(
    name="EV vehicles batteries power required",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_ev_vehicles": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
    },
)
def ev_vehicles_batteries_power_required():
    """
    Total battery power required for the Electric vehicles over the years
    """
    return (
        sum(
            total_number_ev_vehicles().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            )
            * vehicle_electric_power().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        * unit_conversion_tw_kw()
        * batteries_per_ev_vehicle()
    )


@component.add(
    name="HEV batteries capacity required",
    units="TW*h/cycle",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_electrified_vehicles": 1,
        "capacity_ev": 1,
        "unit_conversion_kwh_twh": 1,
    },
)
def hev_batteries_capacity_required():
    """
    Total battery capacity required for the hybrid vehicles over the years
    """
    return (
        sum(
            total_number_electrified_vehicles()
            .loc[:, :, _subscript_dict["BATTERY VEHICLES I"]]
            .rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "TRANSPORT MODE I": "BATTERY VEHICLES I!",
                }
            )
            * capacity_ev().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        / unit_conversion_kwh_twh()
    )


@component.add(
    name="HEV vehicles batteries power required",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_electrified_vehicles": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
    },
)
def hev_vehicles_batteries_power_required():
    """
    Total battery power required for the power vehicles over the years
    """
    return (
        sum(
            total_number_electrified_vehicles()
            .loc[:, :, _subscript_dict["BATTERY VEHICLES I"]]
            .rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "TRANSPORT MODE I": "BATTERY VEHICLES I!",
                }
            )
            * vehicle_electric_power().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
        )
        * unit_conversion_tw_kw()
        * batteries_per_ev_vehicle()
    )


@component.add(
    name="lifetime electrified vehicle batteries",
    units="Year",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_delivered_by_electrified_vehicles_battery_lifetime": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_wh": 1,
        "unit_converison_wh_kwh": 1,
        "unit_conversion_hours_year": 1,
        "cf_electrified_vehicle": 1,
        "vehicle_electric_power": 1,
        "max_lifetime_ev_batteries": 1,
    },
)
def lifetime_electrified_vehicle_batteries():
    """
    Lifetime of electrified vehicle batteries. Minimum value between the lifetime of a battery given by its self-degradation (MAX_LIFETIME_EV_BATTERIES), and the maximum number of cycles due to its total use (both for mobility and as V2G option).
    """
    return np.minimum(
        zidz(
            zidz(
                zidz(
                    zidz(
                        energy_delivered_by_electrified_vehicles_battery_lifetime()
                        * unit_conversion_j_mj(),
                        unit_conversion_j_wh(),
                    ),
                    unit_converison_wh_kwh(),
                ),
                unit_conversion_hours_year(),
            ),
            cf_electrified_vehicle() * vehicle_electric_power(),
        ),
        max_lifetime_ev_batteries(),
    )


@component.add(
    name="new transport electried vehicle batteries capacity",
    units="TW*h/(Year*cycle)",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capacity_ev": 1,
        "total_number_electrified_vehicles": 1,
        "unit_conversion_kwh_twh": 1,
        "one_year": 2,
        "transport_electrified_vehicle_batteries_capacity": 1,
        "discarded_transport_electrified_vehicle_batteries_capacity": 1,
        "share_of_new_ev_subtechn_batteries": 1,
    },
)
def new_transport_electried_vehicle_batteries_capacity():
    """
    Electric capacity fed into the transport system by hybrid commercial vehicles by battery type
    """
    return (
        (
            np.maximum(
                0,
                capacity_ev()
                * total_number_electrified_vehicles()
                .loc[:, :, _subscript_dict["BATTERY VEHICLES I"]]
                .rename({"TRANSPORT MODE I": "BATTERY VEHICLES I"})
                .transpose(
                    "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I"
                )
                / unit_conversion_kwh_twh()
                / one_year()
                - (
                    sum(
                        transport_electrified_vehicle_batteries_capacity().rename(
                            {"EV BATTERIES I": "EV BATTERIES I!"}
                        ),
                        dim=["EV BATTERIES I!"],
                    )
                    / one_year()
                ).transpose(
                    "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I"
                ),
            )
            + sum(
                discarded_transport_electrified_vehicle_batteries_capacity().rename(
                    {"EV BATTERIES I": "EV BATTERIES I!"}
                ),
                dim=["EV BATTERIES I!"],
            ).transpose("TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I")
        )
        * share_of_new_ev_subtechn_batteries().transpose(
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
            "REGIONS 35 I",
            "EV BATTERIES I",
        )
    ).transpose(
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    )


@component.add(
    name="new transport electrified vehicle batteries power",
    units="TW/Year",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "vehicle_electric_power": 1,
        "total_number_electrified_vehicles": 1,
        "one_year": 2,
        "unit_conversion_tw_kw": 1,
        "batteries_per_ev_vehicle": 1,
        "transport_electrified_vehicle_batteries_power": 1,
        "discarded_transport_electrified_vehicle_batteries_power": 1,
        "share_of_new_ev_subtechn_batteries": 1,
    },
)
def new_transport_electrified_vehicle_batteries_power():
    """
    Electric power fed into the transport system by electrified vehicles by battery type
    """
    return (
        (
            np.maximum(
                0,
                vehicle_electric_power()
                * total_number_electrified_vehicles()
                .loc[:, :, _subscript_dict["BATTERY VEHICLES I"]]
                .rename({"TRANSPORT MODE I": "BATTERY VEHICLES I"})
                .transpose(
                    "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I"
                )
                / one_year()
                * unit_conversion_tw_kw()
                * batteries_per_ev_vehicle()
                - (
                    sum(
                        transport_electrified_vehicle_batteries_power().rename(
                            {"EV BATTERIES I": "EV BATTERIES I!"}
                        ),
                        dim=["EV BATTERIES I!"],
                    )
                    / one_year()
                ).transpose(
                    "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I"
                ),
            )
            + sum(
                discarded_transport_electrified_vehicle_batteries_power().rename(
                    {"EV BATTERIES I": "EV BATTERIES I!"}
                ),
                dim=["EV BATTERIES I!"],
            ).transpose("TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "REGIONS 35 I")
        )
        * share_of_new_ev_subtechn_batteries().transpose(
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
            "REGIONS 35 I",
            "EV BATTERIES I",
        )
    ).transpose(
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    )


@component.add(
    name="power discarded batteries 9R",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"power_discarded_vehicle_batteries": 2},
)
def power_discarded_batteries_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "EV BATTERIES I": _subscript_dict["EV BATTERIES I"],
        },
        ["REGIONS 9 I", "EV BATTERIES I"],
    )
    value.loc[["EU27"], :] = (
        sum(
            power_discarded_vehicle_batteries()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        power_discarded_vehicle_batteries()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    return value


@component.add(
    name="power discarded vehicle batteries",
    units="TW/Year",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"discarded_transport_electrified_vehicle_batteries_power": 1},
)
def power_discarded_vehicle_batteries():
    """
    Capacity of discarded electric batteries.
    """
    return sum(
        discarded_transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="power new vehicle batteries 35R",
    units="TW/Year",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_transport_electrified_vehicle_batteries_power": 1},
)
def power_new_vehicle_batteries_35r():
    """
    Capacity of new and replaced electric batteries.
    """
    return sum(
        new_transport_electrified_vehicle_batteries_power().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="share of EV batteries",
    units="DMNL",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ev_vehicles_batteries_capacity": 2},
)
def share_of_ev_batteries():
    """
    Share of EV batteries in the EV vehicles.
    """
    return zidz(
        total_ev_vehicles_batteries_capacity(),
        sum(
            total_ev_vehicles_batteries_capacity().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        ).expand_dims({"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]}, 1),
    )


@component.add(
    name="total electrified vehicles batteries power required",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ev_vehicles_batteries_power_required": 1,
        "hev_vehicles_batteries_power_required": 1,
    },
)
def total_electrified_vehicles_batteries_power_required():
    """
    Total power required for electrified vehicles (EV + hybrid).
    """
    return (
        ev_vehicles_batteries_power_required() + hev_vehicles_batteries_power_required()
    )


@component.add(
    name="total EV vehicles batteries capacity",
    units="TW*h/cycle",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"transport_electrified_vehicle_batteries_capacity": 1},
)
def total_ev_vehicles_batteries_capacity():
    """
    Total capacity of EV batteries in the BEV vehicles.
    """
    return sum(
        transport_electrified_vehicle_batteries_capacity().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
    )


@component.add(
    name="transport electrified vehicle batteries capacity",
    units="TW*h/cycle",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_transport_electrified_vehicle_batteries_capacity": 1},
    other_deps={
        "_integ_transport_electrified_vehicle_batteries_capacity": {
            "initial": {},
            "step": {
                "new_transport_electried_vehicle_batteries_capacity": 1,
                "discarded_transport_electrified_vehicle_batteries_capacity": 1,
            },
        }
    },
)
def transport_electrified_vehicle_batteries_capacity():
    """
    Electric capacity in the transport system by electrified vehicles by battery type
    """
    return _integ_transport_electrified_vehicle_batteries_capacity()


_integ_transport_electrified_vehicle_batteries_capacity = Integ(
    lambda: new_transport_electried_vehicle_batteries_capacity()
    - discarded_transport_electrified_vehicle_batteries_capacity(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "EV BATTERIES I": _subscript_dict["EV BATTERIES I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
        },
        [
            "REGIONS 35 I",
            "EV BATTERIES I",
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
        ],
    ),
    "_integ_transport_electrified_vehicle_batteries_capacity",
)


@component.add(
    name="transport electrified vehicle batteries power",
    units="TW",
    subscripts=[
        "REGIONS 35 I",
        "EV BATTERIES I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_transport_electrified_vehicle_batteries_power": 1},
    other_deps={
        "_integ_transport_electrified_vehicle_batteries_power": {
            "initial": {},
            "step": {
                "new_transport_electrified_vehicle_batteries_power": 1,
                "discarded_transport_electrified_vehicle_batteries_power": 1,
            },
        }
    },
)
def transport_electrified_vehicle_batteries_power():
    """
    Electric power in the transport system by electrified vehicles by battery type
    """
    return _integ_transport_electrified_vehicle_batteries_power()


_integ_transport_electrified_vehicle_batteries_power = Integ(
    lambda: new_transport_electrified_vehicle_batteries_power()
    - discarded_transport_electrified_vehicle_batteries_power(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "EV BATTERIES I": _subscript_dict["EV BATTERIES I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
        },
        [
            "REGIONS 35 I",
            "EV BATTERIES I",
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
        ],
    ),
    "_integ_transport_electrified_vehicle_batteries_power",
)
