"""
Module energyghg_emissions
Translated using PySD version 3.13.4
"""

@component.add(
    name="buildings final energy consumption by FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 6,
        "base_final_energy_consumption_households_coicop": 6,
        "final_energy_consumption_buildings_and_transport": 6,
        "share_energy_consumption_solid_bio_vs_solid_fossil": 4,
    },
)
def buildings_final_energy_consumption_by_fe():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "NRG FE I"],
    )
    value.loc[:, ["FE elec"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH ELECTRICITY"]
            .reset_coords(drop=True),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH ELECTRICITY"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE gas"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH GAS"]
            .reset_coords(drop=True),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH GAS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH HEAT"]
            .reset_coords(drop=True),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH HEAT"]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"]] = 0
    value.loc[:, ["FE liquid"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH LIQUID FUELS"]
            .reset_coords(drop=True),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH LIQUID FUELS"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * share_energy_consumption_solid_bio_vs_solid_fossil(),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * share_energy_consumption_solid_bio_vs_solid_fossil(),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"]] = (
        if_then_else(
            switch_energy() == 0,
            lambda: base_final_energy_consumption_households_coicop()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * (1 - share_energy_consumption_solid_bio_vs_solid_fossil()),
            lambda: final_energy_consumption_buildings_and_transport()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * (1 - share_energy_consumption_solid_bio_vs_solid_fossil()),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="buildings GHG emissions 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def buildings_ghg_emissions_35r():
    return (
        sum(
            buildings_ghg_emissions_end_use_energy_by_fe_35r().rename(
                {"NRG FE I": "NRG FE I!"}
            ),
            dim=["NRG FE I!"],
        )
        / unit_conversion_kg_mt()
    )


@component.add(
    name="buildings GHG emissions end use energy by FE 35R",
    units="kg/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emission_factors_residential_stationary_combustion": 1,
        "buildings_final_energy_consumption_by_fe": 1,
    },
)
def buildings_ghg_emissions_end_use_energy_by_fe_35r():
    """
    Greenhouse gas emissions generated by energy end-use in buildings, by region, type of final enerhy and type of gas, in kg/year.
    """
    return np.maximum(
        0,
        ghg_emission_factors_residential_stationary_combustion()
        * buildings_final_energy_consumption_by_fe().transpose(
            "NRG FE I", "REGIONS 35 I"
        ),
    ).transpose("REGIONS 35 I", "NRG FE I", "GHG I")


@component.add(
    name="CO2 emissions by passenger transport mode and power train 35R",
    units="kg/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_emissions_end_use_energy": 7,
        "ghg_intensity_emissions_by_fe_35r": 4,
        "energy_passenger_transport_consumption": 4,
        "unit_conversion_mj_ej": 4,
        "unit_conversion_kg_mt": 4,
    },
)
def co2_emissions_by_passenger_transport_mode_and_power_train_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "GHG I",
        ],
    )
    value.loc[:, ["ICE gasoline"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "ICE gasoline", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE gasoline"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["ICE diesel"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "ICE diesel", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE diesel"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["ICE gas"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "ICE gas", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE gas"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["ICE LPG"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "ICE LPG", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["ICE LPG"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], ["BEV"], :, ["CO2"]] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[_subscript_dict["REGIONS 8 I"], "BEV", :, :]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * ghg_intensity_emissions_by_fe_35r()
            .loc[_subscript_dict["REGIONS 8 I"], "FE elec", "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS 8 I"})
            * unit_conversion_kg_mt()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["PHEV"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "PHEV", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["HEV"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "HEV", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["HEV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["FCEV"], :, ["CO2"]] = (
        passenger_transport_emissions_end_use_energy()
        .loc[:, "FCEV", :, "CO2"]
        .reset_coords(drop=True)
        .expand_dims({"TRANSPORT POWER TRAIN I": ["FCEV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], ["BEV"], :, ["CO2"]] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[_subscript_dict["REGIONS EU27 I"], "BEV", :, :]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * ghg_intensity_emissions_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE elec", "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"})
            * unit_conversion_kg_mt()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["BEV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], ["EV"], :, ["CO2"]] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[_subscript_dict["REGIONS EU27 I"], "EV", :, :]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS 35 I": "REGIONS EU27 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * ghg_intensity_emissions_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE elec", "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"})
            * unit_conversion_kg_mt()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["EV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, ["HPV"], :, :] = 0
    value.loc[_subscript_dict["REGIONS 8 I"], ["EV"], :, ["CO2"]] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[_subscript_dict["REGIONS 8 I"], "EV", :, :]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * ghg_intensity_emissions_by_fe_35r()
            .loc[_subscript_dict["REGIONS 8 I"], "FE elec", "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS 8 I"})
            * unit_conversion_kg_mt()
            / unit_conversion_mj_ej()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["EV"]}, 1)
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    return value


@component.add(
    name="CO2 emissions private transport by region",
    units="kg/Year",
    subscripts=["REGIONS 35 I", "PRIVATE TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_passenger_transport_mode_and_power_train_35r": 1},
)
def co2_emissions_private_transport_by_region():
    return sum(
        co2_emissions_by_passenger_transport_mode_and_power_train_35r()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], "CO2"]
        .reset_coords(drop=True)
        .rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="CO2 emissions public transport by region",
    units="kg/Year",
    subscripts=["REGIONS 35 I", "PUBLIC TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_passenger_transport_mode_and_power_train_35r": 1},
)
def co2_emissions_public_transport_by_region():
    return sum(
        co2_emissions_by_passenger_transport_mode_and_power_train_35r()
        .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], "CO2"]
        .reset_coords(drop=True)
        .rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!"],
    )


@component.add(
    name="CO2 intensity of passenger transport 9R",
    units="g/(Year*km*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_transport_ghg_emissions_all_energy_chain_35r": 2,
        "total_passenger_transport_demand": 2,
        "unit_conversion_g_mt": 2,
    },
)
def co2_intensity_of_passenger_transport_9r():
    """
    CO2_intensity_of_passenger_transport_9R
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        zidz(
            sum(
                private_passenger_transport_ghg_emissions_all_energy_chain_35r()
                .loc[_subscript_dict["REGIONS 8 I"], :, "CO2"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS 8 I", "NRG FE I": "NRG FE I!"}),
                dim=["NRG FE I!"],
            ),
            total_passenger_transport_demand()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 35 I": "REGIONS 8 I"}),
        )
        * unit_conversion_g_mt()
    ).values
    value.loc[["EU27"]] = (
        zidz(
            sum(
                private_passenger_transport_ghg_emissions_all_energy_chain_35r()
                .loc[_subscript_dict["REGIONS EU27 I"], :, "CO2"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS EU27 I!", "NRG FE I": "NRG FE I!"}),
                dim=["REGIONS EU27 I!", "NRG FE I!"],
            ),
            sum(
                total_passenger_transport_demand()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
        )
        * unit_conversion_g_mt()
    )
    return value


@component.add(
    name="CO2eq energy emissions 35R",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_energy_emissions_by_sector_35r": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_tco2eq_gtco2eq": 3,
        "unit_conversion_mt_t": 3,
    },
)
def co2eq_energy_emissions_35r():
    return (
        ghg_energy_emissions_by_sector_35r().loc[:, :, "CO2"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CO2"]),
            lambda: float(gwp_100_year().loc["CO2"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        / unit_conversion_mt_t()
        + ghg_energy_emissions_by_sector_35r().loc[:, :, "CH4"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CH4"]),
            lambda: float(gwp_100_year().loc["CH4"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        / unit_conversion_mt_t()
        + ghg_energy_emissions_by_sector_35r().loc[:, :, "N2O"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["N2O"]),
            lambda: float(gwp_100_year().loc["N2O"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        / unit_conversion_mt_t()
    )


@component.add(
    name="delayed TS GHG emissions households COICOP 35 R CO2eq",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq": 1},
    other_deps={
        "_delayfixed_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq": {
            "initial": {"time_step": 1},
            "step": {"ghg_emissions_households_coicop_35_r_co2eq": 1},
        }
    },
)
def delayed_ts_ghg_emissions_households_coicop_35_r_co2eq():
    """
    Delayed (time step) GHG emissions from households by COICOP category.
    """
    return _delayfixed_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq()


_delayfixed_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq = DelayFixed(
    lambda: ghg_emissions_households_coicop_35_r_co2eq(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq",
)


@component.add(
    name="delayed TS GHG energy emissions 35R CO2eq",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_ghg_energy_emissions_35r_co2eq": 1},
    other_deps={
        "_delayfixed_delayed_ts_ghg_energy_emissions_35r_co2eq": {
            "initial": {"time_step": 1},
            "step": {"imv_ghg_energy_emissions_35r_co2eq": 1},
        }
    },
)
def delayed_ts_ghg_energy_emissions_35r_co2eq():
    """
    Delayed GHG energy emissions in GtCO2eq
    """
    return _delayfixed_delayed_ts_ghg_energy_emissions_35r_co2eq()


_delayfixed_delayed_ts_ghg_energy_emissions_35r_co2eq = DelayFixed(
    lambda: imv_ghg_energy_emissions_35r_co2eq(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_ghg_energy_emissions_35r_co2eq",
)


@component.add(
    name="delayed TS implicit CO2 emission factor sectors",
    units="MtCO2eq/TJ",
    subscripts=[
        "REGIONS 35 I",
        "SECTORS FINAL ENERGY I",
        "SECTORS NON ENERGY I",
        "GHG ENERGY USE I",
    ],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_implicit_co2_emission_factor_sectors": 1},
    other_deps={
        "_delayfixed_delayed_ts_implicit_co2_emission_factor_sectors": {
            "initial": {
                "initial_delayed_co2_emissions_factor_fe_sector": 1,
                "time_step": 1,
            },
            "step": {"implicit_co2_emission_factor_fe_sectors": 1},
        }
    },
)
def delayed_ts_implicit_co2_emission_factor_sectors():
    """
    Delayed (time step) implicit CO2 emission factor by sector of final energy and by non energy sectors.
    """
    return _delayfixed_delayed_ts_implicit_co2_emission_factor_sectors()


_delayfixed_delayed_ts_implicit_co2_emission_factor_sectors = DelayFixed(
    lambda: implicit_co2_emission_factor_fe_sectors(),
    lambda: time_step(),
    lambda: initial_delayed_co2_emissions_factor_fe_sector(),
    time_step,
    "_delayfixed_delayed_ts_implicit_co2_emission_factor_sectors",
)


@component.add(
    name="delayed TS implicit ghg emission factor households COICOP",
    units="MtCO2eq/TJ",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_implicit_ghg_emission_factor_households_coicop": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_implicit_ghg_emission_factor_households_coicop": {
            "initial": {"time_step": 1},
            "step": {"implicit_ghg_emission_factor_households_coicop": 1},
        }
    },
)
def delayed_ts_implicit_ghg_emission_factor_households_coicop():
    """
    Delayed (time step) households implicit GHG emission factor by COICOP category.]
    """
    return _delayfixed_delayed_ts_implicit_ghg_emission_factor_households_coicop()


_delayfixed_delayed_ts_implicit_ghg_emission_factor_households_coicop = DelayFixed(
    lambda: implicit_ghg_emission_factor_households_coicop(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_implicit_ghg_emission_factor_households_coicop",
)


@component.add(
    name="delayed TS IMV GHG energy emissions 35R CO2eq until 2015",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015": {
            "initial": {"time_step": 1},
            "step": {"imv_ghg_energy_emissions_35r_co2eq_until_2015": 1},
        }
    },
)
def delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015():
    """
    Delayed variable to modularize.
    """
    return _delayfixed_delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015()


_delayfixed_delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015 = DelayFixed(
    lambda: imv_ghg_energy_emissions_35r_co2eq_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015",
)


@component.add(
    name="EMISSION FACTORS CHARCOAL BIOCHAR PRODUCTION",
    units="gCO2/kg",
    subscripts=["NGR EF CHARCOAL BIOCHAR PRODUCTION CO2"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factors_charcoal_biochar_production"
    },
)
def emission_factors_charcoal_biochar_production():
    return _ext_constant_emission_factors_charcoal_biochar_production()


_ext_constant_emission_factors_charcoal_biochar_production = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EF_CHARCOAL_BIOCHAR_PRODUCTION_CO2*",
    {
        "NGR EF CHARCOAL BIOCHAR PRODUCTION CO2": _subscript_dict[
            "NGR EF CHARCOAL BIOCHAR PRODUCTION CO2"
        ]
    },
    _root,
    {
        "NGR EF CHARCOAL BIOCHAR PRODUCTION CO2": _subscript_dict[
            "NGR EF CHARCOAL BIOCHAR PRODUCTION CO2"
        ]
    },
    "_ext_constant_emission_factors_charcoal_biochar_production",
)


@component.add(
    name="EMISSION FACTORS COAL TO GAS PRODUCTION",
    units="kg/TJ",
    subscripts=["GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factors_coal_to_gas_production"
    },
)
def emission_factors_coal_to_gas_production():
    """
    GHG Emissions factor in the process of converting Coal to Liquids in Refinery
    """
    return _ext_constant_emission_factors_coal_to_gas_production()


_ext_constant_emission_factors_coal_to_gas_production = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EMISSION_FACTORS_COAL_TO_GAS_PRODUCTION*",
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    _root,
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    "_ext_constant_emission_factors_coal_to_gas_production",
)


@component.add(
    name="EMISSION FACTORS COKE PRODUCTION",
    units="kg CO2/tonne",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_coke_production"},
)
def emission_factors_coke_production():
    return _ext_constant_emission_factors_coke_production()


_ext_constant_emission_factors_coke_production = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EF_COKE_PRODUCTION_CO2*",
    {},
    _root,
    {},
    "_ext_constant_emission_factors_coke_production",
)


@component.add(
    name="EMISSION FACTORS FUGITIVES EXTRACTION",
    units="g/m3",
    subscripts=["NRG PE I", "GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_fugitives_extraction"},
)
def emission_factors_fugitives_extraction():
    """
    Greenhouse gas emission factors due to fugitive emissions generated by the extraction of fossil energy resources, in g/m3.
    """
    return _ext_constant_emission_factors_fugitives_extraction()


_ext_constant_emission_factors_fugitives_extraction = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EF_FUGITIVES_EXTRACTION_GHG",
    {
        "NRG PE I": _subscript_dict["NRG PE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    _root,
    {
        "NRG PE I": _subscript_dict["NRG PE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    "_ext_constant_emission_factors_fugitives_extraction",
)


@component.add(
    name="EMISSION FACTORS FUGITIVES REFINING",
    units="g/m3",
    subscripts=["NRG PE I", "GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_fugitives_refining"},
)
def emission_factors_fugitives_refining():
    """
    Greenhouse gas emission factors due to fugitive emissions generated by the refining process, in g/m3.
    """
    return _ext_constant_emission_factors_fugitives_refining()


_ext_constant_emission_factors_fugitives_refining = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EF_FUGITIVES_REFINING_GHG",
    {
        "NRG PE I": _subscript_dict["NRG PE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    _root,
    {
        "NRG PE I": _subscript_dict["NRG PE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    "_ext_constant_emission_factors_fugitives_refining",
)


@component.add(
    name="EMISSION FACTORS FUGITIVES SUPPLY",
    units="g/m3",
    subscripts=["NRG FE I", "GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_fugitives_supply"},
)
def emission_factors_fugitives_supply():
    return _ext_constant_emission_factors_fugitives_supply()


_ext_constant_emission_factors_fugitives_supply = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EF_FUGITIVES_SUPPLY_GHG",
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    _root,
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
    },
    "_ext_constant_emission_factors_fugitives_supply",
)


@component.add(
    name="EMISSION FACTORS GAS TO LIQUID PRODUCTION",
    units="kg/TJ",
    subscripts=["GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factors_gas_to_liquid_production"
    },
)
def emission_factors_gas_to_liquid_production():
    """
    GHG Emissions factor in the process of converting Coal to Liquids in Refinery
    """
    return _ext_constant_emission_factors_gas_to_liquid_production()


_ext_constant_emission_factors_gas_to_liquid_production = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_FUGITIVES_GAS_OIL_FUEL_TRANS",
    "EMISSION_FACTORS_GAS_TO_LIQUID_PRODUCTION",
    {"GHG ENERGY USE I": ["CO2"]},
    _root,
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    "_ext_constant_emission_factors_gas_to_liquid_production",
)


@component.add(
    name="EMISSION FACTORS OFF ROAD TRANSPORTATION",
    units="kg/TJ",
    subscripts=["NRG EF OFF ROAD TRANSPORTATION"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factors_off_road_transportation"
    },
)
def emission_factors_off_road_transportation():
    return _ext_constant_emission_factors_off_road_transportation()


_ext_constant_emission_factors_off_road_transportation = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "EF_OFF_ROAD_TRANSPORTATION_CO2*",
    {
        "NRG EF OFF ROAD TRANSPORTATION": _subscript_dict[
            "NRG EF OFF ROAD TRANSPORTATION"
        ]
    },
    _root,
    {
        "NRG EF OFF ROAD TRANSPORTATION": _subscript_dict[
            "NRG EF OFF ROAD TRANSPORTATION"
        ]
    },
    "_ext_constant_emission_factors_off_road_transportation",
)


@component.add(
    name="EMISSION FACTORS PRIVATE TRANSPORT",
    units="kg/TJ",
    subscripts=["TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I", "GHG I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_emission_factors_private_transport"},
)
def emission_factors_private_transport():
    """
    Greenhouse gas mobility emission factors of private transport vehicles, by type of power train, type of trasnport and type of gas, in kg/TJ.
    """
    value = xr.DataArray(
        np.nan,
        {
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I", "GHG I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CO2"]] = True
    def_subs.loc[:, :, ["CH4"]] = True
    def_subs.loc[:, :, ["N2O"]] = True
    value.values[def_subs.values] = (
        _ext_constant_emission_factors_private_transport().values[def_subs.values]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CO2"]] = False
    except_subs.loc[:, :, ["CH4"]] = False
    except_subs.loc[:, :, ["N2O"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_constant_emission_factors_private_transport = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "CO2_EMISSION_FACTORS_PRIVATE_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
        "GHG I": ["CO2"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
        "GHG I": _subscript_dict["GHG I"],
    },
    "_ext_constant_emission_factors_private_transport",
)

_ext_constant_emission_factors_private_transport.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "CH4_EMISSION_FACTORS_PRIVATE_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
        "GHG I": ["CH4"],
    },
)

_ext_constant_emission_factors_private_transport.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "N2O_EMISSION_FACTORS_PRIVATE_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
        "GHG I": ["N2O"],
    },
)


@component.add(
    name="EMISSION FACTORS PUBLIC TRANSPORT",
    units="kg/TJ",
    subscripts=["TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I", "GHG I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_emission_factors_public_transport"},
)
def emission_factors_public_transport():
    """
    Greenhouse gas mobility emission factors of public transport vehicles, by type of power train, type of trasnport and type of gas, in kg/TJ.
    """
    value = xr.DataArray(
        np.nan,
        {
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I", "GHG I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CO2"]] = True
    def_subs.loc[:, :, ["CH4"]] = True
    def_subs.loc[:, :, ["N2O"]] = True
    value.values[def_subs.values] = (
        _ext_constant_emission_factors_public_transport().values[def_subs.values]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CO2"]] = False
    except_subs.loc[:, :, ["CH4"]] = False
    except_subs.loc[:, :, ["N2O"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_constant_emission_factors_public_transport = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "CO2_EMISSION_FACTORS_PUBLIC_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
        "GHG I": ["CO2"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
        "GHG I": _subscript_dict["GHG I"],
    },
    "_ext_constant_emission_factors_public_transport",
)

_ext_constant_emission_factors_public_transport.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "CH4_EMISSION_FACTORS_PUBLIC_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
        "GHG I": ["CH4"],
    },
)

_ext_constant_emission_factors_public_transport.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "N2O_EMISSION_FACTORS_PUBLIC_TRANSPORT",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PUBLIC TRANSPORT I": _subscript_dict["PUBLIC TRANSPORT I"],
        "GHG I": ["N2O"],
    },
)


@component.add(
    name="EMISSION FACTORS RAIL TRANSPORTATION",
    units="kg/TJ",
    subscripts=["NRG EF RAIL TRANSPORT"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_rail_transportation"},
)
def emission_factors_rail_transportation():
    return _ext_constant_emission_factors_rail_transportation()


_ext_constant_emission_factors_rail_transportation = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "EF_RAIL_TRANSPORTATION_CO2*",
    {"NRG EF RAIL TRANSPORT": _subscript_dict["NRG EF RAIL TRANSPORT"]},
    _root,
    {"NRG EF RAIL TRANSPORT": _subscript_dict["NRG EF RAIL TRANSPORT"]},
    "_ext_constant_emission_factors_rail_transportation",
)


@component.add(
    name="EMISSION FACTORS ROAD TRANSPORTATION",
    units="kg/TJ",
    subscripts=["NRG EF ROAD TRANSPORTATION I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_emission_factors_road_transportation"},
)
def emission_factors_road_transportation():
    return _ext_constant_emission_factors_road_transportation()


_ext_constant_emission_factors_road_transportation = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "EF_ROAD_TRANSPORTATION_CO2*",
    {"NRG EF ROAD TRANSPORTATION I": _subscript_dict["NRG EF ROAD TRANSPORTATION I"]},
    _root,
    {"NRG EF ROAD TRANSPORTATION I": _subscript_dict["NRG EF ROAD TRANSPORTATION I"]},
    "_ext_constant_emission_factors_road_transportation",
)


@component.add(
    name="EMISSION FACTORS STATIONARY COMBUSTION",
    units="kg/TJ",
    subscripts=["NRG PROTRA I", "NRG TI I", "GHG I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_emission_factors_stationary_combustion"},
)
def emission_factors_stationary_combustion():
    value = xr.DataArray(
        np.nan,
        {
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "NRG TI I": _subscript_dict["NRG TI I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["NRG PROTRA I", "NRG TI I", "GHG I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, :, ["CO2"]] = True
    def_subs.loc[:, :, ["CH4"]] = True
    def_subs.loc[:, :, ["N2O"]] = True
    value.values[def_subs.values] = (
        _ext_constant_emission_factors_stationary_combustion().values[def_subs.values]
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CO2"]] = False
    except_subs.loc[:, :, ["CH4"]] = False
    except_subs.loc[:, :, ["N2O"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_constant_emission_factors_stationary_combustion = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_STATIONARY_COM",
    "EF_TRANSFORMATION_CO2_BY_NRG_PROTRA_I",
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "GHG I": ["CO2"],
    },
    _root,
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "GHG I": _subscript_dict["GHG I"],
    },
    "_ext_constant_emission_factors_stationary_combustion",
)

_ext_constant_emission_factors_stationary_combustion.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_STATIONARY_COM",
    "EF_TRANSFORMATION_CH4_BY_NRG_PROTRA_I",
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "GHG I": ["CH4"],
    },
)

_ext_constant_emission_factors_stationary_combustion.add(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_STATIONARY_COM",
    "EF_TRANSFORMATION_N2O_BY_NRG_PROTRA_I",
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
        "GHG I": ["N2O"],
    },
)


@component.add(
    name="EMISSION FACTORS WATER BORNE NAVIGATION",
    units="kg/TJ",
    subscripts=["NRG EF WATER BORNE NAVIGATION"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_emission_factors_water_borne_navigation"
    },
)
def emission_factors_water_borne_navigation():
    return _ext_constant_emission_factors_water_borne_navigation()


_ext_constant_emission_factors_water_borne_navigation = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MOBILE_COM",
    "EF_WATER_BORNE_NAVIGATION_CO2*",
    {"NRG EF WATER BORNE NAVIGATION": _subscript_dict["NRG EF WATER BORNE NAVIGATION"]},
    _root,
    {"NRG EF WATER BORNE NAVIGATION": _subscript_dict["NRG EF WATER BORNE NAVIGATION"]},
    "_ext_constant_emission_factors_water_borne_navigation",
)


@component.add(
    name="energy passenger transport consumption by FE 9R",
    units="MJ",
    subscripts=["REGIONS 9 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_passenger_transport_consumption_by_fe_35r": 2},
)
def energy_passenger_transport_consumption_by_fe_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
        },
        ["REGIONS 9 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = sum(
        energy_passenger_transport_consumption_by_fe_35r()
        .loc[_subscript_dict["REGIONS 8 I"], :, :, :]
        .rename({"REGIONS 35 I": "REGIONS 8 I", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["HOUSEHOLDS I!"],
    ).values
    value.loc[["EU27"], :, :] = (
        sum(
            energy_passenger_transport_consumption_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :, :]
            .rename(
                {"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="final energy demand by FE",
    units="TJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_bysectors_and_fe_9r": 1},
)
def final_energy_demand_by_fe():
    """
    Final energy demand by region and type of final energy, in TJ/year.
    """
    return sum(
        final_energy_demand_bysectors_and_fe_9r().rename(
            {"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}
        ),
        dim=["SECTORS NON ENERGY I!"],
    )


@component.add(
    name="final energy demand by FE EJ 9R",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_bysectors_and_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def final_energy_demand_by_fe_ej_9r():
    return (
        sum(
            final_energy_demand_bysectors_and_fe_9r().rename(
                {"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}
            ),
            dim=["SECTORS NON ENERGY I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="final energy demand by final energy sector and non energy sector",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 6},
)
def final_energy_demand_by_final_energy_sector_and_non_energy_sector():
    """
    Final energy demand by sector and final energy in economic classification
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
        },
        ["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    )
    value.loc[:, ["REFINING"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE liquid"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    value.loc[:, ["HYDROGEN PRODUCTION"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 1)
        .values
    )
    value.loc[:, ["DISTRIBUTION ELECTRICITY"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE elec"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER ELECTRICITY TRANSPORT": _subscript_dict[
                    "CLUSTER ELECTRICITY TRANSPORT"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["DISTRIBUTION GAS"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE gas"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE heat"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], :] = (
        final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE solid fossil"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["COKE"], :] = 0
    return value


@component.add(
    name="final energy demand bysectors and FE 9R",
    units="TJ/Year",
    subscripts=["REGIONS 9 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 2},
)
def final_energy_demand_bysectors_and_fe_9r():
    """
    Final energy demand by 9 regions, by sector and type of final energy, in TJ/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 9 I", "SECTORS NON ENERGY I", "NRG FE I"],
    )
    value.loc[["EU27"], :, :] = (
        np.maximum(
            0,
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[_subscript_dict["REGIONS EU27 I"], :, :]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = np.maximum(
        0,
        final_energy_demand_by_sector_and_fe()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"}),
    ).values
    return value


@component.add(
    name="GHG all emissions 35R",
    units="Gt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_energy_emissions_by_sector_35r": 1,
        "unit_conversion_mt_gt": 3,
        "buildings_ghg_emissions_35r": 1,
        "private_transport_ghg_emissions_35r": 1,
    },
)
def ghg_all_emissions_35r():
    """
    + Buildings_GHG_emissions[REGIONS_35_I,GHG_I]/UNIT_CONVERSION_Mt_Gt+ SUM(passenger_transport_GHG_emissions_all_energy_chain[REGIONS_35_I,NRG_FE_ I!,GHG_I])/UNIT_CONVERSION_Mt_Gt
    """
    return (
        sum(
            ghg_energy_emissions_by_sector_35r().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        / unit_conversion_mt_gt()
        + buildings_ghg_emissions_35r() / unit_conversion_mt_gt()
        + sum(
            private_transport_ghg_emissions_35r().rename({"NRG FE I": "NRG FE I!"}),
            dim=["NRG FE I!"],
        )
        / unit_conversion_mt_gt()
    )


@component.add(
    name="GHG all emissions 35R CO2eq",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_all_emissions_35r": 1,
        "unit_conversion_t_gt": 1,
        "gwp_100_year": 1,
        "select_gwp_time_frame_sp": 1,
        "gwp_20_year": 1,
        "unit_conversion_tco2eq_mtco2eq": 1,
    },
)
def ghg_all_emissions_35r_co2eq():
    """
    GHG emissions by region and type fo gas
    """
    return (
        ghg_all_emissions_35r()
        * unit_conversion_t_gt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: gwp_20_year(),
            lambda: gwp_100_year(),
        )
        / unit_conversion_tco2eq_mtco2eq()
    )


@component.add(
    name="GHG all emissions 35R CO2eq total",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_all_emissions_35r_co2eq": 1},
)
def ghg_all_emissions_35r_co2eq_total():
    return sum(
        ghg_all_emissions_35r_co2eq().rename({"GHG I": "GHG I!"}), dim=["GHG I!"]
    )


@component.add(
    name="GHG all emissions EU27",
    units="Gt/Year",
    subscripts=["REGIONS 36 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_all_emissions_35r": 1},
)
def ghg_all_emissions_eu27():
    return sum(
        ghg_all_emissions_35r()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    ).expand_dims({"REGIONS 36 I": ["EU27"]}, 0)


@component.add(
    name="GHG coal extraction emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I", "SECTORS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "extraction_of_coal": 2,
        "underground_coal_mining_emission_factors": 1,
        "ghg_volume_to_mass_conversion_factor": 2,
        "unit_conversion_t_mt": 2,
        "unit_conversion_mt_ej": 2,
        "surface_coal_mining_emission_factors": 1,
        "pe_by_commodity": 1,
        "world_pe_by_commodity": 1,
    },
)
def ghg_coal_extraction_emissions():
    """
    Greenhouse gas emissions emitted during the mining process in coal mines. Surface mines and underground mines have different emission factors and in this variable the assumption that all hard coal is mined in underground mines and all brown coal is mined in surface mines is taken: https://www.britannica.com/technology/coal-mining/Choosing-a-mining-method
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "GHG I": _subscript_dict["GHG I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 9 I", "GHG I", "SECTORS I"],
    )
    value.loc[:, _subscript_dict["GHG ENERGY USE I"], ["MINING COAL"]] = (
        (
            (
                float(extraction_of_coal().loc["HARD COAL"])
                * underground_coal_mining_emission_factors()
                * ghg_volume_to_mass_conversion_factor()
                * unit_conversion_t_mt()
                * float(unit_conversion_mt_ej().loc["HARD COAL"])
                + float(extraction_of_coal().loc["BROWN COAL"])
                * surface_coal_mining_emission_factors()
                * ghg_volume_to_mass_conversion_factor()
                * unit_conversion_t_mt()
                * float(unit_conversion_mt_ej().loc["BROWN COAL"])
            )
            * zidz(
                pe_by_commodity().loc[:, "PE coal"].reset_coords(drop=True),
                float(world_pe_by_commodity().loc["PE coal"]),
            )
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["GHG ENERGY USE I"], ["MINING COAL"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG EMISSION FACTORS RESIDENTIAL STATIONARY COMBUSTION",
    units="kg/TJ",
    subscripts=["NRG FE I", "GHG I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_ghg_emission_factors_residential_stationary_combustion"
    },
)
def ghg_emission_factors_residential_stationary_combustion():
    """
    Greenhouse gas emission factors in stationary combustion systems by type final energy and type of gas ( CO2, CH4 and N2O ) in kg/TJ.
    """
    value = xr.DataArray(
        np.nan,
        {"NRG FE I": _subscript_dict["NRG FE I"], "GHG I": _subscript_dict["GHG I"]},
        ["NRG FE I", "GHG I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CO2", "CH4", "N2O"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_ghg_emission_factors_residential_stationary_combustion().values[
        def_subs.values
    ]
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["GHG ENERGY USE I"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_constant_ghg_emission_factors_residential_stationary_combustion = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_STATIONARY_COM",
    "GHG_EMISSION_FACTORS_RESIDENTIAL_STATIONARY_COMBUSTION",
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "GHG I": _subscript_dict["GHG ENERGY USE I"],
    },
    _root,
    {"NRG FE I": _subscript_dict["NRG FE I"], "GHG I": _subscript_dict["GHG I"]},
    "_ext_constant_ghg_emission_factors_residential_stationary_combustion",
)


@component.add(
    name="GHG EMISSION FACTORS STATIONARY COMBUSTION",
    units="kg/TJ",
    subscripts=["NRG FE I", "GHG I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_constant_ghg_emission_factors_stationary_combustion"
    },
)
def ghg_emission_factors_stationary_combustion():
    """
    Greenhouse gas emission factors in stationary combustion systems by type final energy and type of gas ( CO2, CH4 and N2O ) in kg/TJ.
    """
    value = xr.DataArray(
        np.nan,
        {"NRG FE I": _subscript_dict["NRG FE I"], "GHG I": _subscript_dict["GHG I"]},
        ["NRG FE I", "GHG I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["CO2", "CH4", "N2O"]] = True
    value.values[
        def_subs.values
    ] = _ext_constant_ghg_emission_factors_stationary_combustion().values[
        def_subs.values
    ]
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["GHG ENERGY USE I"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_constant_ghg_emission_factors_stationary_combustion = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_STATIONARY_COM",
    "GHG_EMISSION_FACTORS_STATIONARY_COMBUSTION",
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "GHG I": _subscript_dict["GHG ENERGY USE I"],
    },
    _root,
    {"NRG FE I": _subscript_dict["NRG FE I"], "GHG I": _subscript_dict["GHG I"]},
    "_ext_constant_ghg_emission_factors_stationary_combustion",
)


@component.add(
    name="GHG emissions all energy chain 35R total",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_all_energy_chain_by_sector_35r": 1},
)
def ghg_emissions_all_energy_chain_35r_total():
    return sum(
        ghg_emissions_all_energy_chain_by_sector_35r().rename(
            {"SECTORS I": "SECTORS I!"}
        ),
        dim=["SECTORS I!"],
    )


@component.add(
    name="GHG emissions all energy chain 9R",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_by_protra_sectors_9r": 5,
        "ghg_fugitive_emissions_refining": 1,
        "ghg_fugitive_emissions_supply": 1,
        "ghg_coal_extraction_emissions": 1,
        "ghg_oil_extraction_emissions": 1,
        "ghg_nat_gas_extraction_emissions": 1,
    },
)
def ghg_emissions_all_energy_chain_9r():
    """
    GHG emissions of PROTRA sectors and the rest of all energy chain.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG I"],
    )
    value.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_emissions_by_protra_sectors_9r()
        .loc[:, "ELECTRICITY GAS", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims(
            {"CLUSTER GAS POWER PLANTS": _subscript_dict["CLUSTER GAS POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_emissions_by_protra_sectors_9r()
        .loc[:, "ELECTRICITY OIL", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims(
            {"CLUSTER OIL POWER PLANTS": _subscript_dict["CLUSTER OIL POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_emissions_by_protra_sectors_9r()
        .loc[:, "ELECTRICITY COAL", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims(
            {"CLUSTER COAL POWER PLANTS": _subscript_dict["CLUSTER COAL POWER PLANTS"]},
            1,
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_emissions_by_protra_sectors_9r()
        .loc[:, "ELECTRICITY OTHER", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims(
            {
                "CLUSTER BIOMASS POWER PLANTS": _subscript_dict[
                    "CLUSTER BIOMASS POWER PLANTS"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_emissions_by_protra_sectors_9r()
        .loc[:, "STEAM HOT WATER", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS ENERGY I"], :] = True
    except_subs.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["DISTRIBUTION GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :] = True
    except_subs.loc[:, ["EXTRACTION GAS"], :] = False
    except_subs.loc[:, ["MINING COAL"], :] = False
    except_subs.loc[:, ["EXTRACTION OIL"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_fugitive_emissions_refining()
        .loc[:, "REFINING", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    value.loc[:, ["DISTRIBUTION GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_fugitive_emissions_supply()
        .loc[:, "DISTRIBUTION GAS", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], :] = (
        ghg_coal_extraction_emissions()
        .loc[:, :, "MINING COAL"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION OIL"], :] = (
        ghg_oil_extraction_emissions()
        .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION OIL"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION OIL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION GAS"], :] = (
        ghg_nat_gas_extraction_emissions()
        .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION GAS"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION GAS"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG emissions all energy chain by sector 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "base_output_real": 1,
        "ghg_emissions_all_energy_chain_per_unit_of_sector_output_35r": 2,
        "unit_conversion_mt_t": 2,
        "output_real": 1,
    },
)
def ghg_emissions_all_energy_chain_by_sector_35r():
    return if_then_else(
        switch_energy() == 0,
        lambda: ghg_emissions_all_energy_chain_per_unit_of_sector_output_35r()
        * base_output_real()
        * unit_conversion_mt_t(),
        lambda: ghg_emissions_all_energy_chain_per_unit_of_sector_output_35r()
        * output_real()
        * unit_conversion_mt_t(),
    )


@component.add(
    name="GHG emissions all energy chain per unit of sector output 35R",
    units="t/Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_all_energy_chain_per_unit_of_sector_output_9r": 2},
)
def ghg_emissions_all_energy_chain_per_unit_of_sector_output_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = (
        ghg_emissions_all_energy_chain_per_unit_of_sector_output_9r()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], :, :] = (
        ghg_emissions_all_energy_chain_per_unit_of_sector_output_9r()
        .loc["EU27", :, :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0)
        .values
    )
    return value


@component.add(
    name="GHG emissions all energy chain per unit of sector output 9R",
    units="t/Mdollars 2015",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "base_output_real": 2,
        "ghg_emissions_all_energy_chain_9r": 4,
        "unit_conversion_t_mt": 4,
        "output_real_9r": 2,
    },
)
def ghg_emissions_all_energy_chain_per_unit_of_sector_output_9r():
    """
    In the second equation, the BASE OUTPUT REAL[EU27, SECTORS I, GHG I] subscript component does not exist -> it is calculated via SUM( x[i!] )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = if_then_else(
        switch_energy() == 0,
        lambda: zidz(
            ghg_emissions_all_energy_chain_9r()
            .loc[_subscript_dict["REGIONS 8 I"], :, :]
            .rename({"REGIONS 9 I": "REGIONS 8 I"}),
            base_output_real()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 35 I": "REGIONS 8 I"})
            .expand_dims({"GHG I": _subscript_dict["GHG I"]}, 2),
        )
        * unit_conversion_t_mt(),
        lambda: zidz(
            ghg_emissions_all_energy_chain_9r()
            .loc[_subscript_dict["REGIONS 8 I"], :, :]
            .rename({"REGIONS 9 I": "REGIONS 8 I"}),
            output_real_9r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            .expand_dims({"GHG I": _subscript_dict["GHG I"]}, 2),
        )
        * unit_conversion_t_mt(),
    ).values
    value.loc[["EU27"], :, :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: zidz(
                ghg_emissions_all_energy_chain_9r()
                .loc["EU27", :, :]
                .reset_coords(drop=True),
                sum(
                    base_output_real()
                    .loc[_subscript_dict["REGIONS EU27 I"], :]
                    .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                    dim=["REGIONS EU27 I!"],
                ).expand_dims({"GHG I": _subscript_dict["GHG I"]}, 1),
            )
            * unit_conversion_t_mt(),
            lambda: zidz(
                ghg_emissions_all_energy_chain_9r()
                .loc["EU27", :, :]
                .reset_coords(drop=True),
                output_real_9r()
                .loc["EU27", :]
                .reset_coords(drop=True)
                .expand_dims({"GHG I": _subscript_dict["GHG I"]}, 1),
            )
            * unit_conversion_t_mt(),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="GHG emissions by PROTRA sectors 9R",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ti_by_protra_and_commodity": 28,
        "share_to_elec_chp_plants": 14,
        "emission_factors_stationary_combustion": 39,
        "unit_conversion_kg_mt": 5,
        "unit_conversion_tj_ej": 5,
    },
)
def ghg_emissions_by_protra_sectors_9r():
    """
    Greenhouse gas emissions in energy production sectors ( elec and heat ), by region, energy production sector and type of gas, in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG I"],
    )
    value.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP gas fuels"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels CCS",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP gas fuels",
                    "TI gas fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER GAS POWER PLANTS": _subscript_dict["CLUSTER GAS POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP liquid fuels"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels CCS",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP liquid fuels",
                    "TI liquid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER OIL POWER PLANTS": _subscript_dict["CLUSTER OIL POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP solid fossil"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER COAL POWER PLANTS": _subscript_dict["CLUSTER COAL POWER PLANTS"]},
            1,
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP waste", "TI waste"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP waste"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP waste", "TI waste"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP waste",
                        "TI waste",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP waste CCS",
                        "TI waste",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid bio", "TI solid bio"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP solid bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP solid bio",
                    "TI solid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP solid bio", "TI solid bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP solid bio",
                    "TI solid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid bio"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP liquid fuels"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP liquid fuels",
                    "TI liquid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP liquid fuels", "TI liquid bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP liquid fuels",
                    "TI liquid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas bio"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP gas fuels"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP gas fuels",
                    "TI gas bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP gas fuels", "TI gas bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP gas fuels",
                    "TI gas bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {
                "CLUSTER BIOMASS POWER PLANTS": _subscript_dict[
                    "CLUSTER BIOMASS POWER PLANTS"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP solid fossil"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP solid fossil",
                    "TI solid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid bio", "TI solid bio"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP solid bio"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid bio",
                        "TI solid bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid bio CCS",
                        "TI solid bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP solid bio", "TI solid bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP solid fossil",
                    "TI solid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP waste", "TI waste"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP waste"]
                    .reset_coords(drop=True)
                )
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP waste", "TI waste"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc["PROTRA HP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP liquid fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels CCS",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP liquid fuels",
                    "TI liquid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP gas fuels",
                    "TI gas fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP gas fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels CCS",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid bio"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP liquid fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels",
                        "TI liquid bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels CCS",
                        "TI liquid bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP liquid fuels", "TI liquid bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP liquid fuels",
                    "TI liquid bio",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP gas fuels", "TI gas bio"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP gas fuels",
                    "TI gas fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas bio"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP gas fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels",
                        "TI gas bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels CCS",
                        "TI gas bio",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG emissions by sector",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ti_by_protra_and_commodity": 16,
        "share_to_elec_chp_plants": 8,
        "emission_factors_stationary_combustion": 24,
        "unit_conversion_kg_mt": 9,
        "unit_conversion_tj_ej": 5,
        "final_energy_demand_bysectors_and_fe_9r": 4,
        "ghg_emission_factors_stationary_combustion": 4,
        "ghg_fugitive_emissions_refining": 1,
        "ghg_fugitive_emissions_supply": 1,
        "ghg_coal_extraction_emissions": 1,
        "ghg_oil_extraction_emissions": 1,
        "ghg_nat_gas_extraction_emissions": 1,
    },
)
def ghg_emissions_by_sector():
    """
    Greenhouse gas emissions by region, sector and type of gas ( CO2, CH4 and N2O ) taking into account the source of the gas emission in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG I"],
    )
    value.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP gas fuels"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels CCS",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP gas fuels",
                    "TI gas fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER GAS POWER PLANTS": _subscript_dict["CLUSTER GAS POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP liquid fuels"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels CCS",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA PP liquid fuels",
                    "TI liquid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER OIL POWER PLANTS": _subscript_dict["CLUSTER OIL POWER PLANTS"]}, 1
        )
        .values
    )
    value.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP solid fossil"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {"CLUSTER COAL POWER PLANTS": _subscript_dict["CLUSTER COAL POWER PLANTS"]},
            1,
        )
        .values
    )
    value.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP waste", "TI waste"]
                .reset_coords(drop=True)
                * share_to_elec_chp_plants()
                .loc[:, "PROTRA CHP waste"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA PP waste", "TI waste"]
                .reset_coords(drop=True)
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP waste",
                        "TI waste",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA PP waste CCS",
                        "TI waste",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims(
            {
                "CLUSTER BIOMASS POWER PLANTS": _subscript_dict[
                    "CLUSTER BIOMASS POWER PLANTS"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            (
                ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP solid fossil"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP solid fossil CCS",
                        "TI solid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP solid fossil", "TI solid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP solid fossil",
                    "TI solid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP waste", "TI waste"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP waste"]
                    .reset_coords(drop=True)
                )
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA CHP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP waste", "TI waste"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc["PROTRA HP waste", "TI waste", _subscript_dict["GHG ENERGY USE I"]]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP liquid fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP liquid fuels CCS",
                        "TI liquid fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP liquid fuels", "TI liquid fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP liquid fuels",
                    "TI liquid fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA HP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * emission_factors_stationary_combustion()
                .loc[
                    "PROTRA HP gas fuels",
                    "TI gas fossil",
                    _subscript_dict["GHG ENERGY USE I"],
                ]
                .reset_coords(drop=True)
                .rename({"GHG I": "GHG ENERGY USE I"})
                + ti_by_protra_and_commodity()
                .loc[:, "PROTRA CHP gas fuels", "TI gas fossil"]
                .reset_coords(drop=True)
                * (
                    1
                    - share_to_elec_chp_plants()
                    .loc[:, "PROTRA CHP gas fuels"]
                    .reset_coords(drop=True)
                )
                * (
                    emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                    - emission_factors_stationary_combustion()
                    .loc[
                        "PROTRA CHP gas fuels CCS",
                        "TI gas fossil",
                        _subscript_dict["GHG ENERGY USE I"],
                    ]
                    .reset_coords(drop=True)
                    .rename({"GHG I": "GHG ENERGY USE I"})
                )
            )
            / unit_conversion_kg_mt()
            * unit_conversion_tj_ej()
        )
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS ENERGY I"], :] = True
    except_subs.loc[:, ["ELECTRICITY GAS"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY OIL"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["ELECTRICITY COAL"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["ELECTRICITY OTHER"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    except_subs.loc[:, ["STEAM HOT WATER"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = False
    except_subs.loc[:, ["DISTRIBUTION GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        False
    )
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :] = True
    except_subs.loc[:, ["EXTRACTION GAS"], :] = False
    except_subs.loc[:, ["MINING COAL"], :] = False
    except_subs.loc[:, ["EXTRACTION OIL"], :] = False
    value.values[except_subs.values] = (
        sum(
            final_energy_demand_bysectors_and_fe_9r().rename({"NRG FE I": "NRG FE I!"})
            * ghg_emission_factors_stationary_combustion().rename(
                {"NRG FE I": "NRG FE I!"}
            ),
            dim=["NRG FE I!"],
        )
        / unit_conversion_kg_mt()
    ).values[except_subs.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :].values]
    value.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_fugitive_emissions_refining()
        .loc[:, "REFINING", _subscript_dict["GHG ENERGY USE I"]]
        .reset_coords(drop=True)
        .rename({"GHG I": "GHG ENERGY USE I"})
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    value.loc[:, ["DISTRIBUTION GAS"], _subscript_dict["GHG ENERGY USE I"]] = (
        ghg_fugitive_emissions_supply()
        .loc[:, "DISTRIBUTION GAS", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], :] = (
        (
            ghg_coal_extraction_emissions()
            .loc[:, :, "MINING COAL"]
            .reset_coords(drop=True)
            + sum(
                final_energy_demand_bysectors_and_fe_9r()
                .loc[:, "MINING COAL", :]
                .reset_coords(drop=True)
                .rename({"NRG FE I": "NRG FE I!"})
                * ghg_emission_factors_stationary_combustion().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION OIL"], :] = (
        (
            ghg_oil_extraction_emissions()
            .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION OIL"]
            .reset_coords(drop=True)
            .rename({"REGIONS 36 I": "REGIONS 9 I"})
            + sum(
                final_energy_demand_bysectors_and_fe_9r()
                .loc[:, "EXTRACTION OIL", :]
                .reset_coords(drop=True)
                .rename({"NRG FE I": "NRG FE I!"})
                * ghg_emission_factors_stationary_combustion().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION OIL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION GAS"], :] = (
        (
            ghg_nat_gas_extraction_emissions()
            .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION GAS"]
            .reset_coords(drop=True)
            .rename({"REGIONS 36 I": "REGIONS 9 I"})
            + sum(
                final_energy_demand_bysectors_and_fe_9r()
                .loc[:, "EXTRACTION GAS", :]
                .reset_coords(drop=True)
                .rename({"NRG FE I": "NRG FE I!"})
                * ghg_emission_factors_stationary_combustion().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION GAS"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG emissions by transport mode",
    units="g/(Year*km*person)",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r": 1,
        "passenger_transport_real_supply": 1,
        "unit_conversion_g_mt": 1,
    },
)
def ghg_emissions_by_transport_mode():
    """
    GHG emissions per cápita and km by transport mode.
    """
    return (
        zidz(
            sum(
                passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            ),
            sum(
                passenger_transport_real_supply().rename(
                    {
                        "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["TRANSPORT POWER TRAIN I!", "HOUSEHOLDS I!"],
            ).expand_dims({"GHG I": _subscript_dict["GHG I"]}, 2),
        )
        * unit_conversion_g_mt()
    )


@component.add(
    name="GHG emissions final energy by sector 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 11,
        "ghg_emission_factors_stationary_combustion": 1,
        "unit_conversion_kg_mt": 6,
        "emission_factors_public_transport": 10,
    },
)
def ghg_emissions_final_energy_by_sector_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "GHG I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TRANSPORT RAIL"], :] = False
    except_subs.loc[:, ["TRANSPORT OTHER LAND"], :] = False
    except_subs.loc[:, ["TRANSPORT SEA"], :] = False
    except_subs.loc[:, ["TRANSPORT INLAND WATER"], :] = False
    except_subs.loc[:, ["TRANSPORT AIR"], :] = False
    value.values[except_subs.values] = (
        sum(
            final_energy_demand_by_sector_and_fe().rename({"NRG FE I": "NRG FE I!"})
            * ghg_emission_factors_stationary_combustion().rename(
                {"NRG FE I": "NRG FE I!"}
            ),
            dim=["NRG FE I!"],
        )
        / unit_conversion_kg_mt()
    ).values[except_subs.values]
    value.loc[:, ["TRANSPORT RAIL"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT RAIL", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "RAIL", :]
                .reset_coords(drop=True)
                + final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT RAIL", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "RAIL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT RAIL"]}, 1)
        .values
    )
    value.loc[:, ["TRANSPORT OTHER LAND"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT OTHER LAND", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "BUS", :]
                .reset_coords(drop=True)
                + final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT OTHER LAND", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "BUS", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT OTHER LAND"]}, 1)
        .values
    )
    value.loc[:, ["TRANSPORT SEA"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT SEA", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "MARINE", :]
                .reset_coords(drop=True)
                + final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT SEA", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "MARINE", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT SEA"]}, 1)
        .values
    )
    value.loc[:, ["TRANSPORT INLAND WATER"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT INLAND WATER", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "RAIL", :]
                .reset_coords(drop=True)
                + final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT INLAND WATER", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "MARINE", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT INLAND WATER"]}, 1)
        .values
    )
    value.loc[:, ["TRANSPORT AIR"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT AIR", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gasoline", "AIR INTERNATIONAL", :]
                .reset_coords(drop=True)
                + final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT AIR", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "AIR INTERNATIONAL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT AIR"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG emissions final energy by sector and FE economic classification",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I", "GHG I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"imv_ghg_emissions_final_energy_by_sector_and_fe_35r": 6},
)
def ghg_emissions_final_energy_by_sector_and_fe_economic_classification():
    """
    GHG emissions from final energy demand by sector and final energy in economic classification
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "SECTORS I", "SECTORS MAP I", "GHG I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["REFINING"], _subscript_dict["SECTORS NON ENERGY I"], :] = False
    except_subs.loc[
        :, ["HYDROGEN PRODUCTION"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = False
    except_subs.loc[
        :, ["DISTRIBUTION ELECTRICITY"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = False
    except_subs.loc[
        :, ["DISTRIBUTION GAS"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = False
    except_subs.loc[
        :, ["STEAM HOT WATER"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = False
    except_subs.loc[:, ["MINING COAL"], _subscript_dict["SECTORS NON ENERGY I"], :] = (
        False
    )
    value.values[except_subs.values] = 0
    value.loc[:, ["REFINING"], _subscript_dict["SECTORS NON ENERGY I"], :] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    value.loc[
        :, ["HYDROGEN PRODUCTION"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE hydrogen", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 1)
        .values
    )
    value.loc[
        :, ["DISTRIBUTION ELECTRICITY"], _subscript_dict["SECTORS NON ENERGY I"], :
    ] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE elec", :]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER ELECTRICITY TRANSPORT": _subscript_dict[
                    "CLUSTER ELECTRICITY TRANSPORT"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["DISTRIBUTION GAS"], _subscript_dict["SECTORS NON ENERGY I"], :] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE gas", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], _subscript_dict["SECTORS NON ENERGY I"], :] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE heat", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], _subscript_dict["SECTORS NON ENERGY I"], :] = (
        imv_ghg_emissions_final_energy_by_sector_and_fe_35r()
        .loc[:, :, "FE solid fossil", :]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG emissions final energy by sector and FE economic classification CO2eq",
    units="MtCO2eq/Year",
    subscripts=[
        "REGIONS 35 I",
        "SECTORS FINAL ENERGY I",
        "SECTORS NON ENERGY I",
        "GHG ENERGY USE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_final_energy_by_sector_and_fe_economic_classification": 3,
        "unit_conversion_t_mt": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_tco2eq_mtco2eq": 3,
    },
)
def ghg_emissions_final_energy_by_sector_and_fe_economic_classification_co2eq():
    """
    Final energy demand by sector and final energy in economic classification
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        [
            "REGIONS 35 I",
            "SECTORS FINAL ENERGY I",
            "SECTORS NON ENERGY I",
            "GHG ENERGY USE I",
        ],
    )
    value.loc[:, :, :, ["CO2"]] = (
        (
            ghg_emissions_final_energy_by_sector_and_fe_economic_classification()
            .loc[
                :,
                _subscript_dict["SECTORS FINAL ENERGY I"],
                _subscript_dict["SECTORS NON ENERGY I"],
                "CO2",
            ]
            .reset_coords(drop=True)
            .rename(
                {
                    "SECTORS I": "SECTORS FINAL ENERGY I",
                    "SECTORS MAP I": "SECTORS NON ENERGY I",
                }
            )
            * unit_conversion_t_mt()
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CO2"]),
                lambda: float(gwp_100_year().loc["CO2"]),
            )
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 3)
        .values
    )
    value.loc[:, :, :, ["CH4"]] = (
        (
            ghg_emissions_final_energy_by_sector_and_fe_economic_classification()
            .loc[
                :,
                _subscript_dict["SECTORS FINAL ENERGY I"],
                _subscript_dict["SECTORS NON ENERGY I"],
                "CH4",
            ]
            .reset_coords(drop=True)
            .rename(
                {
                    "SECTORS I": "SECTORS FINAL ENERGY I",
                    "SECTORS MAP I": "SECTORS NON ENERGY I",
                }
            )
            * unit_conversion_t_mt()
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CH4"]),
                lambda: float(gwp_100_year().loc["CH4"]),
            )
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 3)
        .values
    )
    value.loc[:, :, :, ["N2O"]] = (
        (
            ghg_emissions_final_energy_by_sector_and_fe_economic_classification()
            .loc[
                :,
                _subscript_dict["SECTORS FINAL ENERGY I"],
                _subscript_dict["SECTORS NON ENERGY I"],
                "N2O",
            ]
            .reset_coords(drop=True)
            .rename(
                {
                    "SECTORS I": "SECTORS FINAL ENERGY I",
                    "SECTORS MAP I": "SECTORS NON ENERGY I",
                }
            )
            * unit_conversion_t_mt()
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["N2O"]),
                lambda: float(gwp_100_year().loc["N2O"]),
            )
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 3)
        .values
    )
    return value


@component.add(
    name="GHG emissions households 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 1,
        "unit_conversion_t_kg": 1,
        "unit_conversion_t_mt": 1,
        "private_transport_ghg_emissions_35r": 1,
    },
)
def ghg_emissions_households_35r():
    return (
        buildings_ghg_emissions_end_use_energy_by_fe_35r()
        * unit_conversion_t_kg()
        / unit_conversion_t_mt()
        + private_transport_ghg_emissions_35r()
    )


@component.add(
    name="GHG emissions households COICOP 35 R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 7,
        "unit_conversion_t_kg": 7,
        "unit_conversion_t_mt": 7,
        "private_transport_ghg_emissions_35r": 7,
    },
)
def ghg_emissions_households_coicop_35_r():
    """
    Housheolds GHG emissions by COICOP category
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG I"],
    )
    value.loc[:, ["HH ELECTRICITY"], :] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE elec", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE elec", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP ENERGY BUILDINGS I": ["HH ELECTRICITY"]}, 1)
        .values
    )
    value.loc[:, ["HH GAS"], :] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE gas", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE gas", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE hydrogen", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE hydrogen", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP ENERGY BUILDINGS I": ["HH GAS"]}, 1)
        .values
    )
    value.loc[:, ["HH HEAT"], :] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE heat", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE heat", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP ENERGY BUILDINGS I": ["HH HEAT"]}, 1)
        .values
    )
    value.loc[:, ["HH LIQUID FUELS"], :] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE liquid", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
        )
        .expand_dims({"COICOP ENERGY BUILDINGS I": ["HH LIQUID FUELS"]}, 1)
        .values
    )
    value.loc[:, ["HH FUEL TRANSPORT"], :] = (
        private_transport_ghg_emissions_35r()
        .loc[:, "FE liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"COICOP ENERGY I": ["HH FUEL TRANSPORT"]}, 1)
        .values
    )
    value.loc[:, ["HH SOLID FUELS"], :] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE solid bio", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE solid bio", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE solid fossil", :]
            .reset_coords(drop=True)
            * unit_conversion_t_kg()
            / unit_conversion_t_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE solid fossil", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"COICOP ENERGY BUILDINGS I": ["HH SOLID FUELS"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["COICOP NON ENERGY I"], :] = 0
    return value


@component.add(
    name="GHG emissions households COICOP 35 R CO2eq",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_households_coicop_35_r": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_t_mt": 3,
        "unit_conversion_tco2eq_mtco2eq": 3,
    },
)
def ghg_emissions_households_coicop_35_r_co2eq():
    """
    GHG emissions from households by COICOP category.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    )
    value.loc[:, :, ["CO2"]] = (
        (
            ghg_emissions_households_coicop_35_r()
            .loc[:, :, "CO2"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CO2"]),
                lambda: float(gwp_100_year().loc["CO2"]),
            )
            * unit_conversion_t_mt()
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 2)
        .values
    )
    value.loc[:, :, ["CH4"]] = (
        (
            ghg_emissions_households_coicop_35_r()
            .loc[:, :, "CH4"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CH4"]),
                lambda: float(gwp_100_year().loc["CH4"]),
            )
            * unit_conversion_t_mt()
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 2)
        .values
    )
    value.loc[:, :, ["N2O"]] = (
        (
            ghg_emissions_households_coicop_35_r()
            .loc[:, :, "N2O"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["N2O"]),
                lambda: float(gwp_100_year().loc["N2O"]),
            )
            * unit_conversion_t_mt()
            / unit_conversion_tco2eq_mtco2eq()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 2)
        .values
    )
    return value


@component.add(
    name="GHG emissions households total",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_households_coicop_35_r_co2eq": 1},
)
def ghg_emissions_households_total():
    """
    GHG emissions from households
    """
    return sum(
        ghg_emissions_households_coicop_35_r_co2eq().rename(
            {"COICOP I": "COICOP I!", "GHG ENERGY USE I": "GHG ENERGY USE I!"}
        ),
        dim=["COICOP I!", "GHG ENERGY USE I!"],
    )


@component.add(
    name="GHG emissions in energy consuming sectors",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emission_factors_stationary_combustion": 1,
        "final_energy_demand_by_fe": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def ghg_emissions_in_energy_consuming_sectors():
    """
    Greenhouse gas emissions in energy consuming sectors by region, type of final energy and type of gas, in Mt/year.
    """
    return (
        (
            ghg_emission_factors_stationary_combustion()
            * final_energy_demand_by_fe().transpose("NRG FE I", "REGIONS 9 I")
        )
        / unit_conversion_kg_mt()
    ).transpose("REGIONS 9 I", "NRG FE I", "GHG I")


@component.add(
    name="GHG emissions per unit of sector output",
    units="t/Mdollars 2015",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_by_sector": 1,
        "output_real_9r": 1,
        "unit_conversion_t_mt": 1,
    },
)
def ghg_emissions_per_unit_of_sector_output():
    """
    Intensity of GHG emissions by sector and type of gas in t/M$
    """
    return (
        zidz(
            ghg_emissions_by_sector(),
            output_real_9r().expand_dims({"GHG I": _subscript_dict["GHG I"]}, 2),
        )
        * unit_conversion_t_mt()
    )


@component.add(
    name="GHG energy emissions 35R CO2eq total",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_ghg_energy_emissions_35r_co2eq": 1},
)
def ghg_energy_emissions_35r_co2eq_total():
    return sum(
        imv_ghg_energy_emissions_35r_co2eq().rename(
            {"GHG ENERGY USE I": "GHG ENERGY USE I!"}
        ),
        dim=["GHG ENERGY USE I!"],
    )


@component.add(
    name="GHG energy emissions by sector 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_all_energy_chain_by_sector_35r": 4,
        "ghg_emissions_final_energy_by_sector_35r": 4,
    },
)
def ghg_energy_emissions_by_sector_35r():
    """
    GHG emissions all energy sector chain sectors and final energy demand in non-energy sectors.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG I"],
    )
    value.loc[:, _subscript_dict["SECTORS ENERGY I"], :] = (
        ghg_emissions_all_energy_chain_by_sector_35r()
        .loc[:, _subscript_dict["SECTORS ENERGY I"], :]
        .rename({"SECTORS I": "SECTORS ENERGY I"})
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :] = True
    except_subs.loc[:, ["EXTRACTION GAS"], :] = False
    except_subs.loc[:, ["MINING COAL"], :] = False
    except_subs.loc[:, ["EXTRACTION OIL"], :] = False
    value.values[
        except_subs.values
    ] = ghg_emissions_final_energy_by_sector_35r().values[
        except_subs.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :].values
    ]
    value.loc[:, ["EXTRACTION GAS"], :] = (
        (
            ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "EXTRACTION GAS", :]
            .reset_coords(drop=True)
            + ghg_emissions_final_energy_by_sector_35r()
            .loc[:, "EXTRACTION GAS", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], :] = (
        (
            ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "MINING COAL", :]
            .reset_coords(drop=True)
            + ghg_emissions_final_energy_by_sector_35r()
            .loc[:, "MINING COAL", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["EXTRACTION OIL"], :] = (
        (
            ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "EXTRACTION OIL", :]
            .reset_coords(drop=True)
            + ghg_emissions_final_energy_by_sector_35r()
            .loc[:, "EXTRACTION OIL", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION OIL"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG energy emissions households heating 35R CO2eq",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_tco2eq_gtco2eq": 3,
        "unit_conversion_mt_t": 3,
    },
)
def ghg_energy_emissions_households_heating_35r_co2eq():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "NRG FE I", "GHG ENERGY USE I"],
    )
    value.loc[:, :, ["CO2"]] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, :, "CO2"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CO2"]),
                lambda: float(gwp_100_year().loc["CO2"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 2)
        .values
    )
    value.loc[:, :, ["CH4"]] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, :, "CH4"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CH4"]),
                lambda: float(gwp_100_year().loc["CH4"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 2)
        .values
    )
    value.loc[:, :, ["N2O"]] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, :, "N2O"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["N2O"]),
                lambda: float(gwp_100_year().loc["N2O"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 2)
        .values
    )
    return value


@component.add(
    name="GHG energy emissions households private transport 35R CO2eq",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_transport_ghg_emissions_35r": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_tco2eq_gtco2eq": 3,
        "unit_conversion_mt_t": 3,
    },
)
def ghg_energy_emissions_households_private_transport_35r_co2eq():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "NRG FE I", "GHG ENERGY USE I"],
    )
    value.loc[:, :, ["CO2"]] = (
        (
            private_transport_ghg_emissions_35r()
            .loc[:, :, "CO2"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CO2"]),
                lambda: float(gwp_100_year().loc["CO2"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 2)
        .values
    )
    value.loc[:, :, ["CH4"]] = (
        (
            private_transport_ghg_emissions_35r()
            .loc[:, :, "CH4"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CH4"]),
                lambda: float(gwp_100_year().loc["CH4"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 2)
        .values
    )
    value.loc[:, :, ["N2O"]] = (
        (
            private_transport_ghg_emissions_35r()
            .loc[:, :, "N2O"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["N2O"]),
                lambda: float(gwp_100_year().loc["N2O"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 2)
        .values
    )
    return value


@component.add(
    name="GHG energy supply emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_fugitive_emissions_supply": 1},
)
def ghg_energy_supply_emissions():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "GHG I"],
    )
    value.loc[:, _subscript_dict["GHG ENERGY USE I"]] = sum(
        ghg_fugitive_emissions_supply().rename({"SECTORS I": "SECTORS I!"}),
        dim=["SECTORS I!"],
    ).values
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["GHG ENERGY USE I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG energy transformation emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_by_protra_sectors_9r": 1},
)
def ghg_energy_transformation_emissions():
    """
    Total greenhouse gas emissions generated in energy production sectors ( elec and heat )by region and type of gas, in Mt/year.
    """
    return sum(
        ghg_emissions_by_protra_sectors_9r().rename({"SECTORS I": "SECTORS I!"}),
        dim=["SECTORS I!"],
    )


@component.add(
    name="GHG extraction emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_coal_extraction_emissions": 1,
        "ghg_nat_gas_extraction_emissions": 1,
        "ghg_oil_extraction_emissions": 1,
    },
)
def ghg_extraction_emissions():
    """
    Greenhouse gas emissions generated by the extraction of fossil fuels, in Mt/year.
    """
    return (
        ghg_coal_extraction_emissions().loc[:, :, "MINING COAL"].reset_coords(drop=True)
        + ghg_nat_gas_extraction_emissions()
        .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION GAS"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        + ghg_oil_extraction_emissions()
        .loc[_subscript_dict["REGIONS 9 I"], :, "EXTRACTION OIL"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
    )


@component.add(
    name="GHG fugitive emissions refining",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "emission_factors_fugitives_refining": 2,
        "ti_by_proref_and_commodity": 3,
        "unit_conversion_toe_m3": 1,
        "unit_conversion_j_toe": 1,
        "unit_conversion_j_ej": 2,
        "unit_conversion_g_mt": 2,
        "unit_conversion_j_m3_nat_gas": 1,
        "emission_factors_coal_to_gas_production": 1,
        "unit_conversion_kg_mt": 1,
        "emission_factors_gas_to_liquid_production": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def ghg_fugitive_emissions_refining():
    """
    Greenhouse gas emissions due to fugitive emissions generated by the refining process, in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG I"],
    )
    value.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = (
        (
            emission_factors_fugitives_refining()
            .loc["PE oil", :]
            .reset_coords(drop=True)
            * ti_by_proref_and_commodity()
            .loc[:, "PROREF refinery oil", "TI liquid fossil"]
            .reset_coords(drop=True)
            * 1
            / unit_conversion_toe_m3()
            * 1
            / unit_conversion_j_toe()
            * unit_conversion_j_ej()
            / unit_conversion_g_mt()
            + emission_factors_fugitives_refining()
            .loc["PE natural gas", :]
            .reset_coords(drop=True)
            * ti_by_proref_and_commodity()
            .loc[:, "PROREF refinery oil", "TI gas fossil"]
            .reset_coords(drop=True)
            / unit_conversion_j_m3_nat_gas()
            * unit_conversion_j_ej()
            / unit_conversion_g_mt()
            + (
                emission_factors_coal_to_gas_production()
                + float(emission_factors_gas_to_liquid_production().loc["CO2"])
            )
            * ti_by_proref_and_commodity()
            .loc[:, "PROREF refinery coal", "TI gas fossil"]
            .reset_coords(drop=True)
            * unit_conversion_tj_ej()
            / unit_conversion_kg_mt()
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["REFINING"], _subscript_dict["GHG ENERGY USE I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG fugitive emissions supply",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "SECTORS I", "GHG ENERGY USE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "emission_factors_fugitives_supply": 2,
        "total_fe_including_net_trade": 2,
        "unit_conversion_j_ej": 2,
        "unit_conversion_j_m3_nat_gas": 1,
        "unit_conversion_g_mt": 2,
        "unit_conversion_j_toe": 1,
        "unit_conversion_toe_m3": 1,
    },
)
def ghg_fugitive_emissions_supply():
    """
    Greenhouse gas emissions due to fugitive emissions generated during the fossil fuel transport, in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 9 I", "SECTORS I", "GHG ENERGY USE I"],
    )
    value.loc[:, ["DISTRIBUTION GAS"], :] = (
        (
            (
                emission_factors_fugitives_supply()
                .loc["FE gas", :]
                .reset_coords(drop=True)
                * total_fe_including_net_trade()
                .loc[:, "FE gas"]
                .reset_coords(drop=True)
                * unit_conversion_j_ej()
                * 1
                / unit_conversion_j_m3_nat_gas()
            )
            / unit_conversion_g_mt()
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["TRANSPORT PIPELINE"], :] = (
        (
            (
                emission_factors_fugitives_supply()
                .loc["FE liquid", :]
                .reset_coords(drop=True)
                * total_fe_including_net_trade()
                .loc[:, "FE liquid"]
                .reset_coords(drop=True)
                * 1
                / unit_conversion_toe_m3()
                * 1
                / unit_conversion_j_toe()
                * unit_conversion_j_ej()
            )
            / unit_conversion_g_mt()
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims(
            {"CLUSTER GAS PIPELINES": _subscript_dict["CLUSTER GAS PIPELINES"]}, 1
        )
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["DISTRIBUTION GAS"], :] = False
    except_subs.loc[:, ["TRANSPORT PIPELINE"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG intensity emissions by FE 35R",
    units="Mt/EJ",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_protra_emissions_by_fe_35r": 1,
        "final_energy_demand_by_fe_35r": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def ghg_intensity_emissions_by_fe_35r():
    return zidz(
        ghg_protra_emissions_by_fe_35r(),
        (final_energy_demand_by_fe_35r() / unit_conversion_tj_ej()).expand_dims(
            {"GHG I": _subscript_dict["GHG I"]}, 2
        ),
    )


@component.add(
    name="GHG intensity of passenger transport 35R",
    units="g/(Year*km*person)",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "private_passenger_transport_ghg_emissions_all_energy_chain_35r": 1,
        "total_passenger_transport_demand": 1,
        "unit_conversion_g_mt": 1,
    },
)
def ghg_intensity_of_passenger_transport_35r():
    """
    GHG emissions per cápita and km.
    """
    return (
        zidz(
            sum(
                private_passenger_transport_ghg_emissions_all_energy_chain_35r().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            ),
            total_passenger_transport_demand().expand_dims(
                {"GHG I": _subscript_dict["GHG I"]}, 1
            ),
        )
        * unit_conversion_g_mt()
    )


@component.add(
    name="GHG nat gas extraction emissions",
    units="Mt/Year",
    subscripts=["REGIONS 36 I", "GHG I", "SECTORS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_pe_by_commodity": 2,
        "emission_factors_fugitives_extraction": 1,
        "unit_conversion_j_m3_nat_gas": 1,
        "unit_conversion_j_ej": 1,
        "unit_conversion_g_mt": 1,
        "pe_by_commodity": 1,
    },
)
def ghg_nat_gas_extraction_emissions():
    """
    Greenhouse gas emissions due to fugitive emissions generated by the extraction natural gas resources.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "GHG I": _subscript_dict["GHG I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 36 I", "GHG I", "SECTORS I"],
    )
    value.loc[
        _subscript_dict["REGIONS 9 I"],
        _subscript_dict["GHG ENERGY USE I"],
        ["EXTRACTION GAS"],
    ] = (
        (
            float(world_pe_by_commodity().loc["PE natural gas"])
            * emission_factors_fugitives_extraction()
            .loc["PE natural gas", :]
            .reset_coords(drop=True)
            / unit_conversion_j_m3_nat_gas()
            * unit_conversion_j_ej()
            / unit_conversion_g_mt()
            * zidz(
                pe_by_commodity().loc[:, "PE natural gas"].reset_coords(drop=True),
                float(world_pe_by_commodity().loc["PE natural gas"]),
            )
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION GAS"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[
        _subscript_dict["REGIONS 9 I"],
        _subscript_dict["GHG ENERGY USE I"],
        ["EXTRACTION GAS"],
    ] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG oil extraction emissions",
    units="Mt/Year",
    subscripts=["REGIONS 36 I", "GHG I", "SECTORS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "world_pe_by_commodity": 2,
        "emission_factors_fugitives_extraction": 1,
        "unit_conversion_toe_m3": 1,
        "unit_conversion_j_toe": 1,
        "unit_conversion_j_ej": 1,
        "unit_conversion_g_mt": 1,
        "pe_by_commodity": 1,
    },
)
def ghg_oil_extraction_emissions():
    """
    Greenhouse gas emissions due to fugitive emissions generated by the extraction of oil resources.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "GHG I": _subscript_dict["GHG I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 36 I", "GHG I", "SECTORS I"],
    )
    value.loc[
        _subscript_dict["REGIONS 9 I"],
        _subscript_dict["GHG ENERGY USE I"],
        ["EXTRACTION OIL"],
    ] = (
        (
            float(world_pe_by_commodity().loc["PE oil"])
            * emission_factors_fugitives_extraction()
            .loc["PE oil", :]
            .reset_coords(drop=True)
            / unit_conversion_toe_m3()
            / unit_conversion_j_toe()
            * unit_conversion_j_ej()
            / unit_conversion_g_mt()
            * zidz(
                pe_by_commodity().loc[:, "PE oil"].reset_coords(drop=True),
                float(world_pe_by_commodity().loc["PE oil"]),
            )
        )
        .transpose("REGIONS 9 I", "GHG ENERGY USE I")
        .expand_dims({"CLUSTER QUARRYING": ["EXTRACTION OIL"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[
        _subscript_dict["REGIONS 9 I"],
        _subscript_dict["GHG ENERGY USE I"],
        ["EXTRACTION OIL"],
    ] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="GHG PROTRA emissions by FE 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_all_energy_chain_by_sector_35r": 5,
        "private_transport_ghg_emissions_35r": 5,
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 5,
        "final_energy_demand_by_sector_and_fe": 5,
        "unit_conversion_kg_mt": 10,
        "ghg_emission_factors_stationary_combustion": 5,
    },
)
def ghg_protra_emissions_by_fe_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG FE I", "GHG I"],
    )
    value.loc[:, ["FE elec"], :] = (
        (
            ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "ELECTRICITY COAL", :]
            .reset_coords(drop=True)
            + ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "ELECTRICITY GAS", :]
            .reset_coords(drop=True)
            + ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "ELECTRICITY OIL", :]
            .reset_coords(drop=True)
            + ghg_emissions_all_energy_chain_by_sector_35r()
            .loc[:, "ELECTRICITY OTHER", :]
            .reset_coords(drop=True)
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE gas"], :] = (
        (
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[:, :, "FE gas"]
                .reset_coords(drop=True)
                .rename({"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}),
                dim=["SECTORS NON ENERGY I!"],
            )
            * ghg_emission_factors_stationary_combustion()
            .loc["FE gas", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE gas", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE gas", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"], :] = (
        ghg_emissions_all_energy_chain_by_sector_35r()
        .loc[:, "STEAM HOT WATER", :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"], :] = (
        (
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[:, :, "FE hydrogen"]
                .reset_coords(drop=True)
                .rename({"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}),
                dim=["SECTORS NON ENERGY I!"],
            )
            * ghg_emission_factors_stationary_combustion()
            .loc["FE hydrogen", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE hydrogen", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE hydrogen", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"], :] = (
        (
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[:, :, "FE liquid"]
                .reset_coords(drop=True)
                .rename({"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}),
                dim=["SECTORS NON ENERGY I!"],
            )
            * ghg_emission_factors_stationary_combustion()
            .loc["FE liquid", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE liquid", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE liquid", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"], :] = (
        (
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[:, :, "FE solid bio"]
                .reset_coords(drop=True)
                .rename({"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}),
                dim=["SECTORS NON ENERGY I!"],
            )
            * ghg_emission_factors_stationary_combustion()
            .loc["FE solid bio", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE solid bio", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE solid bio", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"], :] = (
        (
            sum(
                final_energy_demand_by_sector_and_fe()
                .loc[:, :, "FE solid fossil"]
                .reset_coords(drop=True)
                .rename({"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}),
                dim=["SECTORS NON ENERGY I!"],
            )
            * ghg_emission_factors_stationary_combustion()
            .loc["FE solid fossil", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
            + private_transport_ghg_emissions_35r()
            .loc[:, "FE solid fossil", :]
            .reset_coords(drop=True)
            + buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, "FE solid fossil", :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="GHG refining emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_fugitive_emissions_refining": 1},
)
def ghg_refining_emissions():
    """
    Greenhouse gas emissions generated by the refining process, in Mt/year.
    """
    return (
        ghg_fugitive_emissions_refining().loc[:, "REFINING", :].reset_coords(drop=True)
    )


@component.add(
    name="households end use energy emissions 9R",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_ghg_emissions_end_use_energy_35r": 2},
)
def households_end_use_energy_emissions_9r():
    """
    Greenhouse gas emissions generated in households by region ( 9 regions), type of final energy and type of gas, in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "GHG I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = sum(
        households_ghg_emissions_end_use_energy_35r()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 35 I": "REGIONS 8 I", "NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    ).values
    value.loc[["EU27"], :] = (
        sum(
            households_ghg_emissions_end_use_energy_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!", "NRG FE I": "NRG FE I!"}),
            dim=["REGIONS EU27 I!", "NRG FE I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="households GHG emissions end use energy 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "buildings_ghg_emissions_end_use_energy_by_fe_35r": 1,
        "private_passenger_transport_emissions_end_use_energy_by_fe": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def households_ghg_emissions_end_use_energy_35r():
    """
    Greenhouse gas emissions generated in households by region, type of final energy and type of gas, in Mt/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG FE I", "GHG I"],
    )
    value.loc[:, :, _subscript_dict["GHG ENERGY USE I"]] = (
        (
            buildings_ghg_emissions_end_use_energy_by_fe_35r()
            .loc[:, :, _subscript_dict["GHG ENERGY USE I"]]
            .rename({"GHG I": "GHG ENERGY USE I"})
            + private_passenger_transport_emissions_end_use_energy_by_fe()
            .loc[:, :, _subscript_dict["GHG ENERGY USE I"]]
            .rename({"GHG I": "GHG ENERGY USE I"})
        )
        / unit_conversion_kg_mt()
    ).values
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CO2"]] = False
    except_subs.loc[:, :, ["CH4"]] = False
    except_subs.loc[:, :, ["N2O"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="implicit CO2 emission factor FE sectors",
    units="MtCO2eq/TJ",
    subscripts=[
        "REGIONS 35 I",
        "SECTORS FINAL ENERGY I",
        "SECTORS NON ENERGY I",
        "GHG ENERGY USE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_final_energy_by_sector_and_fe_economic_classification_co2eq": 1,
        "final_energy_demand_by_final_energy_sector_and_non_energy_sector": 1,
    },
)
def implicit_co2_emission_factor_fe_sectors():
    """
    Implicit CO2 emission factor by sector of final energy and by non energy sectors
    """
    return zidz(
        ghg_emissions_final_energy_by_sector_and_fe_economic_classification_co2eq(),
        final_energy_demand_by_final_energy_sector_and_non_energy_sector().expand_dims(
            {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]}, 3
        ),
    )


@component.add(
    name="implicit GHG emission factor households COICOP",
    units="MtCO2eq/TJ",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_households_coicop_35_r_co2eq": 1,
        "final_energy_consumption_buildings_and_transport": 1,
    },
)
def implicit_ghg_emission_factor_households_coicop():
    """
    Households implicit GHG emission factor by COICOP category.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    )
    value.loc[:, _subscript_dict["COICOP ENERGY I"], :] = zidz(
        ghg_emissions_households_coicop_35_r_co2eq()
        .loc[:, _subscript_dict["COICOP ENERGY I"], :]
        .rename({"COICOP I": "COICOP ENERGY I"}),
        final_energy_consumption_buildings_and_transport().expand_dims(
            {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]}, 2
        ),
    ).values
    value.loc[:, _subscript_dict["COICOP NON ENERGY I"], :] = 0
    return value


@component.add(
    name="IMV GHG emissions final energy by sector and FE 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 11,
        "ghg_emission_factors_stationary_combustion": 1,
        "unit_conversion_kg_mt": 11,
        "emission_factors_public_transport": 10,
    },
)
def imv_ghg_emissions_final_energy_by_sector_and_fe_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I", "GHG I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TRANSPORT RAIL"], ["FE liquid"], :] = False
    except_subs.loc[:, ["TRANSPORT OTHER LAND"], ["FE liquid"], :] = False
    except_subs.loc[:, ["TRANSPORT SEA"], ["FE liquid"], :] = False
    except_subs.loc[:, ["TRANSPORT INLAND WATER"], ["FE liquid"], :] = False
    except_subs.loc[:, ["TRANSPORT AIR"], ["FE liquid"], :] = False
    except_subs.loc[:, ["TRANSPORT RAIL"], ["FE gas"], :] = False
    except_subs.loc[:, ["TRANSPORT OTHER LAND"], ["FE gas"], :] = False
    except_subs.loc[:, ["TRANSPORT SEA"], ["FE gas"], :] = False
    except_subs.loc[:, ["TRANSPORT INLAND WATER"], ["FE gas"], :] = False
    except_subs.loc[:, ["TRANSPORT AIR"], ["FE gas"], :] = False
    value.values[except_subs.values] = (
        (
            final_energy_demand_by_sector_and_fe()
            * ghg_emission_factors_stationary_combustion()
        )
        / unit_conversion_kg_mt()
    ).values[except_subs.values]
    value.loc[:, ["TRANSPORT RAIL"], ["FE liquid"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT RAIL", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "RAIL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT RAIL"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT OTHER LAND"], ["FE liquid"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT OTHER LAND", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "BUS", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT OTHER LAND"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT SEA"], ["FE liquid"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT SEA", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "MARINE", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT SEA"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT INLAND WATER"], ["FE liquid"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT INLAND WATER", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE diesel", "RAIL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT INLAND WATER"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT AIR"], ["FE liquid"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT AIR", "FE liquid"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gasoline", "AIR INTERNATIONAL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT AIR"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT RAIL"], ["FE gas"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT RAIL", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "RAIL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT RAIL"]}, 1)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT OTHER LAND"], ["FE gas"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT OTHER LAND", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "BUS", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT OTHER LAND"]}, 1)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT SEA"], ["FE gas"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT SEA", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "MARINE", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT SEA"]}, 1)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT INLAND WATER"], ["FE gas"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT INLAND WATER", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "MARINE", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT INLAND WATER"]}, 1)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, ["TRANSPORT AIR"], ["FE gas"], :] = (
        (
            (
                final_energy_demand_by_sector_and_fe()
                .loc[:, "TRANSPORT AIR", "FE gas"]
                .reset_coords(drop=True)
                * emission_factors_public_transport()
                .loc["ICE gas", "AIR INTERNATIONAL", :]
                .reset_coords(drop=True)
            )
            / unit_conversion_kg_mt()
        )
        .expand_dims({"CLUSTER TRANSPORT": ["TRANSPORT AIR"]}, 1)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    return value


@component.add(
    name="IMV GHG energy emissions 35R CO2eq",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_energy_emissions_by_sector_35r": 3,
        "gwp_100_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_20_year": 3,
        "unit_conversion_tco2eq_gtco2eq": 3,
        "unit_conversion_mt_t": 3,
    },
)
def imv_ghg_energy_emissions_35r_co2eq():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    )
    value.loc[:, :, ["CO2"]] = (
        (
            ghg_energy_emissions_by_sector_35r()
            .loc[:, :, "CO2"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CO2"]),
                lambda: float(gwp_100_year().loc["CO2"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 2)
        .values
    )
    value.loc[:, :, ["CH4"]] = (
        (
            ghg_energy_emissions_by_sector_35r()
            .loc[:, :, "CH4"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["CH4"]),
                lambda: float(gwp_100_year().loc["CH4"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 2)
        .values
    )
    value.loc[:, :, ["N2O"]] = (
        (
            ghg_energy_emissions_by_sector_35r()
            .loc[:, :, "N2O"]
            .reset_coords(drop=True)
            * if_then_else(
                select_gwp_time_frame_sp() == 1,
                lambda: float(gwp_20_year().loc["N2O"]),
                lambda: float(gwp_100_year().loc["N2O"]),
            )
            / unit_conversion_tco2eq_gtco2eq()
            / unit_conversion_mt_t()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 2)
        .values
    )
    return value


@component.add(
    name="IMV GHG energy emissions 35R CO2eq until 2015",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_imv_ghg_energy_emissions_35r_co2eq_until_2015": 1},
    other_deps={
        "_sampleiftrue_imv_ghg_energy_emissions_35r_co2eq_until_2015": {
            "initial": {"imv_ghg_energy_emissions_35r_co2eq": 1},
            "step": {"time": 1, "imv_ghg_energy_emissions_35r_co2eq": 1},
        }
    },
)
def imv_ghg_energy_emissions_35r_co2eq_until_2015():
    """
    Variable used to isolate the economic module, when the switch is deactivated. When this happens the variable takes the 2015 values.
    """
    return _sampleiftrue_imv_ghg_energy_emissions_35r_co2eq_until_2015()


_sampleiftrue_imv_ghg_energy_emissions_35r_co2eq_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "GHG ENERGY USE I"],
    ),
    lambda: imv_ghg_energy_emissions_35r_co2eq(),
    lambda: imv_ghg_energy_emissions_35r_co2eq(),
    "_sampleiftrue_imv_ghg_energy_emissions_35r_co2eq_until_2015",
)


@component.add(
    name="INITIAL DELAYED CO2 EMISSIONS FACTOR FE SECTOR",
    units="MtCO2eq/TJ",
    subscripts=[
        "REGIONS 35 I",
        "SECTORS FINAL ENERGY I",
        "SECTORS NON ENERGY I",
        "GHG ENERGY USE I",
    ],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_delayed_co2_emissions_factor_fe_sector": 1},
    other_deps={
        "_initial_initial_delayed_co2_emissions_factor_fe_sector": {
            "initial": {"implicit_co2_emission_factor_fe_sectors": 1},
            "step": {},
        }
    },
)
def initial_delayed_co2_emissions_factor_fe_sector():
    """
    Initila implicit CO2 emission factor by sector of final energy and by non energy sectors
    """
    return _initial_initial_delayed_co2_emissions_factor_fe_sector()


_initial_initial_delayed_co2_emissions_factor_fe_sector = Initial(
    lambda: implicit_co2_emission_factor_fe_sectors(),
    "_initial_initial_delayed_co2_emissions_factor_fe_sector",
)


@component.add(
    name="initial share passengers private transport by type of power train",
    units="1",
    subscripts=["REGIONS 35 I", "TRANSPORT POWER TRAIN I", "PRIVATE TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_passenger_private_fleet_by_type_of_hh": 2},
)
def initial_share_passengers_private_transport_by_type_of_power_train():
    """
    Initial share of passengers transport by type of power train (share of gasoline_engine, diesel_engines,...)
    """
    return zidz(
        sum(
            initial_passenger_private_fleet_by_type_of_hh().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        ),
        sum(
            initial_passenger_private_fleet_by_type_of_hh().rename(
                {
                    "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                    "PRIVATE TRANSPORT I": "PRIVATE TRANSPORT I!",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["TRANSPORT POWER TRAIN I!", "PRIVATE TRANSPORT I!", "HOUSEHOLDS I!"],
        )
        .expand_dims(
            {"TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"]}, 1
        )
        .expand_dims(
            {"PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"]}, 2
        ),
    )


@component.add(
    name="passenger transport emissions end use energy",
    units="kg/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "energy_passenger_transport_consumption": 4,
        "share_elec_in_phev": 2,
        "emission_factors_private_transport": 2,
        "unit_conversion_j_mj": 4,
        "unit_conversion_j_tj": 4,
        "emission_factors_public_transport": 2,
    },
)
def passenger_transport_emissions_end_use_energy():
    """
    Greenhouse gas emissions generated by passengers transport vehicles, by region, power train, transport mode and type of gas, in kg/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "GHG I",
        ],
    )
    value.loc[:, ["PHEV"], _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[:, "PHEV", _subscript_dict["PRIVATE TRANSPORT I"], :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * (1 - share_elec_in_phev())
            * emission_factors_private_transport()
            .loc["PHEV", :, :]
            .reset_coords(drop=True)
            * unit_conversion_j_mj()
            / unit_conversion_j_tj()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .values
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = True
    except_subs.loc[:, ["PHEV"], _subscript_dict["PRIVATE TRANSPORT I"], :] = False
    value.values[except_subs.values] = (
        sum(
            energy_passenger_transport_consumption()
            .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["HOUSEHOLDS I!"],
        )
        * emission_factors_private_transport()
        * unit_conversion_j_mj()
        / unit_conversion_j_tj()
    ).values[except_subs.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :].values]
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = True
    except_subs.loc[:, ["PHEV"], _subscript_dict["PUBLIC TRANSPORT I"], :] = False
    value.values[except_subs.values] = (
        sum(
            energy_passenger_transport_consumption()
            .loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :]
            .rename(
                {
                    "PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I",
                    "HOUSEHOLDS I": "HOUSEHOLDS I!",
                }
            ),
            dim=["HOUSEHOLDS I!"],
        )
        * emission_factors_public_transport()
        * unit_conversion_j_mj()
        / unit_conversion_j_tj()
    ).values[except_subs.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :].values]
    value.loc[:, ["PHEV"], _subscript_dict["PUBLIC TRANSPORT I"], :] = (
        (
            sum(
                energy_passenger_transport_consumption()
                .loc[:, "PHEV", _subscript_dict["PUBLIC TRANSPORT I"], :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PASSENGERS TRANSPORT MODE I": "PUBLIC TRANSPORT I",
                        "HOUSEHOLDS I": "HOUSEHOLDS I!",
                    }
                ),
                dim=["HOUSEHOLDS I!"],
            )
            * (1 - share_elec_in_phev())
            * emission_factors_public_transport()
            .loc["PHEV", :, :]
            .reset_coords(drop=True)
            * unit_conversion_j_mj()
            / unit_conversion_j_tj()
        )
        .expand_dims({"TRANSPORT POWER TRAIN I": ["PHEV"]}, 1)
        .values
    )
    return value


@component.add(
    name="passenger transport emissions end use energy by FE and transport mode",
    units="kg/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_hh_transport_energy_bottom_up": 2,
        "passengers_transport_ghg_emissions": 5,
        "passenger_transport_emissions_end_use_energy": 5,
    },
)
def passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode():
    """
    Greenhouse gas emissions generated by passengers transport vehicles, by region, type of final energy and type of gas, in kg/year.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    )
    value.loc[:, ["FE elec"], :, :] = 0
    value.loc[:, ["FE gas"], :, :] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: passengers_transport_ghg_emissions()
            .loc[:, "ICE gas", :, :]
            .reset_coords(drop=True),
            lambda: passenger_transport_emissions_end_use_energy()
            .loc[:, "ICE gas", :, :]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"], :, :] = 0
    value.loc[:, ["FE hydrogen"], :, :] = 0
    value.loc[:, ["FE liquid"], :, :] = (
        if_then_else(
            switch_eco_hh_transport_energy_bottom_up() == 0,
            lambda: passengers_transport_ghg_emissions()
            .loc[:, "ICE gasoline", :, :]
            .reset_coords(drop=True)
            + passengers_transport_ghg_emissions()
            .loc[:, "ICE diesel", :, :]
            .reset_coords(drop=True)
            + passengers_transport_ghg_emissions()
            .loc[:, "ICE LPG", :, :]
            .reset_coords(drop=True)
            + passengers_transport_ghg_emissions()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True),
            lambda: passenger_transport_emissions_end_use_energy()
            .loc[:, "ICE gasoline", :, :]
            .reset_coords(drop=True)
            + passenger_transport_emissions_end_use_energy()
            .loc[:, "ICE diesel", :, :]
            .reset_coords(drop=True)
            + passenger_transport_emissions_end_use_energy()
            .loc[:, "ICE LPG", :, :]
            .reset_coords(drop=True)
            + passenger_transport_emissions_end_use_energy()
            .loc[:, "PHEV", :, :]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"], :, :] = 0
    value.loc[:, ["FE solid fossil"], :, :] = 0
    return value


@component.add(
    name="passenger transport GHG emissions all energy chain by transport mode 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec": 6,
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_fe_elec": 1,
    },
)
def passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG FE I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    )
    value.loc[:, ["FE gas"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE gas", :, :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE heat", :, :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE liquid", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE solid fossil", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    value.loc[:, ["FE elec"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_fe_elec()
        .loc[:, "FE elec", :, :]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE hydrogen", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"], :, :] = (
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
        .loc[:, "FE solid bio", :, :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    return value


@component.add(
    name="passenger transport GHG emissions all energy chain by transport mode 35R exc FE elec",
    units="Mt/Year",
    subscripts=[
        "REGIONS 35 I",
        "NRG COMMODITIES I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode": 6,
        "unit_conversion_kg_mt": 6,
    },
)
def passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG COMMODITIES I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    )
    value.loc[:, ["FE gas"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE gas", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE heat", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE liquid", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE solid fossil", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE hydrogen", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"], :, :] = (
        (
            passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
            .loc[:, "FE solid bio", :, :]
            .reset_coords(drop=True)
            / unit_conversion_kg_mt()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    return value


@component.add(
    name="passenger transport GHG emissions all energy chain by transport mode 35R FE elec",
    subscripts=[
        "REGIONS 35 I",
        "FINAL ENERGY TRANSMISSION I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_intensity_emissions_by_fe_35r": 1,
        "energy_passenger_transport_consumption_by_fe_35r": 1,
        "unit_conversion_mj_ej": 1,
    },
)
def passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_fe_elec():
    return (
        (
            ghg_intensity_emissions_by_fe_35r()
            .loc[:, "FE elec", :]
            .reset_coords(drop=True)
            * sum(
                energy_passenger_transport_consumption_by_fe_35r()
                .loc[:, "FE elec", :, :]
                .reset_coords(drop=True)
                .rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"}),
                dim=["HOUSEHOLDS I!"],
            )
            / unit_conversion_mj_ej()
        )
        .transpose("REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "GHG I")
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
    )


@component.add(
    name="passengers transport GHG emissions",
    units="kg/Year",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
        "GHG I",
    ],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "transport_final_energy_consumption_by_fe": 1,
        "emission_factors_private_transport": 1,
        "initial_share_passengers_private_transport_by_type_of_power_train": 1,
    },
)
def passengers_transport_ghg_emissions():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                "PASSENGERS TRANSPORT MODE I"
            ],
            "GHG I": _subscript_dict["GHG I"],
        },
        [
            "REGIONS 35 I",
            "TRANSPORT POWER TRAIN I",
            "PASSENGERS TRANSPORT MODE I",
            "GHG I",
        ],
    )
    value.loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :] = (
        transport_final_energy_consumption_by_fe()
        .loc[:, "FE liquid"]
        .reset_coords(drop=True)
        * emission_factors_private_transport()
        * initial_share_passengers_private_transport_by_type_of_power_train()
    ).values
    value.loc[:, :, _subscript_dict["PUBLIC TRANSPORT I"], :] = 0
    return value


@component.add(
    name="private passenger transport emissions end use energy by FE",
    units="kg/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode": 1
    },
)
def private_passenger_transport_emissions_end_use_energy_by_fe():
    return sum(
        passenger_transport_emissions_end_use_energy_by_fe_and_transport_mode()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
        dim=["PRIVATE TRANSPORT I!"],
    )


@component.add(
    name="private passenger transport GHG emissions all energy chain 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r": 1
    },
)
def private_passenger_transport_ghg_emissions_all_energy_chain_35r():
    """
    Private passenger transport GHG direct emissions including indirect electricity consumption PROTRA emissions.
    """
    return sum(
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r()
        .loc[:, :, _subscript_dict["PRIVATE TRANSPORT I"], :]
        .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
        dim=["PRIVATE TRANSPORT I!"],
    )


@component.add(
    name="private transport GHG emissions 35R",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "NRG FE I", "GHG I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec": 5
    },
)
def private_transport_ghg_emissions_35r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 35 I", "NRG FE I", "GHG I"],
    )
    value.loc[:, ["FE gas"], :] = (
        sum(
            passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
            .loc[:, "FE gas", _subscript_dict["PRIVATE TRANSPORT I"], :]
            .reset_coords(drop=True)
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
            dim=["PRIVATE TRANSPORT I!"],
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE elec"], :] = 0
    value.loc[:, ["FE heat"], :] = 0
    value.loc[:, ["FE hydrogen"], :] = (
        sum(
            passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
            .loc[:, "FE hydrogen", _subscript_dict["PRIVATE TRANSPORT I"], :]
            .reset_coords(drop=True)
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
            dim=["PRIVATE TRANSPORT I!"],
        )
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"], :] = (
        sum(
            passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
            .loc[:, "FE liquid", _subscript_dict["PRIVATE TRANSPORT I"], :]
            .reset_coords(drop=True)
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
            dim=["PRIVATE TRANSPORT I!"],
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"], :] = (
        sum(
            passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
            .loc[:, "FE solid bio", _subscript_dict["PRIVATE TRANSPORT I"], :]
            .reset_coords(drop=True)
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
            dim=["PRIVATE TRANSPORT I!"],
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"], :] = (
        sum(
            passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r_exc_fe_elec()
            .loc[:, "FE solid fossil", _subscript_dict["PRIVATE TRANSPORT I"], :]
            .reset_coords(drop=True)
            .rename({"PASSENGERS TRANSPORT MODE I": "PRIVATE TRANSPORT I!"}),
            dim=["PRIVATE TRANSPORT I!"],
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="SURFACE COAL MINING EMISSION FACTORS",
    units="m3/t",
    subscripts=["GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_surface_coal_mining_emission_factors"},
)
def surface_coal_mining_emission_factors():
    """
    Greenhouse gas factors emission due to fugitive emissions generated by the extraction of coal in surface mines.
    """
    return _ext_constant_surface_coal_mining_emission_factors()


_ext_constant_surface_coal_mining_emission_factors = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MINING",
    "SURFACE_COAL_MINING_EMISSION_FACTORS*",
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    _root,
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    "_ext_constant_surface_coal_mining_emission_factors",
)


@component.add(
    name="top down transport emissions",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passengers_transport_ghg_emissions": 1, "unit_conversion_kg_mt": 1},
)
def top_down_transport_emissions():
    return (
        sum(
            passengers_transport_ghg_emissions().rename(
                {"TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!"}
            ),
            dim=["TRANSPORT POWER TRAIN I!"],
        )
        / unit_conversion_kg_mt()
    )


@component.add(
    name="total GHG emissions 35R",
    units="Gt/Year",
    subscripts=["GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_all_emissions_35r": 1},
)
def total_ghg_emissions_35r():
    return sum(
        ghg_all_emissions_35r().rename({"REGIONS 35 I": "REGIONS 35 I!"}),
        dim=["REGIONS 35 I!"],
    )


@component.add(
    name="total GHG energy chain emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_all_emissions_35r": 2},
)
def total_ghg_energy_chain_emissions_9r():
    """
    Total greenhouse gas emissions generated in all energy chain, by region and type of gas, in Gt/year. ---9R_old_eq--- (GHG_extraction_emissions[REGIONS 9 I,GHG I]+ GHG_refining_emissions[REGIONS 9 I,GHG I]+ GHG_energy_transformation_emissions[REGIONS 9 I,GHG I]+ GHG_energy_supply_emissions[REGIONS 9 I,GHG I]+ GHG_energy_use_emissions[REGIONS 9 I,GHG I])/UNIT_CONVERSION_Mt_Gt
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "GHG I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        ghg_all_emissions_35r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"], :] = (
        sum(
            ghg_all_emissions_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="total passenger transport GHG emissions",
    units="Mt/Year",
    subscripts=["REGIONS 35 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r": 1
    },
)
def total_passenger_transport_ghg_emissions():
    return sum(
        passenger_transport_ghg_emissions_all_energy_chain_by_transport_mode_35r().rename(
            {
                "NRG FE I": "NRG FE I!",
                "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
            }
        ),
        dim=["NRG FE I!", "PASSENGERS TRANSPORT MODE I!"],
    )


@component.add(
    name="total private transport CO2 emissions by region",
    units="Mt/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emissions_private_transport_by_region": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def total_private_transport_co2_emissions_by_region():
    return (
        sum(
            co2_emissions_private_transport_by_region().rename(
                {"PRIVATE TRANSPORT I": "PRIVATE TRANSPORT I!"}
            ),
            dim=["PRIVATE TRANSPORT I!"],
        )
        / unit_conversion_kg_mt()
    )


@component.add(
    name="transport final energy consumption by FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_consumption_buildings_and_transport": 1},
)
def transport_final_energy_consumption_by_fe():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "NRG FE I"],
    )
    value.loc[:, ["FE liquid"]] = (
        final_energy_consumption_buildings_and_transport()
        .loc[:, "HH FUEL TRANSPORT"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["FE liquid"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="UNDERGROUND COAL MINING EMISSION FACTORS",
    units="m3/t",
    subscripts=["GHG ENERGY USE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_underground_coal_mining_emission_factors"
    },
)
def underground_coal_mining_emission_factors():
    """
    Greenhouse gas factors emission due to fugitive emissions generated by the extraction of coal in underground mines.
    """
    return _ext_constant_underground_coal_mining_emission_factors()


_ext_constant_underground_coal_mining_emission_factors = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "EF_MINING",
    "UNDERGROUND_COAL_MINING_EMISSION_FACTORS*",
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    _root,
    {"GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"]},
    "_ext_constant_underground_coal_mining_emission_factors",
)


@component.add(
    name="UNIT CONVERSION J m3 nat gas",
    units="J/m3",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_unit_conversion_j_m3_nat_gas"},
)
def unit_conversion_j_m3_nat_gas():
    return _ext_constant_unit_conversion_j_m3_nat_gas()


_ext_constant_unit_conversion_j_m3_nat_gas = ExtConstant(
    "model_parameters/constants.xlsx",
    "Constants",
    "UNIT_CONVERSION_J_m3_nat_gas",
    {},
    _root,
    {},
    "_ext_constant_unit_conversion_j_m3_nat_gas",
)
