"""
Module climateother_ghg_cycles
Translated using PySD version 3.14.0
"""

@component.add(
    name="CH4 atm conc",
    units="ppb",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_in_atm": 1, "ppb_ch4_per_mton_ch4": 1},
)
def ch4_atm_conc():
    """
    CH4 in atmosphere concentration.
    """
    return ch4_in_atm() * ppb_ch4_per_mton_ch4()


@component.add(
    name="CH4 emissions from permafrost and clathrate",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sensitivity_of_methane_emissions_to_permafrost_and_clathrate": 1,
        "reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature": 1,
        "temperature_change": 1,
        "temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate": 1,
    },
)
def ch4_emissions_from_permafrost_and_clathrate():
    """
    Methane emissions from melting permafrost and clathrate outgassing are assumed to be nonlinear. Emissions are assumed to be zero if warming over preindustrial levels is less than a threshold and linear in temperature above the threshold. The default sensitivity is zero, but the strength of the effect and threshold can be set by the user.
    """
    return (
        sensitivity_of_methane_emissions_to_permafrost_and_clathrate()
        * reference_sensitivity_of_ch4_from_permafrost_and_clathrate_to_temperature()
        * np.maximum(
            0,
            temperature_change()
            - temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate(),
        )
    )


@component.add(
    name="CH4 fractional uptake",
    units="1/Years",
    limits=(5.0, 15.0),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "reference_ch4_time_constant": 1,
        "stratospheric_ch4_path_share": 2,
        "preindustrial_ch4": 1,
        "tropospheric_ch4_path_share": 2,
        "ch4_in_atm": 1,
    },
)
def ch4_fractional_uptake():
    """
    dCH4/dt = E – k1*CH4*OH – k2*CH4 E = emissions. The k1 path is dominant (k2 reflects soil processes and other minor sinks) dOH/dt = F – k3*CH4*OH – k4*OH F = formation. In this case the methane reaction is the minor path (15-20% of loss) so OH in equilibrium is OHeq = F/(k3*CH4+k4) substituting dCH4/dt = E – k1*CH4* F/(k3*CH4+k4) – k2*CH4 thus the total fractional uptake is k1*F/(k3*CH4+k4)+k2 which is robust at W Formulated from Meinshausen et al., 2011
    """
    return (
        1
        / reference_ch4_time_constant()
        * (
            tropospheric_ch4_path_share()
            / (
                stratospheric_ch4_path_share() * (ch4_in_atm() / preindustrial_ch4())
                + 1
                - stratospheric_ch4_path_share()
            )
            + (1 - tropospheric_ch4_path_share())
        )
    )


@component.add(
    name="CH4 in atm",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_ch4_in_atm": 1},
    other_deps={
        "_integ_ch4_in_atm": {
            "initial": {"initial_ch4": 1},
            "step": {
                "ch4_emissions_from_permafrost_and_clathrate": 1,
                "global_anthropogenic_ch4_emissions": 1,
                "natural_ch4_emissions": 1,
                "ch4_uptake": 1,
            },
        }
    },
)
def ch4_in_atm():
    """
    CH4 in atmosphere.
    """
    return _integ_ch4_in_atm()


_integ_ch4_in_atm = Integ(
    lambda: ch4_emissions_from_permafrost_and_clathrate()
    + global_anthropogenic_ch4_emissions()
    + natural_ch4_emissions()
    - ch4_uptake(),
    lambda: initial_ch4(),
    "_integ_ch4_in_atm",
)


@component.add(
    name="CH4 uptake",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_in_atm": 1, "ch4_fractional_uptake": 1},
)
def ch4_uptake():
    """
    CH4 removed from the atmosphere, considering the time constant (time that the gas takes to be removed from the atmosphere)
    """
    return ch4_in_atm() * ch4_fractional_uptake()


@component.add(
    name="EXO CH4 EMISSIONS AGRICULTURE",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_exo_ch4_emissions_agriculture",
        "__data__": "_ext_data_exo_ch4_emissions_agriculture",
        "time": 1,
    },
)
def exo_ch4_emissions_agriculture():
    """
    exogenous information from simulation ojo: (still with zeros!)=
    """
    return _ext_data_exo_ch4_emissions_agriculture(time())


_ext_data_exo_ch4_emissions_agriculture = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_EXO_SIMULATION",
    "EXO_CH4_EMISSIONS_AGRICULTURE",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_data_exo_ch4_emissions_agriculture",
)


@component.add(
    name="EXO N2O EMISSIONS AGRICULTURE",
    units="Mt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_exo_n2o_emissions_agriculture",
        "__data__": "_ext_data_exo_n2o_emissions_agriculture",
        "time": 1,
    },
)
def exo_n2o_emissions_agriculture():
    """
    exogenous information from simulation
    """
    return _ext_data_exo_n2o_emissions_agriculture(time())


_ext_data_exo_n2o_emissions_agriculture = ExtData(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_EXO_SIMULATION",
    "EXO_N2O_EMISSIONS_AGRICULTURE",
    None,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_data_exo_n2o_emissions_agriculture",
)


@component.add(
    name="EXO TOTAL CH4 ENERGY EMISSIONS 9R",
    units="Gt/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_total_ch4_energy_emissions_9r",
        "__lookup__": "_ext_lookup_exo_total_ch4_energy_emissions_9r",
    },
)
def exo_total_ch4_energy_emissions_9r(x, final_subs=None):
    """
    exogenous information from simulation
    """
    return _ext_lookup_exo_total_ch4_energy_emissions_9r(x, final_subs)


_ext_lookup_exo_total_ch4_energy_emissions_9r = ExtLookup(
    "model_parameters/climate/climate.xlsx",
    "World",
    "TIME_EXO_SIMULATION",
    "EXO_TOTAL_CH4_ENERGY_AND_IPPUS_EMISSIONS_9R",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_total_ch4_energy_emissions_9r",
)


@component.add(
    name="flux C from permafrost release",
    units="Gt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "sensitivity_of_methane_emissions_to_permafrost_and_clathrate": 1,
        "reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature": 1,
        "temperature_change": 1,
        "temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate": 1,
    },
)
def flux_c_from_permafrost_release():
    """
    Flux C release from permafrost to atmosphere.
    """
    return (
        sensitivity_of_methane_emissions_to_permafrost_and_clathrate()
        * reference_sensitivity_of_c_from_permafrost_and_clathrate_to_temperature()
        * np.maximum(
            0,
            temperature_change()
            - temperature_threshold_for_methane_emissions_from_permafrost_and_clathrate(),
        )
    )


@component.add(
    name="global anthropogenic CH4 emissions",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_anthro_emissions": 1},
)
def global_anthropogenic_ch4_emissions():
    """
    Global emissions of CH4 due to human activities
    """
    return sum(
        ch4_anthro_emissions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="global CH4 emissions",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"global_anthropogenic_ch4_emissions": 1, "natural_ch4_emissions": 1},
)
def global_ch4_emissions():
    """
    Global CH4 emission from anthropogenic and natural sources.
    """
    return global_anthropogenic_ch4_emissions() + natural_ch4_emissions()


@component.add(
    name="global HFC emissions",
    units="t/Year",
    subscripts=["HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hfc_emissions": 9},
)
def global_hfc_emissions():
    """
    HFC global emissions
    """
    value = xr.DataArray(
        np.nan, {"HFC TYPE I": _subscript_dict["HFC TYPE I"]}, ["HFC TYPE I"]
    )
    value.loc[["HFC134a"]] = sum(
        hfc_emissions()
        .loc[:, "HFC134a"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC23"]] = sum(
        hfc_emissions()
        .loc[:, "HFC23"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC32"]] = sum(
        hfc_emissions()
        .loc[:, "HFC32"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC125"]] = sum(
        hfc_emissions()
        .loc[:, "HFC125"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC143a"]] = sum(
        hfc_emissions()
        .loc[:, "HFC143a"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC152a"]] = sum(
        hfc_emissions()
        .loc[:, "HFC152a"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC227ea"]] = sum(
        hfc_emissions()
        .loc[:, "HFC227ea"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC245ca"]] = sum(
        hfc_emissions()
        .loc[:, "HFC245ca"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["HFC4310mee"]] = sum(
        hfc_emissions()
        .loc[:, "HFC4310mee"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    return value


@component.add(
    name="global N2O emissions",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_anthro_emissions": 1, "natural_n2o_emissions": 1},
)
def global_n2o_emissions():
    """
    Global N2O emissions.
    """
    return (
        sum(
            n2o_anthro_emissions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        + natural_n2o_emissions()
    )


@component.add(
    name="global SF6 emissions",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sf6_emissions": 1},
)
def global_sf6_emissions():
    """
    SF6 global emissions
    """
    return sum(
        sf6_emissions().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="global total PFC emissions",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pfc_emissions": 1, "natural_pfc_emissions": 1},
)
def global_total_pfc_emissions():
    """
    Global total PFC emissions
    """
    return (
        sum(
            pfc_emissions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        + natural_pfc_emissions()
    )


@component.add(
    name="HFC atm conc",
    units="ppt",
    subscripts=["HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hfc_in_atm": 1, "ppt_hfc_per_tons_hfc": 1},
)
def hfc_atm_conc():
    """
    HFC in atmosphere concentration.
    """
    return hfc_in_atm() * ppt_hfc_per_tons_hfc()


@component.add(
    name="HFC in atm",
    units="t",
    limits=(2.5924e-43, np.nan),
    subscripts=["HFC TYPE I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_hfc_in_atm": 1},
    other_deps={
        "_integ_hfc_in_atm": {
            "initial": {"initial_hfc": 1},
            "step": {"global_hfc_emissions": 1, "hfc_uptake": 1},
        }
    },
)
def hfc_in_atm():
    """
    HFC in atmosphere.
    """
    return _integ_hfc_in_atm()


_integ_hfc_in_atm = Integ(
    lambda: global_hfc_emissions() - hfc_uptake(),
    lambda: initial_hfc(),
    "_integ_hfc_in_atm",
)


@component.add(
    name="HFC uptake",
    units="t/Year",
    subscripts=["HFC TYPE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hfc_in_atm": 1, "time_const_for_hfc": 1},
)
def hfc_uptake():
    """
    HFC removed from the atmosphere, considering the time constant (time that the gas takes to be removed from the atmosphere)
    """
    return hfc_in_atm() / time_const_for_hfc()


@component.add(
    name="INIT PFC IN ATM",
    units="t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"init_pfc_in_atm_con": 1, "ppt_pfc_per_tons_pfc": 1},
)
def init_pfc_in_atm():
    """
    Initial PFC in atmosphere.
    """
    return init_pfc_in_atm_con() / ppt_pfc_per_tons_pfc()


@component.add(
    name="INITIAL CH4",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_ch4": 1},
    other_deps={
        "_initial_initial_ch4": {
            "initial": {"initial_ch4_conc": 1, "ppb_ch4_per_mton_ch4": 1},
            "step": {},
        }
    },
)
def initial_ch4():
    """
    Initial CH4.
    """
    return _initial_initial_ch4()


_initial_initial_ch4 = Initial(
    lambda: initial_ch4_conc() / ppb_ch4_per_mton_ch4(), "_initial_initial_ch4"
)


@component.add(
    name="INITIAL HFC",
    units="t",
    subscripts=["HFC TYPE I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_hfc": 1},
    other_deps={
        "_initial_initial_hfc": {
            "initial": {"inital_hfc_con": 1, "ppt_hfc_per_tons_hfc": 1},
            "step": {},
        }
    },
)
def initial_hfc():
    """
    Initial HFC.
    """
    return _initial_initial_hfc()


_initial_initial_hfc = Initial(
    lambda: inital_hfc_con() / ppt_hfc_per_tons_hfc(), "_initial_initial_hfc"
)


@component.add(
    name="INITIAL N2O",
    units="Mt",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_n2o": 1},
    other_deps={
        "_initial_initial_n2o": {
            "initial": {"initial_n2o_conc": 1, "ppb_n2o_per_mtonn": 1},
            "step": {},
        }
    },
)
def initial_n2o():
    """
    Initial N2O.
    """
    return _initial_initial_n2o()


_initial_initial_n2o = Initial(
    lambda: initial_n2o_conc() / ppb_n2o_per_mtonn(), "_initial_initial_n2o"
)


@component.add(
    name="INITIAL SF6",
    units="t",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_sf6_con": 1, "ppt_sf6_per_tons_sf6": 1},
)
def initial_sf6():
    """
    Initial SF6.
    """
    return initial_sf6_con() / ppt_sf6_per_tons_sf6()


@component.add(
    name="N2O atm conc",
    units="ppb",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_in_atm": 1, "ppb_n2o_per_mtonn": 1},
)
def n2o_atm_conc():
    """
    N2O in atmosphere concentration.
    """
    return n2o_in_atm() * ppb_n2o_per_mtonn()


@component.add(
    name="N2O in atm",
    units="Mt",
    limits=(3.01279e-43, np.nan),
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_n2o_in_atm": 1},
    other_deps={
        "_integ_n2o_in_atm": {
            "initial": {"initial_n2o": 1},
            "step": {"global_n2o_emissions": 1, "n2o_uptake": 1},
        }
    },
)
def n2o_in_atm():
    """
    N2O in atmosphere.
    """
    return _integ_n2o_in_atm()


_integ_n2o_in_atm = Integ(
    lambda: global_n2o_emissions() - n2o_uptake(),
    lambda: initial_n2o(),
    "_integ_n2o_in_atm",
)


@component.add(
    name="N2O uptake",
    units="Mt/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"n2o_in_atm": 1, "time_const_for_n2o": 1},
)
def n2o_uptake():
    """
    N2O removed from the atmosphere, considering the time constant (time that the gas takes to be removed from the atmosphere)
    """
    return n2o_in_atm() / time_const_for_n2o()


@component.add(
    name="NATURAL PFC EMISSIONS",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"preindustrial_pfc": 1, "time_const_for_pfc": 1},
)
def natural_pfc_emissions():
    """
    Natural PFC emissions.
    """
    return preindustrial_pfc() / time_const_for_pfc()


@component.add(
    name="PFC atm conc",
    units="ppt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pfc_in_atm": 1, "ppt_pfc_per_tons_pfc": 1},
)
def pfc_atm_conc():
    """
    PFC in atmosphere concentration.
    """
    return pfc_in_atm() * ppt_pfc_per_tons_pfc()


@component.add(
    name="PFC in atm",
    units="t",
    limits=(3.01279e-43, np.nan),
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_pfc_in_atm": 1},
    other_deps={
        "_integ_pfc_in_atm": {
            "initial": {"init_pfc_in_atm": 1},
            "step": {"global_total_pfc_emissions": 1, "pfc_uptake": 1},
        }
    },
)
def pfc_in_atm():
    """
    PFC in atmosphere.
    """
    return _integ_pfc_in_atm()


_integ_pfc_in_atm = Integ(
    lambda: global_total_pfc_emissions() - pfc_uptake(),
    lambda: init_pfc_in_atm(),
    "_integ_pfc_in_atm",
)


@component.add(
    name="PFC uptake",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pfc_in_atm": 1, "time_const_for_pfc": 1},
)
def pfc_uptake():
    """
    PFC removed from the atmosphere, considering the time constant (time that the gas takes to be removed from the atmosphere)
    """
    return pfc_in_atm() / time_const_for_pfc()


@component.add(
    name="PPB CH4 PER MTON CH4",
    units="ppb/Mt",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_ppb_ch4_per_mton_ch4": 1},
    other_deps={
        "_initial_ppb_ch4_per_mton_ch4": {
            "initial": {
                "unit_conversion_ppt_mol": 1,
                "ch4_molar_mass": 1,
                "unit_conversion_g_mt": 1,
                "unit_conversion_ppt_ppb": 1,
            },
            "step": {},
        }
    },
)
def ppb_ch4_per_mton_ch4():
    """
    Ppb CH4 per Mtons CH4.
    """
    return _initial_ppb_ch4_per_mton_ch4()


_initial_ppb_ch4_per_mton_ch4 = Initial(
    lambda: unit_conversion_ppt_mol()
    / ch4_molar_mass()
    * unit_conversion_g_mt()
    / unit_conversion_ppt_ppb(),
    "_initial_ppb_ch4_per_mton_ch4",
)


@component.add(
    name="PPB N2O PER MTONN",
    units="ppb/Mt",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_ppb_n2o_per_mtonn": 1},
    other_deps={
        "_initial_ppb_n2o_per_mtonn": {
            "initial": {
                "unit_conversion_ppt_mol": 1,
                "n2o_n_molar_mass": 1,
                "unit_conversion_g_mt": 1,
                "unit_conversion_ppt_ppb": 1,
            },
            "step": {},
        }
    },
)
def ppb_n2o_per_mtonn():
    """
    Ppb N2O per Mtons Nitrogen.
    """
    return _initial_ppb_n2o_per_mtonn()


_initial_ppb_n2o_per_mtonn = Initial(
    lambda: unit_conversion_ppt_mol()
    / n2o_n_molar_mass()
    * unit_conversion_g_mt()
    / unit_conversion_ppt_ppb(),
    "_initial_ppb_n2o_per_mtonn",
)


@component.add(
    name="PPT HFC PER TONS HFC",
    units="ppt/t",
    subscripts=["HFC TYPE I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_ppt_hfc_per_tons_hfc": 1},
    other_deps={
        "_initial_ppt_hfc_per_tons_hfc": {
            "initial": {
                "unit_conversion_ppt_mol": 1,
                "hfc_molar_mass": 1,
                "unit_conversion_g_t": 1,
            },
            "step": {},
        }
    },
)
def ppt_hfc_per_tons_hfc():
    """
    Ppt HFC per tons HFC.
    """
    return _initial_ppt_hfc_per_tons_hfc()


_initial_ppt_hfc_per_tons_hfc = Initial(
    lambda: unit_conversion_ppt_mol() / hfc_molar_mass() * unit_conversion_g_t(),
    "_initial_ppt_hfc_per_tons_hfc",
)


@component.add(
    name="PPT PFC PER TONS PFC",
    units="ppt/t",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_ppt_pfc_per_tons_pfc": 1},
    other_deps={
        "_initial_ppt_pfc_per_tons_pfc": {
            "initial": {
                "unit_conversion_ppt_mol": 1,
                "cf4_molar_mass": 1,
                "unit_conversion_g_t": 1,
            },
            "step": {},
        }
    },
)
def ppt_pfc_per_tons_pfc():
    """
    based on CF4
    """
    return _initial_ppt_pfc_per_tons_pfc()


_initial_ppt_pfc_per_tons_pfc = Initial(
    lambda: unit_conversion_ppt_mol() / cf4_molar_mass() * unit_conversion_g_t(),
    "_initial_ppt_pfc_per_tons_pfc",
)


@component.add(
    name="PPT SF6 PER TONS SF6",
    units="ppt/tonsSF6",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_ppt_sf6_per_tons_sf6": 1},
    other_deps={
        "_initial_ppt_sf6_per_tons_sf6": {
            "initial": {
                "unit_conversion_ppt_mol": 1,
                "sf6_molar_mass": 1,
                "unit_conversion_g_t": 1,
            },
            "step": {},
        }
    },
)
def ppt_sf6_per_tons_sf6():
    """
    Ppt SF6 per tons SF6.
    """
    return _initial_ppt_sf6_per_tons_sf6()


_initial_ppt_sf6_per_tons_sf6 = Initial(
    lambda: unit_conversion_ppt_mol() / sf6_molar_mass() * unit_conversion_g_t(),
    "_initial_ppt_sf6_per_tons_sf6",
)


@component.add(
    name="PREINDUSTRIAL PFC",
    units="t",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_preindustrial_pfc": 1},
    other_deps={
        "_initial_preindustrial_pfc": {
            "initial": {"preindustrial_pfc_conc": 1, "ppt_pfc_per_tons_pfc": 1},
            "step": {},
        }
    },
)
def preindustrial_pfc():
    """
    Preindustrial PFC in atmosphere.
    """
    return _initial_preindustrial_pfc()


_initial_preindustrial_pfc = Initial(
    lambda: preindustrial_pfc_conc() / ppt_pfc_per_tons_pfc(),
    "_initial_preindustrial_pfc",
)


@component.add(
    name="SF6 atm conc",
    units="ppt",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sf6_in_atm": 1, "ppt_sf6_per_tons_sf6": 1},
)
def sf6_atm_conc():
    """
    SF6 in atmosphere concentration.
    """
    return sf6_in_atm() * ppt_sf6_per_tons_sf6()


@component.add(
    name="SF6 in atm",
    units="t",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_sf6_in_atm": 1},
    other_deps={
        "_integ_sf6_in_atm": {
            "initial": {"initial_sf6": 1},
            "step": {"global_sf6_emissions": 1, "sf6_uptake": 1},
        }
    },
)
def sf6_in_atm():
    """
    SF6 in atmosphere.
    """
    return _integ_sf6_in_atm()


_integ_sf6_in_atm = Integ(
    lambda: global_sf6_emissions() - sf6_uptake(),
    lambda: initial_sf6(),
    "_integ_sf6_in_atm",
)


@component.add(
    name="SF6 uptake",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"sf6_in_atm": 1, "time_const_for_sf6": 1},
)
def sf6_uptake():
    """
    SF6 removed from the atmosphere, considering the time constant (time that the gas takes to be removed from the atmosphere)
    """
    return sf6_in_atm() / time_const_for_sf6()


@component.add(
    name="time const for CH4",
    units="Years",
    limits=(5.0, 15.0),
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"ch4_fractional_uptake": 1},
)
def time_const_for_ch4():
    """
    Time constant for CH4
    """
    return 1 / ch4_fractional_uptake()


@component.add(
    name="total C from permafrost",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_total_c_from_permafrost": 1},
    other_deps={
        "_integ_total_c_from_permafrost": {
            "initial": {},
            "step": {
                "flux_c_from_permafrost_release": 1,
                "unit_conversion_mt_gt": 1,
                "ch4_emissions_from_permafrost_and_clathrate": 1,
                "unit_conversion_ch4_c": 1,
            },
        }
    },
)
def total_c_from_permafrost():
    """
    In terms of total C mass (of both CO2 and CH4) released from permafrost melting, experts estimated that 15-33 Pg C (n=27) could be released by 2040, reaching 120-195 Pg C by 2100, and 276-414 Pg C by 2300 under the high warming scenario (Fig. 1c). 1 PgC = 1GtonC.
    """
    return _integ_total_c_from_permafrost()


_integ_total_c_from_permafrost = Integ(
    lambda: flux_c_from_permafrost_release()
    + ch4_emissions_from_permafrost_and_clathrate()
    / unit_conversion_ch4_c()
    / unit_conversion_mt_gt(),
    lambda: 0,
    "_integ_total_c_from_permafrost",
)


@component.add(
    name="total CH4 released",
    units="Gt",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_total_ch4_released": 1},
    other_deps={
        "_integ_total_ch4_released": {
            "initial": {},
            "step": {
                "ch4_emissions_from_permafrost_and_clathrate": 1,
                "unit_conversion_ch4_c": 1,
                "unit_conversion_mt_gt": 1,
            },
        }
    },
)
def total_ch4_released():
    """
    Of C emissions released from melting of permafrost, only about 2.3 % was expected to be in the form of CH4, corresponding to W.26-0.85 Pg CH4-C by 2040, 2.03-6.21 Pg CH4-C by 2100 and 4.61-14.24 Pg CH4-C by 2300 (Fig. 1d).
    """
    return _integ_total_ch4_released()


_integ_total_ch4_released = Integ(
    lambda: ch4_emissions_from_permafrost_and_clathrate()
    / unit_conversion_ch4_c()
    / unit_conversion_mt_gt(),
    lambda: 0,
    "_integ_total_ch4_released",
)
