"""
Module climatetipping_points
Translated using PySD version 3.14.0
"""

@component.add(
    name="AMAZ tipping point in simulation period",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_time": 1,
        "random_uniform_function_amaz": 1,
        "cum_prob_amaz_tp_c1": 1,
    },
)
def amaz_tipping_point_in_simulation_period():
    """
    Warning: has MGIS tipping point being triggered during the simulation time?
    """
    return if_then_else(
        time() < final_time(),
        lambda: 0,
        lambda: if_then_else(
            random_uniform_function_amaz() > 1 - cum_prob_amaz_tp_c1(),
            lambda: 1,
            lambda: 0,
        ),
    )


@component.add(
    name="AMOC WEAKENING tipping point in simulation period",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_time": 1,
        "random_uniform_function_amoc_weakening": 1,
        "cum_prob_amoc_weakening_tp_c1": 1,
    },
)
def amoc_weakening_tipping_point_in_simulation_period():
    """
    Warning: has MGIS tipping point being triggered during the simulation time? IF_THEN_ELSE(Time<FINAL_TIME,0, IF_THEN_ELSE(RANDOM_UNIFORM_FUNCTION_AMOC_WEAKENING>1-CUM_PROB_AMOC_WEAKENI NG_TP_C1, 1, 0))
    """
    return if_then_else(
        time() < final_time(),
        lambda: 0,
        lambda: if_then_else(
            random_uniform_function_amoc_weakening() > cum_prob_amoc_weakening_tp_c1(),
            lambda: 1,
            lambda: 0,
        ),
    )


@component.add(
    name="CUM PROB AMAZ TP C1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "prob_amaz_tp_2010_2200_c1": 2,
        "final_time": 2,
        "temperature_change": 2,
    },
)
def cum_prob_amaz_tp_c1():
    """
    Adjustment of the cumulative probability to the analyzed period in the simulation.
    """
    return if_then_else(
        time() < 2100,
        lambda: prob_amaz_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - time()),
        lambda: prob_amaz_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - 2099),
    )


@component.add(
    name="CUM PROB AMOC WEAKENING TP C1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "final_time": 2,
        "temperature_change": 2,
        "prob_amoc_weakening_tp_2010_2100_c1": 2,
    },
)
def cum_prob_amoc_weakening_tp_c1():
    """
    Adjustment of the cumulative probability to the analyzed period in the simulation.
    """
    return if_then_else(
        time() < 2100,
        lambda: prob_amoc_weakening_tp_2010_2100_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - time()),
        lambda: prob_amoc_weakening_tp_2010_2100_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - 2099),
    )


@component.add(
    name="CUM PROB DAIS TP C1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "prob_dais_tp_2010_2200_c1": 2,
        "final_time": 2,
        "temperature_change": 2,
    },
)
def cum_prob_dais_tp_c1():
    """
    Adjustment of the cumulative probability to the analyzed period in the simulation.
    """
    return if_then_else(
        time() < 2100,
        lambda: prob_dais_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - time()),
        lambda: prob_dais_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - 2099),
    )


@component.add(
    name="CUM PROB MGIS TP C1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "prob_mgis_tp_2010_2200_c1": 2,
        "final_time": 2,
        "temperature_change": 2,
    },
)
def cum_prob_mgis_tp_c1():
    """
    Adjustment of the cumulative probability to the analyzed period in the simulation.
    """
    return if_then_else(
        time() < 2100,
        lambda: prob_mgis_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - time()),
        lambda: prob_mgis_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - 2099),
    )


@component.add(
    name="CUM PROB NINO TP C1",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "prob_nino_tp_2010_2200_c1": 2,
        "final_time": 2,
        "temperature_change": 2,
    },
)
def cum_prob_nino_tp_c1():
    """
    Adjustment of the cumulative probability to the analyzed period in the simulation.
    """
    return if_then_else(
        time() < 2100,
        lambda: prob_nino_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - time()),
        lambda: prob_nino_tp_2010_2200_c1()
        * temperature_change()
        * (final_time() - 2020)
        / (2100 - 2099),
    )


@component.add(
    name="DAIS tipping point in simulation period",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_time": 1,
        "cum_prob_dais_tp_c1": 1,
        "random_uniform_function_dais": 1,
    },
)
def dais_tipping_point_in_simulation_period():
    """
    Warning: has MGIS tipping point being triggered during the simulation time?
    """
    return if_then_else(
        time() < final_time(),
        lambda: 0,
        lambda: if_then_else(
            random_uniform_function_dais() > 1 - cum_prob_dais_tp_c1(),
            lambda: 1,
            lambda: 0,
        ),
    )


@component.add(
    name="MGIS tipping point in simulation period",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_time": 1,
        "cum_prob_mgis_tp_c1": 1,
        "random_uniform_function_mgis": 1,
    },
)
def mgis_tipping_point_in_simulation_period():
    """
    Warning: has MGIS tipping point being triggered during the simulation time?
    """
    return if_then_else(
        time() < final_time(),
        lambda: 0,
        lambda: if_then_else(
            random_uniform_function_mgis() > 1 - cum_prob_mgis_tp_c1(),
            lambda: 1,
            lambda: 0,
        ),
    )


@component.add(
    name="NINO tipping point in simulation period",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "final_time": 1,
        "random_uniform_function_nino": 1,
        "cum_prob_nino_tp_c1": 1,
    },
)
def nino_tipping_point_in_simulation_period():
    """
    Warning: has MGIS tipping point being triggered during the simulation time?
    """
    return if_then_else(
        time() < final_time(),
        lambda: 0,
        lambda: if_then_else(
            random_uniform_function_nino() > 1 - cum_prob_nino_tp_c1(),
            lambda: 1,
            lambda: 0,
        ),
    )


@component.add(
    name="NOISE SEED",
    units="DMNL",
    comp_type="Stateful",
    comp_subtype="Initial",
    depends_on={"_initial_noise_seed": 1},
    other_deps={"_initial_noise_seed": {"initial": {"time": 1}, "step": {}}},
)
def noise_seed():
    """
    Changing NOISE SEED will then generate alternative noise streams in different simulations.
    """
    return _initial_noise_seed()


_initial_noise_seed = Initial(
    lambda: get_time_value(__data["time"], 2, 0, 10), "_initial_noise_seed"
)


@component.add(
    name="RANDOM UNIFORM FUNCTION AMAZ",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"noise_seed": 1, "time": 1},
)
def random_uniform_function_amaz():
    """
    Generator of random number for AMAZ.
    """
    return np.random.uniform(0, 1, size=())


@component.add(
    name="RANDOM UNIFORM FUNCTION AMOC WEAKENING",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"noise_seed": 1, "time": 1},
)
def random_uniform_function_amoc_weakening():
    """
    Generator of random number for AMOC weakening. AMOC can be have a bimodal or bistable probability fuction: Sijp, W.P., Zika, J.D., d’Orgeville, M. et al. Revisiting meridional overturing bistability using a minimal set of state variables: stochastic theory. Clim Dyn 43, 1661-1676 (2014). https://doi.org/10.1007/s00382-013-1992-5. However, this bistability is valid for a time interval much larger than modelled in this program.
    """
    return np.random.uniform(0, 1, size=())


@component.add(
    name="RANDOM UNIFORM FUNCTION DAIS",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"noise_seed": 1, "time": 1},
)
def random_uniform_function_dais():
    """
    Generator of random number for DAIS.
    """
    return np.random.uniform(0, 1, size=())


@component.add(
    name="RANDOM UNIFORM FUNCTION MGIS",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"noise_seed": 1, "time": 1},
)
def random_uniform_function_mgis():
    """
    Generator of random number for MGIS.
    """
    return np.random.uniform(0, 1, size=())


@component.add(
    name="RANDOM UNIFORM FUNCTION NINO",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"noise_seed": 1, "time": 1},
)
def random_uniform_function_nino():
    """
    Generator of random number for NIÑO.
    """
    return np.random.uniform(0, 1, size=())


@component.add(
    name='"SWITCH: WILIAM: AMOC change"', comp_type="Constant", comp_subtype="Normal"
)
def switch_wiliam_amoc_change():
    return 0


@component.add(
    name="temperature change AMOC weakening",
    units="DegreesC",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_wiliam_amoc_change": 1,
        "amoc_weakening_tipping_point_in_simulation_period": 1,
        "time": 1,
        "values_temperature_amoc_change": 1,
    },
)
def temperature_change_amoc_weakening():
    """
    Temperature will change in some LOCOMOTION regions (in UE27, UK and USMCA), if tipping point is activated. Values source is Liu et al.,2020: Liu, W., Fedorov, A. V., Xie, S.-P. & Hu, S. Climate impacts of a weakened Atlantic meridional overturning circulation in a warming climate. Sci. Adv. 6, https://doi.org/10.1126/sciadv.aaz4876 (2020).
    """
    return if_then_else(
        switch_wiliam_amoc_change() == 0,
        lambda: xr.DataArray(
            0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: if_then_else(
            np.logical_and(
                amoc_weakening_tipping_point_in_simulation_period() == 1, time() > 2080
            ),
            lambda: values_temperature_amoc_change(),
            lambda: xr.DataArray(
                0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
            ),
        ),
    )


@component.add(
    name="values temperature AMOC change",
    subscripts=["REGIONS 9 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_values_temperature_amoc_change"},
)
def values_temperature_amoc_change():
    """
    Load values from the excel file. Values were based on: Liu, W., Fedorov, A. V., Xie, S.-P. & Hu, S. Climate impacts of a weakened Atlantic meridional overturning circulation in a warming climate. Sci. Adv. 6, https://doi.org/10.1126/sciadv.aaz4876 (2020).
    """
    return _ext_constant_values_temperature_amoc_change()


_ext_constant_values_temperature_amoc_change = ExtConstant(
    "model_parameters/climate/climate.xlsx",
    "World",
    "AMOC_tchanges",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_constant_values_temperature_amoc_change",
)
