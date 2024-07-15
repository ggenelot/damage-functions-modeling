"""
Module economylabour
Translated using PySD version 3.14.0
"""

@component.add(
    name="annual growth labour productivity",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 3,
        "aux_growth_labour_productivity": 1,
        "annual_labour_productivity_variation": 1,
    },
)
def annual_growth_labour_productivity():
    """
    Annual growth labour productivity.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: if_then_else(
            time() == integer(time()),
            lambda: annual_labour_productivity_variation(),
            lambda: aux_growth_labour_productivity(),
        ),
    )


@component.add(
    name="annual labour productivity",
    units="Mdollars 2015/Mhours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2, "labour_productivity": 1, "aux_labour_productivity": 1},
)
def annual_labour_productivity():
    return if_then_else(
        time() == integer(time()),
        lambda: labour_productivity(),
        lambda: aux_labour_productivity(),
    )


@component.add(
    name="annual labour productivity variation",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_labour_productivity_variation_sp": 1,
        "initial_year_labour_productivity_variation_sp": 1,
        "time": 1,
        "labour_productivity_variation_sp": 1,
        "labour_productivity_variation_default": 1,
    },
)
def annual_labour_productivity_variation():
    """
    Labour productivity variation. IF_THEN_ELSE(SWITCH_CALIBRATION_LABOUR_PRODUCTIVITY=1,calibrated_labour_productivity_ growth[REGIONS 35 I,SECTORS I], IF_THEN_ELSE(Time<INITIAL_YEAR_LABOUR_PRODUCTIVITY_VARIATION_SP,LABOUR_PRODUCTIVITY_V ARIATION_DEFAULT[REGIONS 35 I], IF_THEN_ELSE(SELECT_LABOUR_PRODUCTIVITY_VARIATION_SP=0, LABOUR_PRODUCTIVITY_VARIATION_DEFAULT[REGIONS 35 I], IF_THEN_ELSE(SELECT_PROPENSITY_TO_CONSUME_SP=1,LABOUR_PRODUCTIVITY_VARIATION_HIGH_PRO PENSITY_TO_CONSUME_SP[REGIONS 35 I ], LABOUR_PRODUCTIVITY_VARIATION_SP[REGIONS 35 I,SECTORS I] )) ))
    """
    return if_then_else(
        np.logical_and(
            select_labour_productivity_variation_sp() == 1,
            initial_year_labour_productivity_variation_sp() >= time(),
        ),
        lambda: labour_productivity_variation_sp(),
        lambda: labour_productivity_variation_default().expand_dims(
            {"SECTORS I": _subscript_dict["SECTORS I"]}, 1
        ),
    )


@component.add(
    name="annual variation hours per worker",
    units="Mhours/(Year*Year*kpeople)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "initial_year_working_time_variation_sp": 2,
        "final_year_working_time_variation_sp": 2,
        "working_time_target": 1,
        "initial_hours_per_worker": 1,
    },
)
def annual_variation_hours_per_worker():
    """
    Annual variation hours per worker
    """
    return if_then_else(
        np.logical_or(
            time() < initial_year_working_time_variation_sp(),
            time() >= final_year_working_time_variation_sp(),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
            },
            ["REGIONS 35 I", "SECTORS I"],
        ),
        lambda: (working_time_target() - initial_hours_per_worker())
        / (
            final_year_working_time_variation_sp()
            - initial_year_working_time_variation_sp()
        ),
    )


@component.add(
    name="annual wage hour variation",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_limit_annual_growth_wages_sp": 1,
        "time": 1,
        "initial_limit_annual_growth_wages_sp": 1,
        "limit_lower_bound_annual_growth_wages_sp": 1,
        "annual_wage_hour_variation_index": 2,
        "limit_upper_bound_annual_growth_wages_sp": 1,
    },
)
def annual_wage_hour_variation():
    """
    Annual wage hour variation. MAX(MIN(annual_wage_hour_variation_index[REGIONS_35_I,SECTORS_I]/100-1,0.1) ,-0.02)
    """
    return if_then_else(
        np.logical_and(
            select_limit_annual_growth_wages_sp() == 1,
            time() >= initial_limit_annual_growth_wages_sp(),
        ).expand_dims({"SECTORS I": _subscript_dict["SECTORS I"]}, 1),
        lambda: np.maximum(
            np.minimum(
                annual_wage_hour_variation_index() / 100 - 1,
                limit_upper_bound_annual_growth_wages_sp(),
            ),
            limit_lower_bound_annual_growth_wages_sp(),
        ),
        lambda: annual_wage_hour_variation_index() / 100 - 1,
    )


@component.add(
    name="annual wage hour variation index",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_labour": 1,
        "non_accelerating_wage_inflation_rate_of_unemployment": 4,
        "epsilon_wage_hour": 2,
        "initial_delayed_consumer_price_index": 2,
        "delayed_ts_labour_productivity": 4,
        "constant_wage": 2,
        "unemployment_rate": 4,
        "labour_productivity": 2,
        "alpha_wage_hour": 2,
        "initial_delayed_2_consumer_price_index": 1,
        "gamma_wage_hour": 2,
        "delayed_consumer_price_index": 2,
        "delayed_2_consumer_price_index": 1,
    },
)
def annual_wage_hour_variation_index():
    """
    Index wage per hour annual growth
    """
    return if_then_else(
        switch_eco_labour() == 0,
        lambda: np.exp(
            constant_wage()
            + if_then_else(
                (
                    unemployment_rate()
                    / non_accelerating_wage_inflation_rate_of_unemployment()
                    <= 0
                ).expand_dims({"SECTORS I": _subscript_dict["SECTORS I"]}, 1),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    alpha_wage_hour()
                    * np.log(
                        unemployment_rate()
                        / non_accelerating_wage_inflation_rate_of_unemployment()
                    )
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
            + if_then_else(
                delayed_ts_labour_productivity() <= 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    epsilon_wage_hour()
                    * np.log(
                        zidz(labour_productivity(), delayed_ts_labour_productivity())
                    ).transpose("SECTORS I", "REGIONS 35 I")
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
            + if_then_else(
                (initial_delayed_consumer_price_index() <= 0).expand_dims(
                    {"SECTORS I": _subscript_dict["SECTORS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    gamma_wage_hour()
                    * np.log(
                        initial_delayed_consumer_price_index()
                        / initial_delayed_2_consumer_price_index()
                    )
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
        ),
        lambda: np.exp(
            constant_wage()
            + if_then_else(
                (
                    unemployment_rate()
                    / non_accelerating_wage_inflation_rate_of_unemployment()
                    <= 0
                ).expand_dims({"SECTORS I": _subscript_dict["SECTORS I"]}, 1),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    alpha_wage_hour()
                    * np.log(
                        unemployment_rate()
                        / non_accelerating_wage_inflation_rate_of_unemployment()
                    )
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
            + if_then_else(
                delayed_ts_labour_productivity() <= 0,
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    epsilon_wage_hour()
                    * np.log(
                        zidz(labour_productivity(), delayed_ts_labour_productivity())
                    ).transpose("SECTORS I", "REGIONS 35 I")
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
            + if_then_else(
                (delayed_consumer_price_index() <= 0).expand_dims(
                    {"SECTORS I": _subscript_dict["SECTORS I"]}, 1
                ),
                lambda: xr.DataArray(
                    0,
                    {
                        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                        "SECTORS I": _subscript_dict["SECTORS I"],
                    },
                    ["REGIONS 35 I", "SECTORS I"],
                ),
                lambda: (
                    gamma_wage_hour()
                    * np.log(
                        delayed_consumer_price_index()
                        / delayed_2_consumer_price_index()
                    )
                ).transpose("REGIONS 35 I", "SECTORS I"),
            )
        ),
    )


@component.add(
    name="aux growth labour productivity",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_growth_labour_productivity": 1},
    other_deps={
        "_delayfixed_aux_growth_labour_productivity": {
            "initial": {"time_step": 1},
            "step": {"annual_growth_labour_productivity": 1},
        }
    },
)
def aux_growth_labour_productivity():
    """
    Auxiliar annual growth labour productivity
    """
    return _delayfixed_aux_growth_labour_productivity()


_delayfixed_aux_growth_labour_productivity = DelayFixed(
    lambda: annual_growth_labour_productivity(),
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
    "_delayfixed_aux_growth_labour_productivity",
)


@component.add(
    name="aux labour productivity",
    units="Mdollars 2015/Mhours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_labour_productivity": 1},
    other_deps={
        "_delayfixed_aux_labour_productivity": {
            "initial": {"time_step": 1},
            "step": {"annual_labour_productivity": 1},
        }
    },
)
def aux_labour_productivity():
    """
    Auxiliar labour productivity.
    """
    return _delayfixed_aux_labour_productivity()


_delayfixed_aux_labour_productivity = DelayFixed(
    lambda: annual_labour_productivity(),
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
    "_delayfixed_aux_labour_productivity",
)


@component.add(
    name="average wage hour",
    units="dollars/Hour",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "labour_compensation": 1,
        "unit_conversion_dollars_mdollars": 1,
        "hours_worked": 1,
        "unit_conversion_hours_mhours": 1,
    },
)
def average_wage_hour():
    """
    Weighted average wage per hour.
    """
    return zidz(
        sum(
            labour_compensation().rename({"SECTORS I": "SECTORS I!"})
            * unit_conversion_dollars_mdollars(),
            dim=["SECTORS I!"],
        ),
        sum(
            hours_worked().rename({"SECTORS I": "SECTORS I!"})
            * unit_conversion_hours_mhours(),
            dim=["SECTORS I!"],
        ),
    )


@component.add(
    name="BASE WORKING AGE POPULATION",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_base_working_age_population"},
)
def base_working_age_population():
    """
    Working age population: persons aged 15 years and older.
    """
    return _ext_constant_base_working_age_population()


_ext_constant_base_working_age_population = ExtConstant(
    "model_parameters/economy/Primary_Inputs.xlsx",
    "BASE_Working_age_pop",
    "BASE_WORKING_AGE_POPULATION",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_base_working_age_population",
)


@component.add(
    name="climate change impact in labour productivity",
    units="Mdollars 2015/(Mhours*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_climate_change_damage": 1,
        "switch_eco_climate_change_damage_labour_productivity": 1,
        "switch_eco_labour": 1,
        "labour_productivity": 1,
        "heat_stress_incremental_damage_function": 1,
        "vector_borne_diseases_incremental_damage_function": 1,
    },
)
def climate_change_impact_in_labour_productivity():
    """
    Climate change impact in labour productivity
    """
    return if_then_else(
        np.logical_or(
            switch_climate_change_damage() == 0,
            np.logical_or(
                switch_eco_climate_change_damage_labour_productivity() == 0,
                switch_eco_labour() == 0,
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
        lambda: labour_productivity()
        * (
            heat_stress_incremental_damage_function()
            + vector_borne_diseases_incremental_damage_function()
        ),
    )


@component.add(
    name="delayed 2 consumer price index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_2_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_2_consumer_price_index": {
            "initial": {"initial_delayed_2_consumer_price_index": 1},
            "step": {
                "time": 1,
                "initial_delayed_2_consumer_price_index": 1,
                "consumer_price_index": 1,
            },
        }
    },
)
def delayed_2_consumer_price_index():
    """
    Delayed Consumer price index.
    """
    return _delayfixed_delayed_2_consumer_price_index()


_delayfixed_delayed_2_consumer_price_index = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_2_consumer_price_index(),
        lambda: consumer_price_index(),
    ),
    lambda: 2,
    lambda: initial_delayed_2_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_2_consumer_price_index",
)


@component.add(
    name="delayed consumer price index",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_consumer_price_index": 1},
    other_deps={
        "_delayfixed_delayed_consumer_price_index": {
            "initial": {"initial_delayed_consumer_price_index": 1},
            "step": {
                "time": 1,
                "initial_delayed_consumer_price_index": 1,
                "consumer_price_index": 1,
            },
        }
    },
)
def delayed_consumer_price_index():
    """
    Delayed Consumer price index.
    """
    return _delayfixed_delayed_consumer_price_index()


_delayfixed_delayed_consumer_price_index = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_consumer_price_index(),
        lambda: consumer_price_index(),
    ),
    lambda: 1,
    lambda: initial_delayed_consumer_price_index(),
    time_step,
    "_delayfixed_delayed_consumer_price_index",
)


@component.add(
    name="delayed TS hours worked",
    units="Mhours/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_hours_worked": 1},
    other_deps={
        "_delayfixed_delayed_ts_hours_worked": {
            "initial": {"initial_delayed_hours_worked": 1, "time_step": 1},
            "step": {"time": 1, "initial_delayed_hours_worked": 1, "hours_worked": 1},
        }
    },
)
def delayed_ts_hours_worked():
    """
    Delayed hours worked.
    """
    return _delayfixed_delayed_ts_hours_worked()


_delayfixed_delayed_ts_hours_worked = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: initial_delayed_hours_worked(), lambda: hours_worked()
    ),
    lambda: time_step(),
    lambda: initial_delayed_hours_worked(),
    time_step,
    "_delayfixed_delayed_ts_hours_worked",
)


@component.add(
    name="delayed TS labour compensation total",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_labour_compensation_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_labour_compensation_total": {
            "initial": {"initial_labour_compensation": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_labour_compensation": 1,
                "labour_compensation_total": 1,
            },
        }
    },
)
def delayed_ts_labour_compensation_total():
    """
    Delayed labour compensation total.
    """
    return _delayfixed_delayed_ts_labour_compensation_total()


_delayfixed_delayed_ts_labour_compensation_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: sum(
            initial_labour_compensation().rename({"SECTORS I": "SECTORS I!"}),
            dim=["SECTORS I!"],
        ),
        lambda: labour_compensation_total(),
    ),
    lambda: time_step(),
    lambda: sum(
        initial_labour_compensation().rename({"SECTORS I": "SECTORS I!"}),
        dim=["SECTORS I!"],
    ),
    time_step,
    "_delayfixed_delayed_ts_labour_compensation_total",
)


@component.add(
    name="delayed TS labour productivity",
    units="Mdollars 2015/Mhours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_labour_productivity": 1},
    other_deps={
        "_delayfixed_delayed_ts_labour_productivity": {
            "initial": {"initial_delayed_labour_productivity": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_labour_productivity": 1,
                "labour_productivity": 1,
            },
        }
    },
)
def delayed_ts_labour_productivity():
    """
    Delayed labour productivity.
    """
    return _delayfixed_delayed_ts_labour_productivity()


_delayfixed_delayed_ts_labour_productivity = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_labour_productivity(),
        lambda: labour_productivity(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_labour_productivity(),
    time_step,
    "_delayfixed_delayed_ts_labour_productivity",
)


@component.add(
    name="delayed TS unemployment rate",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_unemployment_rate": 1},
    other_deps={
        "_delayfixed_delayed_ts_unemployment_rate": {
            "initial": {"initial_delayed_unemployment_rate": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_unemployment_rate": 1,
                "unemployment_rate": 1,
            },
        }
    },
)
def delayed_ts_unemployment_rate():
    """
    Delayed unemployment rate.
    """
    return _delayfixed_delayed_ts_unemployment_rate()


_delayfixed_delayed_ts_unemployment_rate = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_unemployment_rate(),
        lambda: unemployment_rate(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_unemployment_rate(),
    time_step,
    "_delayfixed_delayed_ts_unemployment_rate",
)


@component.add(
    name="delayed TS wage hour",
    units="dollars/Hour",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_wage_hour": 1},
    other_deps={
        "_delayfixed_delayed_ts_wage_hour": {
            "initial": {"initial_delayed_wage_hour": 1, "time_step": 1},
            "step": {"time": 1, "initial_delayed_wage_hour": 1, "wage_hour": 1},
        }
    },
)
def delayed_ts_wage_hour():
    """
    Delayed (time step) wage per hour.
    """
    return _delayfixed_delayed_ts_wage_hour()


_delayfixed_delayed_ts_wage_hour = DelayFixed(
    lambda: if_then_else(
        time() <= 2016, lambda: initial_delayed_wage_hour(), lambda: wage_hour()
    ),
    lambda: time_step(),
    lambda: initial_delayed_wage_hour(),
    time_step,
    "_delayfixed_delayed_ts_wage_hour",
)


@component.add(
    name="delayed TS wage hour total",
    units="dollars/Hour",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_wage_hour_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_wage_hour_total": {
            "initial": {"initial_delayed_wage_hour_total": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_delayed_wage_hour_total": 1,
                "average_wage_hour": 1,
            },
        }
    },
)
def delayed_ts_wage_hour_total():
    """
    Delayed weighted average wage per hour.
    """
    return _delayfixed_delayed_ts_wage_hour_total()


_delayfixed_delayed_ts_wage_hour_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_wage_hour_total(),
        lambda: average_wage_hour(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_wage_hour_total(),
    time_step,
    "_delayfixed_delayed_ts_wage_hour_total",
)


@component.add(
    name="delayed TS working age population",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_working_age_population": 1},
    other_deps={
        "_delayfixed_delayed_ts_working_age_population": {
            "initial": {"time_step": 1},
            "step": {"working_age_population": 1},
        }
    },
)
def delayed_ts_working_age_population():
    return _delayfixed_delayed_ts_working_age_population()


_delayfixed_delayed_ts_working_age_population = DelayFixed(
    lambda: working_age_population(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    time_step,
    "_delayfixed_delayed_ts_working_age_population",
)


@component.add(
    name="employment by sector",
    units="kpeople",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"hours_worked": 1, "hours_per_worker": 1},
)
def employment_by_sector():
    """
    Employment.
    """
    return zidz(hours_worked(), hours_per_worker())


@component.add(
    name="employment total",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_by_sector": 1},
)
def employment_total():
    """
    Total employment.
    """
    return sum(
        employment_by_sector().rename({"SECTORS I": "SECTORS I!"}), dim=["SECTORS I!"]
    )


@component.add(
    name="FINAL YEAR WORKING TIME VARIATION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_final_year_working_time_variation_sp"},
)
def final_year_working_time_variation_sp():
    return _ext_constant_final_year_working_time_variation_sp()


_ext_constant_final_year_working_time_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "FINAL_YEAR_WORKING_TIME_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_final_year_working_time_variation_sp",
)


@component.add(
    name="hours per worker",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "initial_year_working_time_variation_sp": 1,
        "initial_hours_per_worker": 1,
        "model_explorer_working_time_variation": 1,
        "stock_hours_per_worker": 1,
        "switch_model_explorer": 1,
    },
)
def hours_per_worker():
    """
    Hours per worker by sector including the option of the Model Explorer. The variation is limited by a maximum number of hours to avoid unrealistic settings.
    """
    return if_then_else(
        time() < initial_year_working_time_variation_sp(),
        lambda: initial_hours_per_worker(),
        lambda: if_then_else(
            switch_model_explorer() == 1,
            lambda: model_explorer_working_time_variation(),
            lambda: stock_hours_per_worker(),
        ),
    )


@component.add(
    name="hours worked",
    units="Mhours/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_labour": 1,
        "base_output_real": 1,
        "labour_productivity": 2,
        "output_real": 1,
    },
)
def hours_worked():
    """
    Hours worked.
    """
    return if_then_else(
        switch_eco_labour() == 0,
        lambda: zidz(base_output_real(), labour_productivity()),
        lambda: zidz(output_real(), labour_productivity()),
    )


@component.add(
    name="INITIAL DELAYED 2 CONSUMER PRICE INDEX",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_delayed_2_consumer_price_index"},
)
def initial_delayed_2_consumer_price_index():
    """
    Delayed consumer price index, 2 periods
    """
    return _ext_constant_initial_delayed_2_consumer_price_index()


_ext_constant_initial_delayed_2_consumer_price_index = ExtConstant(
    "model_parameters/economy/Primary_Inputs.xlsx",
    "Consumer_Price_Index_t2",
    "INITIAL_DELAYED_2_CONSUMER_PRICE_INDEX",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_delayed_2_consumer_price_index",
)


@component.add(
    name="INITIAL LIMIT ANNUAL GROWTH WAGES SP",
    units="Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_limit_annual_growth_wages_sp"},
)
def initial_limit_annual_growth_wages_sp():
    """
    Inital year limits anual growth wages
    """
    return _ext_constant_initial_limit_annual_growth_wages_sp()


_ext_constant_initial_limit_annual_growth_wages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_LIMIT_ANNUAL_GROWTH_WAGES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_initial_limit_annual_growth_wages_sp",
)


@component.add(
    name="INITIAL YEAR LABOUR PRODUCTIVITY VARIATION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_year_labour_productivity_variation_sp"
    },
)
def initial_year_labour_productivity_variation_sp():
    """
    Initial year labour productivity variation.
    """
    return _ext_constant_initial_year_labour_productivity_variation_sp()


_ext_constant_initial_year_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_LABOUR_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_labour_productivity_variation_sp",
)


@component.add(
    name="INITIAL YEAR WORKING TIME VARIATION SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_initial_year_working_time_variation_sp"},
)
def initial_year_working_time_variation_sp():
    return _ext_constant_initial_year_working_time_variation_sp()


_ext_constant_initial_year_working_time_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "INITIAL_YEAR_WORKING_TIME_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_initial_year_working_time_variation_sp",
)


@component.add(
    name="labour compensation",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "hours_worked": 1,
        "unit_conversion_hours_mhours": 1,
        "wage_hour": 1,
        "unit_conversion_dollars_mdollars": 1,
    },
)
def labour_compensation():
    """
    Labour compensation in nominal terms.
    """
    return (hours_worked() * unit_conversion_hours_mhours()) * (
        wage_hour() / unit_conversion_dollars_mdollars()
    )


@component.add(
    name="labour compensation total",
    units="Mdollars/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_compensation": 1},
)
def labour_compensation_total():
    """
    Total labour compensation
    """
    return sum(
        labour_compensation().rename({"SECTORS I": "SECTORS I!"}), dim=["SECTORS I!"]
    )


@component.add(
    name="labour force",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Stateful",
    comp_subtype="Smooth",
    depends_on={
        "time": 1,
        "switch_eco_participation_rate": 1,
        "working_age_population": 1,
        "initial_participation_rate": 1,
        "_smooth_labour_force": 1,
    },
    other_deps={
        "_smooth_labour_force": {
            "initial": {"participation_rate": 1, "working_age_population": 1},
            "step": {"participation_rate": 1, "working_age_population": 1},
        }
    },
)
def labour_force():
    """
    Labour force.
    """
    return if_then_else(
        np.logical_or(time() <= 2015, switch_eco_participation_rate() == 0),
        lambda: initial_participation_rate() * working_age_population(),
        lambda: _smooth_labour_force(),
    )


_smooth_labour_force = Smooth(
    lambda: participation_rate() * working_age_population(),
    lambda: xr.DataArray(
        8, {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, ["REGIONS 35 I"]
    ),
    lambda: participation_rate() * working_age_population(),
    lambda: 1,
    "_smooth_labour_force",
)


@component.add(
    name="labour productivity",
    units="Mdollars 2015/Mhours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_labour_productivity": 1},
    other_deps={
        "_integ_labour_productivity": {
            "initial": {"initial_labour_productivity": 1},
            "step": {
                "labour_productivity_variation": 1,
                "climate_change_impact_in_labour_productivity": 1,
            },
        }
    },
)
def labour_productivity():
    """
    Labour productivity
    """
    return _integ_labour_productivity()


_integ_labour_productivity = Integ(
    lambda: labour_productivity_variation()
    - climate_change_impact_in_labour_productivity(),
    lambda: initial_labour_productivity(),
    "_integ_labour_productivity",
)


@component.add(
    name="labour productivity variation",
    units="Mdollars 2015/(Mhours*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "round_annual_growth_labour_productivity": 1,
        "annual_labour_productivity": 1,
    },
)
def labour_productivity_variation():
    """
    Variation labour productivity
    """
    return round_annual_growth_labour_productivity() * annual_labour_productivity()


@component.add(
    name="LABOUR PRODUCTIVITY VARIATION DEFAULT",
    units="1/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_labour_productivity_variation_default",
        "__data__": "_ext_data_labour_productivity_variation_default",
        "time": 1,
    },
)
def labour_productivity_variation_default():
    """
    Default scenario for labour productivity variation
    """
    return _ext_data_labour_productivity_variation_default(time())


_ext_data_labour_productivity_variation_default = ExtData(
    "model_parameters/economy/Primary_Inputs.xlsx",
    "EXO_Lab_productivity_growth_def",
    "TIME_LAB_PROD",
    "LABOUR_PRODUCTIVITY_VARIATION_DEFAULT",
    None,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_data_labour_productivity_variation_default",
)


@component.add(
    name="LABOUR PRODUCTIVITY VARIATION SP",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_labour_productivity_variation_sp"},
)
def labour_productivity_variation_sp():
    """
    Labour productivity variation scenario
    """
    return _ext_constant_labour_productivity_variation_sp()


_ext_constant_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LABOUR_PRODUCTIVITY_VARIATION_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_labour_productivity_variation_sp",
)


@component.add(
    name="LIMIT LOWER BOUND ANNUAL GROWTH WAGES SP",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limit_lower_bound_annual_growth_wages_sp"
    },
)
def limit_lower_bound_annual_growth_wages_sp():
    """
    Lower bound limit to annual growth of wages
    """
    return _ext_constant_limit_lower_bound_annual_growth_wages_sp()


_ext_constant_limit_lower_bound_annual_growth_wages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LIMIT_LOWER_BOUND_ANNUAL_GROWTH_WAGES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_limit_lower_bound_annual_growth_wages_sp",
)


@component.add(
    name="LIMIT UPPER BOUND ANNUAL GROWTH WAGES SP",
    units="DMNL/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_limit_upper_bound_annual_growth_wages_sp"
    },
)
def limit_upper_bound_annual_growth_wages_sp():
    """
    Upper bound limit to annual growth of wages
    """
    return _ext_constant_limit_upper_bound_annual_growth_wages_sp()


_ext_constant_limit_upper_bound_annual_growth_wages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "LIMIT_UPPER_BOUND_ANNUAL_GROWTH_WAGES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_limit_upper_bound_annual_growth_wages_sp",
)


@component.add(
    name="participation rate",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "constant_participation_rate": 1,
        "beta_participation_rate": 1,
        "delayed_ts_unemployment_rate": 1,
        "delayed_ts_consumer_price_index": 1,
        "delayed_ts_wage_hour_total": 1,
        "epsilon_participation_rate": 1,
        "price_transformation": 1,
    },
)
def participation_rate():
    """
    Particpation rate: share of active population in the labour market (i.e., labour force divided by working-age population)
    """
    return np.exp(
        constant_participation_rate()
        + beta_participation_rate() * np.log(1 - delayed_ts_unemployment_rate())
        + epsilon_participation_rate()
        * np.log(
            zidz(
                delayed_ts_wage_hour_total(),
                delayed_ts_consumer_price_index() / price_transformation(),
            )
        )
    )


@component.add(
    name="round annual growth labour productivity",
    units="1/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"annual_growth_labour_productivity": 1},
)
def round_annual_growth_labour_productivity():
    """
    Annual growth labour productivity rounded
    """
    return integer(annual_growth_labour_productivity() * 1000) / 1000


@component.add(
    name="SELECT LABOUR PRODUCTIVITY VARIATION SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_labour_productivity_variation_sp"
    },
)
def select_labour_productivity_variation_sp():
    """
    Switch year labour productivity variation. 0: Default 1: Scenario
    """
    return _ext_constant_select_labour_productivity_variation_sp()


_ext_constant_select_labour_productivity_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_LABOUR_PRODUCTIVITY_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_labour_productivity_variation_sp",
)


@component.add(
    name="SELECT LIMIT ANNUAL GROWTH WAGES SP",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_limit_annual_growth_wages_sp"},
)
def select_limit_annual_growth_wages_sp():
    """
    Select limits annual growth wages: 0: No limit 1: Limit
    """
    return _ext_constant_select_limit_annual_growth_wages_sp()


_ext_constant_select_limit_annual_growth_wages_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_LIMIT_ANNUAL_GROWTH_WAGES_SP*",
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    _root,
    {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]},
    "_ext_constant_select_limit_annual_growth_wages_sp",
)


@component.add(
    name="SELECT WORKING TIME VARIATION SP",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_working_time_variation_sp"},
)
def select_working_time_variation_sp():
    """
    0: Default: No working time variation 1: User defined
    """
    return _ext_constant_select_working_time_variation_sp()


_ext_constant_select_working_time_variation_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_WORKING_TIME_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_working_time_variation_sp",
)


@component.add(
    name="stock hours per worker",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_stock_hours_per_worker": 1},
    other_deps={
        "_integ_stock_hours_per_worker": {
            "initial": {"initial_hours_per_worker": 1},
            "step": {"annual_variation_hours_per_worker": 1},
        }
    },
)
def stock_hours_per_worker():
    """
    Hours per worker by sector.
    """
    return _integ_stock_hours_per_worker()


_integ_stock_hours_per_worker = Integ(
    lambda: annual_variation_hours_per_worker(),
    lambda: initial_hours_per_worker(),
    "_integ_stock_hours_per_worker",
)


@component.add(
    name="SWITCH DEM2ECO WORKING AGE POPULATION",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_dem2eco_working_age_population"},
)
def switch_dem2eco_working_age_population():
    """
    Intermodule links SWITCH, it can take two values: 0: the link is broken, the intermodule variable is replaced by an exogenous parameter. 1: the link between modules is operational.
    """
    return _ext_constant_switch_dem2eco_working_age_population()


_ext_constant_switch_dem2eco_working_age_population = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_DEM2ECO_WORKING_AGE_POPULATION",
    {},
    _root,
    {},
    "_ext_constant_switch_dem2eco_working_age_population",
)


@component.add(
    name="SWITCH ECO LABOUR",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_labour"},
)
def switch_eco_labour():
    """
    This switch can take two values: 0: the (sub)module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the (sub)module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_eco_labour()


_ext_constant_switch_eco_labour = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_LABOUR",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_labour",
)


@component.add(
    name="SWITCH ECO PARTICIPATION RATE",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco_participation_rate"},
)
def switch_eco_participation_rate():
    """
    1: dynamic endogenous participation rate 0: exogenous participation rate
    """
    return _ext_constant_switch_eco_participation_rate()


_ext_constant_switch_eco_participation_rate = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO_PARTICIPATION_RATE",
    {},
    _root,
    {},
    "_ext_constant_switch_eco_participation_rate",
)


@component.add(
    name="SWITCH ECONOMY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_economy"},
)
def switch_economy():
    """
    This switch can take two values: 0: the module runs isolated from the rest of WILIAM, replacing inter(sub)module variables with exogenous parameters. 1: the module runs integrated with the rest of WILIAM.
    """
    return _ext_constant_switch_economy()


_ext_constant_switch_economy = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECONOMY",
    {},
    _root,
    {},
    "_ext_constant_switch_economy",
)


@component.add(
    name="unemployment rate",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"employment_total": 1, "labour_force": 1},
)
def unemployment_rate():
    """
    Unemployment rate.
    """
    return np.maximum(1 - zidz(employment_total(), labour_force()), 0)


@component.add(
    name="unemployment total",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"labour_force": 1, "employment_total": 1},
)
def unemployment_total():
    """
    Total unemployment.
    """
    return labour_force() - employment_total()


@component.add(
    name="wage hour",
    units="dollars/Hours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wage_hour_stock": 1},
)
def wage_hour():
    """
    Wage per hour corrected for downward rigidity IF_THEN_ELSE(wage_hour_stock[REGIONS_35_I,SECTORS_I]>delayed_wage_hour[REGIONS_35_I,S ECTORS_I],wage_hour_stock[REGIONS_35_I ,SECTORS_I],delayed_wage_hour[REGIONS_35_I,SECTORS_I])
    """
    return wage_hour_stock()


@component.add(
    name="wage hour stock",
    units="dollars/Hours",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_wage_hour_stock": 1},
    other_deps={
        "_integ_wage_hour_stock": {
            "initial": {"initial_wage_hour": 1},
            "step": {"time": 1, "wage_hour_variation": 1},
        }
    },
)
def wage_hour_stock():
    return _integ_wage_hour_stock()


_integ_wage_hour_stock = Integ(
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
        lambda: wage_hour_variation(),
    ),
    lambda: initial_wage_hour(),
    "_integ_wage_hour_stock",
)


@component.add(
    name="wage hour variation",
    units="dollars/(Hours*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"wage_hour_stock": 1, "annual_wage_hour_variation": 1},
)
def wage_hour_variation():
    """
    Wage hour variation.
    """
    return wage_hour_stock() * annual_wage_hour_variation()


@component.add(
    name="working age population",
    units="kpeople",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "switch_economy": 1,
        "switch_eco_labour": 1,
        "switch_dem2eco_working_age_population": 1,
        "base_working_age_population": 1,
        "unit_conversion_kpeople_people": 1,
        "total_population_over_15": 1,
    },
)
def working_age_population():
    """
    Working age population defined as 15 years old and older.
    """
    return if_then_else(
        np.logical_or(
            time() <= 2015,
            np.logical_or(
                switch_economy() == 0,
                np.logical_or(
                    switch_eco_labour() == 0,
                    switch_dem2eco_working_age_population() == 0,
                ),
            ),
        ),
        lambda: base_working_age_population(),
        lambda: total_population_over_15() * unit_conversion_kpeople_people(),
    )


@component.add(
    name="WORKING TIME TARGET",
    units="Mhours/(kpeople*Year)",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_working_time_variation_sp": 1,
        "initial_hours_per_worker": 2,
        "working_time_variation_target_sp": 1,
    },
)
def working_time_target():
    """
    Target policy to vary working time with relation to 2015 values.
    """
    return if_then_else(
        select_working_time_variation_sp() == 0,
        lambda: initial_hours_per_worker(),
        lambda: initial_hours_per_worker() * (1 + working_time_variation_target_sp()),
    )


@component.add(
    name="WORKING TIME VARIATION TARGET SP",
    units="1",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_working_time_variation_target_sp"},
)
def working_time_variation_target_sp():
    """
    Cumulative variation in working time by region and sector with relation to the 2015 values between final and initial year (write always positive number, =1 corresponds to historic value, values higher than 1 correspond to increases (eg., 2 means double hours worked), and lower than 1 reductions (eg 0.5 means half hours worked and 0<=> nul working time). After the final year, the number of worked hours remains constant
    """
    return _ext_constant_working_time_variation_target_sp()


_ext_constant_working_time_variation_target_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "WORKING_TIME_VARIATION_TARGET_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "SECTORS I": _subscript_dict["SECTORS I"],
    },
    "_ext_constant_working_time_variation_target_sp",
)
