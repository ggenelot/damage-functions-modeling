"""
Module energyvariability.power2heat
Translated using PySD version 3.13.4
"""

@component.add(
    name="CF PROSUP ELEC2HEAT",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_cf_prosup_elec2heat"},
)
def cf_prosup_elec2heat():
    return _ext_constant_cf_prosup_elec2heat()


_ext_constant_cf_prosup_elec2heat = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "CF_PROSUP_ELEC2HEAT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_cf_prosup_elec2heat",
)


@component.add(
    name="FE heat demand",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fe_excluding_trade": 1},
)
def fe_heat_demand():
    """
    Heat demand by region
    """
    return fe_excluding_trade().loc[:, "FE heat"].reset_coords(drop=True)


@component.add(
    name="INITIAL HEAT EFFICIENCY P2H",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_heat_efficiency_p2h"},
)
def initial_heat_efficiency_p2h():
    """
    Initial heat efficiency for P2H technologies
    """
    return _ext_constant_initial_heat_efficiency_p2h()


_ext_constant_initial_heat_efficiency_p2h = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_HEAT_EFFICIENCY_HEAT_PUMPS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_initial_heat_efficiency_p2h",
)

_ext_constant_initial_heat_efficiency_p2h.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_HEAT_EFFICIENCY_ELECTRIC_BOILERS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="INITIAL INSTALLED CAPACITY P2H",
    units="TW",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_installed_capacity_p2h"},
)
def initial_installed_capacity_p2h():
    """
    Initial installed capacity of heat pumps power-to-heat technology
    """
    return _ext_constant_initial_installed_capacity_p2h()


_ext_constant_initial_installed_capacity_p2h = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_INSTALLED_CAPACITY_HEAT_PUMPS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_initial_installed_capacity_p2h",
)

_ext_constant_initial_installed_capacity_p2h.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_INSTALLED_CAPACITY_ELECTRIC_BOILERS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="INITIAL LIFETIME P2H",
    units="Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_lifetime_p2h"},
)
def initial_lifetime_p2h():
    """
    Initial value of lifetime for P2H technologies
    """
    return _ext_constant_initial_lifetime_p2h()


_ext_constant_initial_lifetime_p2h = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_LIFETIME_HEAT_PUMPS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_initial_lifetime_p2h",
)

_ext_constant_initial_lifetime_p2h.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_LIFETIME_ELECTRIC_BOILERS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="INITIAL YEAR P2H EXPANSION SP",
    units="Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_p2h_expansion_sp"},
)
def initial_year_p2h_expansion_sp():
    """
    Initial year of the policy scenario for power-to-heat technologies
    """
    return _ext_constant_initial_year_p2h_expansion_sp()


_ext_constant_initial_year_p2h_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_INITIAL_HEAT_PUMPS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_initial_year_p2h_expansion_sp",
)

_ext_constant_initial_year_p2h_expansion_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_INITIAL_ELECTRIC_BOILERS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="maximum capacity expansion P2H",
    units="TW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_by_commodity": 1,
        "unit_conversion_twh_ej": 1,
        "cf_prosup_elec2heat": 1,
        "unit_conversion_hours_year": 1,
    },
)
def maximum_capacity_expansion_p2h():
    """
    Signal to follow the heat demand. Ratio between the installed capacity of P2H and the averaage hourly load of heat demand
    """
    return (
        to_by_commodity().loc[:, "TO heat"].reset_coords(drop=True)
        * unit_conversion_twh_ej()
        / (cf_prosup_elec2heat() * unit_conversion_hours_year())
    )


@component.add(
    name="OBJECTIVE CAPACITY P2H SP",
    units="TW",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_capacity_p2h_sp"},
)
def objective_capacity_p2h_sp():
    """
    Final installed capacity of the policy scenario for power-to-heat technologies
    """
    return _ext_constant_objective_capacity_p2h_sp()


_ext_constant_objective_capacity_p2h_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_HEAT_PUMPS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_objective_capacity_p2h_sp",
)

_ext_constant_objective_capacity_p2h_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_ELECTRIC_BOILERS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="PROSUP P2H capacity decomissioning",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_p2h_capacity_stock": 1, "initial_lifetime_p2h": 1},
)
def prosup_p2h_capacity_decomissioning():
    """
    Power-to-heat transformation capacities that are being decomissioned each year (depends solely on the lifetime/depreciation periode of the power plant)
    """
    return prosup_p2h_capacity_stock() / initial_lifetime_p2h()


@component.add(
    name="PROSUP P2H capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_nrg_proflex_capacity_expansion_endogenous": 1,
        "time": 1,
        "year_final_p2h_expansion_sp": 2,
        "initial_year_p2h_expansion_sp": 2,
        "one_year": 1,
        "objective_capacity_p2h_sp": 1,
        "prosup_flexopt_elec_capacity_expansion": 1,
        "remaining_potential_capacity_p2h": 1,
        "prosup_p2h_capacity_decomissioning": 1,
    },
)
def prosup_p2h_capacity_expansion():
    """
    New power-to-heat capacity added to the energy transformation system
    """
    return (
        if_then_else(
            switch_nrg_proflex_capacity_expansion_endogenous() == 0,
            lambda: ramp(
                __data["time"],
                objective_capacity_p2h_sp()
                / (year_final_p2h_expansion_sp() - initial_year_p2h_expansion_sp()),
                initial_year_p2h_expansion_sp(),
                year_final_p2h_expansion_sp(),
            )
            / one_year(),
            lambda: prosup_flexopt_elec_capacity_expansion()
            .loc[:, _subscript_dict["PROSUP P2H I"]]
            .rename({"PRO FLEXOPT I": "PROSUP P2H I"}),
        )
        * np.maximum(0, remaining_potential_capacity_p2h())
        + prosup_p2h_capacity_decomissioning()
    )


@component.add(
    name="PROSUP P2H capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_prosup_p2h_capacity_stock": 1},
    other_deps={
        "_integ_prosup_p2h_capacity_stock": {
            "initial": {"initial_installed_capacity_p2h": 1},
            "step": {
                "prosup_p2h_capacity_expansion": 1,
                "prosup_p2h_capacity_decomissioning": 1,
            },
        }
    },
)
def prosup_p2h_capacity_stock():
    """
    Capacity stock of power-to-heat transformation technology capacities (PROSUP)
    """
    return _integ_prosup_p2h_capacity_stock()


_integ_prosup_p2h_capacity_stock = Integ(
    lambda: prosup_p2h_capacity_expansion() - prosup_p2h_capacity_decomissioning(),
    lambda: initial_installed_capacity_p2h(),
    "_integ_prosup_p2h_capacity_stock",
)


@component.add(
    name="PROSUP P2H thermal efficiency",
    units="DMNL",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_prosup_p2h_thermal_efficiency"},
)
def prosup_p2h_thermal_efficiency():
    """
    Thermal efficiencies of power-to-heat technologies (COP)
    """
    return _ext_constant_prosup_p2h_thermal_efficiency()


_ext_constant_prosup_p2h_thermal_efficiency = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_HEAT_EFFICIENCY_HEAT_PUMPS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_prosup_p2h_thermal_efficiency",
)

_ext_constant_prosup_p2h_thermal_efficiency.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "INITIAL_HEAT_EFFICIENCY_ELECTRIC_BOILERS*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)


@component.add(
    name="PROSUP TO P2H technologies",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I", "NRG TO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "prosup_p2h_capacity_stock": 4,
        "cf_prosup_elec2heat": 4,
        "unit_conversion_hours_year": 4,
        "unit_conversion_twh_ej": 4,
        "prosup_p2h_thermal_efficiency": 2,
    },
)
def prosup_to_p2h_technologies():
    """
    Electricity (consumption) and heat (generation) of power-to-heat technologies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS 9 I", "PROSUP P2H I", "NRG TO I"],
    )
    value.loc[:, ["PROSUP P2H heat pump"], ["TO elec"]] = (
        (
            prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H heat pump"]
            .reset_coords(drop=True)
            * cf_prosup_elec2heat()
            * unit_conversion_hours_year()
            / unit_conversion_twh_ej()
        )
        .expand_dims({"NRG PRO I": ["PROSUP P2H heat pump"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 2)
        .values
    )
    value.loc[:, ["PROSUP P2H heat pump"], ["TO heat"]] = (
        (
            prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H heat pump"]
            .reset_coords(drop=True)
            * cf_prosup_elec2heat()
            * unit_conversion_hours_year()
            * prosup_p2h_thermal_efficiency()
            .loc[:, "PROSUP P2H heat pump"]
            .reset_coords(drop=True)
            / unit_conversion_twh_ej()
        )
        .expand_dims({"NRG PRO I": ["PROSUP P2H heat pump"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 2)
        .values
    )
    value.loc[:, ["PROSUP P2H electric boiler"], ["TO elec"]] = (
        (
            prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H electric boiler"]
            .reset_coords(drop=True)
            * cf_prosup_elec2heat()
            * unit_conversion_hours_year()
            / unit_conversion_twh_ej()
        )
        .expand_dims({"NRG PRO I": ["PROSUP P2H electric boiler"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 2)
        .values
    )
    value.loc[:, ["PROSUP P2H electric boiler"], ["TO heat"]] = (
        (
            prosup_p2h_capacity_stock()
            .loc[:, "PROSUP P2H electric boiler"]
            .reset_coords(drop=True)
            * cf_prosup_elec2heat()
            * unit_conversion_hours_year()
            * prosup_p2h_thermal_efficiency()
            .loc[:, "PROSUP P2H electric boiler"]
            .reset_coords(drop=True)
            / unit_conversion_twh_ej()
        )
        .expand_dims({"NRG PRO I": ["PROSUP P2H electric boiler"]}, 1)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 2)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROSUP P2H heat pump"], ["TO elec"]] = False
    except_subs.loc[:, ["PROSUP P2H heat pump"], ["TO heat"]] = False
    except_subs.loc[:, ["PROSUP P2H electric boiler"], ["TO elec"]] = False
    except_subs.loc[:, ["PROSUP P2H electric boiler"], ["TO heat"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="RATIO CAPACITY STORAGE P2H",
    units="GWh/TW",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ratio_capacity_storage_p2h"},
)
def ratio_capacity_storage_p2h():
    """
    Ratio of thermal storage capacity per installed capacity of power-to-heat technology. The value is the result of calculations on heat generation and average demand (cases for EU, Bulgaria and rest of the regions). It was envisioned to provide necessary storage for at least 24 h operation with no additional heat generation. Heat demand is much bigger now since all the heat demand is district heating demand so I would advise increasing the values for both the heat pumps and storage capacities.
    """
    return _ext_constant_ratio_capacity_storage_p2h()


_ext_constant_ratio_capacity_storage_p2h = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "RATIO_CAPACITY_STORAGE_P2H",
    {},
    _root,
    {},
    "_ext_constant_ratio_capacity_storage_p2h",
)


@component.add(
    name="remaining potential capacity P2H",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"maximum_capacity_expansion_p2h": 2, "prosup_p2h_capacity_stock": 1},
)
def remaining_potential_capacity_p2h():
    """
    Remaining potential taking into account FE heat demand.
    """
    return zidz(
        maximum_capacity_expansion_p2h()
        - sum(
            prosup_p2h_capacity_stock().rename({"PROSUP P2H I": "PROSUP P2H I!"}),
            dim=["PROSUP P2H I!"],
        ),
        maximum_capacity_expansion_p2h(),
    )


@component.add(
    name="SWITCH NRG PROFLEX CF ENDOGENOUS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_proflex_cf_endogenous"},
)
def switch_nrg_proflex_cf_endogenous():
    """
    0: exogenous CF for PROFLEX based on inputs from scenario_parameters.xlsx 1: endogneous CF based on regressions
    """
    return _ext_constant_switch_nrg_proflex_cf_endogenous()


_ext_constant_switch_nrg_proflex_cf_endogenous = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_PROFLEX_CF_ENDOGENOUS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_proflex_cf_endogenous",
)


@component.add(
    name="thermal storage",
    units="GWh",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"prosup_p2h_capacity_stock": 1, "ratio_capacity_storage_p2h": 1},
)
def thermal_storage():
    """
    Thermal storage capacity in gigawatts-hour (GWh) of power-to-heat technology
    """
    return prosup_p2h_capacity_stock() * ratio_capacity_storage_p2h()


@component.add(
    name="YEAR FINAL P2H EXPANSION SP",
    units="Year",
    subscripts=["REGIONS 9 I", "PROSUP P2H I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_p2h_expansion_sp"},
)
def year_final_p2h_expansion_sp():
    """
    Final year of the policy scenario for power-to-heat technologies
    """
    return _ext_constant_year_final_p2h_expansion_sp()


_ext_constant_year_final_p2h_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_HEAT_PUMPS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H heat pump"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": _subscript_dict["PROSUP P2H I"],
    },
    "_ext_constant_year_final_p2h_expansion_sp",
)

_ext_constant_year_final_p2h_expansion_sp.add(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_ELECTRIC_BOILERS_EXPANSION_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PROSUP P2H I": ["PROSUP P2H electric boiler"],
    },
)
