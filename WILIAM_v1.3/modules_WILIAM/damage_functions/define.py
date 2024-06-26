"""
Module damage_functions.define
Translated using PySD version 3.14.0
"""

@component.add(
    name='"DEFINE: 46: damage function"',
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "define_46_eta1": 1,
        "temperature_change": 3,
        "define_46_eta2": 1,
        "define_46_exponent": 1,
        "define_46_eta3": 1,
    },
)
def define_46_damage_function():
    return 1 - 1 / (
        1
        + define_46_eta1() * temperature_change()
        + define_46_eta2() * temperature_change() ** 2
        + define_46_eta3() * temperature_change() ** define_46_exponent()
    )


@component.add(name='"DEFINE: 46: eta1"', comp_type="Constant", comp_subtype="Normal")
def define_46_eta1():
    """
    Based on Dietz and Stern (2015); Dt = 50% when Tat=4°C
    """
    return 0


@component.add(name='"DEFINE: 46: eta2"', comp_type="Constant", comp_subtype="Normal")
def define_46_eta2():
    """
    Based on Dietz and Stern (2015); Dt = 50% when Tat=4°C
    """
    return 0.00284


@component.add(name='"DEFINE: 46: eta3"', comp_type="Constant", comp_subtype="Normal")
def define_46_eta3():
    """
    Based on Dietz and Stern (2015); Dt = 50% when Tat=4°C
    """
    return 8e-05


@component.add(
    name='"DEFINE: 46: exponent"', comp_type="Constant", comp_subtype="Normal"
)
def define_46_exponent():
    return 6.754
