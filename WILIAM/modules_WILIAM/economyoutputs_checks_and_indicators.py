"""
Module economyoutputs_checks_and_indicators
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual GDP real 1R growth",
    units="Mdollars 2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_1r": 1, "delayed_gdp_real_1r": 1},
)
def annual_gdp_real_1r_growth():
    """
    Annual growth gross domestic product in real terms: World
    """
    return gdp_real_1r() - delayed_gdp_real_1r()


@component.add(
    name="delayed GDP real 1R",
    units="Mdollars 2015/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_gdp_real_1r": 1},
    other_deps={
        "_delayfixed_delayed_gdp_real_1r": {
            "initial": {"gdp_real_1r": 1},
            "step": {"gdp_real_1r": 1},
        }
    },
)
def delayed_gdp_real_1r():
    """
    Delayed gross domestic product in real terms: World
    """
    return _delayfixed_delayed_gdp_real_1r()


_delayfixed_delayed_gdp_real_1r = DelayFixed(
    lambda: gdp_real_1r(),
    lambda: 1,
    lambda: gdp_real_1r(),
    time_step,
    "_delayfixed_delayed_gdp_real_1r",
)


@component.add(
    name="economy dashboard",
    subscripts=["REGIONS 35 I", "DASHBOARD ECONOMY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 4,
        "labour_compensation_real": 1,
        "net_operating_surplus_real": 1,
        "consumption_fixed_capital_real": 1,
        "taxes_production_real": 1,
        "gross_value_added_real": 5,
        "taxes_products_by_sector_real": 1,
        "taxes_products_final_demand_real": 5,
        "final_demand_dometic_in_basic_prices_real_by_component": 4,
        "final_demand_imports_in_basic_prices_real_by_component": 4,
        "total_imports_real_by_product": 2,
        "total_exports_real_by_product": 2,
        "employment_total": 1,
        "labour_force": 1,
        "unemployment_rate": 1,
        "gross_domestic_product_deflator": 6,
        "government_revenue": 1,
        "government_expenditure": 1,
        "government_budget_balance": 2,
        "government_debt": 2,
        "disposable_income_real": 3,
        "consumption_coicop_real": 2,
        "population_35_regions": 2,
        "unit_conversion_dollars_2015_mdollars_2015": 2,
        "consumer_price_index": 1,
        "disposable_income": 2,
        "consumption_coicop": 2,
        "output_real": 1,
        "real_capital_stock": 1,
    },
)
def economy_dashboard():
    """
    Dashboard of the economy. Monetary values in 1000 Million USD 2015 prices. per capita vaules in USD 2015. Employment in million of people.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "DASHBOARD ECONOMY I": _subscript_dict["DASHBOARD ECONOMY I"],
        },
        ["REGIONS 35 I", "DASHBOARD ECONOMY I"],
    )
    value.loc[:, ["DB GDP"]] = (
        (gross_domestic_product_real_supply_side() / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB LABOUR COMPENSATION"]] = (
        (
            sum(
                labour_compensation_real().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB LABOUR COMPENSATION"]}, 1)
        .values
    )
    value.loc[:, ["DB NET OPERATING SURPLUS"]] = (
        (
            sum(
                net_operating_surplus_real().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB NET OPERATING SURPLUS"]}, 1)
        .values
    )
    value.loc[:, ["DB CONSUMPTION FIXED CAPITAL"]] = (
        (
            sum(
                consumption_fixed_capital_real().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB CONSUMPTION FIXED CAPITAL"]}, 1)
        .values
    )
    value.loc[:, ["DB TAXES PRODUCTION"]] = (
        (
            sum(
                taxes_production_real().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB TAXES PRODUCTION"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA AGRICULTURE"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS AGRICULTURE I"]]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS MAP I": "SECTORS AGRICULTURE I!",
                    }
                ),
                dim=["SECTORS AGRICULTURE I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA AGRICULTURE"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA EXTRACTION"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS MAP I": "SECTORS EXTRACTION I!",
                    }
                ),
                dim=["SECTORS EXTRACTION I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA EXTRACTION"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA ENERGY"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS ENERGY I"]]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS MAP I": "SECTORS ENERGY I!",
                    }
                ),
                dim=["SECTORS ENERGY I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA ENERGY"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA INDUSTRY"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS INDUSTRY I"]]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS MAP I": "SECTORS INDUSTRY I!",
                    }
                ),
                dim=["SECTORS INDUSTRY I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA INDUSTRY"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA SERVICES"]] = (
        (
            sum(
                gross_value_added_real()
                .loc[:, _subscript_dict["SECTORS SERVICES I"]]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "SECTORS MAP I": "SECTORS SERVICES I!",
                    }
                ),
                dim=["SECTORS SERVICES I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA SERVICES"]}, 1)
        .values
    )
    value.loc[:, ["DB GVA TAXES PRODUCTS TOTAL"]] = (
        (
            (
                sum(
                    taxes_products_by_sector_real().rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 I",
                            "SECTORS MAP I": "SECTORS I!",
                        }
                    ),
                    dim=["SECTORS I!"],
                )
                + sum(
                    taxes_products_final_demand_real().rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 I",
                            "FINAL DEMAND I": "FINAL DEMAND I!",
                        }
                    ),
                    dim=["FINAL DEMAND I!"],
                )
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GVA TAXES PRODUCTS TOTAL"]}, 1)
        .values
    )
    value.loc[:, ["DB HH CONSUMPTION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "CONSUMPTION W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "CONSUMPTION W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "CONSUMPTION W"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 MAP I": "REGIONS 35 I"})
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH CONSUMPTION"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV CONSUMPTION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "GOVERNMENT W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "GOVERNMENT W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "GOVERNMENT W"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 MAP I": "REGIONS 35 I"})
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV CONSUMPTION"]}, 1)
        .values
    )
    value.loc[:, ["DB GROSS FIXED CAPITAL FORMATION"]] = (
        (
            final_demand_dometic_in_basic_prices_real_by_component()
            .loc[:, "GROSS FIXED CAPITAL FORMATION W"]
            .reset_coords(drop=True)
            / 1000
            + final_demand_imports_in_basic_prices_real_by_component()
            .loc[:, "GROSS FIXED CAPITAL FORMATION W"]
            .reset_coords(drop=True)
            / 1000
            + taxes_products_final_demand_real()
            .loc[:, "GROSS FIXED CAPITAL FORMATION W"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 MAP I": "REGIONS 35 I"})
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GROSS FIXED CAPITAL FORMATION"]}, 1)
        .values
    )
    value.loc[:, ["DB OTHER FINAL DEMAND"]] = (
        (
            sum(
                final_demand_dometic_in_basic_prices_real_by_component()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"
                    ],
                ]
                .rename(
                    {
                        "FINAL DEMAND I": "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!"
                    }
                ),
                dim=["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!"],
            )
            / 1000
            + sum(
                final_demand_imports_in_basic_prices_real_by_component()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"
                    ],
                ]
                .rename(
                    {
                        "FINAL DEMAND I": "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!"
                    }
                ),
                dim=["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!"],
            )
            / 1000
            + sum(
                taxes_products_final_demand_real()
                .loc[
                    :,
                    _subscript_dict[
                        "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I"
                    ],
                ]
                .rename(
                    {
                        "REGIONS 35 MAP I": "REGIONS 35 I",
                        "FINAL DEMAND I": "FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!",
                    }
                ),
                dim=["FINAL DEMAND EXCEPT CONSUMPTION INVESTMENT GOVERNMENT I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB OTHER FINAL DEMAND"]}, 1)
        .values
    )
    value.loc[:, ["DB TRADE BALANCE"]] = (
        (
            sum(
                total_exports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
            - sum(
                total_imports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB TRADE BALANCE"]}, 1)
        .values
    )
    value.loc[:, ["DB EXPORTS"]] = (
        (
            sum(
                total_exports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB EXPORTS"]}, 1)
        .values
    )
    value.loc[:, ["DB IMPORTS"]] = (
        (
            sum(
                total_imports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB IMPORTS"]}, 1)
        .values
    )
    value.loc[:, ["DB EMPLOYMENT"]] = (
        (employment_total() / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB EMPLOYMENT"]}, 1)
        .values
    )
    value.loc[:, ["DB LABOUR FORCE"]] = (
        (labour_force() / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB LABOUR FORCE"]}, 1)
        .values
    )
    value.loc[:, ["DB UNEMPLOYMENT RATE"]] = (
        unemployment_rate()
        .expand_dims({"DASHBOARD ECONOMY I": ["DB UNEMPLOYMENT RATE"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV REVENUE"]] = (
        (zidz(government_revenue(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV REVENUE"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV EXPENDITURE"]] = (
        (zidz(government_expenditure(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV EXPENDITURE"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV BALANCE"]] = (
        (zidz(government_budget_balance(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV BALANCE"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV BALANCE TO GDP"]] = (
        zidz(
            zidz(government_budget_balance(), gross_domestic_product_deflator()),
            gross_domestic_product_real_supply_side(),
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV BALANCE TO GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV DEBT"]] = (
        (zidz(government_debt(), gross_domestic_product_deflator()) / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV DEBT"]}, 1)
        .values
    )
    value.loc[:, ["DB GOV DEBT TO GDP"]] = (
        zidz(
            zidz(government_debt(), gross_domestic_product_deflator()),
            gross_domestic_product_real_supply_side(),
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GOV DEBT TO GDP"]}, 1)
        .values
    )
    value.loc[:, ["DB HH DISPOSABLE INCOME"]] = (
        (disposable_income_real() / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH DISPOSABLE INCOME"]}, 1)
        .values
    )
    value.loc[:, ["DB HH CONSUMPTION COICOP"]] = (
        (
            sum(
                consumption_coicop_real().rename({"COICOP I": "COICOP I!"}),
                dim=["COICOP I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH CONSUMPTION COICOP"]}, 1)
        .values
    )
    value.loc[:, ["DB HH SAVINGS"]] = (
        (
            disposable_income_real() / 1000
            - sum(
                consumption_coicop_real().rename({"COICOP I": "COICOP I!"}),
                dim=["COICOP I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH SAVINGS"]}, 1)
        .values
    )
    value.loc[:, ["DB GDP PER CAPITA"]] = (
        (
            zidz(gross_domestic_product_real_supply_side(), population_35_regions())
            * unit_conversion_dollars_2015_mdollars_2015()
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB GDP PER CAPITA"]}, 1)
        .values
    )
    value.loc[:, ["DB DISPOSABLE INCOME PER CAPITA"]] = (
        (
            zidz(disposable_income_real(), population_35_regions())
            * unit_conversion_dollars_2015_mdollars_2015()
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB DISPOSABLE INCOME PER CAPITA"]}, 1)
        .values
    )
    value.loc[:, ["DB CONSUMER PRICE INDEX"]] = (
        consumer_price_index()
        .expand_dims({"DASHBOARD ECONOMY I": ["DB CONSUMER PRICE INDEX"]}, 1)
        .values
    )
    value.loc[:, ["DB HH DISPOSABLE INCOME NOMINAL"]] = (
        (disposable_income() / 1000)
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH DISPOSABLE INCOME NOMINAL"]}, 1)
        .values
    )
    value.loc[:, ["DB HH CONSUMPTION COICOP NOMINAL"]] = (
        (
            sum(
                consumption_coicop().rename({"COICOP I": "COICOP I!"}),
                dim=["COICOP I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH CONSUMPTION COICOP NOMINAL"]}, 1)
        .values
    )
    value.loc[:, ["DB HH SAVINGS NOMINAL"]] = (
        (
            disposable_income() / 1000
            - sum(
                consumption_coicop().rename({"COICOP I": "COICOP I!"}),
                dim=["COICOP I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB HH SAVINGS NOMINAL"]}, 1)
        .values
    )
    value.loc[:, ["DB OUTPUT"]] = (
        (
            sum(output_real().rename({"SECTORS I": "SECTORS I!"}), dim=["SECTORS I!"])
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB OUTPUT"]}, 1)
        .values
    )
    value.loc[:, ["DB CAPITAL STOCK"]] = (
        (
            sum(
                real_capital_stock().rename({"SECTORS I": "SECTORS I!"}),
                dim=["SECTORS I!"],
            )
            / 1000
        )
        .expand_dims({"DASHBOARD ECONOMY I": ["DB CAPITAL STOCK"]}, 1)
        .values
    )
    return value


@component.add(
    name="economy dashboard 1R",
    subscripts=["DASHBOARD ECONOMY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_dashboard_9r": 10,
        "population_9_regions": 2,
        "unit_conversion_dollars_2015_mdollars_2015": 2,
        "weights_consumption_9r": 1,
    },
)
def economy_dashboard_1r():
    """
    Dashboard of the economy_ EU27. Monetary values in 1000 Million USD 2015 prices. per capita vaules in USD 2015. Employment in million of people.
    """
    value = xr.DataArray(
        np.nan,
        {"DASHBOARD ECONOMY I": _subscript_dict["DASHBOARD ECONOMY I"]},
        ["DASHBOARD ECONOMY I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[["DB UNEMPLOYMENT RATE"]] = False
    except_subs.loc[["DB GOV BALANCE TO GDP"]] = False
    except_subs.loc[["DB GOV DEBT TO GDP"]] = False
    except_subs.loc[["DB GDP PER CAPITA"]] = False
    except_subs.loc[["DB DISPOSABLE INCOME PER CAPITA"]] = False
    except_subs.loc[["DB CONSUMER PRICE INDEX"]] = False
    value.values[except_subs.values] = sum(
        economy_dashboard_9r().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    ).values[except_subs.values]
    value.loc[["DB UNEMPLOYMENT RATE"]] = 1 - zidz(
        sum(
            economy_dashboard_9r()
            .loc[:, "DB EMPLOYMENT"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
        sum(
            economy_dashboard_9r()
            .loc[:, "DB LABOUR FORCE"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )
    value.loc[["DB GOV BALANCE TO GDP"]] = zidz(
        sum(
            economy_dashboard_9r()
            .loc[:, "DB GOV BALANCE"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
        sum(
            economy_dashboard_9r()
            .loc[:, "DB GDP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )
    value.loc[["DB GOV DEBT TO GDP"]] = zidz(
        sum(
            economy_dashboard_9r()
            .loc[:, "DB GOV DEBT"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
        sum(
            economy_dashboard_9r()
            .loc[:, "DB GDP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )
    value.loc[["DB GDP PER CAPITA"]] = (
        zidz(
            sum(
                economy_dashboard_9r()
                .loc[:, "DB GDP"]
                .reset_coords(drop=True)
                .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                dim=["REGIONS 9 I!"],
            ),
            sum(
                population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                dim=["REGIONS 9 I!"],
            ),
        )
        * unit_conversion_dollars_2015_mdollars_2015()
        * 1000
    )
    value.loc[["DB DISPOSABLE INCOME PER CAPITA"]] = (
        zidz(
            sum(
                economy_dashboard_9r()
                .loc[:, "DB HH DISPOSABLE INCOME"]
                .reset_coords(drop=True)
                .rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                dim=["REGIONS 9 I!"],
            ),
            sum(
                population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
                dim=["REGIONS 9 I!"],
            ),
        )
        * unit_conversion_dollars_2015_mdollars_2015()
        * 1000
    )
    value.loc[["DB CONSUMER PRICE INDEX"]] = sum(
        economy_dashboard_9r()
        .loc[:, "DB CONSUMER PRICE INDEX"]
        .reset_coords(drop=True)
        .rename({"REGIONS 9 I": "REGIONS 9 I!"})
        * weights_consumption_9r().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )
    return value


@component.add(
    name="economy dashboard 9R",
    subscripts=["REGIONS 9 I", "DASHBOARD ECONOMY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"economy_dashboard": 1, "economy_dashboard_eu27": 1},
)
def economy_dashboard_9r():
    """
    Dashboard of the economy: 9 regions. Monetary values in 1000 Million USD 2015 prices. per capita vaules in USD 2015. Employment in million of people.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "DASHBOARD ECONOMY I": _subscript_dict["DASHBOARD ECONOMY I"],
        },
        ["REGIONS 9 I", "DASHBOARD ECONOMY I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        economy_dashboard()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"], :] = (
        economy_dashboard_eu27()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="economy dashboard EU27",
    subscripts=["REGIONS 36 I", "DASHBOARD ECONOMY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_dashboard": 10,
        "population_35_regions": 2,
        "unit_conversion_dollars_2015_mdollars_2015": 2,
        "weights_consumption_eu27": 1,
    },
)
def economy_dashboard_eu27():
    """
    Dashboard of the economy: EU27. Monetary values in 1000 Million USD 2015 prices. per capita vaules in USD 2015. Employment in million of people.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "DASHBOARD ECONOMY I": _subscript_dict["DASHBOARD ECONOMY I"],
        },
        ["REGIONS 36 I", "DASHBOARD ECONOMY I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[["EU27"], :] = True
    except_subs.loc[["EU27"], ["DB UNEMPLOYMENT RATE"]] = False
    except_subs.loc[["EU27"], ["DB GOV BALANCE TO GDP"]] = False
    except_subs.loc[["EU27"], ["DB GOV DEBT TO GDP"]] = False
    except_subs.loc[["EU27"], ["DB GDP PER CAPITA"]] = False
    except_subs.loc[["EU27"], ["DB DISPOSABLE INCOME PER CAPITA"]] = False
    except_subs.loc[["EU27"], ["DB CONSUMER PRICE INDEX"]] = False
    value.values[except_subs.values] = (
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values[except_subs.loc[["EU27"], :].values]
    )
    value.loc[["EU27"], ["DB UNEMPLOYMENT RATE"]] = 1 - zidz(
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB EMPLOYMENT"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB LABOUR FORCE"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
    )
    value.loc[["EU27"], ["DB GOV BALANCE TO GDP"]] = zidz(
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB GOV BALANCE"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB GDP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
    )
    value.loc[["EU27"], ["DB GOV DEBT TO GDP"]] = zidz(
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB GOV DEBT"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 I"], "DB GDP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        ),
    )
    value.loc[["EU27"], ["DB GDP PER CAPITA"]] = (
        zidz(
            sum(
                economy_dashboard()
                .loc[_subscript_dict["REGIONS EU27 I"], "DB GDP"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
            sum(
                population_35_regions()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
        )
        * unit_conversion_dollars_2015_mdollars_2015()
        * 1000
    )
    value.loc[["EU27"], ["DB DISPOSABLE INCOME PER CAPITA"]] = (
        zidz(
            sum(
                economy_dashboard()
                .loc[_subscript_dict["REGIONS EU27 I"], "DB HH DISPOSABLE INCOME"]
                .reset_coords(drop=True)
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
            sum(
                population_35_regions()
                .loc[_subscript_dict["REGIONS EU27 I"]]
                .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
                dim=["REGIONS EU27 I!"],
            ),
        )
        * unit_conversion_dollars_2015_mdollars_2015()
        * 1000
    )
    value.loc[["EU27"], ["DB CONSUMER PRICE INDEX"]] = sum(
        economy_dashboard()
        .loc[_subscript_dict["REGIONS EU27 I"], "DB CONSUMER PRICE INDEX"]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"})
        * weights_consumption_eu27().rename({"REGIONS EU27 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )
    return value


@component.add(
    name="GDP real 1R",
    units="Mdollars 2015/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"economy_dashboard_1r": 1},
)
def gdp_real_1r():
    """
    Gross domestic product in real terms: World
    """
    return float(economy_dashboard_1r().loc["DB GDP"]) * 1000


@component.add(
    name="GDP real 9R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"economy_dashboard_9r": 1},
)
def gdp_real_9r():
    """
    Gross domestic product in real terms: 9 regions
    """
    return economy_dashboard_9r().loc[:, "DB GDP"].reset_coords(drop=True) * 1000


@component.add(
    name="GDP real index",
    units="DMNL",
    subscripts=["REGIONS 36 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_dashboard": 1,
        "initial_gross_domestic_product_real_supply_side": 2,
        "economy_dashboard_9r": 1,
    },
)
def gdp_real_index():
    """
    GDP real index (2015=100)
    """
    value = xr.DataArray(
        np.nan, {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, ["REGIONS 36 I"]
    )
    value.loc[_subscript_dict["REGIONS 35 I"]] = (
        zidz(
            economy_dashboard().loc[:, "DB GDP"].reset_coords(drop=True),
            initial_gross_domestic_product_real_supply_side()
            .loc[_subscript_dict["REGIONS 35 I"]]
            .rename({"REGIONS 36 I": "REGIONS 35 I"}),
        )
        * 100
    ).values
    value.loc[["EU27"]] = (
        zidz(
            float(economy_dashboard_9r().loc["EU27", "DB GDP"]),
            float(initial_gross_domestic_product_real_supply_side().loc["EU27"]),
        )
        * 100
    )
    return value


@component.add(
    name="GDPpc 9R real",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "economy_dashboard_9r": 1,
        "unit_conversion_dollars_2015_mdollars_2015": 1,
    },
)
def gdppc_9r_real():
    """
    Gross domestic product per capita in real terms: 9 regions
    """
    return (
        economy_dashboard_9r().loc[:, "DB GDP PER CAPITA"].reset_coords(drop=True)
        / unit_conversion_dollars_2015_mdollars_2015()
    )


@component.add(
    name="INITIAL GROSS DOMESTIC PRODUCT REAL SUPPLY SIDE",
    subscripts=["REGIONS 36 I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={
        "_initial_initial_gross_domestic_product_real_supply_side": 1,
        "_initial_initial_gross_domestic_product_real_supply_side_1": 1,
    },
    other_deps={
        "_initial_initial_gross_domestic_product_real_supply_side": {
            "initial": {"economy_dashboard": 1},
            "step": {},
        },
        "_initial_initial_gross_domestic_product_real_supply_side_1": {
            "initial": {"economy_dashboard_9r": 1},
            "step": {},
        },
    },
)
def initial_gross_domestic_product_real_supply_side():
    value = xr.DataArray(
        np.nan, {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, ["REGIONS 36 I"]
    )
    value.loc[_subscript_dict["REGIONS 35 I"]] = (
        _initial_initial_gross_domestic_product_real_supply_side().values
    )
    value.loc[["EU27"]] = (
        _initial_initial_gross_domestic_product_real_supply_side_1().values
    )
    return value


_initial_initial_gross_domestic_product_real_supply_side = Initial(
    lambda: economy_dashboard().loc[:, "DB GDP"].reset_coords(drop=True),
    "_initial_initial_gross_domestic_product_real_supply_side",
)

_initial_initial_gross_domestic_product_real_supply_side_1 = Initial(
    lambda: xr.DataArray(
        float(economy_dashboard_9r().loc["EU27", "DB GDP"]),
        {"REGIONS 36 I": ["EU27"]},
        ["REGIONS 36 I"],
    ),
    "_initial_initial_gross_domestic_product_real_supply_side_1",
)


@component.add(
    name="weights consumption 9R",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"economy_dashboard_9r": 2},
)
def weights_consumption_9r():
    """
    Shares of the 9 regions in total world consumption. This is used to calcaute weighted consumer price index of the world
    """
    return zidz(
        economy_dashboard_9r()
        .loc[:, "DB HH CONSUMPTION COICOP"]
        .reset_coords(drop=True),
        sum(
            economy_dashboard_9r()
            .loc[:, "DB HH CONSUMPTION COICOP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 9 I": "REGIONS 9 MAP I!"}),
            dim=["REGIONS 9 MAP I!"],
        ),
    )


@component.add(
    name="weights consumption EU27",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"economy_dashboard": 2},
)
def weights_consumption_eu27():
    """
    EU27 sahres in total consumption of the EU27. This is used to calcaute weighted consumer price index of the EU27
    """
    return zidz(
        economy_dashboard()
        .loc[_subscript_dict["REGIONS EU27 I"], "DB HH CONSUMPTION COICOP"]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 I": "REGIONS EU27 I"}),
        sum(
            economy_dashboard()
            .loc[_subscript_dict["REGIONS EU27 MAP I"], "DB HH CONSUMPTION COICOP"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 I": "REGIONS EU27 MAP I!"}),
            dim=["REGIONS EU27 MAP I!"],
        ),
    )
