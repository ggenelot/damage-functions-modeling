"""
Module energyeroi.dynamic_eroi_system
Translated using PySD version 3.14.0
"""

@component.add(
    name="aux EROI system until 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_aux_eroi_system_until_2015": 1},
    other_deps={
        "_delayfixed_aux_eroi_system_until_2015": {
            "initial": {"time_step": 1},
            "step": {"eroi_system_until_2015": 1},
        }
    },
)
def aux_eroi_system_until_2015():
    """
    Auxiliary variable to estimate the EROIst of the system in the year 2015. The method is not mathematically exact, but the error tends to 0 when the TIME STEP decreases.
    """
    return _delayfixed_aux_eroi_system_until_2015()


_delayfixed_aux_eroi_system_until_2015 = DelayFixed(
    lambda: eroi_system_until_2015(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_aux_eroi_system_until_2015",
)


@component.add(
    name="delayed EROI system",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_eroi_system": 1},
    other_deps={
        "_delayfixed_delayed_eroi_system": {"initial": {}, "step": {"eroi_system": 1}}
    },
)
def delayed_eroi_system():
    """
    EROIst of the system delayed 1 year.
    """
    return _delayfixed_delayed_eroi_system()


_delayfixed_delayed_eroi_system = DelayFixed(
    lambda: eroi_system(),
    lambda: 1,
    lambda: xr.DataArray(
        0, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
    ),
    time_step,
    "_delayfixed_delayed_eroi_system",
)


@component.add(
    name="EROI FC system from 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "eroi_system_until_2015": 2, "delayed_eroi_system": 2},
)
def eroi_fc_system_from_2015():
    """
    EROI of the system feedback from the year 2015: variation in final energy demand to compensate the variation in the EROI in relation to the base year 2015.
    """
    return if_then_else(
        time() < 2016,
        lambda: xr.DataArray(
            1, {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, ["REGIONS 9 I"]
        ),
        lambda: (delayed_eroi_system() / (delayed_eroi_system() - 1))
        * ((eroi_system_until_2015() - 1) / eroi_system_until_2015()),
    )


@component.add(
    name="EROI system",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"eroist_system": 1},
)
def eroi_system():
    """
    EROI of the system.
    """
    return eroist_system()


@component.add(
    name="EROI system until 2015",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "aux_eroi_system_until_2015": 1, "eroi_system": 1},
)
def eroi_system_until_2015():
    """
    EROIst of the energy system until the year 2015.
    """
    return if_then_else(
        time() > 2015, lambda: aux_eroi_system_until_2015(), lambda: eroi_system()
    )


@component.add(
    name="EROIst system",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1, "fenust_system": 1},
)
def eroist_system():
    """
    EROI standard of the system.
    """
    return np.maximum(0, total_fe_energy_uses() / fenust_system())


@component.add(
    name="FEnUst system",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "prosup_sector_energy_own_consumption_per_commodity": 1,
        "total_dynfenust_energy_transformation": 1,
    },
)
def fenust_system():
    """
    Energy used (in final terms) of the full system at EROI standard level.
    """
    return (
        sum(
            prosup_sector_energy_own_consumption_per_commodity().rename(
                {"NRG TO I": "NRG TO I!"}
            ),
            dim=["NRG TO I!"],
        )
        + total_dynfenust_energy_transformation()
    )


@component.add(
    name="global EROIst system",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_fe_energy_uses": 1, "fenust_system": 1},
)
def global_eroist_system():
    """
    EROIst of the whole world.
    """
    return np.maximum(
        0,
        sum(
            total_fe_energy_uses().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        / sum(
            fenust_system().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        ),
    )


@component.add(
    name="share dynFEnUst energy transformation vs total FE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_dynfenust_energy_transformation": 1, "total_fe_energy_uses": 1},
)
def share_dynfenust_energy_transformation_vs_total_fe():
    """
    Share of dynamic final energy investments for RES technologies vs total FE.
    """
    return zidz(total_dynfenust_energy_transformation(), total_fe_energy_uses())


@component.add(
    name="SWITCH NRG EROI FEEDBACK",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_nrg_eroi_feedback"},
)
def switch_nrg_eroi_feedback():
    """
    switch: 0 to deactivate EROI feedback, 1 to activate feedback to energy demand.
    """
    return _ext_constant_switch_nrg_eroi_feedback()


_ext_constant_switch_nrg_eroi_feedback = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG_EROI_FEEDBACK",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg_eroi_feedback",
)


@component.add(
    name="Total dynFEnUst energy transformation",
    units="EJ/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_dynfenu_protra": 1,
        "total_fenust_protra_eroi_exogenous": 1,
        "fenust_prosto_elec_dedicated": 1,
    },
)
def total_dynfenust_energy_transformation():
    """
    Total (dynamic) final energy investment for RES and storage.
    """
    return (
        total_dynfenu_protra()
        + 0
        + total_fenust_protra_eroi_exogenous()
        + sum(
            fenust_prosto_elec_dedicated().rename(
                {"PROSTO ELEC DEDICATED I": "PROSTO ELEC DEDICATED I!"}
            ),
            dim=["PROSTO ELEC DEDICATED I!"],
        )
    )
