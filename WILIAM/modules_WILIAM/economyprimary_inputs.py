"""
Module economyprimary_inputs
Translated using PySD version 3.14.0
"""

@component.add(
    name="delayed TS net operating surplus",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_net_operating_surplus": 1},
    other_deps={
        "_delayfixed_delayed_ts_net_operating_surplus": {
            "initial": {"initial_delayed_net_operating_surplus": 1, "time_step": 1},
            "step": {"net_operating_surplus": 1},
        }
    },
)
def delayed_ts_net_operating_surplus():
    """
    Delayed net operating surplus
    """
    return _delayfixed_delayed_ts_net_operating_surplus()


_delayfixed_delayed_ts_net_operating_surplus = DelayFixed(
    lambda: net_operating_surplus().rename(
        {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
    ),
    lambda: time_step(),
    lambda: initial_delayed_net_operating_surplus(),
    time_step,
    "_delayfixed_delayed_ts_net_operating_surplus",
)


@component.add(
    name="delayed TS net operating surplus exc scarcity rents",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_delayed_net_operating_surplus": 1,
        "initial_delayed_net_operating_surplus_to_output_real": 2,
        "delayed_ts_net_operating_surplus": 1,
        "delayed_ts_output_real": 1,
        "delayed_ts_net_operating_surplus_to_output_real": 1,
    },
)
def delayed_ts_net_operating_surplus_exc_scarcity_rents():
    """
    Delayed net operating surplus excluding scarcity rents. IF_THEN_ELSE(Time <=2015,INITIAL_DELAYED_NET_OPERATING_SURPLUS[REGIONS_35_I,SECTORS_EXTRACTIO N_I],IF_THEN_ELSE(delayed_TS_net_operating_surplus_to_output_real [REGIONS_35_I,SECTORS_EXTRACTION_I]<=1.1*INITIAL_DELAYED_NET_OPERATING_SURPLUS_TO_OUT PUT_REAL[REGIONS_35_I,SECTORS_EXTRACTION_I],delayed_TS_net_operating_surplu s [REGIONS_35_I,SECTORS_EXTRACTION_I],1.1*INITIAL_DELAYED_NET_OPERATING_SURPLUS_TO_OUTP UT_REAL[REGIONS_35_I,SECTORS_EXTRACTION_I]* delayed_TS_output_real [REGIONS_35_I,SECTORS_EXTRACTION_I]))
    """
    return if_then_else(
        time() <= 2015,
        lambda: initial_delayed_net_operating_surplus(),
        lambda: if_then_else(
            delayed_ts_net_operating_surplus_to_output_real()
            <= 1.1 * initial_delayed_net_operating_surplus_to_output_real(),
            lambda: delayed_ts_net_operating_surplus(),
            lambda: 1.1
            * initial_delayed_net_operating_surplus_to_output_real()
            * delayed_ts_output_real(),
        ),
    )


@component.add(
    name="delayed TS net operating surplus to output real",
    units="Mdollars/Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"delayed_ts_net_operating_surplus": 1, "delayed_ts_output_real": 1},
)
def delayed_ts_net_operating_surplus_to_output_real():
    """
    Ratio net operating surplus to real output
    """
    return zidz(delayed_ts_net_operating_surplus(), delayed_ts_output_real())


@component.add(
    name="delayed TS net operating surplus total",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_net_operating_surplus": 1,
        "delayed_ts_net_operating_surplus": 1,
    },
)
def delayed_ts_net_operating_surplus_total():
    """
    Delayed total net operating surplus.
    """
    return if_then_else(
        time() <= 2015,
        lambda: initial_net_operating_surplus(),
        lambda: sum(
            delayed_ts_net_operating_surplus().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="delayed TS total net operating surplus distributed to households",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "delayed_ts_net_operating_surplus": 1,
        "delayed_ts_net_operating_surplus_exc_scarcity_rents": 1,
    },
)
def delayed_ts_total_net_operating_surplus_distributed_to_households():
    """
    Total net operating surplus distributed to households
    """
    return if_then_else(
        time() <= 2015,
        lambda: sum(
            delayed_ts_net_operating_surplus().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
        lambda: sum(
            delayed_ts_net_operating_surplus_exc_scarcity_rents().rename(
                {"SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="gross domestic product deflator",
    units="Mdollars/Mdollars 2015",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_nominal": 1,
        "gross_domestic_product_real_supply_side": 1,
    },
)
def gross_domestic_product_deflator():
    """
    Deflator of the gross domestic product
    """
    return zidz(
        gross_domestic_product_nominal(), gross_domestic_product_real_supply_side()
    )


@component.add(
    name="gross domestic product nominal",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_value_added": 1,
        "taxes_products_by_sector": 1,
        "taxes_products_final_demand": 1,
        "tax_ghg_paid_by_sector": 1,
        "taxes_on_resources_paid_by_extraction_sectors": 1,
        "tax_ghg_households": 1,
    },
)
def gross_domestic_product_nominal():
    """
    Gross domestic product in nominal terms.
    """
    return (
        sum(
            gross_value_added().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_products_by_sector().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_products_final_demand().rename(
                {
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                    "FINAL DEMAND I": "FINAL DEMAND I!",
                }
            ),
            dim=["FINAL DEMAND I!"],
        )
        + sum(
            tax_ghg_paid_by_sector().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_on_resources_paid_by_extraction_sectors().rename(
                {"SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + tax_ghg_households()
    )


@component.add(
    name="gross domestic product real demand side",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_dometic_in_basic_prices_real_by_component": 1,
        "final_demand_imports_in_basic_prices_real_by_component": 1,
        "total_exports_real_by_product": 1,
        "total_imports_real_by_product": 1,
        "taxes_products_final_demand_real": 1,
    },
)
def gross_domestic_product_real_demand_side():
    """
    Gross domrestic product in real terms from the demand side
    """
    return (
        sum(
            final_demand_dometic_in_basic_prices_real_by_component().rename(
                {"FINAL DEMAND I": "FINAL DEMAND I!"}
            ),
            dim=["FINAL DEMAND I!"],
        )
        + sum(
            final_demand_imports_in_basic_prices_real_by_component().rename(
                {"FINAL DEMAND I": "FINAL DEMAND I!"}
            ),
            dim=["FINAL DEMAND I!"],
        )
        + sum(
            total_exports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        )
        - sum(
            total_imports_real_by_product().rename({"SECTORS I": "SECTORS I!"}),
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


@component.add(
    name="gross domestic product real supply side",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_value_added_real": 1,
        "taxes_products_by_sector_real": 1,
        "taxes_products_final_demand_real": 1,
    },
)
def gross_domestic_product_real_supply_side():
    """
    Gross domestic porduct in real terms calculated from the supply side
    """
    return (
        sum(
            gross_value_added_real().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_products_by_sector_real().rename(
                {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I!"}
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


@component.add(
    name="gross value added",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_consumption_fixed_capital_real": 1,
        "net_value_added": 2,
        "consumption_fixed_capital": 1,
    },
)
def gross_value_added():
    """
    Gross value added in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: net_value_added().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        + initial_consumption_fixed_capital_real().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        ),
        lambda: net_value_added().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        + consumption_fixed_capital().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        ),
    )


@component.add(
    name="gross value added real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_intermediates_domestic_real": 1,
        "taxes_products_by_sector_real": 2,
        "base_output_real": 1,
        "initial_intermediate_imports_and_exports_real": 1,
        "output_real": 1,
        "intermediates_domestic_real": 1,
        "intermediate_imports_and_exports_real": 1,
    },
)
def gross_value_added_real():
    """
    Gross value added in real terms
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: base_output_real().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        - sum(
            initial_intermediates_domestic_real().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        - sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        )
        - taxes_products_by_sector_real(),
        lambda: output_real().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        - sum(
            intermediates_domestic_real().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        - sum(
            intermediate_imports_and_exports_real().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        )
        - taxes_products_by_sector_real(),
    )


@component.add(
    name="INITIAL DELAYED NET OPERATING SURPLUS TO OUTPUT REAL",
    units="Mdollars/Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_delayed_net_operating_surplus_to_output_real": 1},
    other_deps={
        "_initial_initial_delayed_net_operating_surplus_to_output_real": {
            "initial": {
                "initial_delayed_net_operating_surplus": 1,
                "delayed_ts_output_real": 1,
            },
            "step": {},
        }
    },
)
def initial_delayed_net_operating_surplus_to_output_real():
    """
    Initial ratio delayed net operating surplus to output real
    """
    return _initial_initial_delayed_net_operating_surplus_to_output_real()


_initial_initial_delayed_net_operating_surplus_to_output_real = Initial(
    lambda: zidz(initial_delayed_net_operating_surplus(), delayed_ts_output_real()),
    "_initial_initial_delayed_net_operating_surplus_to_output_real",
)


@component.add(
    name="INITIAL INTERMEDIATE IMPORTS AND EXPORTS REAL",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_intermediate_imports_and_exports_real": 1},
    other_deps={
        "_initial_initial_intermediate_imports_and_exports_real": {
            "initial": {"intermediate_imports_and_exports_real": 1},
            "step": {},
        }
    },
)
def initial_intermediate_imports_and_exports_real():
    return _initial_initial_intermediate_imports_and_exports_real()


_initial_initial_intermediate_imports_and_exports_real = Initial(
    lambda: intermediate_imports_and_exports_real(),
    "_initial_initial_intermediate_imports_and_exports_real",
)


@component.add(
    name="INITIAL INTERMEDIATES DOMESTIC REAL",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_intermediates_domestic_real": 1},
    other_deps={
        "_initial_initial_intermediates_domestic_real": {
            "initial": {"intermediates_domestic_real": 1},
            "step": {},
        }
    },
)
def initial_intermediates_domestic_real():
    """
    Initial value for variable intermediates_domestic_real
    """
    return _initial_initial_intermediates_domestic_real()


_initial_initial_intermediates_domestic_real = Initial(
    lambda: intermediates_domestic_real(),
    "_initial_initial_intermediates_domestic_real",
)


@component.add(
    name="INITIAL TAXES PRODUCTS DOMESTIC",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_taxes_products_domestic": 1},
    other_deps={
        "_initial_initial_taxes_products_domestic": {
            "initial": {
                "taxes_products_domestic_final_demand_real": 1,
                "mdollars_per_mdollars_2015": 1,
            },
            "step": {},
        }
    },
)
def initial_taxes_products_domestic():
    return _initial_initial_taxes_products_domestic()


_initial_initial_taxes_products_domestic = Initial(
    lambda: taxes_products_domestic_final_demand_real() * mdollars_per_mdollars_2015(),
    "_initial_initial_taxes_products_domestic",
)


@component.add(
    name="INITIAL TAXES PRODUCTS IMPORTS",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_taxes_products_imports": 1},
    other_deps={
        "_initial_initial_taxes_products_imports": {
            "initial": {
                "taxes_products_imports_final_demand_real": 1,
                "mdollars_per_mdollars_2015": 1,
            },
            "step": {},
        }
    },
)
def initial_taxes_products_imports():
    return _initial_initial_taxes_products_imports()


_initial_initial_taxes_products_imports = Initial(
    lambda: taxes_products_imports_final_demand_real() * mdollars_per_mdollars_2015(),
    "_initial_initial_taxes_products_imports",
)


@component.add(
    name="labour compensation real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_value_added_real": 1,
        "taxes_production_real": 1,
        "share_labour_compensation_net_value_added": 1,
    },
)
def labour_compensation_real():
    """
    Labour compensation in real terms.
    """
    return (
        net_value_added_real() - taxes_production_real()
    ) * share_labour_compensation_net_value_added()


@component.add(
    name="net domestic product real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "gross_domestic_product_real_supply_side": 2,
        "initial_consumption_fixed_capital_real": 1,
        "consumption_fixed_capital_real": 1,
    },
)
def net_domestic_product_real():
    """
    Net domestic product in real terms. This is equivalent to GDP but removing the part of the investments associated with the replacement of capital due to depreciation and climate change damages.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: gross_domestic_product_real_supply_side()
        - sum(
            initial_consumption_fixed_capital_real().rename(
                {"SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        ),
        lambda: gross_domestic_product_real_supply_side()
        - sum(
            consumption_fixed_capital_real().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="net operating surplus",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "mark_up": 1,
        "output_real": 1,
        "price_output": 1,
        "price_transformation": 1,
        "mdollars_per_mdollars_2015": 1,
    },
)
def net_operating_surplus():
    """
    Gross value added in nominal terms.
    """
    return (
        mark_up().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        * output_real().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        * price_output().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
        )
        / price_transformation()
        * mdollars_per_mdollars_2015()
    )


@component.add(
    name="net operating surplus real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "net_value_added_real": 1,
        "labour_compensation_real": 1,
        "taxes_production_real": 1,
    },
)
def net_operating_surplus_real():
    """
    Net operating surplus in real terms.
    """
    return net_value_added_real() - labour_compensation_real() - taxes_production_real()


@component.add(
    name="net value added",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_taxes_production": 1,
        "initial_labour_compensation": 1,
        "net_operating_surplus": 2,
        "labour_compensation": 1,
        "taxes_production": 1,
    },
)
def net_value_added():
    """
    Net value added in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: net_operating_surplus().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        )
        + initial_labour_compensation()
        + initial_taxes_production(),
        lambda: net_operating_surplus().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        )
        + labour_compensation()
        + taxes_production(),
    )


@component.add(
    name="net value added real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "gross_value_added_real": 2,
        "initial_consumption_fixed_capital_real": 1,
        "consumption_fixed_capital_real": 1,
    },
)
def net_value_added_real():
    """
    Net value added in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: gross_value_added_real().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        )
        - initial_consumption_fixed_capital_real(),
        lambda: gross_value_added_real().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"}
        )
        - consumption_fixed_capital_real(),
    )


@component.add(
    name="non distributed operating surplus and scarcity rents",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_total_net_operating_surplus_distributed_to_households": 1,
        "households_net_operating_surplus": 1,
        "number_of_households_by_income_and_type": 1,
        "unit_conversion_dollars_mdollars": 1,
        "scarcity_rents": 1,
    },
)
def non_distributed_operating_surplus_and_scarcity_rents():
    """
    Non distributed operating surplus and scarcity rents
    """
    return (
        delayed_ts_total_net_operating_surplus_distributed_to_households()
        - sum(
            households_net_operating_surplus().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        )
        / unit_conversion_dollars_mdollars()
        + scarcity_rents()
    )


@component.add(
    name="scarcity rents",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_net_operating_surplus_total": 1,
        "delayed_ts_total_net_operating_surplus_distributed_to_households": 1,
    },
)
def scarcity_rents():
    """
    Scarcity rents due to tdightness between the demad and suppluy of materials and/or labour. These rents are accumulated and are not distributed to households
    """
    return (
        delayed_ts_net_operating_surplus_total()
        - delayed_ts_total_net_operating_surplus_distributed_to_households()
    )


@component.add(
    name="share labour compensation net value added",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation": 1, "taxes_production": 1, "net_value_added": 1},
)
def share_labour_compensation_net_value_added():
    """
    Share of labour compensation over net value added.
    """
    return zidz(labour_compensation(), net_value_added() - taxes_production())


@component.add(
    name="Stock of non distributed operating surplus and scarcity rents",
    units="Mdollars",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={
        "_integ_stock_of_non_distributed_operating_surplus_and_scarcity_rents": 1
    },
    other_deps={
        "_integ_stock_of_non_distributed_operating_surplus_and_scarcity_rents": {
            "initial": {},
            "step": {
                "time": 1,
                "non_distributed_operating_surplus_and_scarcity_rents": 1,
            },
        }
    },
)
def stock_of_non_distributed_operating_surplus_and_scarcity_rents():
    """
    Stock of non distributed operating surplus and scarcity rents
    """
    return _integ_stock_of_non_distributed_operating_surplus_and_scarcity_rents()


_integ_stock_of_non_distributed_operating_surplus_and_scarcity_rents = Integ(
    lambda: if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: non_distributed_operating_surplus_and_scarcity_rents(),
    ),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    "_integ_stock_of_non_distributed_operating_surplus_and_scarcity_rents",
)


@component.add(
    name="SWITCH ECO PRIMARY INPUTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_primary_inputs"},
)
def switch_eco_primary_inputs():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_primary_inputs()


_ext_constant_switch_eco_primary_inputs = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PRIMARY_INPUTS",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_primary_inputs",
)


@component.add(
    name="taxes production",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "mdollars_per_mdollars_2015": 2,
        "base_output_real": 1,
        "initial_price_of_output": 1,
        "price_transformation": 2,
        "tax_rate_production": 2,
        "output_real": 1,
        "price_output": 1,
    },
)
def taxes_production():
    """
    Taxes on production in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: tax_rate_production()
        * base_output_real()
        * zidz(initial_price_of_output(), price_transformation())
        * mdollars_per_mdollars_2015(),
        lambda: tax_rate_production()
        * output_real()
        * zidz(price_output(), price_transformation())
        * mdollars_per_mdollars_2015(),
    )


@component.add(
    name="taxes production real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "tax_rate_output_default_default": 1,
        "switch_eco_primary_inputs": 1,
        "base_output_real": 1,
        "output_real": 1,
    },
)
def taxes_production_real():
    """
    Net taxes on production in real terms.
    """
    return tax_rate_output_default_default() * if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: base_output_real(),
        lambda: output_real(),
    )


@component.add(
    name="taxes products by sector",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_products_domestic_by_sector": 1,
        "taxes_products_imports_by_sector": 1,
    },
)
def taxes_products_by_sector():
    """
    Net taxes on products by sector in nominal terms.
    """
    return taxes_products_domestic_by_sector().rename(
        {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
    ) + sum(
        taxes_products_imports_by_sector().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS MAP I"}
        ),
        dim=["REGIONS 35 I!"],
    )


@component.add(
    name="taxes products by sector real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "taxes_products_domestic_by_sector_real": 1,
        "taxes_products_imports_by_sector_real": 1,
    },
)
def taxes_products_by_sector_real():
    """
    Net taxes on products paid by sectors in real terms.
    """
    return taxes_products_domestic_by_sector_real().rename(
        {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
    ) + sum(
        taxes_products_imports_by_sector_real().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS MAP I"}
        ),
        dim=["REGIONS 35 I!"],
    )


@component.add(
    name="taxes products domestic by sector",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_intermediates_domestic_real": 1,
        "mdollars_per_mdollars_2015": 2,
        "initial_price_of_output": 1,
        "price_transformation": 2,
        "trade_and_transportation_margins_paid_for_domestic_products_by_sectors": 2,
        "tax_rate_products_domestic_by_sectors_default": 2,
        "intermediates_domestic_real": 1,
        "price_output": 1,
    },
)
def taxes_products_domestic_by_sector():
    """
    Net taxes on domestic products by sector in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediates_domestic_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (initial_price_of_output() / price_transformation())
            * mdollars_per_mdollars_2015()
            * (
                1
                + trade_and_transportation_margins_paid_for_domestic_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_domestic_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
        lambda: sum(
            intermediates_domestic_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (
                price_output().rename({"SECTORS I": "SECTORS MAP I!"})
                / price_transformation()
            )
            * mdollars_per_mdollars_2015()
            * (
                1
                + trade_and_transportation_margins_paid_for_domestic_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_domestic_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
    )


@component.add(
    name="taxes products domestic by sector real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_intermediates_domestic_real": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_by_sectors": 2,
        "tax_rate_products_domestic_by_sectors_default": 2,
        "intermediates_domestic_real": 1,
    },
)
def taxes_products_domestic_by_sector_real():
    """
    Net taxes on domestic products paid by sectors in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediates_domestic_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (
                1
                + trade_and_transportation_margins_paid_for_domestic_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_domestic_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
        lambda: sum(
            intermediates_domestic_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (
                1
                + trade_and_transportation_margins_paid_for_domestic_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_domestic_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
    )


@component.add(
    name="taxes products final demand",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_taxes_products_imports": 1,
        "initial_taxes_products_domestic": 1,
        "taxes_products_imports_final_demand": 1,
        "taxes_products_domestic_final_demand": 1,
    },
)
def taxes_products_final_demand():
    """
    Net taxes on final products in nominal terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_taxes_products_domestic().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            initial_taxes_products_imports().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        ),
        lambda: sum(
            taxes_products_domestic_final_demand().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_products_imports_final_demand().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        ),
    )


@component.add(
    name="taxes products final demand real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 MAP I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_taxes_products_imports": 1,
        "initial_taxes_products_domestic": 1,
        "taxes_products_imports_final_demand_real": 1,
        "taxes_products_domestic_final_demand_real": 1,
    },
)
def taxes_products_final_demand_real():
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_taxes_products_domestic().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            initial_taxes_products_imports().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        ),
        lambda: sum(
            taxes_products_domestic_final_demand_real().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS I!"}
            ),
            dim=["SECTORS I!"],
        )
        + sum(
            taxes_products_imports_final_demand_real().rename(
                {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
            ),
            dim=["REGIONS 35 I!", "SECTORS I!"],
        ),
    )


@component.add(
    name="taxes products imports by sector",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "REGIONS 35 MAP I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_intermediate_imports_and_exports_real": 1,
        "mdollars_per_mdollars_2015": 2,
        "tax_rate_products_imports_by_sectors_default": 2,
        "initial_price_of_output": 1,
        "price_transformation": 2,
        "trade_and_transportation_margins_paid_for_imported_products_by_sectors": 2,
        "price_output": 1,
        "intermediate_imports_and_exports_real": 1,
    },
)
def taxes_products_imports_by_sector():
    """
    Net taxes on imported products by sector in nominal terms. IF_THEN_ELSE(SWITCH_ECO_PRIMARY_INPUTS=0, SUM(INITIAL_INTERMEDIATE_IMPORTS_AND_EXPORTS_REAL[REGIONS 35 I,SECTORS MAP I!,REGIONS 35 MAP I,SECTORS I]* (BASE_PRICE_OUTPUT[REGIONS 35 I ,SECTORS MAP I!]/PRICE_TRANSFORMATION))*TAX_RATE_INTERMEDIATE_PRODUCTS_IMPORTS_AGGREGATE D[REGIONS 35 I,REGIONS 35 MAP I ,SECTORS I ],SUM(intermediate_imports_and_exports_real[REGIONS 35 I,SECTORS MAP I!,REGIONS 35 MAP I,SECTORS I]*(price_output [REGIONS 35 I ,SECTORS MAP I!]/PRICE_TRANSFORMATION))*TAX_RATE_INTERMEDIATE_PRODUCTS_IMPORTS_AGGREGATE D[REGIONS 35 I,REGIONS 35 MAP I ,SECTORS I ])
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (initial_price_of_output() / price_transformation())
            * mdollars_per_mdollars_2015()
            * (
                1
                + trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_imports_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
        lambda: sum(
            intermediate_imports_and_exports_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * (
                price_output().rename({"SECTORS I": "SECTORS MAP I!"})
                / price_transformation()
            )
            * mdollars_per_mdollars_2015()
            * (
                1
                + trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                    {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                )
            )
            * tax_rate_products_imports_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
    )


@component.add(
    name="taxes products imports by sector real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "REGIONS 35 MAP I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_primary_inputs": 1,
        "initial_intermediate_imports_and_exports_real": 1,
        "tax_rate_products_imports_by_sectors_default": 2,
        "trade_and_transportation_margins_paid_for_imported_products_by_sectors": 2,
        "intermediate_imports_and_exports_real": 1,
    },
)
def taxes_products_imports_by_sector_real():
    """
    Net taxes on imported products paid by sectors in real terms.
    """
    return if_then_else(
        switch_eco_primary_inputs() == 0,
        lambda: sum(
            initial_intermediate_imports_and_exports_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * tax_rate_products_imports_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
        lambda: sum(
            intermediate_imports_and_exports_real().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            )
            * tax_rate_products_imports_by_sectors_default().rename(
                {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
            ),
            dim=["SECTORS MAP I!"],
        ),
    )
