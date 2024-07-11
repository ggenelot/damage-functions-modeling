"""
Module energycapacities.protra
Translated using PySD version 3.14.0
"""

@component.add(
    name="applied TO reserve factor by commodity",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"exogenous_to_reserve_factor": 1},
)
def applied_to_reserve_factor_by_commodity():
    """
    Reserve factor accounting for excess-capacities that need to be installed in order to ensure sufficient transformation capacities. Only Elec and Heat used.
    """
    return exogenous_to_reserve_factor()


@component.add(
    name="capacity stock PROTRA PP solar PV by subtechnology",
    units="TW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1": 1,
    },
    other_deps={
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology": {
            "initial": {
                "initial_protra_capacity_stock": 1,
                "share_pv_subtechnologies_before_2020": 1,
            },
            "step": {
                "protra_pp_solar_pv_by_subtechnology_capacity_expansion": 1,
                "protra_pp_solar_pv_by_subtechnology_capacity_decomissioning": 1,
            },
        },
        "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1": {
            "initial": {
                "initial_protra_capacity_stock": 1,
                "share_pv_subtechnologies_before_2020": 1,
            },
            "step": {
                "protra_pp_solar_pv_by_subtechnology_capacity_expansion": 1,
                "protra_pp_solar_pv_by_subtechnology_capacity_decomissioning": 1,
            },
        },
    },
)
def capacity_stock_protra_pp_solar_pv_by_subtechnology():
    """
    solar PV capacity installed by panel subtechnology
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[:, ["PROTRA PP solar open space PV"], :] = (
        _integ_capacity_stock_protra_pp_solar_pv_by_subtechnology().values
    )
    value.loc[:, ["PROTRA PP solar urban PV"], :] = (
        _integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1().values
    )
    return value


_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology = Integ(
    lambda: (
        protra_pp_solar_pv_by_subtechnology_capacity_expansion()
        .loc[:, "PROTRA PP solar open space PV", :]
        .reset_coords(drop=True)
        - protra_pp_solar_pv_by_subtechnology_capacity_decomissioning()
        .loc[:, "PROTRA PP solar open space PV", :]
        .reset_coords(drop=True)
    ).expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1),
    lambda: (
        initial_protra_capacity_stock()
        .loc[_subscript_dict["REGIONS 9 I"], "TO elec", "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * share_pv_subtechnologies_before_2020()
    ).expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1),
    "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology",
)

_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1 = Integ(
    lambda: (
        protra_pp_solar_pv_by_subtechnology_capacity_expansion()
        .loc[:, "PROTRA PP solar urban PV", :]
        .reset_coords(drop=True)
        - protra_pp_solar_pv_by_subtechnology_capacity_decomissioning()
        .loc[:, "PROTRA PP solar urban PV", :]
        .reset_coords(drop=True)
    ).expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1),
    lambda: (
        initial_protra_capacity_stock()
        .loc[_subscript_dict["REGIONS 9 I"], "TO elec", "PROTRA PP solar urban PV"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * share_pv_subtechnologies_before_2020()
    ).expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1),
    "_integ_capacity_stock_protra_pp_solar_pv_by_subtechnology_1",
)


@component.add(
    name="CF LOSS SHARE STOPPING PROTRA CAPACITY EXPANSION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp"
    },
)
def cf_loss_share_stopping_protra_capacity_expansion_sp():
    """
    If the configuration of the power system cannot deal with variabilty of RES, the regressions estimate a reduction in the effective annual load hours. This parameter represents the threshold beyond which the loss in the CF would prevent investors to continue expanding the capacity of this technology.
    """
    return _ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp()


_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP",
    {},
    _root,
    {},
    "_ext_constant_cf_loss_share_stopping_protra_capacity_expansion_sp",
)


@component.add(
    name="CHP capacity utilization rate",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_utilization_rate": 1},
)
def chp_capacity_utilization_rate():
    """
    Rate of CHP capacity utilization to adjust the allocates.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA CHP I"]] = False
    value.values[except_subs.values] = 1
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA CHP I"]] = (
        protra_capacity_utilization_rate()
        .loc[:, _subscript_dict["PROTRA CHP I"]]
        .rename({"NRG PROTRA I": "PROTRA CHP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="DELAYED PROTRA CAPACITY EMPIRICAL",
    units="TW",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_protra_capacity_empirical": 1},
    other_deps={
        "_delayfixed_delayed_protra_capacity_empirical": {
            "initial": {"initial_protra_capacity_stock": 1},
            "step": {"protra_capacity_empirical_in_tw": 1},
        }
    },
)
def delayed_protra_capacity_empirical():
    """
    delayed capacity
    """
    return _delayfixed_delayed_protra_capacity_empirical()


_delayfixed_delayed_protra_capacity_empirical = DelayFixed(
    lambda: protra_capacity_empirical_in_tw(),
    lambda: 1,
    lambda: initial_protra_capacity_stock(),
    time_step,
    "_delayfixed_delayed_protra_capacity_empirical",
)


@component.add(
    name="EXOGENOUS TO RESERVE FACTOR",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"overcapacity_factor_empiric": 1},
)
def exogenous_to_reserve_factor():
    """
    exogeneous factor for the reserve factor in capacity expansion for stability testing purposes elec: 1.296 heat: 1.15 rest: 1.00
    """
    return overcapacity_factor_empiric()


@component.add(
    name="global max TO available from existing stock by commodity",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_available_by_commodity": 1},
)
def global_max_to_available_from_existing_stock_by_commodity():
    return sum(
        to_available_by_commodity().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="global PROTRA capacity stock",
    units="TW",
    subscripts=["NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_operative_capacity_stock_selected": 1},
)
def global_protra_capacity_stock():
    """
    globaly aggregated capacity stock
    """
    return sum(
        protra_operative_capacity_stock_selected().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="global TO decomissioned by commodity",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_decomissioned_by_commodity": 1},
)
def global_to_decomissioned_by_commodity():
    return sum(
        to_decomissioned_by_commodity().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="global TO required",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_required": 1},
)
def global_to_required():
    return sum(
        to_required().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="global TO shortfall",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_shortfall": 1},
)
def global_to_shortfall():
    """
    total global shortfall to be allocated to the different technologies
    """
    return sum(
        to_shortfall().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="INITIAL PROTRA CAPACITY STOCK",
    units="TW",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_protra_capacity_stock": 1},
    other_deps={
        "_initial_initial_protra_capacity_stock": {
            "initial": {"protra_capacity_empirical_in_tw": 1},
            "step": {},
        }
    },
)
def initial_protra_capacity_stock():
    """
    initial capacity stock (in year 2005)
    """
    return _initial_initial_protra_capacity_stock()


_initial_initial_protra_capacity_stock = Initial(
    lambda: protra_capacity_empirical_in_tw(), "_initial_initial_protra_capacity_stock"
)


@component.add(
    name="net PROTRA capacity expansion annual growth",
    units="1/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_selected": 1,
        "protra_capacity_decommissioning_selected": 1,
        "protra_operative_capacity_stock_selected": 1,
    },
)
def net_protra_capacity_expansion_annual_growth():
    """
    Net annual growth of capacity expansion (expressed as a decimal).
    """
    return zidz(
        protra_capacity_expansion_selected()
        - protra_capacity_decommissioning_selected(),
        protra_operative_capacity_stock_selected(),
    )


@component.add(
    name="OVERCAPACITY FACTOR EMPIRIC",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Constant",
    comp_subtype="External, Normal",
    depends_on={"__external__": "_ext_constant_overcapacity_factor_empiric"},
)
def overcapacity_factor_empiric():
    """
    Empirical overcapacity factors for electricity and heat. Note that for heat overcapacity factors are generally higher (in those regions where we have significant heat demand and capacities), for those countries without significant demand it was set to 1.25 on default.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS 9 I", "NRG TO I"],
    )
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[:, ["TO elec"]] = True
    def_subs.loc[:, ["TO heat"]] = True
    value.values[def_subs.values] = _ext_constant_overcapacity_factor_empiric().values[
        def_subs.values
    ]
    value.loc[:, ["TO gas"]] = 1
    value.loc[:, ["TO hydrogen"]] = 1
    value.loc[:, ["TO liquid"]] = 1
    value.loc[:, ["TO solid bio"]] = 1
    value.loc[:, ["TO solid fossil"]] = 1
    return value


_ext_constant_overcapacity_factor_empiric = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "OVERCAPACITY_FACTOR_ELEC*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "NRG TO I": ["TO elec"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG TO I": _subscript_dict["NRG TO I"],
    },
    "_ext_constant_overcapacity_factor_empiric",
)

_ext_constant_overcapacity_factor_empiric.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "OVERCAPACITY_FACTOR_HEAT*",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"], "NRG TO I": ["TO heat"]},
)


@component.add(
    name="production from CHP expansion",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "PROTRA CHP I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "max_to_from_existing_stock_by_protra": 1,
        "protra_heat_shortfall_allocation": 2,
        "chp_heat_power_ratio_9r": 1,
    },
)
def production_from_chp_expansion():
    """
    elec and heat production from heat allocation IF_THEN_ELSE( max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_heat, PROTRA_CHP_I] = 0 , 0 , PROTRA_heat_shortfall_allocation[REGIONS_9_I, TO_heat, PROTRA_CHP_I] / max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_heat, PROTRA_CHP_I] * max_TO_from_existing_stock_by_PROTRA[REGIONS_9_I, TO_elec, PROTRA_CHP_I] )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
        },
        ["REGIONS 9 I", "NRG TO I", "PROTRA CHP I"],
    )
    value.loc[:, ["TO elec"], :] = (
        if_then_else(
            max_to_from_existing_stock_by_protra()
            .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA CHP I"})
            == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "PROTRA CHP I": _subscript_dict["PROTRA CHP I"],
                },
                ["REGIONS 9 I", "PROTRA CHP I"],
            ),
            lambda: protra_heat_shortfall_allocation()
            .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA CHP I"})
            / chp_heat_power_ratio_9r(),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"], :] = (
        protra_heat_shortfall_allocation()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA CHP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = False
    except_subs.loc[:, ["TO heat"], :] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="production from HP expansion",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_heat_shortfall_allocation": 1},
)
def production_from_hp_expansion():
    """
    production of Heatplants from heat shortfall allocation
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
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA HP I"]] = (
        protra_heat_shortfall_allocation()
        .loc[:, "TO heat", _subscript_dict["PROTRA HP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA HP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA HP I"]] = False
    value.values[except_subs.values] = 0
    return value


@component.add(
    name="PROTRA capacity decommissioning",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "protra_capacity_variation_empirical": 3,
        "protra_lifetime": 1,
        "protra_capacity_stock": 1,
    },
)
def protra_capacity_decommissioning():
    """
    Transformation capacities that are being decomissioned each year (depends solely on the lifetime/depreciation periode of the power plant)
    """
    return if_then_else(
        np.logical_and(
            time() < 2020,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS 9 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS 9 I"})
            < 0,
        ),
        lambda: -protra_capacity_variation_empirical()
        .loc[_subscript_dict["REGIONS 9 I"], :, :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"}),
        lambda: if_then_else(
            np.logical_and(
                time() < 2020,
                protra_capacity_variation_empirical()
                .loc[_subscript_dict["REGIONS 9 I"], :, :]
                .rename({"REGIONS 36 I": "REGIONS 9 I"})
                >= 0,
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "NRG TO I": _subscript_dict["NRG TO I"],
                    "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                },
                ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
            ),
            lambda: protra_capacity_stock() / protra_lifetime(),
        ),
    )


@component.add(
    name="PROTRA capacity decommissioning 35R",
    units="TW/Year",
    subscripts=["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning_selected": 1,
        "protra_capacity_decommissioning_eu27": 1,
    },
)
def protra_capacity_decommissioning_35r():
    """
    Capacity decommissioning of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = (
        protra_capacity_decommissioning_selected()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], :, :] = (
        protra_capacity_decommissioning_eu27().values
    )
    return value


@component.add(
    name="PROTRA capacity decommissioning EU27",
    units="TW/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "protra_capacity_decommissioning_selected": 1,
        "share_protra_capacity_stock_eu27": 1,
    },
)
def protra_capacity_decommissioning_eu27():
    """
    PROTRA capacity stock decommissioning for the 27 EU countries. Until 2020 historic data and thereafter downscaling the information from the aggregated EU27. The MIN function takes only those empirical negative values which mean new capacity. Old equation: IF_THEN_ELSE( Time <= 2020, -MIN(0 , PROTRA_CAPACITY_VARIATION_EMPIRICAL[REGIONS EU27 I,NRG TO I,NRG PROTRA I]), PROTRA capacity stock EU27[REGIONS EU27 I,NRG TO I,NRG PROTRA I]/PROTRA LIFETIME[EU27,NRG PROTRA I] )
    """
    return if_then_else(
        time() <= 2020,
        lambda: -np.minimum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
        ),
        lambda: (
            protra_capacity_decommissioning_selected()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * share_protra_capacity_stock_eu27().transpose(
                "NRG TO I", "NRG PROTRA I", "REGIONS EU27 I"
            )
        ).transpose("REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"),
    )


@component.add(
    name="PROTRA capacity decommissioning EU27 2nd approach",
    units="TW/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "protra_lifetime": 1,
        "protra_capacity_stock_eu27_2nd_approach": 1,
    },
)
def protra_capacity_decommissioning_eu27_2nd_approach():
    return if_then_else(
        time() <= 2020,
        lambda: -np.minimum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
        ),
        lambda: protra_capacity_stock_eu27_2nd_approach()
        / protra_lifetime().loc["EU27", :].reset_coords(drop=True),
    )


@component.add(
    name="PROTRA capacity decommissioning selected",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_decommissioning": 1},
)
def protra_capacity_decommissioning_selected():
    """
    Selection of the method to account the decommission of process transformation capacities
    """
    return protra_capacity_decommissioning()


@component.add(
    name="PROTRA CAPACITY EMPIRICAL",
    units="GW",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Data",
    comp_subtype="External, Normal",
    depends_on={
        "__external__": "_ext_data_protra_capacity_empirical",
        "__data__": "_ext_data_protra_capacity_empirical",
        "time": 1,
    },
)
def protra_capacity_empirical():
    """
    Empirical capacites of conversion technologies, disaggregated in WILIAM technologies. Source: JRC_IDEES, IEA, IRENA, IAE; (note: unit in excel file is GW)
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
    def_subs = xr.zeros_like(value, dtype=bool)
    def_subs.loc[
        ["AUSTRIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["AUSTRIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["BELGIUM"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["BELGIUM"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["BULGARIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["BULGARIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["CHINA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["CHINA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["CROATIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["CROATIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["CYPRUS"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["CYPRUS"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["CZECH REPUBLIC"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["CZECH REPUBLIC"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["DENMARK"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["DENMARK"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["EASOC"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["EASOC"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["ESTONIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["ESTONIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["EU27"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["EU27"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["FINLAND"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["FINLAND"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["FRANCE"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["FRANCE"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["GERMANY"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["GERMANY"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["GREECE"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["GREECE"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["HUNGARY"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["HUNGARY"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["INDIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["INDIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["IRELAND"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["IRELAND"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["ITALY"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["ITALY"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["LATAM"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["LATAM"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["LATVIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["LATVIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["LITHUANIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["LITHUANIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["LROW"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["LROW"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["LUXEMBOURG"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["LUXEMBOURG"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["MALTA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["MALTA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["NETHERLANDS"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["NETHERLANDS"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["POLAND"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["POLAND"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["PORTUGAL"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["PORTUGAL"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["ROMANIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["ROMANIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["RUSSIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["RUSSIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["SLOVAKIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["SLOVAKIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["SLOVENIA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["SLOVENIA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["SPAIN"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["SPAIN"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["SWEDEN"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["SWEDEN"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["UK"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["UK"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    def_subs.loc[
        ["USMCA"],
        ["TO heat"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA HP gas fuels",
            "PROTRA HP solid bio",
            "PROTRA HP geothermal",
            "PROTRA HP liquid fuels",
            "PROTRA HP solar DEACTIVATED",
            "PROTRA HP solid fossil",
            "PROTRA HP waste",
        ],
    ] = True
    def_subs.loc[
        ["USMCA"],
        ["TO elec"],
        [
            "PROTRA CHP gas fuels",
            "PROTRA CHP gas fuels CCS",
            "PROTRA CHP geothermal DEACTIVATED",
            "PROTRA CHP liquid fuels",
            "PROTRA CHP liquid fuels CCS",
            "PROTRA CHP solid fossil",
            "PROTRA CHP solid fossil CCS",
            "PROTRA CHP waste",
            "PROTRA CHP solid bio",
            "PROTRA CHP solid bio CCS",
            "PROTRA PP solid bio",
            "PROTRA PP solid bio CCS",
            "PROTRA PP gas fuels",
            "PROTRA PP gas fuels CCS",
            "PROTRA PP geothermal",
            "PROTRA PP hydropower dammed",
            "PROTRA PP hydropower run of river",
            "PROTRA PP liquid fuels",
            "PROTRA PP liquid fuels CCS",
            "PROTRA PP nuclear",
            "PROTRA PP oceanic",
            "PROTRA PP solar CSP",
            "PROTRA PP solar open space PV",
            "PROTRA PP solar urban PV",
            "PROTRA PP solid fossil",
            "PROTRA PP solid fossil CCS",
            "PROTRA PP waste",
            "PROTRA PP waste CCS",
            "PROTRA PP wind offshore",
            "PROTRA PP wind onshore",
        ],
    ] = True
    value.values[def_subs.values] = _ext_data_protra_capacity_empirical(time()).values[
        def_subs.values
    ]
    value.loc[:, ["TO gas"], ["PROTRA blending gas fuels"]] = 10000
    value.loc[:, ["TO liquid"], ["PROTRA blending liquid fuels"]] = 10000
    value.loc[:, ["TO hydrogen"], ["PROTRA no process TI hydrogen"]] = 10000
    value.loc[:, ["TO solid bio"], ["PROTRA no process TI solid bio"]] = 10000
    value.loc[:, ["TO solid fossil"], ["PROTRA no process TI solid fossil"]] = 10000
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA HP I"]] = True
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA HP I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA CHP I"]] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA CHP I"]] = False
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP I"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA NP I"]] = True
    except_subs.loc[:, ["TO hydrogen"], ["PROTRA no process TI hydrogen"]] = False
    except_subs.loc[:, ["TO solid bio"], ["PROTRA no process TI solid bio"]] = False
    except_subs.loc[:, ["TO solid fossil"], ["PROTRA no process TI solid fossil"]] = (
        False
    )
    except_subs.loc[:, ["TO gas"], ["PROTRA blending gas fuels"]] = False
    except_subs.loc[:, ["TO liquid"], ["PROTRA blending liquid fuels"]] = False
    value.values[except_subs.values] = 0
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, _subscript_dict["PROTRA PP I"]] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = False
    value.values[except_subs.values] = 0
    return value


_ext_data_protra_capacity_empirical = ExtData(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "AUSTRIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["AUSTRIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
    _root,
    {
        "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
        "NRG TO I": _subscript_dict["NRG TO I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_data_protra_capacity_empirical",
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "AUSTRIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["AUSTRIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BELGIUM_TO_heat",
    None,
    {
        "REGIONS 36 I": ["BELGIUM"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BELGIUM_TO_elec",
    None,
    {
        "REGIONS 36 I": ["BELGIUM"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BULGARIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["BULGARIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "BULGARIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["BULGARIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CHINA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["CHINA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CHINA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["CHINA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CROATIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["CROATIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CROATIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["CROATIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CYPRUS_TO_heat",
    None,
    {
        "REGIONS 36 I": ["CYPRUS"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CYPRUS_TO_elec",
    None,
    {
        "REGIONS 36 I": ["CYPRUS"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CZECH_REPUBLIC_TO_heat",
    None,
    {
        "REGIONS 36 I": ["CZECH REPUBLIC"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "CZECH_REPUBLIC_TO_elec",
    None,
    {
        "REGIONS 36 I": ["CZECH REPUBLIC"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "DENMARK_TO_heat",
    None,
    {
        "REGIONS 36 I": ["DENMARK"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "DENMARK_TO_elec",
    None,
    {
        "REGIONS 36 I": ["DENMARK"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EASOC_TO_heat",
    None,
    {
        "REGIONS 36 I": ["EASOC"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EASOC_TO_elec",
    None,
    {
        "REGIONS 36 I": ["EASOC"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ESTONIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["ESTONIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ESTONIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["ESTONIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EU27_TO_heat",
    None,
    {
        "REGIONS 36 I": ["EU27"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "EU27_TO_elec",
    None,
    {
        "REGIONS 36 I": ["EU27"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FINLAND_TO_heat",
    None,
    {
        "REGIONS 36 I": ["FINLAND"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FINLAND_TO_elec",
    None,
    {
        "REGIONS 36 I": ["FINLAND"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FRANCE_TO_heat",
    None,
    {
        "REGIONS 36 I": ["FRANCE"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "FRANCE_TO_elec",
    None,
    {
        "REGIONS 36 I": ["FRANCE"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GERMANY_TO_heat",
    None,
    {
        "REGIONS 36 I": ["GERMANY"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GERMANY_TO_elec",
    None,
    {
        "REGIONS 36 I": ["GERMANY"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GREECE_TO_heat",
    None,
    {
        "REGIONS 36 I": ["GREECE"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "GREECE_TO_elec",
    None,
    {
        "REGIONS 36 I": ["GREECE"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "HUNGARY_TO_heat",
    None,
    {
        "REGIONS 36 I": ["HUNGARY"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "HUNGARY_TO_elec",
    None,
    {
        "REGIONS 36 I": ["HUNGARY"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "INDIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["INDIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "INDIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["INDIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "IRELAND_TO_heat",
    None,
    {
        "REGIONS 36 I": ["IRELAND"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "IRELAND_TO_elec",
    None,
    {
        "REGIONS 36 I": ["IRELAND"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ITALY_TO_heat",
    None,
    {
        "REGIONS 36 I": ["ITALY"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ITALY_TO_elec",
    None,
    {
        "REGIONS 36 I": ["ITALY"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATAM_TO_heat",
    None,
    {
        "REGIONS 36 I": ["LATAM"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATAM_TO_elec",
    None,
    {
        "REGIONS 36 I": ["LATAM"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATVIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["LATVIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LATVIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["LATVIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LITHUANIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["LITHUANIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LITHUANIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["LITHUANIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LROW_TO_heat",
    None,
    {
        "REGIONS 36 I": ["LROW"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LROW_TO_elec",
    None,
    {
        "REGIONS 36 I": ["LROW"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LUXEMBOURG_TO_heat",
    None,
    {
        "REGIONS 36 I": ["LUXEMBOURG"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "LUXEMBOURG_TO_elec",
    None,
    {
        "REGIONS 36 I": ["LUXEMBOURG"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "MALTA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["MALTA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "MALTA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["MALTA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "NETHERLANDS_TO_heat",
    None,
    {
        "REGIONS 36 I": ["NETHERLANDS"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "NETHERLANDS_TO_elec",
    None,
    {
        "REGIONS 36 I": ["NETHERLANDS"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "POLAND_TO_heat",
    None,
    {
        "REGIONS 36 I": ["POLAND"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "POLAND_TO_elec",
    None,
    {
        "REGIONS 36 I": ["POLAND"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "PORTUGAL_TO_heat",
    None,
    {
        "REGIONS 36 I": ["PORTUGAL"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "PORTUGAL_TO_elec",
    None,
    {
        "REGIONS 36 I": ["PORTUGAL"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ROMANIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["ROMANIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "ROMANIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["ROMANIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "RUSSIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["RUSSIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "RUSSIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["RUSSIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVAKIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["SLOVAKIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVAKIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["SLOVAKIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVENIA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["SLOVENIA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SLOVENIA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["SLOVENIA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SPAIN_TO_heat",
    None,
    {
        "REGIONS 36 I": ["SPAIN"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SPAIN_TO_elec",
    None,
    {
        "REGIONS 36 I": ["SPAIN"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SWEDEN_TO_heat",
    None,
    {
        "REGIONS 36 I": ["SWEDEN"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "SWEDEN_TO_elec",
    None,
    {
        "REGIONS 36 I": ["SWEDEN"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "UK_TO_heat",
    None,
    {
        "REGIONS 36 I": ["UK"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "UK_TO_elec",
    None,
    {
        "REGIONS 36 I": ["UK"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "USMCA_TO_heat",
    None,
    {
        "REGIONS 36 I": ["USMCA"],
        "NRG TO I": ["TO heat"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP HP I"],
    },
)

_ext_data_protra_capacity_empirical.add(
    "model_parameters/energy/PROTRA_capacity_vensim_import.xlsx",
    "PROTRA_capacity",
    "PROTRA_CAP_TIME",
    "USMCA_TO_elec",
    None,
    {
        "REGIONS 36 I": ["USMCA"],
        "NRG TO I": ["TO elec"],
        "NRG PROTRA I": _subscript_dict["PROTRA CHP PP I"],
    },
)


@component.add(
    name="PROTRA CAPACITY EMPIRICAL IN TW",
    units="TW",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_empirical": 1, "unit_conversion_gw_tw": 1},
)
def protra_capacity_empirical_in_tw():
    """
    empirical capacities in TW
    """
    return protra_capacity_empirical() / unit_conversion_gw_tw()


@component.add(
    name="PROTRA capacity expansion",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "protra_capacity_variation_empirical": 3,
        "protra_shortfall_allocation": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
        "one_year": 1,
    },
)
def protra_capacity_expansion():
    """
    New transformation capacity added to the energy transformation system
    """
    return (
        if_then_else(
            np.logical_and(
                time() < 2020,
                protra_capacity_variation_empirical()
                .loc[_subscript_dict["REGIONS 9 I"], :, :]
                .rename({"REGIONS 36 I": "REGIONS 9 I"})
                > 0,
            ),
            lambda: protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS 9 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS 9 I"}),
            lambda: if_then_else(
                np.logical_and(
                    time() < 2020,
                    protra_capacity_variation_empirical()
                    .loc[_subscript_dict["REGIONS 9 I"], :, :]
                    .rename({"REGIONS 36 I": "REGIONS 9 I"})
                    <= 0,
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                        "NRG TO I": _subscript_dict["NRG TO I"],
                        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                    },
                    ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
                ),
                lambda: zidz(
                    protra_shortfall_allocation(),
                    protra_max_full_load_hours_after_constraints().expand_dims(
                        {"NRG TO I": _subscript_dict["NRG TO I"]}, 1
                    ),
                )
                / unit_conversion_tw_per_ej_per_year(),
            ),
        )
        / one_year()
    )


@component.add(
    name="PROTRA capacity expansion 35R",
    units="TW/Year",
    subscripts=["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_selected": 1,
        "protra_capacity_expansion_eu27": 1,
    },
)
def protra_capacity_expansion_35r():
    """
    Capacity expansion of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = (
        protra_capacity_expansion_selected()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], :, :] = (
        protra_capacity_expansion_eu27().values
    )
    return value


@component.add(
    name="PROTRA capacity expansion EU27",
    units="TW/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "protra_capacity_expansion_selected": 1,
        "share_protra_capacity_stock_eu27": 1,
    },
)
def protra_capacity_expansion_eu27():
    """
    Until 2020 historic data and thereafter downscaling of the capacity expansion for the 27 EU countries taking as reference the capacity stock of each country. The MAX function takes only those empirical positive values which mean new capacity.
    """
    return if_then_else(
        time() <= 2020,
        lambda: np.maximum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
        ),
        lambda: (
            protra_capacity_expansion_selected()
            .loc["EU27", :, :]
            .reset_coords(drop=True)
            * share_protra_capacity_stock_eu27().transpose(
                "NRG TO I", "NRG PROTRA I", "REGIONS EU27 I"
            )
        ).transpose("REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"),
    )


@component.add(
    name="PROTRA capacity expansion EU27 2nd approach",
    units="TW/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "protra_capacity_variation_empirical": 1,
        "shares_to_shortfall_by_commodity_eu27_2nd_approach": 1,
        "protra_capacity_expansion": 1,
    },
)
def protra_capacity_expansion_eu27_2nd_approach():
    return if_then_else(
        time() <= 2020,
        lambda: np.maximum(
            0,
            protra_capacity_variation_empirical()
            .loc[_subscript_dict["REGIONS EU27 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
        ),
        lambda: (
            protra_capacity_expansion().loc["EU27", :, :].reset_coords(drop=True)
            * shares_to_shortfall_by_commodity_eu27_2nd_approach().transpose(
                "NRG TO I", "REGIONS EU27 I"
            )
        ).transpose("REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"),
    )


@component.add(
    name="PROTRA CAPACITY EXPANSION POLICY WEIGHT SP",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_policy_weight_sp"
    },
)
def protra_capacity_expansion_policy_weight_sp():
    """
    capacity expansion policy weight: 0=only endogenous LCOE signal, 1 = only exogenous signal
    """
    return _ext_constant_protra_capacity_expansion_policy_weight_sp()


_ext_constant_protra_capacity_expansion_policy_weight_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PROTRA_CAPACITY_EXPANSION_POLICY_WEIGHT_SP",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_protra_capacity_expansion_policy_weight_sp",
)


@component.add(
    name="PROTRA CAPACITY EXPANSION PRIORITIES VECTOR SP",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_protra_capacity_expansion_priorities_vector_sp"
    },
)
def protra_capacity_expansion_priorities_vector_sp():
    """
    scenario parameter for policy parameters
    """
    return _ext_constant_protra_capacity_expansion_priorities_vector_sp()


_ext_constant_protra_capacity_expansion_priorities_vector_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "CAPACITY_EXPANSION_POLICY_PRIORITIES_SP*",
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_capacity_expansion_priorities_vector_sp",
)


@component.add(
    name="PROTRA capacity expansion selected",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials_calculator": 1,
        "protra_capacity_expansion": 1,
        "protra_capacity_expansion_calculator": 1,
    },
)
def protra_capacity_expansion_selected():
    """
    Selection of the method to account the expansion of process transformation capacities
    """
    return if_then_else(
        switch_materials_calculator() == 0,
        lambda: protra_capacity_expansion(),
        lambda: protra_capacity_expansion_calculator().expand_dims(
            {"NRG TO I": _subscript_dict["NRG TO I"]}, 1
        ),
    )


@component.add(
    name="PROTRA capacity stock",
    units="TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_protra_capacity_stock": 1},
    other_deps={
        "_integ_protra_capacity_stock": {
            "initial": {"initial_protra_capacity_stock": 1},
            "step": {
                "protra_capacity_expansion": 1,
                "protra_capacity_decommissioning": 1,
            },
        }
    },
)
def protra_capacity_stock():
    """
    Capacity stock of TI-TO transformation technology capacities by TO (PROTRA)
    """
    return _integ_protra_capacity_stock()


_integ_protra_capacity_stock = Integ(
    lambda: protra_capacity_expansion() - protra_capacity_decommissioning(),
    lambda: initial_protra_capacity_stock()
    .loc[_subscript_dict["REGIONS 9 I"], :, :]
    .rename({"REGIONS 36 I": "REGIONS 9 I"}),
    "_integ_protra_capacity_stock",
)


@component.add(
    name="PROTRA capacity stock 35R",
    units="TW/Year",
    subscripts=["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 1,
        "protra_capacity_stock_eu27": 1,
    },
)
def protra_capacity_stock_35r():
    """
    Capacity stock of the PROTRA for the 35 regions downscaling the information from EU27 aggregated to the 27 EU countries taking as reference the empirical variation of capacity stock for each country.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 35 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = (
        protra_operative_capacity_stock_selected()
        .loc[_subscript_dict["REGIONS 8 I"], :, :]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        .values
    )
    value.loc[_subscript_dict["REGIONS EU27 I"], :, :] = (
        protra_capacity_stock_eu27().values
    )
    return value


@component.add(
    name="PROTRA capacity stock EU27",
    units="TW",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_protra_capacity_stock_eu27": 1},
    other_deps={
        "_integ_protra_capacity_stock_eu27": {
            "initial": {"protra_capacity_empirical_in_tw": 1},
            "step": {
                "protra_capacity_expansion_eu27": 1,
                "protra_capacity_decommissioning_eu27": 1,
            },
        }
    },
)
def protra_capacity_stock_eu27():
    """
    PROTRA capacity stock for the 27 EU countries downscaling the information from the aggregated EU27.
    """
    return _integ_protra_capacity_stock_eu27()


_integ_protra_capacity_stock_eu27 = Integ(
    lambda: protra_capacity_expansion_eu27() - protra_capacity_decommissioning_eu27(),
    lambda: protra_capacity_empirical_in_tw()
    .loc[_subscript_dict["REGIONS EU27 I"], :, :]
    .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
    "_integ_protra_capacity_stock_eu27",
)


@component.add(
    name="PROTRA capacity stock EU27 2nd approach",
    units="TW",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_protra_capacity_stock_eu27_2nd_approach": 1},
    other_deps={
        "_integ_protra_capacity_stock_eu27_2nd_approach": {
            "initial": {"protra_capacity_empirical_in_tw": 1},
            "step": {
                "protra_capacity_expansion_eu27_2nd_approach": 1,
                "protra_capacity_decommissioning_eu27_2nd_approach": 1,
            },
        }
    },
)
def protra_capacity_stock_eu27_2nd_approach():
    """
    PROTRA capacity stock for the 27 EU countries downscaling the information from the aggregated EU27.
    """
    return _integ_protra_capacity_stock_eu27_2nd_approach()


_integ_protra_capacity_stock_eu27_2nd_approach = Integ(
    lambda: protra_capacity_expansion_eu27_2nd_approach()
    - protra_capacity_decommissioning_eu27_2nd_approach(),
    lambda: protra_capacity_empirical_in_tw()
    .loc[_subscript_dict["REGIONS EU27 I"], :, :]
    .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
    "_integ_protra_capacity_stock_eu27_2nd_approach",
)


@component.add(
    name="PROTRA CAPACITY VARIATION EMPIRICAL",
    units="TW",
    subscripts=["REGIONS 36 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_empirical_in_tw": 1,
        "delayed_protra_capacity_empirical": 1,
    },
)
def protra_capacity_variation_empirical():
    """
    net capacity addition (positiv) or reduction (negativ) calculated from empirical values
    """
    return protra_capacity_empirical_in_tw() - delayed_protra_capacity_empirical()


@component.add(
    name="PROTRA CHP and HP expansion request",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_heat_expansion_request_with_res_potentials": 2,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def protra_chp_and_hp_expansion_request():
    """
    Request of heat to be generated by each PROTRA CHP and HP. Priority is given to heat allocation. We assign the same amount for all technologies (if they are not affected by a potential) in order to avoid biases. We take the TO_shortfall of heat as reference. TESTING: [REGIONS_9_I,TO_heat,PROTRA_CHP_HP_I] -> max_TO_from_existing_stock_by_PROTRA_delayed[REGIONS_9_I,TO_heat,PROTRA_CHP _HP_I]
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
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO heat"], :] = True
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP NON CCS I"]] = (
        protra_heat_expansion_request_with_res_potentials()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP HP NON CCS I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA CHP HP NON CCS I"})
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP CCS I"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 4,
            ),
            lambda: protra_heat_expansion_request_with_res_potentials()
            .loc[:, "TO heat", _subscript_dict["PROTRA CHP HP CCS I"]]
            .reset_coords(drop=True)
            .rename({"NRG PRO I": "PROTRA CHP HP CCS I"}),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "PROTRA CHP HP CCS I": _subscript_dict["PROTRA CHP HP CCS I"],
                },
                ["REGIONS 9 I", "PROTRA CHP HP CCS I"],
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA elec expansion request",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request_with_limits": 2,
        "select_availability_unmature_energy_technologies_sp": 2,
    },
)
def protra_elec_expansion_request():
    """
    Request of electricity to be generated by each PROTRA PP (after substracting the electricity generation from CHP, since priority is first given to heat allocation). We assign the same amount for all technologies (if they are not affected by a potential) in order to avoid biases. We take the TO_shortfall of electricity as reference.
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
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA PP I"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA PP NON CCS I"]] = (
        protra_elec_expansion_request_with_limits()
        .loc[:, "TO elec", _subscript_dict["PROTRA PP NON CCS I"]]
        .reset_coords(drop=True)
        .rename({"PROTRA PP I": "PROTRA PP NON CCS I"})
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA PP CCS I"]] = (
        if_then_else(
            np.logical_or(
                select_availability_unmature_energy_technologies_sp() == 1,
                select_availability_unmature_energy_technologies_sp() == 4,
            ),
            lambda: protra_elec_expansion_request_with_limits()
            .loc[:, "TO elec", _subscript_dict["PROTRA PP CCS I"]]
            .reset_coords(drop=True)
            .rename({"PROTRA PP I": "PROTRA PP CCS I"}),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "PROTRA PP CCS I": _subscript_dict["PROTRA PP CCS I"],
                },
                ["REGIONS 9 I", "PROTRA PP CCS I"],
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA elec expansion request with limits",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA PP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request_with_limits_res": 1,
        "protra_elec_expansion_request_with_limits_nres": 1,
    },
)
def protra_elec_expansion_request_with_limits():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PROTRA PP I": _subscript_dict["PROTRA PP I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA PP I"],
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA RES PP I"]] = (
        protra_elec_expansion_request_with_limits_res()
        .loc[:, "TO elec", _subscript_dict["PROTRA RES PP I"]]
        .reset_coords(drop=True)
        .rename({"NRG PRO I": "PROTRA RES PP I"})
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA PP NRES I"]] = (
        protra_elec_expansion_request_with_limits_nres()
        .loc[:, "TO elec", :]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA elec expansion request with limits NRES",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA PP NRES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_elec_shortfall_to_be_allocated": 2,
        "stress_signal_uranium_scarcity": 1,
    },
)
def protra_elec_expansion_request_with_limits_nres():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "PROTRA PP NRES I": _subscript_dict["PROTRA PP NRES I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "PROTRA PP NRES I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], :] = True
    except_subs.loc[:, ["TO elec"], ["PROTRA PP nuclear"]] = False
    value.values[except_subs.values] = (
        remaining_elec_shortfall_to_be_allocated()
        .loc[:, "TO elec"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"PROTRA PP NRES I": _subscript_dict["PROTRA PP NRES I"]}, 2)
        .values[except_subs.loc[:, ["TO elec"], :].values]
    )
    value.loc[:, ["TO elec"], ["PROTRA PP nuclear"]] = (
        (
            remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO elec"]
            .reset_coords(drop=True)
            * (
                1
                - stress_signal_uranium_scarcity()
                .loc[:, "TO elec", "PROTRA PP nuclear"]
                .reset_coords(drop=True)
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP nuclear"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA elec expansion request with limits RES",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_potential_protra_res_pp": 5,
        "remaining_elec_shortfall_to_be_allocated": 11,
        "unlimited_protra_res_parameter": 1,
        "switch_law2nrg_solarland": 1,
        "stress_signal_solar_land": 1,
        "stress_signal_protra_curtailed": 4,
        "switch_energy": 2,
        "switch_nrg_limited_res_potentials": 5,
        "switch_nrg_variability_effects": 4,
        "switch_law2nrg_available_forestry_products_for_industry": 1,
        "signal_availability_forestry_products_for_energy": 1,
    },
)
def protra_elec_expansion_request_with_limits_res():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials and global uranium maximum extraction curve. To avoid errors with low RES potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
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
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA RES PP I"]] = True
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar urban PV"]] = False
    except_subs.loc[:, ["TO elec"], ["PROTRA PP solar CSP"]] = False
    except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA SOLID BIO I"]] = False
    value.values[except_subs.values] = (
        if_then_else(
            remaining_potential_protra_res_pp()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            > 0,
            lambda: remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO elec"]
            .reset_coords(drop=True)
            .expand_dims({"PROTRA RES PP I": _subscript_dict["PROTRA RES PP I"]}, 1),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "PROTRA RES PP I": _subscript_dict["PROTRA RES PP I"],
                },
                ["REGIONS 9 I", "PROTRA RES PP I"],
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values[
            except_subs.loc[:, ["TO elec"], _subscript_dict["PROTRA RES PP I"]].values
        ]
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar open space PV"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 0,
                lambda: xr.DataArray(
                    unlimited_protra_res_parameter(),
                    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                    ["REGIONS 9 I"],
                ),
                lambda: if_then_else(
                    np.logical_or(
                        switch_energy() == 0, switch_law2nrg_solarland() == 0
                    ),
                    lambda: if_then_else(
                        remaining_potential_protra_res_pp()
                        .loc[:, "TO elec", "PROTRA PP solar open space PV"]
                        .reset_coords(drop=True)
                        > 0,
                        lambda: remaining_elec_shortfall_to_be_allocated()
                        .loc[:, "TO elec"]
                        .reset_coords(drop=True),
                        lambda: xr.DataArray(
                            0,
                            {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                            ["REGIONS 9 I"],
                        ),
                    ),
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO elec"]
                    .reset_coords(drop=True)
                    * stress_signal_solar_land(),
                ),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO elec", "PROTRA PP solar open space PV"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA WIND I"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO elec", _subscript_dict["PROTRA WIND I"]]
                    .reset_coords(drop=True)
                    .rename({"PROTRA RES PP I": "PROTRA WIND I"})
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO elec"]
                    .reset_coords(drop=True)
                    .expand_dims(
                        {"PROTRA WIND I": _subscript_dict["PROTRA WIND I"]}, 1
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                            "PROTRA WIND I": _subscript_dict["PROTRA WIND I"],
                        },
                        ["REGIONS 9 I", "PROTRA WIND I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO elec"]
                .reset_coords(drop=True)
                .expand_dims({"PROTRA WIND I": _subscript_dict["PROTRA WIND I"]}, 1),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO elec", _subscript_dict["PROTRA WIND I"]]
                .reset_coords(drop=True)
                .rename({"NRG PROTRA I": "PROTRA WIND I"})
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar urban PV"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO elec", "PROTRA PP solar urban PV"]
                    .reset_coords(drop=True)
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO elec"]
                    .reset_coords(drop=True),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                        ["REGIONS 9 I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO elec"]
                .reset_coords(drop=True),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO elec", "PROTRA PP solar urban PV"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], ["PROTRA PP solar CSP"]] = (
        (
            if_then_else(
                switch_nrg_limited_res_potentials() == 1,
                lambda: if_then_else(
                    remaining_potential_protra_res_pp()
                    .loc[:, "TO elec", "PROTRA PP solar CSP"]
                    .reset_coords(drop=True)
                    > 0,
                    lambda: remaining_elec_shortfall_to_be_allocated()
                    .loc[:, "TO elec"]
                    .reset_coords(drop=True),
                    lambda: xr.DataArray(
                        0,
                        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
                        ["REGIONS 9 I"],
                    ),
                ),
                lambda: remaining_elec_shortfall_to_be_allocated()
                .loc[:, "TO elec"]
                .reset_coords(drop=True),
            )
            * (
                1
                - stress_signal_protra_curtailed()
                .loc[:, "TO elec", "PROTRA PP solar CSP"]
                .reset_coords(drop=True)
                * switch_nrg_variability_effects()
            )
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 2)
        .values
    )
    value.loc[:, ["TO elec"], _subscript_dict["PROTRA SOLID BIO I"]] = (
        if_then_else(
            np.logical_or(
                switch_nrg_limited_res_potentials() == 0,
                np.logical_or(
                    switch_law2nrg_available_forestry_products_for_industry() == 0,
                    switch_energy() == 0,
                ),
            ),
            lambda: remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO elec"]
            .reset_coords(drop=True),
            lambda: remaining_elec_shortfall_to_be_allocated()
            .loc[:, "TO elec"]
            .reset_coords(drop=True)
            * signal_availability_forestry_products_for_energy(),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"PROTRA SOLID BIO I": _subscript_dict["PROTRA SOLID BIO I"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA elec shortfall allocation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PRO I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_elec_expansion_request": 1,
        "protra_priority_vector": 1,
        "remaining_elec_shortfall_to_be_allocated": 1,
    },
)
def protra_elec_shortfall_allocation():
    """
    Allocating remaining elec shortfall (after deducting elec-production from CHPs) to PP-technologies ALLOCATE_BY_PRIORITY( PROTRA_expansion_limit[REGIONS 9 I,TO elec,PROTRA PP I], PROTRA CAPACITY EXPANSION PRIORITIES VECTOR SP[REGIONS 9 I,PROTRA PP I], ELMCOUNT(PROTRA PP I), 0.1, remaining_shortfall_to_be_allocated[REGIONS 9 I,TO elec] )
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
            protra_elec_expansion_request()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True),
            protra_priority_vector(),
            remaining_elec_shortfall_to_be_allocated()
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
    name="PROTRA heat expansion request with RES potentials",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_shortfall": 13,
        "remaining_potential_protra_res_chp_hp": 5,
        "switch_nrg_limited_res_potentials": 6,
        "switch_law2nrg_available_forestry_products_for_industry": 1,
        "switch_energy": 1,
        "signal_availability_forestry_products_for_energy": 1,
    },
)
def protra_heat_expansion_request_with_res_potentials():
    """
    Capacity expansion request for PROTRA elec incorporating RES potentials. To avoid errors with low potentials' estimates, we consider the following cases: - The limitation cannot influence during historic time (i.e., before 2020). - If "remaining potential" < 0, then the new capacity is set to 0, and we let the capacity stock decrease due to decommissioning until the capacity stock and CF (before curtailment) matches the potential. - If "remaining potential" > 0, we let the potential limit the new additions in the future.
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
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP I"]] = True
    except_subs.loc[:, ["TO heat"], ["PROTRA CHP geothermal DEACTIVATED"]] = False
    except_subs.loc[:, ["TO heat"], ["PROTRA CHP waste"]] = False
    except_subs.loc[:, ["TO heat"], ["PROTRA HP geothermal"]] = False
    except_subs.loc[:, ["TO heat"], ["PROTRA HP solar DEACTIVATED"]] = False
    except_subs.loc[:, ["TO heat"], ["PROTRA HP waste"]] = False
    except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA SOLID BIO I"]] = False
    value.values[except_subs.values] = (
        to_shortfall()
        .loc[:, "TO heat"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"PROTRA CHP HP I": _subscript_dict["PROTRA CHP HP I"]}, 2)
        .values[
            except_subs.loc[:, ["TO heat"], _subscript_dict["PROTRA CHP HP I"]].values
        ]
    )
    value.loc[:, ["TO heat"], ["PROTRA CHP geothermal DEACTIVATED"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO heat", "PROTRA CHP geothermal DEACTIVATED"]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA CHP geothermal DEACTIVATED"]}, 2)
        .values
    )
    value.loc[:, ["TO heat"], ["PROTRA CHP waste"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO heat", "PROTRA CHP waste"]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA CHP waste"]}, 2)
        .values
    )
    value.loc[:, ["TO heat"], ["PROTRA HP geothermal"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO heat", "PROTRA HP geothermal"]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA HP geothermal"]}, 2)
        .values
    )
    value.loc[:, ["TO heat"], ["PROTRA HP solar DEACTIVATED"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO heat", "PROTRA HP solar DEACTIVATED"]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA HP solar DEACTIVATED"]}, 2)
        .values
    )
    value.loc[:, ["TO heat"], ["PROTRA HP waste"]] = (
        if_then_else(
            switch_nrg_limited_res_potentials() == 1,
            lambda: if_then_else(
                remaining_potential_protra_res_chp_hp()
                .loc[:, "TO heat", "PROTRA HP waste"]
                .reset_coords(drop=True)
                > 0,
                lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
                lambda: xr.DataArray(
                    0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA HP waste"]}, 2)
        .values
    )
    value.loc[:, ["TO heat"], _subscript_dict["PROTRA SOLID BIO I"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                np.logical_or(
                    switch_law2nrg_available_forestry_products_for_industry() == 0,
                    switch_nrg_limited_res_potentials() == 0,
                ),
            ),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
            lambda: to_shortfall().loc[:, "TO heat"].reset_coords(drop=True)
            * signal_availability_forestry_products_for_energy(),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .expand_dims({"PROTRA SOLID BIO I": _subscript_dict["PROTRA SOLID BIO I"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA heat shortfall allocation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_chp_and_hp_expansion_request": 1,
        "protra_priority_vector": 1,
        "to_shortfall": 1,
    },
)
def protra_heat_shortfall_allocation():
    """
    Allocating heat shortfall to new heat (CHP and HP) capacities
    """
    return allocate_available(
        protra_chp_and_hp_expansion_request()
        .loc[:, "TO heat", :]
        .reset_coords(drop=True),
        protra_priority_vector(),
        to_shortfall().loc[:, "TO heat"].reset_coords(drop=True),
    ).expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)


@component.add(
    name="PROTRA LIFETIME",
    units="Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_lifetime"},
)
def protra_lifetime():
    return _ext_constant_protra_lifetime()


_ext_constant_protra_lifetime = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "CHINA",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["CHINA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
    },
    "_ext_constant_protra_lifetime",
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EASOC",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["EASOC"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "EU27",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["EU27"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "INDIA",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["INDIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LATAM",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["LATAM"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "LROW",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["LROW"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "RUSSIA",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["RUSSIA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "UK",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["UK"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)

_ext_constant_protra_lifetime.add(
    "model_parameters/energy/energy-transformation.xlsm",
    "USMCA",
    "PROTRA_LIFETIME*",
    {"REGIONS 9 I": ["USMCA"], "NRG PROTRA I": _subscript_dict["NRG PROTRA I"]},
)


@component.add(
    name="PROTRA operative capacity stock selected",
    units="TW",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock": 1},
)
def protra_operative_capacity_stock_selected():
    """
    Selection of the capacity stock for PROTRA: 1: accounting of the age of facilities; 2: one stock
    """
    return protra_capacity_stock()


@component.add(
    name="PROTRA PP solar PV by subtechnology capacity decomissioning",
    units="TW/Year",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning_selected": 2,
        "share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 2,
    },
)
def protra_pp_solar_pv_by_subtechnology_capacity_decomissioning():
    """
    Decomissed solar PV capacity installed by panel subtechnology old equation 1: MAX( capacity stock PROTRA PP solar PV by subtechnology[REGIONS 9 I,PROTRA PP solar open space PV,PROTRA PP SOLAR PV SUBTECHNOLOGIES I ] * ZIDZ( 1 , PROTRA LIFETIME[REGIONS 9 I,PROTRA PP solar open space PV] ) , 0 ) old equation 2: MAX( capacity stock PROTRA PP solar PV by subtechnology[REGIONS 9 I,PROTRA PP solar urban PV,PROTRA PP SOLAR PV SUBTECHNOLOGIES I ] * ZIDZ( 1 , PROTRA LIFETIME[REGIONS 9 I,PROTRA PP solar urban PV] ) , 0 )
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[:, ["PROTRA PP solar open space PV"], :] = (
        np.maximum(
            protra_capacity_decommissioning_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * share_capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA PP solar open space PV", :]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP solar urban PV"], :] = (
        np.maximum(
            protra_capacity_decommissioning_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * share_capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA PP solar urban PV", :]
            .reset_coords(drop=True),
            0,
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="PROTRA PP solar PV by subtechnology capacity expansion",
    units="TW/Year",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_selected": 2,
        "share_new_pv_subtechn_land": 1,
        "share_new_pv_subtechn_urban": 1,
    },
)
def protra_pp_solar_pv_by_subtechnology_capacity_expansion():
    """
    new solar PV capacity installed by panel subtechnology
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[:, ["PROTRA PP solar open space PV"], :] = (
        (
            protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * share_new_pv_subtechn_land()
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP solar urban PV"], :] = (
        (
            protra_capacity_expansion_selected()
            .loc[:, "TO elec", "PROTRA PP solar urban PV"]
            .reset_coords(drop=True)
            * share_new_pv_subtechn_urban()
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="protra priority vector",
    subscripts=["REGIONS 9 I", "NRG PRO I", "pprofile"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pwidth_protra_capacity_expansion_priorities_vector_sp": 1,
        "protra_capacity_expansion_priorities_vector_sp": 1,
        "protra_capacity_expansion_policy_weight_sp": 2,
        "lcoe_by_protra_priority_signal": 1,
        "model_explorer_protra_capacity_expansion": 1,
        "switch_model_explorer": 1,
    },
)
def protra_priority_vector():
    """
    PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP[REGIONS 9 I,NRG PROTRA I]
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
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, :, ["ppriority"]] = True
    except_subs.loc[:, _subscript_dict["NRG PROTRA I"], ["ppriority"]] = False
    value.values[except_subs.values] = 0
    value.loc[:, :, ["pwidth"]] = (
        pwidth_protra_capacity_expansion_priorities_vector_sp()
    )
    value.loc[:, :, ["pextra"]] = 0
    value.loc[:, _subscript_dict["NRG PROTRA I"], ["ppriority"]] = (
        if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_protra_capacity_expansion(),
            lambda: protra_capacity_expansion_policy_weight_sp()
            * protra_capacity_expansion_priorities_vector_sp()
            + (1 - protra_capacity_expansion_policy_weight_sp())
            * lcoe_by_protra_priority_signal(),
        )
        .expand_dims({"pprofile": ["ppriority"]}, 2)
        .values
    )
    return value


@component.add(
    name="PROTRA shortfall allocation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "production_from_chp_expansion": 1,
        "protra_elec_shortfall_allocation": 1,
        "production_from_hp_expansion": 1,
    },
)
def protra_shortfall_allocation():
    """
    Shortfall allocated to PROTRA. Equals the energy production potential of the new production capacity. No-Process processes (gas, hydrogen etc.) are set to 0 (no expansion, as capacity is very big already anyway)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG TO I", "NRG PROTRA I"],
    )
    value.loc[:, :, _subscript_dict["PROTRA CHP I"]] = (
        production_from_chp_expansion().values
    )
    value.loc[:, :, _subscript_dict["PROTRA PP I"]] = (
        protra_elec_shortfall_allocation()
        .loc[:, :, _subscript_dict["PROTRA PP I"]]
        .rename({"NRG PRO I": "PROTRA PP I"})
        .values
    )
    value.loc[:, :, _subscript_dict["PROTRA HP I"]] = (
        production_from_hp_expansion()
        .loc[:, :, _subscript_dict["PROTRA HP I"]]
        .rename({"NRG PRO I": "PROTRA HP I"})
        .values
    )
    value.loc[:, :, _subscript_dict["PROTRA NP I"]] = 0
    return value


@component.add(
    name="PWIDTH PROTRA CAPACITY EXPANSION PRIORITIES VECTOR SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp"
    },
)
def pwidth_protra_capacity_expansion_priorities_vector_sp():
    """
    One of the parameters of the Vensim ALLOCATE_AVAILABLE function used to specify the curves to be used for supply and demand. Note that the priorities and widths specified should all be of the same order of magnitude. For example, it does not make sense to have one priority be 20 and another 2e6 if width is 100.
    """
    return _ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp()


_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "PWIDTH_PROTRA_CAPACITY_EXPANSION_PRIORITIES_VECTOR_SP",
    {},
    _root,
    {},
    "_ext_constant_pwidth_protra_capacity_expansion_priorities_vector_sp",
)


@component.add(
    name="ratio final energy demand to TO avialble by commodity EU27",
    units="TJ/EJ",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_eu27": 7,
        "to_available_by_commodity_eu27": 7,
    },
)
def ratio_final_energy_demand_to_to_avialble_by_commodity_eu27():
    value = xr.DataArray(
        np.nan, {"NRG TO I": _subscript_dict["NRG TO I"]}, ["NRG TO I"]
    )
    value.loc[["TO elec"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE elec"]),
        float(to_available_by_commodity_eu27().loc["TO elec"]),
    )
    value.loc[["TO gas"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE gas"]),
        float(to_available_by_commodity_eu27().loc["TO gas"]),
    )
    value.loc[["TO heat"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE heat"]),
        float(to_available_by_commodity_eu27().loc["TO heat"]),
    )
    value.loc[["TO hydrogen"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE hydrogen"]),
        float(to_available_by_commodity_eu27().loc["TO hydrogen"]),
    )
    value.loc[["TO liquid"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE liquid"]),
        float(to_available_by_commodity_eu27().loc["TO liquid"]),
    )
    value.loc[["TO solid bio"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE solid bio"]),
        float(to_available_by_commodity_eu27().loc["TO solid bio"]),
    )
    value.loc[["TO solid fossil"]] = zidz(
        float(final_energy_demand_by_fe_eu27().loc["FE solid fossil"]),
        float(to_available_by_commodity_eu27().loc["TO solid fossil"]),
    )
    return value


@component.add(
    name="remaining elec shortfall to be allocated",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_shortfall": 1, "production_from_chp_expansion": 1},
)
def remaining_elec_shortfall_to_be_allocated():
    """
    TO_elec quantity that remains to be allocated after deducting CHP-Production.
    """
    return np.maximum(
        to_shortfall().loc[:, "TO elec"].reset_coords(drop=True)
        - sum(
            production_from_chp_expansion()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"PROTRA CHP I": "PROTRA CHP I!"}),
            dim=["PROTRA CHP I!"],
        ),
        0,
    ).expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)


@component.add(
    name="remaining global shortfall after heat allocation",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "remaining_elec_shortfall_to_be_allocated": 1,
        "to_shortfall": 2,
        "protra_heat_shortfall_allocation": 1,
    },
)
def remaining_global_shortfall_after_heat_allocation():
    """
    check variable: remaining global shortfall after heat allocation
    """
    value = xr.DataArray(
        np.nan, {"NRG TO I": _subscript_dict["NRG TO I"]}, ["NRG TO I"]
    )
    value.loc[["TO elec"]] = sum(
        remaining_elec_shortfall_to_be_allocated()
        .loc[:, "TO elec"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    value.loc[["TO heat"]] = sum(
        to_shortfall()
        .loc[:, "TO heat"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    ) - sum(
        protra_heat_shortfall_allocation()
        .loc[:, "TO heat", _subscript_dict["PROTRA CHP HP I"]]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!", "NRG PRO I": "PROTRA CHP HP I!"}),
        dim=["REGIONS 9 I!", "PROTRA CHP HP I!"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["TO elec"]] = False
    except_subs.loc[["TO heat"]] = False
    value.values[except_subs.values] = sum(
        to_shortfall().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    ).values[except_subs.values]
    return value


@component.add(
    name="share capacity stock PROTRA PP solar PV by subtechnology",
    units="1",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capacity_stock_protra_pp_solar_pv_by_subtechnology": 4},
)
def share_capacity_stock_protra_pp_solar_pv_by_subtechnology():
    """
    Share of each subtechnoly solar PV capacity installed respect total PV capacity.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[:, ["PROTRA PP solar open space PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA PP solar open space PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA PP solar open space PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                ),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            ).expand_dims(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP solar urban PV"], :] = (
        zidz(
            capacity_stock_protra_pp_solar_pv_by_subtechnology()
            .loc[:, "PROTRA PP solar urban PV", :]
            .reset_coords(drop=True),
            sum(
                capacity_stock_protra_pp_solar_pv_by_subtechnology()
                .loc[:, "PROTRA PP solar urban PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                ),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            ).expand_dims(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                    ]
                },
                1,
            ),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 1)
        .values
    )
    return value


@component.add(
    name="share PROTRA capacity stock EU27",
    units="DMNL",
    subscripts=["REGIONS EU27 I", "NRG TO I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"protra_capacity_stock_eu27": 2},
)
def share_protra_capacity_stock_eu27():
    """
    Share of PROTRA capacity stock of each EU 27 country with relation to the total EU27.
    """
    return zidz(
        protra_capacity_stock_eu27(),
        sum(
            protra_capacity_stock_eu27().rename({"REGIONS EU27 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ).expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0),
    )


@component.add(
    name="SHARE PV SUBTECHNOLOGIES BEFORE 2020",
    units="DMNL",
    subscripts=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_share_pv_subtechnologies_before_2020",
        "__data__": "_ext_data_share_pv_subtechnologies_before_2020",
        "time": 1,
    },
)
def share_pv_subtechnologies_before_2020():
    """
    historical share data from photovoltaics report (Fraunhofer)
    """
    return _ext_data_share_pv_subtechnologies_before_2020(time())


_ext_data_share_pv_subtechnologies_before_2020 = ExtData(
    "model_parameters/energy/energy-transformation.xlsm",
    "Efficiency_improvements",
    "SHARE_PV_BEFORE_2020_TIME",
    "SHARE_PV_BEFORE_2020",
    "interpolate",
    {
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
        ]
    },
    _root,
    {
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
        ]
    },
    "_ext_data_share_pv_subtechnologies_before_2020",
)


@component.add(
    name="shares TO shortfall by commodity EU27 2nd approach",
    units="1",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_shortfall_by_commodity_eu27_2nd_approach": 2},
)
def shares_to_shortfall_by_commodity_eu27_2nd_approach():
    return zidz(
        to_shortfall_by_commodity_eu27_2nd_approach(),
        sum(
            to_shortfall_by_commodity_eu27_2nd_approach().rename(
                {"REGIONS EU27 I": "REGIONS EU27 MAP I!"}
            ),
            dim=["REGIONS EU27 MAP I!"],
        ).expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0),
    )


@component.add(
    name="stress signal PROTRA curtailed",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_loss_share_stopping_protra_capacity_expansion_sp": 1,
        "variation_cf_curtailed_protra": 1,
    },
)
def stress_signal_protra_curtailed():
    """
    Capacity expansion request falls to 0 when the variation of CF falls to the value of CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP.
    """
    return np.minimum(
        1,
        np.maximum(
            0,
            (0 - 1)
            / (0 - cf_loss_share_stopping_protra_capacity_expansion_sp())
            * variation_cf_curtailed_protra()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True),
        ),
    ).expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)


@component.add(
    name="stress signal uranium scarcity",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_loss_share_stopping_protra_capacity_expansion_sp": 1,
        "variation_cf_nuclear_after_uranium_scarcity": 1,
    },
)
def stress_signal_uranium_scarcity():
    """
    Capacity expansion request falls to 0 when the variation of CF falls to the value of CF_LOSS_SHARE_STOPPING_PROTRA_CAPACITY_EXPANSION_SP.
    """
    return xr.DataArray(
        np.minimum(
            1,
            np.maximum(
                0,
                (0 - 1)
                / (0 - cf_loss_share_stopping_protra_capacity_expansion_sp())
                * variation_cf_nuclear_after_uranium_scarcity(),
            ),
        ),
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG COMMODITIES I": _subscript_dict["NRG COMMODITIES I"],
            "NRG PRO I": _subscript_dict["NRG PRO I"],
        },
        ["REGIONS 9 I", "NRG COMMODITIES I", "NRG PRO I"],
    )


@component.add(
    name="SWITCH LAW2NRG SOLARLAND",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_law2nrg_solarland"},
)
def switch_law2nrg_solarland():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_law2nrg_solarland()


_ext_constant_switch_law2nrg_solarland = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2NRG_SOLARLAND",
    {},
    _root,
    {},
    "_ext_constant_switch_law2nrg_solarland",
)


@component.add(
    name="SWITCH MAT2NRG URANIUM AVAILABILITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_mat2nrg_uranium_availability"},
)
def switch_mat2nrg_uranium_availability():
    """
    This SWITCH can take 2 values: 1: uranium use is constrained by uranium availability in materials module 0: uranium use is unlimited
    """
    return _ext_constant_switch_mat2nrg_uranium_availability()


_ext_constant_switch_mat2nrg_uranium_availability = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2NRG_URANIUM_AVAILABILITY",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2nrg_uranium_availability",
)


@component.add(
    name="TO available by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_operative_capacity_stock_selected": 2,
        "protra_max_full_load_hours_after_constraints": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "chp_capacity_utilization_rate": 1,
    },
)
def to_available_by_commodity():
    """
    max TO that can be produced from existing PROTRA stock; Max heat production is based on max. full load hours (of CHPs and HP). Max elec production is based on ACTUAL full load hours of CHPs (neccesary because of the stepwise allocation approach) and max. full load hours of PP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS 9 I", "NRG TO I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"]] = False
    value.values[except_subs.values] = vector_select(
        protra_operative_capacity_stock_selected().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        (
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG PROTRA I": "NRG PROTRA I!"}
            )
            * unit_conversion_tw_per_ej_per_year()
        ).expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1),
        ["NRG PROTRA I!"],
        0,
        0,
        0,
    ).values[except_subs.values]
    value.loc[:, ["TO elec"]] = (
        vector_select(
            protra_operative_capacity_stock_selected()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG PROTRA I": "NRG PROTRA I!"}
            )
            * chp_capacity_utilization_rate()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"})
            * unit_conversion_tw_per_ej_per_year(),
            ["NRG PROTRA I!"],
            0,
            0,
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO available by commodity by country EU27",
    units="EJ/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock_eu27": 2,
        "protra_max_full_load_hours_after_constraints": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "chp_capacity_utilization_rate": 1,
    },
)
def to_available_by_commodity_by_country_eu27():
    """
    max TO that can be produced from existing PROTRA stock; Max heat production is based on max. full load hours (of CHPs and HP). Max elec production is based on ACTUAL full load hours of CHPs (neccesary because of the stepwise allocation approach) and max. full load hours of PP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS EU27 I", "NRG TO I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"]] = False
    value.values[except_subs.values] = vector_select(
        protra_capacity_stock_eu27().rename({"NRG PROTRA I": "NRG PROTRA I!"}),
        (
            protra_max_full_load_hours_after_constraints()
            .loc["EU27", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"})
            * unit_conversion_tw_per_ej_per_year()
        )
        .expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0)
        .expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1),
        ["NRG PROTRA I!"],
        0,
        0,
        0,
    ).values[except_subs.values]
    value.loc[:, ["TO elec"]] = (
        vector_select(
            protra_capacity_stock_eu27()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            (
                protra_max_full_load_hours_after_constraints()
                .loc["EU27", :]
                .reset_coords(drop=True)
                .rename({"NRG PROTRA I": "NRG PROTRA I!"})
                * chp_capacity_utilization_rate()
                .loc["EU27", "TO elec", :]
                .reset_coords(drop=True)
                .rename({"NRG PROTRA I": "NRG PROTRA I!"})
                * unit_conversion_tw_per_ej_per_year()
            ).expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0),
            ["NRG PROTRA I!"],
            0,
            0,
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO available by commodity by country EU27 2nd approach",
    units="EJ/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock_eu27_2nd_approach": 2,
        "protra_max_full_load_hours_after_constraints": 2,
        "unit_conversion_tw_per_ej_per_year": 2,
        "chp_capacity_utilization_rate": 1,
    },
)
def to_available_by_commodity_by_country_eu27_2nd_approach():
    """
    max TO that can be produced from existing PROTRA stock; Max heat production is based on max. full load hours (of CHPs and HP). Max elec production is based on ACTUAL full load hours of CHPs (neccesary because of the stepwise allocation approach) and max. full load hours of PP.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS EU27 I", "NRG TO I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["TO elec"]] = False
    value.values[except_subs.values] = vector_select(
        protra_capacity_stock_eu27_2nd_approach().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        (
            protra_max_full_load_hours_after_constraints()
            .loc["EU27", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"})
            * unit_conversion_tw_per_ej_per_year()
        )
        .expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0)
        .expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1),
        ["NRG PROTRA I!"],
        0,
        0,
        0,
    ).values[except_subs.values]
    value.loc[:, ["TO elec"]] = (
        vector_select(
            protra_capacity_stock_eu27_2nd_approach()
            .loc[:, "TO elec", :]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "NRG PROTRA I!"}),
            (
                protra_max_full_load_hours_after_constraints()
                .loc["EU27", :]
                .reset_coords(drop=True)
                .rename({"NRG PROTRA I": "NRG PROTRA I!"})
                * chp_capacity_utilization_rate()
                .loc["EU27", "TO elec", :]
                .reset_coords(drop=True)
                .rename({"NRG PROTRA I": "NRG PROTRA I!"})
                * unit_conversion_tw_per_ej_per_year()
            ).expand_dims({"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]}, 0),
            ["NRG PROTRA I!"],
            0,
            0,
            0,
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO available by commodity EU27",
    units="EJ/Year",
    subscripts=["NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_available_by_commodity": 1},
)
def to_available_by_commodity_eu27():
    return to_available_by_commodity().loc["EU27", :].reset_coords(drop=True)


@component.add(
    name="TO decomissioned by commodity",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning_selected": 1,
        "protra_max_full_load_hours_after_constraints": 1,
        "unit_conversion_tw_per_ej_per_year": 1,
    },
)
def to_decomissioned_by_commodity():
    """
    TO that is missing in the next year because of decomissioned PROTRA capacities
    """
    return vector_select(
        protra_capacity_decommissioning_selected().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        (
            protra_max_full_load_hours_after_constraints().rename(
                {"NRG PROTRA I": "NRG PROTRA I!"}
            )
            * unit_conversion_tw_per_ej_per_year()
        ).expand_dims({"NRG TO I": _subscript_dict["NRG TO I"]}, 1),
        ["NRG PROTRA I!"],
        0,
        0,
        0,
    )


@component.add(
    name="TO required",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_by_commodity": 1, "applied_to_reserve_factor_by_commodity": 1},
)
def to_required():
    """
    TO required including overcapacity to account for next timesteps growth
    """
    return to_by_commodity() * applied_to_reserve_factor_by_commodity()


@component.add(
    name="TO required by commodity EU27",
    units="EJ/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_35r": 7,
        "ratio_final_energy_demand_to_to_avialble_by_commodity_eu27": 7,
    },
)
def to_required_by_commodity_eu27():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"],
            "NRG TO I": _subscript_dict["NRG TO I"],
        },
        ["REGIONS EU27 I", "NRG TO I"],
    )
    value.loc[:, ["TO elec"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE elec"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO elec"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .values
    )
    value.loc[:, ["TO gas"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE gas"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO gas"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO gas"]}, 1)
        .values
    )
    value.loc[:, ["TO heat"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE heat"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO heat"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO heat"]}, 1)
        .values
    )
    value.loc[:, ["TO hydrogen"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE hydrogen"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO hydrogen"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO hydrogen"]}, 1)
        .values
    )
    value.loc[:, ["TO liquid"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE liquid"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO liquid"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO liquid"]}, 1)
        .values
    )
    value.loc[:, ["TO solid bio"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE solid bio"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO solid bio"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid bio"]}, 1)
        .values
    )
    value.loc[:, ["TO solid fossil"]] = (
        zidz(
            final_energy_demand_by_fe_35r()
            .loc[_subscript_dict["REGIONS EU27 I"], "FE solid fossil"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
            float(
                ratio_final_energy_demand_to_to_avialble_by_commodity_eu27().loc[
                    "TO solid fossil"
                ]
            ),
        )
        .expand_dims({"NRG COMMODITIES I": ["TO solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="TO shortfall",
    units="EJ/Year",
    subscripts=["REGIONS 9 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"to_required": 1, "to_available_by_commodity": 1},
)
def to_shortfall():
    """
    Additional TO that needs to be provided to account for current demand (in time t) and additional demand for decomissioned capacities and demand growth (in t+1)
    """
    return np.maximum(0, to_required() - to_available_by_commodity())


@component.add(
    name="TO shortfall by commodity EU27",
    units="EJ/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_required_by_commodity_eu27": 1,
        "to_available_by_commodity_by_country_eu27": 1,
    },
)
def to_shortfall_by_commodity_eu27():
    return np.maximum(
        to_required_by_commodity_eu27() - to_available_by_commodity_by_country_eu27(), 0
    )


@component.add(
    name="TO shortfall by commodity EU27 2nd approach",
    units="EJ/Year",
    subscripts=["REGIONS EU27 I", "NRG TO I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "to_required_by_commodity_eu27": 1,
        "to_available_by_commodity_by_country_eu27_2nd_approach": 1,
    },
)
def to_shortfall_by_commodity_eu27_2nd_approach():
    return np.maximum(
        to_required_by_commodity_eu27()
        - to_available_by_commodity_by_country_eu27_2nd_approach(),
        0,
    )
