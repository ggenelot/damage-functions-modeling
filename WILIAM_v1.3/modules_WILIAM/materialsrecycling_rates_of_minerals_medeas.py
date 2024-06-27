"""
Module materialsrecycling_rates_of_minerals_medeas
Translated using PySD version 3.14.0
"""

@component.add(
    name="a lineal regr rr alt techn",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_alternative_technologies_sp_w": 1,
        "current_recycling_rates_minerals_alt_techn": 1,
        "target_year_p_rr_minerals_alt_techn_w": 1,
        "start_year_p_rr_minerals_alt_techn_w": 1,
    },
)
def a_lineal_regr_rr_alt_techn():
    """
    a parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr alt technology").
    """
    return (
        target_rr_alternative_technologies_sp_w()
        - current_recycling_rates_minerals_alt_techn()
    ) / (
        target_year_p_rr_minerals_alt_techn_w() - start_year_p_rr_minerals_alt_techn_w()
    )


@component.add(
    name="a lineal regr rr Rest",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_rest_sp_w": 1,
        "current_eol_rr_minerals": 1,
        "target_year_p_rr_minerals_rest_w": 1,
        "start_year_p_rr_minerals_rest_w": 1,
    },
)
def a_lineal_regr_rr_rest():
    """
    a parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr Rest").
    """
    return (target_rr_rest_sp_w() - current_eol_rr_minerals()) / (
        target_year_p_rr_minerals_rest_w() - start_year_p_rr_minerals_rest_w()
    )


@component.add(
    name="b lineal regr rr alt techn",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_alternative_technologies_sp_w": 1,
        "target_year_p_rr_minerals_alt_techn_w": 1,
        "a_lineal_regr_rr_alt_techn": 1,
    },
)
def b_lineal_regr_rr_alt_techn():
    """
    b parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr alt technology").
    """
    return (
        target_rr_alternative_technologies_sp_w()
        - a_lineal_regr_rr_alt_techn() * target_year_p_rr_minerals_alt_techn_w()
    )


@component.add(
    name="b lineal regr rr Rest",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "target_rr_rest_sp_w": 1,
        "a_lineal_regr_rr_rest": 1,
        "target_year_p_rr_minerals_rest_w": 1,
    },
)
def b_lineal_regr_rr_rest():
    """
    b parameter of lineal regression "y=a*TIME+b" where y corresponds to the evolution of the recycling rate of each mineral over time ("by mineral rr Rest").
    """
    return (
        target_rr_rest_sp_w()
        - a_lineal_regr_rr_rest() * target_year_p_rr_minerals_rest_w()
    )


@component.add(
    name="by mineral rr alt techn",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "a_lineal_regr_rr_alt_techn": 1,
        "time": 1,
        "b_lineal_regr_rr_alt_techn": 1,
    },
)
def by_mineral_rr_alt_techn():
    """
    Recycling rates over time by mineral for alternative technologies (RES elec & EV batteries).
    """
    return a_lineal_regr_rr_alt_techn() * time() + b_lineal_regr_rr_alt_techn()


@component.add(
    name="by mineral rr alt techn 1yr",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_by_mineral_rr_alt_techn_1yr": 1},
    other_deps={
        "_delayfixed_by_mineral_rr_alt_techn_1yr": {
            "initial": {"current_recycling_rates_minerals_alt_techn": 1},
            "step": {"by_mineral_rr_alt_techn": 1},
        }
    },
)
def by_mineral_rr_alt_techn_1yr():
    """
    Recycling rates over time delayed 1 year by mineral for alternative technologies (RES elec & EV batteries).
    """
    return _delayfixed_by_mineral_rr_alt_techn_1yr()


_delayfixed_by_mineral_rr_alt_techn_1yr = DelayFixed(
    lambda: by_mineral_rr_alt_techn(),
    lambda: 1,
    lambda: current_recycling_rates_minerals_alt_techn(),
    time_step,
    "_delayfixed_by_mineral_rr_alt_techn_1yr",
)


@component.add(
    name="by mineral rr Rest",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"a_lineal_regr_rr_rest": 1, "time": 1, "b_lineal_regr_rr_rest": 1},
)
def by_mineral_rr_rest():
    """
    Recycling rates over time by mineral for the rest of the economy.
    """
    return a_lineal_regr_rr_rest() * time() + b_lineal_regr_rr_rest()


@component.add(
    name="by mineral rr Rest 1yr",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_by_mineral_rr_rest_1yr": 1},
    other_deps={
        "_delayfixed_by_mineral_rr_rest_1yr": {
            "initial": {"current_recycling_rates_minerals_alt_techn": 1},
            "step": {"by_mineral_rr_rest": 1},
        }
    },
)
def by_mineral_rr_rest_1yr():
    """
    Recycling rates over time delayed 1 year by mineral for the rest of the economy.
    """
    return _delayfixed_by_mineral_rr_rest_1yr()


_delayfixed_by_mineral_rr_rest_1yr = DelayFixed(
    lambda: by_mineral_rr_rest(),
    lambda: 1,
    lambda: current_recycling_rates_minerals_alt_techn(),
    time_step,
    "_delayfixed_by_mineral_rr_rest_1yr",
)


@component.add(
    name="by mineral rr variation alt techn",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historic_improvement_recycling_rates_minerals": 2,
        "by_mineral_rr_alt_techn_1yr": 1,
        "start_year_p_rr_minerals_alt_techn_w": 1,
        "by_mineral_rr_alt_techn": 1,
    },
)
def by_mineral_rr_variation_alt_techn():
    """
    Variation of recycling rates per mineral for alternative technologies (RES elec & EV batteries).
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {"MATERIALS I": _subscript_dict["MATERIALS I"]},
            ["MATERIALS I"],
        ),
        lambda: if_then_else(
            time() < start_year_p_rr_minerals_alt_techn_w(),
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {"MATERIALS I": _subscript_dict["MATERIALS I"]},
                ["MATERIALS I"],
            ),
            lambda: by_mineral_rr_alt_techn() - by_mineral_rr_alt_techn_1yr(),
        ),
    )


@component.add(
    name="by mineral rr variation Rest",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historic_improvement_recycling_rates_minerals": 2,
        "by_mineral_rr_rest_1yr": 1,
        "by_mineral_rr_rest": 1,
        "start_year_p_rr_minerals_rest_w": 1,
    },
)
def by_mineral_rr_variation_rest():
    """
    Variation of recycling rates per mineral for the rest of the economy.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            historic_improvement_recycling_rates_minerals(),
            {"MATERIALS I": _subscript_dict["MATERIALS I"]},
            ["MATERIALS I"],
        ),
        lambda: if_then_else(
            time() < start_year_p_rr_minerals_rest_w(),
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {"MATERIALS I": _subscript_dict["MATERIALS I"]},
                ["MATERIALS I"],
            ),
            lambda: by_mineral_rr_rest() - by_mineral_rr_rest_1yr(),
        ),
    )


@component.add(
    name="common rr minerals variation alt techn",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "start_year_p_common_rr_minerals_alt_techn_w": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "policy_common_rr_minerals_variation_alt_techn_sp_w": 1,
    },
)
def common_rr_minerals_variation_alt_techn():
    """
    Recycling rates of minererals (common annual variation).
    """
    return xr.DataArray(
        if_then_else(
            time() < start_year_p_common_rr_minerals_alt_techn_w(),
            lambda: historic_improvement_recycling_rates_minerals(),
            lambda: policy_common_rr_minerals_variation_alt_techn_sp_w(),
        ),
        {"MATERIALS I": _subscript_dict["MATERIALS I"]},
        ["MATERIALS I"],
    )


@component.add(
    name="common rr minerals variation Rest",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "start_year_p_common_rr_minerals_rest_w": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "policy_common_rr_minerals_variation_rest_sp_w": 1,
    },
)
def common_rr_minerals_variation_rest():
    """
    Recycling rates of minererals (common annual variation).
    """
    return xr.DataArray(
        if_then_else(
            time() < start_year_p_common_rr_minerals_rest_w(),
            lambda: historic_improvement_recycling_rates_minerals(),
            lambda: policy_common_rr_minerals_variation_rest_sp_w(),
        ),
        {"MATERIALS I": _subscript_dict["MATERIALS I"]},
        ["MATERIALS I"],
    )


@component.add(
    name="constrain rr improv for alt techn per mineral",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eol_recycling_rates_minerals_bu_techs": 1,
        "maximum_recycling_rates_minerals": 1,
    },
)
def constrain_rr_improv_for_alt_techn_per_mineral():
    """
    Constraint recycling rate improvement for alternative technologies (RES elec & EV batteries) per material.
    """
    return if_then_else(
        eol_recycling_rates_minerals_bu_techs() < maximum_recycling_rates_minerals(),
        lambda: xr.DataArray(
            1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="constrain rr improv for Rest per mineral",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "eol_recycling_rates_minerals_roe": 1,
        "maximum_recycling_rates_minerals": 1,
    },
)
def constrain_rr_improv_for_rest_per_mineral():
    """
    Remaining recycling rate improvement for the rest of the economy per material.
    """
    return if_then_else(
        eol_recycling_rates_minerals_roe() < maximum_recycling_rates_minerals(),
        lambda: xr.DataArray(
            1, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
        lambda: xr.DataArray(
            0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
        ),
    )


@component.add(
    name="CURRENT RECYCLING RATES MINERALS ALT TECHN",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "current_eol_rr_minerals": 1,
        "rr_minerals_alt_techn_res_vs_total_economy": 1,
    },
)
def current_recycling_rates_minerals_alt_techn():
    """
    Current recycling rates of minerales for alternative technologies. Since these technologies are novel and often include materials which are used in small quantities in complex products, the recycling rates of the used minerals are lower than for the whole economy (following the parameter "EOL-RR minerals alt techn RES vs. total economy").
    """
    return current_eol_rr_minerals() * rr_minerals_alt_techn_res_vs_total_economy()


@component.add(
    name="EOL recycling rates minerals BU techs",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eol_recycling_rates_minerals_bu_techs": 1},
    other_deps={
        "_integ_eol_recycling_rates_minerals_bu_techs": {
            "initial": {"current_recycling_rates_minerals_alt_techn": 1},
            "step": {"improvement_recycling_rates_minerals_alt_techn": 1},
        }
    },
)
def eol_recycling_rates_minerals_bu_techs():
    """
    Recycling rates minerals of alternative technologies (RES elec & EV batteries).
    """
    return _integ_eol_recycling_rates_minerals_bu_techs()


_integ_eol_recycling_rates_minerals_bu_techs = Integ(
    lambda: improvement_recycling_rates_minerals_alt_techn(),
    lambda: current_recycling_rates_minerals_alt_techn(),
    "_integ_eol_recycling_rates_minerals_bu_techs",
)


@component.add(
    name="EOL recycling rates minerals RoE",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_eol_recycling_rates_minerals_roe": 1},
    other_deps={
        "_integ_eol_recycling_rates_minerals_roe": {
            "initial": {"current_eol_rr_minerals": 1},
            "step": {"improvement_recycling_rates_minerals_rest": 1},
        }
    },
)
def eol_recycling_rates_minerals_roe():
    """
    Recycling rates minerals for the rest of the economy.
    """
    return _integ_eol_recycling_rates_minerals_roe()


_integ_eol_recycling_rates_minerals_roe = Integ(
    lambda: improvement_recycling_rates_minerals_rest(),
    lambda: current_eol_rr_minerals(),
    "_integ_eol_recycling_rates_minerals_roe",
)


@component.add(
    name="improvement recycling rates minerals alt techn",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "switch_nrg_dynamic_eroist": 1,
        "common_rr_minerals_variation_alt_techn": 1,
        "eol_recycling_rates_minerals_bu_techs": 1,
        "select_mineral_rr_targets_sp_w": 1,
        "by_mineral_rr_variation_alt_techn": 1,
        "constrain_rr_improv_for_alt_techn_per_mineral": 1,
    },
)
def improvement_recycling_rates_minerals_alt_techn():
    """
    Annual improvement of the recycling rates of minerals for alternative technologies (RES elec & EV batteries).
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {"MATERIALS I": _subscript_dict["MATERIALS I"]},
                ["MATERIALS I"],
            ),
            lambda: if_then_else(
                switch_nrg_dynamic_eroist() == 1,
                lambda: xr.DataArray(
                    0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
                ),
                lambda: if_then_else(
                    select_mineral_rr_targets_sp_w() == 2,
                    lambda: common_rr_minerals_variation_alt_techn()
                    * eol_recycling_rates_minerals_bu_techs(),
                    lambda: by_mineral_rr_variation_alt_techn(),
                ),
            ),
        )
        * constrain_rr_improv_for_alt_techn_per_mineral()
    )


@component.add(
    name="improvement recycling rates minerals Rest",
    units="DMNL",
    subscripts=["MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "historic_improvement_recycling_rates_minerals": 1,
        "select_mineral_rr_targets_sp_w": 1,
        "by_mineral_rr_variation_rest": 1,
        "common_rr_minerals_variation_rest": 1,
        "eol_recycling_rates_minerals_roe": 1,
        "constrain_rr_improv_for_rest_per_mineral": 1,
    },
)
def improvement_recycling_rates_minerals_rest():
    """
    Annual improvement of the recycling rates of minerals for the rest of the economy.
    """
    return (
        if_then_else(
            time() < 2015,
            lambda: xr.DataArray(
                historic_improvement_recycling_rates_minerals(),
                {"MATERIALS I": _subscript_dict["MATERIALS I"]},
                ["MATERIALS I"],
            ),
            lambda: if_then_else(
                select_mineral_rr_targets_sp_w() == 2,
                lambda: common_rr_minerals_variation_rest()
                * eol_recycling_rates_minerals_roe(),
                lambda: by_mineral_rr_variation_rest(),
            ),
        )
        * constrain_rr_improv_for_rest_per_mineral()
    )
