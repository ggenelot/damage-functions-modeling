"""
Module energyeroi.ev_batteries_esoi
Translated using PySD version 3.14.0
"""

@component.add(
    name="dynFEnU materials EV batteries",
    units="EJ",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenu_per_material_ev_batteries": 1},
)
def dynfenu_materials_ev_batteries():
    """
    Required embodied final energy of total material consumption for EV batteries.
    """
    return sum(
        dynfenu_per_material_ev_batteries().rename({"MATERIALS I": "MATERIALS I!"}),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="dynFEnU materials EV batteries 9R",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynfenu_materials_ev_batteries": 2},
)
def dynfenu_materials_ev_batteries_9r():
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
            dynfenu_materials_ev_batteries()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        dynfenu_materials_ev_batteries()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    return value


@component.add(
    name="dynFEnU per material EV batteries",
    units="EJ",
    subscripts=["REGIONS 35 I", "MATERIALS I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 1,
        "embodied_fe_intensity_materials_36r": 1,
        "unit_conversion_mj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def dynfenu_per_material_ev_batteries():
    """
    Required embodied final energy of material consumption for EV batteries.
    """
    return (
        materials_required_for_new_ev_batteries()
        * embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 35 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 35 I"})
        * (unit_conversion_kg_mt() / unit_conversion_mj_ej())
    )


@component.add(
    name="dynFEnUpou EV",
    units="EJ/Year",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_ev": 1,
        "power_new_vehicle_batteries_35r": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_mj_ej": 1,
        "fenu_intensity_total_materials_of_charger_and_grids": 1,
        "fenu_intensity_transport_total_ev_vehicles_technology": 1,
    },
)
def dynfenupou_ev():
    """
    Dynamic final energy invested for EV batteries and auxiliary systems (chargers and grids), including transport of materials.
    """
    return (
        dynfenust_ev()
        + (
            fenu_intensity_transport_total_ev_vehicles_technology()
            + fenu_intensity_total_materials_of_charger_and_grids()
        )
        * power_new_vehicle_batteries_35r()
        * unit_conversion_mw_tw()
        / unit_conversion_mj_ej()
    )


@component.add(
    name="dynFEnUst EV",
    units="EJ/Year",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_ev_batteries": 1,
        "power_new_vehicle_batteries_35r": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_mj_ej": 1,
        "fenu_intensity_transport_materials_batteries": 1,
    },
)
def dynfenust_ev():
    """
    Dynamic final energy invested for EV batteries (including transport of materials).
    """
    return (
        dynfenust_ev_batteries()
        + fenu_intensity_transport_materials_batteries()
        * power_new_vehicle_batteries_35r()
        * unit_conversion_mw_tw()
        / unit_conversion_mj_ej()
    )


@component.add(
    name="dynFEnUst EV batteries",
    units="EJ/Year",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenust_intensity_ev_batteries": 2,
        "power_new_vehicle_batteries_35r": 1,
        "power_discarded_vehicle_batteries": 1,
        "share_energy_requirements_for_decom_ev_batteries": 1,
    },
)
def dynfenust_ev_batteries():
    """
    Dynamic final energy invested for EV batteries.
    """
    return (
        dynfenust_intensity_ev_batteries() * power_new_vehicle_batteries_35r()
        + power_discarded_vehicle_batteries()
        * dynfenust_intensity_ev_batteries()
        * share_energy_requirements_for_decom_ev_batteries()
    )


@component.add(
    name="dynFEnUst intensity EV batteries",
    units="EJ/TW",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynfenu_materials_ev_batteries": 1,
        "power_new_vehicle_batteries_35r": 1,
    },
)
def dynfenust_intensity_ev_batteries():
    """
    Energy use (in final energy terms) per new installed capacity (TW) over lifetime for EV batteries. Dynamic variable affected by recycling policies.
    """
    return zidz(dynfenu_materials_ev_batteries(), power_new_vehicle_batteries_35r())


@component.add(
    name="ESOI final electrified vehicle",
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
        "energy_delivered_by_electrified_vehicles_battery_lifetime": 2,
        "ol_ev_batteries": 2,
        "eabe": 1,
        "fenu_intensity_total_materials_of_charger_and_grids": 1,
        "share_energy_requirements_for_decom_ev_batteries": 1,
        "fenust_intensity_batteries_electrified_vehicles": 1,
        "fenu_intensity_transport_total_ev_vehicles_technology": 1,
        "vehicle_electric_power": 2,
        "ev_charge_losses_share": 2,
        "unit_conversion_kw_mw": 2,
    },
)
def esoi_final_electrified_vehicle():
    """
    Dynamic ESOI final over lifetime of electrified vehicle battery
    """
    return zidz(
        energy_delivered_by_electrified_vehicles_battery_lifetime()
        * (1 - ol_ev_batteries())
        * (1 - eabe()),
        fenust_intensity_batteries_electrified_vehicles()
        * (1 + share_energy_requirements_for_decom_ev_batteries())
        + fenu_intensity_transport_total_ev_vehicles_technology()
        * vehicle_electric_power()
        / unit_conversion_kw_mw()
        + (
            fenu_intensity_total_materials_of_charger_and_grids()
            * vehicle_electric_power()
            / unit_conversion_kw_mw()
        )
        + energy_delivered_by_electrified_vehicles_battery_lifetime()
        * (1 - ol_ev_batteries())
        * (ev_charge_losses_share() / 1 - ev_charge_losses_share()),
    )


@component.add(
    name="ESOI st electrified vehicle",
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
        "energy_delivered_by_electrified_vehicles_battery_lifetime": 1,
        "ol_ev_batteries": 1,
        "fenust_intensity_batteries_electrified_vehicles": 1,
        "share_energy_requirements_for_decom_ev_batteries": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_kw_mw": 1,
        "fenu_intensity_transport_materials_batteries": 1,
    },
)
def esoi_st_electrified_vehicle():
    """
    Dynamic ESOIst over lifetime of electrified vehicle battery
    """
    return zidz(
        energy_delivered_by_electrified_vehicles_battery_lifetime()
        * (1 - ol_ev_batteries()),
        fenust_intensity_batteries_electrified_vehicles()
        * (1 + share_energy_requirements_for_decom_ev_batteries())
        + fenu_intensity_transport_materials_batteries()
        * vehicle_electric_power()
        / unit_conversion_kw_mw(),
    )


@component.add(
    name="FEnU intensity charger and grids",
    units="MJ/MW",
    subscripts=["REGIONS 35 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_fe_intensity_materials_36r": 1,
        "machining_rate_ev_batteries": 1,
        "materials_required_for_new_ev_chargers_grids": 1,
        "materials_required_for_new_ev_chargers": 1,
        "unit_conversion_kg_mt": 1,
        "power_new_vehicle_batteries_35r": 1,
        "unit_conversion_mw_tw": 1,
    },
)
def fenu_intensity_charger_and_grids():
    """
    EnU (final energy) per material of the chargers and grids for the EV batteries
    """
    return zidz(
        embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 35 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 35 I"})
        * machining_rate_ev_batteries()
        * (
            materials_required_for_new_ev_chargers()
            + materials_required_for_new_ev_chargers_grids()
        )
        * unit_conversion_kg_mt(),
        (
            sum(
                power_new_vehicle_batteries_35r().rename(
                    {"EV BATTERIES I": "EV BATTERIES I!"}
                ),
                dim=["EV BATTERIES I!"],
            )
            * unit_conversion_mw_tw()
        ).expand_dims({"MATERIALS I": _subscript_dict["MATERIALS I"]}, 1),
    )


@component.add(
    name="FEnU intensity total materials of charger and grids",
    units="MJ/MW",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenu_intensity_charger_and_grids": 1},
)
def fenu_intensity_total_materials_of_charger_and_grids():
    """
    EnU (final energy) of the chargers and grids for the EV batteries
    """
    return sum(
        fenu_intensity_charger_and_grids().rename({"MATERIALS I": "MATERIALS I!"}),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="FEnU intensity transport materials batteries",
    units="MJ/MW",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 2,
        "unit_conversion_kg_mt": 2,
        "power_new_vehicle_batteries_35r": 2,
        "matrix_unit_prefixes": 2,
    },
)
def fenu_intensity_transport_materials_batteries():
    """
    Energy used (final energy) to transport battery materials using the methodology of De Castro et al.
    """
    return (
        1.19
        * zidz(
            sum(
                materials_required_for_new_ev_batteries().rename(
                    {"MATERIALS I": "MATERIALS I!"}
                )
                * unit_conversion_kg_mt(),
                dim=["MATERIALS I!"],
            ),
            power_new_vehicle_batteries_35r() * 1000000.0,
        )
        * 500
        * 3.5
        + 1.09
        * zidz(
            sum(
                materials_required_for_new_ev_batteries().rename(
                    {"MATERIALS I": "MATERIALS I!"}
                )
                * unit_conversion_kg_mt(),
                dim=["MATERIALS I!"],
            ),
            power_new_vehicle_batteries_35r()
            * float(matrix_unit_prefixes().loc["tera", "mega"]),
        )
        * 10000
        * 0.2
        + 1.19 * 0 * 3.5 * 250
    ) / float(matrix_unit_prefixes().loc["mega", "kilo"])


@component.add(
    name="FEnU intensity transport total EV vehicles technology",
    units="MJ/MW",
    subscripts=["REGIONS 35 I", "EV BATTERIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_ev_batteries": 2,
        "unit_conversion_kg_mt": 3,
        "power_new_vehicle_batteries_35r": 5,
        "matrix_unit_prefixes": 7,
        "total_materials_required_for_new_ev_chargers_and_grids_without_cement": 2,
        "cement_required_for_new_ev_chargers_and_grids": 1,
    },
)
def fenu_intensity_transport_total_ev_vehicles_technology():
    """
    Energy used (final energy) to transport battery and infrastructure materials using the methodology of De Castro et al.
    """
    return (
        1.19
        * (
            zidz(
                sum(
                    materials_required_for_new_ev_batteries().rename(
                        {"MATERIALS I": "MATERIALS I!"}
                    ),
                    dim=["MATERIALS I!"],
                )
                * unit_conversion_kg_mt(),
                power_new_vehicle_batteries_35r()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
            + zidz(
                total_materials_required_for_new_ev_chargers_and_grids_without_cement()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV BATTERIES I": "EV BATTERIES I!"}
                    ),
                    dim=["EV BATTERIES I!"],
                )
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
        )
        * 500
        * 3.5
        + 1.09
        * (
            zidz(
                sum(
                    materials_required_for_new_ev_batteries().rename(
                        {"MATERIALS I": "MATERIALS I!"}
                    ),
                    dim=["MATERIALS I!"],
                )
                * unit_conversion_kg_mt(),
                power_new_vehicle_batteries_35r()
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
            + zidz(
                total_materials_required_for_new_ev_chargers_and_grids_without_cement()
                * unit_conversion_kg_mt(),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV BATTERIES I": "EV BATTERIES I!"}
                    ),
                    dim=["EV BATTERIES I!"],
                )
                * float(matrix_unit_prefixes().loc["tera", "mega"]),
            )
        )
        * 10000
        * 0.2
        + (
            1.19
            * zidz(
                cement_required_for_new_ev_chargers_and_grids(),
                sum(
                    power_new_vehicle_batteries_35r().rename(
                        {"EV BATTERIES I": "EV BATTERIES I!"}
                    )
                    * float(matrix_unit_prefixes().loc["tera", "mega"]),
                    dim=["EV BATTERIES I!"],
                ),
            )
            * 3.5
            * 250
        )
    ) / float(matrix_unit_prefixes().loc["mega", "kilo"])


@component.add(
    name="FEnUst intensity batteries electrified vehicles",
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
        "embodied_fe_intensity_materials_36r": 1,
        "machining_rate_ev_batteries": 1,
        "materials_per_new_capacity_installed_ev_batteries": 1,
        "scrap_rate": 1,
        "vehicle_electric_power": 1,
        "unit_conversion_kw_mw": 1,
    },
)
def fenust_intensity_batteries_electrified_vehicles():
    """
    Energy use (in final terms) per new battery for the manufacturing of electrified Vehicles batteries.
    """
    return (
        sum(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 35 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 35 I", "MATERIALS I": "MATERIALS I!"})
            * machining_rate_ev_batteries()
            * materials_per_new_capacity_installed_ev_batteries().rename(
                {"MATERIALS I": "MATERIALS I!"}
            ),
            dim=["MATERIALS I!"],
        )
        * (1 + scrap_rate())
        * vehicle_electric_power()
        / unit_conversion_kw_mw()
    )


@component.add(
    name="total ESOIfinal electrified vehicles",
    units="DMNL",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "esoi_final_electrified_vehicle": 1,
        "new_transport_electrified_vehicle_batteries_power": 2,
    },
)
def total_esoifinal_electrified_vehicles():
    """
    Weighted-average ESOI final for all EV subtechnologies.
    """
    return zidz(
        sum(
            esoi_final_electrified_vehicle().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            )
            * new_transport_electrified_vehicle_batteries_power().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        ),
        sum(
            new_transport_electrified_vehicle_batteries_power().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        ),
    )


@component.add(
    name="total ESOIst electrified vehicles",
    units="DMNL",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "BATTERY VEHICLES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "esoi_st_electrified_vehicle": 1,
        "new_transport_electrified_vehicle_batteries_power": 2,
    },
)
def total_esoist_electrified_vehicles():
    """
    Weighted-average ESOIst (standard) for all EV subtechnologies.
    """
    return zidz(
        sum(
            esoi_st_electrified_vehicle().rename({"EV BATTERIES I": "EV BATTERIES I!"})
            * new_transport_electrified_vehicle_batteries_power().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        ),
        sum(
            new_transport_electrified_vehicle_batteries_power().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        ),
    )
