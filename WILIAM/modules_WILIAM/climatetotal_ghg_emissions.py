"""
Module climatetotal_ghg_emissions
Translated using PySD version 3.13.4
"""

@component.add(
    name="aux CH4 correction factor",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_ch4_correction_factor": 1},
    other_deps={
        "_delayfixed_aux_ch4_correction_factor": {
            "initial": {"time_step": 1},
            "step": {"correction_factor_by_ch4_historic_data": 1},
        }
    },
)
def aux_ch4_correction_factor():
    return _delayfixed_aux_ch4_correction_factor()


_delayfixed_aux_ch4_correction_factor = DelayFixed(
    lambda: correction_factor_by_ch4_historic_data(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_aux_ch4_correction_factor",
)


@component.add(
    name="aux CHO2 LUC correction factor",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_cho2_luc_correction_factor": 1},
    other_deps={
        "_delayfixed_aux_cho2_luc_correction_factor": {
            "initial": {"time_step": 1},
            "step": {"correction_factor_by_co2_luc_historic_data": 1},
        }
    },
)
def aux_cho2_luc_correction_factor():
    return _delayfixed_aux_cho2_luc_correction_factor()


_delayfixed_aux_cho2_luc_correction_factor = DelayFixed(
    lambda: correction_factor_by_co2_luc_historic_data(),
    lambda: time_step(),
    lambda: 0,
    time_step,
    "_delayfixed_aux_cho2_luc_correction_factor",
)


@component.add(
    name="aux N2O correction factor",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_n2o_correction_factor": 1},
    other_deps={
        "_delayfixed_aux_n2o_correction_factor": {
            "initial": {"time_step": 1},
            "step": {"correction_factor_by_n2o_historic_data": 1},
        }
    },
)
def aux_n2o_correction_factor():
    return _delayfixed_aux_n2o_correction_factor()


_delayfixed_aux_n2o_correction_factor = DelayFixed(
    lambda: correction_factor_by_n2o_historic_data(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_aux_n2o_correction_factor",
)


@component.add(
    name="C cumulative GHG emissions",
    units="Gt",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cumulative_ghg_emissions": 1,
        "unit_conversion_c_co2": 1,
        "gwp_20_year": 1,
        "unit_conversion_tco2eq_gtco2eq": 1,
        "unit_conversion_t_gt": 1,
    },
)
def c_cumulative_ghg_emissions():
    """
    Cumulative GHG emissions in carbon-content equivalent.
    """
    return (
        cumulative_ghg_emissions()
        * unit_conversion_c_co2()
        / float(gwp_20_year().loc["CO2"])
        * unit_conversion_tco2eq_gtco2eq()
        / unit_conversion_t_gt()
    )


@component.add(
    name="CH4 agriculture emissions corrected by historic data",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "exo_ch4_emissions_agriculture": 1,
        "ch4_emissions_agriculture": 1,
        "correction_factor_by_ch4_historic_data": 1,
    },
)
def ch4_agriculture_emissions_corrected_by_historic_data():
    return if_then_else(
        time() < 2022,
        lambda: exo_ch4_emissions_agriculture(),
        lambda: ch4_emissions_agriculture() * correction_factor_by_ch4_historic_data(),
    )


@component.add(
    name="CH4 ANTHRO EMISSIONS",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "ch4_agriculture_emissions_corrected_by_historic_data": 2,
        "ch4_total_anthro_rest_of_emissions_rcp": 8,
        "model_explorer_rcp_ghg_emissions": 4,
        "unit_conversion_mt_gt": 6,
        "exo_ch4_energy_emissions_9r": 2,
        "ch4_ippus_emissions_9r": 2,
        "total_ghg_energy_emissions_9r": 2,
        "ch4_waste_emissions_9r": 2,
        "switch_climate": 2,
        "select_rcp_for_exogenous_ghg_emissions_sp": 3,
    },
)
def ch4_anthro_emissions():
    """
    "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare) except Power Plants, Energy Conversion, Extraction, and Distribution. TODO:Corrected with endogenous data "Total CH4 emissions fossil fuels" and "Agriculture emissions " Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5 IF_THEN_ELSE(SWITCH_MODEL_EXPLORER=1, total_GHG_energy_emissions_9R[REGIONS_9_I,CH4]*UNIT_CONVERSION_Mt_Gt+ IF_THEN_ELSE(model_explorer_RCP_GHG_emissions=1, CH4_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP[REGIONS_9_I,RCP26], IF_THEN_ELSE(model_explorer_RCP_GHG_emissions=2, CH4_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP[REGIONS_9_I,RCP45], IF_THEN_ELSE(model_explorer_RCP_GHG_emissions=3, CH4_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP[REGIONS_9_I,RCP60], IF_THEN_ELSE(model_explorer_RCP_GHG_emissions=4, CH4_TOTAL_ANTHRO_REST_OF_EMISSIONS_RCP[REGIONS_9_I,RCP85], 0)))),
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            switch_climate() == 1,
            lambda: total_ghg_energy_emissions_9r()
            .loc[:, "CH4"]
            .reset_coords(drop=True)
            * unit_conversion_mt_gt()
            + ch4_agriculture_emissions_corrected_by_historic_data()
            + ch4_ippus_emissions_9r() * unit_conversion_mt_gt()
            + ch4_waste_emissions_9r(),
            lambda: exo_ch4_energy_emissions_9r() * unit_conversion_mt_gt()
            + if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: ch4_total_anthro_rest_of_emissions_rcp()
                .loc[:, "RCP26"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: ch4_total_anthro_rest_of_emissions_rcp()
                    .loc[:, "RCP45"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: ch4_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP60"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: ch4_total_anthro_rest_of_emissions_rcp()
                            .loc[:, "RCP85"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            switch_climate() == 1,
            lambda: total_ghg_energy_emissions_9r()
            .loc[:, "CH4"]
            .reset_coords(drop=True)
            * unit_conversion_mt_gt()
            + ch4_agriculture_emissions_corrected_by_historic_data()
            + ch4_ippus_emissions_9r() * unit_conversion_mt_gt()
            + ch4_waste_emissions_9r(),
            lambda: exo_ch4_energy_emissions_9r() * unit_conversion_mt_gt()
            + if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: ch4_total_anthro_rest_of_emissions_rcp()
                .loc[:, "RCP26"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: ch4_total_anthro_rest_of_emissions_rcp()
                    .loc[:, "RCP45"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: ch4_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP60"]
                        .reset_coords(drop=True),
                        lambda: ch4_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP85"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="CO2 cropsoil and luc emissions corrected by historic data",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "co2_soil_and_luc_emissions_historical": 1,
        "co2_landuse_emissions_and_crop_soil_management": 1,
        "correction_factor_by_co2_luc_historic_data": 1,
    },
)
def co2_cropsoil_and_luc_emissions_corrected_by_historic_data():
    """
    Before: CO2_SOIL_AND_LUC_EMISSIONS[REGIONS_9_I] Before: IF_THEN_ELSE(Time<2016, CO2_SOIL_AND_LUC_EMISSIONS[REGIONS_9_I], soil_and_landuse_emissions[REGIONS_9_I]*correction_factor_by_CO2_LUC_histor ic_data[REGIONS_9_I])
    """
    return if_then_else(
        time() < 2016,
        lambda: co2_soil_and_luc_emissions_historical(),
        lambda: co2_landuse_emissions_and_crop_soil_management()
        * correction_factor_by_co2_luc_historic_data(),
    )


@component.add(
    name="CO2 emissions per capita 9R",
    units="t/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ghg_emissions_per_capita_9r": 1},
)
def co2_emissions_per_capita_9r():
    """
    CO2 emissions per capita by region.
    """
    return ghg_emissions_per_capita_9r().loc[:, "CO2"].reset_coords(drop=True)


@component.add(
    name="CO2 land use change emissions",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate": 1,
        "switch_law2cli_luc_co2_emissions": 1,
        "co2_soil_and_luc_emissions_historical": 1,
        "co2_cropsoil_and_luc_emissions_corrected_by_historic_data": 1,
    },
)
def co2_land_use_change_emissions():
    """
    Sum of endogenous LUC and cropland management emissions *(in the future we expect to reflect more "LULUCF emisions as growth/extraction unbalance from forests)
    """
    return if_then_else(
        np.logical_or(switch_climate() == 0, switch_law2cli_luc_co2_emissions() == 0),
        lambda: co2_soil_and_luc_emissions_historical(),
        lambda: co2_cropsoil_and_luc_emissions_corrected_by_historic_data(),
    )


@component.add(
    name="CO2 LAND USE CHANGE EMISSIONS EXOGENOUS PROJECTION",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"past_trends_co2_land_use_change_emissions": 1},
)
def co2_land_use_change_emissions_exogenous_projection():
    """
    The model assumes by default the extrapolation of past trends of CO2 land-use change emissions test
    """
    return past_trends_co2_land_use_change_emissions()


@component.add(
    name="CO2 landuse emissions and crop soil management",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "c_landuse1_to_landuse2_emissions_region": 1,
        "soil_emissions_cropland_management_delayed": 1,
        "unit_conversion_t_gt": 1,
        "unit_conversion_c_co2": 1,
    },
)
def co2_landuse_emissions_and_crop_soil_management():
    return (
        (
            c_landuse1_to_landuse2_emissions_region()
            + soil_emissions_cropland_management_delayed()
        )
        / unit_conversion_t_gt()
        / unit_conversion_c_co2()
    )


@component.add(
    name="CO2 SOIL AND LUC EMISSIONS HISTORICAL",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_co2_soil_and_luc_emissions_historical",
        "__data__": "_ext_data_co2_soil_and_luc_emissions_historical",
        "time": 1,
    },
)
def co2_soil_and_luc_emissions_historical():
    """
    Historical information from Edgar
    """
    return _ext_data_co2_soil_and_luc_emissions_historical(time())


_ext_data_co2_soil_and_luc_emissions_historical = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_LULUCF_HISTORICAL",
    "LULUCF_EMISSIONS_HISTORICAL_DATA",
    "interpolate",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_data_co2_soil_and_luc_emissions_historical",
)


@component.add(
    name="correction factor by CH4 historic data",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "ch4_emissions_agriculture": 1,
        "exo_ch4_emissions_agriculture": 1,
        "aux_ch4_correction_factor": 1,
    },
)
def correction_factor_by_ch4_historic_data():
    return if_then_else(
        time() < 2021,
        lambda: zidz(exo_ch4_emissions_agriculture(), ch4_emissions_agriculture()),
        lambda: aux_ch4_correction_factor(),
    )


@component.add(
    name="correction factor by CO2 LUC historic data",
    units="1",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "co2_soil_and_luc_emissions_historical": 1,
        "co2_landuse_emissions_and_crop_soil_management": 1,
        "aux_cho2_luc_correction_factor": 1,
    },
)
def correction_factor_by_co2_luc_historic_data():
    return if_then_else(
        time() < 2019,
        lambda: zidz(
            sum(
                co2_soil_and_luc_emissions_historical().rename(
                    {"REGIONS 9 I": "REGIONS 9 I!"}
                ),
                dim=["REGIONS 9 I!"],
            ),
            sum(
                co2_landuse_emissions_and_crop_soil_management().rename(
                    {"REGIONS 9 I": "REGIONS 9 I!"}
                ),
                dim=["REGIONS 9 I!"],
            ),
        ),
        lambda: aux_cho2_luc_correction_factor(),
    )


@component.add(
    name="correction factor by N2O historic data",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "exo_n2o_emissions_agriculture": 1,
        "n2o_emissions_agriculture": 1,
        "aux_n2o_correction_factor": 1,
    },
)
def correction_factor_by_n2o_historic_data():
    return if_then_else(
        time() < 2021,
        lambda: zidz(exo_n2o_emissions_agriculture(), n2o_emissions_agriculture()),
        lambda: aux_n2o_correction_factor(),
    )


@component.add(
    name="cumulative GHG emissions",
    units="GtCO2eq",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cumulative_ghg_emissions": 1},
    other_deps={
        "_integ_cumulative_ghg_emissions": {
            "initial": {},
            "step": {"total_ghg_emissions": 1},
        }
    },
)
def cumulative_ghg_emissions():
    """
    Cumulative GHG emissions.
    """
    return _integ_cumulative_ghg_emissions()


_integ_cumulative_ghg_emissions = Integ(
    lambda: total_ghg_emissions(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    "_integ_cumulative_ghg_emissions",
)


@component.add(
    name="exo CH4 energy emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_total_ch4_energy_emissions_9r": 1},
)
def exo_ch4_energy_emissions_9r():
    """
    exogenous information from siulation
    """
    return exo_total_ch4_energy_emissions_9r(time())


@component.add(
    name="exo CO2 energy emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_total_co2_energy_emissions_9r": 1},
)
def exo_co2_energy_emissions_9r():
    """
    exogenous information from siulation
    """
    return exo_total_co2_energy_emissions_9r(time())


@component.add(
    name="exo N2O energy emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "exo_total_n2o_energy_emissions_9r": 1},
)
def exo_n2o_energy_emissions_9r():
    return exo_total_n2o_energy_emissions_9r(time())


@component.add(
    name="EXO TOTAL CO2 ENERGY EMISSIONS 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_total_co2_energy_emissions_9r",
        "__lookup__": "_ext_lookup_exo_total_co2_energy_emissions_9r",
    },
)
def exo_total_co2_energy_emissions_9r(x, final_subs=None):
    """
    exogenous information from simulation
    """
    return _ext_lookup_exo_total_co2_energy_emissions_9r(x, final_subs)


_ext_lookup_exo_total_co2_energy_emissions_9r = ExtLookup(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_EXO_SIMULATION",
    "EXO_TOTAL_CO2_ENERGY_AND_IPPUS_EMISSIONS_9R",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_total_co2_energy_emissions_9r",
)


@component.add(
    name="EXO TOTAL N2O ENERGY EMISSIONS 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_total_n2o_energy_emissions_9r",
        "__lookup__": "_ext_lookup_exo_total_n2o_energy_emissions_9r",
    },
)
def exo_total_n2o_energy_emissions_9r(x, final_subs=None):
    return _ext_lookup_exo_total_n2o_energy_emissions_9r(x, final_subs)


_ext_lookup_exo_total_n2o_energy_emissions_9r = ExtLookup(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_EXO_SIMULATION",
    "EXO_TOTAL_N2O_ENERGY_AND_IPPUS_EMISSIONS_9R",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_total_n2o_energy_emissions_9r",
)


@component.add(
    name="GHG emissions per capita 9R",
    units="t/(Year*person)",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_energy_chain_emissions_9r": 3,
        "population_9_regions": 6,
        "unit_conversion_t_gt": 3,
        "pfc_emissions": 1,
        "global_sf6_emissions": 1,
        "global_hfc_emissions": 1,
    },
)
def ghg_emissions_per_capita_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "GHG I": _subscript_dict["GHG I"],
        },
        ["REGIONS 9 I", "GHG I"],
    )
    value.loc[:, ["CO2"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "CO2"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 1)
        .values
    )
    value.loc[:, ["CH4"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "CH4"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 1)
        .values
    )
    value.loc[:, ["N2O"]] = (
        (
            zidz(
                total_ghg_energy_chain_emissions_9r()
                .loc[:, "N2O"]
                .reset_coords(drop=True),
                population_9_regions(),
            )
            * unit_conversion_t_gt()
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 1)
        .values
    )
    value.loc[:, ["PFCs"]] = (
        zidz(pfc_emissions(), population_9_regions())
        .expand_dims({"GHG I": ["PFCs"]}, 1)
        .values
    )
    value.loc[:, ["SF6"]] = (
        zidz(
            xr.DataArray(
                global_sf6_emissions(),
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                ["REGIONS 9 I"],
            ),
            population_9_regions(),
        )
        .expand_dims({"GHG I": ["SF6"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["HFC TYPE I"]] = (
        zidz(
            global_hfc_emissions().expand_dims(
                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 1
            ),
            population_9_regions().expand_dims(
                {"HFC TYPE I": _subscript_dict["HFC TYPE I"]}, 0
            ),
        )
        .transpose("REGIONS 9 I", "HFC TYPE I")
        .values
    )
    return value


@component.add(
    name="HFC EMISSIONS",
    units="t/Year",
    subscripts=["REGIONS 9 I", "HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 9,
        "hfc_emissions_rcp_6_0_endog": 18,
        "hfc_emissions_rcp_8_5_endog": 18,
        "hfc_emissions_rcp_2_6_endog": 18,
        "model_explorer_rcp_ghg_emissions": 36,
        "hfc_emissions_rcp_4_5_endog": 18,
        "select_rcp_for_exogenous_ghg_emissions_sp": 27,
    },
)
def hfc_emissions():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare) Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "HFC TYPE I": _subscript_dict["HFC TYPE I"],
        },
        ["REGIONS 9 I", "HFC TYPE I"],
    )
    value.loc[:, ["HFC134a"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC134a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC134a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC134a"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC134a"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC134a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC134a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC134a"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC134a"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC134a"]}, 1)
        .values
    )
    value.loc[:, ["HFC23"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC23"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC23"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC23"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC23"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC23"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC23"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC23"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC23"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC23"]}, 1)
        .values
    )
    value.loc[:, ["HFC32"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC32"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC32"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC32"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC32"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC32"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC32"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC32"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC32"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC32"]}, 1)
        .values
    )
    value.loc[:, ["HFC125"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC125"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC125"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC125"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC125"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC125"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC125"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC125"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC125"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC125"]}, 1)
        .values
    )
    value.loc[:, ["HFC143a"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC143a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC143a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC143a"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC143a"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC143a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC143a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC143a"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC143a"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC143a"]}, 1)
        .values
    )
    value.loc[:, ["HFC152a"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC152a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC152a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC152a"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC152a"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC152a"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC152a"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC152a"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC152a"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC152a"]}, 1)
        .values
    )
    value.loc[:, ["HFC227ea"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC227ea"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC227ea"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC227ea"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC227ea"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC227ea"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC227ea"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC227ea"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC227ea"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC227ea"]}, 1)
        .values
    )
    value.loc[:, ["HFC245ca"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC245ca"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC245ca"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC245ca"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC245ca"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC245ca"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC245ca"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC245ca"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC245ca"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC245ca"]}, 1)
        .values
    )
    value.loc[:, ["HFC4310mee"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC4310mee"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC4310mee"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC4310mee"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: hfc_emissions_rcp_8_5_endog()
                            .loc[:, "HFC4310mee"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: hfc_emissions_rcp_2_6_endog()
                .loc[:, "HFC4310mee"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: hfc_emissions_rcp_4_5_endog()
                    .loc[:, "HFC4310mee"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: hfc_emissions_rcp_6_0_endog()
                        .loc[:, "HFC4310mee"]
                        .reset_coords(drop=True),
                        lambda: hfc_emissions_rcp_8_5_endog()
                        .loc[:, "HFC4310mee"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        )
        .expand_dims({"GHG I": ["HFC4310mee"]}, 1)
        .values
    )
    return value


@component.add(
    name="HFC emissions RCP 2 6 endog",
    units="t/Year",
    subscripts=["REGIONS 9 I", "HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_hfc_emissions_rcp_2_6": 9,
        "share_co2_energy_emissions_by_region_9r": 9,
    },
)
def hfc_emissions_rcp_2_6_endog():
    """
    PFC anthropogenic emissions from RCP2.6 depending on real GDP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "HFC TYPE I": _subscript_dict["HFC TYPE I"],
        },
        ["REGIONS 9 I", "HFC TYPE I"],
    )
    value.loc[:, ["HFC134a"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC134a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC134a"]}, 1)
        .values
    )
    value.loc[:, ["HFC23"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC23"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC23"]}, 1)
        .values
    )
    value.loc[:, ["HFC32"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC32"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC32"]}, 1)
        .values
    )
    value.loc[:, ["HFC125"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC125"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC125"]}, 1)
        .values
    )
    value.loc[:, ["HFC143a"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC143a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC143a"]}, 1)
        .values
    )
    value.loc[:, ["HFC152a"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC152a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC152a"]}, 1)
        .values
    )
    value.loc[:, ["HFC227ea"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC227ea"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC227ea"]}, 1)
        .values
    )
    value.loc[:, ["HFC245ca"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC245ca"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC245ca"]}, 1)
        .values
    )
    value.loc[:, ["HFC4310mee"]] = (
        (
            float(global_hfc_emissions_rcp_2_6().loc["HFC4310mee"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC4310mee"]}, 1)
        .values
    )
    return value


@component.add(
    name="HFC emissions RCP 4 5 endog",
    units="t/Year",
    subscripts=["REGIONS 9 I", "HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_hfc_emissions_rcp_4_5": 9,
        "share_co2_energy_emissions_by_region_9r": 9,
    },
)
def hfc_emissions_rcp_4_5_endog():
    """
    PFC anthropogenic emissions from RCP4.5 depending on real GDP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "HFC TYPE I": _subscript_dict["HFC TYPE I"],
        },
        ["REGIONS 9 I", "HFC TYPE I"],
    )
    value.loc[:, ["HFC134a"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC134a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC134a"]}, 1)
        .values
    )
    value.loc[:, ["HFC23"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC23"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC23"]}, 1)
        .values
    )
    value.loc[:, ["HFC32"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC32"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC32"]}, 1)
        .values
    )
    value.loc[:, ["HFC125"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC125"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC125"]}, 1)
        .values
    )
    value.loc[:, ["HFC143a"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC143a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC143a"]}, 1)
        .values
    )
    value.loc[:, ["HFC152a"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC152a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC152a"]}, 1)
        .values
    )
    value.loc[:, ["HFC227ea"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC227ea"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC227ea"]}, 1)
        .values
    )
    value.loc[:, ["HFC245ca"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC245ca"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC245ca"]}, 1)
        .values
    )
    value.loc[:, ["HFC4310mee"]] = (
        (
            float(global_hfc_emissions_rcp_4_5().loc["HFC4310mee"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC4310mee"]}, 1)
        .values
    )
    return value


@component.add(
    name="HFC emissions RCP 6 0 endog",
    units="t/Year",
    subscripts=["REGIONS 9 I", "HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_hfc_emissions_rcp_6_0": 9,
        "share_co2_energy_emissions_by_region_9r": 9,
    },
)
def hfc_emissions_rcp_6_0_endog():
    """
    PFC anthropogenic emissions from RCP6.0 depending on real GDP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "HFC TYPE I": _subscript_dict["HFC TYPE I"],
        },
        ["REGIONS 9 I", "HFC TYPE I"],
    )
    value.loc[:, ["HFC134a"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC134a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC134a"]}, 1)
        .values
    )
    value.loc[:, ["HFC23"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC23"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC23"]}, 1)
        .values
    )
    value.loc[:, ["HFC32"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC32"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC32"]}, 1)
        .values
    )
    value.loc[:, ["HFC125"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC125"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC125"]}, 1)
        .values
    )
    value.loc[:, ["HFC143a"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC143a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC143a"]}, 1)
        .values
    )
    value.loc[:, ["HFC152a"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC152a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC152a"]}, 1)
        .values
    )
    value.loc[:, ["HFC227ea"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC227ea"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC227ea"]}, 1)
        .values
    )
    value.loc[:, ["HFC245ca"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC245ca"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC245ca"]}, 1)
        .values
    )
    value.loc[:, ["HFC4310mee"]] = (
        (
            float(global_hfc_emissions_rcp_6_0().loc["HFC4310mee"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC4310mee"]}, 1)
        .values
    )
    return value


@component.add(
    name="HFC emissions RCP 8 5 endog",
    units="t/Year",
    subscripts=["REGIONS 9 I", "HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_hfc_emissions_rcp_8_5": 9,
        "share_co2_energy_emissions_by_region_9r": 9,
    },
)
def hfc_emissions_rcp_8_5_endog():
    """
    PFC anthropogenic emissions from RCP8.5 depending on real GDP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "HFC TYPE I": _subscript_dict["HFC TYPE I"],
        },
        ["REGIONS 9 I", "HFC TYPE I"],
    )
    value.loc[:, ["HFC134a"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC134a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC134a"]}, 1)
        .values
    )
    value.loc[:, ["HFC23"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC23"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC23"]}, 1)
        .values
    )
    value.loc[:, ["HFC32"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC32"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC32"]}, 1)
        .values
    )
    value.loc[:, ["HFC125"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC125"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC125"]}, 1)
        .values
    )
    value.loc[:, ["HFC143a"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC143a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC143a"]}, 1)
        .values
    )
    value.loc[:, ["HFC152a"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC152a"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC152a"]}, 1)
        .values
    )
    value.loc[:, ["HFC227ea"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC227ea"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC227ea"]}, 1)
        .values
    )
    value.loc[:, ["HFC245ca"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC245ca"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC245ca"]}, 1)
        .values
    )
    value.loc[:, ["HFC4310mee"]] = (
        (
            float(global_hfc_emissions_rcp_8_5().loc["HFC4310mee"])
            * share_co2_energy_emissions_by_region_9r()
        )
        .expand_dims({"GHG I": ["HFC4310mee"]}, 1)
        .values
    )
    return value


@component.add(
    name="N2O agriculture emissions corrected by historic data",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "exo_n2o_emissions_agriculture": 1,
        "correction_factor_by_n2o_historic_data": 1,
        "n2o_emissions_agriculture": 1,
    },
)
def n2o_agriculture_emissions_corrected_by_historic_data():
    return if_then_else(
        time() < 2022,
        lambda: np.maximum(0, exo_n2o_emissions_agriculture()),
        lambda: n2o_emissions_agriculture() * correction_factor_by_n2o_historic_data(),
    )


@component.add(
    name="N2O ANTHRO EMISSIONS",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "n2o_ippus_emissions_9r": 2,
        "model_explorer_rcp_ghg_emissions": 4,
        "n2o_total_anthro_rest_of_emissions_rcp": 8,
        "n2o_agriculture_emissions_corrected_by_historic_data": 2,
        "unit_conversion_mt_gt": 6,
        "n2o_waste_emissions_9r": 2,
        "total_ghg_energy_emissions_9r": 2,
        "exo_n2o_energy_emissions_9r": 2,
        "switch_climate": 2,
        "select_rcp_for_exogenous_ghg_emissions_sp": 3,
    },
)
def n2o_anthro_emissions():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare). TODO: corrected with endogenous data "agriculture: fertilizers, animals, soil" CH4 emissions fossil fuels". Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            switch_climate() == 1,
            lambda: total_ghg_energy_emissions_9r()
            .loc[:, "N2O"]
            .reset_coords(drop=True)
            * unit_conversion_mt_gt()
            + n2o_ippus_emissions_9r() * unit_conversion_mt_gt()
            + n2o_agriculture_emissions_corrected_by_historic_data()
            + n2o_waste_emissions_9r(),
            lambda: exo_n2o_energy_emissions_9r() * unit_conversion_mt_gt()
            + if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: n2o_total_anthro_rest_of_emissions_rcp()
                .loc[:, "RCP26"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: n2o_total_anthro_rest_of_emissions_rcp()
                    .loc[:, "RCP45"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: n2o_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP60"]
                        .reset_coords(drop=True),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: n2o_total_anthro_rest_of_emissions_rcp()
                            .loc[:, "RCP85"]
                            .reset_coords(drop=True),
                            lambda: xr.DataArray(
                                0,
                                {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                                ["REGIONS 9 I"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            switch_climate() == 1,
            lambda: total_ghg_energy_emissions_9r()
            .loc[:, "N2O"]
            .reset_coords(drop=True)
            * unit_conversion_mt_gt()
            + n2o_ippus_emissions_9r() * unit_conversion_mt_gt()
            + n2o_agriculture_emissions_corrected_by_historic_data()
            + n2o_waste_emissions_9r(),
            lambda: exo_n2o_energy_emissions_9r() * unit_conversion_mt_gt()
            + if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: n2o_total_anthro_rest_of_emissions_rcp()
                .loc[:, "RCP26"]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: n2o_total_anthro_rest_of_emissions_rcp()
                    .loc[:, "RCP45"]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: n2o_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP60"]
                        .reset_coords(drop=True),
                        lambda: n2o_total_anthro_rest_of_emissions_rcp()
                        .loc[:, "RCP85"]
                        .reset_coords(drop=True),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="past trends CO2 land use change emissions",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Data",
    comp_subtype="Normal",
    depends_on={
        "past_trends_global_co2_land_use_change_emissions": 1,
        "number_of_regions": 1,
    },
)
def past_trends_co2_land_use_change_emissions():
    """
    [DICE-2013R] Land-use change emissions. Cte at 2010 level for the period 1990-2100 as first approximation. MEDEAS : Past trends CO2 land use change emissions W/NUMBER_OF_REGIONS (in fact the emissions are not equally distributed)
    """
    return xr.DataArray(
        past_trends_global_co2_land_use_change_emissions() / number_of_regions(),
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        ["REGIONS 9 I"],
    )


@component.add(
    name="PFC EMISSIONS",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_rcp_ghg_emissions": 4,
        "pfc_emissions_rcp_endog": 8,
        "select_rcp_for_exogenous_ghg_emissions_sp": 3,
    },
)
def pfc_emissions():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare) Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: if_then_else(
            model_explorer_rcp_ghg_emissions() == 1,
            lambda: pfc_emissions_rcp_endog().loc["RCP26", :].reset_coords(drop=True),
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 2,
                lambda: pfc_emissions_rcp_endog()
                .loc["RCP45", :]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 3,
                    lambda: pfc_emissions_rcp_endog()
                    .loc["RCP60", :]
                    .reset_coords(drop=True),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 4,
                        lambda: pfc_emissions_rcp_endog()
                        .loc["RCP85", :]
                        .reset_coords(drop=True),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                            ["REGIONS 9 I"],
                        ),
                    ),
                ),
            ),
        ),
        lambda: if_then_else(
            select_rcp_for_exogenous_ghg_emissions_sp() == 1,
            lambda: pfc_emissions_rcp_endog().loc["RCP26", :].reset_coords(drop=True),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                lambda: pfc_emissions_rcp_endog()
                .loc["RCP45", :]
                .reset_coords(drop=True),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                    lambda: pfc_emissions_rcp_endog()
                    .loc["RCP60", :]
                    .reset_coords(drop=True),
                    lambda: pfc_emissions_rcp_endog()
                    .loc["RCP85", :]
                    .reset_coords(drop=True),
                ),
            ),
        ),
    )


@component.add(
    name="PFC emissions RCP endog",
    units="t/Year",
    subscripts=["RCP SCENARIO I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_pfc_emissions_rcp": 1,
        "share_co2_energy_emissions_by_region_9r": 1,
    },
)
def pfc_emissions_rcp_endog():
    """
    PFC anthropogenic emissions from RCPs depending on real GDP.
    """
    return global_pfc_emissions_rcp() * share_co2_energy_emissions_by_region_9r()


@component.add(
    name="SF6 EMISSIONS",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_rcp_ghg_emissions": 4,
        "sf6_emissions_rcp_endog": 8,
        "select_rcp_for_exogenous_ghg_emissions_sp": 3,
    },
)
def sf6_emissions():
    """
    Historic data + projections "Representative Concentration Pathways" (RCPs, see http://tntcat.iiasa.ac.at:8787/RcpDb/dsd?Action=htmlpage&page=compare) Choose RCP: 1. RCP 2.6 2. RCP 4.5 3. RCP 6.0 4. RCP 8.5
    """
    return xr.DataArray(
        if_then_else(
            switch_model_explorer() == 1,
            lambda: if_then_else(
                model_explorer_rcp_ghg_emissions() == 1,
                lambda: sum(
                    sf6_emissions_rcp_endog()
                    .loc["RCP26", :]
                    .reset_coords(drop=True)
                    .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                    dim=["REGIONS 9 I!"],
                ),
                lambda: if_then_else(
                    model_explorer_rcp_ghg_emissions() == 2,
                    lambda: sum(
                        sf6_emissions_rcp_endog()
                        .loc["RCP45", :]
                        .reset_coords(drop=True)
                        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                        dim=["REGIONS 9 I!"],
                    ),
                    lambda: if_then_else(
                        model_explorer_rcp_ghg_emissions() == 3,
                        lambda: sum(
                            sf6_emissions_rcp_endog()
                            .loc["RCP60", :]
                            .reset_coords(drop=True)
                            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                            dim=["REGIONS 9 I!"],
                        ),
                        lambda: if_then_else(
                            model_explorer_rcp_ghg_emissions() == 4,
                            lambda: sum(
                                sf6_emissions_rcp_endog()
                                .loc["RCP85", :]
                                .reset_coords(drop=True)
                                .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                                dim=["REGIONS 9 I!"],
                            ),
                            lambda: 0,
                        ),
                    ),
                ),
            ),
            lambda: if_then_else(
                select_rcp_for_exogenous_ghg_emissions_sp() == 1,
                lambda: sum(
                    sf6_emissions_rcp_endog()
                    .loc["RCP26", :]
                    .reset_coords(drop=True)
                    .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                    dim=["REGIONS 9 I!"],
                ),
                lambda: if_then_else(
                    select_rcp_for_exogenous_ghg_emissions_sp() == 2,
                    lambda: sum(
                        sf6_emissions_rcp_endog()
                        .loc["RCP45", :]
                        .reset_coords(drop=True)
                        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                        dim=["REGIONS 9 I!"],
                    ),
                    lambda: if_then_else(
                        select_rcp_for_exogenous_ghg_emissions_sp() == 3,
                        lambda: sum(
                            sf6_emissions_rcp_endog()
                            .loc["RCP60", :]
                            .reset_coords(drop=True)
                            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                            dim=["REGIONS 9 I!"],
                        ),
                        lambda: sum(
                            sf6_emissions_rcp_endog()
                            .loc["RCP85", :]
                            .reset_coords(drop=True)
                            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                            dim=["REGIONS 9 I!"],
                        ),
                    ),
                ),
            ),
        ),
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
        ["REGIONS 9 I"],
    )


@component.add(
    name="SF6 emissions RCP endog",
    units="t/Year",
    subscripts=["RCP SCENARIO I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "global_sf6_emissions_rcp": 1,
        "share_co2_energy_emissions_by_region_9r": 1,
    },
)
def sf6_emissions_rcp_endog():
    """
    SF6 anthropogenic emissions from RCPs depending on real GDP.
    """
    return global_sf6_emissions_rcp() * share_co2_energy_emissions_by_region_9r()


@component.add(
    name="share CO2 energy emissions by region 9R",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ghg_energy_chain_emissions_9r": 2},
)
def share_co2_energy_emissions_by_region_9r():
    """
    Share of CO2 energy emissions by region.
    """
    return zidz(
        total_ghg_energy_chain_emissions_9r().loc[:, "CO2"].reset_coords(drop=True),
        sum(
            total_ghg_energy_chain_emissions_9r()
            .loc[:, "CO2"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )


@component.add(
    name="SWITCH CLIMATE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_climate"},
)
def switch_climate():
    """
    This switch can take two values: 0: the climate module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters (if necessary if can be easily programmed to isolate also from land and water) 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_climate()


_ext_constant_switch_climate = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_CLIMATE",
    {},
    _root,
    {},
    "_ext_constant_switch_climate",
)


@component.add(
    name="SWITCH LAW2CLI LUC CO2 EMISSIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law2cli_luc_co2_emissions"},
)
def switch_law2cli_luc_co2_emissions():
    """
    1: land-use change emissions endogenous from land_and_water module 0: land-use change emissions exogenous
    """
    return _ext_constant_switch_law2cli_luc_co2_emissions()


_ext_constant_switch_law2cli_luc_co2_emissions = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2CLI_LUC_CO2_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_switch_law2cli_luc_co2_emissions",
)


@component.add(
    name="SWITCH NRG2CLI ENERGY CO2 EMISSIONS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2cli_energy_co2_emissions"},
)
def switch_nrg2cli_energy_co2_emissions():
    """
    1: energy-related emissions endogenous from energy module 0: energy-related emissions exogenous
    """
    return _ext_constant_switch_nrg2cli_energy_co2_emissions()


_ext_constant_switch_nrg2cli_energy_co2_emissions = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2CLI_ENERGY_CO2_EMISSIONS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2cli_energy_co2_emissions",
)


@component.add(
    name="total CO2 emissions",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_land_use_change_emissions": 1,
        "total_co2_energy_emissions_9r": 1,
        "co2_ippus_emissions_9r": 1,
        "co2_waste_emissions_9r": 1,
    },
)
def total_co2_emissions():
    """
    Total annual CO2 emissions.
    """
    return (
        co2_land_use_change_emissions()
        + total_co2_energy_emissions_9r()
        + co2_ippus_emissions_9r()
        + co2_waste_emissions_9r()
    )


@component.add(
    name="total CO2 energy emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate": 1,
        "switch_nrg2cli_energy_co2_emissions": 1,
        "total_ghg_energy_chain_emissions_9r": 1,
        "exo_co2_energy_emissions_9r": 1,
    },
)
def total_co2_energy_emissions_9r():
    """
    Total greenhouse gas emissions generated in all energy chain, by region and type of gas.
    """
    return if_then_else(
        np.logical_or(
            switch_climate() == 1, switch_nrg2cli_energy_co2_emissions() == 0
        ),
        lambda: total_ghg_energy_chain_emissions_9r()
        .loc[:, "CO2"]
        .reset_coords(drop=True),
        lambda: exo_co2_energy_emissions_9r(),
    )


@component.add(
    name="total CO2e emissions per capita 1R",
    units="t/(Year*person)",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_co2e_emissions_per_capita_9r": 1},
)
def total_co2e_emissions_per_capita_1r():
    """
    Total world emissions of carbon dioxide equivalent.
    """
    return (
        sum(
            total_co2e_emissions_per_capita_9r().rename(
                {"REGIONS 9 I": "REGIONS 9 I!"}
            ),
            dim=["REGIONS 9 I!"],
        )
        / 9
    )


@component.add(
    name="total CO2e emissions per capita 9R",
    units="t/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_ghg_emissions": 1,
        "population_9_regions": 1,
        "unit_conversion_t_gt": 1,
    },
)
def total_co2e_emissions_per_capita_9r():
    """
    total_CO2e_emissions_per_capita_9R
    """
    return zidz(total_ghg_emissions(), population_9_regions()) * unit_conversion_t_gt()


@component.add(
    name="total cumulative C emissions",
    units="Gt",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_cumulative_co2_emissions": 1, "unit_conversion_c_co2": 1},
)
def total_cumulative_c_emissions():
    """
    Total cumulative C emissions.
    """
    return total_cumulative_co2_emissions() * unit_conversion_c_co2()


@component.add(
    name="total cumulative CO2 emissions",
    units="Gt",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_total_cumulative_co2_emissions": 1},
    other_deps={
        "_integ_total_cumulative_co2_emissions": {
            "initial": {"cumulative_co2_emissions_to_2005": 1},
            "step": {"total_co2_emissions": 1},
        }
    },
)
def total_cumulative_co2_emissions():
    """
    Total cumulative CO2 emissions.
    """
    return _integ_total_cumulative_co2_emissions()


_integ_total_cumulative_co2_emissions = Integ(
    lambda: total_co2_emissions(),
    lambda: cumulative_co2_emissions_to_2005(),
    "_integ_total_cumulative_co2_emissions",
)


@component.add(
    name="total GHG emissions",
    units="GtCO2eq/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_co2_emissions": 1,
        "unit_conversion_t_gt": 1,
        "gwp_20_year": 14,
        "select_gwp_time_frame_sp": 14,
        "gwp_100_year": 14,
        "unit_conversion_tco2eq_gtco2eq": 14,
        "ch4_anthro_emissions": 1,
        "unit_conversion_t_mt": 2,
        "n2o_anthro_emissions": 1,
        "pfc_emissions": 1,
        "sf6_emissions": 1,
        "hfc_emissions": 9,
    },
)
def total_ghg_emissions():
    """
    Total greenhouse gas emissions from all sources.
    """
    return (
        total_co2_emissions()
        * unit_conversion_t_gt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CO2"]),
            lambda: float(gwp_100_year().loc["CO2"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + ch4_anthro_emissions()
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["CH4"]),
            lambda: float(gwp_100_year().loc["CH4"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + n2o_anthro_emissions()
        * unit_conversion_t_mt()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["N2O"]),
            lambda: float(gwp_100_year().loc["N2O"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + pfc_emissions()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["PFCs"]),
            lambda: float(gwp_100_year().loc["PFCs"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + sf6_emissions()
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["SF6"]),
            lambda: float(gwp_100_year().loc["SF6"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC134a"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC134a"]),
            lambda: float(gwp_100_year().loc["HFC134a"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC23"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC23"]),
            lambda: float(gwp_100_year().loc["HFC23"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC32"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC32"]),
            lambda: float(gwp_100_year().loc["HFC32"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC125"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC125"]),
            lambda: float(gwp_100_year().loc["HFC125"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC143a"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC143a"]),
            lambda: float(gwp_100_year().loc["HFC143a"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC152a"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC152a"]),
            lambda: float(gwp_100_year().loc["HFC152a"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC227ea"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC227ea"]),
            lambda: float(gwp_100_year().loc["HFC227ea"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC245ca"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC245ca"]),
            lambda: float(gwp_100_year().loc["HFC245ca"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
        + hfc_emissions().loc[:, "HFC4310mee"].reset_coords(drop=True)
        * if_then_else(
            select_gwp_time_frame_sp() == 1,
            lambda: float(gwp_20_year().loc["HFC4310mee"]),
            lambda: float(gwp_100_year().loc["HFC4310mee"]),
        )
        / unit_conversion_tco2eq_gtco2eq()
    )


@component.add(
    name="total GHG energy emissions 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I", "GHG I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_ghg_energy_chain_emissions_9r": 1},
)
def total_ghg_energy_emissions_9r():
    return total_ghg_energy_chain_emissions_9r()
