"""
Module energyend_use.total_energy_demand
Translated using PySD version 3.13.4
"""

@component.add(
    name="adjustment factor estimate final energy substitution component 2015",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"estimate_final_energy_substitution_component_2015": 1},
)
def adjustment_factor_estimate_final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Sum of the first estimation of the final energy substitution by sector and final energy in 2015 to normalize this variable.
    """
    return sum(
        estimate_final_energy_substitution_component_2015().rename(
            {"NRG FE I": "NRG FE I!"}
        ),
        dim=["NRG FE I!"],
    )


@component.add(
    name="BASE FE PRICES",
    units="DMNL",
    subscripts=["NRG FE I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def base_fe_prices():
    """
    Default final energy price development variable. Used only when SWITCH_ECO2NRG_PRICE_OUTPUT is deactivated. (When switch is activated, the endogenous price from economy-module is used) (Note: Index, 2015=100).
    """
    return xr.DataArray(1, {"NRG FE I": _subscript_dict["NRG FE I"]}, ["NRG FE I"])


@component.add(
    name="delayed final energy substitution component",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_final_energy_substitution_component": 1},
    other_deps={
        "_delayfixed_delayed_final_energy_substitution_component": {
            "initial": {"final_energy_substitution_component_2015": 1, "time_step": 1},
            "step": {"final_energy_substitution_component": 1},
        }
    },
)
def delayed_final_energy_substitution_component():
    return _delayfixed_delayed_final_energy_substitution_component()


_delayfixed_delayed_final_energy_substitution_component = DelayFixed(
    lambda: final_energy_substitution_component(),
    lambda: time_step(),
    lambda: final_energy_substitution_component_2015(),
    time_step,
    "_delayfixed_delayed_final_energy_substitution_component",
)


@component.add(
    name="elec by sector FE and output",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "FINAL ENERGY TRANSMISSION I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_final_energy_demand_by_sector_and_fe": 1,
        "total_final_energy_intensities_by_sector": 1,
    },
)
def elec_by_sector_fe_and_output():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Electricy intensity by sector assuming the shame shares that in energy demand.
    """
    return (
        share_final_energy_demand_by_sector_and_fe()
        .loc[:, :, "FE elec"]
        .reset_coords(drop=True)
        * total_final_energy_intensities_by_sector()
    ).expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 2)


@component.add(
    name="energy efficiency annual improvement",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_energy_efficiency_anual_improvement": 1,
        "start_year_final_energy_efficiency_rate_top_down_sectors_sp": 1,
        "historical_energy_efficiency_annual_improvement": 1,
        "final_energy_efficiency_rate_top_down_sectors_sp": 1,
        "time": 1,
    },
)
def energy_efficiency_annual_improvement():
    """
    Energy efficiency annual improvement by sector and final energy as a function of the historical trends and exogenous policies.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_energy_efficiency_anual_improvement(),
        lambda: if_then_else(
            time() < start_year_final_energy_efficiency_rate_top_down_sectors_sp(),
            lambda: historical_energy_efficiency_annual_improvement(),
            lambda: final_energy_efficiency_rate_top_down_sectors_sp(),
        ),
    )


@component.add(
    name="energy efficiency component",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_energy_efficiency_component": 1},
    other_deps={
        "_integ_energy_efficiency_component": {
            "initial": {"energy_efficiengy_component_2015": 3},
            "step": {"variation_energy_efficiency_component": 1},
        }
    },
)
def energy_efficiency_component():
    """
    Energy efficiency by sector and final energy estimated with a top-down approach
    """
    return _integ_energy_efficiency_component()


_integ_energy_efficiency_component = Integ(
    lambda: variation_energy_efficiency_component(),
    lambda: if_then_else(
        energy_efficiengy_component_2015() == 0,
        lambda: energy_efficiengy_component_2015()
        .loc[:, :, "FE elec"]
        .reset_coords(drop=True)
        .expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 2),
        lambda: energy_efficiengy_component_2015(),
    ),
    "_integ_energy_efficiency_component",
)


@component.add(
    name="energy efficiengy component 2015",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_intensities_by_sector_and_fe": 1,
        "adjustment_factor_estimate_final_energy_substitution_component_2015": 1,
        "estimate_final_energy_demand_by_sector_fe_and_output_2015": 1,
    },
)
def energy_efficiengy_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the energy efficiency by sector and final energy in 2015
    """
    return if_then_else(
        final_energy_intensities_by_sector_and_fe() <= 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                "NRG FE I": _subscript_dict["NRG FE I"],
            },
            ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
        ),
        lambda: estimate_final_energy_demand_by_sector_fe_and_output_2015()
        * adjustment_factor_estimate_final_energy_substitution_component_2015(),
    )


@component.add(
    name="estimate final energy demand by sector FE and output 2015",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"elec_by_sector_fe_and_output": 1, "relative_energy_intensity_2015": 1},
)
def estimate_final_energy_demand_by_sector_fe_and_output_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the final energy demand by sector and final energy in 2015 used to disaggregate the two components.
    """
    return elec_by_sector_fe_and_output().loc[:, :, "FE elec"].reset_coords(
        drop=True
    ) * relative_energy_intensity_2015().loc[
        _subscript_dict["SECTORS NON ENERGY I"], :
    ].rename(
        {"SECTORS I": "SECTORS NON ENERGY I"}
    )


@component.add(
    name="estimate final energy substitution component 2015",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_intensities_by_sector_and_fe": 1,
        "estimate_final_energy_demand_by_sector_fe_and_output_2015": 1,
    },
)
def estimate_final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. First estimation of the final energy substitution by sector and final energy in 2015 (non-normalized).
    """
    return zidz(
        final_energy_intensities_by_sector_and_fe(),
        estimate_final_energy_demand_by_sector_fe_and_output_2015(),
    )


@component.add(
    name="final energy demand by FE 35R",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 1,
        "households_final_energy_demand_by_fe": 1,
    },
)
def final_energy_demand_by_fe_35r():
    """
    Final energy demand by final energy 35 regions
    """
    return (
        sum(
            final_energy_demand_by_sector_and_fe().rename(
                {"SECTORS NON ENERGY I": "SECTORS NON ENERGY I!"}
            ),
            dim=["SECTORS NON ENERGY I!"],
        )
        + households_final_energy_demand_by_fe()
    )


@component.add(
    name="final energy demand by FE 9R",
    units="TJ/Year",
    subscripts=["REGIONS 9 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_fe_eu27": 1,
        "final_energy_demand_by_fe_35r": 1,
    },
)
def final_energy_demand_by_fe_9r():
    """
    Final energy demand by final energy 9 regions (not including non-energy uses).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 9 I", "NRG FE I"],
    )
    value.loc[["EU27"], :] = (
        final_energy_demand_by_fe_eu27()
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    return value


@component.add(
    name="final energy demand by FE EU27",
    units="TJ/Year",
    subscripts=["NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_fe_35r": 1},
)
def final_energy_demand_by_fe_eu27():
    """
    Final energy demand by final energy EU27
    """
    return sum(
        final_energy_demand_by_fe_35r()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )


@component.add(
    name="final energy demand by sector and FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "final_energy_intensities_by_sector_and_fe": 3,
        "base_output_real": 2,
        "switch_eco2nrg_output_real": 1,
        "output_real": 1,
    },
)
def final_energy_demand_by_sector_and_fe():
    """
    Final energy demand by sector and final energy estimated with a top-down approach
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: final_energy_intensities_by_sector_and_fe()
        * base_output_real()
        .loc[:, _subscript_dict["SECTORS NON ENERGY I"]]
        .rename({"SECTORS I": "SECTORS NON ENERGY I"}),
        lambda: if_then_else(
            switch_eco2nrg_output_real() == 0,
            lambda: final_energy_intensities_by_sector_and_fe()
            * base_output_real()
            .loc[:, _subscript_dict["SECTORS NON ENERGY I"]]
            .rename({"SECTORS I": "SECTORS NON ENERGY I"}),
            lambda: final_energy_intensities_by_sector_and_fe()
            * output_real()
            .loc[:, _subscript_dict["SECTORS NON ENERGY I"]]
            .rename({"SECTORS I": "SECTORS NON ENERGY I"}),
        ),
    )


@component.add(
    name="FINAL ENERGY EFFICIENCY RATE TOP DOWN SECTORS SP",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_final_energy_efficiency_rate_top_down_sectors_sp"
    },
)
def final_energy_efficiency_rate_top_down_sectors_sp():
    """
    Energy effiency annual improvement policy
    """
    return _ext_constant_final_energy_efficiency_rate_top_down_sectors_sp()


_ext_constant_final_energy_efficiency_rate_top_down_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "FINAL_ENERGY_EFFICIENCY_RATE_TOP_DOWN_SECTORS_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_final_energy_efficiency_rate_top_down_sectors_sp",
)


@component.add(
    name="final energy intensities by sector and FE",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_final_energy_intensities_by_sector_and_fe": 1},
    other_deps={
        "_integ_final_energy_intensities_by_sector_and_fe": {
            "initial": {"historical_energy_intensities_top_down_by_sector_and_fe": 1},
            "step": {"variation_energy_intensity_by_sector_and_fe": 1},
        }
    },
)
def final_energy_intensities_by_sector_and_fe():
    """
    Final energy intensities by sector and final energy estimated with a top-down approach
    """
    return _integ_final_energy_intensities_by_sector_and_fe()


_integ_final_energy_intensities_by_sector_and_fe = Integ(
    lambda: variation_energy_intensity_by_sector_and_fe()
    .loc[:, _subscript_dict["SECTORS NON ENERGY I"], :]
    .rename({"SECTORS I": "SECTORS NON ENERGY I"}),
    lambda: historical_energy_intensities_top_down_by_sector_and_fe()
    .loc[:, _subscript_dict["SECTORS NON ENERGY I"], :]
    .rename({"SECTORS I": "SECTORS NON ENERGY I"}),
    "_integ_final_energy_intensities_by_sector_and_fe",
)


@component.add(
    name="final energy substituion annual variation",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 7,
        "trend_of_final_energy_substituion_annual_variation": 8,
        "price_final_energy": 9,
        "switch_law2nrg_available_forestry_products_for_industry": 1,
        "switch_energy": 1,
        "signal_availability_forestry_products_for_energy_35r": 1,
        "switch_nrg_limited_res_potentials": 1,
    },
)
def final_energy_substituion_annual_variation():
    """
    Estimated final energy annunal substitution by sector and final energy as a function of the historical trends, the final energy prioces and exogenous policies. (not normalized)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    )
    value.loc[:, :, ["FE elec"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE elec"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"]}, 1
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 2)
        .values
    )
    value.loc[:, :, ["FE gas"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE gas"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True)
                - price_final_energy().loc[:, :, "FE gas"].reset_coords(drop=True),
            )
            / price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, :, ["FE heat"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE heat"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"]}, 1
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 2)
        .values
    )
    value.loc[:, :, ["FE hydrogen"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE hydrogen"]
            .reset_coords(drop=True),
        )
        .expand_dims(
            {"SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"]}, 1
        )
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 2)
        .values
    )
    value.loc[:, :, ["FE liquid"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE liquid"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True)
                - price_final_energy().loc[:, :, "FE liquid"].reset_coords(drop=True),
            )
            / price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, :, ["FE solid bio"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
            lambda: if_then_else(
                np.logical_or(
                    switch_energy() == 0,
                    np.logical_or(
                        switch_law2nrg_available_forestry_products_for_industry() == 0,
                        switch_nrg_limited_res_potentials() == 0,
                    ),
                ),
                lambda: trend_of_final_energy_substituion_annual_variation()
                .loc[:, "FE solid bio"]
                .reset_coords(drop=True),
                lambda: trend_of_final_energy_substituion_annual_variation()
                .loc[:, "FE solid bio"]
                .reset_coords(drop=True)
                + (signal_availability_forestry_products_for_energy_35r() - 1),
            ),
        )
        .expand_dims(
            {"SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"]}, 1
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 2)
        .values
    )
    value.loc[:, :, ["FE solid fossil"]] = (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: trend_of_final_energy_substituion_annual_variation()
            .loc[:, "FE solid fossil"]
            .reset_coords(drop=True)
            + np.minimum(
                0,
                price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True)
                - price_final_energy()
                .loc[:, :, "FE solid fossil"]
                .reset_coords(drop=True),
            )
            / price_final_energy().loc[:, :, "FE elec"].reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="final energy substitution component",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_final_energy_substitution_component": 1},
    other_deps={
        "_integ_final_energy_substitution_component": {
            "initial": {"final_energy_substitution_component_2015": 1},
            "step": {"variation_final_energy_substitution_component": 1},
        }
    },
)
def final_energy_substitution_component():
    """
    Final energy substitution by sector and final energy estimated with a top-down approach
    """
    return _integ_final_energy_substitution_component()


_integ_final_energy_substitution_component = Integ(
    lambda: variation_final_energy_substitution_component(),
    lambda: final_energy_substitution_component_2015(),
    "_integ_final_energy_substitution_component",
)


@component.add(
    name="final energy substitution component 2015",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "estimate_final_energy_substitution_component_2015": 1,
        "adjustment_factor_estimate_final_energy_substitution_component_2015": 1,
    },
)
def final_energy_substitution_component_2015():
    """
    Auxiliary variable used in the method to disaggregate in 2015 the two components of the final energy intensity: energy efficiency and final energy substitution. Estimation of the final energy substitution by sector and final energy in 2015
    """
    return zidz(
        estimate_final_energy_substitution_component_2015(),
        adjustment_factor_estimate_final_energy_substitution_component_2015().expand_dims(
            {"NRG FE I": _subscript_dict["NRG FE I"]}, 2
        ),
    )


@component.add(
    name="final energy substitution component aux",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_final_energy_substitution_component": 2,
        "time_step": 1,
        "final_energy_substituion_annual_variation": 1,
    },
)
def final_energy_substitution_component_aux():
    """
    Auxiliary variable to normalize the final energy annual substitution by sector and final energy. Bounded [0,1].
    """
    return np.maximum(
        0,
        np.minimum(
            1,
            delayed_final_energy_substitution_component()
            + final_energy_substituion_annual_variation()
            * delayed_final_energy_substitution_component()
            * time_step(),
        ),
    )


@component.add(
    name="FINAL ENERGY SUBSTITUTION RATE TOP DOWN SECTORS SP",
    units="1/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_final_energy_substitution_rate_top_down_sectors_sp"
    },
)
def final_energy_substitution_rate_top_down_sectors_sp():
    """
    Final energy substitution policy
    """
    return _ext_constant_final_energy_substitution_rate_top_down_sectors_sp()


_ext_constant_final_energy_substitution_rate_top_down_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "FINAL_ENERGY_SUBSTITUTION_RATE_TOP_DOWN_SECTORS_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_final_energy_substitution_rate_top_down_sectors_sp",
)


@component.add(
    name="HISTORICAL ENERGY EFFICIENCY ANNUAL IMPROVEMENT",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_energy_efficiency_annual_improvement"
    },
)
def historical_energy_efficiency_annual_improvement():
    """
    Historical energy effiency annual variation form IEA balances 2000-2015 (no difference between sectors).
    """
    return _ext_constant_historical_energy_efficiency_annual_improvement()


_ext_constant_historical_energy_efficiency_annual_improvement = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Hist_energy_intensity_variation",
    "HISTORIC_ENERGY_EFFICIENCY_IMPROVEMENT*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_historical_energy_efficiency_annual_improvement",
)


@component.add(
    name="HISTORICAL FINAL ENERGY SUBSTITUTION",
    units="1/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_historical_final_energy_substitution"},
)
def historical_final_energy_substitution():
    """
    Historical final energy annual substitution form IEA balances 2000-2015 (no difference between sectors).
    """
    return _ext_constant_historical_final_energy_substitution()


_ext_constant_historical_final_energy_substitution = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Hist_energy_intensity_variation",
    "HISTORIC_FINAL_ENERGY_SUBSTITUTION",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_historical_final_energy_substitution",
)


@component.add(
    name="households final energy demand buildings by FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "imv_final_energy_consumption_buildings_households": 6,
        "share_energy_consumption_solid_bio_vs_solid_fossil": 2,
    },
)
def households_final_energy_demand_buildings_by_fe():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "NRG FE I"],
    )
    value.loc[:, ["FE elec"]] = (
        imv_final_energy_consumption_buildings_households()
        .loc[:, "HH ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[:, ["FE gas"]] = (
        imv_final_energy_consumption_buildings_households()
        .loc[:, "HH GAS"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[:, ["FE heat"]] = (
        imv_final_energy_consumption_buildings_households()
        .loc[:, "HH HEAT"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 1)
        .values
    )
    value.loc[:, ["FE hydrogen"]] = 0
    value.loc[:, ["FE liquid"]] = (
        imv_final_energy_consumption_buildings_households()
        .loc[:, "HH LIQUID FUELS"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[:, ["FE solid bio"]] = (
        (
            imv_final_energy_consumption_buildings_households()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * share_energy_consumption_solid_bio_vs_solid_fossil()
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid bio"]}, 1)
        .values
    )
    value.loc[:, ["FE solid fossil"]] = (
        (
            imv_final_energy_consumption_buildings_households()
            .loc[:, "HH SOLID FUELS"]
            .reset_coords(drop=True)
            * (1 - share_energy_consumption_solid_bio_vs_solid_fossil())
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 1)
        .values
    )
    return value


@component.add(
    name="households final energy demand by FE",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "initial_final_energy_consumption_households_by_fe": 1,
        "households_final_energy_demand_buildings_by_fe": 1,
        "households_final_energy_demand_transport_by_fe": 1,
    },
)
def households_final_energy_demand_by_fe():
    """
    Households final energy demand by final energy.
    """
    return if_then_else(
        switch_energy() == 0,
        lambda: initial_final_energy_consumption_households_by_fe(),
        lambda: households_final_energy_demand_transport_by_fe()
        .loc[_subscript_dict["REGIONS 35 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 35 I"})
        + households_final_energy_demand_buildings_by_fe(),
    )


@component.add(
    name="households final energy demand transport by FE",
    units="TJ/Year",
    subscripts=["REGIONS 36 I", "NRG FE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"imv_final_energy_consumption_transport_households": 3},
)
def households_final_energy_demand_transport_by_fe():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 36 I", "NRG FE I"],
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE elec"]] = (
        imv_final_energy_consumption_transport_households()
        .loc[:, "HH ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE gas"]] = (
        imv_final_energy_consumption_transport_households()
        .loc[:, "HH GAS"]
        .reset_coords(drop=True)
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE heat"]] = 0
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE hydrogen"]] = 0
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE liquid"]] = (
        imv_final_energy_consumption_transport_households()
        .loc[:, "HH FUEL TRANSPORT"]
        .reset_coords(drop=True)
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["FE solid bio"]] = 0
    value.loc[:, ["FE solid fossil"]] = 0
    return value


@component.add(
    name="IMV HISTORIC HOUSEHOLDS FINAL ENERGY",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_imv_historic_households_final_energy"},
)
def imv_historic_households_final_energy():
    """
    Data of final energy consumption in households in 2015
    """
    return _ext_constant_imv_historic_households_final_energy()


_ext_constant_imv_historic_households_final_energy = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Households_final_energy",
    "HISTORIC_HOUSEHOLDS_FINAL_ENERGY",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_imv_historic_households_final_energy",
)


@component.add(
    name="MINIMUM ENERGY EFFICIENCY VERSUS INITIAL",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def minimum_energy_efficiency_versus_initial():
    """
    Minimum value that the energy efficiency for each economic sector could reach, obviously always above zero. This minimum value is very difficult to estimate, but based on historical values it has been considered that it can reach 30% of the value of 2009. (Capellán-Pérez et al., 2014)
    """
    return xr.DataArray(
        0.3,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    )


@component.add(
    name="price final energy",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 7,
        "switch_eco2nrg_price_fe_intensities_substitution": 7,
        "base_fe_prices": 8,
        "imv_final_energy_price_purchaser_price_sectors_with_co2_tax": 6,
    },
)
def price_final_energy():
    """
    Price by final energy obtaining for the price output corresponding sector: FE_elec: DISTRIBUTION_ELECTRICITY FE_gas: DISTRIBUTION_GAS FE_heat: STEAM_HOT_WATER FE_hydrogen: HYDROGEN_PRODUCTION FE_liquid: RFINING FE_solid_bio FE_solid_fossil:MINING_COAL
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    )
    value.loc[:, :, ["FE elec"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE elec"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "DISTRIBUTION ELECTRICITY", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE elec"]}, 2)
        .values
    )
    value.loc[:, :, ["FE gas"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE gas"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "DISTRIBUTION GAS", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE gas"]}, 2)
        .values
    )
    value.loc[:, :, ["FE heat"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE heat"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "STEAM HOT WATER", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"FINAL ENERGY TRANSMISSION I": ["FE heat"]}, 2)
        .values
    )
    value.loc[:, :, ["FE hydrogen"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE hydrogen"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "HYDROGEN PRODUCTION", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE hydrogen"]}, 2)
        .values
    )
    value.loc[:, :, ["FE liquid"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE liquid"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "REFINING", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE liquid"]}, 2)
        .values
    )
    value.loc[:, :, ["FE solid bio"]] = if_then_else(
        np.logical_or(
            switch_energy() == 0,
            switch_eco2nrg_price_fe_intensities_substitution() == 0,
        ),
        lambda: float(base_fe_prices().loc["FE solid bio"]),
        lambda: float(base_fe_prices().loc["FE solid bio"]),
    )
    value.loc[:, :, ["FE solid fossil"]] = (
        if_then_else(
            np.logical_or(
                switch_energy() == 0,
                switch_eco2nrg_price_fe_intensities_substitution() == 0,
            ),
            lambda: xr.DataArray(
                float(base_fe_prices().loc["FE solid fossil"]),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                },
                ["REGIONS 35 I", "SECTORS NON ENERGY I"],
            ),
            lambda: imv_final_energy_price_purchaser_price_sectors_with_co2_tax()
            .loc[:, "MINING COAL", :]
            .reset_coords(drop=True),
        )
        .expand_dims({"NRG COMMODITIES I": ["FE solid fossil"]}, 2)
        .values
    )
    return value


@component.add(
    name="RELATIVE ENERGY INTENSITY 2015",
    units="DMNL",
    subscripts=["SECTORS I", "NRG FE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_relative_energy_intensity_2015"},
)
def relative_energy_intensity_2015():
    """
    Exogenous variable that estimates the final energy intensity ratio beetween the different final energies. These data are the key to the disaggregation in 2015 between the two components of the final energy intensity: energy efficiency and final energy substitution. The data are provisional and should be updated in the next WILIAM version.
    """
    return _ext_constant_relative_energy_intensity_2015()


_ext_constant_relative_energy_intensity_2015 = ExtConstant(
    "model_parameters/energy/energy-end_use-sector_intensities.xlsx",
    "Relative_energy_intensity_2015",
    "RELATIVE_ENERGY_INTENSITY_2015",
    {
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    _root,
    {
        "SECTORS I": _subscript_dict["SECTORS I"],
        "NRG FE I": _subscript_dict["NRG FE I"],
    },
    "_ext_constant_relative_energy_intensity_2015",
)


@component.add(
    name="SELECT FINAL ENERGY SUBSTITUTION RATE TOP DOWN SECTORS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_final_energy_substitution_rate_top_down_sectors_sp"
    },
)
def select_final_energy_substitution_rate_top_down_sectors_sp():
    """
    Select final energy substitution policy option: 0: No final energy substitution 1: Final energy substitution follows historical trends* 2: Final energy substitution defined by user: FINAL ENERGY SUBSTITUTION* *The evolution of the final energy substitution is not only exogenous defiened by those variables, it also depends endogenously on the final energy prices
    """
    return _ext_constant_select_final_energy_substitution_rate_top_down_sectors_sp()


_ext_constant_select_final_energy_substitution_rate_top_down_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_FINAL_ENERGY_SUBSTITUTION_RATE_TOP_DOWN_SECTORS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_final_energy_substitution_rate_top_down_sectors_sp",
)


@component.add(
    name="share final energy demand by sector and FE",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_demand_by_sector_and_fe": 1,
        "total_final_energy_demand_by_sector": 1,
    },
)
def share_final_energy_demand_by_sector_and_fe():
    """
    Share of each final enegy demand in the total final energy demand by sector
    """
    return zidz(
        final_energy_demand_by_sector_and_fe(),
        total_final_energy_demand_by_sector().expand_dims(
            {"NRG FE I": _subscript_dict["NRG FE I"]}, 2
        ),
    )


@component.add(
    name="signal availability forestry products for energy 35R",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"signal_availability_forestry_products_for_energy": 2},
)
def signal_availability_forestry_products_for_energy_35r():
    value = xr.DataArray(
        np.nan, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    )
    value.loc[_subscript_dict["REGIONS EU27 I"]] = float(
        signal_availability_forestry_products_for_energy().loc["EU27"]
    )
    value.loc[_subscript_dict["REGIONS 8 I"]] = (
        signal_availability_forestry_products_for_energy()
        .loc[_subscript_dict["REGIONS 8 I"]]
        .rename({"REGIONS 9 I": "REGIONS 8 I"})
        .values
    )
    return value


@component.add(
    name="START YEAR FINAL ENERGY EFFICIENCY RATE TOP DOWN SECTORS SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_final_energy_efficiency_rate_top_down_sectors_sp"
    },
)
def start_year_final_energy_efficiency_rate_top_down_sectors_sp():
    """
    Start year energy effiency annual improvement policy
    """
    return _ext_constant_start_year_final_energy_efficiency_rate_top_down_sectors_sp()


_ext_constant_start_year_final_energy_efficiency_rate_top_down_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "START_YEAR_FINAL_ENERGY_EFFICIENCY_RATE_TOP_DOWN_SECTORS_SP",
    {},
    _root,
    {},
    "_ext_constant_start_year_final_energy_efficiency_rate_top_down_sectors_sp",
)


@component.add(
    name="START YEAR FINAL ENERGY SUBSTITUTION RATE TOP DOWN SECTORS SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_final_energy_substitution_rate_top_down_sectors_sp"
    },
)
def start_year_final_energy_substitution_rate_top_down_sectors_sp():
    """
    Start year final energy subsitution policy
    """
    return _ext_constant_start_year_final_energy_substitution_rate_top_down_sectors_sp()


_ext_constant_start_year_final_energy_substitution_rate_top_down_sectors_sp = (
    ExtConstant(
        "scenario_parameters/scenario_parameters.xlsx",
        "energy",
        "START_YEAR_FINAL_ENERGY_SUBSTITUTION_RATE_TOP_DOWN_SECTORS_SP",
        {},
        _root,
        {},
        "_ext_constant_start_year_final_energy_substitution_rate_top_down_sectors_sp",
    )
)


@component.add(
    name="SWITCH ECO2NRG OUTPUT REAL",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2nrg_output_real"},
)
def switch_eco2nrg_output_real():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM
    """
    return _ext_constant_switch_eco2nrg_output_real()


_ext_constant_switch_eco2nrg_output_real = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_OUTPUT_REAL",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_output_real",
)


@component.add(
    name="SWITCH ECO2NRG PRICE FE INTENSITIES SUBSTITUTION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco2nrg_price_fe_intensities_substitution"
    },
)
def switch_eco2nrg_price_fe_intensities_substitution():
    """
    Shift to allow endogenizing the substitution of final energies depending on the evolution of their relative price: 1: final energy prices influence the final energy intensities substitution 0: final energy prices do not influence the final energy intensities substitution
    """
    return _ext_constant_switch_eco2nrg_price_fe_intensities_substitution()


_ext_constant_switch_eco2nrg_price_fe_intensities_substitution = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_PRICE_FE_INTENSITIES_SUBSTITUTION",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_price_fe_intensities_substitution",
)


@component.add(
    name="SWITCH ENERGY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_energy"},
)
def switch_energy():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_energy()


_ext_constant_switch_energy = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ENERGY",
    {},
    _root,
    {},
    "_ext_constant_switch_energy",
)


@component.add(
    name="SWITCH LAW2NRG AVAILABLE FORESTRY PRODUCTS FOR INDUSTRY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_law2nrg_available_forestry_products_for_industry"
    },
)
def switch_law2nrg_available_forestry_products_for_industry():
    """
    =1:available forestry products for industry energy use affects the final energy intensities =0:final energy intensites are not affected by available forestry for industry energy use
    """
    return _ext_constant_switch_law2nrg_available_forestry_products_for_industry()


_ext_constant_switch_law2nrg_available_forestry_products_for_industry = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_LAW2NRG_LIMIT_FORESTRY_PRODUCTS_FOR_INDUSTRY_ENERGY",
    {},
    _root,
    {},
    "_ext_constant_switch_law2nrg_available_forestry_products_for_industry",
)


@component.add(
    name="total FES",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_substitution_component": 1},
)
def total_fes():
    """
    Total final energy substitution by sector and final energy estimated with a top-down approach
    """
    return sum(
        final_energy_substitution_component().rename({"NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    ).expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 2)


@component.add(
    name="total final energy demand by sector",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_demand_by_sector_and_fe": 1},
)
def total_final_energy_demand_by_sector():
    """
    Final energy demand by sector estimated with a top-down approach
    """
    return sum(
        final_energy_demand_by_sector_and_fe().rename({"NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    )


@component.add(
    name="total final energy intensities by sector",
    units="TJ/million$",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_energy_intensities_by_sector_and_fe": 1},
)
def total_final_energy_intensities_by_sector():
    """
    Final energy intensities by sector estimated with a top-down approach
    """
    return sum(
        final_energy_intensities_by_sector_and_fe().rename({"NRG FE I": "NRG FE I!"}),
        dim=["NRG FE I!"],
    )


@component.add(
    name="trend of final energy substituion annual variation",
    units="1/Year",
    subscripts=["REGIONS 35 I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "final_energy_substitution_rate_top_down_sectors_sp": 1,
        "historical_final_energy_substitution": 2,
        "start_year_final_energy_substitution_rate_top_down_sectors_sp": 1,
        "select_final_energy_substitution_rate_top_down_sectors_sp": 2,
    },
)
def trend_of_final_energy_substituion_annual_variation():
    """
    Estimated final energy annunal substitution by final energy as a function of the exogenous policies
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "NRG FE I": _subscript_dict["NRG FE I"],
            },
            ["REGIONS 35 I", "NRG FE I"],
        ),
        lambda: if_then_else(
            select_final_energy_substitution_rate_top_down_sectors_sp() == 0,
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "NRG FE I": _subscript_dict["NRG FE I"],
                },
                ["REGIONS 35 I", "NRG FE I"],
            ),
            lambda: if_then_else(
                select_final_energy_substitution_rate_top_down_sectors_sp() == 1,
                lambda: historical_final_energy_substitution(),
                lambda: if_then_else(
                    time()
                    < start_year_final_energy_substitution_rate_top_down_sectors_sp(),
                    lambda: historical_final_energy_substitution(),
                    lambda: final_energy_substitution_rate_top_down_sectors_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="variation energy efficiency component",
    units="TJ/million$/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "energy_efficiency_component": 1,
        "energy_efficiengy_component_2015": 2,
        "minimum_energy_efficiency_versus_initial": 1,
        "energy_efficiency_annual_improvement": 3,
    },
)
def variation_energy_efficiency_component():
    """
    Variation of the energy efficiency by sector and final energy as a function of the historical trends and exogenous policies.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                "NRG FE I": _subscript_dict["NRG FE I"],
            },
            ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
        ),
        lambda: if_then_else(
            (energy_efficiency_annual_improvement() < 0)
            .expand_dims(
                {"SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"]}, 1
            )
            .expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 2),
            lambda: energy_efficiency_annual_improvement()
            * (
                energy_efficiency_component()
                - minimum_energy_efficiency_versus_initial()
                * energy_efficiengy_component_2015()
            ),
            lambda: energy_efficiency_annual_improvement()
            * energy_efficiengy_component_2015(),
        ),
    )


@component.add(
    name="variation energy intensity by sector and FE",
    units="TJ/million$/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_intensities_by_sector_and_fe": 1,
        "variation_energy_efficiency_component": 1,
        "final_energy_substitution_component": 1,
        "variation_final_energy_substitution_component": 1,
        "energy_efficiency_component": 1,
    },
)
def variation_energy_intensity_by_sector_and_fe():
    """
    Variation of the final energy intensities by sector and final energy as a function of the energy efficiencies and the final energy substitution. Bounded to avoid negative numbers.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    )
    value.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :] = np.maximum(
        -final_energy_intensities_by_sector_and_fe(),
        final_energy_substitution_component() * variation_energy_efficiency_component()
        + energy_efficiency_component()
        * variation_final_energy_substitution_component(),
    ).values
    value.loc[:, _subscript_dict["SECTORS ENERGY I"], :] = 0
    return value


@component.add(
    name="variation final energy substitution component",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_energy_substitution_component_aux": 2,
        "final_energy_substitution_component": 1,
    },
)
def variation_final_energy_substitution_component():
    """
    Variation of the final energy substitution by sector and final energy as a function of the historical trends, the final energy prioces and exogenous policies.
    """
    return (
        zidz(
            final_energy_substitution_component_aux(),
            sum(
                final_energy_substitution_component_aux().rename(
                    {"NRG FE I": "NRG FE I!"}
                ),
                dim=["NRG FE I!"],
            ).expand_dims({"NRG FE I": _subscript_dict["NRG FE I"]}, 2),
        )
        - final_energy_substitution_component()
    )
