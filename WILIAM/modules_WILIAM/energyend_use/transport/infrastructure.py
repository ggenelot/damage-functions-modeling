"""
Module energyend_use.transport.infrastructure
Translated using PySD version 3.14.0
"""

@component.add(
    name="capacity EV chargers",
    units="TW",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capacity_per_ev_charger": 1,
        "number_ev_chargers_by_type": 1,
        "unit_conversion_tw_kw": 1,
    },
)
def capacity_ev_chargers():
    """
    Total capacity in MW of the different types of EVchargers installed
    """
    return (
        capacity_per_ev_charger()
        * number_ev_chargers_by_type().transpose("EV CHARGERS I", "REGIONS 35 I")
        * unit_conversion_tw_kw()
    ).transpose("REGIONS 35 I", "EV CHARGERS I")


@component.add(
    name="initial railway catenary length",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_railway_tracks_length": 1,
        "share_electrified_rails_vs_train_activity": 1,
    },
)
def initial_railway_catenary_length():
    """
    initial length of railway catenary
    """
    return initial_railway_tracks_length() * share_electrified_rails_vs_train_activity()


@component.add(
    name="length grid to EV chargers",
    units="km",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_length_grid_to_ev_chargers": 1},
    other_deps={
        "_integ_length_grid_to_ev_chargers": {
            "initial": {"initial_length_electric_grid_to_connect_ev_chargers": 1},
            "step": {
                "new_length_grid_to_ev_chargers": 1,
                "wear_length_grid_to_ev_chargers": 1,
            },
        }
    },
)
def length_grid_to_ev_chargers():
    """
    Temporaly evolution of the km of electric grid to connect the EV chargers per type of EV charger
    """
    return _integ_length_grid_to_ev_chargers()


_integ_length_grid_to_ev_chargers = Integ(
    lambda: new_length_grid_to_ev_chargers() - wear_length_grid_to_ev_chargers(),
    lambda: initial_length_electric_grid_to_connect_ev_chargers().expand_dims(
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0
    ),
    "_integ_length_grid_to_ev_chargers",
)


@component.add(
    name="new length grid to EV chargers",
    units="km/Year",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "length_electric_grid_to_connect_ev_chargers": 1,
        "number_ev_chargers_by_type": 1,
        "unit_conversion_km_m": 1,
        "length_grid_to_ev_chargers": 1,
        "one_year": 1,
    },
)
def new_length_grid_to_ev_chargers():
    """
    New km of the grids to connect the EV chargers per type of EV charger
    """
    return (
        (
            length_electric_grid_to_connect_ev_chargers()
            * number_ev_chargers_by_type().transpose("EV CHARGERS I", "REGIONS 35 I")
            * unit_conversion_km_m()
            - length_grid_to_ev_chargers().transpose("EV CHARGERS I", "REGIONS 35 I")
        )
        / one_year()
    ).transpose("REGIONS 35 I", "EV CHARGERS I")


@component.add(
    name="new railway catenary",
    units="km/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_catenary_length": 1,
        "railway_catenary_length": 1,
        "one_year": 1,
    },
)
def new_railway_catenary():
    """
    new km of railway catenary
    """
    return (required_catenary_length() - railway_catenary_length()) / one_year()


@component.add(
    name="new railway tracks",
    units="km/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_railway_tracks_length": 2,
        "railway_tracks_length": 2,
        "one_year": 1,
    },
)
def new_railway_tracks():
    """
    new km of railway tracks
    """
    return (
        if_then_else(
            required_railway_tracks_length() - railway_tracks_length() < 0,
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
            lambda: required_railway_tracks_length() - railway_tracks_length(),
        )
        / one_year()
    )


@component.add(
    name="number EV chargers by type",
    units="chargers",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_number_ev_chargers_by_type": 1},
    other_deps={
        "_integ_number_ev_chargers_by_type": {
            "initial": {"initial_number_ev_chargers_by_type": 1},
            "step": {"number_new_ev_chargers": 1, "number_wear_ev_chargers": 1},
        }
    },
)
def number_ev_chargers_by_type():
    """
    Temporal evolution of the number of different types EV chargers
    """
    return _integ_number_ev_chargers_by_type()


_integ_number_ev_chargers_by_type = Integ(
    lambda: number_new_ev_chargers() - number_wear_ev_chargers(),
    lambda: initial_number_ev_chargers_by_type().expand_dims(
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 0
    ),
    "_integ_number_ev_chargers_by_type",
)


@component.add(
    name="number new EV chargers",
    units="chargers/Year",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_chargers_per_type_of_vehicle": 1,
        "total_number_ev_vehicles": 1,
        "number_ev_chargers_by_type": 1,
        "one_year": 1,
    },
)
def number_new_ev_chargers():
    """
    New EV chargers to install
    """
    return (
        (
            sum(
                number_chargers_per_type_of_vehicle().rename(
                    {
                        "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                        "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                    }
                )
                * total_number_ev_vehicles()
                .rename(
                    {
                        "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                        "BATTERY VEHICLES I": "BATTERY VEHICLES I!",
                    }
                )
                .transpose(
                    "TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!", "REGIONS 35 I"
                ),
                dim=["TRANSPORT POWER TRAIN I!", "BATTERY VEHICLES I!"],
            )
            - number_ev_chargers_by_type().transpose("EV CHARGERS I", "REGIONS 35 I")
        )
        / one_year()
    ).transpose("REGIONS 35 I", "EV CHARGERS I")


@component.add(
    name="number wear EV chargers",
    units="chargers/Year",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_ev_chargers_by_type": 1, "lifetime_ev_chargers": 1},
)
def number_wear_ev_chargers():
    """
    Wear EV chargers to uninstall
    """
    return number_ev_chargers_by_type() / lifetime_ev_chargers()


@component.add(
    name="railway catenary length",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_railway_catenary_length": 1},
    other_deps={
        "_integ_railway_catenary_length": {
            "initial": {"initial_railway_catenary_length": 1},
            "step": {"new_railway_catenary": 1, "wear_railways_catenary": 1},
        }
    },
)
def railway_catenary_length():
    """
    railway catenary km length
    """
    return _integ_railway_catenary_length()


_integ_railway_catenary_length = Integ(
    lambda: new_railway_catenary() - wear_railways_catenary(),
    lambda: initial_railway_catenary_length(),
    "_integ_railway_catenary_length",
)


@component.add(
    name="railway tracks length",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_railway_tracks_length": 1},
    other_deps={
        "_integ_railway_tracks_length": {
            "initial": {"initial_railway_tracks_length": 1},
            "step": {
                "new_railway_tracks": 1,
                "replacement_railway_lines_length": 1,
                "wear_railway_tracks": 1,
            },
        }
    },
)
def railway_tracks_length():
    """
    railway tracks km length
    """
    return _integ_railway_tracks_length()


_integ_railway_tracks_length = Integ(
    lambda: new_railway_tracks()
    + replacement_railway_lines_length()
    - wear_railway_tracks(),
    lambda: xr.DataArray(
        initial_railway_tracks_length(),
        {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
        ["REGIONS 35 I"],
    ),
    "_integ_railway_tracks_length",
)


@component.add(
    name="ratio capacity EV batteries vs capacity chargers",
    units="DMNL",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ev_batteries_power": 1, "total_capacity_ev_chargers": 1},
)
def ratio_capacity_ev_batteries_vs_capacity_chargers():
    """
    Ratio between battery and charger capacities
    """
    return zidz(
        ev_batteries_power(),
        total_capacity_ev_chargers().expand_dims(
            {"EV BATTERIES I": _subscript_dict["EV BATTERIES I"]}, 1
        ),
    )


@component.add(
    name="reestimate share train elec vs total train",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 2},
)
def reestimate_share_train_elec_vs_total_train():
    """
    percents train over 1.
    """
    return zidz(
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, "EV", "RAIL", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        ),
        sum(
            public_passenger_vehicle_fleet()
            .loc[:, :, "RAIL", :]
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
    name="replacement railway lines length",
    units="km/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wear_railway_tracks": 1},
)
def replacement_railway_lines_length():
    """
    km replaced of railway tracks
    """
    return wear_railway_tracks() * 0


@component.add(
    name="required catenary length",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "railway_tracks_length": 1,
        "share_electrified_rails_vs_train_activity": 1,
    },
)
def required_catenary_length():
    """
    km of railway catenary required
    """
    return railway_tracks_length() * share_electrified_rails_vs_train_activity()


@component.add(
    name="required railway tracks length",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_number_trains": 1,
        "total_length_rail_tracks_vs_lines_historic": 1,
        "length_railway_lines_per_locomotive_historic": 1,
    },
)
def required_railway_tracks_length():
    """
    km of railway tracks required
    """
    return (
        total_number_trains()
        * total_length_rail_tracks_vs_lines_historic()
        * length_railway_lines_per_locomotive_historic()
    )


@component.add(
    name="share electrified rails vs train activity",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "reestimate_share_train_elec_vs_total_train": 1,
        "passenger_transport_demand_public_fleet": 2,
    },
)
def share_electrified_rails_vs_train_activity():
    """
    COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_A*(reestimate_share_train_elec_vs_total_tra in[REGIONS 35 I])^2+COEFFICIENT_EQUATION_ELECTRIFIED_CONSTANT_B *reestimate_share_train_elec_vs_total_train[REGIONS 35 I] Ratio between combustion and electric train activity. On a graph with x-axis representing the world train activity (/1) and y-axis representing the world percentage of electrified rails (/1). Equation of the parabola joining the points (0.0) and (1.1) through the point (0.5.0.27). 50% of the railway activity is carried out on the 27% of rails that are electrified.
    """
    return zidz(
        reestimate_share_train_elec_vs_total_train()
        * sum(
            passenger_transport_demand_public_fleet()
            .loc[:, "RAIL", :]
            .reset_coords(drop=True)
            .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["HOUSEHOLDS I!"],
        ),
        sum(
            passenger_transport_demand_public_fleet()
            .loc[:, "RAIL", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS 35 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
            dim=["REGIONS 35 I!", "HOUSEHOLDS I!"],
        ),
    )


@component.add(
    name="total capacity EV chargers",
    units="TW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capacity_ev_chargers": 1},
)
def total_capacity_ev_chargers():
    """
    Total capacity in MW of EVchargers installed
    """
    return sum(
        capacity_ev_chargers().rename({"EV CHARGERS I": "EV CHARGERS I!"}),
        dim=["EV CHARGERS I!"],
    )


@component.add(
    name="total length grid to EV chargers",
    units="km",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"length_grid_to_ev_chargers": 1},
)
def total_length_grid_to_ev_chargers():
    """
    Total km of electric grid to connect the EV chargers
    """
    return sum(
        length_grid_to_ev_chargers().rename({"EV CHARGERS I": "EV CHARGERS I!"}),
        dim=["EV CHARGERS I!"],
    )


@component.add(
    name="total number trains",
    units="locomotives",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def total_number_trains():
    """
    Total number of locomotives
    """
    return sum(
        public_passenger_vehicle_fleet()
        .loc[:, :, "RAIL", :]
        .reset_coords(drop=True)
        .rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="wear length grid to EV chargers",
    units="km/Year",
    subscripts=["REGIONS 35 I", "EV CHARGERS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "length_grid_to_ev_chargers": 1,
        "lifetime_electric_grid_to_connect_ev_chargers": 1,
    },
)
def wear_length_grid_to_ev_chargers():
    """
    Wear km of the grids to connect the EV chargers per type of EV charger
    """
    return (
        length_grid_to_ev_chargers() / lifetime_electric_grid_to_connect_ev_chargers()
    )


@component.add(
    name="wear railway tracks",
    units="km/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"railway_tracks_length": 1, "lifetime_railway_tracks": 1},
)
def wear_railway_tracks():
    """
    wear km of railway tracks
    """
    return railway_tracks_length() / lifetime_railway_tracks()


@component.add(
    name="wear railways catenary",
    units="km/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"railway_catenary_length": 1, "lifetime_railway_catenary": 1},
)
def wear_railways_catenary():
    """
    wear km of railway catenary
    """
    return railway_catenary_length() / lifetime_railway_catenary()
