"""
Module energytransformation.main
Translated using PySD version 3.14.0
"""

@component.add(
    name="bioenergy input share",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"energy_available_from_crops": 1, "ti_gas_liquids": 1},
)
def bioenergy_input_share():
    """
    Endogenous bioenergy input share as given by the availability in the land-use module.
    """
    return zidz(energy_available_from_crops(), ti_gas_liquids())


@component.add(
    name="delayed TS bioenergy input share",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_bioenergy_input_share": 1},
    other_deps={
        "_delayfixed_delayed_ts_bioenergy_input_share": {
            "initial": {"time_step": 1},
            "step": {"bioenergy_input_share": 1},
        }
    },
)
def delayed_ts_bioenergy_input_share():
    """
    DELAY to avoid feedback problems.
    """
    return _delayfixed_delayed_ts_bioenergy_input_share()


_delayfixed_delayed_ts_bioenergy_input_share = DelayFixed(
    lambda: bioenergy_input_share(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_bioenergy_input_share",
)


@component.add(
    name="exogenous PROTRA input shares",
    units="1",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_exogenous_protra_input_shares": 1},
    other_deps={
        "_integ_exogenous_protra_input_shares": {
            "initial": {"protra_input_shares_empiric": 1},
            "step": {"variation_exogenous_protra_input_shares": 1},
        }
    },
)
def exogenous_protra_input_shares():
    """
    Input fuel shares (some transformation processes can take more than one fuel, e.g. gas plants can be driven with biogas or fossil gas).
    """
    return _integ_exogenous_protra_input_shares()


_integ_exogenous_protra_input_shares = Integ(
    lambda: variation_exogenous_protra_input_shares(),
    lambda: protra_input_shares_empiric(),
    "_integ_exogenous_protra_input_shares",
)


@component.add(
    name="FE domestic",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_net_import_share_by_region": 1, "fe_excluding_trade": 1},
)
def fe_domestic():
    """
    domestic part of TFC
    """
    return (
        (
            1
            - fe_net_import_share_by_region()
            .loc[:, _subscript_dict["REGIONS 9 I"]]
            .rename({"REGIONS 36 I": "REGIONS 9 I"})
        )
        * fe_excluding_trade().transpose("NRG FE I", "REGIONS 9 I")
    ).transpose("REGIONS 9 I", "NRG FE I")


@component.add(
    name="FE excluding trade",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_demand_transformation": 1,
        "iea_total_fe_empirical": 1,
        "final_energy_demand_by_fe_9r": 1,
        "final_non_energy_demand_by_fe_9r": 1,
        "unit_conversion_tj_ej": 1,
    },
)
def fe_excluding_trade():
    """
    Final energy Demand coming from End-Use Submodule including both energy end-uses and non-energy uses. does NOT include imports or exports, only domestic demand. equivalent to Total Final Consumpton (TFC) in IEA energy balances.
    """
    return if_then_else(
        switch_nrg_demand_transformation() == 0,
        lambda: iea_total_fe_empirical(),
        lambda: (final_energy_demand_by_fe_9r() + final_non_energy_demand_by_fe_9r())
        / unit_conversion_tj_ej(),
    )


@component.add(
    name="FE EXPORT MARKET SHARE",
    units="DMNL",
    subscripts=["NRG FE I", "REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fe_export_market_share"},
)
def fe_export_market_share():
    """
    Market share of global export market, extracted from IEA energy balances for 2015 and kept constant over the rest of the modelling horizon
    """
    return _ext_constant_fe_export_market_share()


_ext_constant_fe_export_market_share = ExtConstant(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_EXPORT_MARKET_SHARE",
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
    },
    _root,
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
    },
    "_ext_constant_fe_export_market_share",
)


@component.add(
    name="FE net exports by region",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"global_fe_trade": 1, "fe_export_market_share": 1},
)
def fe_net_exports_by_region():
    """
    TFC exports
    """
    return (
        global_fe_trade()
        * fe_export_market_share()
        .loc[:, _subscript_dict["REGIONS 9 I"]]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
    ).transpose("REGIONS 9 I", "NRG FE I")


@component.add(
    name="FE NET IMPORT SHARE BY REGION",
    units="DMNL",
    subscripts=["NRG FE I", "REGIONS 36 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_fe_net_import_share_by_region"},
)
def fe_net_import_share_by_region():
    """
    Import shares gross domestic consumption derived from IEA energy balances (fixed for further simulation)
    """
    return _ext_constant_fe_net_import_share_by_region()


_ext_constant_fe_net_import_share_by_region = ExtConstant(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_IMPORT_SHARE_BY_REGION",
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
    },
    _root,
    {
        "NRG FE I": _subscript_dict["NRG FE I"],
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
    },
    "_ext_constant_fe_net_import_share_by_region",
)


@component.add(
    name="FE net imports",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1, "fe_net_import_share_by_region": 1},
)
def fe_net_imports():
    """
    Imports of final energy calculated from fixed import share.
    """
    return fe_excluding_trade() * fe_net_import_share_by_region().loc[
        :, _subscript_dict["REGIONS 9 I"]
    ].rename({"REGIONS 36 I": "REGIONS 9 I"}).transpose("REGIONS 9 I", "NRG FE I")


@component.add(
    name="global FE trade",
    units="EJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_net_imports": 1},
)
def global_fe_trade():
    """
    Total market size of final energy trade = sum of all regions imports.
    """
    return sum(
        fe_net_imports().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="IEA TOTAL FE EMPIRICAL",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_iea_total_fe_empirical",
        "__data__": "_ext_data_iea_total_fe_empirical",
        "time": 1,
    },
)
def iea_total_fe_empirical():
    """
    Empiric data for total final energy consumption from IEA energy balances in WILIAM regional aggregation
    """
    return _ext_data_iea_total_fe_empirical(time())


_ext_data_iea_total_fe_empirical = ExtData(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_CHINA",
    "interpolate",
    {"REGIONS 9 I": ["CHINA"], "NRG FE I": _subscript_dict["NRG FE I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_data_iea_total_fe_empirical",
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_INDIA",
    "interpolate",
    {"REGIONS 9 I": ["INDIA"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_RUSSIA",
    "interpolate",
    {"REGIONS 9 I": ["RUSSIA"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_UK",
    "interpolate",
    {"REGIONS 9 I": ["UK"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_EU27",
    "interpolate",
    {"REGIONS 9 I": ["EU27"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_EASOC",
    "interpolate",
    {"REGIONS 9 I": ["EASOC"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_LATAM",
    "interpolate",
    {"REGIONS 9 I": ["LATAM"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_USMCA",
    "interpolate",
    {"REGIONS 9 I": ["USMCA"], "NRG FE I": _subscript_dict["NRG FE I"]},
)

_ext_data_iea_total_fe_empirical.add(
    "model_parameters/energy/FE_Trade_Shares.xlsx",
    "VENSIM_IMPORT",
    "TFC_TIME",
    "TFC_LROW",
    "interpolate",
    {"REGIONS 9 I": ["LROW"], "NRG FE I": _subscript_dict["NRG FE I"]},
)


@component.add(
    name="PE by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_and_commodity": 1},
)
def pe_by_commodity():
    """
    Domestic primary energy (PE) demand/consumption resulting from final energy (FE) demand and the current energy system setup. +++++++++++ This formula can be used for debugging: IF_THEN_ELSE ( Time < 2006, SUM(PE_by_PROREF_and_commodity[REGIONS_9_I,NRG_PROREF_I!,NRG_PE_I]) , 0 )
    """
    return sum(
        pe_by_proref_and_commodity().rename({"NRG PROREF I": "NRG PROREF I!"}),
        dim=["NRG PROREF I!"],
    )


@component.add(
    name="PE by commodity dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_and_commodity_dem": 1},
)
def pe_by_commodity_dem():
    """
    Domestic primary energy (PE) demand/consumption resulting from final energy (FE) demand and the current energy system setup.
    """
    return sum(
        pe_by_proref_and_commodity_dem().rename({"NRG PROREF I": "NRG PROREF I!"}),
        dim=["NRG PROREF I!"],
    )


@component.add(
    name="PE by PROREF",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_refinery_process": 1, "proref_conversion_factors": 1},
)
def pe_by_proref():
    """
    PE required taking into account refineration losses (oil refineration, coal refineration, bio refinery, and natural gas 2 hydrogen processing).
    """
    return xidz(ti_by_refinery_process(), proref_conversion_factors(), 0)


@component.add(
    name="PE by PROREF and commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref": 1, "proref_input_shares_sp": 1},
)
def pe_by_proref_and_commodity():
    """
    PE disaggregated by refinery process and commodity
    """
    return pe_by_proref() * proref_input_shares_sp()


@component.add(
    name="PE by PROREF and commodity dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I", "NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_proref_dem": 1, "proref_input_shares_sp": 1},
)
def pe_by_proref_and_commodity_dem():
    """
    PE disaggregated by refinery process and commodity
    """
    return pe_by_proref_dem() * proref_input_shares_sp()


@component.add(
    name="PE by PROREF dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_refinery_process_dem": 1, "proref_conversion_factors": 1},
)
def pe_by_proref_dem():
    """
    PE required taking into account refineration losses (oil refineration, coal refineration, bio refinery, and natural gas 2 hydrogen processing).
    """
    return xidz(ti_by_refinery_process_dem(), proref_conversion_factors(), 0)


@component.add(
    name="PROSUP flexibility technologies",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_to_p2h_technologies": 1, "to_commodities_electrolytic_h2": 1},
)
def prosup_flexibility_technologies():
    """
    Flexibility Technologies contain: Power2Heat, Synthetic Gas production, FE_Hydrogen production (=H2 & H2 derived Fuels for final consumption)
    """
    return (
        sum(
            prosup_to_p2h_technologies().rename({"PROSUP P2H I": "PROSUP P2H I!"}),
            dim=["PROSUP P2H I!"],
        )
        + to_commodities_electrolytic_h2()
    )


@component.add(
    name="PROSUP flexibility technologies demand aggregated",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_flexibility_technologies": 1},
)
def prosup_flexibility_technologies_demand_aggregated():
    return prosup_flexibility_technologies()


@component.add(
    name="PROSUP sector energy own consumption per commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "fe_excluding_trade": 5,
        "prosup_energy_sector_own_consumption_share": 5,
    },
)
def prosup_sector_energy_own_consumption_per_commodity():
    """
    Energy sector own consumption for elec, gas, liquids and (district-)heat excluding storage losses (!)
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
        (
            fe_excluding_trade().loc[:, "FE elec"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP sector energy own consumption elec"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        (
            fe_excluding_trade().loc[:, "FE gas"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP sector energy own consumption gas"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        (
            fe_excluding_trade().loc[:, "FE heat"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP sector energy own consumption heat"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = 0
    value.loc[:, ["TO liquid"]] = (
        (
            fe_excluding_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP sector energy own consumption liquid"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = 0
    value.loc[:, ["TO solid fossil"]] = (
        (
            fe_excluding_trade().loc[:, "FE solid fossil"].reset_coords(drop=True)
            * prosup_energy_sector_own_consumption_share()
            .loc[:, "PROSUP sector energy own consumption solid fossil"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROSUP storage losses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"total_prosto_losses_elec": 1, "imv_prosup_storage_losses": 2},
)
def prosup_storage_losses():
    """
    Storage losses for elec, gas and heat
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
        total_prosto_losses_elec()
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        imv_prosup_storage_losses()
        .loc[:, "PROSUP storage losses gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        imv_prosup_storage_losses()
        .loc[:, "PROSUP storage losses heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = 0
    value.loc[:, ["TO liquid"]] = 0
    value.loc[:, ["TO solid bio"]] = 0
    value.loc[:, ["TO solid fossil"]] = 0
    return value


@component.add(
    name="PROSUP transmission losses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 3, "prosup_transmission_loss_shares": 3},
)
def prosup_transmission_losses():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
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
        (
            fe_excluding_trade().loc[:, "FE elec"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP transmission losses elec"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        (
            fe_excluding_trade().loc[:, "FE gas"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP transmission losses gas"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        (
            fe_excluding_trade().loc[:, "FE heat"].reset_coords(drop=True)
            * prosup_transmission_loss_shares()
            .loc[:, "PROSUP transmission losses heat"]
            .reset_coords(drop=True)
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = 0
    value.loc[:, ["TO liquid"]] = 0
    value.loc[:, ["TO solid bio"]] = 0
    value.loc[:, ["TO solid fossil"]] = 0
    return value


@component.add(
    name="PROTRA conversion efficiencies complete matrix",
    units="DMNL",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_conversion_efficiency_elec_2015": 1,
        "protra_conversion_efficiency_heat_2015": 1,
        "protra_no_process_efficiencies_36r": 5,
    },
)
def protra_conversion_efficiencies_complete_matrix():
    """
    complete matrix (PROTRA x TO) of conversion efficincies for all 36 regions, based on empirical data.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[:, ["TO elec"], :] = (
        protra_conversion_efficiency_elec_2015()
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"], :] = (
        protra_conversion_efficiency_heat_2015()
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO hydrogen", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO solid bio", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO solid fossil", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"], :] = (
        protra_no_process_efficiencies_36r()
        .loc[:, "TO gas", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA CONVERSION EFFICIENCY ELEC 2015",
    units="DMNL",
    subscripts=["REGIONS 36 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_conversion_efficiency_elec_2015"},
)
def protra_conversion_efficiency_elec_2015():
    """
    elec conversion efficiency (elec output per total input) of PROTRA conversion technologies for all 36 regions, based on empirical data.
    """
    return _ext_constant_protra_conversion_efficiency_elec_2015()


_ext_constant_protra_conversion_efficiency_elec_2015 = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "el_eff",
    "TO_elec_conversion_efficiency_2015",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_conversion_efficiency_elec_2015",
)


@component.add(
    name="PROTRA CONVERSION EFFICIENCY HEAT 2015",
    units="DMNL",
    subscripts=["REGIONS 36 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_conversion_efficiency_heat_2015"},
)
def protra_conversion_efficiency_heat_2015():
    """
    heat conversion efficiency (Heat output per total input) of PROTRA conversion technologies for all 36 regions in year 2015, based on empirical data.
    """
    return _ext_constant_protra_conversion_efficiency_heat_2015()


_ext_constant_protra_conversion_efficiency_heat_2015 = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "th_eff",
    "TO_heat_conversion_efficiency_2015",
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_conversion_efficiency_heat_2015",
)


@component.add(
    name="PROTRA fuel utilization ratio",
    units="DMNL",
    subscripts=["REGIONS 36 I", "NRG PROTRA I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"protra_conversion_efficiencies_complete_matrix": 1},
)
def protra_fuel_utilization_ratio():
    """
    TO per 1 Unit of TI (CHPs collapsed to fuel utilization ratio)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 36 I", "NRG PROTRA I"],
    )
    value.loc[_subscript_dict["REGIONS 9 I"], _subscript_dict["PROTRA PP CHP HP I"]] = (
        sum(
            protra_conversion_efficiencies_complete_matrix()
            .loc[
                _subscript_dict["REGIONS 9 I"], :, _subscript_dict["PROTRA PP CHP HP I"]
            ]
            .rename(
                {
                    "REGIONS 36 I": "REGIONS 9 I",
                    "NRG TO I": "NRG TO I!",
                    "NRG PROTRA I": "PROTRA PP CHP HP I",
                }
            ),
            dim=["NRG TO I!"],
        ).values
    )
    value.loc[:, _subscript_dict["PROTRA NP I"]] = 1
    return value


@component.add(
    name="PROTRA input share TI bio",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "switch_nrg_limited_res_potentials": 2,
        "exogenous_protra_input_shares": 2,
        "delayed_ts_bioenergy_input_share": 2,
    },
)
def protra_input_share_ti_bio():
    """
    PROTRA inputs shares bioenergy for gas and liquids. For the fossil TI share it is set to 0 since it will be defined in the next variable.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "NRG TI I": _subscript_dict["NRG TI I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    )
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: exogenous_protra_input_shares()
            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
            lambda: delayed_ts_bioenergy_input_share().expand_dims(
                {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0, switch_nrg_limited_res_potentials() == 0
            ),
            lambda: exogenous_protra_input_shares()
            .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], "TI liquid bio"]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
            lambda: delayed_ts_bioenergy_input_share().expand_dims(
                {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]}, 1
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid bio"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        False
    )
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA input shares",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exogenous_protra_input_shares": 1, "protra_input_share_ti_bio": 4},
)
def protra_input_shares():
    """
    PROTRA inputs shares after accounting for eventual bioenergy limits from land-use module.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "NRG TI I": _subscript_dict["NRG TI I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas fossil"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        False
    )
    except_subs.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid fossil"]] = (
        False
    )
    value.values[except_subs.values] = exogenous_protra_input_shares().values[
        except_subs.values
    ]
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = (
        protra_input_share_ti_bio()
        .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA TI GAS I"})
        .expand_dims({"NRG COMMODITIES I": ["TI gas bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas fossil"]] = (
        (
            1
            - protra_input_share_ti_bio()
            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA TI GAS I"})
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        protra_input_share_ti_bio()
        .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], "TI liquid bio"]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"})
        .expand_dims({"NRG COMMODITIES I": ["TI liquid bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid fossil"]] = (
        (
            1
            - protra_input_share_ti_bio()
            .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], "TI liquid bio"]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"})
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA NO PROCESS EFFICIENCIES",
    units="DMNL",
    subscripts=["NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_no_process_efficiencies"},
)
def protra_no_process_efficiencies():
    """
    instrumental efficiencies, assigning PROTRA processes (blending processes and direct run-through processess) to the acompaning TO-fuels
    """
    return _ext_constant_protra_no_process_efficiencies()


_ext_constant_protra_no_process_efficiencies = ExtConstant(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_gas*",
    {"NRG COMMODITIES I": ["TO gas"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    _root,
    {
        "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_no_process_efficiencies",
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_hydrogen*",
    {
        "NRG COMMODITIES I": ["TO hydrogen"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_liquid*",
    {
        "NRG COMMODITIES I": ["TO liquid"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_solid_bio*",
    {
        "NRG COMMODITIES I": ["TO solid bio"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
)

_ext_constant_protra_no_process_efficiencies.add(
    "model_parameters/energy/PROTRA_efficiency.xlsx",
    "aux_eff",
    "aux_eff_TO_solid_fossil*",
    {
        "NRG COMMODITIES I": ["TO solid fossil"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
)


@component.add(
    name="PROTRA no process efficiencies 36R",
    units="DMNL",
    subscripts=["REGIONS 36 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_no_process_efficiencies": 5},
)
def protra_no_process_efficiencies_36r():
    """
    upscaled for 36 regions
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 36 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    )
    value.loc[:, ["TO gas"], :] = (
        protra_no_process_efficiencies()
        .loc["TO gas", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, 0)
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"], :] = (
        protra_no_process_efficiencies()
        .loc["TO hydrogen", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, 0)
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"], :] = (
        protra_no_process_efficiencies()
        .loc["TO liquid", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, 0)
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"], :] = (
        protra_no_process_efficiencies()
        .loc["TO solid bio", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, 0)
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"], :] = (
        protra_no_process_efficiencies()
        .loc["TO solid fossil", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, 0)
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="share total transmission loss",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"total_prosup_transmission_losses": 3, "fe_excluding_trade": 3},
)
def share_total_transmission_loss():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
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
        zidz(
            total_prosup_transmission_losses()
            .loc[:, "TO elec"]
            .reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE elec"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        zidz(
            total_prosup_transmission_losses().loc[:, "TO gas"].reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE gas"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        zidz(
            total_prosup_transmission_losses()
            .loc[:, "TO heat"]
            .reset_coords(drop=True),
            fe_excluding_trade().loc[:, "FE heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = 0
    value.loc[:, ["TO liquid"]] = 0
    value.loc[:, ["TO solid bio"]] = 0
    value.loc[:, ["TO solid fossil"]] = 0
    return value


@component.add(
    name="SWITCH NRG DEMAND TRANSFORMATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_demand_transformation"},
)
def switch_nrg_demand_transformation():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 0=hard-link to Final Energy Consumption 2005-2019 (Source: IEA energy balances) 1: the (sub)module runs integrated with the rest of WILIAM.1=Use endogeneous FE Demand .
    """
    return _ext_constant_switch_nrg_demand_transformation()


_ext_constant_switch_nrg_demand_transformation = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_DEMAND_TRANSFORMATION",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_demand_transformation",
)


@component.add(
    name="SWITCH NRG TRADE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_trade"},
)
def switch_nrg_trade():
    """
    switch: 0 to deactivate FE trade, 1 to activate
    """
    return _ext_constant_switch_nrg_trade()


_ext_constant_switch_nrg_trade = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_TRADE",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_trade",
)


@component.add(
    name="SWITCH POLICY SHARE BIOENERGY IN TI LIQUIDS AND GASES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp"
    },
)
def switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp():
    """
    SWITCH policy: 0: policy deactivated (no replacement of oil and natural gas by biofuels and biogases, respectively) 1: poilicy activated (replacement of oil and natural gas by biofuels and biogases, respectively)
    """
    return _ext_constant_switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp()


_ext_constant_switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_POLICY_SHARE_BIOENERGY_IN_TI_LIQUIDS_AND_GASES_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp",
)


@component.add(
    name="TARGET SHARE BIOENERGY IN TI LIQUIDS AND GASES SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_share_bioenergy_in_ti_liquids_and_gases_sp"
    },
)
def target_share_bioenergy_in_ti_liquids_and_gases_sp():
    """
    Target value by region in the final year of the share of bioenergy in the total liquids and gases (bioenergy + fossil).
    """
    return _ext_constant_target_share_bioenergy_in_ti_liquids_and_gases_sp()


_ext_constant_target_share_bioenergy_in_ti_liquids_and_gases_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "TARGET_SHARE_BIOENERGY_IN_TI_LIQUIDS_AND_GASES_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_target_share_bioenergy_in_ti_liquids_and_gases_sp",
)


@component.add(
    name="TI by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_protra_and_commodity": 1},
)
def ti_by_commodity():
    """
    TI required to satisfy FE demand from society (aggregated by TI Commodity), taking into account type of fuel (fossil/bio) that the plants are fed with (currently exogeneous).
    """
    return sum(
        ti_by_protra_and_commodity().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="TI by commodity dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_protra_and_commodity_dem": 1},
)
def ti_by_commodity_dem():
    """
    TI required to satisfy FE demand from society (aggregated by TI Commodity), taking into account type of fuel (fossil/bio) that the plants are fed with (currently exogeneous).
    """
    return sum(
        ti_by_protra_and_commodity_dem().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="TI by process",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_allocated_by_process": 1, "protra_fuel_utilization_ratio": 1},
)
def ti_by_process():
    """
    TI required to satisfy FE demand from society taking into account conversion efficiencies
    """
    return to_allocated_by_process() / protra_fuel_utilization_ratio().loc[
        _subscript_dict["REGIONS 9 I"], :
    ].rename({"REGIONS 36 I": "REGIONS 9 I"})


@component.add(
    name="TI by PROREF and commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_commodity": 1, "proref_output_shares": 1},
)
def ti_by_proref_and_commodity():
    return (ti_by_commodity() * proref_output_shares()).transpose(
        "REGIONS 9 I", "NRG PROREF I", "NRG TI I"
    )


@component.add(
    name="TI by PROREF and commodity dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_commodity_dem": 1, "proref_output_shares": 1},
)
def ti_by_proref_and_commodity_dem():
    return (ti_by_commodity_dem() * proref_output_shares()).transpose(
        "REGIONS 9 I", "NRG PROREF I", "NRG TI I"
    )


@component.add(
    name="TI by PROTRA and commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 1, "protra_input_shares": 1},
)
def ti_by_protra_and_commodity():
    """
    TI by transformation technology and type of TI-commodity (after Input-fuel-share for those technologies that can take more than one input fuel, e.g. biogas/fossil gas, etc.)
    """
    return ti_by_process() * protra_input_shares()


@component.add(
    name="TI by PROTRA and commodity dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 1, "exogenous_protra_input_shares": 1},
)
def ti_by_protra_and_commodity_dem():
    """
    TI by transformation technology and type of TI-commodity (after Input-fuel-share for those technologies that can take more than one input fuel, e.g. biogas/fossil gas, etc.)
    """
    return ti_by_process() * exogenous_protra_input_shares()


@component.add(
    name="TI by refinery process",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_proref_and_commodity": 1},
)
def ti_by_refinery_process():
    """
    TI required to satisfy FE demand of society disaggregated to refinery processes with shares.
    """
    return sum(
        ti_by_proref_and_commodity().rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )


@component.add(
    name="TI by refinery process dem",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROREF I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_proref_and_commodity_dem": 1},
)
def ti_by_refinery_process_dem():
    """
    TI required to satisfy FE demand of society disaggregated to refinery processes with shares.
    """
    return sum(
        ti_by_proref_and_commodity_dem().rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )


@component.add(
    name="TI gas liquids",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ti_by_process": 2},
)
def ti_gas_liquids():
    """
    TI from gas and liquids. Auxiliary variable to implement feedback of crops available for energy.
    """
    return sum(
        ti_by_process()
        .loc[:, _subscript_dict["PROTRA TI GAS I"]]
        .rename({"NRG PROTRA I": "PROTRA TI GAS I!"}),
        dim=["PROTRA TI GAS I!"],
    ) + sum(
        ti_by_process()
        .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"]]
        .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I!"}),
        dim=["PROTRA TI LIQUIDS I!"],
    )


@component.add(
    name="TO allocated by process",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_to_allocated": 1},
)
def to_allocated_by_process():
    """
    TO required to satisfy FE-demand from society (disaggregated by transformation technology)
    """
    return sum(
        protra_to_allocated().rename({"NRG TO I": "NRG TO I!"}), dim=["NRG TO I!"]
    )


@component.add(
    name="TO by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_fe_including_net_trade": 7,
        "prosup_transmission_losses": 3,
        "prosup_storage_losses": 7,
        "prosup_sector_energy_own_consumption_per_commodity": 7,
        "prosup_flexibility_technologies": 7,
    },
)
def to_by_commodity():
    """
    Transformation Output required to fulfill final energy demand. TO = Final Energy + Transmission Losses + storage losses + sector energy own consumption + Flexibility Technology Utilization (Hydrogen, P2Heat, P2Gas, P2Liquid). Note 1: for TO_heat, TO_hydrogen, TO_liquid and TO_gas the amount of energy from the corresponding flexibility technologies is substracted; it reduces the amount of TO that needs to be covered by other process. Note 2: for TO_elec, TO_solid_bio and TO_solid_fossil, the amount of energy from the corresponding flexibility technologies (mostly electricity) increases the amount of TO needed to run these flexibility processes.
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
            0,
            total_fe_including_net_trade().loc[:, "FE elec"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO elec"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO elec"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO elec"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE gas"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO gas"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO gas"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO gas"]
            .reset_coords(drop=True)
            - prosup_flexibility_technologies()
            .loc[:, "TO gas"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE heat"].reset_coords(drop=True)
            + prosup_transmission_losses().loc[:, "TO heat"].reset_coords(drop=True)
            + prosup_storage_losses().loc[:, "TO heat"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO heat"]
            .reset_coords(drop=True)
            - prosup_flexibility_technologies()
            .loc[:, "TO heat"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE hydrogen"].reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO hydrogen"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO hydrogen"]
            .reset_coords(drop=True)
            - prosup_flexibility_technologies()
            .loc[:, "TO hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade().loc[:, "FE liquid"].reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO liquid"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO liquid"]
            .reset_coords(drop=True)
            - prosup_flexibility_technologies()
            .loc[:, "TO liquid"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade()
            .loc[:, "FE solid bio"]
            .reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO solid bio"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO solid bio"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO solid bio"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"]] = (
        np.maximum(
            0,
            total_fe_including_net_trade()
            .loc[:, "FE solid fossil"]
            .reset_coords(drop=True)
            + 0
            + prosup_storage_losses().loc[:, "TO solid fossil"].reset_coords(drop=True)
            + prosup_sector_energy_own_consumption_per_commodity()
            .loc[:, "TO solid fossil"]
            .reset_coords(drop=True)
            + prosup_flexibility_technologies()
            .loc[:, "TO solid fossil"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="total FE excluding trade by region",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1},
)
def total_fe_excluding_trade_by_region():
    return sum(
        fe_excluding_trade().rename({"NRG FE I": "NRG FE I!"}), dim=["NRG FE I!"]
    )


@component.add(
    name="total FE IEA Model CHECK",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"iea_total_fe_empirical": 1, "fe_excluding_trade": 1},
)
def total_fe_iea_model_check():
    return iea_total_fe_empirical() - fe_excluding_trade()


@component.add(
    name="total FE including net trade",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_trade": 1,
        "fe_net_exports_by_region": 1,
        "fe_domestic": 1,
        "fe_excluding_trade": 1,
    },
)
def total_fe_including_net_trade():
    """
    total final energy demand/consumption, including imports/exports of final energy commodities (or transformation inputs).
    """
    return if_then_else(
        switch_nrg_trade() == 1,
        lambda: fe_domestic() + fe_net_exports_by_region(),
        lambda: fe_excluding_trade(),
    )


@component.add(
    name="total PE by region",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def total_pe_by_region():
    """
    Total primary energy by region.
    """
    return sum(pe_by_commodity().rename({"NRG PE I": "NRG PE I!"}), dim=["NRG PE I!"])


@component.add(
    name="total PROSUP transmission losses",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_transmission_losses": 7,
        "elec_transmission_losses_by_prosto": 1,
    },
)
def total_prosup_transmission_losses():
    """
    transmission losses for grid-bound energy commodities (elec, gas, heat)
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
        (
            prosup_transmission_losses().loc[:, "TO elec"].reset_coords(drop=True)
            + sum(
                elec_transmission_losses_by_prosto().rename(
                    {"PROSTO ELEC I": "PROSTO ELEC I!"}
                ),
                dim=["PROSTO ELEC I!"],
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        prosup_transmission_losses()
        .loc[:, "TO gas"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        prosup_transmission_losses()
        .loc[:, "TO heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = (
        prosup_transmission_losses()
        .loc[:, "TO hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"]] = (
        prosup_transmission_losses()
        .loc[:, "TO liquid"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = (
        prosup_transmission_losses()
        .loc[:, "TO solid bio"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"]] = (
        prosup_transmission_losses()
        .loc[:, "TO solid fossil"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="variation exogenous PROTRA input shares",
    units="1/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 4,
        "model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases": 4,
        "switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp": 4,
        "year_final_share_bioenergy_in_ti_liquids_and_gases_sp": 8,
        "time": 8,
        "target_share_bioenergy_in_ti_liquids_and_gases_sp": 4,
        "year_initial_share_bioenergy_in_ti_liquids_and_gases_sp": 8,
        "protra_input_shares_empiric": 4,
    },
)
def variation_exogenous_protra_input_shares():
    """
    PROTRA input shares after applying policies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "NRG TI I": _subscript_dict["NRG TI I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "NRG TI I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas fossil"]] = False
    except_subs.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        False
    )
    except_subs.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid fossil"]] = (
        False
    )
    value.values[except_subs.values] = 0
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas bio"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA TI GAS I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp() == 0
                ).expand_dims(
                    {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                    },
                    ["REGIONS 9 I", "PROTRA TI GAS I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                        ).expand_dims(
                            {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                        ),
                        lambda: zidz(
                            target_share_bioenergy_in_ti_liquids_and_gases_sp()
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas bio"]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                            (
                                year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                            ).expand_dims(
                                {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]},
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI GAS I"], ["TI gas fossil"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas fossil"]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA TI GAS I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp() == 0
                ).expand_dims(
                    {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                    },
                    ["REGIONS 9 I", "PROTRA TI GAS I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                        },
                        ["REGIONS 9 I", "PROTRA TI GAS I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                        ).expand_dims(
                            {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]}, 1
                        ),
                        lambda: zidz(
                            (1 - target_share_bioenergy_in_ti_liquids_and_gases_sp())
                            - protra_input_shares_empiric()
                            .loc[:, _subscript_dict["PROTRA TI GAS I"], "TI gas fossil"]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI GAS I"}),
                            (
                                year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                            ).expand_dims(
                                {"PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"]},
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI GAS I": _subscript_dict["PROTRA TI GAS I"],
                            },
                            ["REGIONS 9 I", "PROTRA TI GAS I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI gas fossil"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid bio"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], "TI liquid bio"]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA TI LIQUIDS I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp() == 0
                ).expand_dims(
                    {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"],
                    },
                    ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]},
                        1,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                        ).expand_dims(
                            {
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ]
                            },
                            1,
                        ),
                        lambda: zidz(
                            target_share_bioenergy_in_ti_liquids_and_gases_sp()
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA TI LIQUIDS I"],
                                "TI liquid bio",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                            (
                                year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                            ).expand_dims(
                                {
                                    "PROTRA TI LIQUIDS I": _subscript_dict[
                                        "PROTRA TI LIQUIDS I"
                                    ]
                                },
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid bio"]}, 2)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], ["TI liquid fossil"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_target_share_bioenergy_in_fossil_liquids_and_gases()
            .loc[:, _subscript_dict["PROTRA TI LIQUIDS I"], "TI liquid fossil"]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA TI LIQUIDS I"}),
            lambda: if_then_else(
                (
                    switch_policy_share_bioenergy_in_ti_liquids_and_gases_sp() == 0
                ).expand_dims(
                    {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"],
                    },
                    ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                ),
                lambda: if_then_else(
                    (
                        time()
                        < year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                    ).expand_dims(
                        {"PROTRA TI LIQUIDS I": _subscript_dict["PROTRA TI LIQUIDS I"]},
                        1,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA TI LIQUIDS I": _subscript_dict[
                                "PROTRA TI LIQUIDS I"
                            ],
                        },
                        ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                    ),
                    lambda: if_then_else(
                        (
                            time()
                            < year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                        ).expand_dims(
                            {
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ]
                            },
                            1,
                        ),
                        lambda: zidz(
                            (1 - target_share_bioenergy_in_ti_liquids_and_gases_sp())
                            - protra_input_shares_empiric()
                            .loc[
                                :,
                                _subscript_dict["PROTRA TI LIQUIDS I"],
                                "TI liquid fossil",
                            ]
                            .reset_coords(drop=True)
                            .rename({"NRG PROTRA I": "PROTRA TI LIQUIDS I"}),
                            (
                                year_final_share_bioenergy_in_ti_liquids_and_gases_sp()
                                - year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()
                            ).expand_dims(
                                {
                                    "PROTRA TI LIQUIDS I": _subscript_dict[
                                        "PROTRA TI LIQUIDS I"
                                    ]
                                },
                                1,
                            ),
                        ),
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                "PROTRA TI LIQUIDS I": _subscript_dict[
                                    "PROTRA TI LIQUIDS I"
                                ],
                            },
                            ["REGIONS 9 I", "PROTRA TI LIQUIDS I"],
                        ),
                    ),
                ),
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TI liquid fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="world FE excluding trade by commodity",
    units="EJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1},
)
def world_fe_excluding_trade_by_commodity():
    return sum(
        fe_excluding_trade().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="world PE by commodity",
    units="EJ/Year",
    subscripts=["NRG PE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pe_by_commodity": 1},
)
def world_pe_by_commodity():
    """
    World primary energy demand aggregated by PE (primary energy) commodity.
    """
    return sum(
        pe_by_commodity().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="YEAR FINAL SHARE BIOENERGY IN TI LIQUIDS AND GASES SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_share_bioenergy_in_ti_liquids_and_gases_sp"
    },
)
def year_final_share_bioenergy_in_ti_liquids_and_gases_sp():
    """
    Final year to implement the policy of replacing fossil fuel by bioenergy for liquids and gases.
    """
    return _ext_constant_year_final_share_bioenergy_in_ti_liquids_and_gases_sp()


_ext_constant_year_final_share_bioenergy_in_ti_liquids_and_gases_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_SHARE_BIOENERGY_IN_TI_LIQUIDS_AND_GASES_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_share_bioenergy_in_ti_liquids_and_gases_sp",
)


@component.add(
    name="YEAR INITIAL SHARE BIOENERGY IN TI LIQUIDS AND GASES SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_share_bioenergy_in_ti_liquids_and_gases_sp"
    },
)
def year_initial_share_bioenergy_in_ti_liquids_and_gases_sp():
    """
    Initial year to activate the policy of replacing fossil fuel by bioenergy for liquids and gases.
    """
    return _ext_constant_year_initial_share_bioenergy_in_ti_liquids_and_gases_sp()


_ext_constant_year_initial_share_bioenergy_in_ti_liquids_and_gases_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_INITIAL_SHARE_BIOENERGY_IN_TI_LIQUIDS_AND_GASES_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_initial_share_bioenergy_in_ti_liquids_and_gases_sp",
)
