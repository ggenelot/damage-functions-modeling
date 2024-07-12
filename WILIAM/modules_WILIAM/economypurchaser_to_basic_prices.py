"""
Module economypurchaser_to_basic_prices
Translated using PySD version 3.14.0
"""

@component.add(
    name="delayed TS final demand total in purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices": 1},
    other_deps={
        "_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices": {
            "initial": {
                "initial_final_demand_at_purchaser_prices_total": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "initial_final_demand_at_purchaser_prices_total": 1,
                "final_demand_total_in_purchaser_prices": 1,
            },
        }
    },
)
def delayed_ts_final_demand_total_in_purchaser_prices():
    """
    Delayed (time step) final demand in purchaser prices and nominal terms.
    """
    return _delayfixed_delayed_ts_final_demand_total_in_purchaser_prices()


_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_final_demand_at_purchaser_prices_total(),
        lambda: final_demand_total_in_purchaser_prices(),
    ),
    lambda: time_step(),
    lambda: initial_final_demand_at_purchaser_prices_total(),
    time_step,
    "_delayfixed_delayed_ts_final_demand_total_in_purchaser_prices",
)


@component.add(
    name="delayed TS gross domestic product growth",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_domestic_product_growth": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_domestic_product_growth": {
            "initial": {"time_step": 1},
            "step": {"gross_domestic_product_growth_ts": 1},
        }
    },
)
def delayed_ts_gross_domestic_product_growth():
    """
    Delayed (times tep) GDP growth
    """
    return _delayfixed_delayed_ts_gross_domestic_product_growth()


_delayfixed_delayed_ts_gross_domestic_product_growth = DelayFixed(
    lambda: gross_domestic_product_growth_ts(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0.02, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_gross_domestic_product_growth",
)


@component.add(
    name="delayed TS gross domestic product nominal",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gross_domestic_product_nominal": 1},
    other_deps={
        "_delayfixed_delayed_ts_gross_domestic_product_nominal": {
            "initial": {"initial_delayed_gdp": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_gdp": 1,
                "gross_domestic_product_nominal": 1,
            },
        }
    },
)
def delayed_ts_gross_domestic_product_nominal():
    """
    Delayed (time step) gross domestic product in nominal terms
    """
    return _delayfixed_delayed_ts_gross_domestic_product_nominal()


_delayfixed_delayed_ts_gross_domestic_product_nominal = DelayFixed(
    lambda: if_then_else(
        time() <= 2014,
        lambda: initial_delayed_gdp(),
        lambda: gross_domestic_product_nominal(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_gdp(),
    time_step,
    "_delayfixed_delayed_ts_gross_domestic_product_nominal",
)


@component.add(
    name="final demand domestic basic prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "taxes_products_domestic_final_demand": 1,
        "margins_paid_domestic": 1,
        "margins_received_domestic": 1,
    },
)
def final_demand_domestic_basic_prices():
    """
    Final demand domestic in basic prices and nominal terms.
    """
    return (
        final_demand_domestic_in_purchaser_prices()
        - taxes_products_domestic_final_demand()
        - margins_paid_domestic()
        + margins_received_domestic()
    )


@component.add(
    name="final demand domestic in basic prices real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "initial_price_of_output": 1,
        "mdollars_per_mdollars_2015": 2,
        "price_transformation": 2,
        "final_demand_domestic_basic_prices": 2,
        "price_output": 1,
    },
)
def final_demand_domestic_in_basic_prices_real():
    """
    Final demand domestic products in basic prices and real terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_domestic_basic_prices()
        * zidz(price_transformation(), initial_price_of_output())
        / mdollars_per_mdollars_2015(),
        lambda: final_demand_domestic_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                },
                ["REGIONS 35 I", "SECTORS I"],
            ),
            price_output(),
        )
        / mdollars_per_mdollars_2015(),
    )


@component.add(
    name="final demand domestic in purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "initial_import_shares_final_demand": 1,
        "final_demand_total_in_purchaser_prices_exc_households_ghg_taxes": 2,
        "import_shares_final_demand_constrained": 1,
    },
)
def final_demand_domestic_in_purchaser_prices():
    """
    Final demand domestic in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_total_in_purchaser_prices_exc_households_ghg_taxes()
        * (1 - initial_import_shares_final_demand()),
        lambda: final_demand_total_in_purchaser_prices_exc_households_ghg_taxes()
        * (1 - import_shares_final_demand_constrained()),
    )


@component.add(
    name="final demand dometic in basic prices real by component",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_domestic_in_basic_prices_real": 1},
)
def final_demand_dometic_in_basic_prices_real_by_component():
    """
    Total final demand real in basic prices
    """
    return sum(
        final_demand_domestic_in_basic_prices_real().rename(
            {"SECTORS I": "SECTORS I!"}
        ),
        dim=["SECTORS I!"],
    )


@component.add(
    name="final demand imports basic prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "margins_paid_imports": 1,
        "taxes_products_imports_final_demand": 1,
        "margins_received_imports": 1,
    },
)
def final_demand_imports_basic_prices():
    """
    Final demand imports in basic prices and nominal terms.
    """
    return (
        final_demand_imports_by_origin_in_purchaser_prices().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
        )
        - margins_paid_imports()
        - taxes_products_imports_final_demand()
        + margins_received_imports()
    )


@component.add(
    name="final demand imports by origin in purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "initial_import_shares_origin_final_demand": 1,
        "final_demand_imports_in_purchaser_prices": 2,
        "import_shares_origin_final_demand": 1,
    },
)
def final_demand_imports_by_origin_in_purchaser_prices():
    """
    Final demand imports by origin in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_imports_in_purchaser_prices()
        * initial_import_shares_origin_final_demand().transpose(
            "REGIONS 35 I", "SECTORS I", "FINAL DEMAND I", "REGIONS 35 MAP I"
        ),
        lambda: final_demand_imports_in_purchaser_prices()
        * import_shares_origin_final_demand().transpose(
            "REGIONS 35 I", "SECTORS I", "FINAL DEMAND I", "REGIONS 35 MAP I"
        ),
    ).transpose("REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "FINAL DEMAND I")


@component.add(
    name="final demand imports in basic prices real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "price_transformation": 2,
        "final_demand_imports_basic_prices": 2,
        "mdollars_per_mdollars_2015": 2,
        "initial_price_of_output": 1,
        "price_output": 1,
    },
)
def final_demand_imports_in_basic_prices_real():
    """
    Final demand imported products in basic prices and real terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_imports_basic_prices()
        * zidz(price_transformation(), initial_price_of_output())
        / mdollars_per_mdollars_2015(),
        lambda: final_demand_imports_basic_prices()
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                },
                ["REGIONS 35 I", "SECTORS I"],
            ),
            price_output(),
        )
        / mdollars_per_mdollars_2015(),
    )


@component.add(
    name="final demand imports in basic prices real by component",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_imports_in_basic_prices_real": 1},
)
def final_demand_imports_in_basic_prices_real_by_component():
    """
    Total final demand real in basic prices
    """
    return sum(
        final_demand_imports_in_basic_prices_real().rename(
            {
                "REGIONS 35 I": "REGIONS 35 MAP I!",
                "SECTORS I": "SECTORS I!",
                "REGIONS 35 MAP I": "REGIONS 35 I",
            }
        ),
        dim=["REGIONS 35 MAP I!", "SECTORS I!"],
    )


@component.add(
    name="final demand imports in purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "initial_import_shares_final_demand": 1,
        "final_demand_total_in_purchaser_prices_exc_households_ghg_taxes": 2,
        "import_shares_final_demand_constrained": 1,
    },
)
def final_demand_imports_in_purchaser_prices():
    """
    Final demand imports in purchaser prices and nominal terms.
    """
    return if_then_else(
        switch_eco_trade() == 0,
        lambda: final_demand_total_in_purchaser_prices_exc_households_ghg_taxes()
        * initial_import_shares_final_demand(),
        lambda: final_demand_total_in_purchaser_prices_exc_households_ghg_taxes()
        * import_shares_final_demand_constrained(),
    )


@component.add(
    name="final demand total in basic prices real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_dometic_in_basic_prices_real_by_component": 1,
        "final_demand_imports_in_basic_prices_real_by_component": 1,
    },
)
def final_demand_total_in_basic_prices_real():
    """
    Total final demand real in basic prices
    """
    return (
        final_demand_dometic_in_basic_prices_real_by_component()
        + final_demand_imports_in_basic_prices_real_by_component()
    )


@component.add(
    name="final demand total in purchaser prices",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_final_demand_at_purchaser_prices_total": 4,
        "delayed_ts_final_demand_total_in_purchaser_prices": 1,
        "delayed_ts_gross_domestic_product_growth": 1,
        "switch_eco_government": 1,
        "government_consumption_purchaser_prices": 1,
        "switch_eco_investment": 1,
        "gross_fixed_capital_formation_by_good": 1,
        "switch_eco_households": 1,
        "total_households_consumption_purchaser_prices": 1,
    },
)
def final_demand_total_in_purchaser_prices():
    """
    Final demand in purchaser prices and nominal terms.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
        },
        ["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    )
    value.loc[
        :, :, _subscript_dict["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"]
    ] = if_then_else(
        time() <= 2015,
        lambda: initial_final_demand_at_purchaser_prices_total()
        .loc[
            :,
            :,
            _subscript_dict["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"],
        ]
        .rename(
            {
                "FINAL DEMAND I": "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"
            }
        ),
        lambda: (1 + delayed_ts_gross_domestic_product_growth())
        * delayed_ts_final_demand_total_in_purchaser_prices()
        .loc[
            :,
            :,
            _subscript_dict["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"],
        ]
        .rename(
            {
                "FINAL DEMAND I": "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"
            }
        ),
    ).values
    value.loc[:, :, ["GOVERNMENT W"]] = (
        if_then_else(
            switch_eco_government() == 0,
            lambda: initial_final_demand_at_purchaser_prices_total()
            .loc[:, :, "GOVERNMENT W"]
            .reset_coords(drop=True),
            lambda: government_consumption_purchaser_prices(),
        )
        .expand_dims(
            {"FINAL DEMAND CONSUMPTION INVESTMENT GOVERNMENT I": ["GOVERNMENT W"]}, 2
        )
        .values
    )
    value.loc[:, :, ["GROSS FIXED CAPITAL FORMATION W"]] = (
        if_then_else(
            switch_eco_investment() == 0,
            lambda: initial_final_demand_at_purchaser_prices_total()
            .loc[:, :, "GROSS FIXED CAPITAL FORMATION W"]
            .reset_coords(drop=True),
            lambda: gross_fixed_capital_formation_by_good(),
        )
        .expand_dims(
            {
                "FINAL DEMAND CONSUMPTION INVESTMENT GOVERNMENT I": [
                    "GROSS FIXED CAPITAL FORMATION W"
                ]
            },
            2,
        )
        .values
    )
    value.loc[:, :, ["CONSUMPTION W"]] = (
        if_then_else(
            switch_eco_households() == 0,
            lambda: initial_final_demand_at_purchaser_prices_total()
            .loc[:, :, "CONSUMPTION W"]
            .reset_coords(drop=True),
            lambda: total_households_consumption_purchaser_prices(),
        )
        .expand_dims(
            {"FINAL DEMAND CONSUMPTION INVESTMENT GOVERNMENT I": ["CONSUMPTION W"]}, 2
        )
        .values
    )
    return value


@component.add(
    name="final demand total in purchaser prices exc households GHG taxes",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_total_in_purchaser_prices": 2,
        "ghg_emissions_households_coicop_35_r": 1,
        "co2_tax_rate_households": 1,
        "consumption_structure_coicop": 1,
    },
)
def final_demand_total_in_purchaser_prices_exc_households_ghg_taxes():
    """
    Final demand in purchaser prices and nominal terms, minus GHG taxes paid by household
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
        },
        ["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, :, ["CONSUMPTION W"]] = False
    value.values[except_subs.values] = final_demand_total_in_purchaser_prices().values[
        except_subs.values
    ]
    value.loc[:, :, ["CONSUMPTION W"]] = (
        (
            final_demand_total_in_purchaser_prices()
            .loc[:, :, "CONSUMPTION W"]
            .reset_coords(drop=True)
            - sum(
                co2_tax_rate_households().rename(
                    {"GHG ENERGY USE I": "GHG ENERGY USE I!"}
                )
                * ghg_emissions_households_coicop_35_r()
                .loc[:, :, _subscript_dict["GHG ENERGY USE I"]]
                .rename({"COICOP I": "COICOP I!", "GHG I": "GHG ENERGY USE I!"})
                .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "COICOP I!")
                * consumption_structure_coicop()
                .rename({"COICOP I": "COICOP I!"})
                .transpose("REGIONS 35 I", "COICOP I!", "SECTORS I"),
                dim=["GHG ENERGY USE I!", "COICOP I!"],
            )
        )
        .expand_dims(
            {"FINAL DEMAND CONSUMPTION INVESTMENT GOVERNMENT I": ["CONSUMPTION W"]}, 2
        )
        .values
    )
    return value


@component.add(
    name="gross domestic product growth TS",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "delayed_ts_gross_domestic_product_nominal": 1,
    },
)
def gross_domestic_product_growth_ts():
    """
    Gros domestic product growth by Time Step
    """
    return (
        zidz(
            gross_domestic_product_nominal(),
            delayed_ts_gross_domestic_product_nominal(),
        )
        - 1
    )


@component.add(
    name="margins paid domestic",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "taxes_products_domestic_final_demand": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
    },
)
def margins_paid_domestic():
    """
    Margins paid domestic in nominal terms.
    """
    return (
        final_demand_domestic_in_purchaser_prices()
        - taxes_products_domestic_final_demand()
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                    "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
                },
                ["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
            ),
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand(),
        )
    )


@component.add(
    name="margins paid imports",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "taxes_products_imports_final_demand": 1,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
    },
)
def margins_paid_imports():
    """
    Margins paid imports in nominal terms.
    """
    return (
        final_demand_imports_by_origin_in_purchaser_prices().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
        )
        - taxes_products_imports_final_demand()
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                    "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
                    "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
                },
                ["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
            ),
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
            ),
        )
    )


@component.add(
    name="margins received domestic",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "margins_paid_domestic": 1,
        "trade_and_transportation_margins_received_for_domestic_products_for_final_demand": 1,
    },
)
def margins_received_domestic():
    """
    Margins recived domestic in nominal terms.
    """
    return (
        sum(
            margins_paid_domestic().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        * trade_and_transportation_margins_received_for_domestic_products_for_final_demand().transpose(
            "REGIONS 35 I", "FINAL DEMAND I", "SECTORS I"
        )
    ).transpose("REGIONS 35 I", "SECTORS I", "FINAL DEMAND I")


@component.add(
    name="margins received imports",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "margins_paid_imports": 1,
        "trade_and_transportation_margins_received_for_imported_products_for_final_demand": 1,
    },
)
def margins_received_imports():
    """
    Margins recived imports in nominal terms.
    """
    return (
        sum(
            margins_paid_imports().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        * trade_and_transportation_margins_received_for_imported_products_for_final_demand()
        .rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
        )
        .transpose("REGIONS 35 I", "REGIONS 35 MAP I", "FINAL DEMAND I", "SECTORS I")
    ).transpose("REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I")


@component.add(
    name="SWITCH ECO TRADE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_trade"},
)
def switch_eco_trade():
    """
    This switch can take two values: 0: Trade shares remain constant 1: Trade shares linked to trade module
    """
    return _ext_constant_switch_eco_trade()


_ext_constant_switch_eco_trade = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_TRADE",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_trade",
)


@component.add(
    name="taxes products domestic final demand",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_purchaser_prices": 1,
        "tax_rate_final_products_domestic_default": 1,
    },
)
def taxes_products_domestic_final_demand():
    """
    Net taxes on domestic final products in nominal terms.
    """
    return final_demand_domestic_in_purchaser_prices() * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                    "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
                },
                ["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
            ),
            1 + tax_rate_final_products_domestic_default(),
        )
    )


@component.add(
    name="taxes products domestic final demand real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_basic_prices_real": 2,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 2,
        "trade_and_transportation_margins_received_for_domestic_products_for_final_demand": 1,
        "tax_rate_final_products_domestic_default": 1,
    },
)
def taxes_products_domestic_final_demand_real():
    """
    Taxes on domestic final products in real terms
    """
    return (
        final_demand_domestic_in_basic_prices_real()
        * (
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
        )
        - (
            sum(
                final_demand_domestic_in_basic_prices_real().rename(
                    {"SECTORS I": "SECTORS MAP I!"}
                )
                * trade_and_transportation_margins_paid_for_domestic_products_for_final_demand().rename(
                    {"SECTORS I": "SECTORS MAP I!"}
                ),
                dim=["SECTORS MAP I!"],
            )
            * trade_and_transportation_margins_received_for_domestic_products_for_final_demand().transpose(
                "REGIONS 35 I", "FINAL DEMAND I", "SECTORS I"
            )
        ).transpose("REGIONS 35 I", "SECTORS I", "FINAL DEMAND I")
    ) * tax_rate_final_products_domestic_default()


@component.add(
    name="taxes products imports final demand",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_by_origin_in_purchaser_prices": 1,
        "tax_rate_final_products_imports_default": 1,
    },
)
def taxes_products_imports_final_demand():
    """
    Net taxes on imported final products in nominal terms.
    """
    return final_demand_imports_by_origin_in_purchaser_prices().rename(
        {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
    ) * (
        1
        - zidz(
            xr.DataArray(
                1,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                    "REGIONS 35 MAP I": _subscript_dict["REGIONS 35 MAP I"],
                    "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
                },
                ["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
            ),
            1 + tax_rate_final_products_imports_default(),
        )
    )


@component.add(
    name="taxes products imports final demand real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_in_basic_prices_real": 2,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 2,
        "trade_and_transportation_margins_received_for_imported_products_for_final_demand": 1,
        "tax_rate_final_products_imports_default": 1,
    },
)
def taxes_products_imports_final_demand_real():
    """
    Taxes on imported final products in real terms
    """
    return (
        final_demand_imports_in_basic_prices_real()
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
            )
        )
        - (
            sum(
                final_demand_imports_in_basic_prices_real().rename(
                    {"SECTORS I": "SECTORS I!"}
                )
                * trade_and_transportation_margins_paid_for_imported_products_for_final_demand().rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS I": "SECTORS I!",
                        "REGIONS 35 I": "REGIONS 35 MAP I",
                    }
                ),
                dim=["SECTORS I!"],
            )
            * trade_and_transportation_margins_received_for_imported_products_for_final_demand()
            .rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
            )
            .transpose(
                "REGIONS 35 I", "REGIONS 35 MAP I", "FINAL DEMAND I", "SECTORS I"
            )
        ).transpose("REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I")
    ) * tax_rate_final_products_imports_default()
