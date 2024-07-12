"""
Module damage_functions.dice
Translated using PySD version 3.13.4
"""

@component.add(
    name='"DICE: 5: damage function phi2"', comp_type="Constant", comp_subtype="Normal"
)
def dice_5_damage_function_phi2():
    return 0.003467


@component.add(
    name='"DICE: 5: damage function phi 1"', comp_type="Constant", comp_subtype="Normal"
)
def dice_5_damage_function_phi_1():
    return 0


@component.add(
    name='"DICE: 5: EQ damage function"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dice_5_damage_function_phi_1": 1,
        "temperature_change": 2,
        "dice_5_damage_function_phi2": 1,
    },
)
def dice_5_eq_damage_function():
    return (
        dice_5_damage_function_phi_1() * temperature_change()
        + dice_5_damage_function_phi2() * temperature_change() ** 2
    )


@component.add(
    name='"DICE: 6: abatment theta 1"', comp_type="Constant", comp_subtype="Normal"
)
def dice_6_abatment_theta_1():
    return 0.109062


@component.add(
    name='"DICE: 6: abatment theta 2"', comp_type="Constant", comp_subtype="Normal"
)
def dice_6_abatment_theta_2():
    return 2.6


@component.add(
    name='"DICE: 6: Emissions control rate"',
    comp_type="Constant",
    comp_subtype="Normal",
)
def dice_6_emissions_control_rate():
    """
    TODO: checker cette valeur là
    """
    return 0


@component.add(
    name='"DICE: 6: EQ abatment function"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dice_6_abatment_theta_1": 1,
        "dice_6_abatment_theta_2": 1,
        "dice_6_emissions_control_rate": 1,
    },
)
def dice_6_eq_abatment_function():
    return (
        dice_6_abatment_theta_1()
        * dice_6_emissions_control_rate() ** dice_6_abatment_theta_2()
    )
