"""
Module energytransformation.allocation_protra.opex
Translated using PySD version 3.14.0
"""

@component.add(
    name="biomass price function",
    comp_type="Auxiliary",
    comp_subtype="with Lookup",
    depends_on={"pe_forestry_demand_delayed": 1},
)
def biomass_price_function():
    """
    Price-cost curve from Rogner et al 2012
    !EJ/yr
    !$/GJ
    """
    return np.interp(
        pe_forestry_demand_delayed(),
        [
            2.60035,
            4.41968,
            6.23928,
            7.31991,
            7.33025,
            7.82069,
            9.75033,
            11.5697,
            13.389,
            15.2083,
            17.0277,
            18.847,
            20.6664,
            22.4857,
            24.305,
            26.1244,
            27.9437,
            29.7631,
            31.5824,
            33.4017,
            35.2211,
            37.0404,
            38.8597,
            40.6791,
            42.4984,
            44.3178,
            46.1378,
            46.4779,
            46.7293,
            46.7397,
            46.7502,
            46.7607,
            46.7711,
            47.2618,
            49.1917,
            51.011,
            52.8303,
            54.6497,
            56.469,
            58.2884,
            60.1077,
            61.9279,
            62.2683,
            62.5197,
            62.5302,
            62.5406,
            62.5511,
            62.5615,
            63.052,
            64.9816,
            66.8009,
            68.6203,
            70.4396,
            72.259,
            74.0783,
            75.8976,
            77.717,
            79.5363,
            81.1076,
        ],
        [
            1.04792,
            1.04676,
            1.05221,
            1.19357,
            1.45751,
            1.91401,
            2.0142,
            2.01304,
            2.01187,
            2.01071,
            2.00955,
            2.00839,
            2.00723,
            2.00607,
            2.0049,
            2.00374,
            2.00258,
            2.00142,
            2.00026,
            1.99909,
            1.99793,
            1.99677,
            1.99561,
            1.99445,
            1.99329,
            1.99212,
            2.00861,
            2.24559,
            2.33038,
            2.59736,
            2.86433,
            3.13131,
            3.39828,
            3.85999,
            3.96711,
            3.96595,
            3.96478,
            3.96362,
            3.96246,
            3.9613,
            3.96014,
            3.98104,
            4.22574,
            4.31053,
            4.5775,
            4.84448,
            5.11146,
            5.37843,
            5.83494,
            5.93512,
            5.93396,
            5.9328,
            5.93164,
            5.93048,
            5.92931,
            5.92815,
            5.92699,
            5.92583,
            5.92482,
        ],
    )


@component.add(
    name="Biomass price global Mdollars per EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "biomass_price_function": 1,
        "unit_conversion_gj_ej": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def biomass_price_global_mdollars_per_ej():
    """
    Biomass price per energy unit.
    """
    return (
        biomass_price_function()
        * unit_conversion_gj_ej()
        / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="CCS OM COST FACTOR", units="DMNL", comp_type="Constant", comp_subtype="Normal"
)
def ccs_om_cost_factor():
    """
    Cost factor accounting for increased O&M cost of CCS plants.
    """
    return 1.3


@component.add(
    name="CO2 cost by PROTRA and region",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_fuel_utilization_ratio": 1,
        "co2_emission_factor_by_protra_mt_per_ej": 1,
        "co2_tax_rate_sectors": 1,
    },
)
def co2_cost_by_protra_and_region():
    """
    CO2 cost by PROTRA, taking into account the CO2 tax (for industry), emission factors and conversion efficiencies.
    """
    return (
        1
        / protra_fuel_utilization_ratio()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * co2_emission_factor_by_protra_mt_per_ej()
        * co2_tax_rate_sectors()
        .loc[_subscript_dict["REGIONS 9 I"], "CO2"]
        .reset_coords(drop=True)
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
    )


@component.add(
    name="CO2 emission factor by PROTRA",
    units="kg/TJ",
    subscripts=["NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"emission_factors_stationary_combustion": 24},
)
def co2_emission_factor_by_protra():
    """
    regions not strictly required here, in emission intensities values are the same for all regions. Oter PROTRA equations pending.
    """
    value = xr.DataArray(
        np.nan, {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]}, ["NRG PROTRA I"]
    )
    value.loc[["PROTRA CHP gas fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP gas fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP gas fuels CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP gas fuels CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP geothermal DEACTIVATED"]] = 0
    value.loc[["PROTRA CHP liquid fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP liquid fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP liquid fuels CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP liquid fuels CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP solid fossil"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP solid fossil", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP solid fossil CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP solid fossil CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP waste"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP waste", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP solid bio"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP solid bio", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA CHP solid bio CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA CHP solid bio CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA HP gas fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA HP gas fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA HP solid bio"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA HP solid bio", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA HP geothermal"]] = 0
    value.loc[["PROTRA HP liquid fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA HP liquid fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA HP solar DEACTIVATED"]] = 0
    value.loc[["PROTRA HP solid fossil"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA HP solid fossil", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA HP waste"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA HP waste", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP solid bio"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP solid bio", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP solid bio CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP solid bio CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP gas fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP gas fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP gas fuels CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP gas fuels CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP geothermal"]] = 0
    value.loc[["PROTRA PP hydropower dammed"]] = 0
    value.loc[["PROTRA PP hydropower run of river"]] = 0
    value.loc[["PROTRA PP liquid fuels"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP liquid fuels", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP liquid fuels CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP liquid fuels CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP nuclear"]] = 0
    value.loc[["PROTRA PP oceanic"]] = 0
    value.loc[["PROTRA PP solar CSP"]] = 0
    value.loc[["PROTRA PP solar open space PV"]] = 0
    value.loc[["PROTRA PP solar urban PV"]] = 0
    value.loc[["PROTRA PP solid fossil"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP solid fossil", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP solid fossil CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP solid fossil CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP waste"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP waste", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP waste CCS"]] = sum(
        emission_factors_stationary_combustion()
        .loc["PROTRA PP waste CCS", :, "CO2"]
        .reset_coords(drop=True)
        .rename({"NRG TI I": "NRG TI I!"}),
        dim=["NRG TI I!"],
    )
    value.loc[["PROTRA PP wind offshore"]] = 0
    value.loc[["PROTRA PP wind onshore"]] = 0
    value.loc[["PROTRA blending gas fuels"]] = 0
    value.loc[["PROTRA blending liquid fuels"]] = 0
    value.loc[["PROTRA no process TI hydrogen"]] = 0
    value.loc[["PROTRA no process TI solid bio"]] = 0
    value.loc[["PROTRA no process TI solid fossil"]] = 0
    return value


@component.add(
    name="CO2 emission factor by PROTRA MT per EJ",
    units="Mt/EJ",
    subscripts=["NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "co2_emission_factor_by_protra": 1,
        "unit_conversion_tj_ej": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def co2_emission_factor_by_protra_mt_per_ej():
    return (
        co2_emission_factor_by_protra()
        * unit_conversion_tj_ej()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="Coal price Mdollars per EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "coal_price_historical_t": 1,
        "estimated_coal_price": 1,
        "mixed_coal_conversion_factor_mt_to_ej": 1,
    },
)
def coal_price_mdollars_per_ej():
    """
    Coal price per energy unit (taking into account hard coal / brown coal as part of the energy mixture).
    """
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: coal_price_historical_t() * 44.4,
        lambda: estimated_coal_price() * mixed_coal_conversion_factor_mt_to_ej(),
    )


@component.add(
    name="CONVERSION FACTOR Mt to EJ",
    subscripts=["COAL TYPES I"],
    comp_type="Constant",
    comp_subtype="Normal",
)
def conversion_factor_mt_to_ej():
    """
    Conversion factor Mt to EJ of hard coal and brown coal based on the Source: Global Energy Assessment-Toward a Sustainable Future (Rogner et al., 2012)
    """
    value = xr.DataArray(
        np.nan, {"COAL TYPES I": _subscript_dict["COAL TYPES I"]}, ["COAL TYPES I"]
    )
    value.loc[["HARD COAL"]] = 40.51
    value.loc[["BROWN COAL"]] = 103.3
    return value


@component.add(
    name="fuel cost by PROTRA and region",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_fuel_utilization_ratio": 1,
        "fuel_price_by_protra_9r_adjusted": 1,
    },
)
def fuel_cost_by_protra_and_region():
    """
    fuelcost by production technology, taking into account the endogenous fuel price signal
    """
    return (
        1
        / protra_fuel_utilization_ratio()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * fuel_price_by_protra_9r_adjusted()
    )


@component.add(
    name="fuel price by PROTRA 9R",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fuel_price_by_protra_world": 1},
)
def fuel_price_by_protra_9r():
    """
    Fuel prices per energy unit associated with the corresponding PROTRA plant by REGION.
    """
    return fuel_price_by_protra_world().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="fuel price by PROTRA 9R adjusted",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fuel_price_by_protra_9r": 6,
        "switch_energy": 1,
        "switch_law2nrg_available_forestry_products_for_industry": 1,
        "signal_availability_forestry_products_for_energy": 2,
        "switch_nrg_limited_res_potentials": 1,
    },
)
def fuel_price_by_protra_9r_adjusted():
    """
    Taking into account regionalised solid biomass availability from land use model. Biomass technologies: The scarcity-adjusted price signal for solid_bio technologies is cut off at 5 x the base price to increase the robustness of the model results.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["PROTRA SOLID BIO I"]] = False
    value.values[except_subs.values] = fuel_price_by_protra_9r().values[
        except_subs.values
    ]
    value.loc[:, _subscript_dict["PROTRA SOLID BIO I"]] = if_then_else(
        np.logical_or(
            switch_energy() == 0,
            np.logical_or(
                switch_law2nrg_available_forestry_products_for_industry() == 0,
                switch_nrg_limited_res_potentials() == 0,
            ),
        ),
        lambda: fuel_price_by_protra_9r()
        .loc[:, _subscript_dict["PROTRA SOLID BIO I"]]
        .rename({"NRG PROTRA I": "PROTRA SOLID BIO I"}),
        lambda: if_then_else(
            xidz(
                fuel_price_by_protra_9r()
                .loc[:, _subscript_dict["PROTRA SOLID BIO I"]]
                .rename({"NRG PROTRA I": "PROTRA SOLID BIO I"}),
                signal_availability_forestry_products_for_energy().expand_dims(
                    {"PROTRA SOLID BIO I": _subscript_dict["PROTRA SOLID BIO I"]}, 1
                ),
                1000,
            )
            < 5
            * fuel_price_by_protra_9r()
            .loc[:, _subscript_dict["PROTRA SOLID BIO I"]]
            .rename({"NRG PROTRA I": "PROTRA SOLID BIO I"}),
            lambda: xidz(
                fuel_price_by_protra_9r()
                .loc[:, _subscript_dict["PROTRA SOLID BIO I"]]
                .rename({"NRG PROTRA I": "PROTRA SOLID BIO I"}),
                signal_availability_forestry_products_for_energy().expand_dims(
                    {"PROTRA SOLID BIO I": _subscript_dict["PROTRA SOLID BIO I"]}, 1
                ),
                1000,
            ),
            lambda: 5
            * fuel_price_by_protra_9r()
            .loc[:, _subscript_dict["PROTRA SOLID BIO I"]]
            .rename({"NRG PROTRA I": "PROTRA SOLID BIO I"}),
        ),
    ).values
    return value


@component.add(
    name="fuel price by PROTRA world",
    units="Mdollars/EJ",
    subscripts=["NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gas_price_mdollars_per_ej": 5,
        "oil_price_mdollars_per_ej": 5,
        "coal_price_mdollars_per_ej": 3,
        "biomass_price_global_mdollars_per_ej": 5,
        "nuclear_price_mdollars_per_ej_fictional": 1,
    },
)
def fuel_price_by_protra_world():
    """
    Fuel prices per energy unit associated with the corresponding PROTRA plant.
    """
    value = xr.DataArray(
        np.nan, {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]}, ["NRG PROTRA I"]
    )
    value.loc[["PROTRA CHP gas fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA CHP gas fuels CCS"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA CHP geothermal DEACTIVATED"]] = 0
    value.loc[["PROTRA CHP liquid fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA CHP liquid fuels CCS"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA CHP solid fossil"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA CHP solid fossil CCS"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA CHP waste"]] = 0
    value.loc[["PROTRA CHP solid bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA CHP solid bio CCS"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA HP gas fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA HP solid bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA HP geothermal"]] = 0
    value.loc[["PROTRA HP liquid fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA HP solar DEACTIVATED"]] = 0
    value.loc[["PROTRA HP solid fossil"]] = coal_price_mdollars_per_ej()
    value.loc[["PROTRA HP waste"]] = 0
    value.loc[["PROTRA PP solid bio"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA PP solid bio CCS"]] = biomass_price_global_mdollars_per_ej()
    value.loc[["PROTRA PP gas fuels"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA PP gas fuels CCS"]] = gas_price_mdollars_per_ej()
    value.loc[["PROTRA PP geothermal"]] = 0
    value.loc[["PROTRA PP hydropower dammed"]] = 0
    value.loc[["PROTRA PP hydropower run of river"]] = 0
    value.loc[["PROTRA PP liquid fuels"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA PP liquid fuels CCS"]] = oil_price_mdollars_per_ej()
    value.loc[["PROTRA PP nuclear"]] = nuclear_price_mdollars_per_ej_fictional()
    value.loc[["PROTRA PP oceanic"]] = 0
    value.loc[["PROTRA PP solar CSP"]] = 0
    value.loc[["PROTRA PP solar open space PV"]] = 0
    value.loc[["PROTRA PP solar urban PV"]] = 0
    value.loc[["PROTRA PP solid fossil"]] = 0
    value.loc[["PROTRA PP solid fossil CCS"]] = 0
    value.loc[["PROTRA PP waste"]] = 0
    value.loc[["PROTRA PP waste CCS"]] = 0
    value.loc[["PROTRA PP wind offshore"]] = 0
    value.loc[["PROTRA PP wind onshore"]] = 0
    value.loc[["PROTRA blending gas fuels"]] = 0
    value.loc[["PROTRA blending liquid fuels"]] = 0
    value.loc[["PROTRA no process TI hydrogen"]] = 0
    value.loc[["PROTRA no process TI solid bio"]] = 0
    value.loc[["PROTRA no process TI solid fossil"]] = 0
    return value


@component.add(
    name="Gas price Mdollars per EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "unit_conversion_mmbtu_ej": 2,
        "unit_conversion_dollars_mdollars": 2,
        "gas_price_historical": 1,
        "estimated_gas_price": 1,
    },
)
def gas_price_mdollars_per_ej():
    """
    Gas price per energy unit.
    """
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: gas_price_historical()
        * unit_conversion_mmbtu_ej()
        / unit_conversion_dollars_mdollars(),
        lambda: estimated_gas_price()
        * unit_conversion_mmbtu_ej()
        / unit_conversion_dollars_mdollars(),
    )


@component.add(
    name="INTIAL OPEX by PROTRA and region",
    units="MD/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_intial_opex_by_protra_and_region": 1},
    other_deps={
        "_initial_intial_opex_by_protra_and_region": {"initial": {}, "step": {}}
    },
)
def intial_opex_by_protra_and_region():
    return _initial_intial_opex_by_protra_and_region()


_initial_intial_opex_by_protra_and_region = Initial(
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    ),
    "_initial_intial_opex_by_protra_and_region",
)


@component.add(
    name="max OPEX signal",
    units="MD/EJ",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"opex_by_protra_and_region_delayed_ts": 1},
)
def max_opex_signal():
    return vmax(
        opex_by_protra_and_region_delayed_ts().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="min OPEX signal",
    units="MD/EJ",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"opex_by_protra_and_region_delayed_ts": 1},
)
def min_opex_signal():
    return vmin(
        opex_by_protra_and_region_delayed_ts().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="mixed coal conversion factor Mt to EJ",
    units="Mt/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"extraction_of_coal": 6, "conversion_factor_mt_to_ej": 2},
)
def mixed_coal_conversion_factor_mt_to_ej():
    """
    mixed conversion factor (accounting for hard coal / brown coal share)
    """
    return float(extraction_of_coal().loc["HARD COAL"]) / (
        float(extraction_of_coal().loc["HARD COAL"])
        + float(extraction_of_coal().loc["BROWN COAL"])
    ) * float(conversion_factor_mt_to_ej().loc["HARD COAL"]) + float(
        extraction_of_coal().loc["BROWN COAL"]
    ) / (
        float(extraction_of_coal().loc["HARD COAL"])
        + float(extraction_of_coal().loc["BROWN COAL"])
    ) * float(
        conversion_factor_mt_to_ej().loc["BROWN COAL"]
    )


@component.add(
    name="Nuclear price Mdollars per EJ fictional",
    units="Mdollars/EJ",
    comp_type="Constant",
    comp_subtype="Normal",
)
def nuclear_price_mdollars_per_ej_fictional():
    """
    Nuclear fuel price per energy unit.
    """
    return 4000


@component.add(
    name="O and M cost MDollars per EJ",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"operation_and_maintainance_cost": 10, "ccs_om_cost_factor": 9},
)
def o_and_m_cost_mdollars_per_ej():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I"],
    )
    value.loc[:, _subscript_dict["PROTRA NON CCS I"]] = (
        (operation_and_maintainance_cost() / 3.6 * 10**3)
        .expand_dims({"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0)
        .values
    )
    value.loc[:, ["PROTRA CHP gas fuels CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA CHP gas fuels"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA CHP liquid fuels CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA CHP liquid fuels"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA CHP solid fossil CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA CHP solid fossil"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA CHP solid bio CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA CHP solid bio"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA PP solid bio CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA PP solid bio"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA PP gas fuels CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA PP gas fuels"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA PP liquid fuels CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA PP liquid fuels"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA PP solid fossil CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA PP solid fossil"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, ["PROTRA PP waste CCS"]] = (
        float(operation_and_maintainance_cost().loc["PROTRA PP waste"])
        / 3.6
        * 10**3
        * ccs_om_cost_factor()
    )
    value.loc[:, _subscript_dict["PROTRA NP I"]] = 0
    return value


@component.add(
    name="Oil price Mdollars per EJ",
    units="Mdollars/EJ",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_energy": 1,
        "oil_price_historical_bbl": 1,
        "unit_conversion_oil_bbl_per_ej": 2,
        "estimated_oil_price": 1,
    },
)
def oil_price_mdollars_per_ej():
    """
    Coal price per energy unit.
    """
    return if_then_else(
        np.logical_or(time() < 2015, switch_energy() == 0),
        lambda: oil_price_historical_bbl() * unit_conversion_oil_bbl_per_ej() / 10**6,
        lambda: estimated_oil_price() * unit_conversion_oil_bbl_per_ej() / 10**6,
    )


@component.add(
    name="OPERATION AND MAINTAINANCE COST",
    units="$/MWh",
    subscripts=["PROTRA NON CCS I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_operation_and_maintainance_cost",
        "__data__": "_ext_data_operation_and_maintainance_cost",
        "time": 1,
    },
)
def operation_and_maintainance_cost():
    """
    Operation and maintainance cost, danish energy agency, taking into account fixed maintainance cost and varying operating cost (depending on full load hours). FUTURE WORK: Endogenize this by splitting up into fixed and variable part, and linking the variable part to the actual full-load-hours (After curtailment).
    """
    return _ext_data_operation_and_maintainance_cost(time())


_ext_data_operation_and_maintainance_cost = ExtData(
    "model_parameters/energy/energy-transformation.xlsm",
    "Common",
    "OPERATION_AND_MAINTAINANCE_TIME",
    "OPERATION_AND_MAINTAINANCE_COST",
    "interpolate",
    {"PROTRA NON CCS I": _subscript_dict["PROTRA NON CCS I"]},
    _root,
    {"PROTRA NON CCS I": _subscript_dict["PROTRA NON CCS I"]},
    "_ext_data_operation_and_maintainance_cost",
)


@component.add(
    name="OPEX by PROTRA and region",
    units="Mdollars/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_fuel_utilization_ratio": 1,
        "fuel_price_by_protra_9r_adjusted": 1,
        "co2_emission_factor_by_protra_mt_per_ej": 1,
        "co2_tax_rate_sectors": 1,
        "o_and_m_cost_mdollars_per_ej": 1,
    },
)
def opex_by_protra_and_region():
    """
    Operating expenditures by PROTRA and region, consisting of FUELCOST + CO2-COST + O&M expenditures (note: variables also calculated independetly for ease of use).
    """
    return (
        1
        / protra_fuel_utilization_ratio()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * (
            fuel_price_by_protra_9r_adjusted()
            + (
                co2_emission_factor_by_protra_mt_per_ej()
                * co2_tax_rate_sectors()
                .loc[_subscript_dict["REGIONS 9 I"], "CO2"]
                .reset_coords(drop=True)
                .rename({"REGIONS 36 I": "REGIONS 9 I"})
            ).transpose("REGIONS 9 I", "NRG PROTRA I")
        )
        + o_and_m_cost_mdollars_per_ej()
    )


@component.add(
    name="OPEX by PROTRA and region delayed TS",
    units="MD/EJ",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_opex_by_protra_and_region_delayed_ts": 1},
    other_deps={
        "_delayfixed_opex_by_protra_and_region_delayed_ts": {
            "initial": {"intial_opex_by_protra_and_region": 1, "time_step": 1},
            "step": {"opex_by_protra_and_region": 1},
        }
    },
)
def opex_by_protra_and_region_delayed_ts():
    return _delayfixed_opex_by_protra_and_region_delayed_ts()


_delayfixed_opex_by_protra_and_region_delayed_ts = DelayFixed(
    lambda: opex_by_protra_and_region(),
    lambda: time_step(),
    lambda: intial_opex_by_protra_and_region(),
    time_step,
    "_delayfixed_opex_by_protra_and_region_delayed_ts",
)


@component.add(
    name="PE forestry demand delayed",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_pe_forestry_demand_delayed": 1},
    other_deps={
        "_delayfixed_pe_forestry_demand_delayed": {
            "initial": {"time_step": 1},
            "step": {"world_pe_by_commodity": 1},
        }
    },
)
def pe_forestry_demand_delayed():
    return _delayfixed_pe_forestry_demand_delayed()


_delayfixed_pe_forestry_demand_delayed = DelayFixed(
    lambda: float(world_pe_by_commodity().loc["PE forestry products"]),
    lambda: time_step(),
    lambda: 1,
    time_step,
    "_delayfixed_pe_forestry_demand_delayed",
)


@component.add(
    name="PROTRA utilization priorities endogenous",
    units="DMNL",
    subscripts=["REGIONS 9 I", "NRG PROTRA I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "opex_by_protra_and_region_delayed_ts": 1,
        "min_opex_signal": 2,
        "max_opex_signal": 1,
    },
)
def protra_utilization_priorities_endogenous():
    """
    Endogeneous allocation priorities for technology utilization allocation, based on transformation efficiency, Fuel prices and CO2 prics (so far no O&M cost element included)
    """
    return 1 - zidz(
        opex_by_protra_and_region_delayed_ts() - min_opex_signal(),
        (max_opex_signal() - min_opex_signal()).expand_dims(
            {"NRG PROTRA I": _subscript_dict["NRG PROTRA I"]}, 1
        ),
    )
