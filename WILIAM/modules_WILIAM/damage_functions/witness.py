"""
Module damage_functions.witness
Translated using PySD version 3.13.4
"""

@component.add(
    name='"WITNESS: dice-like damage : EQ dice-like damage"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dice_5_damage_function_phi_1": 1,
        "temperature_change": 2,
        "dice_5_damage_function_phi2": 1,
        "witness_epsilon": 1,
    },
)
def witness_dicelike_damage_eq_dicelike_damage():
    return (
        dice_5_damage_function_phi_1() * temperature_change()
        + dice_5_damage_function_phi2() * temperature_change() ** witness_epsilon()
    )


@component.add(name='"WITNESS: epsilon"', comp_type="Constant", comp_subtype="Normal")
def witness_epsilon():
    return 2


@component.add(
    name='"WITNESS: omega"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"witness_tipping_point_damage_eq_tipping_point_damge": 2},
)
def witness_omega():
    return witness_tipping_point_damage_eq_tipping_point_damge() / (
        1 + witness_tipping_point_damage_eq_tipping_point_damge()
    )


@component.add(
    name='"WITNESS: tipping point damage: EQ tipping point damge"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"temperature_change": 2},
)
def witness_tipping_point_damage_eq_tipping_point_damge():
    return (temperature_change() / 20.46) ** 2 + (temperature_change() / 6.081) ** 6.754
