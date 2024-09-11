"""
Module energyend_use.transport_passengers
Translated using PySD version 3.14.0
"""

@component.add(
    name="base share technologies passenger transport",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_modal_share_by_power_train": 2},
)
def base_share_technologies_passenger_transport():
    """
    Base shares of eahc technology over total light duty vehicles
    """
    return zidz(
        passenger_transport_modal_share_by_power_train(),
        sum(
            passenger_transport_modal_share_by_power_train().rename(
                {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
            ),
            dim=["TRANSPORT POWER TRAIN I!"],
        ).expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 1
        ),
    )


@component.add(
    name="battery lifetime",
    units="Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"max_cycles_batteries_ev": 1, "charge_cycles_per_year": 1},
)
def battery_lifetime():
    """
    Total battery life of a battery, it depends of the total battery cycles and the cycles performed by year.
    """
    return zidz(
        max_cycles_batteries_ev()
        .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 2)
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
        charge_cycles_per_year().transpose(
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
            "REGIONS 35 I",
            "HOUSEHOLDS I",
        ),
    ).transpose(
        "REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I", "HOUSEHOLDS I"
    )


@component.add(
    name="BEV and PHEV LDV 9R sales",
    units="vehicles/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 4},
)
def bev_and_phev_ldv_9r_sales():
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[_subscript_dict["REGIONS 8 I"], "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        + sum(
            new_passenger_private_vehicles()
            .loc[_subscript_dict["REGIONS 8 I"], "PHEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
    ).values
    value.loc[["EU27"]] = sum(
        new_passenger_private_vehicles()
        .loc[_subscript_dict["REGIONS EU27 I"], "BEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[_subscript_dict["REGIONS EU27 I"], "PHEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
    )
    return value


@component.add(name="BEV switch policy", comp_type="Constant", comp_subtype="Normal")
def bev_switch_policy():
    return 0


@component.add(
    name="buses transport demand urban",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buses_transport_demand_urban_income1": 1,
        "buses_transport_demand_urban_income2": 1,
        "buses_transport_demand_urban_income3": 1,
        "buses_transport_demand_urban_income4": 1,
        "buses_transport_demand_urban_income5": 1,
    },
)
def buses_transport_demand_urban():
    return (
        buses_transport_demand_urban_income1()
        + buses_transport_demand_urban_income2()
        + buses_transport_demand_urban_income3()
        + buses_transport_demand_urban_income4()
        + buses_transport_demand_urban_income5()
    )


@component.add(
    name="buses transport demand urban income1",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 6},
)
def buses_transport_demand_urban_income1():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE SINGLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE COUPLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE OTHER"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME1 DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="buses transport demand urban income2",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 6},
)
def buses_transport_demand_urban_income2():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE SINGLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE COUPLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE OTHER"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME2 DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="buses transport demand urban income3",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 6},
)
def buses_transport_demand_urban_income3():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE SINGLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE COUPLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE OTHER"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME3 DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="buses transport demand urban income4",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 6},
)
def buses_transport_demand_urban_income4():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE SINGLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE COUPLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE OTHER"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME4 DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="buses transport demand urban income5",
    units="person*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 6},
)
def buses_transport_demand_urban_income5():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE SINGLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE SINGLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE COUPLE"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE COUPLEWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE OTHER"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
        + passenger_transport_real_supply()
        .loc[:, :, "BUS", "INCOME5 DENSE OTHERWCHILDREN"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="charge cycles per year",
    units="cycle/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "BATTERY VEHICLES I",
        "HOUSEHOLDS I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_passenger_vehicle_distance": 3, "autonomy_ev_vehicles": 3},
)
def charge_cycles_per_year():
    """
    Number of cycles that a vehicle battery makes m in a year, it depends of the autonomy of the battery and the total annual mileage of the vehicle.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "BATTERY VEHICLES I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, ["LDV"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "LDV", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "LDV"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)
            .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
        )
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, :, ["BUS"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "BUS", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "BUS"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)
            .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
        )
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, :, ["MOTORCYCLES 2W 3W"], :] = (
        zidz(
            desired_passenger_vehicle_distance()
            .loc[:, :, "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True),
            autonomy_ev_vehicles()
            .loc[:, "MOTORCYCLES 2W 3W"]
            .reset_coords(drop=True)
            .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)
            .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
        )
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = False
    except_subs.loc[:, :, ["BUS"], :] = False
    except_subs.loc[:, :, ["MOTORCYCLES 2W 3W"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="CO2 passenger transport emissions intensity",
    units="kg/km",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG ENERGY USE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emissions_by_passenger_transport_mode_and_power_train_35r": 1,
        "private_passenger_transport_total_distance_traveled_by_transport_mode": 1,
    },
)
def co2_passenger_transport_emissions_intensity():
    """
    GHG emissions intensity in gGHG/km by POWER_TRAIn and TRANSPORT_MODE
    """
    return zidz(
        co2_emissions_by_passenger_transport_mode_and_power_train_35r()
        .loc[:, :, :, "CO2"]
        .reset_coords(drop=True),
        private_passenger_transport_total_distance_traveled_by_transport_mode(),
    ).expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)


@component.add(
    name="cost of new vehicles acquisition",
    units="$/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "new_passenger_private_vehicles": 1,
        "price_per_vehcile": 2,
        "consumer_price_index": 1,
        "new_passenger_public_vehicles": 1,
    },
)
def cost_of_new_vehicles_acquisition():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        new_passenger_private_vehicles()
        * price_per_vehcile()
        .loc[:, _subscript_dict["PRIVATE TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
        * consumer_price_index()
        / 100
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        new_passenger_public_vehicles()
        * price_per_vehcile()
        .loc[:, _subscript_dict["PUBLIC TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
    ).values
    return value


@component.add(
    name="delayed private vehicle fleet",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_private_vehicle_fleet": 1},
    other_deps={
        "_delayfixed_delayed_private_vehicle_fleet": {
            "initial": {"private_passenger_vehicle_fleet": 1},
            "step": {"private_passenger_vehicle_fleet": 1},
        }
    },
)
def delayed_private_vehicle_fleet():
    return _delayfixed_delayed_private_vehicle_fleet()


_delayfixed_delayed_private_vehicle_fleet = DelayFixed(
    lambda: private_passenger_vehicle_fleet(),
    lambda: 1,
    lambda: private_passenger_vehicle_fleet(),
    time_step,
    "_delayfixed_delayed_private_vehicle_fleet",
)


@component.add(
    name="DESIRED PASSENGER TRANSPORT DEMAND",
    units="persons*km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exo_total_transport_demand_by_region_and_type_of_hh": 1},
)
def desired_passenger_transport_demand():
    return sum(
        exo_total_transport_demand_by_region_and_type_of_hh().rename(
            {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="desired passenger transport demand by mode and power train",
    units="persons*km",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco2nrg_modal_shares_passengers_endogenous": 1,
        "passenger_transport_demand_modal_share_endogenous": 1,
        "total_passenger_transport_demand_by_region": 2,
        "passenger_transport_modal_share_by_power_train": 1,
    },
)
def desired_passenger_transport_demand_by_mode_and_power_train():
    """
    Transport demand by region, power train and transport mode in pass*km. passengers_transport_demand_corrected_by_GDPpc[REGIONS 35 I]*PASSENGER_TRANSPORT_MODAL_SHARE[REGIONS 35 I,POWER TRAIN I ,PASSENGERS TRANSPORT MODE I]
    """
    return if_then_else(
        switch_eco2nrg_modal_shares_passengers_endogenous() == 1,
        lambda: total_passenger_transport_demand_by_region()
        * passenger_transport_demand_modal_share_endogenous(),
        lambda: total_passenger_transport_demand_by_region()
        * passenger_transport_modal_share_by_power_train(),
    )


@component.add(
    name="desired passenger transport demand by region",
    units="km*person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_transport_demand": 1},
)
def desired_passenger_transport_demand_by_region():
    return (
        sum(
            desired_transport_demand().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        / 1000000.0
    )


@component.add(
    name="desired passenger transport demand per capita",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"desired_passenger_transport_demand": 1, "population_35_regions": 1},
)
def desired_passenger_transport_demand_per_capita():
    return zidz(desired_passenger_transport_demand(), population_35_regions())


@component.add(
    name="desired passenger vehicle distance",
    units="km/(Year*vehicle)",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passengers_transport_demand_by_mode_power_train_and_type_of_households": 2,
        "load_factor_private_passenger_transport": 1,
        "private_passenger_vehicle_fleet": 1,
        "load_factor_public_passenger_transport": 1,
        "public_passenger_vehicle_fleet": 1,
        "maximum_load_factor": 1,
        "max_vehicle_distance": 1,
    },
)
def desired_passenger_vehicle_distance():
    """
    Vehicle distance needed to acomply with the desired transport demand ZIDZ(desired_passengers_transport_demand_by_mode_and_type_of_households_mod ified[REGIONS_35_I,POWER_TRAIN_I,PUBLIC_TRANSPORT_I,HOUSEHOLDS_I],(Modified _load_factor_passenger_transport[REGIONS_35_I,POWER_TRAIN_I,PUBLIC_TRANSPOR T_I,HOUSEHOLDS_I]*public_passengers_vehicle_fleet[REGIONS_35_I,POWER_TRAIN_ I,PUBLIC_TRANSPORT_I,HOUSEHOLDS_I]))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = zidz(
        desired_passengers_transport_demand_by_mode_power_train_and_type_of_households()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}),
        load_factor_private_passenger_transport() * private_passenger_vehicle_fleet(),
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        np.minimum(
            max_vehicle_distance()
            .loc[_subscript_dict["PUBLIC TRANSPORT I"]]
            .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
            zidz(
                desired_passengers_transport_demand_by_mode_power_train_and_type_of_households()
                .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
                .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
                np.minimum(
                    load_factor_public_passenger_transport(),
                    maximum_load_factor()
                    .loc[_subscript_dict["PUBLIC TRANSPORT I"]]
                    .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
                )
                * public_passenger_vehicle_fleet(),
            ).transpose(
                "PUBLIC TRANSPORT I",
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "HOUSEHOLDS I",
            ),
        )
        .transpose(
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PUBLIC TRANSPORT I",
            "HOUSEHOLDS I",
        )
        .values
    )
    return value


@component.add(
    name="desired passengers transport demand by mode power train and type of households",
    units="km*person",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_transport_demand_by_mode_and_power_train": 1,
        "share_passenger_transport_demand_by_region_and_type_of_household": 1,
        "reduction_passenger_transport_demand": 1,
    },
)
def desired_passengers_transport_demand_by_mode_power_train_and_type_of_households():
    """
    Transport demand by region, power train, transport mode and type of household modified by transport demand reduction policy, in pass*km.
    """
    return (
        desired_passenger_transport_demand_by_mode_and_power_train()
        * share_passenger_transport_demand_by_region_and_type_of_household()
        * reduction_passenger_transport_demand()
    )


@component.add(
    name="energy consumption private passenger transport by mode",
    units="EJ",
    subscripts=["REGIONS 35 I", "NRG FE I", "PRIVATE TRANSPORT I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def energy_consumption_private_passenger_transport_by_mode():
    """
    Energy passengers transport consumption by region, type of final energy, transport mode and type of household, in EJ. energy_consumption_private_transport_COICOP_physical_units[REGIONS_35_I, HOUSEHOLDS_I, HH_ELECTRICITY]= SUM(energy_consumption_private_transport_by_mode[REGIONS_35_I,FE_elec,PRIVA TE_TRANSPORT_I!,HOUSEHOLDS_I])
    """
    return (
        energy_passenger_transport_consumption_by_fe_35r()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
        / unit_conversion_mj_ej()
    )


@component.add(
    name="energy passenger transport consumption",
    units="MJ",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "mobility_passenger_transport_intensity": 1,
    },
)
def energy_passenger_transport_consumption():
    """
    Energy transport consumption by region, power train,transport mode and type of household in MJ.
    """
    return passenger_transport_real_supply() * mobility_passenger_transport_intensity()


@component.add(
    name="energy passenger transport consumption by FE 35R",
    units="MJ",
    subscripts=[
        "REGIONS 35 I",
        "NRG FE I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption": 10, "share_elec_in_phev": 2},
)
def energy_passenger_transport_consumption_by_fe_35r():
    """
    Energy passengers transport consumption by region, type of final energy, transport mode and type of household, in MJ.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I", "HOUSEHOLDS I"],
    )
    value.loc[:, ["FE elec"], :, :] = (
        (
            energy_passenger_transport_consumption()
            .loc[:, "EV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "BEV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True)
            * share_elec_in_phev()
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE gas"], :, :] = (
        energy_passenger_transport_consumption()
        .loc[:, "ICE gas", :, :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"], :, :] = (
        energy_passenger_transport_consumption()
        .loc[:, "FCEV", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"], :, :] = (
        (
            energy_passenger_transport_consumption()
            .loc[:, "ICE gasoline", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "ICE diesel", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "ICE LPG", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "HEV", :, :]
            .reset_coords(drop=True)
            + energy_passenger_transport_consumption()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True)
            * (1 - share_elec_in_phev())
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"], :, :] = 0
    value.loc[:, ["FE solid bio"], :, :] = 0
    value.loc[:, ["FE solid fossil"], :, :] = 0
    return value


@component.add(
    name="energy passengers transport consumption new",
    units="MJ",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption": 1},
)
def energy_passengers_transport_consumption_new():
    return sum(
        energy_passenger_transport_consumption().rename(
            {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="energy private transport consumption by region and FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_j_mj": 1,
        "unit_conversion_j_tj": 1,
    },
)
def energy_private_transport_consumption_by_region_and_fe():
    """
    Energy private passengers transport consumption by region, and final energy, in TJ/year.
    """
    return (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["PRIVATE TRANSPORT I!", "HOUSEHOLDS I!"],
        )
        * unit_conversion_j_mj()
        / unit_conversion_j_tj()
    )


@component.add(
    name="EXO GDPpc real",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def exo_gdppc_real():
    return xr.DataArray(
        [
            0.0451118,
            0.0427141,
            0.00633706,
            0.0111552,
            0.0193577,
            0.0179868,
            0.0540681,
            0.0163542,
            0.0435244,
            0.0392724,
            0.0412518,
            0.0166724,
            0.011818,
            0.0662618,
            0.0308321,
            0.0119721,
            0.012299,
            0.123406,
            0.025844,
            0.0455362,
            0.0122944,
            0.018584,
            0.00833145,
            0.0161427,
            0.0210165,
            0.0269513,
            0.0543691,
            0.0472851,
            0.00846259,
            0.0138824,
            0.00176239,
            0.0100765,
            0.00936603,
            0.0476612,
            0.00462099,
        ],
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    )


@component.add(
    name="EXO GDPpc SPAIN",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant, Data",
    comp_subtype="Normal",
    depends_on={"exo_gdppc_real": 1},
)
def exo_gdppc_spain():
    """
    GET_DIRECT_DATA( 'model_parameters/energy/energy-end_use-passenger_transport.xlsx' , 'GDPpc' , 'TIME_GDPPC' , 'GDPPC' )
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    )
    value.loc[["SPAIN"]] = float(exo_gdppc_real().loc["SPAIN"])
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["SPAIN"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="EXO total passenger transport demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exo_total_transport_demand_by_region_and_type_of_hh": 1},
)
def exo_total_passenger_transport_demand():
    return sum(
        exo_total_transport_demand_by_region_and_type_of_hh().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="FACTOR PASSENGERS PRIVATE FLEET",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_passengers_private_fleet"},
)
def factor_passengers_private_fleet():
    return _ext_constant_factor_passengers_private_fleet()


_ext_constant_factor_passengers_private_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FACTOR_PRIVATE_FLEET",
    {},
    _root,
    {},
    "_ext_constant_factor_passengers_private_fleet",
)


@component.add(
    name="FACTOR PASSENGERS PUBLIC FLEET",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_factor_passengers_public_fleet"},
)
def factor_passengers_public_fleet():
    return _ext_constant_factor_passengers_public_fleet()


_ext_constant_factor_passengers_public_fleet = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "FACTOR_PUBLIC_FLEET",
    {},
    _root,
    {},
    "_ext_constant_factor_passengers_public_fleet",
)


@component.add(
    name="global BEV and PHEV 2W sales",
    units="vehicles/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 2},
)
def global_bev_and_phev_2w_sales():
    return sum(
        new_passenger_private_vehicles()
        .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[:, "PHEV", "MOTORCYCLES 2W 3W", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="global BEV and PHEV LDV sales",
    units="vehicles/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 2},
)
def global_bev_and_phev_ldv_sales():
    return sum(
        new_passenger_private_vehicles()
        .loc[:, "BEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    ) + sum(
        new_passenger_private_vehicles()
        .loc[:, "PHEV", "LDV", :]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="initial passenger private fleet 1 type HH",
    units="vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passengers_private_fleet": 3},
)
def initial_passenger_private_fleet_1_type_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PRIVATE TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, ["NMT"], ["REPRESENTATIVE HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "NMT"]
        .reset_coords(drop=True)
        .expand_dims({"PASSENGERS TRANSPORT MODE I": ["NMT"]}, 2)
        .expand_dims({"HOUSEHOLDS I": ["REPRESENTATIVE HOUSEHOLD"]}, 3)
        .values
    )
    value.loc[:, :, ["LDV"], ["REPRESENTATIVE HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "LDV"]
        .reset_coords(drop=True)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .expand_dims({"HOUSEHOLDS I": ["REPRESENTATIVE HOUSEHOLD"]}, 3)
        .values
    )
    value.loc[:, :, ["MOTORCYCLES 2W 3W"], ["REPRESENTATIVE HOUSEHOLD"]] = (
        initial_passengers_private_fleet()
        .loc[:, :, "MOTORCYCLES 2W 3W"]
        .reset_coords(drop=True)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .expand_dims({"HOUSEHOLDS I": ["REPRESENTATIVE HOUSEHOLD"]}, 3)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["NMT"], :] = True
    except_subs.loc[:, :, ["NMT"], ["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = True
    except_subs.loc[:, :, ["LDV"], ["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["MOTORCYCLES 2W 3W"], :] = True
    except_subs.loc[:, :, ["MOTORCYCLES 2W 3W"], ["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="initial passenger private fleet by type of HH",
    units="vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_passengers_private_fleet": 1,
        "initial_ldv_fleet": 1,
        "initial_2w_3w_fleet": 1,
    },
)
def initial_passenger_private_fleet_by_type_of_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PRIVATE TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, ["NMT"], :] = (
        (
            initial_passengers_private_fleet().loc[:, :, "NMT"].reset_coords(drop=True)
            / 61
        )
        .expand_dims({"PASSENGERS TRANSPORT MODE I": ["NMT"]}, 2)
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3)
        .values
    )
    value.loc[:, :, ["LDV"], :] = (
        initial_ldv_fleet().expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2).values
    )
    value.loc[:, :, ["MOTORCYCLES 2W 3W"], :] = (
        initial_2w_3w_fleet()
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    return value


@component.add(
    name="INITIAL PASSENGER PUBLIC FLEET BY TYPE OF HH",
    units="vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_passenger_public_fleet_by_type_of_hh": 1},
    other_deps={
        "_initial_initial_passenger_public_fleet_by_type_of_hh": {
            "initial": {"passenger_fleet_demand": 1},
            "step": {},
        }
    },
)
def initial_passenger_public_fleet_by_type_of_hh():
    return _initial_initial_passenger_public_fleet_by_type_of_hh()


_initial_initial_passenger_public_fleet_by_type_of_hh = Initial(
    lambda: passenger_fleet_demand()
    .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
    .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
    "_initial_initial_passenger_public_fleet_by_type_of_hh",
)


@component.add(
    name="initial passenger transport demand per capita by GDPpc",
    units="Year*km*person/Mdollars 2015",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_passenger_transport_demand_per_capita_by_gdppc": 1},
    other_deps={
        "_initial_initial_passenger_transport_demand_per_capita_by_gdppc": {
            "initial": {"passenger_transport_demand_per_capita_by_gdppc": 1},
            "step": {},
        }
    },
)
def initial_passenger_transport_demand_per_capita_by_gdppc():
    return _initial_initial_passenger_transport_demand_per_capita_by_gdppc()


_initial_initial_passenger_transport_demand_per_capita_by_gdppc = Initial(
    lambda: passenger_transport_demand_per_capita_by_gdppc(),
    "_initial_initial_passenger_transport_demand_per_capita_by_gdppc",
)


@component.add(
    name="INITIAL PASSENGER TRANSPORT MODAL SHARE BY REGION",
    units="DMML",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_passenger_transport_modal_share_by_region"
    },
)
def initial_passenger_transport_modal_share_by_region():
    """
    Initial transport passenger modal share by region. Shares total 1 for each country.
    """
    return _ext_constant_initial_passenger_transport_modal_share_by_region()


_ext_constant_initial_passenger_transport_modal_share_by_region = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_PASSENGER_TRANSPORT_MODAL_SHARE_BY_REGION",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_initial_passenger_transport_modal_share_by_region",
)


@component.add(
    name="initial passenger vehicle fleet",
    units="vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_hh_transport_disaggregated": 1,
        "initial_passenger_private_fleet_by_type_of_hh": 1,
        "initial_passenger_private_fleet_1_type_hh": 1,
    },
)
def initial_passenger_vehicle_fleet():
    return if_then_else(
        switch_nrg_hh_transport_disaggregated() == 1,
        lambda: initial_passenger_private_fleet_by_type_of_hh(),
        lambda: initial_passenger_private_fleet_1_type_hh(),
    )


@component.add(
    name="INITIAL passengers transport GHG emissions",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_passengers_transport_ghg_emissions": 1},
    other_deps={
        "_initial_initial_passengers_transport_ghg_emissions": {
            "initial": {"total_passenger_transport_ghg_emissions": 1},
            "step": {},
        }
    },
)
def initial_passengers_transport_ghg_emissions():
    return _initial_initial_passengers_transport_ghg_emissions()


_initial_initial_passengers_transport_ghg_emissions = Initial(
    lambda: total_passenger_transport_ghg_emissions(),
    "_initial_initial_passengers_transport_ghg_emissions",
)


@component.add(
    name="INITIAL POWER TRAIN SHARE BY PASSENGER TRANSPORT MODE",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_power_train_share_by_passenger_transport_mode"
    },
)
def initial_power_train_share_by_passenger_transport_mode():
    """
    Target passenger transport by power train, transport mode and region. Each share totals 1 for each transport mode.
    """
    return _ext_constant_initial_power_train_share_by_passenger_transport_mode()


_ext_constant_initial_power_train_share_by_passenger_transport_mode = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_initial_power_train_share_by_passenger_transport_mode",
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_power_train_share_by_passenger_transport_mode.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="initial public passenger vehicle fleet",
    units="vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_hh_transport_disaggregated": 1,
        "initial_passenger_public_fleet_by_type_of_hh": 1,
        "initial_public_passenger_vehicle_fleet_1_type_of_hh": 1,
    },
)
def initial_public_passenger_vehicle_fleet():
    return if_then_else(
        switch_nrg_hh_transport_disaggregated() == 1,
        lambda: initial_passenger_public_fleet_by_type_of_hh(),
        lambda: initial_public_passenger_vehicle_fleet_1_type_of_hh(),
    )


@component.add(
    name="initial public passenger vehicle fleet 1 type of HH",
    units="vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passengers_public_fleet": 1},
)
def initial_public_passenger_vehicle_fleet_1_type_of_hh():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PUBLIC TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, :, ["REPRESENTATIVE HOUSEHOLD"]] = (
        initial_passengers_public_fleet()
        .expand_dims({"HOUSEHOLDS I": ["REPRESENTATIVE HOUSEHOLD"]}, 3)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, :, ["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="INITIAL RAIL C",
    units="persons*km",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_rail_c": 1},
    other_deps={
        "_initial_initial_rail_c": {
            "initial": {
                "desired_passenger_transport_demand_by_mode_and_power_train": 1
            },
            "step": {},
        }
    },
)
def initial_rail_c():
    return _initial_initial_rail_c()


_initial_initial_rail_c = Initial(
    lambda: sum(
        desired_passenger_transport_demand_by_mode_and_power_train()
        .loc["SPAIN", :, "RAIL"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )
    * 0.342176,
    "_initial_initial_rail_c",
)


@component.add(
    name="INITIAL RAIL MD",
    units="persons*km",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_rail_md": 1},
    other_deps={
        "_initial_initial_rail_md": {
            "initial": {
                "desired_passenger_transport_demand_by_mode_and_power_train": 1
            },
            "step": {},
        }
    },
)
def initial_rail_md():
    return _initial_initial_rail_md()


_initial_initial_rail_md = Initial(
    lambda: sum(
        desired_passenger_transport_demand_by_mode_and_power_train()
        .loc["SPAIN", :, "RAIL"]
        .reset_coords(drop=True)
        .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
        dim=["TRANSPORT POWER TRAIN I!"],
    )
    * 0.118833,
    "_initial_initial_rail_md",
)


@component.add(
    name="LDV transport demand dense HH",
    units="km*person",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 1},
)
def ldv_transport_demand_dense_hh():
    return sum(
        passenger_transport_real_supply()
        .loc[:, :, :, _subscript_dict["HOUSEHOLDS DENSE I"]]
        .rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "HOUSEHOLDS I": "HOUSEHOLDS DENSE I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS DENSE I!"],
    )


@component.add(
    name="lifetime passenger vehicles",
    units="Years",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mileage_vehicles": 10,
        "smooth_desired_passenger_vehicle_distance": 4,
        "mod_passenger_vehicles_lifetime": 6,
        "max_lifetime_passenger_vehicles": 5,
        "desired_passenger_vehicle_distance": 6,
        "battery_lifetime": 1,
        "lifetime_electrified_vehicle_batteries": 25,
    },
)
def lifetime_passenger_vehicles():
    """
    Lifetime vehicles data modified. --Eq-- MAX(MIN(ZIDZ(MILEAGE_VEHICLES[BEV,LDV],desired_passengers_vehicle_distance[REGIONS 35 I,BEV ,LDV,HOUSEHOLDS I] )*mod_passengers_lifetime[REGIONS 35 I,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,LMO,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NMC622,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NMC811,BEV,LDV], MIN(lifetime_electrified_vehicle_batteries[REGIONS 35 I,NCA,BEV,LDV], lifetime_electrified_vehicle_batteries[REGIONS 35 I,LFP,BEV,LDV]))))),1)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = True
    except_subs.loc[:, :, ["BUS"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            zidz(
                mileage_vehicles()
                .loc[:, _subscript_dict["PUBLIC TRANSPORT I"]]
                .rename({"TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
                .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 2)
                .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
                smooth_desired_passenger_vehicle_distance()
                .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
                .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
                .transpose(
                    "TRANSPORT POWER TRAIN I",
                    "PUBLIC TRANSPORT I",
                    "REGIONS 35 I",
                    "HOUSEHOLDS I",
                ),
            )
            * mod_passenger_vehicles_lifetime()
            .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]]
            .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
            .transpose("TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I", "REGIONS 35 I"),
            max_lifetime_passenger_vehicles()
            .loc[_subscript_dict["PUBLIC TRANSPORT I"]]
            .rename({"TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        )
        .transpose(
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PUBLIC TRANSPORT I",
            "HOUSEHOLDS I",
        )
        .values[except_subs.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :].values]
    )
    value.loc[:, :, ["NMT"], :] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["LDV"], :] = True
    except_subs.loc[:, ["BEV"], ["LDV"], :] = False
    except_subs.loc[:, ["PHEV"], ["LDV"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "LDV"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 1)
                    .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
                    smooth_desired_passenger_vehicle_distance()
                    .loc[:, :, "LDV", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT POWER TRAIN I", "REGIONS 35 I", "HOUSEHOLDS I"
                    ),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, :, "LDV"]
                .reset_coords(drop=True)
                .transpose("TRANSPORT POWER TRAIN I", "REGIONS 35 I"),
            ),
            float(max_lifetime_passenger_vehicles().loc["LDV"]),
        )
        .transpose("REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I")
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values[except_subs.loc[:, :, ["LDV"], :].values]
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["BUS"], :] = True
    except_subs.loc[:, ["BEV"], ["BUS"], :] = False
    except_subs.loc[:, ["PHEV"], ["BUS"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "BUS"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 1)
                    .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, "BUS", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT POWER TRAIN I", "REGIONS 35 I", "HOUSEHOLDS I"
                    ),
                ),
            ),
            float(max_lifetime_passenger_vehicles().loc["BUS"]),
        )
        .transpose("REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I")
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values[except_subs.loc[:, :, ["BUS"], :].values]
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["MOTORCYCLES 2W 3W"], :] = True
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"], :] = False
    except_subs.loc[:, ["PHEV"], ["MOTORCYCLES 2W 3W"], :] = False
    value.values[except_subs.values] = (
        np.minimum(
            np.maximum(
                1,
                zidz(
                    mileage_vehicles()
                    .loc[:, "MOTORCYCLES 2W 3W"]
                    .reset_coords(drop=True)
                    .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 1)
                    .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 2),
                    desired_passenger_vehicle_distance()
                    .loc[:, :, "MOTORCYCLES 2W 3W", :]
                    .reset_coords(drop=True)
                    .transpose(
                        "TRANSPORT POWER TRAIN I", "REGIONS 35 I", "HOUSEHOLDS I"
                    ),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, :, "MOTORCYCLES 2W 3W"]
                .reset_coords(drop=True)
                .transpose("TRANSPORT POWER TRAIN I", "REGIONS 35 I"),
            ),
            float(max_lifetime_passenger_vehicles().loc["MOTORCYCLES 2W 3W"]),
        )
        .transpose("REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I")
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values[except_subs.loc[:, :, ["MOTORCYCLES 2W 3W"], :].values]
    )
    value.loc[:, ["BEV"], ["LDV"], :] = (
        np.minimum(
            np.minimum(
                battery_lifetime().loc[:, "BEV", "LDV", :].reset_coords(drop=True),
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "LDV"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "LDV", :]
                    .reset_coords(drop=True),
                ),
            ),
            float(max_lifetime_passenger_vehicles().loc["LDV"]),
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["LDV"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "LDV"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    smooth_desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "LDV", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "PHEV", "LDV"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "LDV"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "LDV"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "LDV"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "LDV"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "LDV"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["BUS"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "BUS"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "BUS", :]
                    .reset_coords(drop=True),
                ),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "BEV", "BUS"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "BEV", "BUS"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "BEV", "BUS"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "BEV", "BUS"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "BEV", "BUS"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["BUS"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "BUS"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    smooth_desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "BUS", :]
                    .reset_coords(drop=True),
                ),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "BUS"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "BUS"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "BUS"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "BUS"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "BUS"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["BEV", "MOTORCYCLES 2W 3W"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "BEV", "MOTORCYCLES 2W 3W"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "BEV", "MOTORCYCLES 2W 3W"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "BEV", "MOTORCYCLES 2W 3W"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "BEV", "MOTORCYCLES 2W 3W"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "BEV", "MOTORCYCLES 2W 3W"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "BEV", "MOTORCYCLES 2W 3W"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["MOTORCYCLES 2W 3W"], :] = (
        np.maximum(
            np.minimum(
                zidz(
                    xr.DataArray(
                        float(mileage_vehicles().loc["PHEV", "MOTORCYCLES 2W 3W"]),
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        ["REGIONS 35 I", "HOUSEHOLDS I"],
                    ),
                    desired_passenger_vehicle_distance()
                    .loc[:, "PHEV", "MOTORCYCLES 2W 3W", :]
                    .reset_coords(drop=True),
                )
                * mod_passenger_vehicles_lifetime()
                .loc[:, "PHEV", "MOTORCYCLES 2W 3W"]
                .reset_coords(drop=True),
                np.minimum(
                    lifetime_electrified_vehicle_batteries()
                    .loc[:, "LMO", "PHEV", "MOTORCYCLES 2W 3W"]
                    .reset_coords(drop=True),
                    np.minimum(
                        lifetime_electrified_vehicle_batteries()
                        .loc[:, "NMC622", "PHEV", "MOTORCYCLES 2W 3W"]
                        .reset_coords(drop=True),
                        np.minimum(
                            lifetime_electrified_vehicle_batteries()
                            .loc[:, "NMC811", "PHEV", "MOTORCYCLES 2W 3W"]
                            .reset_coords(drop=True),
                            np.minimum(
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "NCA", "PHEV", "MOTORCYCLES 2W 3W"]
                                .reset_coords(drop=True),
                                lifetime_electrified_vehicle_batteries()
                                .loc[:, "LFP", "PHEV", "MOTORCYCLES 2W 3W"]
                                .reset_coords(drop=True),
                            ),
                        ),
                    ),
                ),
            ),
            1,
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    return value


@component.add(
    name="load factor LDV",
    units="persons/vehicle",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "desired_passenger_vehicle_distance": 1,
        "private_passenger_vehicle_fleet": 1,
    },
)
def load_factor_ldv():
    """
    Load factor of LDV vechiles by power train and type of household, in persons/vehicle.
    """
    return zidz(
        passenger_transport_real_supply().loc[:, :, "LDV", :].reset_coords(drop=True),
        desired_passenger_vehicle_distance().loc[:, :, "LDV", :].reset_coords(drop=True)
        * private_passenger_vehicle_fleet().loc[:, :, "LDV", :].reset_coords(drop=True),
    )


@component.add(
    name="load factor passenger commercial vehicles",
    units="persons/vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "public_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 1,
    },
)
def load_factor_passenger_commercial_vehicles():
    """
    Load factor of public vehicle transport by region, power train, public trasnport mode and type of household in persons/vehicle.
    """
    return zidz(
        passenger_transport_real_supply()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        public_passenger_vehicle_fleet()
        * desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
    )


@component.add(
    name="load factor private passenger transport",
    units="person/vehicles",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_load_factor_passengers_vehicles": 1,
        "load_factor_private_passenger_transport_change": 1,
    },
)
def load_factor_private_passenger_transport():
    return initial_load_factor_passengers_vehicles().loc[
        :, :, _subscript_dict["PRIVATE TRANSPORT I"]
    ].rename(
        {"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}
    ) * load_factor_private_passenger_transport_change().loc[
        :, :, _subscript_dict["PRIVATE TRANSPORT I"], :
    ].rename(
        {"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}
    )


@component.add(
    name="load factor private passenger transport change",
    units="persons/vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_load_factor_change_sp": 2,
        "time": 2,
        "objective_load_factor_change_sp": 1,
        "year_initial_load_factor_change_sp": 3,
        "year_final_load_factor_change_sp": 2,
        "initial_load_factor_passengers_vehicles": 1,
    },
)
def load_factor_private_passenger_transport_change():
    """
    Vehicle load factor modified with the behavioral change variable. --Eq-- IF_THEN_ELSE(SWITCH_LOAD_FACTOR_CHANGE_SP=0, INITIAL_LOAD_FACTOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PRIVATE_ TRANSPORT_I], IF_THEN_ELSE(SWITCH_LOAD_FACTOR_CHANGE_SP=1:AND:Time<YEAR_INITIAL_LOAD_FACTOR_CHANGE_ SP, INITIAL_LOAD_FACTOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PRIVATE_ TRANSPORT_I], IF_THEN_ELSE(OBJECTIVE_LOAD_FACTOR_CHANGE_SP[REGIONS_35_I,PRIVATE_TRANSPORT_I]=1,INIT IAL_LOAD_FACTOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PR IVATE_TRANSPORT_I], INITIAL_LOAD_FACTOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PRIVATE_ TRANSPORT_I]*(MIN(MAXIMUM_LOAD_FACTOR[PRIVATE_TRANSPORT_I],INITIAL_LOAD_FAC TOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PRIVATE_TRANSP ORT_I]+ (RAMP((OBJECTIVE_LOAD_FACTOR_CHANGE_SP[REGIONS_35_I,PRIVATE_TRANSPORT_I]-INITIAL_LOAD _FACTOR_PASSENGERS_VEHICLES[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I ,PRIVATE_TRANSPORT_I])/(YEAR_FINAL_LOAD_FACTOR_CHANGE_SP-YEAR_INITIAL_LOAD_FACTOR_CHA NGE_SP),YEAR_INITIAL_LOAD_FACTOR_CHANGE_SP,YEAR_FINAL_LOAD_FACTOR_CHANGE_SP )) )) )))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        if_then_else(
            switch_load_factor_change_sp() == 0,
            lambda: xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
                },
                ["REGIONS 35 I", "PRIVATE TRANSPORT I"],
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_load_factor_change_sp() == 1,
                    time() < year_initial_load_factor_change_sp(),
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
                    },
                    ["REGIONS 35 I", "PRIVATE TRANSPORT I"],
                ),
                lambda: 1
                + ramp(
                    __data["time"],
                    (objective_load_factor_change_sp() - 1)
                    / (
                        year_final_load_factor_change_sp()
                        - year_initial_load_factor_change_sp()
                    ),
                    year_initial_load_factor_change_sp(),
                    year_final_load_factor_change_sp(),
                ),
            ),
        )
        .expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 1
        )
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3)
        .values
    )
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        initial_load_factor_passengers_vehicles()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3)
        .values
    )
    return value


@component.add(
    name="load factor public passenger transport",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_load_factor_public_passenger_transport": 1},
    other_deps={
        "_integ_load_factor_public_passenger_transport": {
            "initial": {"initial_load_factor_passengers_vehicles": 1},
            "step": {"variation_load_factor_passenger_transport": 1},
        }
    },
)
def load_factor_public_passenger_transport():
    return _integ_load_factor_public_passenger_transport()


_integ_load_factor_public_passenger_transport = Integ(
    lambda: variation_load_factor_passenger_transport(),
    lambda: initial_load_factor_passengers_vehicles()
    .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]]
    .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
    .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
    "_integ_load_factor_public_passenger_transport",
)


@component.add(
    name="MAX LIFETIME PASSENGER VEHICLES",
    units="Years",
    subscripts=["TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_lifetime_passenger_vehicles"},
)
def max_lifetime_passenger_vehicles():
    return _ext_constant_max_lifetime_passenger_vehicles()


_ext_constant_max_lifetime_passenger_vehicles = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "MAX_LIFETIME_PASSENGER_VEHICLES*",
    {"TRANSPORT MODE I": _subscript_dict["TRANSPORT MODE I"]},
    _root,
    {"TRANSPORT MODE I": _subscript_dict["TRANSPORT MODE I"]},
    "_ext_constant_max_lifetime_passenger_vehicles",
)


@component.add(
    name="MAX VEHICLE DISTANCE",
    units="km/(Year*vehicle)",
    subscripts=["PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_max_vehicle_distance"},
)
def max_vehicle_distance():
    return _ext_constant_max_vehicle_distance()


_ext_constant_max_vehicle_distance = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "MAX_VEHICLE_DISTANCE*",
    {"PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"]},
    _root,
    {"PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"]},
    "_ext_constant_max_vehicle_distance",
)


@component.add(
    name="MAXIMUM LOAD FACTOR",
    units="persons/vehicle",
    subscripts=["PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_maximum_load_factor"},
)
def maximum_load_factor():
    return _ext_constant_maximum_load_factor()


_ext_constant_maximum_load_factor = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "MAX_LOAD_FACTOR*",
    {"PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"]},
    _root,
    {"PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"]},
    "_ext_constant_maximum_load_factor",
)


@component.add(
    name="mobility passenger transport intensity",
    units="MJ/(person*km)",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_fuel_consumption_efficiency": 2,
        "load_factor_private_passenger_transport": 1,
        "load_factor_public_passenger_transport": 1,
    },
)
def mobility_passenger_transport_intensity():
    """
    Energy vehicle consumption modified by efficiency change and load factor policies by region, power train and transport mode in MJ/(person*km)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = zidz(
        passenger_transport_fuel_consumption_efficiency()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
        load_factor_private_passenger_transport(),
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = zidz(
        passenger_transport_fuel_consumption_efficiency()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
        load_factor_public_passenger_transport(),
    ).values
    return value


@component.add(
    name="mod passenger vehicles lifetime",
    units="1",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_fleet_demand": 2,
        "private_passenger_vehicle_fleet": 1,
        "public_passenger_vehicle_fleet": 1,
        "time": 1,
    },
)
def mod_passenger_vehicles_lifetime():
    """
    Modifier of private vehicle lifetime in function of vehicle stock and demand of new vehciles. This variable endogenizes the behavioral change of the users in relation to the lifetime extension of the vehicles, it is designed to modify the lifetime in case the demand for cars is higher than the operational fleet in order not to increase so much the purchase of new vehicles in the short term.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"]] = np.maximum(
        1,
        zidz(
            sum(
                passenger_fleet_demand()
                .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
                .rename(
                    {
                        "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["HOUSEHOLDS I!"],
            ),
            sum(
                private_passenger_vehicle_fleet().rename(
                    {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            ),
        ),
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]] = if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
            },
            ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I"],
        ),
        lambda: np.maximum(
            0.01,
            zidz(
                sum(
                    passenger_fleet_demand()
                    .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
                    .rename(
                        {
                            "PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I",
                            "HOUSEHOLDS I": "HOUSEHOLDS I!",
                        }
                    ),
                    dim=["HOUSEHOLDS I!"],
                ),
                sum(
                    public_passenger_vehicle_fleet().rename(
                        {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
                    ),
                    dim=["HOUSEHOLDS I!"],
                ),
            ),
        ),
    ).values
    return value


@component.add(
    name="modal split",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_exc_ldv_adjusted": 2},
)
def modal_split():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["LDV"]] = False
    value.values[except_subs.values] = modal_split_exc_ldv_adjusted().values[
        except_subs.values
    ]
    value.loc[:, ["LDV"]] = (
        (
            1
            - sum(
                modal_split_exc_ldv_adjusted().rename(
                    {"PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!"}
                ),
                dim=["PASSENGERS TRANSPORT MODE I!"],
            )
        )
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 1)
        .values
    )
    return value


@component.add(
    name="modal split BUS",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_public": 1, "subshare_bus": 1},
)
def modal_split_bus():
    return modal_split_public() * subshare_bus()


@component.add(
    name="modal split exc LDV",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_modal_share_by_power_train": 1,
        "modal_split_bus": 1,
        "modal_split_rail": 1,
    },
)
def modal_split_exc_ldv():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BUS"]] = False
    except_subs.loc[:, ["RAIL"]] = False
    except_subs.loc[:, ["LDV"]] = False
    value.values[except_subs.values] = sum(
        passenger_transport_modal_share_by_power_train().rename(
            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
        ),
        dim=["TRANSPORT POWER TRAIN I!"],
    ).values[except_subs.values]
    value.loc[:, ["BUS"]] = (
        modal_split_bus().expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 1).values
    )
    value.loc[:, ["RAIL"]] = (
        modal_split_rail().expand_dims({"FREIGHT TRANSPORT MODE I": ["RAIL"]}, 1).values
    )
    value.loc[:, ["LDV"]] = 0
    return value


@component.add(
    name="modal split exc LDV adjusted",
    units="DMNL",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_exc_ldv": 4},
)
def modal_split_exc_ldv_adjusted():
    """
    Adjustmento of modal split when shares >1
    """
    return if_then_else(
        (
            sum(
                modal_split_exc_ldv().rename(
                    {"PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!"}
                ),
                dim=["PASSENGERS TRANSPORT MODE I!"],
            )
            > 1
        ).expand_dims(
            {
                "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                    "PASSENGERS TRANSPORT MODE I"
                ]
            },
            1,
        ),
        lambda: zidz(
            modal_split_exc_ldv(),
            sum(
                modal_split_exc_ldv().rename(
                    {"PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!"}
                ),
                dim=["PASSENGERS TRANSPORT MODE I!"],
            ).expand_dims(
                {
                    "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                        "PASSENGERS TRANSPORT MODE I"
                    ]
                },
                1,
            ),
        ),
        lambda: modal_split_exc_ldv(),
    )


@component.add(
    name="modal split public",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trend_modal_split_public": 1,
        "sigma_public_transport": 1,
        "initial_price_coicop": 1,
        "price_coicop": 1,
    },
)
def modal_split_public():
    """
    Share of pulbic transport calcualted as a function of the price of fuel and a trend
    """
    return np.exp(
        trend_modal_split_public()
        + sigma_public_transport()
        * np.log(
            zidz(
                price_coicop().loc[:, "HH FUEL TRANSPORT"].reset_coords(drop=True),
                initial_price_coicop()
                .loc[:, "HH FUEL TRANSPORT"]
                .reset_coords(drop=True),
            )
        )
    )


@component.add(
    name="modal split rail",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"modal_split_public": 1, "subshare_rail": 1},
)
def modal_split_rail():
    return modal_split_public() * subshare_rail()


@component.add(
    name="new passenger private vehicles",
    units="vehicle/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_fleet_demand": 10,
        "private_passenger_vehicle_fleet": 10,
        "factor_passengers_private_fleet": 5,
        "year_initial_passenger_transport_share_sp": 2,
        "time": 2,
        "bev_switch_policy": 2,
    },
)
def new_passenger_private_vehicles():
    """
    New private vehicle flow by region, power train, private transport mode and type of household, in number of vehicles/year. --Eq-- IF_THEN_ELSE(BEV_switch_policy=1:AND:Time>=YEAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP, IF_THEN_ELSE(passenger_fleet_demand[REGIONS_35_I,BEV,LDV,HOUSEHOLDS_I]<private_passen ger_vehicle_fleet [REGIONS_35_I,BEV,LDV,HOUSEHOLDS_I], 0 , (SUM(passenger_fleet_demand[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I !,LDV,HOUSEHOLDS_I])- SUM(private_passenger_vehicle_fleet[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I!,LDV,HOUSEHO LDS_I]))*FACTOR_PASSENGERS_PRIVATE_FLEET ), IF_THEN_ELSE(passenger_fleet_demand[REGIONS_35_I,BEV,LDV,HOUSEHOLDS_I]<private_passen ger_vehicle_fleet [REGIONS_35_I,BEV,LDV,HOUSEHOLDS_I], 0 , (passenger_fleet_demand[REGIONS_35_I,BEV ,LDV,HOUSEHOLDS_I]- private_passenger_vehicle_fleet[REGIONS_35_I,BEV,LDV,HOUSEHOLDS_I])*FACTOR_PASSENGERS _PRIVATE_FLEET )) --Eq-- MAX(0, MIN(MAXIMUM_BUDGET_FOR_VEHICLES[transport mode,type household]/PRICE_PER_VEHICLE[transport mode,type household], (Vehicle_fleet_demand[transport mode,type household]-vehicle_fleet[transport mode,type household])*FACTOR))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PRIVATE TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["LDV"], :] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"], :] = False
    value.values[except_subs.values] = if_then_else(
        passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
        < private_passenger_vehicle_fleet(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PRIVATE TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
        lambda: (
            passenger_fleet_demand()
            .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
            - private_passenger_vehicle_fleet()
        )
        * factor_passengers_private_fleet(),
    ).values[except_subs.values]
    value.loc[:, ["BEV"], ["LDV"], :] = (
        if_then_else(
            np.logical_and(
                bev_switch_policy() == 1,
                time() >= year_initial_passenger_transport_share_sp(),
            ),
            lambda: if_then_else(
                passenger_fleet_demand().loc[:, "BEV", "LDV", :].reset_coords(drop=True)
                < private_passenger_vehicle_fleet()
                .loc[:, "BEV", "LDV", :]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                    },
                    ["REGIONS 35 I", "HOUSEHOLDS I"],
                ),
                lambda: (
                    sum(
                        passenger_fleet_demand()
                        .loc[:, :, "LDV", :]
                        .reset_coords(drop=True)
                        .rename(
                            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                        ),
                        dim=["TRANSPORT POWER TRAIN I!"],
                    )
                    - sum(
                        private_passenger_vehicle_fleet()
                        .loc[:, :, "LDV", :]
                        .reset_coords(drop=True)
                        .rename(
                            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                        ),
                        dim=["TRANSPORT POWER TRAIN I!"],
                    )
                )
                * factor_passengers_private_fleet(),
            ),
            lambda: if_then_else(
                passenger_fleet_demand().loc[:, "BEV", "LDV", :].reset_coords(drop=True)
                < private_passenger_vehicle_fleet()
                .loc[:, "BEV", "LDV", :]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                    },
                    ["REGIONS 35 I", "HOUSEHOLDS I"],
                ),
                lambda: (
                    passenger_fleet_demand()
                    .loc[:, "BEV", "LDV", :]
                    .reset_coords(drop=True)
                    - private_passenger_vehicle_fleet()
                    .loc[:, "BEV", "LDV", :]
                    .reset_coords(drop=True)
                )
                * factor_passengers_private_fleet(),
            ),
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"], :] = (
        if_then_else(
            np.logical_and(
                bev_switch_policy() == 1,
                time() >= year_initial_passenger_transport_share_sp() + 2,
            ),
            lambda: if_then_else(
                passenger_fleet_demand()
                .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                .reset_coords(drop=True)
                < private_passenger_vehicle_fleet()
                .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                    },
                    ["REGIONS 35 I", "HOUSEHOLDS I"],
                ),
                lambda: (
                    sum(
                        passenger_fleet_demand()
                        .loc[:, :, "MOTORCYCLES 2W 3W", :]
                        .reset_coords(drop=True)
                        .rename(
                            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                        ),
                        dim=["TRANSPORT POWER TRAIN I!"],
                    )
                    - sum(
                        private_passenger_vehicle_fleet()
                        .loc[:, :, "MOTORCYCLES 2W 3W", :]
                        .reset_coords(drop=True)
                        .rename(
                            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                        ),
                        dim=["TRANSPORT POWER TRAIN I!"],
                    )
                )
                * factor_passengers_private_fleet(),
            ),
            lambda: if_then_else(
                passenger_fleet_demand()
                .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                .reset_coords(drop=True)
                < private_passenger_vehicle_fleet()
                .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                .reset_coords(drop=True),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                    },
                    ["REGIONS 35 I", "HOUSEHOLDS I"],
                ),
                lambda: (
                    passenger_fleet_demand()
                    .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                    .reset_coords(drop=True)
                    - private_passenger_vehicle_fleet()
                    .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
                    .reset_coords(drop=True)
                )
                * factor_passengers_private_fleet(),
            ),
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    return value


@component.add(
    name="new passenger public vehicles",
    units="vehicle/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_fleet_demand": 2,
        "public_passenger_vehicle_fleet": 2,
        "factor_passengers_public_fleet": 1,
    },
)
def new_passenger_public_vehicles():
    """
    New public vehicle flow by region, power train, public transport mode and type of household, in number of vehicles/year.
    """
    return if_then_else(
        passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
        < public_passenger_vehicle_fleet(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PUBLIC TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
        lambda: (
            passenger_fleet_demand()
            .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
            .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
            - public_passenger_vehicle_fleet()
        )
        * factor_passengers_public_fleet(),
    )


@component.add(
    name="new private passenger vehicles",
    units="vehicles/Year",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 1},
)
def new_private_passenger_vehicles():
    return (
        new_passenger_private_vehicles()
        .loc[:, :, :, "REPRESENTATIVE HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="new public passenger vehicles",
    units="vehicles/Year",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_public_vehicles": 1},
)
def new_public_passenger_vehicles():
    return (
        new_passenger_public_vehicles()
        .loc[:, :, :, "REPRESENTATIVE HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="occupancy rate",
    units="DMML",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_load_factor": 1, "maximum_load_factor": 1},
)
def occupancy_rate():
    return zidz(
        real_load_factor(),
        maximum_load_factor()
        .loc[_subscript_dict["PUBLIC TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
        .expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)
        .expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 1
        )
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
    )


@component.add(
    name="passenger fleet demand",
    units="vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passengers_transport_demand_by_mode_power_train_and_type_of_households": 2,
        "load_factor_public_passenger_transport": 1,
        "maximum_load_factor": 1,
        "initial_passengers_vehicle_distance": 2,
        "load_factor_private_passenger_transport": 1,
    },
)
def passenger_fleet_demand():
    """
    Vehicle fleet demand by region, power train, transport mode and type of household in vehicles. ZIDZ(desired_passengers_transport_demand_by_mode_and_type_of_households_modified[REGI ONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I ,HOUSEHOLDS I],(modified_load_factor_passenger_transport[REGIONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I ,HOUSEHOLDS I]* INITIAL_PASSENGERS_VEHICLE_DISTANCE[REGIONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I]))
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = zidz(
        desired_passengers_transport_demand_by_mode_power_train_and_type_of_households()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        np.minimum(
            load_factor_public_passenger_transport(),
            maximum_load_factor()
            .loc[_subscript_dict["PUBLIC TRANSPORT I"]]
            .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        )
        * initial_passengers_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
    ).values
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = zidz(
        desired_passengers_transport_demand_by_mode_power_train_and_type_of_households()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}),
        load_factor_private_passenger_transport()
        * initial_passengers_vehicle_distance()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"]]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}),
    ).values
    return value


@component.add(
    name="passenger transport baseline",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passenger_transport_demand_share": 1},
)
def passenger_transport_baseline():
    return initial_passenger_transport_demand_share()


@component.add(
    name="passenger transport demand corrected by GDPpc",
    units="km*person",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_dynamic_transport_demand": 1,
        "desired_passenger_transport_demand": 1,
        "exo_gdppc_spain": 1,
        "initial_passenger_transport_demand_per_capita_by_gdppc": 1,
        "population_35_regions": 1,
    },
)
def passenger_transport_demand_corrected_by_gdppc():
    """
    total transport demand by region in pass*km. --- EXO_GDPpc_real[REGIONS 35 I]*initial_passengers_transport_demand_per_capita_by_GDPpc[REGIONS 35 I]*population_35_regions [REGIONS 35 I ]
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        ["REGIONS 35 I", "HOUSEHOLDS I"],
    )
    value.loc[:, ["REPRESENTATIVE HOUSEHOLD"]] = (
        if_then_else(
            switch_nrg_dynamic_transport_demand() == 0,
            lambda: desired_passenger_transport_demand(),
            lambda: exo_gdppc_spain()
            * initial_passenger_transport_demand_per_capita_by_gdppc()
            * population_35_regions(),
        )
        .expand_dims({"HOUSEHOLDS I": ["REPRESENTATIVE HOUSEHOLD"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["REPRESENTATIVE HOUSEHOLD"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="passenger transport demand modal share endogenous",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "passenger_transport_modal_share_by_power_train": 1,
        "share_technologies_passenger_transport": 1,
        "modal_split": 1,
    },
)
def passenger_transport_demand_modal_share_endogenous():
    """
    Shares of passanger transport demand by technology and mode
    """
    return np.maximum(
        1e-06,
        if_then_else(
            time() < 2015,
            lambda: passenger_transport_modal_share_by_power_train(),
            lambda: share_technologies_passenger_transport() * modal_split(),
        ),
    )


@component.add(
    name="passenger transport demand per capita by GDPpc",
    units="Year*km*person/Mdollars 2015",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_transport_demand_per_capita": 1,
        "exo_gdppc_spain": 1,
    },
)
def passenger_transport_demand_per_capita_by_gdppc():
    """
    Total transport demand per capita by unit of GDPpc.
    """
    return zidz(desired_passenger_transport_demand_per_capita(), exo_gdppc_spain())


@component.add(
    name="passenger transport demand public fleet",
    units="persons*km",
    subscripts=["REGIONS 35 I", "PUBLIC TRANSPORT I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply_by_mode": 1},
)
def passenger_transport_demand_public_fleet():
    """
    Public transport supply by region, public transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    return (
        passenger_transport_real_supply_by_mode()
        .loc[:, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
    )


@component.add(
    name="passenger transport fuel consumption efficiency",
    units="MJ/(km*vehicles)",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_consumption_initial": 1,
        "passenger_transport_fuel_consumption_efficiency_change": 1,
    },
)
def passenger_transport_fuel_consumption_efficiency():
    """
    Energy vehicle consumption modified by efficiency change policy by region, power train and transport mode in MJ/(vehicle*km)
    """
    return (
        final_energy_consumption_initial()
        * passenger_transport_fuel_consumption_efficiency_change()
    )


@component.add(
    name="passenger transport fuel consumption efficiency change",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fuel_consumption_efficiency_change_sp": 2,
        "objective_fuel_consumption_efficiency_change_sp": 1,
        "year_final_fuel_consumption_efficiency_change_sp": 2,
        "time": 2,
        "year_initial_fuel_consumption_efficiency_change_sp": 3,
    },
)
def passenger_transport_fuel_consumption_efficiency_change():
    """
    Passenger transport fuel consumption efficiency variation.
    """
    return if_then_else(
        switch_fuel_consumption_efficiency_change_sp() == 0,
        lambda: xr.DataArray(
            1,
            {
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                    "PASSENGERS TRANSPORT MODE I"
                ],
            },
            ["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
        ),
        lambda: if_then_else(
            np.logical_and(
                switch_fuel_consumption_efficiency_change_sp() == 1,
                time() < year_initial_fuel_consumption_efficiency_change_sp(),
            ),
            lambda: xr.DataArray(
                1,
                {
                    "TRANSPORT POWER TRAIN I": _subscript_dict[
                        "TRANSPORT POWER TRAIN I"
                    ],
                    "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                        "PASSENGERS TRANSPORT MODE I"
                    ],
                },
                ["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
            ),
            lambda: 1
            + ramp(
                __data["time"],
                (objective_fuel_consumption_efficiency_change_sp() - 1)
                / (
                    year_final_fuel_consumption_efficiency_change_sp()
                    - year_initial_fuel_consumption_efficiency_change_sp()
                ),
                year_initial_fuel_consumption_efficiency_change_sp(),
                year_final_fuel_consumption_efficiency_change_sp(),
            ),
        ),
    ).expand_dims({"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0)


@component.add(
    name="passenger transport GHG emissions",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_ghg_emissions": 1},
)
def passenger_transport_ghg_emissions():
    return total_passenger_transport_ghg_emissions()


@component.add(
    name="passenger transport modal share by power train",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_passenger_transport_demand_modal_share": 1,
        "year_initial_passenger_transport_share_sp": 2,
        "time": 1,
        "passenger_transport_baseline": 3,
        "target_passenger_transport_modal_share_by_power_train": 1,
        "year_final_passenger_transport_share_sp": 2,
        "switch_passenger_transport_modal_share_sp": 1,
    },
)
def passenger_transport_modal_share_by_power_train():
    """
    Demand transport share by transport mode and power train. ---Eq--- IF_THEN_ELSE(SWITCH_MODEL_EXPLORER =1,model_explorer_passenger_transport_demand_modal_share[REGIONS 35 I,TRANSPORT POWER TRAIN I ,PASSENGERS TRANSPORT MODE I], IF_THEN_ELSE(SWITCH_PASSENGER_TRANSPORT_MODAL_SHARE_SP=0,INITIAL_PASSENGER_TRANSPORT_ DEMAND_SHARE[REGIONS 35 I,TRANSPORT POWER TRAIN I ,PASSENGERS TRANSPORT MODE I], IF_THEN_ELSE(SWITCH_PASSENGER_TRANSPORT_MODAL_SHARE_SP=1:AND:Time<YEAR_INITIAL_PASSEN GER_TRANSPORT_SHARE_SP,smooth_modal_share [REGIONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I], INITIAL_PASSENGER_TRANSPORT_DEMAND_SHARE[REGIONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I]+(RAMP((objective_passenger_transport_demand_modal_share [REGIONS 35 I,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I]-INITIAL_PASSENGER_TRANSPORT_DEMAND_SHARE[REGIONS 35 I ,TRANSPORT POWER TRAIN I,PASSENGERS TRANSPORT MODE I])/ (YEAR_FINAL_PASSENGER_TRANSPORT_SHARE_SP-YEAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP),Y EAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP ,YEAR_FINAL_PASSENGER_TRANSPORT_SHARE_SP))))) --EQ2-- IF_THEN_ELSE(SWITCH_MODEL_EXPLORER =1,model_explorer_passenger_transport_demand_modal_share[REGIONS_35_I,TRANS PORT_POWER_TRAIN_I ,PASSENGERS_TRANSPORT_MODE_I], IF_THEN_ELSE(SWITCH_PASSENGER_TRANSPORT_MODAL_SHARE_SP=0,INITIAL_PASSENGER_TRANSPORT_ DEMAND_SHARE[REGIONS_35_I,TRANSPORT_POWER_TRAIN_I ,PASSENGERS_TRANSPORT_MODE_I], IF_THEN_ELSE(SWITCH_PASSENGER_TRANSPORT_MODAL_SHARE_SP=1:AND:Time<YEAR_INITIAL_PASSEN GER_TRANSPORT_SHARE_SP,smooth_modal_share [REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PASSENGERS_TRANSPORT_MODE_I], PASSENGER_TRANSPORT_DEMAND_MODAL_SHARE_INITIAL_POLICY_YEAR[REGIONS_35_I,TRANSPORT_POW ER_TRAIN_I,PASSENGERS_TRANSPORT_MODE_I]+(RAMP((objective_passenger_transpor t_demand_modal_share [REGIONS_35_I,TRANSPORT_POWER_TRAIN_I,PASSENGERS_TRANSPORT_MODE_I]-PASSENGER_TRANSPOR T_DEMAND_MODAL_SHARE_INITIAL_POLICY_YEAR[REGIONS_35_I,TRANSPORT_POWER_TRAIN _I,PASSENGERS_TRANSPORT_MODE_I])/ (YEAR_FINAL_PASSENGER_TRANSPORT_SHARE_SP-YEAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP),Y EAR_INITIAL_PASSENGER_TRANSPORT_SHARE_SP ,YEAR_FINAL_PASSENGER_TRANSPORT_SHARE_SP)))))
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_passenger_transport_demand_modal_share(),
        lambda: if_then_else(
            switch_passenger_transport_modal_share_sp() == 0,
            lambda: passenger_transport_baseline(),
            lambda: passenger_transport_baseline()
            + ramp(
                __data["time"],
                (
                    target_passenger_transport_modal_share_by_power_train()
                    - passenger_transport_baseline()
                )
                / (
                    year_final_passenger_transport_share_sp()
                    - year_initial_passenger_transport_share_sp()
                ),
                year_initial_passenger_transport_share_sp(),
                year_final_passenger_transport_share_sp(),
            ),
        ),
    )


@component.add(
    name="passenger transport real supply",
    units="persons*km",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_vehicle_distance": 2,
        "load_factor_private_passenger_transport": 1,
        "private_passenger_vehicle_fleet": 1,
        "load_factor_public_passenger_transport": 1,
        "public_passenger_vehicle_fleet": 1,
    },
)
def passenger_transport_real_supply():
    """
    Transport supply by region, power train, transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
        * load_factor_private_passenger_transport()
        * private_passenger_vehicle_fleet()
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
        * load_factor_public_passenger_transport()
        * public_passenger_vehicle_fleet()
    ).values
    return value


@component.add(
    name="passenger transport real supply by mode",
    units="persons*km",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 1},
)
def passenger_transport_real_supply_by_mode():
    """
    Transport supply by region, transport mode and type of household after all policy and endogenous modifications, in persons*km.
    """
    return sum(
        passenger_transport_real_supply().rename(
            {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
        ),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="passengers by transport modes",
    units="person",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "load_factor_private_passenger_transport": 1,
        "passenger_fleet_demand": 2,
        "load_factor_public_passenger_transport": 1,
    },
)
def passengers_by_transport_modes():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        load_factor_private_passenger_transport()
        * passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"})
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        load_factor_public_passenger_transport()
        * passenger_fleet_demand()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"})
    ).values
    return value


@component.add(
    name="PRICE PER VEHCILE",
    units="$/vehicle",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_price_per_vehcile"},
)
def price_per_vehcile():
    return _ext_constant_price_per_vehcile()


_ext_constant_price_per_vehcile = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "CAPEX",
    "PRICE_PER_VEHICLE",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_price_per_vehcile",
)


@component.add(
    name="private passenger transport total distance traveled by transport mode",
    units="km/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 2,
        "public_passenger_vehicle_fleet": 1,
    },
)
def private_passenger_transport_total_distance_traveled_by_transport_mode():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"]] = (
        sum(
            private_passenger_vehicle_fleet().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        * sum(
            desired_passenger_vehicle_distance()
            .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["HOUSEHOLDS I!"],
        )
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"]] = (
        sum(
            public_passenger_vehicle_fleet().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        * sum(
            desired_passenger_vehicle_distance()
            .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["HOUSEHOLDS I!"],
        )
    ).values
    return value


@component.add(
    name="private passenger vehicle fleet",
    units="vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_private_passenger_vehicle_fleet": 1},
    other_deps={
        "_integ_private_passenger_vehicle_fleet": {
            "initial": {"initial_passenger_vehicle_fleet": 1},
            "step": {
                "new_passenger_private_vehicles": 1,
                "wear_passenger_private_vehicles": 1,
            },
        }
    },
)
def private_passenger_vehicle_fleet():
    """
    Private fleet stock by region, power train, private transport mode and type of household, in number of vehicles.
    """
    return _integ_private_passenger_vehicle_fleet()


_integ_private_passenger_vehicle_fleet = Integ(
    lambda: new_passenger_private_vehicles() - wear_passenger_private_vehicles(),
    lambda: initial_passenger_vehicle_fleet(),
    "_integ_private_passenger_vehicle_fleet",
)


@component.add(
    name="private vehicle fleet global growth rate",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "delayed_private_vehicle_fleet": 2,
    },
)
def private_vehicle_fleet_global_growth_rate():
    return zidz(
        sum(
            private_passenger_vehicle_fleet().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "PRIVATE TRANSPORT I": "PRIVATE TRANSPORT I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "PRIVATE TRANSPORT I!", "HOUSEHOLDS I!"],
        )
        - sum(
            delayed_private_vehicle_fleet().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "PRIVATE TRANSPORT I": "PRIVATE TRANSPORT I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "PRIVATE TRANSPORT I!", "HOUSEHOLDS I!"],
        ),
        sum(
            delayed_private_vehicle_fleet().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "PRIVATE TRANSPORT I": "PRIVATE TRANSPORT I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "PRIVATE TRANSPORT I!", "HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="private vehicle fleet growth rate",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "delayed_private_vehicle_fleet": 2,
    },
)
def private_vehicle_fleet_growth_rate():
    return zidz(
        sum(
            private_passenger_vehicle_fleet().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            - delayed_private_vehicle_fleet().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        ),
        sum(
            delayed_private_vehicle_fleet().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="private vehicle ownership",
    units="vehicles/kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "population_35_regions": 1,
        "unit_conversion_kpeople_people": 1,
    },
)
def private_vehicle_ownership():
    """
    Number of car ownership per 1000 persons.
    """
    return (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, :, "LDV", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
        )
        / population_35_regions()
        / unit_conversion_kpeople_people()
    )


@component.add(
    name="private vehicle ownership 9R",
    units="vehicles/kpeople",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 2,
        "population_9_regions": 2,
        "unit_conversion_kpeople_people": 2,
    },
)
def private_vehicle_ownership_9r():
    """
    private_vehicle_ownership_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        zidz(
            sum(
                private_passenger_vehicle_fleet()
                .loc[_subscript_dict["REGIONS 8 I"], :, "LDV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "REGIONS 35 I": "REGIONS 8 I",
                        "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
            ),
            population_9_regions()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 9 I": "REGIONS 8 I"}),
        )
        / unit_conversion_kpeople_people()
    ).values
    value.loc[["EU27"]] = (
        zidz(
            sum(
                private_passenger_vehicle_fleet()
                .loc[_subscript_dict["REGIONS EU27 I"], :, "LDV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "REGIONS 35 I": "REGIONS EU27 I!",
                        "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["REGIONS EU27 I!", "TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
            ),
            float(population_9_regions().loc["EU27"]),
        )
        / unit_conversion_kpeople_people()
    )
    return value


@component.add(
    name="public passenger vehicle fleet",
    units="vehicle",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_public_passenger_vehicle_fleet": 1},
    other_deps={
        "_integ_public_passenger_vehicle_fleet": {
            "initial": {"initial_public_passenger_vehicle_fleet": 1},
            "step": {
                "new_passenger_public_vehicles": 1,
                "wear_passenger_public_vehicles": 1,
            },
        }
    },
)
def public_passenger_vehicle_fleet():
    """
    Public fleet stock by region, power train, public transport mode and type of household, in number of vehicles. The fleet by type of households is a "virtual" fleet needee to satisfy teh public transport demand by type of household, it do not correspond to a real number of vehicles only used by each type of household.
    """
    return _integ_public_passenger_vehicle_fleet()


_integ_public_passenger_vehicle_fleet = Integ(
    lambda: new_passenger_public_vehicles() - wear_passenger_public_vehicles(),
    lambda: initial_public_passenger_vehicle_fleet(),
    "_integ_public_passenger_vehicle_fleet",
)


@component.add(
    name="real load factor",
    units="Year*person",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_real_supply": 1,
        "public_passenger_vehicle_fleet": 1,
        "desired_passenger_vehicle_distance": 1,
    },
)
def real_load_factor():
    return zidz(
        passenger_transport_real_supply()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        public_passenger_vehicle_fleet()
        * desired_passenger_vehicle_distance()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
    )


@component.add(
    name="reduction passenger transport demand",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_reduction_passenger_transport_demand": 1,
        "time": 2,
        "switch_reduction_passenger_transport_demand_sp": 2,
        "year_final_reduction_passenger_transport_demand_sp": 2,
        "year_initial_reduction_passenger_transport_demand_sp": 3,
        "objective_reduction_passenger_transport_demand_sp": 1,
    },
)
def reduction_passenger_transport_demand():
    """
    1+(RAMP((OBJECTIVE_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP[POWER TRAIN I,PASSENGERS TRANSPORT MODE I]-1)/ (YEAR_FINAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP-YEAR_INITIAL_REDUCTION_PASSENGER_ TRANSPORT_DEMAND_SP),YEAR_INITIAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP ,YEAR_FINAL_REDUCTION_PASSENGER_TRANSPORT_DEMAND_SP))
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_reduction_passenger_transport_demand().expand_dims(
            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 2
        ),
        lambda: if_then_else(
            switch_reduction_passenger_transport_demand_sp() == 0,
            lambda: xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                        "PASSENGERS TRANSPORT MODE I"
                    ],
                },
                ["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_reduction_passenger_transport_demand_sp() == 1,
                    time() < year_initial_reduction_passenger_transport_demand_sp(),
                ),
                lambda: xr.DataArray(
                    1,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                            "PASSENGERS TRANSPORT MODE I"
                        ],
                    },
                    ["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
                ),
                lambda: 1
                + ramp(
                    __data["time"],
                    (objective_reduction_passenger_transport_demand_sp() - 1)
                    / (
                        year_final_reduction_passenger_transport_demand_sp()
                        - year_initial_reduction_passenger_transport_demand_sp()
                    ),
                    year_initial_reduction_passenger_transport_demand_sp(),
                    year_final_reduction_passenger_transport_demand_sp(),
                ),
            ),
        )
        .transpose("PASSENGERS TRANSPORT MODE I", "REGIONS 35 I")
        .expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 0
        ),
    ).transpose(
        "REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"
    )


@component.add(
    name="share BEV BUS",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trend_bev_bus": 1,
        "delayed_ts_price_output": 2,
        "sigma_fuel_bus": 1,
        "initial_price_of_output": 2,
        "sigma_elect_bus": 1,
    },
)
def share_bev_bus():
    """
    Share of battery electric buses
    """
    return np.exp(
        trend_bev_bus()
        + sigma_fuel_bus()
        * np.log(
            zidz(
                delayed_ts_price_output().loc[:, "REFINING"].reset_coords(drop=True),
                initial_price_of_output(),
            )
        )
        + sigma_elect_bus()
        * np.log(
            zidz(
                delayed_ts_price_output()
                .loc[:, "DISTRIBUTION ELECTRICITY"]
                .reset_coords(drop=True),
                initial_price_of_output(),
            )
        )
    )


@component.add(
    name="share BEV LDV",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trend_bev_ldv": 1,
        "initial_price_coicop": 2,
        "sigma_fuel_ldv": 1,
        "price_coicop": 2,
        "sigma_elect_ldv": 1,
    },
)
def share_bev_ldv():
    """
    Share of battery electric light duty vehicles
    """
    return np.exp(
        trend_bev_ldv()
        + sigma_fuel_ldv()
        * np.log(
            zidz(
                price_coicop().loc[:, "HH FUEL TRANSPORT"].reset_coords(drop=True),
                initial_price_coicop()
                .loc[:, "HH FUEL TRANSPORT"]
                .reset_coords(drop=True),
            )
        )
        + sigma_elect_ldv()
        * np.log(
            zidz(
                price_coicop().loc[:, "HH ELECTRICITY"].reset_coords(drop=True),
                initial_price_coicop().loc[:, "HH ELECTRICITY"].reset_coords(drop=True),
            )
        )
    )


@component.add(
    name="share consumption for private transport electricity",
    units="1",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_transport_real": 1,
        "households_consumption_coicop_real": 1,
    },
)
def share_consumption_for_private_transport_electricity():
    return zidz(
        households_consumption_transport_real()
        .loc[:, :, "HH ELECTRICITY"]
        .reset_coords(drop=True),
        sum(
            households_consumption_coicop_real().rename({"COICOP I": "COICOP I!"}),
            dim=["COICOP I!"],
        ),
    )


@component.add(
    name="share consumption for private transport gas",
    units="1",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_transport_real": 1,
        "households_consumption_coicop_real": 1,
    },
)
def share_consumption_for_private_transport_gas():
    return zidz(
        households_consumption_transport_real()
        .loc[:, :, "HH GAS"]
        .reset_coords(drop=True),
        sum(
            households_consumption_coicop_real().rename({"COICOP I": "COICOP I!"}),
            dim=["COICOP I!"],
        ),
    )


@component.add(
    name="share consumption for private transport liquids",
    units="1",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_consumption_transport_real": 1,
        "households_consumption_coicop_real": 1,
    },
)
def share_consumption_for_private_transport_liquids():
    return zidz(
        households_consumption_transport_real()
        .loc[:, :, "HH FUEL TRANSPORT"]
        .reset_coords(drop=True),
        sum(
            households_consumption_coicop_real().rename({"COICOP I": "COICOP I!"}),
            dim=["COICOP I!"],
        ),
    )


@component.add(
    name="share LD RAIL",
    units="DMML",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "desired_passenger_transport_demand_by_mode_and_power_train": 2,
        "initial_rail_c": 1,
        "initial_rail_md": 1,
    },
)
def share_ld_rail():
    """
    Share of LD TRAIN
    """
    return zidz(
        sum(
            desired_passenger_transport_demand_by_mode_and_power_train()
            .loc["SPAIN", :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        )
        - initial_rail_c()
        - initial_rail_md(),
        sum(
            desired_passenger_transport_demand_by_mode_and_power_train()
            .loc["SPAIN", :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
    )


@component.add(
    name="share MD RAIL",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_rail_c": 1,
        "desired_passenger_transport_demand_by_mode_and_power_train": 1,
    },
)
def share_md_rail():
    return zidz(
        initial_rail_c(),
        sum(
            desired_passenger_transport_demand_by_mode_and_power_train()
            .loc["SPAIN", :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
    )


@component.add(
    name="share new vehicles acquisition vs GDP",
    units="Mdollars/Mdollars 2015",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cost_of_new_vehicles_acquisition": 1,
        "unit_conversion_dollars_mdollars": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def share_new_vehicles_acquisition_vs_gdp():
    return zidz(
        cost_of_new_vehicles_acquisition() / unit_conversion_dollars_mdollars(),
        gross_domestic_product_real_supply_side()
        .expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 1
        )
        .expand_dims(
            {
                "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                    "PASSENGERS TRANSPORT MODE I"
                ]
            },
            2,
        )
        .expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3),
    )


@component.add(
    name="share passenger transport demand by region and type of household",
    units="1",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_passenger_transport_demand_by_region_and_type_of_household": 1,
        "total_passenger_transport_demand_by_region": 1,
    },
)
def share_passenger_transport_demand_by_region_and_type_of_household():
    return zidz(
        total_passenger_transport_demand_by_region_and_type_of_household(),
        total_passenger_transport_demand_by_region().expand_dims(
            {"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1
        ),
    )


@component.add(
    name="share technologies passenger transport",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_technologies_passenger_transport_exc_fuel_adjusted": 5,
        "split_gasoline_diesel_passanger_transport": 4,
    },
)
def share_technologies_passenger_transport():
    """
    Shares technologies in passanger transport by mode
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["ICE gasoline"], ["LDV"]] = False
    except_subs.loc[:, ["ICE diesel"], ["LDV"]] = False
    except_subs.loc[:, ["ICE gasoline"], ["BUS"]] = False
    except_subs.loc[:, ["ICE diesel"], ["BUS"]] = False
    value.values[
        except_subs.values
    ] = share_technologies_passenger_transport_exc_fuel_adjusted().values[
        except_subs.values
    ]
    value.loc[:, ["ICE gasoline"], ["LDV"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE gasoline", "LDV"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passenger_transport_exc_fuel_adjusted()
                    .loc[:, :, "LDV"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
                    dim=["TRANSPORT POWER TRAIN I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE gasoline"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE diesel"], ["LDV"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE diesel", "LDV"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passenger_transport_exc_fuel_adjusted()
                    .loc[:, :, "LDV"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
                    dim=["TRANSPORT POWER TRAIN I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE diesel"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE gasoline"], ["BUS"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE gasoline", "BUS"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passenger_transport_exc_fuel_adjusted()
                    .loc[:, :, "BUS"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
                    dim=["TRANSPORT POWER TRAIN I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE gasoline"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["ICE diesel"], ["BUS"]] = (
        (
            split_gasoline_diesel_passanger_transport()
            .loc[:, "ICE diesel", "BUS"]
            .reset_coords(drop=True)
            * (
                1
                - sum(
                    share_technologies_passenger_transport_exc_fuel_adjusted()
                    .loc[:, :, "BUS"]
                    .reset_coords(drop=True)
                    .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
                    dim=["TRANSPORT POWER TRAIN I!"],
                )
            )
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE diesel"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    return value


@component.add(
    name="share technologies passenger transport exc fuel",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "base_share_technologies_passenger_transport": 1,
        "share_bev_bus": 1,
        "share_bev_ldv": 1,
    },
)
def share_technologies_passenger_transport_exc_fuel():
    """
    Shares technologies in passanger transport by mode, exclunding gasoline and diesel
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["BUS"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["ICE gasoline"], ["LDV"]] = False
    except_subs.loc[:, ["ICE diesel"], ["LDV"]] = False
    except_subs.loc[:, ["ICE gasoline"], ["BUS"]] = False
    except_subs.loc[:, ["ICE diesel"], ["BUS"]] = False
    value.values[except_subs.values] = (
        base_share_technologies_passenger_transport().values[except_subs.values]
    )
    value.loc[:, ["BEV"], ["BUS"]] = (
        share_bev_bus()
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        share_bev_ldv()
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["ICE gasoline"], ["LDV"]] = 0
    value.loc[:, ["ICE diesel"], ["LDV"]] = 0
    value.loc[:, ["ICE gasoline"], ["BUS"]] = 0
    value.loc[:, ["ICE diesel"], ["BUS"]] = 0
    return value


@component.add(
    name="share technologies passenger transport exc fuel adjusted",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_technologies_passenger_transport_exc_fuel": 4},
)
def share_technologies_passenger_transport_exc_fuel_adjusted():
    """
    Shares technologies adjsuted when > 1
    """
    return if_then_else(
        (
            sum(
                share_technologies_passenger_transport_exc_fuel().rename(
                    {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                ),
                dim=["TRANSPORT POWER TRAIN I!"],
            )
            > 1
        ).expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 2
        ),
        lambda: zidz(
            share_technologies_passenger_transport_exc_fuel(),
            sum(
                share_technologies_passenger_transport_exc_fuel().rename(
                    {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
                ),
                dim=["TRANSPORT POWER TRAIN I!"],
            ).expand_dims(
                {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]},
                1,
            ),
        ).transpose(
            "REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "TRANSPORT POWER TRAIN I"
        ),
        lambda: share_technologies_passenger_transport_exc_fuel().transpose(
            "REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "TRANSPORT POWER TRAIN I"
        ),
    ).transpose(
        "REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"
    )


@component.add(
    name="share urban Vs interurban",
    units="1",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buses_transport_demand_urban": 1,
        "passenger_transport_real_supply": 1,
    },
)
def share_urban_vs_interurban():
    return zidz(
        buses_transport_demand_urban(),
        sum(
            passenger_transport_real_supply()
            .loc[:, :, "BUS", :]
            .reset_coords(drop=True)
            .rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="share urban Vs rural",
    units="1",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ldv_transport_demand_dense_hh": 1,
        "passenger_transport_real_supply": 1,
    },
)
def share_urban_vs_rural():
    return zidz(
        ldv_transport_demand_dense_hh(),
        sum(
            passenger_transport_real_supply().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="SIGMA ELECT BUS",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sigma_elect_bus"},
)
def sigma_elect_bus():
    """
    Sigma electricity LDV
    """
    return _ext_constant_sigma_elect_bus()


_ext_constant_sigma_elect_bus = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "endogenize_transport_share",
    "SIGMA_ELECT_BUS",
    {},
    _root,
    {},
    "_ext_constant_sigma_elect_bus",
)


@component.add(
    name="SIGMA ELECT LDV",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sigma_elect_ldv"},
)
def sigma_elect_ldv():
    """
    Sigma electricity LDV
    """
    return _ext_constant_sigma_elect_ldv()


_ext_constant_sigma_elect_ldv = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "endogenize_transport_share",
    "SIGMA_ELECT_LDV",
    {},
    _root,
    {},
    "_ext_constant_sigma_elect_ldv",
)


@component.add(
    name="SIGMA FUEL BUS",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sigma_fuel_bus"},
)
def sigma_fuel_bus():
    """
    Sigma fuel LDV
    """
    return _ext_constant_sigma_fuel_bus()


_ext_constant_sigma_fuel_bus = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "endogenize_transport_share",
    "SIGMA_FUEL_BUS",
    {},
    _root,
    {},
    "_ext_constant_sigma_fuel_bus",
)


@component.add(
    name="SIGMA FUEL LDV",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sigma_fuel_ldv"},
)
def sigma_fuel_ldv():
    """
    Sigma fuel LDV
    """
    return _ext_constant_sigma_fuel_ldv()


_ext_constant_sigma_fuel_ldv = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "endogenize_transport_share",
    "SIGMA_FUEL_LDV",
    {},
    _root,
    {},
    "_ext_constant_sigma_fuel_ldv",
)


@component.add(
    name="SIGMA PUBLIC TRANSPORT",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_sigma_public_transport"},
)
def sigma_public_transport():
    return _ext_constant_sigma_public_transport()


_ext_constant_sigma_public_transport = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "endogenize_transport_share",
    "SIGMA_PUBLIC_TRANSPORT",
    {},
    _root,
    {},
    "_ext_constant_sigma_public_transport",
)


@component.add(
    name="smooth desired passenger vehicle distance",
    units="km/(Year*vehicle)",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_desired_passenger_vehicle_distance": 1},
    other_deps={
        "_smooth_smooth_desired_passenger_vehicle_distance": {
            "initial": {"initial_passengers_vehicle_distance": 1},
            "step": {"desired_passenger_vehicle_distance": 1},
        }
    },
)
def smooth_desired_passenger_vehicle_distance():
    return _smooth_smooth_desired_passenger_vehicle_distance()


_smooth_smooth_desired_passenger_vehicle_distance = Smooth(
    lambda: desired_passenger_vehicle_distance(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    ),
    lambda: initial_passengers_vehicle_distance().expand_dims(
        {"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 3
    ),
    lambda: 1,
    "_smooth_smooth_desired_passenger_vehicle_distance",
)


@component.add(
    name="smooth lifetime passengers vehicles",
    units="Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_lifetime_passengers_vehicles": 1},
    other_deps={
        "_smooth_smooth_lifetime_passengers_vehicles": {
            "initial": {"lifetime_passenger_vehicles": 1},
            "step": {"lifetime_passenger_vehicles": 1},
        }
    },
)
def smooth_lifetime_passengers_vehicles():
    return _smooth_smooth_lifetime_passengers_vehicles()


_smooth_smooth_lifetime_passengers_vehicles = Smooth(
    lambda: lifetime_passenger_vehicles(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "HOUSEHOLDS I",
        ],
    ),
    lambda: lifetime_passenger_vehicles(),
    lambda: 1,
    "_smooth_smooth_lifetime_passengers_vehicles",
)


@component.add(
    name="smooth wear passenger private vehicles mod factor",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_wear_passenger_private_vehicles_mod_factor": 1},
    other_deps={
        "_smooth_smooth_wear_passenger_private_vehicles_mod_factor": {
            "initial": {"wear_passenger_private_vehicles_mod_factor": 1},
            "step": {"wear_passenger_private_vehicles_mod_factor": 1},
        }
    },
)
def smooth_wear_passenger_private_vehicles_mod_factor():
    return _smooth_smooth_wear_passenger_private_vehicles_mod_factor()


_smooth_smooth_wear_passenger_private_vehicles_mod_factor = Smooth(
    lambda: wear_passenger_private_vehicles_mod_factor(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PRIVATE TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    ),
    lambda: wear_passenger_private_vehicles_mod_factor(),
    lambda: 1,
    "_smooth_smooth_wear_passenger_private_vehicles_mod_factor",
)


@component.add(
    name="smooth wear passenger public vehicles mod factor",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"_smooth_smooth_wear_passenger_public_vehicles_mod_factor": 1},
    other_deps={
        "_smooth_smooth_wear_passenger_public_vehicles_mod_factor": {
            "initial": {"wear_passenger_public_vehicles_mod_factor": 1},
            "step": {"wear_passenger_public_vehicles_mod_factor": 1},
        }
    },
)
def smooth_wear_passenger_public_vehicles_mod_factor():
    return _smooth_smooth_wear_passenger_public_vehicles_mod_factor()


_smooth_smooth_wear_passenger_public_vehicles_mod_factor = Smooth(
    lambda: wear_passenger_public_vehicles_mod_factor(),
    lambda: xr.DataArray(
        2,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PUBLIC TRANSPORT I",
            "HOUSEHOLDS I",
        ],
    ),
    lambda: wear_passenger_public_vehicles_mod_factor(),
    lambda: 1,
    "_smooth_smooth_wear_passenger_public_vehicles_mod_factor",
)


@component.add(
    name="split gasoline diesel passanger transport",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passenger_transport": 6},
)
def split_gasoline_diesel_passanger_transport():
    """
    Split gasoline and diesel
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["ICE gasoline"], :] = False
    except_subs.loc[:, ["ICE diesel"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["ICE gasoline"], :] = (
        zidz(
            base_share_technologies_passenger_transport()
            .loc[:, "ICE gasoline", :]
            .reset_coords(drop=True),
            base_share_technologies_passenger_transport()
            .loc[:, "ICE gasoline", :]
            .reset_coords(drop=True)
            + base_share_technologies_passenger_transport()
            .loc[:, "ICE diesel", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE gasoline"]}, 1)
        .values
    )
    value.loc[:, ["ICE diesel"], :] = (
        zidz(
            base_share_technologies_passenger_transport()
            .loc[:, "ICE diesel", :]
            .reset_coords(drop=True),
            base_share_technologies_passenger_transport()
            .loc[:, "ICE gasoline", :]
            .reset_coords(drop=True)
            + base_share_technologies_passenger_transport()
            .loc[:, "ICE diesel", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE diesel"]}, 1)
        .values
    )
    return value


@component.add(
    name="subshare bus",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_modal_share_by_power_train": 3},
)
def subshare_bus():
    return zidz(
        sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "BUS"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
        sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        )
        + sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "BUS"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
    )


@component.add(
    name="subshare rail",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_modal_share_by_power_train": 3},
)
def subshare_rail():
    """
    Share of rail over total bublic transportation
    """
    return zidz(
        sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
        sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        )
        + sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "BUS"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        ),
    )


@component.add(
    name="SWITCH NRG DYNAMIC TRANSPORT DEMAND",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_dynamic_transport_demand"},
)
def switch_nrg_dynamic_transport_demand():
    """
    =1 the model runs with passenger transport demand dinamically modified by the GDPpc and 1 type of HH =0 the model runs with static input passenger transport demand and 1 type of HH
    """
    return _ext_constant_switch_nrg_dynamic_transport_demand()


_ext_constant_switch_nrg_dynamic_transport_demand = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_DYNAMIC_TRANSPORT_DEMAND",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_dynamic_transport_demand",
)


@component.add(
    name="SWITCH NRG HH TRANSPORT DISAGGREGATED",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_hh_transport_disaggregated"},
)
def switch_nrg_hh_transport_disaggregated():
    """
    This switch can take two values: 0: the passenger transport module runs with 1 type of HH aggregated in REPRESENTATIVE HH subscript. 1: the passenger transport module runs disaggregated in 61 type of HH.
    """
    return _ext_constant_switch_nrg_hh_transport_disaggregated()


_ext_constant_switch_nrg_hh_transport_disaggregated = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_HH_TRANSPORT_DISAGGREGATED",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_hh_transport_disaggregated",
)


@component.add(
    name="TARGET PASSENGER TRANSPORT MODAL SHARE BY POWER TRAIN",
    units="DMML",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_passenger_transport_modal_share_by_region_sp": 1,
        "target_power_train_share_by_passenger_transport_mode_sp": 1,
    },
)
def target_passenger_transport_modal_share_by_power_train():
    """
    Target passenger transport modal share by power train and region.
    """
    return (
        target_passenger_transport_modal_share_by_region_sp()
        * target_power_train_share_by_passenger_transport_mode_sp().transpose(
            "REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "TRANSPORT POWER TRAIN I"
        )
    ).transpose(
        "REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"
    )


@component.add(
    name="TARGET PASSENGER TRANSPORT MODAL SHARE BY REGION SP",
    units="DMML",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_passenger_transport_modal_share_by_region_sp"
    },
)
def target_passenger_transport_modal_share_by_region_sp():
    """
    Transport passenger modal share by region. Shares total 1 for each country.
    """
    return _ext_constant_target_passenger_transport_modal_share_by_region_sp()


_ext_constant_target_passenger_transport_modal_share_by_region_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_PASSENGER_TRANSPORT_MODAL_SHARE_BY_REGION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_target_passenger_transport_modal_share_by_region_sp",
)


@component.add(
    name="TARGET POWER TRAIN SHARE BY PASSENGER TRANSPORT MODE SP",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_power_train_share_by_passenger_transport_mode_sp"
    },
)
def target_power_train_share_by_passenger_transport_mode_sp():
    """
    Target passenger transport by power train, transport mode and region. Each share totals 1 for each transport mode.
    """
    return _ext_constant_target_power_train_share_by_passenger_transport_mode_sp()


_ext_constant_target_power_train_share_by_passenger_transport_mode_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_target_power_train_share_by_passenger_transport_mode_sp",
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_target_power_train_share_by_passenger_transport_mode_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "TARGET_POWER_TRAIN_SHARE_BY_PASSENGER_TRANSPORT_MODE_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="total energy consumption passenger transport",
    units="EJ",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def total_energy_consumption_passenger_transport():
    """
    Total energy passengers transport consumption by type of final energy in EJ.
    """
    return (
        sum(
            energy_passenger_transport_consumption_by_fe_35r().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 I!",
                    "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["REGIONS 35 I!", "PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
        )
        / unit_conversion_mj_ej()
    )


@component.add(
    name="total new number EV vehicles",
    units="vehicles",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "new_passenger_public_vehicles": 1,
        "new_passenger_private_vehicles": 2,
    },
)
def total_new_number_ev_vehicles():
    """
    New number of EV vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    )
    value.loc[:, ["BEV"], ["MDV"]] = 0
    value.loc[:, ["BEV"], ["BUS"]] = (
        sum(
            new_passenger_public_vehicles()
            .loc[:, "BEV", "BUS", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = (
        sum(
            new_passenger_private_vehicles()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["MDV"]] = False
    except_subs.loc[:, ["BEV"], ["BUS"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total number electrified vehicles",
    units="vehicles",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "TRANSPORT MODE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 6,
        "public_passenger_vehicle_fleet": 3,
    },
)
def total_number_electrified_vehicles():
    """
    number_of_electrified_vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "TRANSPORT MODE I": _subscript_dict["TRANSPORT MODE I"],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "TRANSPORT MODE I"],
    )
    value.loc[:, ["HEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["HEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["HEV"], ["MOTORCYCLES 2W 3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["HEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "PHEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["MOTORCYCLES 2W 3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "HEV", "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    value.loc[:, ["HEV"], ["BUS"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "HEV", "BUS", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["HEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["PHEV"], ["BUS"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "PHEV", "BUS", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["BUS"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "BEV", "BUS", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["HEV"], ["LDV"]] = False
    except_subs.loc[:, ["HEV"], ["MOTORCYCLES 2W 3W"]] = False
    except_subs.loc[:, ["PHEV"], ["LDV"]] = False
    except_subs.loc[:, ["PHEV"], ["MOTORCYCLES 2W 3W"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = False
    except_subs.loc[:, ["HEV"], ["BUS"]] = False
    except_subs.loc[:, ["PHEV"], ["BUS"]] = False
    except_subs.loc[:, ["BEV"], ["BUS"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total number EV vehicles",
    units="vehicles",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_passenger_vehicle_fleet": 1,
        "private_passenger_vehicle_fleet": 2,
    },
)
def total_number_ev_vehicles():
    """
    number of EV vehicles
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "BATTERY VEHICLES I": _subscript_dict["BATTERY VEHICLES I"],
        },
        ["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    )
    value.loc[:, ["BEV"], ["MDV"]] = 0
    value.loc[:, ["BEV"], ["BUS"]] = (
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "BEV", "BUS", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["BUS"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["LDV"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "LDV", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["LDV"]}, 2)
        .values
    )
    value.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = (
        sum(
            private_passenger_vehicle_fleet()
            .loc[:, "BEV", "MOTORCYCLES 2W 3W", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"BATTERY VEHICLES I": ["MOTORCYCLES 2W 3W"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["BEV"], ["MDV"]] = False
    except_subs.loc[:, ["BEV"], ["BUS"]] = False
    except_subs.loc[:, ["BEV"], ["LDV"]] = False
    except_subs.loc[:, ["BEV"], ["MOTORCYCLES 2W 3W"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="total passenger transport cumulated GHG emissions",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_total_passenger_transport_cumulated_ghg_emissions": 1},
    other_deps={
        "_integ_total_passenger_transport_cumulated_ghg_emissions": {
            "initial": {"initial_passengers_transport_ghg_emissions": 1},
            "step": {"passenger_transport_ghg_emissions": 1},
        }
    },
)
def total_passenger_transport_cumulated_ghg_emissions():
    return _integ_total_passenger_transport_cumulated_ghg_emissions()


_integ_total_passenger_transport_cumulated_ghg_emissions = Integ(
    lambda: passenger_transport_ghg_emissions(),
    lambda: initial_passengers_transport_ghg_emissions(),
    "_integ_total_passenger_transport_cumulated_ghg_emissions",
)


@component.add(
    name="total passenger transport demand",
    units="km*person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply": 1},
)
def total_passenger_transport_demand():
    """
    Transport demand by region.
    """
    return sum(
        passenger_transport_real_supply().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=[
            "TRANSPORT POWER TRAIN I!",
            "PASSENGERS TRANSPORT MODE I!",
            "HOUSEHOLDS I!",
        ],
    )


@component.add(
    name="total passenger transport demand by region",
    units="km*person",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand_by_region_and_type_of_household": 1},
)
def total_passenger_transport_demand_by_region():
    return sum(
        total_passenger_transport_demand_by_region_and_type_of_household().rename(
            {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="total passenger transport demand by region and type of household",
    units="km*person",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_hh_transport_disaggregated": 1,
        "passenger_transport_demand_corrected_by_gdppc": 1,
        "desired_transport_demand": 1,
        "switch_energy": 1,
        "exo_total_transport_demand_by_region_and_type_of_hh": 1,
    },
)
def total_passenger_transport_demand_by_region_and_type_of_household():
    """
    total transport demand comes from standalone part if SWITCH HH TRANSPORT DISAGREGATED=0, if SWITCH ENERGY=0 o SWITCH ECO HH TRANSPORT ENERGY BOTTOM UP=0 then transport demand comes from EXO transport demand variable in other case the transport demand comes from the economy transport demand variable.
    """
    return if_then_else(
        switch_nrg_hh_transport_disaggregated() == 0,
        lambda: passenger_transport_demand_corrected_by_gdppc(),
        lambda: if_then_else(
            switch_energy() == 0,
            lambda: exo_total_transport_demand_by_region_and_type_of_hh(),
            lambda: desired_transport_demand(),
        ),
    )


@component.add(
    name="total passenger transport energy consumption by region",
    units="MJ",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption_by_fe_35r": 1},
)
def total_passenger_transport_energy_consumption_by_region():
    """
    Energy consumption by the passenger transport by region.
    """
    return sum(
        energy_passenger_transport_consumption_by_fe_35r().rename(
            {
                "NRG FE I": "NRG FE I!",
                "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=["NRG FE I!", "PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="total passengers transport modes",
    units="person",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passengers_by_transport_modes": 1},
)
def total_passengers_transport_modes():
    return sum(
        passengers_by_transport_modes().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="total private passenger vehicle fleet",
    units="vehicles",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"private_passenger_vehicle_fleet": 1},
)
def total_private_passenger_vehicle_fleet():
    return (
        private_passenger_vehicle_fleet()
        .loc[:, :, :, "REPRESENTATIVE HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="total public passenger vehicle fleet",
    units="vehicles",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def total_public_passenger_vehicle_fleet():
    return (
        public_passenger_vehicle_fleet()
        .loc[:, :, :, "REPRESENTATIVE HOUSEHOLD"]
        .reset_coords(drop=True)
    )


@component.add(
    name="total share consumption private transport",
    units="1",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_consumption_for_private_transport_electricity": 1,
        "share_consumption_for_private_transport_gas": 1,
        "share_consumption_for_private_transport_liquids": 1,
    },
)
def total_share_consumption_private_transport():
    return (
        share_consumption_for_private_transport_electricity()
        + share_consumption_for_private_transport_gas()
        + share_consumption_for_private_transport_liquids()
    )


@component.add(
    name="total sum passenger transport demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand_by_region_and_type_of_household": 1},
)
def total_sum_passenger_transport_demand():
    return sum(
        total_passenger_transport_demand_by_region_and_type_of_household().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="traffic volume per capita",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand": 1, "population_35_regions": 1},
)
def traffic_volume_per_capita():
    """
    Number of kilometers traveled per inhabitant per year.
    """
    return zidz(total_passenger_transport_demand(), population_35_regions())


@component.add(
    name="trend BEV BUS",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passenger_transport": 2},
)
def trend_bev_bus():
    """
    Constant BEV BUS
    """
    return if_then_else(
        base_share_technologies_passenger_transport()
        .loc[:, "BEV", "BUS"]
        .reset_coords(drop=True)
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: np.log(
            base_share_technologies_passenger_transport()
            .loc[:, "BEV", "BUS"]
            .reset_coords(drop=True)
        ),
    )


@component.add(
    name="trend BEV LDV",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"base_share_technologies_passenger_transport": 2},
)
def trend_bev_ldv():
    """
    Constant BEV LDV
    """
    return if_then_else(
        base_share_technologies_passenger_transport()
        .loc[:, "BEV", "LDV"]
        .reset_coords(drop=True)
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: np.log(
            base_share_technologies_passenger_transport()
            .loc[:, "BEV", "LDV"]
            .reset_coords(drop=True)
        ),
    )


@component.add(
    name="trend modal split public",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_modal_share_by_power_train": 4},
)
def trend_modal_split_public():
    """
    Constant public transportation
    """
    return if_then_else(
        sum(
            passenger_transport_modal_share_by_power_train()
            .loc[:, :, "BUS"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
            + passenger_transport_modal_share_by_power_train()
            .loc[:, :, "RAIL"]
            .reset_coords(drop=True)
            .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
            dim=["TRANSPORT POWER TRAIN I!"],
        )
        == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: np.log(
            sum(
                passenger_transport_modal_share_by_power_train()
                .loc[:, :, "BUS"]
                .reset_coords(drop=True)
                .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"})
                + passenger_transport_modal_share_by_power_train()
                .loc[:, :, "RAIL"]
                .reset_coords(drop=True)
                .rename({"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}),
                dim=["TRANSPORT POWER TRAIN I!"],
            )
        ),
    )


@component.add(
    name="variation load factor passenger transport",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "new_passenger_public_vehicles": 4,
        "occupancy_rate": 7,
        "load_factor_public_passenger_transport": 4,
    },
)
def variation_load_factor_passenger_transport():
    """
    IF_THEN_ELSE(occupancy_rate[REGIONS 35 I,TRANSPORT POWER TRAIN I,PUBLIC TRANSPORT I,HOUSEHOLDS I]<0.5, occupancy_factor[REGIONS 35 I,TRANSPORT POWER TRAIN I,PUBLIC TRANSPORT I,HOUSEHOLDS I]*0.02, IF_THEN_ELSE(occupancy_rate[REGIONS 35 I,TRANSPORT POWER TRAIN I,PUBLIC TRANSPORT I,HOUSEHOLDS I]>0.5:AND:occupancy_rate [REGIONS 35 I,TRANSPORT POWER TRAIN I,PUBLIC TRANSPORT I,HOUSEHOLDS I]<0.75, occupancy_factor[REGIONS 35 I,TRANSPORT POWER TRAIN I,PUBLIC TRANSPORT I,HOUSEHOLDS I]*0.01, 0))
    """
    return if_then_else(
        np.logical_and(new_passenger_public_vehicles() > 20, occupancy_rate() < 0.75),
        lambda: load_factor_public_passenger_transport() * 0.2,
        lambda: if_then_else(
            np.logical_and(
                new_passenger_public_vehicles() > 20,
                np.logical_and(occupancy_rate() > 0.75, occupancy_rate() < 0.8),
            ),
            lambda: load_factor_public_passenger_transport() * 0.1,
            lambda: if_then_else(
                np.logical_and(
                    new_passenger_public_vehicles() > 20,
                    np.logical_and(occupancy_rate() > 0.8, occupancy_rate() < 0.9),
                ),
                lambda: load_factor_public_passenger_transport() * 0.05,
                lambda: if_then_else(
                    np.logical_and(
                        new_passenger_public_vehicles() > 20,
                        np.logical_and(occupancy_rate() > 0.9, occupancy_rate() < 0.95),
                    ),
                    lambda: load_factor_public_passenger_transport() * 0.025,
                    lambda: xr.DataArray(
                        0.01,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "TRANSPORT POWER TRAIN I": _subscript_dict[
                                "TRANSPORT POWER TRAIN I"
                            ],
                            "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
                            "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
                        },
                        [
                            "REGIONS 35 I",
                            "TRANSPORT POWER TRAIN I",
                            "PUBLIC TRANSPORT I",
                            "HOUSEHOLDS I",
                        ],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="wear passenger private vehicles",
    units="vehicle/Years",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_vehicle_fleet": 1,
        "smooth_lifetime_passengers_vehicles": 1,
        "smooth_wear_passenger_private_vehicles_mod_factor": 1,
    },
)
def wear_passenger_private_vehicles():
    """
    Private vehicle scrapping flow in vehicles/year
    """
    return (
        zidz(
            private_passenger_vehicle_fleet(),
            smooth_lifetime_passengers_vehicles()
            .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I"}),
        )
        * smooth_wear_passenger_private_vehicles_mod_factor()
    )


@component.add(
    name="wear passenger private vehicles mod factor",
    units="1",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PRIVATE TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_private_vehicles": 1, "time": 1},
)
def wear_passenger_private_vehicles_mod_factor():
    """
    Factor that modifies the wear passenger private vehicles when the flow of new vehicles goes to 0.
    """
    return if_then_else(
        np.logical_and(new_passenger_private_vehicles() == 0, time() > 2005),
        lambda: xr.DataArray(
            2,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PRIVATE TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PRIVATE TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
    )


@component.add(
    name="wear passenger public vehicles",
    units="vehicles/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "public_passenger_vehicle_fleet": 1,
        "smooth_lifetime_passengers_vehicles": 1,
        "smooth_wear_passenger_public_vehicles_mod_factor": 1,
    },
)
def wear_passenger_public_vehicles():
    """
    Public vehicle scrapping flow in vehicles/year.
    """
    return (
        zidz(
            public_passenger_vehicle_fleet(),
            smooth_lifetime_passengers_vehicles()
            .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
            .rename({"PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I"}),
        )
        * smooth_wear_passenger_public_vehicles_mod_factor()
    )


@component.add(
    name="wear passenger public vehicles mod factor",
    units="1",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PUBLIC TRANSPORT I",
        "HOUSEHOLDS I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"new_passenger_public_vehicles": 1, "time": 1},
)
def wear_passenger_public_vehicles_mod_factor():
    return if_then_else(
        np.logical_and(new_passenger_public_vehicles() == 0, time() > 2005),
        lambda: xr.DataArray(
            2,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PUBLIC TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
                "HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"],
            },
            [
                "REGIONS 35 I",
                "TRANSPORT POWER TRAIN I",
                "PUBLIC TRANSPORT I",
                "HOUSEHOLDS I",
            ],
        ),
    )


@component.add(
    name="world total passenger transport demand",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_passenger_transport_demand": 1},
)
def world_total_passenger_transport_demand():
    """
    Total world transport demand.
    """
    return sum(
        total_passenger_transport_demand().rename({"REGIONS 35 I": "REGIONS 35 I!"}),
        dim=["REGIONS 35 I!"],
    )
