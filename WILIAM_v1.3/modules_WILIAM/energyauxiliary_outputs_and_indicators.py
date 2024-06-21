"""
Module energyauxiliary_outputs_and_indicators
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual FE GDP intensity change rate",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_gdp_intensity": 1, "delayed_fe_gdp_intensity": 1},
)
def annual_fe_gdp_intensity_change_rate():
    """
    Annual FE GDP intensity change rate.
    """
    return -1 + zidz(fe_gdp_intensity(), delayed_fe_gdp_intensity())


@component.add(
    name="annual PE GDP intensity change rate",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_gdp_intensity": 1, "delayed_pe_gdp_intensity": 1},
)
def annual_pe_gdp_intensity_change_rate():
    """
    Annual PE GDP intensity change rate.
    """
    return -1 + zidz(pe_gdp_intensity(), delayed_pe_gdp_intensity())


@component.add(
    name="aux final to primary energy by region until 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_final_to_primary_energy_by_region_until_2015": 1},
    other_deps={
        "_delayfixed_aux_final_to_primary_energy_by_region_until_2015": {
            "initial": {"time_step": 1},
            "step": {"final_to_primary_energy_by_region_until_2015": 1},
        }
    },
)
def aux_final_to_primary_energy_by_region_until_2015():
    """
    Auxiliary variable to estimate the final-to-primary energy ratio in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_final_to_primary_energy_by_region_until_2015()


_delayfixed_aux_final_to_primary_energy_by_region_until_2015 = DelayFixed(
    lambda: final_to_primary_energy_by_region_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_aux_final_to_primary_energy_by_region_until_2015",
)


@component.add(
    name="auxiliary FE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliary_fe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_auxiliary_fe_gdp_intensity": {
            "initial": {"time_step": 1},
            "step": {"fe_gdp_intensity_until_2015": 1},
        }
    },
)
def auxiliary_fe_gdp_intensity():
    """
    Auxiliary variable to estimate the cumulative TPES intensity change until 2009.
    """
    return _delayfixed_auxiliary_fe_gdp_intensity()


_delayfixed_auxiliary_fe_gdp_intensity = DelayFixed(
    lambda: fe_gdp_intensity_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_auxiliary_fe_gdp_intensity",
)


@component.add(
    name="auxiliary PE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_auxiliary_pe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_auxiliary_pe_gdp_intensity": {
            "initial": {"time_step": 1},
            "step": {"pe_gdp_intensity_until_2015": 1},
        }
    },
)
def auxiliary_pe_gdp_intensity():
    """
    Auxiliary variable to estimate the cumulative TPES intensity change until 2009.
    """
    return _delayfixed_auxiliary_pe_gdp_intensity()


_delayfixed_auxiliary_pe_gdp_intensity = DelayFixed(
    lambda: pe_gdp_intensity_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_auxiliary_pe_gdp_intensity",
)


@component.add(
    name="CF power system",
    units="TWh/(TW*h)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_to_allocated": 1,
        "unit_conversion_twh_ej": 1,
        "unit_conversion_hours_year": 1,
        "protra_operative_capacity_stock_selected": 1,
    },
)
def cf_power_system():
    """
    Capacity factor of the whole power system
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        )
        * unit_conversion_twh_ej(),
        sum(
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        )
        * unit_conversion_hours_year(),
    )


@component.add(
    name="CO2 EMISSION FACTORS PE",
    units="kg/TJ",
    subscripts=["NRG PE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_co2_emission_factors_pe"},
)
def co2_emission_factors_pe():
    """
    CO2 emission factors per type of primary energy (Source: IPCC 2006 Guidelines). Only fossil fuels, for RES the convention is to assign 0 kg/TJ (consistency with land-use module).
    """
    return _ext_constant_co2_emission_factors_pe()


_ext_constant_co2_emission_factors_pe = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "GHG_emission_factors",
    "CO2_EMISSION_FACTORS_PE*",
    {"NRG PE I": _subscript_dict["NRG PE I"]},
    _root,
    {"NRG PE I": _subscript_dict["NRG PE I"]},
    "_ext_constant_co2_emission_factors_pe",
)


@component.add(
    name="CO2 EMISSION FACTORS PROTRA TI STATIONARY COMBUSTION",
    units="kg/TJ",
    subscripts=["NRG PROTRA I", "NRG TI I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_co2_emission_factors_protra_ti_stationary_combustion"
    },
)
def co2_emission_factors_protra_ti_stationary_combustion():
    return _ext_constant_co2_emission_factors_protra_ti_stationary_combustion()


_ext_constant_co2_emission_factors_protra_ti_stationary_combustion = ExtConstant(
    "model_parameters/energy/energy-GHG_emission_factors.xlsx",
    "GHG_emission_factors",
    "CO2_EMISSION_FACTORS_PROTRA_TI_STATIONARY_COMBUSTION",
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
    _root,
    {
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        "NRG TI I": _subscript_dict["NRG TI I"],
    },
    "_ext_constant_co2_emission_factors_protra_ti_stationary_combustion",
)


@component.add(
    name="CO2 emissions by PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emission_factors_protra_ti_stationary_combustion": 1,
        "ti_by_protra_and_commodity": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emissions_by_protra():
    """
    CO2 emissions by process transformation.
    """
    return (
        sum(
            co2_emission_factors_protra_ti_stationary_combustion().rename(
                {"NRG TI I": "NRG TI I!"}
            )
            * ti_by_protra_and_commodity()
            .rename({"NRG TI I": "NRG TI I!"})
            .transpose("NRG PROTRA I", "NRG TI I!", "REGIONS 9 I"),
            dim=["NRG TI I!"],
        )
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    ).transpose("REGIONS 9 I", "NRG PROTRA I")


@component.add(
    name="CO2 emissions captured CCS",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 1},
)
def co2_emissions_captured_ccs():
    """
    CO2 emissions captured through CCS
    """
    return -sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA CCS I"]]
        .rename({"NRG PROTRA I": "PROTRA CCS I!"}),
        dim=["PROTRA CCS I!"],
    )


@component.add(
    name="CO2 emissions PE combustion before CCS",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "co2_emission_factors_pe": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emissions_pe_combustion_before_ccs():
    """
    Total CO2 emissions from primery energy combustion without accounting for CCS sequestration.
    """
    return (
        pe_by_commodity()
        * co2_emission_factors_pe()
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="CO2 emissions TO elec",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 2, "share_to_elec_chp_plants": 1},
)
def co2_emissions_to_elec():
    """
    CO2 emissions of electricity production.
    """
    return sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA PP I"]]
        .rename({"NRG PROTRA I": "PROTRA PP I!"}),
        dim=["PROTRA PP I!"],
    ) + sum(
        share_to_elec_chp_plants().rename({"PROTRA CHP I": "PROTRA CHP I!"})
        * co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA CHP I"]]
        .rename({"NRG PROTRA I": "PROTRA CHP I!"}),
        dim=["PROTRA CHP I!"],
    )


@component.add(
    name="CO2 emissions TO heat",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 2, "share_to_elec_chp_plants": 1},
)
def co2_emissions_to_heat():
    """
    CO2 emissions of heat production.
    """
    return sum(
        co2_emissions_by_protra()
        .loc[:, _subscript_dict["PROTRA HP I"]]
        .rename({"NRG PROTRA I": "PROTRA HP I!"}),
        dim=["PROTRA HP I!"],
    ) + (
        1
        - sum(
            share_to_elec_chp_plants().rename({"PROTRA CHP I": "PROTRA CHP I!"})
            * co2_emissions_by_protra()
            .loc[:, _subscript_dict["PROTRA CHP I"]]
            .rename({"NRG PROTRA I": "PROTRA CHP I!"}),
            dim=["PROTRA CHP I!"],
        )
    )


@component.add(
    name="CO2 intensity TO elec",
    units="Mt/EJ",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_to_elec": 1, "to_by_commodity": 1},
)
def co2_intensity_to_elec():
    """
    CO2 mass per unit of electricity generation.
    """
    return zidz(
        co2_emissions_to_elec(),
        to_by_commodity().loc[:, "TO elec"].reset_coords(drop=True),
    )


@component.add(
    name="CO2 intensity TO elec gCO2 per kWh",
    units="gCO2/kWh/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_intensity_to_elec": 1},
)
def co2_intensity_to_elec_gco2_per_kwh():
    return co2_intensity_to_elec() * 10**12 / (2.777 * 10**11)


@component.add(
    name="CO2 intensity TO heat",
    units="Mt/EJ",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_to_heat": 1, "to_by_commodity": 1},
)
def co2_intensity_to_heat():
    """
    CO2 mass per unit of heat generation.
    """
    return zidz(
        co2_emissions_to_heat(),
        to_by_commodity().loc[:, "TO heat"].reset_coords(drop=True),
    )


@component.add(
    name="CO2e emissions per unit of sector output",
    units="tCO2eq/Mdollars 2015",
    subscripts=["REGIONS 9 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_by_sector": 3,
        "unit_conversion_t_mt": 3,
        "gwp_20_year": 3,
        "select_gwp_time_frame_sp": 3,
        "gwp_100_year": 3,
        "output_real_9r": 1,
    },
)
def co2e_emissions_per_unit_of_sector_output():
    return zidz(
        ghg_emissions_by_sector().loc[:, :, "CO2"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CO2"]),
            lambda: float(gwp_100_year().loc["CO2"]),
        )
        + ghg_emissions_by_sector().loc[:, :, "CH4"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CH4"]),
            lambda: float(gwp_100_year().loc["CH4"]),
        )
        + ghg_emissions_by_sector().loc[:, :, "N2O"].reset_coords(drop=True)
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["N2O"]),
            lambda: float(gwp_100_year().loc["N2O"]),
        ),
        output_real_9r(),
    )


@component.add(
    name="CO2e intensity of final energy",
    units="GtCO2eq/EJ",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ghg_emissions": 1, "final_energy_demand_by_fe_ej_9r": 1},
)
def co2e_intensity_of_final_energy():
    return zidz(
        total_ghg_emissions().expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 1),
        final_energy_demand_by_fe_ej_9r(),
    )


@component.add(
    name="CO2e intensity of final energy 1R",
    units="GtCO2eq/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2e_intensity_of_final_energy": 1},
)
def co2e_intensity_of_final_energy_1r():
    """
    Total carbon dioxide equivalent intensity of final energy.
    """
    return sum(
        co2e_intensity_of_final_energy().rename(
            {"REGIONS 9 I": "REGIONS 9 I!", "NRG FE I": "NRG FE I!"}
        ),
        dim=["REGIONS 9 I!", "NRG FE I!"],
    )


@component.add(
    name="cumulative FE GDP intensity change from 2015",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "fe_gdp_intensity": 1, "fe_gdp_intensity_until_2015": 1},
)
def cumulative_fe_gdp_intensity_change_from_2015():
    """
    Cumulative TFES intensity change from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: -1 + fe_gdp_intensity() / fe_gdp_intensity_until_2015(),
    )


@component.add(
    name="cumulative PE GDP intensity change from 2015",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "pe_gdp_intensity_until_2015": 1, "pe_gdp_intensity": 1},
)
def cumulative_pe_gdp_intensity_change_from_2015():
    """
    Cumulative TPES intensity change from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: -1 + zidz(pe_gdp_intensity(), pe_gdp_intensity_until_2015()),
    )


@component.add(
    name="delayed FE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_fe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_delayed_fe_gdp_intensity": {
            "initial": {},
            "step": {"fe_gdp_intensity": 1},
        }
    },
)
def delayed_fe_gdp_intensity():
    return _delayfixed_delayed_fe_gdp_intensity()


_delayfixed_delayed_fe_gdp_intensity = DelayFixed(
    lambda: fe_gdp_intensity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_delayed_fe_gdp_intensity",
)


@component.add(
    name="delayed PE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_pe_gdp_intensity": 1},
    other_deps={
        "_delayfixed_delayed_pe_gdp_intensity": {
            "initial": {},
            "step": {"pe_gdp_intensity": 1},
        }
    },
)
def delayed_pe_gdp_intensity():
    return _delayfixed_delayed_pe_gdp_intensity()


_delayfixed_delayed_pe_gdp_intensity = DelayFixed(
    lambda: pe_gdp_intensity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_delayed_pe_gdp_intensity",
)


@component.add(
    name="FE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_energy_uses": 1,
        "unit_conversion_tj_ej": 1,
        "gdp_real_9r": 1,
    },
)
def fe_gdp_intensity():
    """
    Final energy vs GDP ratio per region.
    """
    return zidz(total_fe_energy_uses() * unit_conversion_tj_ej(), gdp_real_9r())


@component.add(
    name="FE GDP intensity until 2015",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "fe_gdp_intensity": 1, "auxiliary_fe_gdp_intensity": 1},
)
def fe_gdp_intensity_until_2015():
    """
    PE GDP intensity until the year 2015.
    """
    return if_then_else(
        time() < 2015, lambda: fe_gdp_intensity(), lambda: auxiliary_fe_gdp_intensity()
    )


@component.add(
    name="FE including trade by commodity per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def fe_including_trade_by_commodity_per_capita():
    return (
        zidz(
            total_fe_including_net_trade(),
            population_9_regions().expand_dims(
                {"NRG FE I": _subscript_dict["NRG FE I"]}, 1
            ),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="final to primary energy by region",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
        "pe_by_commodity": 1,
    },
)
def final_to_primary_energy_by_region():
    """
    Share of total final energy (excluing non-energy uses) vs total primary energy by region.
    """
    return zidz(
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG FE I": "NRG FE I!"}),
            dim=["NRG FE I!"],
        )
        / unit_conversion_tj_ej(),
        sum(pe_by_commodity().rename({"NRG PE I": "NRG PE I!"}), dim=["NRG PE I!"]),
    )


@component.add(
    name="final to primary energy by region until 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "aux_final_to_primary_energy_by_region_until_2015": 1,
        "final_to_primary_energy_by_region": 1,
    },
)
def final_to_primary_energy_by_region_until_2015():
    """
    final-to-primary energy ratio by region until the year 2015.
    """
    return if_then_else(
        time() > 2015,
        lambda: aux_final_to_primary_energy_by_region_until_2015(),
        lambda: final_to_primary_energy_by_region(),
    )


@component.add(
    name="final to primary energy world",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
        "pe_by_commodity": 1,
    },
)
def final_to_primary_energy_world():
    """
    World share of total final energy (excluing non-energy uses) vs total primary energy.
    """
    return xr.DataArray(
        zidz(
            sum(
                final_energy_demand_by_fe_9r().rename(
                    {"REGIONS 9 I": "REGIONS 9 I!", "NRG FE I": "NRG FE I!"}
                ),
                dim=["REGIONS 9 I!", "NRG FE I!"],
            )
            / unit_conversion_tj_ej(),
            sum(
                pe_by_commodity().rename(
                    {"REGIONS 9 I": "REGIONS 9 I!", "NRG PE I": "NRG PE I!"}
                ),
                dim=["REGIONS 9 I!", "NRG PE I!"],
            ),
        ),
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        ["REGIONS 9 I"],
    )


@component.add(
    name="GHG emissions all sectors",
    units="Gt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_by_sector": 1, "unit_conversion_mt_gt": 1},
)
def ghg_emissions_all_sectors():
    return (
        sum(
            ghg_emissions_by_sector().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        / unit_conversion_mt_gt()
    )


@component.add(
    name="GHG emissions sectors and households",
    units="Gt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ghg_emissions_all_sectors": 1,
        "households_end_use_energy_emissions_9r": 1,
        "unit_conversion_mt_gt": 1,
    },
)
def ghg_emissions_sectors_and_households():
    return (
        ghg_emissions_all_sectors()
        + households_end_use_energy_emissions_9r() / unit_conversion_mt_gt()
    )


@component.add(
    name="GHG intensity of final energy",
    units="Mt/EJ",
    subscripts=["REGIONS 9 I", "NRG FE I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_energy_chain_emissions_9r": 1,
        "final_energy_demand_by_fe_ej_9r": 1,
    },
)
def ghg_intensity_of_final_energy():
    return zidz(
        total_ghg_energy_chain_emissions_9r().expand_dims(
            {"NRG FE I": _subscript_dict["NRG FE I"]}, 2
        ),
        final_energy_demand_by_fe_ej_9r().expand_dims(
            {"GHG I": _subscript_dict["GHG I"]}, 1
        ),
    ).transpose("REGIONS 9 I", "NRG FE I", "GHG I")


@component.add(
    name="INITIAL PROSTO DEDICATED CAPACITY EXPANSION",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSTO ELEC DEDICATED I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_prosto_dedicated_capacity_expansion": 1},
    other_deps={
        "_initial_initial_prosto_dedicated_capacity_expansion": {
            "initial": {"prosto_dedicated_capacity_expansion": 1},
            "step": {},
        }
    },
)
def initial_prosto_dedicated_capacity_expansion():
    return _initial_initial_prosto_dedicated_capacity_expansion()


_initial_initial_prosto_dedicated_capacity_expansion = Initial(
    lambda: prosto_dedicated_capacity_expansion(),
    "_initial_initial_prosto_dedicated_capacity_expansion",
)


@component.add(
    name="INITIAL PROTRA CAPACITY EXPANSION",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_protra_capacity_expansion": 1},
    other_deps={
        "_initial_initial_protra_capacity_expansion": {
            "initial": {"protra_capacity_expansion_selected": 1},
            "step": {},
        }
    },
)
def initial_protra_capacity_expansion():
    return _initial_initial_protra_capacity_expansion()


_initial_initial_protra_capacity_expansion = Initial(
    lambda: protra_capacity_expansion_selected(),
    "_initial_initial_protra_capacity_expansion",
)


@component.add(
    name="INITIAL SHARE NEW PV SUBTECHN LAND",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_new_pv_subtechn_land": 1},
    other_deps={
        "_initial_initial_share_new_pv_subtechn_land": {
            "initial": {"share_new_pv_subtechn_land": 1},
            "step": {},
        }
    },
)
def initial_share_new_pv_subtechn_land():
    return _initial_initial_share_new_pv_subtechn_land()


_initial_initial_share_new_pv_subtechn_land = Initial(
    lambda: share_new_pv_subtechn_land(), "_initial_initial_share_new_pv_subtechn_land"
)


@component.add(
    name="INITIAL SHARE NEW PV SUBTECHN URBAN",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_new_pv_subtechn_urban": 1},
    other_deps={
        "_initial_initial_share_new_pv_subtechn_urban": {
            "initial": {"share_new_pv_subtechn_urban": 1},
            "step": {},
        }
    },
)
def initial_share_new_pv_subtechn_urban():
    return _initial_initial_share_new_pv_subtechn_urban()


_initial_initial_share_new_pv_subtechn_urban = Initial(
    lambda: share_new_pv_subtechn_urban(),
    "_initial_initial_share_new_pv_subtechn_urban",
)


@component.add(
    name="INITIAL SHARE PV CAPACITY BY SUBTECHNOLOGY",
    units="DMNL",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_share_pv_capacity_by_subtechnology": 1},
    other_deps={
        "_initial_initial_share_pv_capacity_by_subtechnology": {
            "initial": {"share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1},
            "step": {},
        }
    },
)
def initial_share_pv_capacity_by_subtechnology():
    return _initial_initial_share_pv_capacity_by_subtechnology()


_initial_initial_share_pv_capacity_by_subtechnology = Initial(
    lambda: share_capacity_stock_protra_pp_solar_pv_by_subtechnology(),
    "_initial_initial_share_pv_capacity_by_subtechnology",
)


@component.add(
    name="investment costs PROTRA vs GDP",
    units="1",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_protra_investment_cost_35r": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def investment_costs_protra_vs_gdp():
    return zidz(
        total_protra_investment_cost_35r(), gross_domestic_product_real_supply_side()
    )


@component.add(
    name="LUE solar PV by technology per ha",
    units="ha/MW",
    subscripts=["REGIONS 36 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"lue_solar_pv_by_technology": 1, "unit_conversion_km2_ha": 1},
)
def lue_solar_pv_by_technology_per_ha():
    """
    Land use efficiency of solar PV by technology in ha/MW.
    """
    return zidz(
        xr.DataArray(
            1,
            {
                "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ],
            },
            ["REGIONS 36 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
        ),
        lue_solar_pv_by_technology() * unit_conversion_km2_ha(),
    )


@component.add(
    name="net TFEC energy uses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1, "fenust_system": 1},
)
def net_tfec_energy_uses():
    """
    Net total final energy consumption (final energy minus energy invested to produce energy).
    """
    return total_fe_energy_uses() - fenust_system()


@component.add(
    name="net TFEC energy uses per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_tfec_energy_uses": 1,
        "unit_conversion_gj_ej": 1,
        "population_9_regions": 1,
    },
)
def net_tfec_energy_uses_per_capita():
    """
    Net total final energy consumption per capita.
    """
    return zidz(
        net_tfec_energy_uses() * unit_conversion_gj_ej(), population_9_regions()
    )


@component.add(
    name="passengers transport real 1R",
    units="km*person",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"passenger_transport_real_supply_by_mode": 1},
)
def passengers_transport_real_1r():
    """
    Transport supply after all policy and endogenous modifications, in persons*km.
    """
    return sum(
        passenger_transport_real_supply_by_mode().rename(
            {
                "REGIONS 35 I": "REGIONS 35 I!",
                "PASSENGERS TRANSPORT MODE I": "PASSENGERS TRANSPORT MODE I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=["REGIONS 35 I!", "PASSENGERS TRANSPORT MODE I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="PE by commodity per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def pe_by_commodity_per_capita():
    return (
        zidz(
            pe_by_commodity(),
            population_9_regions().expand_dims(
                {"NRG PE I": _subscript_dict["NRG PE I"]}, 1
            ),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="PE GDP intensity",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_pe_by_region": 1, "unit_conversion_tj_ej": 1, "gdp_real_9r": 1},
)
def pe_gdp_intensity():
    """
    Primary energy vs GDP ratio per region.
    """
    return zidz(total_pe_by_region() * unit_conversion_tj_ej(), gdp_real_9r())


@component.add(
    name="PE GDP intensity until 2015",
    units="TJ/Mdollars 2015",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "pe_gdp_intensity": 1, "auxiliary_pe_gdp_intensity": 1},
)
def pe_gdp_intensity_until_2015():
    """
    PE GDP intensity until the year 2015.
    """
    return if_then_else(
        time() < 2015, lambda: pe_gdp_intensity(), lambda: auxiliary_pe_gdp_intensity()
    )


@component.add(
    name="PE total world",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_pe_by_region": 1},
)
def pe_total_world():
    """
    Total world domestic primary energy consumption.
    """
    return sum(
        total_pe_by_region().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="physical energy intensity TPE vs net energy uses",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_total_net_energy_vs_tpe_energy_uses": 1},
)
def physical_energy_intensity_tpe_vs_net_energy_uses():
    """
    Physical energy intensity
    """
    return zidz(
        xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        share_total_net_energy_vs_tpe_energy_uses(),
    )


@component.add(
    name="physical energy intensity TPES vs final",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_to_primary_energy_by_region": 1},
)
def physical_energy_intensity_tpes_vs_final():
    """
    Physical energy intensity by region.
    """
    return zidz(
        xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        final_to_primary_energy_by_region(),
    )


@component.add(
    name="power density solar PV by technology",
    units="w/m2",
    subscripts=["REGIONS 35 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "lue_solar_pv_by_technology": 2,
        "cf_protra": 2,
        "unit_conversion_w_mw": 2,
        "unit_conversion_m2_km2": 2,
    },
)
def power_density_solar_pv_by_technology():
    """
    Land use efficiency of solar PV by technology in power density terms, ie. We/m2 (1 We = 8760 Wh).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 35 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        lue_solar_pv_by_technology()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 8 I"})
        * cf_protra()
        .loc[_subscript_dict["REGIONS 8 I"], "TO elec", "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        * (unit_conversion_w_mw() / unit_conversion_m2_km2())
    ).values
    value.loc[_subscript_dict["REGIONS EU27 I"], :] = (
        lue_solar_pv_by_technology()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 36 I": "REGIONS EU27 I"})
        * float(cf_protra().loc["EU27", "TO elec", "PROTRA PP solar open space PV"])
        * (unit_conversion_w_mw() / unit_conversion_m2_km2())
    ).values
    return value


@component.add(
    name="PROTRA capacity stock 1R",
    units="TW",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_operative_capacity_stock_selected": 1},
)
def protra_capacity_stock_1r():
    """
    Capacity stock of TI-TO transformation technology capacities by TO (PROTRA)
    """
    return sum(
        protra_operative_capacity_stock_selected().rename(
            {
                "REGIONS 9 I": "REGIONS 9 I!",
                "NRG TO I": "NRG TO I!",
                "NRG PROTRA I": "NRG PROTRA I!",
            }
        ),
        dim=["REGIONS 9 I!", "NRG TO I!", "NRG PROTRA I!"],
    )


@component.add(
    name="PROTRA capacity stock total TO",
    units="TW",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_operative_capacity_stock_selected": 1},
)
def protra_capacity_stock_total_to():
    return sum(
        protra_operative_capacity_stock_selected().rename({"NRG TO I": "NRG TO I!"}),
        dim=["NRG TO I!"],
    )


@component.add(
    name="public vehicle fleet EU27",
    units="vehicles",
    subscripts=["TRANSPORT POWER TRAIN I", "PUBLIC TRANSPORT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1},
)
def public_vehicle_fleet_eu27():
    return sum(
        public_passenger_vehicle_fleet()
        .loc[_subscript_dict["REGIONS EU27 I"], :, :, :]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!", "HOUSEHOLDS I": "HOUSEHOLDS I!"}),
        dim=["REGIONS EU27 I!", "HOUSEHOLDS I!"],
    )


@component.add(
    name="required embodied FE materials BU",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "required_embodied_fe_materials_for_protra": 1,
        "dynfenu_materials_ev_batteries_9r": 1,
        "required_embodied_fe_materials_for_new_grids": 1,
    },
)
def required_embodied_fe_materials_bu():
    """
    Total required embodied primary energy of total material consumption for BU technologies (PROTRA, PROSUP and electric transport).
    """
    return (
        required_embodied_fe_materials_for_protra()
        + sum(
            dynfenu_materials_ev_batteries_9r().rename(
                {"EV BATTERIES I": "EV BATTERIES I!"}
            ),
            dim=["EV BATTERIES I!"],
        )
        + sum(
            required_embodied_fe_materials_for_new_grids().rename(
                {"NRG PROTRA I": "NRG PROTRA I!"}
            ),
            dim=["NRG PROTRA I!"],
        )
    )


@component.add(
    name="share capacity stock VRES vs total elec",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_operative_capacity_stock_selected": 2},
)
def share_capacity_stock_vres_vs_total_elec():
    """
    Share variable renewables capacity in total electricity capacity stock.
    """
    return zidz(
        sum(
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", _subscript_dict["PROTRA VRES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA VRES I!"}),
            dim=["PROTRA VRES I!"],
        ),
        sum(
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        ),
    )


@component.add(
    name="share FE demand commodity",
    units="1",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 2},
)
def share_fe_demand_commodity():
    """
    Share for each final energy (FE, demand) by region over the total FE demand (including energy and non-energy uses).
    """
    return zidz(
        fe_excluding_trade(),
        sum(
            fe_excluding_trade().rename({"NRG FE I": "NRG FE I!"}), dim=["NRG FE I!"]
        ).expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 1),
    )


@component.add(
    name="share FE gas RES vs total gas",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ti_by_proref_and_commodity": 5,
        "share_to_elec_res_vs_total_elec": 1,
        "to_h2_gases_based_fuel": 2,
    },
)
def share_fe_gas_res_vs_total_gas():
    """
    Regional share of renewables in final energy by type of final energy.
    """
    return zidz(
        ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery bio", "TI gas bio"]
        .reset_coords(drop=True)
        + to_h2_gases_based_fuel() * share_to_elec_res_vs_total_elec(),
        ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery coal", "TI gas fossil"]
        .reset_coords(drop=True)
        + ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery oil", "TI gas fossil"]
        .reset_coords(drop=True)
        + ti_by_proref_and_commodity()
        .loc[:, "PROREF transformation PE natural gas 2 TI gas fossil", "TI gas fossil"]
        .reset_coords(drop=True)
        + ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery bio", "TI gas bio"]
        .reset_coords(drop=True)
        + to_h2_gases_based_fuel(),
    )


@component.add(
    name="share FE green hydrogen vs total hydrogen",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_to_elec_res_vs_total_elec": 1,
        "to_electrolytic_pure_h2": 1,
        "to_by_commodity": 1,
    },
)
def share_fe_green_hydrogen_vs_total_hydrogen():
    """
    Share of hydrogen production comming from renewable energy sources
    """
    return zidz(
        share_to_elec_res_vs_total_elec() * to_electrolytic_pure_h2(),
        to_by_commodity().loc[:, "TO hydrogen"].reset_coords(drop=True),
    )


@component.add(
    name="share FE heat RES vs total heat",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_fe_heat_res_vs_total_heat():
    """
    Share renewables in final energy heat consumption (per region)
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO heat", _subscript_dict["PROTRA RES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA RES I!"}),
            dim=["PROTRA RES I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO heat", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        ),
    )


@component.add(
    name="share FE liquid RES vs total liquid",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "ti_by_proref_and_commodity": 4,
        "to_h2_liquids_based_fuel": 2,
        "share_to_elec_res_vs_total_elec": 1,
    },
)
def share_fe_liquid_res_vs_total_liquid():
    """
    Share renewables in final energy liquid consumption (per region)
    """
    return zidz(
        ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery bio", "TI liquid bio"]
        .reset_coords(drop=True)
        + to_h2_liquids_based_fuel() * share_to_elec_res_vs_total_elec(),
        ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery coal", "TI liquid fossil"]
        .reset_coords(drop=True)
        + ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery oil", "TI liquid fossil"]
        .reset_coords(drop=True)
        + ti_by_proref_and_commodity()
        .loc[:, "PROREF refinery bio", "TI liquid bio"]
        .reset_coords(drop=True)
        + to_h2_liquids_based_fuel(),
    )


@component.add(
    name="share FE RES vs total FE",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_including_net_trade": 13, "shares_res_in_fe": 5},
)
def share_fe_res_vs_total_fe():
    """
    Weighted sum of all RES contributions to the different FE sources (per region)
    """
    return (
        total_fe_including_net_trade().loc[:, "FE elec"].reset_coords(drop=True)
        * shares_res_in_fe().loc[:, "FE elec"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
        * shares_res_in_fe().loc[:, "FE gas"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE heat"].reset_coords(drop=True)
        * shares_res_in_fe().loc[:, "FE heat"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
        * shares_res_in_fe().loc[:, "FE hydrogen"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
        * shares_res_in_fe().loc[:, "FE liquid"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE solid bio"].reset_coords(drop=True)
    ) / (
        total_fe_including_net_trade().loc[:, "FE elec"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE heat"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE solid bio"].reset_coords(drop=True)
        + total_fe_including_net_trade()
        .loc[:, "FE solid fossil"]
        .reset_coords(drop=True)
        + total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
    )


@component.add(
    name="share required embodied FE materials BU vs PE total",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"required_embodied_fe_materials_bu": 1, "total_fe_energy_uses": 1},
)
def share_required_embodied_fe_materials_bu_vs_pe_total():
    """
    Share of required embodied final energy of total material consumption for BU technologies (PROTRA, PROSUP and electric transport) vs total final energy.
    """
    return zidz(required_embodied_fe_materials_bu(), total_fe_energy_uses())


@component.add(
    name="share RES in PE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 2},
)
def share_res_in_pe():
    """
    Share of renewable energies in total primary energy (including non-energy uses).
    """
    return zidz(
        sum(
            pe_by_commodity()
            .loc[:, _subscript_dict["NRG PE RES I"]]
            .rename({"NRG PE I": "NRG PE RES I!"}),
            dim=["NRG PE RES I!"],
        ),
        sum(pe_by_commodity().rename({"NRG PE I": "NRG PE I!"}), dim=["NRG PE I!"]),
    )


@component.add(
    name="share TO by commodity",
    units="1",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 2},
)
def share_to_by_commodity():
    """
    Share for each transformation output (TO, production) by region over the total TO.
    """
    return zidz(
        to_by_commodity(),
        sum(
            to_by_commodity().rename({"NRG TO I": "NRG TO I!"}), dim=["NRG TO I!"]
        ).expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1),
    )


@component.add(
    name="share TO elec CHP plants",
    units="1",
    subscripts=["REGIONS 9 I", "PROTRA CHP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 3},
)
def share_to_elec_chp_plants():
    """
    Share of electricity generation in CHP plants vs total generated (electricity + heat).
    """
    return zidz(
        protra_to_allocated()
        .loc[:, "TO elec", _subscript_dict["PROTRA CHP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA CHP I"}),
        protra_to_allocated()
        .loc[:, "TO elec", _subscript_dict["PROTRA CHP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA CHP I"})
        + protra_to_allocated()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA CHP I"}),
    )


@component.add(
    name="share TO elec RES vs total elec",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_to_elec_res_vs_total_elec():
    """
    Share renewables in electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", _subscript_dict["PROTRA RES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA RES I!"}),
            dim=["PROTRA RES I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        ),
    )


@component.add(
    name="share TO elec VRES vs RES",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_to_elec_vres_vs_res():
    """
    Share variable renewables in renewable electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", _subscript_dict["PROTRA VRES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA VRES I!"}),
            dim=["PROTRA VRES I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", _subscript_dict["PROTRA RES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA RES I!"}),
            dim=["PROTRA RES I!"],
        ),
    )


@component.add(
    name="share TO elec VRES vs total elec",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def share_to_elec_vres_vs_total_elec():
    """
    Share variable renewables in electricity generation.
    """
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", _subscript_dict["PROTRA VRES I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA VRES I!"}),
            dim=["PROTRA VRES I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["NRG PROTRA I!"],
        ),
    )


@component.add(
    name="share total net energy vs TPE energy uses",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"net_tfec_energy_uses": 1, "total_pe_energy_uses": 1},
)
def share_total_net_energy_vs_tpe_energy_uses():
    """
    Share of total net final energy vs total primary energy supply (without accounting for non-energy uses).
    """
    return zidz(net_tfec_energy_uses(), total_pe_energy_uses())


@component.add(
    name="share total PROSTO losses vs TO",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_storage_losses": 1, "to_by_commodity": 1},
)
def share_total_prosto_losses_vs_to():
    """
    Share of total storage losses by utility-scale facilities and the transformation outputs.
    """
    return zidz(prosup_storage_losses(), to_by_commodity())


@component.add(
    name="shares RES in FE",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "share_to_elec_res_vs_total_elec": 1,
        "share_fe_gas_res_vs_total_gas": 1,
        "share_fe_heat_res_vs_total_heat": 1,
        "share_fe_green_hydrogen_vs_total_hydrogen": 1,
        "share_fe_liquid_res_vs_total_liquid": 1,
    },
)
def shares_res_in_fe():
    """
    Shares of renewable energy by final energy
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 9 I", "NRG FE I"],
    )
    value.loc[:, ["FE elec"]] = (
        share_to_elec_res_vs_total_elec()
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE gas"]] = (
        share_fe_gas_res_vs_total_gas()
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"]] = (
        share_fe_heat_res_vs_total_heat()
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"]] = (
        share_fe_green_hydrogen_vs_total_hydrogen()
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["FE liquid"]] = (
        share_fe_liquid_res_vs_total_liquid()
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"]] = 1
    value.loc[:, ["FE solid fossil"]] = 0
    return value


@component.add(
    name="total CO2 emissions PE",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2_emissions_pe_combustion": 1},
)
def total_co2_emissions_pe():
    """
    CO2 emissions PE.
    """
    return total_co2_emissions_pe_combustion()


@component.add(
    name="total CO2 emissions PE combustion",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emissions_pe_combustion_before_ccs": 1,
        "co2_emissions_captured_ccs": 1,
    },
)
def total_co2_emissions_pe_combustion():
    """
    CO2 emissions PE combustion accounting for CCS.
    """
    return (
        sum(
            co2_emissions_pe_combustion_before_ccs().rename({"NRG PE I": "NRG PE I!"}),
            dim=["NRG PE I!"],
        )
        - co2_emissions_captured_ccs()
    )


@component.add(
    name="total energy capacities investment costs vs GDP",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_energy_capacities_investment_cost": 1, "gdp_real_9r": 1},
)
def total_energy_capacities_investment_costs_vs_gdp():
    return zidz(total_energy_capacities_investment_cost(), gdp_real_9r())


@component.add(
    name="total energy consumption passengers transport 1S",
    units="EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_energy_consumption_passenger_transport": 1},
)
def total_energy_consumption_passengers_transport_1s():
    """
    Total energy passengers transport consumption of final energy in EJ.
    """
    return sum(
        total_energy_consumption_passenger_transport().rename(
            {"NRG FE I": "NRG FE I!"}
        ),
        dim=["NRG FE I!"],
    )


@component.add(
    name="total FE energy uses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_fe_9r": 1, "unit_conversion_tj_ej": 1},
)
def total_fe_energy_uses():
    """
    Total final energy demand for 9 regions (not including non-energy uses).
    """
    return (
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG FE I": "NRG FE I!"}),
            dim=["NRG FE I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="total FE including trade per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def total_fe_including_trade_per_capita():
    return (
        zidz(
            sum(
                total_fe_including_net_trade().rename({"NRG FE I": "NRG FE I!"}),
                dim=["NRG FE I!"],
            ),
            population_9_regions(),
        )
        * unit_conversion_gj_ej()
    )


@component.add(
    name="total FE including trade per capita 1R",
    units="GJ/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_including_trade_per_capita": 1},
)
def total_fe_including_trade_per_capita_1r():
    """
    Total iron includin trade per capita.
    """
    return sum(
        total_fe_including_trade_per_capita().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="total FE per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_including_trade_per_capita": 1},
)
def total_fe_per_capita():
    """
    total_FE_per_capita
    """
    return total_fe_including_trade_per_capita()


@component.add(
    name="total final energy demand by FE",
    units="TJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_9r": 1,
        "final_non_energy_demand_by_fe_9r": 1,
    },
)
def total_final_energy_demand_by_fe():
    return final_energy_demand_by_fe_9r() + final_non_energy_demand_by_fe_9r()


@component.add(
    name="total final energy intensities 1R 1S",
    units="TJ/million$",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_final_energy_intensities_by_sector": 1},
)
def total_final_energy_intensities_1r_1s():
    """
    Final energy intensities estimated with a top-down approach
    """
    return sum(
        total_final_energy_intensities_by_sector().rename(
            {
                "REGIONS 35 I": "REGIONS 35 I!",
                "SECTORS NON ENERGY I": "SECTORS NON ENERGY I!",
            }
        ),
        dim=["REGIONS 35 I!", "SECTORS NON ENERGY I!"],
    )


@component.add(
    name="total PE energy uses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_by_commodity": 1,
        "final_energy_demand_by_fe_9r": 1,
        "total_final_energy_demand_by_fe": 1,
    },
)
def total_pe_energy_uses():
    """
    Approximation to estimate the total amount of PE for energy uses,taking as proxy the share of energy vs non-energy final energy demand.
    """
    return sum(
        pe_by_commodity().rename({"NRG PE I": "NRG PE I!"}), dim=["NRG PE I!"]
    ) * zidz(
        sum(
            final_energy_demand_by_fe_9r().rename({"NRG FE I": "NRG FE I!"}),
            dim=["NRG FE I!"],
        ),
        sum(
            total_final_energy_demand_by_fe().rename({"NRG FE I": "NRG FE I!"}),
            dim=["NRG FE I!"],
        ),
    )


@component.add(
    name="total PE per region per capita",
    units="GJ/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_pe_by_region": 1,
        "population_9_regions": 1,
        "unit_conversion_gj_ej": 1,
    },
)
def total_pe_per_region_per_capita():
    return zidz(total_pe_by_region(), population_9_regions()) * unit_conversion_gj_ej()


@component.add(
    name="total PROTRA CO2 emissions",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"co2_emissions_by_protra": 1},
)
def total_protra_co2_emissions():
    """
    Total CO2 emissions in process transformations.
    """
    return sum(
        co2_emissions_by_protra().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="total public vehicle fleet 9R",
    units="vehicles",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"public_passenger_vehicle_fleet": 1, "public_vehicle_fleet_eu27": 1},
)
def total_public_vehicle_fleet_9r():
    value = xr.DataArray(
        np.nan, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = sum(
        public_passenger_vehicle_fleet()
        .loc[_subscript_dict["REGIONS 8 I"], :, :, :]
        .rename(
            {
                "REGIONS 35 I": "REGIONS 8 I",
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "PUBLIC TRANSPORT I": "PUBLIC TRANSPORT I!",
                "HOUSEHOLDS I": "HOUSEHOLDS I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "PUBLIC TRANSPORT I!", "HOUSEHOLDS I!"],
    ).values
    value.loc[["EU27"]] = sum(
        public_vehicle_fleet_eu27().rename(
            {
                "TRANSPORT POWER TRAIN I": "TRANSPORT POWER TRAIN I!",
                "PUBLIC TRANSPORT I": "PUBLIC TRANSPORT I!",
            }
        ),
        dim=["TRANSPORT POWER TRAIN I!", "PUBLIC TRANSPORT I!"],
    )
    return value


@component.add(
    name="world FE energy uses",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1},
)
def world_fe_energy_uses():
    return sum(
        total_fe_energy_uses().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="world final energy demand sectors",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_final_energy_demand_sectors_by_fe": 1},
)
def world_final_energy_demand_sectors():
    """
    Global final energy demand (energy uses) from sectors.
    """
    return sum(
        world_final_energy_demand_sectors_by_fe().rename({"NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    )


@component.add(
    name="world final energy demand sectors by FE",
    units="EJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 1, "unit_conversion_tj_ej": 1},
)
def world_final_energy_demand_sectors_by_fe():
    """
    Global final energy demand (energy uses) from sectors by type of final energy.
    """
    return (
        sum(
            final_energy_demand_by_sector_and_fe().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 I!",
                    "SECTORS NON ENERGY I": "SECTORS NON ENERGY I!",
                }
            ),
            dim=["REGIONS 35 I!", "SECTORS NON ENERGY I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world final non energy demand",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_final_non_energy_demand_by_sectors_and_fe": 1},
)
def world_final_non_energy_demand():
    """
    Global final energy demand (non-energy uses) from sectors.
    """
    return sum(
        world_final_non_energy_demand_by_sectors_and_fe().rename(
            {"NRG FE I": "NRG FE I!"}
        ),
        dim=["NRG FE I!"],
    )


@component.add(
    name="world final non energy demand by sectors and FE",
    units="EJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_non_energy_demand_by_sectors_and_fe": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def world_final_non_energy_demand_by_sectors_and_fe():
    """
    Global final energy demand (non-energy uses) from sectors by type of final energy.
    """
    return (
        sum(
            final_non_energy_demand_by_sectors_and_fe().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world households final energy demand by FE",
    units="EJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_final_energy_demand_by_fe": 1, "unit_conversion_tj_ej": 1},
)
def world_households_final_energy_demand_by_fe():
    """
    Global final energy demand from households by type of final energy.
    """
    return (
        sum(
            households_final_energy_demand_by_fe().rename(
                {"REGIONS 35 I": "REGIONS 35 I!"}
            ),
            dim=["REGIONS 35 I!"],
        )
        / unit_conversion_tj_ej()
    )


@component.add(
    name="world households total final energy demand",
    units="EJ/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"world_households_final_energy_demand_by_fe": 1},
)
def world_households_total_final_energy_demand():
    """
    Global final energy demand from households.
    """
    return sum(
        world_households_final_energy_demand_by_fe().rename({"NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    )


@component.add(
    name="WORLD share TO elec RES vs total elec",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 2},
)
def world_share_to_elec_res_vs_total_elec():
    return zidz(
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", _subscript_dict["PROTRA RES I"]]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!", "NRG PROTRA I": "PROTRA RES I!"}),
            dim=["REGIONS 9 I!", "PROTRA RES I!"],
        ),
        sum(
            protra_to_allocated()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!", "NRG PROTRA I": "NRG PROTRA I!"}),
            dim=["REGIONS 9 I!", "NRG PROTRA I!"],
        ),
    )
