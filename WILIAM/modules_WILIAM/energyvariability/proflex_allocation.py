"""
Module energyvariability.proflex_allocation
Translated using PySD version 3.14.0
"""

@component.add(
    name="CF PROSUP FLEXOPT",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "cf_prosup_elec2heat": 1,
        "cf_flexible_electrolysers": 1,
        "cf_v2g_storage_9r": 1,
        "cf_prosto": 1,
    },
)
def cf_prosup_flexopt():
    """
    CF of flexibility options.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG PRO I"],
    )
    value.loc[:, _subscript_dict["PROSUP P2H I"]] = (
        cf_prosup_elec2heat()
        .expand_dims({"PROSUP P2H I": _subscript_dict["PROSUP P2H I"]}, 1)
        .values
    )
    value.loc[:, ["PROSUP elec 2 hydrogen"]] = (
        cf_flexible_electrolysers()
        .expand_dims({"NRG PRO I": ["PROSUP elec 2 hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO V2G"]] = (
        cf_v2g_storage_9r().expand_dims({"NRG PRO I": ["PROSTO V2G"]}, 1).values
    )
    value.loc[:, _subscript_dict["PROSTO ELEC DEDICATED I"]] = (
        cf_prosto()
        .loc[:, _subscript_dict["PROSTO ELEC DEDICATED I"]]
        .rename({"NRG PROSTO I": "PROSTO ELEC DEDICATED I"})
        .values
    )
    value.loc[:, ["PROSUP DSM"]] = 1
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PRO FLEXOPT I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="curtailement TO elec power system",
    units="TW*h/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 4,
        "protra_max_full_load_hours": 4,
        "protra_max_full_load_hours_curtailed": 4,
    },
)
def curtailement_to_elec_power_system():
    """
    Energy curtailed by year.
    """
    return (
        protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", "PROTRA PP wind offshore"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA PP wind offshore"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA PP wind offshore"]
            .reset_coords(drop=True)
        )
        + protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", "PROTRA PP wind onshore"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA PP wind onshore"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA PP wind onshore"]
            .reset_coords(drop=True)
        )
        + protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", "PROTRA PP solar CSP"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA PP solar CSP"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA PP solar CSP"]
            .reset_coords(drop=True)
        )
        + protra_operative_capacity_stock_selected()
        .loc[:, "TO elec", "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        * (
            protra_max_full_load_hours()
            .loc[:, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            - protra_max_full_load_hours_curtailed()
            .loc[:, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="delayed PROFLEX DSM capacity",
    units="Year*TWh/h",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_proflex_dsm_capacity": 1},
    other_deps={
        "_delayfixed_delayed_proflex_dsm_capacity": {
            "initial": {},
            "step": {"proflex_dsm_capacity": 1},
        }
    },
)
def delayed_proflex_dsm_capacity():
    """
    Delayed 1 year demand-side management (DSM) capacity.
    """
    return _delayfixed_delayed_proflex_dsm_capacity()


_delayfixed_delayed_proflex_dsm_capacity = DelayFixed(
    lambda: proflex_dsm_capacity(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_delayed_proflex_dsm_capacity",
)


@component.add(
    name="INITIAL YEAR FLEX ELEC DEMAND SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_flex_elec_demand_sp"},
)
def initial_year_flex_elec_demand_sp():
    """
    Initial year of the policy scenario for flexible electricity demand
    """
    return _ext_constant_initial_year_flex_elec_demand_sp()


_ext_constant_initial_year_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "INITIAL_YEAR_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_initial_year_flex_elec_demand_sp",
)


@component.add(
    name="MINIMUM PROFLEX CAPACITY EXPANSION SP",
    units="TW/Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_minimum_proflex_capacity_expansion_sp"},
)
def minimum_proflex_capacity_expansion_sp():
    """
    Minimum potential of new expansion capacity for flexibility options
    """
    return _ext_constant_minimum_proflex_capacity_expansion_sp()


_ext_constant_minimum_proflex_capacity_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "MINIMUM_PROFLEX_CAPACITY_EXPANSION_SP",
    {},
    _root,
    {},
    "_ext_constant_minimum_proflex_capacity_expansion_sp",
)


@component.add(
    name="OBJECTIVE FLEX ELEC DEMAND SP",
    units="TWh",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_flex_elec_demand_sp"},
)
def objective_flex_elec_demand_sp():
    """
    Objective value of the policy scenario for flexible electricity demand
    """
    return _ext_constant_objective_flex_elec_demand_sp()


_ext_constant_objective_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "OBJECTIVE_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_objective_flex_elec_demand_sp",
)


@component.add(
    name="PROFLEX capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_p2h_capacity_expansion": 1,
        "flexible_electrolysers_capacity_expansion": 1,
        "ev_batteries_power_v2g_9r": 1,
        "prosto_dedicated_capacity_expansion": 1,
        "prosto_capacity_expansion_calculator": 1,
        "switch_materials_calculator": 1,
        "proflex_dsm_capacity": 1,
        "delayed_proflex_dsm_capacity": 1,
    },
)
def proflex_capacity_expansion():
    """
    Annual capacity expansion of options to manage variability. For all processes using hydrogen from electrolyzers (e.g., synthetic fuels) only the cost for producing electrolyzers is included,
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
        },
        ["REGIONS 9 I", "PRO FLEXOPT I"],
    )
    value.loc[:, _subscript_dict["PROSUP P2H I"]] = (
        prosup_p2h_capacity_expansion().values
    )
    value.loc[:, ["PROSUP elec 2 hydrogen"]] = (
        flexible_electrolysers_capacity_expansion()
        .expand_dims({"NRG PRO I": ["PROSUP elec 2 hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["PROSTO V2G"]] = (
        ev_batteries_power_v2g_9r().expand_dims({"NRG PRO I": ["PROSTO V2G"]}, 1).values
    )
    value.loc[:, _subscript_dict["PROSTO ELEC DEDICATED I"]] = if_then_else(
        switch_materials_calculator() == 0,
        lambda: prosto_dedicated_capacity_expansion(),
        lambda: prosto_capacity_expansion_calculator(),
    ).values
    value.loc[:, ["PROSUP DSM"]] = (
        np.maximum(0, proflex_dsm_capacity() - delayed_proflex_dsm_capacity())
        .expand_dims({"NRG PRO I": ["PROSUP DSM"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROFLEX DSM capacity",
    units="Year*TWh/h",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_flex_elec_demand_sp": 3,
        "initial_year_flex_elec_demand_sp": 3,
        "year_final_flex_elec_demand_sp": 3,
        "objective_flex_elec_demand_sp": 2,
        "time": 3,
        "unit_conversion_hours_year": 1,
    },
)
def proflex_dsm_capacity():
    """
    Average hourly load for demand side management. Proxy of "installed capacity" of demand side management.
    """
    return (
        if_then_else(
            switch_flex_elec_demand_sp() == 0,
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
            lambda: if_then_else(
                np.logical_and(
                    switch_flex_elec_demand_sp() == 1,
                    time() < initial_year_flex_elec_demand_sp(),
                ),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: if_then_else(
                    np.logical_and(
                        switch_flex_elec_demand_sp() == 1,
                        time() > year_final_flex_elec_demand_sp(),
                    ),
                    lambda: objective_flex_elec_demand_sp(),
                    lambda: ramp(
                        __data["time"],
                        objective_flex_elec_demand_sp()
                        / (
                            year_final_flex_elec_demand_sp()
                            - initial_year_flex_elec_demand_sp()
                        ),
                        initial_year_flex_elec_demand_sp(),
                        year_final_flex_elec_demand_sp(),
                    ),
                ),
            ),
        )
        / unit_conversion_hours_year()
    )


@component.add(
    name="PROFLEX potential capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "maximum_capacity_expansion_p2h": 1,
        "prosup_p2h_capacity_decomissioning": 1,
        "electrolytic_h2_required_to_satisfy_h2_demand": 1,
        "minimum_proflex_capacity_expansion_sp": 1,
        "flexible_electrolysers_capacity_decommissioning": 1,
        "ratio_maximum_proflex_expansion_sp": 3,
        "select_availability_unmature_energy_technologies_sp": 2,
        "flexible_electrolysers_capacity_stock": 1,
        "maximum_prosto_dedicated": 2,
        "prosto_dedicated_capacity_decomissioning": 2,
        "prosto_dedicated_capacity_stock": 2,
    },
)
def proflex_potential_capacity_expansion():
    """
    Installed capacities of flexibility options. V2G is zero because it is already endogenous. P2H is based on the final heat demand. The last equation (DSM) is zero because this is an exogenous policy assumption. In order to not duplicate, electrolysers are only assigned to PROSUP_elec_2_hydrogen.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROSUP P2H I"]] = (
        np.maximum(
            maximum_capacity_expansion_p2h() - prosup_p2h_capacity_decomissioning(), 0
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], ["PROSUP elec 2 hydrogen"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 2,
            ),
            lambda: if_then_else(
                electrolytic_h2_required_to_satisfy_h2_demand() < 0,
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
                lambda: np.maximum(
                    np.maximum(
                        flexible_electrolysers_capacity_stock()
                        * ratio_maximum_proflex_expansion_sp()
                        - flexible_electrolysers_capacity_decommissioning(),
                        minimum_proflex_capacity_expansion_sp(),
                    ),
                    0,
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROSUP elec 2 hydrogen"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROSTO V2G"]] = 0
    value.loc[:, ["TO elec"], ["PROSTO PHS"]] = (
        np.maximum(
            (
                maximum_prosto_dedicated().loc[:, "PROSTO PHS"].reset_coords(drop=True)
                - prosto_dedicated_capacity_stock()
                .loc[:, "PROSTO PHS"]
                .reset_coords(drop=True)
            )
            * ratio_maximum_proflex_expansion_sp()
            - prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO PHS"]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROSTO PHS"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROSTO STATIONARY BATTERIES"]] = (
        np.maximum(
            (
                maximum_prosto_dedicated()
                .loc[:, "PROSTO STATIONARY BATTERIES"]
                .reset_coords(drop=True)
                - prosto_dedicated_capacity_stock()
                .loc[:, "PROSTO STATIONARY BATTERIES"]
                .reset_coords(drop=True)
            )
            * ratio_maximum_proflex_expansion_sp()
            - prosto_dedicated_capacity_decomissioning()
            .loc[:, "PROSTO STATIONARY BATTERIES"]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROSTO STATIONARY BATTERIES"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROSUP DSM"]] = 0
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], _subscript_dict["PRO FLEXOPT I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROSUP CAPACITY EXPANSION ALLOCATION POLICY PWIDTH SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp"
    },
)
def prosup_capacity_expansion_allocation_policy_pwidth_sp():
    """
    Width for the allocation functions of flexibility options
    """
    return _ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp()


_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROSUP_CAPACITY_EXPANSION_ALLOCATION_POLICY_PWIDTH_SP",
    {},
    _root,
    {},
    "_ext_constant_prosup_capacity_expansion_allocation_policy_pwidth_sp",
)


@component.add(
    name="PROSUP FLEXOPT CAPACITY EXPANSION POLICY PRIORITIES SP",
    units="Dnml",
    subscripts=["REGIONS 9 I", "PRO FLEXOPT I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp"
    },
)
def prosup_flexopt_capacity_expansion_policy_priorities_sp():
    """
    Priorities to allocate new capacity requirements into the existing flexibility options
    """
    return _ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp()


_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROSUP_FLEXOPT_CAPACITY_EXPANSION_POLICY_PRIORITIES_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
    },
    "_ext_constant_prosup_flexopt_capacity_expansion_policy_priorities_sp",
)


@component.add(
    name="PROSUP FLEXOPT elec capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_flexopt_elec_curtailment_allocation": 1,
        "cf_prosup_flexopt": 1,
    },
)
def prosup_flexopt_elec_capacity_expansion():
    """
    Allocate of the capacity expansion for power flexibility options taking into account the CF as well as limits to the maximum level (either endogenous such as the FE heat demand or exogenous such as PHS potential).
    """
    return zidz(
        prosup_flexopt_elec_curtailment_allocation()
        .loc[:, "TO elec", _subscript_dict["PRO FLEXOPT I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PRO FLEXOPT I"}),
        cf_prosup_flexopt()
        .loc[:, _subscript_dict["PRO FLEXOPT I"]]
        .rename({"NRG PRO I": "PRO FLEXOPT I"}),
    )


@component.add(
    name="PROSUP FLEXOPT elec curtailment allocation",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "proflex_potential_capacity_expansion": 1,
        "prosup_flexopt_priority_vector": 1,
        "required_capacity_expansion_flexibility_options": 1,
    },
)
def prosup_flexopt_elec_curtailment_allocation():
    """
    Allocate of the capacity expansion (as it would work 100% CF) for power flexibility options
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    )
    value.loc[:, ["TO elec"], :] = (
        allocate_available(
            proflex_potential_capacity_expansion()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True),
            prosup_flexopt_priority_vector(),
            required_capacity_expansion_flexibility_options()
            .loc[:, "TO elec"]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROSUP FLEXOPT priority vector",
    subscripts=["REGIONS 9 I", "NRG PRO I", "pprofile"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "prosup_flexopt_capacity_expansion_policy_priorities_sp": 1,
        "prosup_capacity_expansion_allocation_policy_pwidth_sp": 1,
    },
)
def prosup_flexopt_priority_vector():
    """
    Vector of parameters for the allocate of capacity expansion of flexibility options
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
            "pprofile": _subscript_dict["pprofile"],
        },
        ["REGIONS 9 I", "NRG PRO I", "pprofile"],
    )
    value.loc[:, :, ["ptype"]] = 3
    value.loc[:, _subscript_dict["PRO FLEXOPT I"], ["ppriority"]] = (
        prosup_flexopt_capacity_expansion_policy_priorities_sp()
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    value.loc[:, :, ["pwidth"]] = (
        prosup_capacity_expansion_allocation_policy_pwidth_sp()
    )
    value.loc[:, :, ["pextra"]] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["PRO FLEXOPT I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="RATIO MAXIMUM PROFLEX EXPANSION SP",
    units="1/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ratio_maximum_proflex_expansion_sp"},
)
def ratio_maximum_proflex_expansion_sp():
    """
    Maximum ratio of the installed capacity of flexibility options that can be installed in the year
    """
    return _ext_constant_ratio_maximum_proflex_expansion_sp()


_ext_constant_ratio_maximum_proflex_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "RATIO_MAXIMUM_PROFLEX_EXPANSION_SP",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_ratio_maximum_proflex_expansion_sp",
)


@component.add(
    name="share curtailment TO elec",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "curtailement_to_elec_power_system": 1,
        "to_by_commodity": 1,
        "unit_conversion_twh_ej": 1,
    },
)
def share_curtailment_to_elec():
    """
    Share of curtailed electricity by region with relation to the total production.
    """
    return zidz(
        curtailement_to_elec_power_system(),
        to_by_commodity().loc[:, "TO elec"].reset_coords(drop=True)
        * unit_conversion_twh_ej(),
    )


@component.add(
    name="SWITCH FLEX ELEC DEMAND SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_flex_elec_demand_sp"},
)
def switch_flex_elec_demand_sp():
    """
    Switch of the policy for the policy of flexible electricity demand
    """
    return _ext_constant_switch_flex_elec_demand_sp()


_ext_constant_switch_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SWITCH_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_switch_flex_elec_demand_sp",
)


@component.add(
    name="YEAR FINAL FLEX ELEC DEMAND SP",
    units="Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_flex_elec_demand_sp"},
)
def year_final_flex_elec_demand_sp():
    """
    Final year of the policy scenario for flexible electricity demand
    """
    return _ext_constant_year_final_flex_elec_demand_sp()


_ext_constant_year_final_flex_elec_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "YEAR_FINAL_FLEX_ELEC_DEMAND_SP*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_year_final_flex_elec_demand_sp",
)
