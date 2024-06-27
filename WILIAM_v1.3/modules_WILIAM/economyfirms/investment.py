"""
Module economyfirms.investment
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual change capital productivity sp",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_capital_productivity_variation_sp": 1,
        "initial_year_capital_productivity_variation_sp": 1,
        "time": 1,
        "capital_productivity_variation_sp": 1,
        "capital_productivity_variation_default": 1,
    },
)
def annual_change_capital_productivity_sp():
    """
    Annual change in capital productivity
    """
    return if_then_else(
        np.logical_and(
            select_capital_productivity_variation_sp() == 1,
            time() >= initial_year_capital_productivity_variation_sp(),
        ),
        lambda: capital_productivity_variation_sp(),
        lambda: capital_productivity_variation_default(),
    )


@component.add(
    name="capital depreciation",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"real_capital_stock": 1, "depreciation_rate": 1},
)
def capital_depreciation():
    """
    Capital depreciation: decline in the value of the stock of capital. Note that the depreciation rate is annual, thus it is divided by the time step
    """
    return real_capital_stock() * depreciation_rate()


@component.add(
    name="capital productivity",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_capital_productivity": 1},
    other_deps={
        "_integ_capital_productivity": {
            "initial": {"initial_capital_productivity": 1},
            "step": {"time": 1, "change_capital_productivity": 1},
        }
    },
)
def capital_productivity():
    """
    Capital productivity
    """
    return _integ_capital_productivity()


_integ_capital_productivity = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: change_capital_productivity(),
    ),
    lambda: initial_capital_productivity(),
    "_integ_capital_productivity",
)


@component.add(
    name="CAPITAL PRODUCTIVITY VARIATION SP",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_capital_productivity_variation_sp"},
)
def capital_productivity_variation_sp():
    return _ext_constant_capital_productivity_variation_sp()


_ext_constant_capital_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "CAPITAL_PRODUCTIVITY_GROWTH_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_capital_productivity_variation_sp",
)


@component.add(
    name="change capital productivity",
    units="1/(Year*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"annual_change_capital_productivity_sp": 1, "capital_productivity": 1},
)
def change_capital_productivity():
    """
    Change capital productivity
    """
    return annual_change_capital_productivity_sp() * capital_productivity()


@component.add(
    name="climate change damage on capital stock",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate_change_damage": 1,
        "switch_eco_climate_change_damage_capital": 1,
        "switch_eco_investment": 1,
        "climate_change_incremental_damage_rate_to_capital_stock": 1,
        "real_capital_stock": 1,
        "climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included": 1,
        "select_climate_change_impacts_sensitivity_sp": 1,
    },
)
def climate_change_damage_on_capital_stock():
    """
    Damages of the capital stock due to climate change. When the investment switch is deactivated it takes the value zero directly, as it would normally take the 2015 value but "Climate change damage rate to capital stock adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage." This happens for both the other variables coming from the view of climate economic damages.
    """
    return if_then_else(
        np.logical_or(
            switch_climate_change_damage() == 0,
            np.logical_or(
                switch_eco_climate_change_damage_capital() == 0,
                switch_eco_investment() == 0,
            ),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: real_capital_stock()
        * if_then_else(
            select_climate_change_impacts_sensitivity_sp() == 0,
            lambda: climate_change_incremental_damage_rate_to_capital_stock(),
            lambda: climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included(),
        ),
    )


@component.add(
    name="climate change incremental damage rate to capital stock extrapolations included",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"climate_change_incremental_damage_rate_to_capital_stock": 2},
)
def climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included():
    """
    Climate change damage rate to capital stock adjusted to be 0 in 2015, since we assume that historical data already accounts for the implicit damage. This variable is defined to allow to include extrapolations.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    value.loc[:, _subscript_dict["SECTORS CLIMATE CHANGE IMPACTS ORIGINAL"]] = (
        climate_change_incremental_damage_rate_to_capital_stock()
        .loc[:, _subscript_dict["SECTORS CLIMATE CHANGE IMPACTS ORIGINAL"]]
        .rename({"SECTORS I": "SECTORS CLIMATE CHANGE IMPACTS ORIGINAL"})
        .values
    )
    value.loc[:, _subscript_dict["SECTORS CLIMATE CHANGE IMPACTS EXTRAPOLATED"]] = (
        climate_change_incremental_damage_rate_to_capital_stock()
        .loc[:, "OTHER SERVICES"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "SECTORS CLIMATE CHANGE IMPACTS EXTRAPOLATED": _subscript_dict[
                    "SECTORS CLIMATE CHANGE IMPACTS EXTRAPOLATED"
                ]
            },
            1,
        )
        .values
    )
    return value


@component.add(
    name="consumption fixed capital",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 1,
        "mdollars_per_mdollars_2015": 2,
        "consumption_fixed_capital_real": 2,
        "price_transformation": 2,
        "initial_price_gfcf": 1,
        "price_gfcf": 1,
    },
)
def consumption_fixed_capital():
    """
    Consumption of fixed cpaital in nominal terms.
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: consumption_fixed_capital_real()
        * (initial_price_gfcf() / price_transformation())
        * mdollars_per_mdollars_2015(),
        lambda: consumption_fixed_capital_real()
        * (price_gfcf().rename({"SECTORS MAP I": "SECTORS I"}) / price_transformation())
        * mdollars_per_mdollars_2015(),
    )


@component.add(
    name="consumption fixed capital real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"capital_depreciation": 1, "climate_change_damage_on_capital_stock": 1},
)
def consumption_fixed_capital_real():
    """
    Consumption of fixed capital in real terms.
    """
    return capital_depreciation() + climate_change_damage_on_capital_stock()


@component.add(
    name="delayed TS output real until 2015",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={"_sampleiftrue_delayed_ts_output_real_until_2015": 1},
    other_deps={
        "_sampleiftrue_delayed_ts_output_real_until_2015": {
            "initial": {"delayed_ts_output_real": 1},
            "step": {"time": 1, "delayed_ts_output_real": 1},
        }
    },
)
def delayed_ts_output_real_until_2015():
    """
    This variable is used to isolate the investment module when the investment switch is zero. For this, the variable contains this historic data of the variable contained inside it until 2015 (2016 because its a delayed one) when it becomes constante at the 2015 level.
    """
    return _sampleiftrue_delayed_ts_output_real_until_2015()


_sampleiftrue_delayed_ts_output_real_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    lambda: delayed_ts_output_real(),
    lambda: delayed_ts_output_real(),
    "_sampleiftrue_delayed_ts_output_real_until_2015",
)


@component.add(
    name="desired private net fixed capital formation real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "switch_eco_investment": 1,
        "net_fixed_capital_formation_to_desired_real_capital": 2,
        "inital_private_gfcf_to_total_gfcf": 2,
        "_smooth_desired_private_net_fixed_capital_formation_real": 1,
        "_smooth_desired_private_net_fixed_capital_formation_real_1": 1,
    },
    other_deps={
        "_smooth_desired_private_net_fixed_capital_formation_real": {
            "initial": {
                "delayed_ts_output_real_until_2015": 1,
                "capital_productivity": 1,
            },
            "step": {"delayed_ts_output_real_until_2015": 1, "capital_productivity": 1},
        },
        "_smooth_desired_private_net_fixed_capital_formation_real_1": {
            "initial": {"delayed_ts_output_real": 1, "capital_productivity": 1},
            "step": {"delayed_ts_output_real": 1, "capital_productivity": 1},
        },
    },
)
def desired_private_net_fixed_capital_formation_real():
    """
    Desired net fixed capital formation in real terms. This is a function of the delayed output, the capital productivity and the ratio of net capital formation to capital stock (all in real terms). When the submodule is isolated (investment switch = 0) from 2015 onwards it takes constant level of delayed output real, modularizing the variable.
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: _smooth_desired_private_net_fixed_capital_formation_real()
        * net_fixed_capital_formation_to_desired_real_capital()
        * inital_private_gfcf_to_total_gfcf(),
        lambda: _smooth_desired_private_net_fixed_capital_formation_real_1()
        * net_fixed_capital_formation_to_desired_real_capital()
        * inital_private_gfcf_to_total_gfcf(),
    )


_smooth_desired_private_net_fixed_capital_formation_real = Smooth(
    lambda: zidz(delayed_ts_output_real_until_2015(), capital_productivity()),
    lambda: xr.DataArray(
        3,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    lambda: zidz(delayed_ts_output_real_until_2015(), capital_productivity()),
    lambda: 1,
    "_smooth_desired_private_net_fixed_capital_formation_real",
)

_smooth_desired_private_net_fixed_capital_formation_real_1 = Smooth(
    lambda: zidz(delayed_ts_output_real(), capital_productivity()),
    lambda: xr.DataArray(
        3,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    lambda: zidz(delayed_ts_output_real(), capital_productivity()),
    lambda: 1,
    "_smooth_desired_private_net_fixed_capital_formation_real_1",
)


@component.add(
    name="government gross fixed capital formation real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "government_investment_by_cofog": 1,
        "structure_government_investment_by_sectors_default": 1,
        "price_gfcf": 1,
        "price_transformation": 1,
        "mdollars_per_mdollars_2015": 1,
    },
)
def government_gross_fixed_capital_formation_real():
    """
    Government gross fixed capital formation by sector in real terms.
    """
    return (
        zidz(
            sum(
                government_investment_by_cofog().rename({"COFOG I": "COFOG I!"}),
                dim=["COFOG I!"],
            )
            * structure_government_investment_by_sectors_default(),
            price_gfcf().rename({"SECTORS MAP I": "SECTORS I"}),
        )
        * price_transformation()
        / mdollars_per_mdollars_2015()
    )


@component.add(
    name="government gross fixed capital formation real until 2015",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={
        "_sampleiftrue_government_gross_fixed_capital_formation_real_until_2015": 1
    },
    other_deps={
        "_sampleiftrue_government_gross_fixed_capital_formation_real_until_2015": {
            "initial": {"government_gross_fixed_capital_formation_real": 1},
            "step": {"time": 1, "government_gross_fixed_capital_formation_real": 1},
        }
    },
)
def government_gross_fixed_capital_formation_real_until_2015():
    """
    Variable used to isolate the investment submodule. When the investment switch is zero this variable is used. This variable uses the historic data of the variable contained inside it until 2015, when it becomes a constant at the 2015 level.
    """
    return _sampleiftrue_government_gross_fixed_capital_formation_real_until_2015()


_sampleiftrue_government_gross_fixed_capital_formation_real_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    lambda: government_gross_fixed_capital_formation_real(),
    lambda: government_gross_fixed_capital_formation_real(),
    "_sampleiftrue_government_gross_fixed_capital_formation_real_until_2015",
)


@component.add(
    name="gross fixed capital formation by good",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 1,
        "mdollars_per_mdollars_2015": 2,
        "gross_fixed_capital_formation_structure": 2,
        "price_transformation": 2,
        "gross_fixed_capital_formation_real": 2,
        "initial_price_of_output": 1,
        "price_output": 1,
    },
)
def gross_fixed_capital_formation_by_good():
    """
    Gross fixed capital formation by type of investment good in purchasers prices and nominal terms.
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: sum(
            gross_fixed_capital_formation_real().rename({"SECTORS I": "SECTORS MAP I!"})
            * gross_fixed_capital_formation_structure()
            .rename({"SECTORS MAP I": "SECTORS MAP I!"})
            .transpose("REGIONS 35 I", "SECTORS MAP I!", "SECTORS I"),
            dim=["SECTORS MAP I!"],
        )
        * zidz(initial_price_of_output(), price_transformation())
        * mdollars_per_mdollars_2015(),
        lambda: sum(
            gross_fixed_capital_formation_real().rename({"SECTORS I": "SECTORS MAP I!"})
            * gross_fixed_capital_formation_structure()
            .rename({"SECTORS MAP I": "SECTORS MAP I!"})
            .transpose("REGIONS 35 I", "SECTORS MAP I!", "SECTORS I"),
            dim=["SECTORS MAP I!"],
        )
        * zidz(price_output(), price_transformation())
        * mdollars_per_mdollars_2015(),
    )


@component.add(
    name="gross fixed capital formation real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 2,
        "private_gfcf_to_replace_climate_damage": 3,
        "capital_depreciation": 3,
        "government_gross_fixed_capital_formation_real_until_2015": 1,
        "inital_private_gfcf_to_total_gfcf": 3,
        "desired_private_net_fixed_capital_formation_real": 3,
        "government_gross_fixed_capital_formation_real": 2,
        "switch_economy": 1,
        "delayed_ts_gfcf_protra_sectors_35r": 1,
        "switch_nrg2eco_investment_costs": 1,
    },
)
def gross_fixed_capital_formation_real():
    """
    Production of each sector in the form of investments goods to be sold (as investment) to other sectors. Gross fixed capital formation in real terms equal to capital stock gap plus depreciation plus climate change losses. When the investment switch is deactivated the variable takes the 2015 level of Government GFCF real.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS ENERGY I"]] = False
    value.values[except_subs.values] = if_then_else(
        switch_eco_investment() == 0,
        lambda: desired_private_net_fixed_capital_formation_real()
        + capital_depreciation() * inital_private_gfcf_to_total_gfcf()
        + private_gfcf_to_replace_climate_damage()
        + government_gross_fixed_capital_formation_real_until_2015(),
        lambda: desired_private_net_fixed_capital_formation_real()
        + capital_depreciation() * inital_private_gfcf_to_total_gfcf()
        + private_gfcf_to_replace_climate_damage()
        + government_gross_fixed_capital_formation_real(),
    ).values[except_subs.values]
    value.loc[:, _subscript_dict["SECTORS ENERGY I"]] = if_then_else(
        np.logical_or(
            switch_economy() == 0,
            np.logical_or(
                switch_eco_investment() == 0, switch_nrg2eco_investment_costs() == 0
            ),
        ),
        lambda: desired_private_net_fixed_capital_formation_real()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS I": "SECTORS ENERGY I"})
        + capital_depreciation()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS I": "SECTORS ENERGY I"})
        * inital_private_gfcf_to_total_gfcf()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS I": "SECTORS ENERGY I"})
        + private_gfcf_to_replace_climate_damage()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS I": "SECTORS ENERGY I"})
        + government_gross_fixed_capital_formation_real()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS I": "SECTORS ENERGY I"}),
        lambda: delayed_ts_gfcf_protra_sectors_35r(),
    ).values
    return value


@component.add(
    name="INITAL PRIVATE GFCF TO TOTAL GFCF",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_private_gross_fixed_capital_formation_real": 1,
        "initial_total_gross_fixed_capital_formation_real": 1,
    },
)
def inital_private_gfcf_to_total_gfcf():
    """
    Initial ratio private gross fixed capital formation to total gross fixed capital formation
    """
    return zidz(
        initial_private_gross_fixed_capital_formation_real(),
        initial_total_gross_fixed_capital_formation_real(),
    )


@component.add(
    name="INITIAL GOVERNMENT GROSS FIXED CAPITAL FORMATION REAL",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_government_gross_fixed_capital_formation_real": 1},
    other_deps={
        "_initial_initial_government_gross_fixed_capital_formation_real": {
            "initial": {"government_gross_fixed_capital_formation_real": 1},
            "step": {},
        }
    },
)
def initial_government_gross_fixed_capital_formation_real():
    """
    Initial government gross fixed capital formation by sector in real terms.
    """
    return _initial_initial_government_gross_fixed_capital_formation_real()


_initial_initial_government_gross_fixed_capital_formation_real = Initial(
    lambda: government_gross_fixed_capital_formation_real(),
    "_initial_initial_government_gross_fixed_capital_formation_real",
)


@component.add(
    name="INITIAL TOTAL GROSS FIXED CAPITAL FORMATION REAL",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_government_gross_fixed_capital_formation_real": 1,
        "initial_private_gross_fixed_capital_formation_real": 1,
    },
)
def initial_total_gross_fixed_capital_formation_real():
    """
    Initial total gross fixed capital formation.
    """
    return (
        initial_government_gross_fixed_capital_formation_real()
        + initial_private_gross_fixed_capital_formation_real()
    )


@component.add(
    name="INITIAL YEAR CAPITAL PRODUCTIVITY VARIATION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_capital_productivity_variation_sp"
    },
)
def initial_year_capital_productivity_variation_sp():
    return _ext_constant_initial_year_capital_productivity_variation_sp()


_ext_constant_initial_year_capital_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_CAPITAL_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_capital_productivity_variation_sp",
)


@component.add(
    name="NET FIXED CAPITAL FORMATION TO DESIRED REAL CAPITAL",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_capital_stock": 3,
        "initial_consumption_fixed_capital_real": 3,
        "initial_total_gross_fixed_capital_formation_real": 3,
    },
)
def net_fixed_capital_formation_to_desired_real_capital():
    """
    Ratio net fixed capital formation to capitla stock in real terms.
    """
    return if_then_else(
        time() <= 2015,
        lambda: zidz(
            initial_total_gross_fixed_capital_formation_real()
            - initial_consumption_fixed_capital_real(),
            initial_capital_stock(),
        ),
        lambda: if_then_else(
            zidz(
                initial_total_gross_fixed_capital_formation_real()
                - initial_consumption_fixed_capital_real(),
                initial_capital_stock(),
            )
            < 0,
            lambda: xr.DataArray(
                0.01,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                },
                ["REGIONS 35 I", "SECTORS I"],
            ),
            lambda: zidz(
                initial_total_gross_fixed_capital_formation_real()
                - initial_consumption_fixed_capital_real(),
                initial_capital_stock(),
            ),
        ),
    )


@component.add(
    name="private GFCF to replace climate damage",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={"climate_change_damage_on_capital_stock": 1},
)
def private_gfcf_to_replace_climate_damage():
    """
    Gross fixed capital formation to replace cliamte damages
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PUBLIC ADMINISTRATION"]] = False
    value.values[except_subs.values] = climate_change_damage_on_capital_stock().values[
        except_subs.values
    ]
    value.loc[:, ["PUBLIC ADMINISTRATION"]] = 0
    return value


@component.add(
    name="public GFCF to replace climate damage",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_investment": 1,
        "climate_change_damage_on_capital_stock": 2,
        "mdollars_per_mdollars_2015": 2,
        "price_transformation": 2,
        "initial_price_gfcf": 1,
        "price_gfcf": 1,
    },
)
def public_gfcf_to_replace_climate_damage():
    """
    Gross fixed capital formation to replace climate damages in nominal terms. When the invesment module runs isolated, this takes the initial price of GFCF. Nonetheless, the variable of damages takes the value of zero. (See in its own equation).
    """
    return if_then_else(
        switch_eco_investment() == 0,
        lambda: climate_change_damage_on_capital_stock()
        .loc[:, "PUBLIC ADMINISTRATION"]
        .reset_coords(drop=True)
        * initial_price_gfcf()
        / price_transformation()
        * mdollars_per_mdollars_2015(),
        lambda: climate_change_damage_on_capital_stock()
        .loc[:, "PUBLIC ADMINISTRATION"]
        .reset_coords(drop=True)
        * price_gfcf().loc[:, "PUBLIC ADMINISTRATION"].reset_coords(drop=True)
        / price_transformation()
        * mdollars_per_mdollars_2015(),
    )


@component.add(
    name="real capital stock",
    units="Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_real_capital_stock": 1},
    other_deps={
        "_integ_real_capital_stock": {
            "initial": {"initial_capital_stock": 1},
            "step": {
                "time": 1,
                "climate_change_damage_on_capital_stock": 2,
                "capital_depreciation": 1,
                "gross_fixed_capital_formation_real": 1,
            },
        }
    },
)
def real_capital_stock():
    """
    Stock of capital in real terms.
    """
    return _integ_real_capital_stock()


_integ_real_capital_stock = Integ(
    lambda: if_then_else(
        time() <= 2015,
        lambda: -climate_change_damage_on_capital_stock(),
        lambda: gross_fixed_capital_formation_real()
        - climate_change_damage_on_capital_stock()
        - capital_depreciation(),
    ),
    lambda: initial_capital_stock(),
    "_integ_real_capital_stock",
)


@component.add(
    name="SELECT CAPITAL PRODUCTIVITY VARIATION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_capital_productivity_variation_sp"
    },
)
def select_capital_productivity_variation_sp():
    """
    Select capital productivity scenario 0: Default values 1: User defined
    """
    return _ext_constant_select_capital_productivity_variation_sp()


_ext_constant_select_capital_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CAPITAL_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_capital_productivity_variation_sp",
)


@component.add(
    name="SELECT CLIMATE CHANGE IMPACTS SENSITIVITY SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_climate_change_impacts_sensitivity_sp"
    },
)
def select_climate_change_impacts_sensitivity_sp():
    """
    0: Extrapolations are off to apply damages to all sectors. 1: Extrapolations are included to apply damages to all sectors.
    """
    return _ext_constant_select_climate_change_impacts_sensitivity_sp()


_ext_constant_select_climate_change_impacts_sensitivity_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CLIMATE_CHANGE_IMPACTS_SENSITIVITY_SP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_change_impacts_sensitivity_sp",
)


@component.add(
    name="SWITCH ECO INVESTMENT",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_investment"},
)
def switch_eco_investment():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_investment()


_ext_constant_switch_eco_investment = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_INVESTMENT",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_investment",
)


@component.add(
    name="SWITCH NRG2ECO INVESTMENT COSTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg2eco_investment_costs"},
)
def switch_nrg2eco_investment_costs():
    """
    This switch can take two values: 0: investment costs are computed for all sectors in the economy module. 1: the investment costs associated to energy sectors come from the energy module.
    """
    return _ext_constant_switch_nrg2eco_investment_costs()


_ext_constant_switch_nrg2eco_investment_costs = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2ECO_INVESTMENT_COSTS",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2eco_investment_costs",
)
