"""
Module economyprices
Translated using PySD version 3.14.0
"""

@component.add(
    name="add mark up low unemployment",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "non_accelerating_wage_inflation_rate_of_unemployment_to_unemployment_ratio": 2,
        "constant_mark_up_curve": 1,
        "alpha_mark_up_curve": 1,
    },
)
def add_mark_up_low_unemployment():
    """
    Increase in mark up due to tightnes in labour market.
    """
    return if_then_else(
        non_accelerating_wage_inflation_rate_of_unemployment_to_unemployment_ratio()
        <= 1,
        lambda: xr.DataArray(
            1, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: np.exp(
            constant_mark_up_curve()
            + alpha_mark_up_curve()
            * np.log(
                non_accelerating_wage_inflation_rate_of_unemployment_to_unemployment_ratio()
            )
        ),
    )


@component.add(
    name="add mark up low unemployment adjusted",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"add_mark_up_low_unemployment": 2},
)
def add_mark_up_low_unemployment_adjusted():
    """
    Adjusted mark-up between 1 and 1.5
    """
    return if_then_else(
        add_mark_up_low_unemployment() < 1,
        lambda: xr.DataArray(
            1, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: np.minimum(add_mark_up_low_unemployment(), 1.5),
    )


@component.add(
    name="add mark up low unemploymnet smooth",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={"time": 1, "_smooth_add_mark_up_low_unemploymnet_smooth": 1},
    other_deps={
        "_smooth_add_mark_up_low_unemploymnet_smooth": {
            "initial": {"add_mark_up_low_unemployment_adjusted": 1},
            "step": {"add_mark_up_low_unemployment_adjusted": 1},
        }
    },
)
def add_mark_up_low_unemploymnet_smooth():
    """
    Smooth mark up increase due to tightnes in the labour market
    """
    return if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            1, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: _smooth_add_mark_up_low_unemploymnet_smooth(),
    )


_smooth_add_mark_up_low_unemploymnet_smooth = Smooth(
    lambda: add_mark_up_low_unemployment_adjusted(),
    lambda: xr.DataArray(
        3, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    lambda: add_mark_up_low_unemployment_adjusted(),
    lambda: 1,
    "_smooth_add_mark_up_low_unemploymnet_smooth",
)


@component.add(
    name="BASE PRICE MATERIALS AND PRIVATE HOUSEHOLDS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def base_price_materials_and_private_households():
    return 100


@component.add(
    name="CO2 TAX HOUSEHOLDS SP",
    units="dollars/tCO2eq",
    subscripts=["REGIONS 36 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_co2_tax_households_sp",
        "__data__": "_ext_data_co2_tax_households_sp",
        "time": 1,
    },
)
def co2_tax_households_sp():
    """
    CO2 tax by region over time.
    """
    return _ext_data_co2_tax_households_sp(time())


_ext_data_co2_tax_households_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "time_index_2100",
    "CO2_TAX_HOUSEHOLDS_SP",
    "interpolate",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_data_co2_tax_households_sp",
)


@component.add(
    name="CO2 tax rate households",
    units="dollars/tCO2eq",
    subscripts=["REGIONS 35 I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_co2_tax_households_sp": 3,
        "select_gases_co2_tax_households_sp": 6,
        "co2_tax_households_sp": 3,
    },
)
def co2_tax_rate_households():
    """
    CO2 tax rate households
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "GHG ENERGY USE I"],
    )
    value.loc[:, ["CO2"]] = (
        if_then_else(
            select_co2_tax_households_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_households_sp() == 0,
                    select_gases_co2_tax_households_sp() == 3,
                ),
                lambda: co2_tax_households_sp()
                .loc[_subscript_dict["REGIONS 35 I"]]
                .rename({"REGIONS 36 I": "REGIONS 35 I"}),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 1)
        .values
    )
    value.loc[:, ["CH4"]] = (
        if_then_else(
            select_co2_tax_households_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_households_sp() == 1,
                    select_gases_co2_tax_households_sp() == 3,
                ),
                lambda: co2_tax_households_sp()
                .loc[_subscript_dict["REGIONS 35 I"]]
                .rename({"REGIONS 36 I": "REGIONS 35 I"}),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 1)
        .values
    )
    value.loc[:, ["N2O"]] = (
        if_then_else(
            select_co2_tax_households_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_households_sp() == 2,
                    select_gases_co2_tax_households_sp() == 3,
                ),
                lambda: co2_tax_households_sp()
                .loc[_subscript_dict["REGIONS 35 I"]]
                .rename({"REGIONS 36 I": "REGIONS 35 I"}),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 1)
        .values
    )
    return value


@component.add(
    name="CO2 tax rate sectors",
    units="dollars/tCO2eq",
    subscripts=["REGIONS 36 I", "GHG ENERGY USE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_co2_tax_sectors_sp": 3,
        "co2_tax_sectors_sp": 3,
        "select_gases_co2_tax_sectors_sp": 6,
    },
)
def co2_tax_rate_sectors():
    """
    CO2 tax rate sectors. =0 if policy si not activated.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 36 I", "GHG ENERGY USE I"],
    )
    value.loc[:, ["CO2"]] = (
        if_then_else(
            select_co2_tax_sectors_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_sectors_sp() == 0,
                    select_gases_co2_tax_sectors_sp() == 3,
                ),
                lambda: co2_tax_sectors_sp(),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
                    ["REGIONS 36 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]}, ["REGIONS 36 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["CO2"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["CH4"]] = (
        if_then_else(
            select_co2_tax_sectors_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_sectors_sp() == 1,
                    select_gases_co2_tax_sectors_sp() == 3,
                ),
                lambda: co2_tax_sectors_sp()
                .loc[_subscript_dict["REGIONS 35 I"]]
                .rename({"REGIONS 36 I": "REGIONS 35 I"}),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["CH4"]}, 1)
        .values
    )
    value.loc[_subscript_dict["REGIONS 35 I"], ["N2O"]] = (
        if_then_else(
            select_co2_tax_sectors_sp() == 1,
            lambda: if_then_else(
                np.logical_or(
                    select_gases_co2_tax_sectors_sp() == 2,
                    select_gases_co2_tax_sectors_sp() == 3,
                ),
                lambda: co2_tax_sectors_sp()
                .loc[_subscript_dict["REGIONS 35 I"]]
                .rename({"REGIONS 36 I": "REGIONS 35 I"}),
                lambda: xr.DataArray(
                    0,
                    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
                    ["REGIONS 35 I"],
                ),
            ),
            lambda: xr.DataArray(
                0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
            ),
        )
        .expand_dims({"GHG ENERGY USE I": ["N2O"]}, 1)
        .values
    )
    return value


@component.add(
    name="CO2 TAX SECTORS SP",
    units="dollars/tCO2eq",
    subscripts=["REGIONS 36 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_co2_tax_sectors_sp",
        "__data__": "_ext_data_co2_tax_sectors_sp",
        "time": 1,
    },
)
def co2_tax_sectors_sp():
    """
    CO2 tax by region over time.
    """
    return _ext_data_co2_tax_sectors_sp(time())


_ext_data_co2_tax_sectors_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "time_index_2100",
    "CO2_TAX_SECTORS_SP",
    "interpolate",
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    _root,
    {"REGIONS 36 I": _subscript_dict["REGIONS 36 I"]},
    "_ext_data_co2_tax_sectors_sp",
)


@component.add(
    name="DELAYED non metals price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_non_metals_price_economy_adjusted():
    """
    Delayed non metals price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED other metals price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_other_metals_price_economy_adjusted():
    """
    Delayed other metals price economy adjusted.
    """
    return 100


@component.add(
    name="DELAYED precious metals price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_precious_metals_price_economy_adjusted():
    """
    Delayed precious metals price economy adjusted.
    """
    return 100


@component.add(
    name="delayed TS GHG emissions households COICOP 35 R CO2eq until 2015",
    units="MtCO2eq/Year",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={
        "_sampleiftrue_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015": 1
    },
    other_deps={
        "_sampleiftrue_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015": {
            "initial": {"delayed_ts_ghg_emissions_households_coicop_35_r_co2eq": 1},
            "step": {
                "time": 1,
                "delayed_ts_ghg_emissions_households_coicop_35_r_co2eq": 1,
            },
        }
    },
)
def delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015():
    """
    This variable is used to modularize the variable contained inside it, so that it makes the historic until 2015, when it becomes constant.
    """
    return (
        _sampleiftrue_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015()
    )


_sampleiftrue_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    ),
    lambda: delayed_ts_ghg_emissions_households_coicop_35_r_co2eq(),
    lambda: delayed_ts_ghg_emissions_households_coicop_35_r_co2eq(),
    "_sampleiftrue_delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015",
)


@component.add(
    name="delayed TS implicit CO2 emissions factor sectors until 2015",
    units="MtCO2eq/TJ",
    subscripts=[
        "REGIONS 35 I",
        "SECTORS FINAL ENERGY I",
        "SECTORS NON ENERGY I",
        "GHG ENERGY USE I",
    ],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={
        "_sampleiftrue_delayed_ts_implicit_co2_emissions_factor_sectors_until_2015": 1
    },
    other_deps={
        "_sampleiftrue_delayed_ts_implicit_co2_emissions_factor_sectors_until_2015": {
            "initial": {"delayed_ts_implicit_co2_emission_factor_sectors": 1},
            "step": {"time": 1, "delayed_ts_implicit_co2_emission_factor_sectors": 1},
        }
    },
)
def delayed_ts_implicit_co2_emissions_factor_sectors_until_2015():
    """
    This variable is created to modularize the variable so that when it reaches 2015 further on it stays at a constant level, that of the 2015 year.
    """
    return _sampleiftrue_delayed_ts_implicit_co2_emissions_factor_sectors_until_2015()


_sampleiftrue_delayed_ts_implicit_co2_emissions_factor_sectors_until_2015 = (
    SampleIfTrue(
        lambda: xr.DataArray(
            time() <= 2015,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
                "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
                "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
            },
            [
                "REGIONS 35 I",
                "SECTORS FINAL ENERGY I",
                "SECTORS NON ENERGY I",
                "GHG ENERGY USE I",
            ],
        ),
        lambda: delayed_ts_implicit_co2_emission_factor_sectors(),
        lambda: delayed_ts_implicit_co2_emission_factor_sectors(),
        "_sampleiftrue_delayed_ts_implicit_co2_emissions_factor_sectors_until_2015",
    )
)


@component.add(
    name="delayed TS implicit ghg emissions factor households COICOP until 2015",
    units="MtCO2eq/TJ",
    subscripts=["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    comp_type="Stateful",
    comp_subtype="SampleIfTrue",
    depends_on={
        "_sampleiftrue_delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015": 1
    },
    other_deps={
        "_sampleiftrue_delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015": {
            "initial": {"delayed_ts_implicit_ghg_emission_factor_households_coicop": 1},
            "step": {
                "time": 1,
                "delayed_ts_implicit_ghg_emission_factor_households_coicop": 1,
            },
        }
    },
)
def delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015():
    """
    This variable is historic until 2015 when it becomes constant at the 2015 level. Its used to isolate the economic module.
    """
    return (
        _sampleiftrue_delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015()
    )


_sampleiftrue_delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015 = SampleIfTrue(
    lambda: xr.DataArray(
        time() <= 2015,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "COICOP I": _subscript_dict["COICOP I"],
            "GHG ENERGY USE I": _subscript_dict["GHG ENERGY USE I"],
        },
        ["REGIONS 35 I", "COICOP I", "GHG ENERGY USE I"],
    ),
    lambda: delayed_ts_implicit_ghg_emission_factor_households_coicop(),
    lambda: delayed_ts_implicit_ghg_emission_factor_households_coicop(),
    "_sampleiftrue_delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015",
)


@component.add(
    name="delayed TS other gas price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_ts_other_gas_price_economy_adjusted():
    """
    Delayed other gas price economy adjusted.
    """
    return 100


@component.add(
    name="delayed TS Pb Zn Tn price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_ts_pb_zn_tn_price_economy_adjusted():
    """
    Delayed lead, zinc and tin price economy adjusted.
    """
    return 100


@component.add(
    name="delayed TS price GFCF",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_gfcf": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_gfcf": {
            "initial": {"initial_price_gfcf": 1, "time_step": 1},
            "step": {"time": 1, "initial_price_gfcf": 1, "price_gfcf": 1},
        }
    },
)
def delayed_ts_price_gfcf():
    """
    Delayed (time step) price of investment goods.
    """
    return _delayfixed_delayed_ts_price_gfcf()


_delayfixed_delayed_ts_price_gfcf = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            initial_price_gfcf(),
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: price_gfcf().rename({"SECTORS MAP I": "SECTORS I"}),
    ),
    lambda: time_step(),
    lambda: xr.DataArray(
        initial_price_gfcf(),
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_price_gfcf",
)


@component.add(
    name="delayed TS price materials and private households",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS EXTRACTION PH I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 13,
        "base_price_materials_and_private_households": 14,
        "delayed_ts_coal_price_economy_adjusted": 1,
        "delayed_ts_oil_price_economy_adjusted": 1,
        "delayed_ts_gas_price_economy_adjusted": 1,
        "delayed_ts_other_gas_price_economy_adjusted": 1,
        "delayed_ts_uranium_price_economy_adjusted": 1,
        "delayed_ts_fe_price_economy_adjusted": 1,
        "delayed_ts_cu_price_economy_adjusted": 1,
        "delayed_ts_ni_price_economy_adjusted": 1,
        "delayed_ts_al_price_economy_adjusted": 1,
        "delayed_precious_metals_price_economy_adjusted": 1,
        "delayed_ts_pb_zn_tn_price_economy_adjusted": 1,
        "delayed_other_metals_price_economy_adjusted": 1,
        "delayed_non_metals_price_economy_adjusted": 1,
    },
)
def delayed_ts_price_materials_and_private_households():
    """
    Delayed price of all materials calculated in materials model and fixed price of private households with employed persons (Sector 95 in NACE classification).
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS EXTRACTION PH I": _subscript_dict["SECTORS EXTRACTION PH I"],
        },
        ["REGIONS 35 I", "SECTORS EXTRACTION PH I"],
    )
    value.loc[:, ["MINING COAL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_coal_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION OIL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_oil_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION GAS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_gas_price_economy_adjusted(),
    )
    value.loc[:, ["EXTRACTION OTHER GAS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_other_gas_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING URANIUM THORIUM"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_uranium_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING IRON"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_fe_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING COPPER"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_cu_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING NICKEL"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_ni_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING ALUMINIUM"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_al_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING PRECIOUS METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_precious_metals_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING LEAD ZINC TIN"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_ts_pb_zn_tn_price_economy_adjusted(),
    )
    value.loc[:, ["MINING AND MANUFACTURING OTHER METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_other_metals_price_economy_adjusted(),
    )
    value.loc[:, ["MINING NON METALS"]] = if_then_else(
        switch_economy() == 0,
        lambda: base_price_materials_and_private_households(),
        lambda: delayed_non_metals_price_economy_adjusted(),
    )
    value.loc[:, ["PRIVATE HOUSEHOLDS"]] = base_price_materials_and_private_households()
    return value


@component.add(
    name="delayed TS price output",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_output": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_output": {
            "initial": {"initial_price_of_output": 1, "time_step": 1},
            "step": {"time": 1, "initial_price_of_output": 1, "price_output": 1},
        }
    },
)
def delayed_ts_price_output():
    """
    Delayed output price.
    """
    return _delayfixed_delayed_ts_price_output()


_delayfixed_delayed_ts_price_output = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            initial_price_of_output(),
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: price_output(),
    ),
    lambda: time_step(),
    lambda: xr.DataArray(
        initial_price_of_output(),
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_price_output",
)


@component.add(
    name="delayed TS price ratio households",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_ratio_households": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_ratio_households": {
            "initial": {"time_step": 1},
            "step": {"time": 1, "price_ratio_households": 1},
        }
    },
)
def delayed_ts_price_ratio_households():
    """
    Delayed price ratio between domestic and foreign products for households.
    """
    return _delayfixed_delayed_ts_price_ratio_households()


_delayfixed_delayed_ts_price_ratio_households = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: np.maximum(0, price_ratio_households()),
    ),
    lambda: time_step(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_price_ratio_households",
)


@component.add(
    name="delayed TS price ratio sectors",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_price_ratio_sectors": 1},
    other_deps={
        "_delayfixed_delayed_ts_price_ratio_sectors": {
            "initial": {"time_step": 1},
            "step": {"time": 1, "price_ratio_sectors": 1},
        }
    },
)
def delayed_ts_price_ratio_sectors():
    """
    Delayed price ratio between domestic and foreign products for intermdiates.
    """
    return _delayfixed_delayed_ts_price_ratio_sectors()


_delayfixed_delayed_ts_price_ratio_sectors = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
                "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
            },
            ["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
        ),
        lambda: price_ratio_sectors(),
    ),
    lambda: time_step(),
    lambda: xr.DataArray(
        1,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
        },
        ["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_price_ratio_sectors",
)


@component.add(
    name="delayed TS taxes on resources paid by extration sectors",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_taxes_on_resources_paid_by_extration_sectors": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_taxes_on_resources_paid_by_extration_sectors": {
            "initial": {"time_step": 1},
            "step": {"taxes_on_resources_paid_by_extraction_sectors": 1},
        }
    },
)
def delayed_ts_taxes_on_resources_paid_by_extration_sectors():
    """
    Delayed (time step) taxes on resources
    """
    return _delayfixed_delayed_ts_taxes_on_resources_paid_by_extration_sectors()


_delayfixed_delayed_ts_taxes_on_resources_paid_by_extration_sectors = DelayFixed(
    lambda: taxes_on_resources_paid_by_extraction_sectors(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_taxes_on_resources_paid_by_extration_sectors",
)


@component.add(
    name="delayed TS uranium price economy adjusted",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="Normal",
)
def delayed_ts_uranium_price_economy_adjusted():
    """
    Delayed price of uranium adjusted.
    """
    return 100


@component.add(
    name="final energy purchaser price sectors without CO2 tax",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_domestic_purchaser_prices_sectors": 1,
        "import_shares_intermediates_constrained": 2,
        "price_import_purchaser_prices_sectors": 1,
    },
)
def final_energy_purchaser_price_sectors_without_co2_tax():
    """
    Final energy price at purchasers prices without CO2 price
    """
    return price_domestic_purchaser_prices_sectors().loc[
        :,
        _subscript_dict["SECTORS FINAL ENERGY I"],
        _subscript_dict["SECTORS NON ENERGY I"],
    ].rename(
        {"SECTORS I": "SECTORS FINAL ENERGY I", "SECTORS MAP I": "SECTORS NON ENERGY I"}
    ) * (
        1
        - import_shares_intermediates_constrained()
        .loc[
            :,
            _subscript_dict["SECTORS FINAL ENERGY I"],
            _subscript_dict["SECTORS NON ENERGY I"],
        ]
        .rename(
            {
                "SECTORS I": "SECTORS FINAL ENERGY I",
                "SECTORS MAP I": "SECTORS NON ENERGY I",
            }
        )
    ) + price_import_purchaser_prices_sectors().loc[
        :,
        _subscript_dict["SECTORS FINAL ENERGY I"],
        _subscript_dict["SECTORS NON ENERGY I"],
    ].rename(
        {"SECTORS I": "SECTORS FINAL ENERGY I", "SECTORS MAP I": "SECTORS NON ENERGY I"}
    ) * import_shares_intermediates_constrained().loc[
        :,
        _subscript_dict["SECTORS FINAL ENERGY I"],
        _subscript_dict["SECTORS NON ENERGY I"],
    ].rename(
        {"SECTORS I": "SECTORS FINAL ENERGY I", "SECTORS MAP I": "SECTORS NON ENERGY I"}
    )


@component.add(
    name="GHG cost per unit of output",
    units="Mdollars/Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tax_ghg_paid_by_sector": 1, "delayed_ts_output_real": 1},
)
def ghg_cost_per_unit_of_output():
    """
    GHG cost per unit of output
    """
    return zidz(tax_ghg_paid_by_sector(), delayed_ts_output_real())


@component.add(
    name="IMPLICIT PRICE FINAL ENERGY SECTORS",
    units="Mdollars/TJ",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_intermediates_total_real_purchaser_prices": 1,
        "initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector": 1,
        "mdollars_per_mdollars_2015": 1,
    },
)
def implicit_price_final_energy_sectors():
    """
    Implicit price of final energy demand by sector
    """
    return (
        zidz(
            initial_intermediates_total_real_purchaser_prices()
            .loc[
                :,
                _subscript_dict["SECTORS FINAL ENERGY I"],
                _subscript_dict["SECTORS NON ENERGY I"],
            ]
            .rename(
                {
                    "SECTORS I": "SECTORS FINAL ENERGY I",
                    "SECTORS MAP I": "SECTORS NON ENERGY I",
                }
            ),
            initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector(),
        )
        * mdollars_per_mdollars_2015()
    )


@component.add(
    name="IMV final energy price purchaser price sectors with CO2 tax",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "final_energy_purchaser_price_sectors_without_co2_tax": 2,
        "unit_conversion_dollars_mdollars": 2,
        "co2_tax_rate_sectors": 2,
        "delayed_ts_implicit_co2_emissions_factor_sectors_until_2015": 1,
        "unit_conversion_tco2eq_mtco2eq": 2,
        "initial_final_energy_price_purchaser_price_sectors_without_co2_tax": 2,
        "implicit_price_final_energy_sectors": 2,
        "delayed_ts_implicit_co2_emission_factor_sectors": 1,
    },
)
def imv_final_energy_price_purchaser_price_sectors_with_co2_tax():
    """
    Final energy price at purchasers prices including CO2 price, when the switch is deactivated the module is isolated.
    """
    return if_then_else(
        switch_economy() == 0,
        lambda: zidz(
            final_energy_purchaser_price_sectors_without_co2_tax(),
            initial_final_energy_price_purchaser_price_sectors_without_co2_tax(),
        )
        + sum(
            zidz(
                co2_tax_rate_sectors()
                .loc[_subscript_dict["REGIONS 35 I"], :]
                .rename(
                    {
                        "REGIONS 36 I": "REGIONS 35 I",
                        "GHG ENERGY USE I": "GHG ENERGY USE I!",
                    }
                )
                / unit_conversion_dollars_mdollars()
                * unit_conversion_tco2eq_mtco2eq()
                * delayed_ts_implicit_co2_emissions_factor_sectors_until_2015()
                .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
                .transpose(
                    "REGIONS 35 I",
                    "GHG ENERGY USE I!",
                    "SECTORS FINAL ENERGY I",
                    "SECTORS NON ENERGY I",
                ),
                implicit_price_final_energy_sectors().expand_dims(
                    {"GHG ENERGY USE I!": ["CO2", "CH4", "N2O"]}, 1
                ),
            ),
            dim=["GHG ENERGY USE I!"],
        ),
        lambda: zidz(
            final_energy_purchaser_price_sectors_without_co2_tax(),
            initial_final_energy_price_purchaser_price_sectors_without_co2_tax()
            + sum(
                zidz(
                    co2_tax_rate_sectors()
                    .loc[_subscript_dict["REGIONS 35 I"], :]
                    .rename(
                        {
                            "REGIONS 36 I": "REGIONS 35 I",
                            "GHG ENERGY USE I": "GHG ENERGY USE I!",
                        }
                    )
                    / unit_conversion_dollars_mdollars()
                    * unit_conversion_tco2eq_mtco2eq()
                    * delayed_ts_implicit_co2_emission_factor_sectors()
                    .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
                    .transpose(
                        "REGIONS 35 I",
                        "GHG ENERGY USE I!",
                        "SECTORS FINAL ENERGY I",
                        "SECTORS NON ENERGY I",
                    ),
                    implicit_price_final_energy_sectors().expand_dims(
                        {"GHG ENERGY USE I!": ["CO2", "CH4", "N2O"]}, 1
                    ),
                ),
                dim=["GHG ENERGY USE I!"],
            ),
        ),
    )


@component.add(
    name="initial delayed estimated oil price",
    comp_type="Constant",
    comp_subtype="Normal",
)
def initial_delayed_estimated_oil_price():
    """
    Initial delayed estimated oil price.
    """
    return 81.1898


@component.add(
    name="INITIAL FINAL ENERGY DEMAND BY FINAL ENERGY SECTOR AND NON ENERGY SECTOR",
    units="TJ/Year",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={
        "_initial_initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector": 1
    },
    other_deps={
        "_initial_initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector": {
            "initial": {
                "final_energy_demand_by_final_energy_sector_and_non_energy_sector": 1
            },
            "step": {},
        }
    },
)
def initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector():
    """
    Initial final energy demand by sector and final energy in economic classification
    """
    return (
        _initial_initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector()
    )


_initial_initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector = Initial(
    lambda: final_energy_demand_by_final_energy_sector_and_non_energy_sector(),
    "_initial_initial_final_energy_demand_by_final_energy_sector_and_non_energy_sector",
)


@component.add(
    name="INITIAL FINAL ENERGY PRICE PURCHASER PRICE SECTORS WITHOUT CO2 TAX",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS NON ENERGY I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={
        "_initial_initial_final_energy_price_purchaser_price_sectors_without_co2_tax": 1
    },
    other_deps={
        "_initial_initial_final_energy_price_purchaser_price_sectors_without_co2_tax": {
            "initial": {"final_energy_purchaser_price_sectors_without_co2_tax": 1},
            "step": {},
        }
    },
)
def initial_final_energy_price_purchaser_price_sectors_without_co2_tax():
    """
    Initial final energy price at purchasers prices without CO2 price
    """
    return _initial_initial_final_energy_price_purchaser_price_sectors_without_co2_tax()


_initial_initial_final_energy_price_purchaser_price_sectors_without_co2_tax = Initial(
    lambda: final_energy_purchaser_price_sectors_without_co2_tax(),
    "_initial_initial_final_energy_price_purchaser_price_sectors_without_co2_tax",
)


@component.add(
    name="INITIAL INTERMEDIATES TOTAL REAL PURCHASER PRICES",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_intermediates_domestic_real": 1,
        "price_domestic_purchaser_prices_sectors": 1,
        "price_import_purchaser_prices_sectors": 1,
        "initial_intermediate_imports_and_exports_real": 1,
    },
)
def initial_intermediates_total_real_purchaser_prices():
    """
    Initial total intermediates in real terms.
    """
    return (
        initial_intermediates_domestic_real()
        * price_domestic_purchaser_prices_sectors()
        + sum(
            initial_intermediate_imports_and_exports_real().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 MAP I!",
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                }
            )
            * price_import_purchaser_prices_sectors().rename(
                {"REGIONS 35 I": "REGIONS 35 MAP I!"}
            ),
            dim=["REGIONS 35 MAP I!"],
        ).transpose("REGIONS 35 I", "SECTORS I", "SECTORS MAP I")
    )


@component.add(
    name="INITIAL PRICE COICOP",
    subscripts=["REGIONS 35 I", "COICOP I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_price_coicop": 1},
    other_deps={
        "_initial_initial_price_coicop": {"initial": {"price_coicop": 1}, "step": {}}
    },
)
def initial_price_coicop():
    """
    Initial price by consumption category (COICOP classification)
    """
    return _initial_initial_price_coicop()


_initial_initial_price_coicop = Initial(
    lambda: price_coicop(), "_initial_initial_price_coicop"
)


@component.add(
    name="initial price with mark up",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_price_with_mark_up": 1},
    other_deps={
        "_initial_initial_price_with_mark_up": {
            "initial": {"price_domestic": 1, "price_import": 1},
            "step": {},
        }
    },
)
def initial_price_with_mark_up():
    """
    Initial price with mark-up.
    """
    return _initial_initial_price_with_mark_up()


_initial_initial_price_with_mark_up = Initial(
    lambda: price_domestic() + price_import(), "_initial_initial_price_with_mark_up"
)


@component.add(
    name="initial primary inputs coefficients",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_initial_primary_inputs_coefficients": 1},
    other_deps={
        "_initial_initial_primary_inputs_coefficients": {
            "initial": {"primary_inputs_coefficients": 1},
            "step": {},
        }
    },
)
def initial_primary_inputs_coefficients():
    """
    Initla primary inputs coefficients
    """
    return _initial_initial_primary_inputs_coefficients()


_initial_initial_primary_inputs_coefficients = Initial(
    lambda: primary_inputs_coefficients(),
    "_initial_initial_primary_inputs_coefficients",
)


@component.add(
    name="INITIAL YEAR MARK UP SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_mark_up_sp"},
)
def initial_year_mark_up_sp():
    """
    Initial year mark-up
    """
    return _ext_constant_initial_year_mark_up_sp()


_ext_constant_initial_year_mark_up_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_MARK_UP_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_mark_up_sp",
)


@component.add(
    name="INITIAL YEAR TAX RATE PRODUCTION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_tax_rate_production_sp"},
)
def initial_year_tax_rate_production_sp():
    """
    Initial year tax rate production
    """
    return _ext_constant_initial_year_tax_rate_production_sp()


_ext_constant_initial_year_tax_rate_production_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_TAX_RATE_PRODUCTION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_tax_rate_production_sp",
)


@component.add(
    name="intermediate imports multipliers",
    units="DMNL",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I", "REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_import": 1, "leontief_inverse": 1},
)
def intermediate_imports_multipliers():
    """
    Intermediate imports multiplier. Imports required (directly and indirectly) to satisfy on unit of final demand.
    """
    return sum(
        technical_coefficients_import().rename(
            {"SECTORS I": "SECTORS MAP I", "SECTORS MAP I": "SECTORS MAP MAP I!"}
        )
        * leontief_inverse().rename(
            {"SECTORS I": "SECTORS MAP MAP I!", "SECTORS MAP I": "SECTORS I"}
        ),
        dim=["SECTORS MAP MAP I!"],
    )


@component.add(
    name="mark up",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_mark_up_sp": 1,
        "initial_year_mark_up_sp": 1,
        "time": 1,
        "mark_up_sp": 1,
        "mark_up_default": 1,
        "add_mark_up_low_unemploymnet_smooth": 1,
    },
)
def mark_up():
    """
    Producers' mark-up: share of profits over total price.
    """
    return if_then_else(
        np.logical_and(select_mark_up_sp() == 1, initial_year_mark_up_sp() <= time()),
        lambda: mark_up_sp(),
        lambda: add_mark_up_low_unemploymnet_smooth() * mark_up_default(),
    )


@component.add(
    name="MARK UP SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_mark_up_sp"},
)
def mark_up_sp():
    """
    Producers' mark-up: share of profits over total price.
    """
    return _ext_constant_mark_up_sp()


_ext_constant_mark_up_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "MARK_UP_VARIATION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_mark_up_sp",
)


@component.add(
    name="non accelerating wage inflation rate of unemployment to unemployment ratio",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_unemployment_rate": 2,
        "non_accelerating_wage_inflation_rate_of_unemployment": 1,
    },
)
def non_accelerating_wage_inflation_rate_of_unemployment_to_unemployment_ratio():
    """
    Ratio on non accelerating wage inflation rate of unemployment to unemployment
    """
    return if_then_else(
        delayed_ts_unemployment_rate() == 0,
        lambda: xr.DataArray(
            10, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
        ),
        lambda: zidz(
            non_accelerating_wage_inflation_rate_of_unemployment(),
            delayed_ts_unemployment_rate(),
        ),
    )


@component.add(
    name="price COICOP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COICOP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_economy": 1,
        "unit_conversion_dollars_mdollars": 2,
        "co2_tax_rate_households": 2,
        "delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015": 1,
        "delayed_ts_implicit_ghg_emission_factor_households_coicop": 1,
        "price_transformation": 2,
        "unit_conversion_tco2eq_mtco2eq": 2,
        "implicit_price_energy_households_coicop": 2,
        "price_coicop_without_co2_tax": 2,
    },
)
def price_coicop():
    """
    Price by consumption category including GHG prices (COICOP classification), when the economy switch is zero its isolated from the rest of the modules.
    """
    return if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            100,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "COICOP I": _subscript_dict["COICOP I"],
            },
            ["REGIONS 35 I", "COICOP I"],
        ),
        lambda: if_then_else(
            switch_economy() == 0,
            lambda: price_coicop_without_co2_tax()
            + sum(
                zidz(
                    co2_tax_rate_households().rename(
                        {"GHG ENERGY USE I": "GHG ENERGY USE I!"}
                    )
                    * unit_conversion_tco2eq_mtco2eq()
                    / unit_conversion_dollars_mdollars()
                    * delayed_ts_implicit_ghg_emissions_factor_households_coicop_until_2015()
                    .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
                    .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "COICOP I"),
                    implicit_price_energy_households_coicop().expand_dims(
                        {"GHG ENERGY USE I!": ["CO2", "CH4", "N2O"]}, 1
                    ),
                ),
                dim=["GHG ENERGY USE I!"],
            )
            * price_transformation(),
            lambda: price_coicop_without_co2_tax()
            + sum(
                zidz(
                    co2_tax_rate_households().rename(
                        {"GHG ENERGY USE I": "GHG ENERGY USE I!"}
                    )
                    * unit_conversion_tco2eq_mtco2eq()
                    / unit_conversion_dollars_mdollars()
                    * delayed_ts_implicit_ghg_emission_factor_households_coicop()
                    .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
                    .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "COICOP I"),
                    implicit_price_energy_households_coicop().expand_dims(
                        {"GHG ENERGY USE I!": ["CO2", "CH4", "N2O"]}, 1
                    ),
                ),
                dim=["GHG ENERGY USE I!"],
            )
            * price_transformation(),
        ),
    )


@component.add(
    name="price COICOP without CO2 tax",
    units="DMNL",
    subscripts=["REGIONS 35 I", "COICOP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_households": 1,
        "base2015_price_coicop": 4,
        "initial_import_shares_origin_final_demand": 2,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 2,
        "initial_import_shares_final_demand": 2,
        "price_transformation": 4,
        "initial_price_of_output": 2,
        "tax_rate_final_products_imports_default": 2,
        "consumption_structure_coicop": 4,
        "tax_rate_final_products_domestic_default": 2,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 2,
        "import_shares_final_demand_constrained": 2,
        "price_output": 2,
    },
)
def price_coicop_without_co2_tax():
    """
    Price by consumption category (COICOP classification)
    """
    return if_then_else(
        switch_eco_households() == 0,
        lambda: (
            sum(
                consumption_structure_coicop().rename({"SECTORS I": "SECTORS I!"})
                * (
                    initial_price_of_output()
                    * (
                        1
                        - initial_import_shares_final_demand()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                    * (
                        1
                        + tax_rate_final_products_domestic_default()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                ),
                dim=["SECTORS I!"],
            )
            / base2015_price_coicop()
        )
        * price_transformation()
        + (
            sum(
                consumption_structure_coicop().rename({"SECTORS I": "SECTORS I!"})
                * (
                    initial_price_of_output()
                    * initial_import_shares_final_demand()
                    .loc[:, :, "CONSUMPTION W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS I": "SECTORS I!"})
                    * initial_import_shares_origin_final_demand()
                    .loc[:, :, :, "CONSUMPTION W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS I!",
                        }
                    )
                    .transpose("REGIONS 35 I", "SECTORS I!", "REGIONS 35 MAP I!")
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                                "SECTORS I": "SECTORS I!",
                            }
                        )
                    ).transpose("REGIONS 35 I", "SECTORS I!", "REGIONS 35 MAP I!")
                    * (
                        1
                        + tax_rate_final_products_imports_default()
                        .loc[:, :, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS 35 I": "REGIONS 35 MAP I!",
                                "SECTORS I": "SECTORS I!",
                                "REGIONS 35 MAP I": "REGIONS 35 I",
                            }
                        )
                    ).transpose("REGIONS 35 I", "SECTORS I!", "REGIONS 35 MAP I!")
                ),
                dim=["SECTORS I!", "REGIONS 35 MAP I!"],
            )
            / base2015_price_coicop()
        )
        * price_transformation(),
        lambda: (
            sum(
                consumption_structure_coicop().rename({"SECTORS I": "SECTORS I!"})
                * (
                    price_output().rename({"SECTORS I": "SECTORS I!"})
                    * (
                        1
                        - import_shares_final_demand_constrained()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                    * (
                        1
                        + tax_rate_final_products_domestic_default()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename({"SECTORS I": "SECTORS I!"})
                    )
                ),
                dim=["SECTORS I!"],
            )
            / base2015_price_coicop()
        )
        * price_transformation()
        + (
            sum(
                consumption_structure_coicop().rename({"SECTORS I": "SECTORS I!"})
                * (
                    price_output().rename(
                        {"REGIONS 35 I": "REGIONS 35 MAP I!", "SECTORS I": "SECTORS I!"}
                    )
                    * import_shares_final_demand_constrained()
                    .loc[:, :, "CONSUMPTION W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS I": "SECTORS I!"})
                    .transpose("SECTORS I!", "REGIONS 35 I")
                    * initial_import_shares_origin_final_demand()
                    .loc[:, :, :, "CONSUMPTION W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS I!",
                        }
                    )
                    * (
                        1
                        + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                        .loc[:, :, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                                "SECTORS I": "SECTORS I!",
                            }
                        )
                    )
                    * (
                        1
                        + tax_rate_final_products_imports_default()
                        .loc[:, :, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        .rename(
                            {
                                "REGIONS 35 I": "REGIONS 35 MAP I!",
                                "SECTORS I": "SECTORS I!",
                                "REGIONS 35 MAP I": "REGIONS 35 I",
                            }
                        )
                    )
                ).transpose("REGIONS 35 I", "SECTORS I!", "REGIONS 35 MAP I!"),
                dim=["SECTORS I!", "REGIONS 35 MAP I!"],
            )
            / base2015_price_coicop()
        )
        * price_transformation(),
    )


@component.add(
    name="price domestic",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients_with_changes_in_material_prices": 1,
        "leontief_inverse": 1,
    },
)
def price_domestic():
    """
    Domestic price without mark-up.
    """
    return sum(
        primary_inputs_coefficients_with_changes_in_material_prices().rename(
            {"SECTORS I": "SECTORS MAP I!"}
        )
        * leontief_inverse().rename(
            {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
        ),
        dim=["SECTORS MAP I!"],
    )


@component.add(
    name="price domestic purchaser prices households",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
        "tax_rate_final_products_domestic_default": 1,
    },
)
def price_domestic_purchaser_prices_households():
    """
    Domestic prices in purchasers prices.
    """
    return (
        price_output()
        / price_transformation()
        * (
            1
            + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
            .loc[:, :, "CONSUMPTION W"]
            .reset_coords(drop=True)
        )
        * (
            1
            + tax_rate_final_products_domestic_default()
            .loc[:, :, "CONSUMPTION W"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="price domestic purchaser prices sectors",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_by_sectors": 1,
        "tax_rate_products_domestic_by_sectors_default": 1,
    },
)
def price_domestic_purchaser_prices_sectors():
    """
    Domestic prices in purchasers prices.
    """
    return (
        price_output()
        * (1 + trade_and_transportation_margins_paid_for_domestic_products_by_sectors())
        * (1 + tax_rate_products_domestic_by_sectors_default())
    )


@component.add(
    name="price GFCF",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_fixed_capital_formation_structure": 2,
        "price_transformation": 6,
        "import_shares_final_demand_constrained": 2,
        "price_output": 2,
        "tax_rate_final_products_domestic_default": 1,
        "trade_and_transportation_margins_paid_for_domestic_products_for_final_demand": 1,
        "base2015_price_gfcf": 2,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
        "tax_rate_final_products_imports_default": 1,
        "import_shares_origin_final_demand": 1,
    },
)
def price_gfcf():
    """
    Price of investment goods.
    """
    return (
        sum(
            gross_fixed_capital_formation_structure().rename(
                {"SECTORS I": "SECTORS I!"}
            )
            * (
                (
                    price_output().rename({"SECTORS I": "SECTORS I!"})
                    / price_transformation()
                )
                * (
                    1
                    - import_shares_final_demand_constrained()
                    .loc[:, :, "GROSS FIXED CAPITAL FORMATION W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS I": "SECTORS I!"})
                )
                * (
                    1
                    + trade_and_transportation_margins_paid_for_domestic_products_for_final_demand()
                    .loc[:, :, "GROSS FIXED CAPITAL FORMATION W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS I": "SECTORS I!"})
                )
                * (
                    1
                    + tax_rate_final_products_domestic_default()
                    .loc[:, :, "GROSS FIXED CAPITAL FORMATION W"]
                    .reset_coords(drop=True)
                    .rename({"SECTORS I": "SECTORS I!"})
                )
            ),
            dim=["SECTORS I!"],
        )
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
                },
                ["REGIONS 35 I", "SECTORS MAP I"],
            ),
            base2015_price_gfcf().rename({"SECTORS I": "SECTORS MAP I"}),
        )
        * price_transformation()
        + sum(
            gross_fixed_capital_formation_structure().rename(
                {"SECTORS I": "SECTORS I!"}
            )
            * (
                (
                    price_output().rename(
                        {"REGIONS 35 I": "REGIONS 35 MAP I!", "SECTORS I": "SECTORS I!"}
                    )
                    / price_transformation()
                )
                * import_shares_final_demand_constrained()
                .loc[:, :, "GROSS FIXED CAPITAL FORMATION W"]
                .reset_coords(drop=True)
                .rename({"SECTORS I": "SECTORS I!"})
                .transpose("SECTORS I!", "REGIONS 35 I")
                * import_shares_origin_final_demand()
                .loc[:, :, :, "GROSS FIXED CAPITAL FORMATION W"]
                .reset_coords(drop=True)
                .rename(
                    {"REGIONS 35 MAP I": "REGIONS 35 MAP I!", "SECTORS I": "SECTORS I!"}
                )
                * (
                    1
                    + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
                    .loc[:, :, :, "GROSS FIXED CAPITAL FORMATION W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS I!",
                        }
                    )
                )
                * (
                    1
                    + tax_rate_final_products_imports_default()
                    .loc[:, :, :, "GROSS FIXED CAPITAL FORMATION W"]
                    .reset_coords(drop=True)
                    .rename(
                        {
                            "REGIONS 35 I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS I!",
                            "REGIONS 35 MAP I": "REGIONS 35 I",
                        }
                    )
                )
            ).transpose("REGIONS 35 I", "SECTORS I!", "REGIONS 35 MAP I!"),
            dim=["SECTORS I!", "REGIONS 35 MAP I!"],
        )
        * zidz(
            xr.DataArray(
                price_transformation(),
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
                },
                ["REGIONS 35 I", "SECTORS MAP I"],
            ),
            base2015_price_gfcf().rename({"SECTORS I": "SECTORS MAP I"}),
        )
        * price_transformation()
    )


@component.add(
    name="price import",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients_with_changes_in_material_prices": 1,
        "intermediate_imports_multipliers": 1,
    },
)
def price_import():
    """
    Import price without mark-up.
    """
    return sum(
        primary_inputs_coefficients_with_changes_in_material_prices().rename(
            {"REGIONS 35 I": "REGIONS 35 MAP I!", "SECTORS I": "SECTORS MAP I!"}
        )
        * intermediate_imports_multipliers().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 MAP I!", "SECTORS MAP I": "SECTORS MAP I!"}
        ),
        dim=["REGIONS 35 MAP I!", "SECTORS MAP I!"],
    )


@component.add(
    name="price import purchaser prices households",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "price_transformation": 1,
        "import_shares_origin_final_demand": 1,
        "trade_and_transportation_margins_paid_for_imported_products_for_final_demand": 1,
        "tax_rate_final_products_imports_default": 1,
    },
)
def price_import_purchaser_prices_households():
    """
    Import prices in purchasers prices.
    """
    return sum(
        price_output().rename({"REGIONS 35 I": "REGIONS 35 MAP I!"})
        / price_transformation()
        * import_shares_origin_final_demand()
        .loc[:, :, :, "CONSUMPTION W"]
        .reset_coords(drop=True)
        .rename({"REGIONS 35 MAP I": "REGIONS 35 MAP I!"})
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_for_final_demand()
            .loc[:, :, :, "CONSUMPTION W"]
            .reset_coords(drop=True)
            .rename({"REGIONS 35 MAP I": "REGIONS 35 MAP I!"})
        )
        * (
            1
            + tax_rate_final_products_imports_default()
            .loc[:, :, :, "CONSUMPTION W"]
            .reset_coords(drop=True)
            .rename(
                {
                    "REGIONS 35 I": "REGIONS 35 MAP I!",
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                }
            )
        ),
        dim=["REGIONS 35 MAP I!"],
    ).transpose("REGIONS 35 I", "SECTORS I")


@component.add(
    name="price import purchaser prices sectors",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_output": 1,
        "import_shares_origin_intermediates": 1,
        "trade_and_transportation_margins_paid_for_imported_products_by_sectors": 1,
        "tax_rate_products_imports_by_sectors_default": 1,
    },
)
def price_import_purchaser_prices_sectors():
    """
    Import prices in purchasers prices.
    """
    return sum(
        price_output().rename({"REGIONS 35 I": "REGIONS 35 MAP I!"})
        * import_shares_origin_intermediates().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 MAP I!"}
        )
        * (
            1
            + trade_and_transportation_margins_paid_for_imported_products_by_sectors().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 MAP I!",
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                }
            )
        )
        * (
            1
            + tax_rate_products_imports_by_sectors_default().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 MAP I!",
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                }
            )
        ),
        dim=["REGIONS 35 MAP I!"],
    ).transpose("REGIONS 35 I", "SECTORS I", "SECTORS MAP I")


@component.add(
    name="price output",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "price_import": 2,
        "price_domestic": 2,
        "price_transformation": 2,
        "initial_price_with_mark_up": 2,
        "switches_mat2eco_by_sector": 1,
        "delayed_ts_price_materials_and_private_households": 1,
        "base_price_materials_and_private_households": 1,
    },
)
def price_output():
    """
    Output price by sector.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS NON EXTRACTION NON PH I"]] = True
    except_subs.loc[:, _subscript_dict["SECTORS EXTRACTION PH I"]] = False
    except_subs.loc[:, ["PRIVATE HOUSEHOLDS"]] = False
    value.values[except_subs.values] = if_then_else(
        time() == 2005,
        lambda: xr.DataArray(
            100,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS NON EXTRACTION NON PH I": _subscript_dict[
                    "SECTORS NON EXTRACTION NON PH I"
                ],
            },
            ["REGIONS 35 I", "SECTORS NON EXTRACTION NON PH I"],
        ),
        lambda: zidz(
            price_domestic()
            .loc[:, _subscript_dict["SECTORS NON EXTRACTION NON PH I"]]
            .rename({"SECTORS I": "SECTORS NON EXTRACTION NON PH I"})
            + price_import()
            .loc[:, _subscript_dict["SECTORS NON EXTRACTION NON PH I"]]
            .rename({"SECTORS I": "SECTORS NON EXTRACTION NON PH I"}),
            initial_price_with_mark_up()
            .loc[:, _subscript_dict["SECTORS NON EXTRACTION NON PH I"]]
            .rename({"SECTORS I": "SECTORS NON EXTRACTION NON PH I"}),
        )
        * price_transformation(),
    ).values[
        except_subs.loc[:, _subscript_dict["SECTORS NON EXTRACTION NON PH I"]].values
    ]
    value.loc[:, _subscript_dict["SECTORS EXTRACTION I"]] = (
        if_then_else(
            (switches_mat2eco_by_sector() == 1).expand_dims(
                {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 1
            ),
            lambda: delayed_ts_price_materials_and_private_households()
            .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
            .rename({"SECTORS EXTRACTION PH I": "SECTORS EXTRACTION I"})
            .transpose("SECTORS EXTRACTION I", "REGIONS 35 I"),
            lambda: if_then_else(
                time() == 2005,
                lambda: xr.DataArray(
                    100,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS EXTRACTION I": _subscript_dict["SECTORS EXTRACTION I"],
                    },
                    ["REGIONS 35 I", "SECTORS EXTRACTION I"],
                ),
                lambda: zidz(
                    price_domestic()
                    .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
                    .rename({"SECTORS I": "SECTORS EXTRACTION I"})
                    + price_import()
                    .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
                    .rename({"SECTORS I": "SECTORS EXTRACTION I"}),
                    initial_price_with_mark_up()
                    .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
                    .rename({"SECTORS I": "SECTORS EXTRACTION I"}),
                )
                * price_transformation(),
            ).transpose("SECTORS EXTRACTION I", "REGIONS 35 I"),
        )
        .transpose("REGIONS 35 I", "SECTORS EXTRACTION I")
        .values
    )
    value.loc[:, ["PRIVATE HOUSEHOLDS"]] = base_price_materials_and_private_households()
    return value


@component.add(
    name="price ratio households",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_domestic_purchaser_prices_households": 1,
        "initial_price_ratio_households": 1,
        "price_import_purchaser_prices_households": 1,
    },
)
def price_ratio_households():
    """
    Price ratio between domestic and foreign products for households.
    """
    return zidz(
        price_domestic_purchaser_prices_households(),
        price_import_purchaser_prices_households() * initial_price_ratio_households(),
    )


@component.add(
    name="price ratio sectors",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "price_domestic_purchaser_prices_sectors": 1,
        "price_import_purchaser_prices_sectors": 1,
        "base2015_price_ratio_sectors": 1,
    },
)
def price_ratio_sectors():
    """
    Price ratio between domestic and foreign products for intermdiates.
    """
    return zidz(
        price_domestic_purchaser_prices_sectors(),
        price_import_purchaser_prices_sectors() * base2015_price_ratio_sectors(),
    )


@component.add(
    name="primary inputs coefficients",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_prices": 1,
        "mark_up": 4,
        "depreciation_rate": 2,
        "technical_coefficients_import": 2,
        "taxes_on_respurces_per_unit_of_output": 2,
        "delayed_ts_price_gfcf": 2,
        "ghg_cost_per_unit_of_output": 2,
        "initial_labour_productivity": 1,
        "tax_rate_production": 2,
        "initial_capital_productivity": 1,
        "delayed_ts_price_output": 8,
        "price_transformation": 12,
        "technical_coefficients_domestic": 2,
        "tax_rate_products_imports_by_sectors_default": 2,
        "initial_wage_hour": 1,
        "tax_rate_products_domestic_by_sectors_default": 2,
        "switch_climate_change_damage": 1,
        "climate_change_incremental_damage_rate_to_capital_stock": 1,
        "capital_productivity": 1,
        "select_climate_change_impacts_sensitivity_sp": 1,
        "labour_productivity": 1,
        "climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included": 1,
        "wage_hour": 1,
        "switch_eco_climate_change_damage_capital": 1,
    },
)
def primary_inputs_coefficients():
    """
    Primary input coeffcients
    """
    return if_then_else(
        switch_eco_prices() == 0,
        lambda: (
            delayed_ts_price_gfcf()
            / price_transformation()
            * depreciation_rate()
            * zidz(
                xr.DataArray(
                    1,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                initial_capital_productivity(),
            )
            + (
                zidz(initial_wage_hour(), initial_labour_productivity())
                + sum(
                    delayed_ts_price_output().rename({"SECTORS I": "SECTORS MAP I!"})
                    / price_transformation()
                    * technical_coefficients_domestic().rename(
                        {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                    )
                    * tax_rate_products_domestic_by_sectors_default().rename(
                        {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                    ),
                    dim=["SECTORS MAP I!"],
                )
                + sum(
                    delayed_ts_price_output().rename(
                        {
                            "REGIONS 35 I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                        }
                    )
                    / price_transformation()
                    * technical_coefficients_import().rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                            "SECTORS MAP I": "SECTORS I",
                        }
                    )
                    * tax_rate_products_imports_by_sectors_default().rename(
                        {
                            "REGIONS 35 I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                            "REGIONS 35 MAP I": "REGIONS 35 I",
                            "SECTORS MAP I": "SECTORS I",
                        }
                    ),
                    dim=["REGIONS 35 MAP I!", "SECTORS MAP I!"],
                )
                + delayed_ts_price_output()
                / price_transformation()
                * tax_rate_production()
                + ghg_cost_per_unit_of_output()
                + taxes_on_respurces_per_unit_of_output()
                + if_then_else(
                    mark_up() < 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "SECTORS I": _subscript_dict["SECTORS I"],
                        },
                        ["REGIONS 35 I", "SECTORS I"],
                    ),
                    lambda: delayed_ts_price_output()
                    / price_transformation()
                    * mark_up(),
                )
            )
        )
        * price_transformation(),
        lambda: (
            delayed_ts_price_gfcf()
            / price_transformation()
            * (
                depreciation_rate()
                + if_then_else(
                    np.logical_or(
                        switch_climate_change_damage() == 0,
                        switch_eco_climate_change_damage_capital() == 0,
                    ),
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "SECTORS I": _subscript_dict["SECTORS I"],
                        },
                        ["REGIONS 35 I", "SECTORS I"],
                    ),
                    lambda: if_then_else(
                        select_climate_change_impacts_sensitivity_sp() == 0,
                        lambda: climate_change_incremental_damage_rate_to_capital_stock(),
                        lambda: climate_change_incremental_damage_rate_to_capital_stock_extrapolations_included(),
                    ),
                )
            )
            * zidz(
                xr.DataArray(
                    1,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                capital_productivity(),
            )
            + (
                zidz(wage_hour(), labour_productivity())
                + sum(
                    delayed_ts_price_output().rename({"SECTORS I": "SECTORS MAP I!"})
                    / price_transformation()
                    * technical_coefficients_domestic().rename(
                        {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                    )
                    * tax_rate_products_domestic_by_sectors_default().rename(
                        {"SECTORS I": "SECTORS MAP I!", "SECTORS MAP I": "SECTORS I"}
                    ),
                    dim=["SECTORS MAP I!"],
                )
                + sum(
                    delayed_ts_price_output().rename(
                        {
                            "REGIONS 35 I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                        }
                    )
                    / price_transformation()
                    * technical_coefficients_import().rename(
                        {
                            "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                            "SECTORS MAP I": "SECTORS I",
                        }
                    )
                    * tax_rate_products_imports_by_sectors_default().rename(
                        {
                            "REGIONS 35 I": "REGIONS 35 MAP I!",
                            "SECTORS I": "SECTORS MAP I!",
                            "REGIONS 35 MAP I": "REGIONS 35 I",
                            "SECTORS MAP I": "SECTORS I",
                        }
                    ),
                    dim=["REGIONS 35 MAP I!", "SECTORS MAP I!"],
                )
                + delayed_ts_price_output()
                / price_transformation()
                * tax_rate_production()
                + ghg_cost_per_unit_of_output()
                + taxes_on_respurces_per_unit_of_output()
                + if_then_else(
                    mark_up() < 0,
                    lambda: xr.DataArray(
                        0,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "SECTORS I": _subscript_dict["SECTORS I"],
                        },
                        ["REGIONS 35 I", "SECTORS I"],
                    ),
                    lambda: delayed_ts_price_output()
                    / price_transformation()
                    * mark_up(),
                )
            )
        )
        * price_transformation(),
    )


@component.add(
    name="primary inputs coefficients with changes in material prices",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "primary_inputs_coefficients": 2,
        "initial_primary_inputs_coefficients": 1,
        "price_transformation": 1,
        "time": 1,
        "delayed_ts_price_materials_and_private_households": 1,
    },
)
def primary_inputs_coefficients_with_changes_in_material_prices():
    """
    Primary input coefficients recalculated taking into account changes in the material prices.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS NON EXTRACTION I"]] = True
    except_subs.loc[:, _subscript_dict["SECTORS EXTRACTION I"]] = False
    value.values[except_subs.values] = (
        primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS NON EXTRACTION I"]]
        .rename({"SECTORS I": "SECTORS NON EXTRACTION I"})
        .values[except_subs.loc[:, _subscript_dict["SECTORS NON EXTRACTION I"]].values]
    )
    value.loc[:, _subscript_dict["SECTORS EXTRACTION I"]] = if_then_else(
        time() >= 2015,
        lambda: initial_primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
        .rename({"SECTORS I": "SECTORS EXTRACTION I"})
        * delayed_ts_price_materials_and_private_households()
        .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
        .rename({"SECTORS EXTRACTION PH I": "SECTORS EXTRACTION I"})
        / price_transformation(),
        lambda: primary_inputs_coefficients()
        .loc[:, _subscript_dict["SECTORS EXTRACTION I"]]
        .rename({"SECTORS I": "SECTORS EXTRACTION I"}),
    ).values
    return value


@component.add(
    name="SELECT CO2 TAX HOUSEHOLDS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_co2_tax_households_sp"},
)
def select_co2_tax_households_sp():
    """
    Select CO2 tax 0: No CO2 tax 1: CO2 tax households
    """
    return _ext_constant_select_co2_tax_households_sp()


_ext_constant_select_co2_tax_households_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CO2_TAX_HOUSEHOLDS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_co2_tax_households_sp",
)


@component.add(
    name="SELECT CO2 TAX SECTORS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_co2_tax_sectors_sp"},
)
def select_co2_tax_sectors_sp():
    """
    Select CO2 tax scenario 0: No CO2 tax 1: CO2 tax sectors
    """
    return _ext_constant_select_co2_tax_sectors_sp()


_ext_constant_select_co2_tax_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_CO2_TAX_SECTORS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_co2_tax_sectors_sp",
)


@component.add(
    name="SELECT GASES CO2 TAX HOUSEHOLDS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_gases_co2_tax_households_sp"},
)
def select_gases_co2_tax_households_sp():
    """
    Select gases affected by CO2 tax 0: CO2 1: CH4 2: N20 3: CO2, CH4, N2O
    """
    return _ext_constant_select_gases_co2_tax_households_sp()


_ext_constant_select_gases_co2_tax_households_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_GASES_CO2_TAX_HOUSEHOLDS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_gases_co2_tax_households_sp",
)


@component.add(
    name="SELECT GASES CO2 TAX SECTORS SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_gases_co2_tax_sectors_sp"},
)
def select_gases_co2_tax_sectors_sp():
    """
    Select gases affected by CO2 tax 0: CO2 1: CH4 2: N20 3: CO2, CH4, N2O
    """
    return _ext_constant_select_gases_co2_tax_sectors_sp()


_ext_constant_select_gases_co2_tax_sectors_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_GASES_CO2_TAX_SECTORS_SP",
    {},
    _root,
    {},
    "_ext_constant_select_gases_co2_tax_sectors_sp",
)


@component.add(
    name="SELECT MARK UP SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_mark_up_sp"},
)
def select_mark_up_sp():
    """
    Switch mark-up 0: Default 1: User defined
    """
    return _ext_constant_select_mark_up_sp()


_ext_constant_select_mark_up_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_MARK_UP_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_mark_up_sp",
)


@component.add(
    name="SELECT TAX RATE PRODUCTION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_tax_rate_production_sp"},
)
def select_tax_rate_production_sp():
    """
    Tax rate production 0: Default 1: User defined
    """
    return _ext_constant_select_tax_rate_production_sp()


_ext_constant_select_tax_rate_production_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_TAX_RATE_PRODUCTION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_tax_rate_production_sp",
)


@component.add(
    name="SWITCH ECO PRICES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_prices"},
)
def switch_eco_prices():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_prices()


_ext_constant_switch_eco_prices = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PRICES",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_prices",
)


@component.add(
    name="switches mat2eco by sector",
    subscripts=["SECTORS EXTRACTION I"],
    comp_type="Constant, Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat2eco_al_price": 1,
        "switch_mat2eco_coal_price": 1,
        "switch_mat2eco_cu_price": 1,
        "switch_mat2eco_fe_price": 1,
        "switch_mat2eco_gas_price": 1,
        "switch_mat2eco_ni_price": 1,
        "switch_mat2eco_oil_price": 1,
    },
)
def switches_mat2eco_by_sector():
    """
    Switches materials to economy by economic sector
    """
    value = xr.DataArray(
        np.nan,
        {"SECTORS EXTRACTION I": _subscript_dict["SECTORS EXTRACTION I"]},
        ["SECTORS EXTRACTION I"],
    )
    value.loc[["MINING AND MANUFACTURING ALUMINIUM"]] = switch_mat2eco_al_price()
    value.loc[["MINING COAL"]] = switch_mat2eco_coal_price()
    value.loc[["MINING AND MANUFACTURING COPPER"]] = switch_mat2eco_cu_price()
    value.loc[["MINING AND MANUFACTURING IRON"]] = switch_mat2eco_fe_price()
    value.loc[["EXTRACTION GAS"]] = switch_mat2eco_gas_price()
    value.loc[["MINING AND MANUFACTURING NICKEL"]] = switch_mat2eco_ni_price()
    value.loc[["EXTRACTION OIL"]] = switch_mat2eco_oil_price()
    value.loc[["EXTRACTION OTHER GAS"]] = 0
    value.loc[["MINING AND MANUFACTURING URANIUM THORIUM"]] = 0
    value.loc[["MINING AND MANUFACTURING PRECIOUS METALS"]] = 0
    value.loc[["MINING AND MANUFACTURING LEAD ZINC TIN"]] = 0
    value.loc[["MINING AND MANUFACTURING OTHER METALS"]] = 0
    value.loc[["MINING NON METALS"]] = 0
    return value


@component.add(
    name="tax GHG households",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015": 1,
        "co2_tax_rate_households": 2,
        "delayed_ts_ghg_emissions_households_coicop_35_r_co2eq": 1,
    },
)
def tax_ghg_households():
    """
    Government revenues from CO taxes: households, properly modularized when the economy witch is zero.
    """
    return if_then_else(
        switch_economy() == 0,
        lambda: sum(
            co2_tax_rate_households().rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
            * delayed_ts_ghg_emissions_households_coicop_35_r_co2eq_until_2015()
            .loc[:, _subscript_dict["COICOP ENERGY I"], :]
            .rename(
                {
                    "COICOP I": "COICOP ENERGY I!",
                    "GHG ENERGY USE I": "GHG ENERGY USE I!",
                }
            )
            .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "COICOP ENERGY I!"),
            dim=["GHG ENERGY USE I!", "COICOP ENERGY I!"],
        ),
        lambda: sum(
            co2_tax_rate_households().rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
            * delayed_ts_ghg_emissions_households_coicop_35_r_co2eq()
            .loc[:, _subscript_dict["COICOP ENERGY I"], :]
            .rename(
                {
                    "COICOP I": "COICOP ENERGY I!",
                    "GHG ENERGY USE I": "GHG ENERGY USE I!",
                }
            )
            .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "COICOP ENERGY I!"),
            dim=["GHG ENERGY USE I!", "COICOP ENERGY I!"],
        ),
    )


@component.add(
    name="tax GHG paid by sector",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_economy": 1,
        "co2_tax_rate_sectors": 2,
        "unit_conversion_dollars_mdollars": 2,
        "unit_conversion_gtco2eq_mtco2eq": 2,
        "unit_conversion_tco2eq_mtco2eq": 2,
        "delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015": 1,
        "delayed_ts_ghg_energy_emissions_35r_co2eq": 1,
    },
)
def tax_ghg_paid_by_sector():
    """
    GHG taxes paid by sector, modularized when the switch of economy is zero.
    """
    return if_then_else(
        switch_economy() == 0,
        lambda: sum(
            co2_tax_rate_sectors()
            .loc[_subscript_dict["REGIONS 35 I"], :]
            .rename(
                {
                    "REGIONS 36 I": "REGIONS 35 I",
                    "GHG ENERGY USE I": "GHG ENERGY USE I!",
                }
            )
            / unit_conversion_dollars_mdollars()
            * unit_conversion_tco2eq_mtco2eq()
            * delayed_ts_imv_ghg_energy_emissions_35r_co2eq_until_2015()
            .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
            .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "SECTORS I"),
            dim=["GHG ENERGY USE I!"],
        )
        * unit_conversion_gtco2eq_mtco2eq(),
        lambda: sum(
            co2_tax_rate_sectors()
            .loc[_subscript_dict["REGIONS 35 I"], :]
            .rename(
                {
                    "REGIONS 36 I": "REGIONS 35 I",
                    "GHG ENERGY USE I": "GHG ENERGY USE I!",
                }
            )
            / unit_conversion_dollars_mdollars()
            * unit_conversion_tco2eq_mtco2eq()
            * delayed_ts_ghg_energy_emissions_35r_co2eq()
            .rename({"GHG ENERGY USE I": "GHG ENERGY USE I!"})
            .transpose("REGIONS 35 I", "GHG ENERGY USE I!", "SECTORS I"),
            dim=["GHG ENERGY USE I!"],
        )
        * unit_conversion_gtco2eq_mtco2eq(),
    )


@component.add(
    name="tax GHG sectors",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"tax_ghg_paid_by_sector": 1},
)
def tax_ghg_sectors():
    """
    Government revenues from GHG taxes paid by sectors
    """
    return sum(
        tax_ghg_paid_by_sector().rename({"SECTORS I": "SECTORS I!"}), dim=["SECTORS I!"]
    )


@component.add(
    name="tax rate production",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "tax_rate_output_default_default": 2,
        "initial_year_tax_rate_production_sp": 1,
        "select_tax_rate_production_sp": 1,
        "tax_rate_production_sp": 1,
    },
)
def tax_rate_production():
    """
    Tax rate on production. Note that these are net tax rates and include both taxes and subsides.
    """
    return if_then_else(
        time() <= 2015,
        lambda: tax_rate_output_default_default(),
        lambda: if_then_else(
            np.logical_and(
                select_tax_rate_production_sp() == 1,
                initial_year_tax_rate_production_sp() >= time(),
            ),
            lambda: tax_rate_production_sp(),
            lambda: tax_rate_output_default_default(),
        ),
    )


@component.add(
    name="TAX RATE PRODUCTION SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_tax_rate_production_sp"},
)
def tax_rate_production_sp():
    """
    Tax rate on production.
    """
    return _ext_constant_tax_rate_production_sp()


_ext_constant_tax_rate_production_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "TAX_RATE_PRODUCTION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_tax_rate_production_sp",
)


@component.add(
    name="taxes on respurces per unit of output",
    units="Mdollars/Mdollars 2015",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_taxes_on_resources_paid_by_extration_sectors": 1,
        "delayed_ts_output_real": 1,
    },
)
def taxes_on_respurces_per_unit_of_output():
    """
    Taxes on resources per unit of output
    """
    return zidz(
        delayed_ts_taxes_on_resources_paid_by_extration_sectors(),
        delayed_ts_output_real(),
    )
