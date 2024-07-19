"""
Module land_and_watervalidation
Translated using PySD version 3.13.4
"""

@component.add(
    name="EXO SHARE AREA RICE CROPLAND",
    units="km2",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_area_rice_cropland",
        "__lookup__": "_ext_lookup_exo_share_area_rice_cropland",
    },
)
def exo_share_area_rice_cropland(x, final_subs=None):
    """
    Exogenous data from simulation de share area rice cropland
    """
    return _ext_lookup_exo_share_area_rice_cropland(x, final_subs)


_ext_lookup_exo_share_area_rice_cropland = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_SHARE_AREA_RICE_CROPLAND",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_area_rice_cropland",
)


@component.add(
    name="EXO SHARE OF AGRICULTURE IN TRANSITION",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_agriculture_in_transition",
        "__lookup__": "_ext_lookup_exo_share_of_agriculture_in_transition",
    },
)
def exo_share_of_agriculture_in_transition(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_agriculture_in_transition(x, final_subs)


_ext_lookup_exo_share_of_agriculture_in_transition = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_agriculture_in_transition",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_of_agriculture_in_transition",
)


@component.add(
    name="EXO SHARE OF INDUSTRIAL AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_industrial_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_industrial_agriculture",
    },
)
def exo_share_of_industrial_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_industrial_agriculture(x, final_subs)


_ext_lookup_exo_share_of_industrial_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_industrial_agriculture",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_of_industrial_agriculture",
)


@component.add(
    name="EXO SHARE OF LOW INPUT AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_low_input_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_low_input_agriculture",
    },
)
def exo_share_of_low_input_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_low_input_agriculture(x, final_subs)


_ext_lookup_exo_share_of_low_input_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_low_input_agriculture",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_of_low_input_agriculture",
)


@component.add(
    name="EXO SHARE OF REGENERATIVE AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_regenerative_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_regenerative_agriculture",
    },
)
def exo_share_of_regenerative_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_regenerative_agriculture(x, final_subs)


_ext_lookup_exo_share_of_regenerative_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_regenerative_agriculture",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_of_regenerative_agriculture",
)


@component.add(
    name="EXO SHARE OF TRADITIONAL AGRICULTURE",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_exo_share_of_traditional_agriculture",
        "__lookup__": "_ext_lookup_exo_share_of_traditional_agriculture",
    },
)
def exo_share_of_traditional_agriculture(x, final_subs=None):
    """
    exogenous data from simulation
    """
    return _ext_lookup_exo_share_of_traditional_agriculture(x, final_subs)


_ext_lookup_exo_share_of_traditional_agriculture = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Emissions",
    "TIME_EXO_SIMULATION",
    "EXO_share_of_traditional_agriculture",
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    _root,
    {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]},
    "_ext_lookup_exo_share_of_traditional_agriculture",
)
