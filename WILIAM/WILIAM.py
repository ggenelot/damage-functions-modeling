"""
Python model 'WILIAM.py'
Translated using PySD
"""

from pathlib import Path
import numpy as np
import xarray as xr

from pysd.py_backend.functions import (
<<<<<<< HEAD
    active_initial,
    vector_sort_order,
    vector_select,
    vector_reorder,
    step,
    modulo,
    sum,
    invert_matrix,
    vmin,
    vmax,
    xidz,
    if_then_else,
    prod,
    ramp,
    zidz,
    integer,
    get_time_value,
)
from pysd.py_backend.statefuls import (
    DelayFixed,
    Initial,
    Smooth,
    Integ,
    Delay,
    SampleIfTrue,
)
from pysd.py_backend.external import ExtLookup, ExtConstant, ExtData
from pysd.py_backend.utils import load_modules, load_model_data
=======
    vector_sort_order,
    modulo,
    step,
    prod,
    vector_select,
    ramp,
    xidz,
    sum,
    integer,
    vmax,
    vector_reorder,
    get_time_value,
    invert_matrix,
    if_then_else,
    active_initial,
    zidz,
    vmin,
)
from pysd.py_backend.statefuls import (
    Smooth,
    SampleIfTrue,
    Delay,
    DelayFixed,
    Initial,
    Integ,
)
from pysd.py_backend.external import ExtConstant, ExtData, ExtLookup
from pysd.py_backend.utils import load_model_data, load_modules
>>>>>>> parent of 9b91d70 (Executed runs that were interrupted + change run.py)
from pysd.py_backend.allocation import allocate_available, allocate_by_priority
from pysd import Component

__pysd_version__ = "3.14.0"

__data = {"scope": None, "time": lambda: 0}

_root = Path(__file__).parent

_subscript_dict, _modules = load_model_data(_root, "WILIAM")

component = Component()

#######################################################################
#                          CONTROL VARIABLES                          #
#######################################################################

_control_vars = {
    "initial_time": lambda: 2005,
    "final_time": lambda: 2006,
    "time_step": lambda: 0.25,
    "saveper": lambda: 1,
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


@component.add(name="Time")
def time():
    """
    Current time of the model.
    """
    return __data["time"]()


@component.add(
    name="FINAL TIME", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def final_time():
    """
    The final time for the simulation.
    """
    return __data["time"].final_time()


@component.add(
    name="INITIAL TIME", units="Year", comp_type="Constant", comp_subtype="Normal"
)
def initial_time():
    """
    Initial time for the simulation of WILIAM. DO NOT MODIFY!!
    """
    return __data["time"].initial_time()


@component.add(
    name="SAVEPER",
    units="Year",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def saveper():
    """
    The frequency with which output is stored.
    """
    return __data["time"].saveper()


@component.add(
    name="TIME STEP",
    units="Year",
    limits=(0.0, np.nan),
    comp_type="Constant",
    comp_subtype="Normal",
)
def time_step():
    """
    The time step for the simulation.Used to delay the price signal, to prevent simultanous calculations.
    """
    return __data["time"].time_step()


#######################################################################
#                           MODEL VARIABLES                           #
#######################################################################

# load modules from modules_WILIAM directory
exec(load_modules("modules_WILIAM", _modules, _root, []))


@component.add(
    name="All minerals virgin base metals",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_all_minerals_virgin_base_metals"},
)
def all_minerals_virgin_base_metals():
    """
    Switch for performing sensitivity analysis: 0. All minerals are virgin: current and future recycling rates set to W% (option to compare with results offline MEDEAS). 1. Real share of virgin/recycled minerals (for normal simulations).
    """
    return _ext_constant_all_minerals_virgin_base_metals()


_ext_constant_all_minerals_virgin_base_metals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "all_minerals_virgin",
    {},
    _root,
    {},
    "_ext_constant_all_minerals_virgin_base_metals",
)


@component.add(
    name="CONSTATN MARK UP0",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_constatn_mark_up0"},
)
def constatn_mark_up0():
    """
    Producers' mark-up: share of profits over total price.
    """
    return _ext_constant_constatn_mark_up0()


_ext_constant_constatn_mark_up0 = ExtConstant(
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
    "_ext_constant_constatn_mark_up0",
)


@component.add(
    name="current EOL RR minerals base metals",
    units="DMNL",
    subscripts=["METALS W I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_current_eol_rr_minerals_base_metals"},
)
def current_eol_rr_minerals_base_metals():
    """
    Current End-Of-Life recycling rates from UNEP (2011)
    """
    return _ext_constant_current_eol_rr_minerals_base_metals()


_ext_constant_current_eol_rr_minerals_base_metals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "current_EOL_rr_minerals_base_metals*",
    {"METALS W I": _subscript_dict["METALS W I"]},
    _root,
    {"METALS W I": _subscript_dict["METALS W I"]},
    "_ext_constant_current_eol_rr_minerals_base_metals",
)


@component.add(
    name="delayed TS uranium extraction rate",
    units="EJ/Year",
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_uranium_extraction_rate": 1},
    other_deps={
        "_delayfixed_delayed_ts_uranium_extraction_rate": {
            "initial": {"initial_global_uranium_extraction_rate": 1, "time_step": 1},
            "step": {"uranium_extraction_rate": 1},
        }
    },
)
def delayed_ts_uranium_extraction_rate():
    """
    Delay to break simulataneous equations in the feedback demand nuclear -> demand uranium -> uranium availability -> demand nuclear.
    """
    return _delayfixed_delayed_ts_uranium_extraction_rate()


_delayfixed_delayed_ts_uranium_extraction_rate = DelayFixed(
    lambda: uranium_extraction_rate(),
    lambda: time_step(),
    lambda: initial_global_uranium_extraction_rate(),
    time_step,
    "_delayfixed_delayed_ts_uranium_extraction_rate",
)


@component.add(name='"FUND: TS.1: alpha"', comp_type="Constant", comp_subtype="Normal")
def fund_ts1_alpha():
    """
    TODO irrelevant
    """
    return 0


@component.add(
    name="Historic improvement recycling rates minerals base metals",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historic_improvement_recycling_rates_minerals_base_metals"
    },
)
def historic_improvement_recycling_rates_minerals_base_metals():
    """
    Due to the large uncertainty and slow evolution of these data, historical recycling rates minerals correspond with the current estimates (UNEP, 2011).
    """
    return _ext_constant_historic_improvement_recycling_rates_minerals_base_metals()


_ext_constant_historic_improvement_recycling_rates_minerals_base_metals = ExtConstant(
    "model_parameters/materials/materials.xlsx",
    "World",
    "historic_improvement_recycling_rates_minerals",
    {},
    _root,
    {},
    "_ext_constant_historic_improvement_recycling_rates_minerals_base_metals",
)


@component.add(
    name="HISTORICAL MEAN EU HOUSEHOLDS PER 100 PEOPLE",
    units="households/person",
    subscripts=["HOUSEHOLDS DEMOGRAPHY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_historical_mean_eu_households_per_100_people"
    },
)
def historical_mean_eu_households_per_100_people():
    """
    Mean historical values for the ratio of households per 100 people
    """
    return _ext_constant_historical_mean_eu_households_per_100_people()


_ext_constant_historical_mean_eu_households_per_100_people = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "DATA_LOADING",
    "MIN_HISTORICAL_HOUSEHOLDS_RATIO*",
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    _root,
    {"HOUSEHOLDS DEMOGRAPHY I": _subscript_dict["HOUSEHOLDS DEMOGRAPHY I"]},
    "_ext_constant_historical_mean_eu_households_per_100_people",
)


@component.add(
    name="INITIAL PASSENGER TRANSPORT DEMAND SHARE EXOGENOUS",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_initial_passenger_transport_demand_share_exogenous"
    },
)
def initial_passenger_transport_demand_share_exogenous():
    """
    Demand transport share by transport mode and power train in 2015 year.
    """
    return _ext_constant_initial_passenger_transport_demand_share_exogenous()


_ext_constant_initial_passenger_transport_demand_share_exogenous = ExtConstant(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_AUSTRIA",
    {
        "REGIONS 35 I": ["AUSTRIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_initial_passenger_transport_demand_share_exogenous",
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_BELGIUM",
    {
        "REGIONS 35 I": ["BELGIUM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_BULGARIA",
    {
        "REGIONS 35 I": ["BULGARIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_CROATIA",
    {
        "REGIONS 35 I": ["CROATIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_CYPRUS",
    {
        "REGIONS 35 I": ["CYPRUS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_CZECH_REPUBLIC",
    {
        "REGIONS 35 I": ["CZECH REPUBLIC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_DENMARK",
    {
        "REGIONS 35 I": ["DENMARK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_ESTONIA",
    {
        "REGIONS 35 I": ["ESTONIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_FINLAND",
    {
        "REGIONS 35 I": ["FINLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_FRANCE",
    {
        "REGIONS 35 I": ["FRANCE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_GERMANY",
    {
        "REGIONS 35 I": ["GERMANY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_GREECE",
    {
        "REGIONS 35 I": ["GREECE"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_HUNGARY",
    {
        "REGIONS 35 I": ["HUNGARY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_IRELAND",
    {
        "REGIONS 35 I": ["IRELAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_ITALY",
    {
        "REGIONS 35 I": ["ITALY"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_LATVIA",
    {
        "REGIONS 35 I": ["LATVIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_LITHUANIA",
    {
        "REGIONS 35 I": ["LITHUANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_LUXEMBOURG",
    {
        "REGIONS 35 I": ["LUXEMBOURG"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_MALTA",
    {
        "REGIONS 35 I": ["MALTA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_NETHERLANDS",
    {
        "REGIONS 35 I": ["NETHERLANDS"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_POLAND",
    {
        "REGIONS 35 I": ["POLAND"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_PORTUGAL",
    {
        "REGIONS 35 I": ["PORTUGAL"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_ROMANIA",
    {
        "REGIONS 35 I": ["ROMANIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_SLOVAKIA",
    {
        "REGIONS 35 I": ["SLOVAKIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_SLOVENIA",
    {
        "REGIONS 35 I": ["SLOVENIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_SPAIN",
    {
        "REGIONS 35 I": ["SPAIN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_SWEDEN",
    {
        "REGIONS 35 I": ["SWEDEN"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_UK",
    {
        "REGIONS 35 I": ["UK"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_CHINA",
    {
        "REGIONS 35 I": ["CHINA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_EASOC",
    {
        "REGIONS 35 I": ["EASOC"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_INDIA",
    {
        "REGIONS 35 I": ["INDIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_LATAM",
    {
        "REGIONS 35 I": ["LATAM"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_RUSSIA",
    {
        "REGIONS 35 I": ["RUSSIA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_USMCA",
    {
        "REGIONS 35 I": ["USMCA"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)

_ext_constant_initial_passenger_transport_demand_share_exogenous.add(
    "model_parameters/energy/energy-end_use-passenger_transport.xlsx",
    "technical_parameters",
    "INITIAL_DEMAND_SHARE_LROW",
    {
        "REGIONS 35 I": ["LROW"],
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
)


@component.add(
    name="model explorer passenger transport demand modal share",
    units="DMNL",
    subscripts=[
        "REGIONS 35 I",
        "TRANSPORT POWER TRAIN I",
        "PASSENGERS TRANSPORT MODE I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
        "initial_passenger_transport_demand_share_exogenous": 7,
        "final_year_model_explorer": 6,
        "scenario_passenger_transport_demand_modal_share_option_1_me": 1,
        "select_passenger_transport_demand_modal_share_me": 3,
        "scenario_passenger_transport_demand_modal_share_option_2_me": 1,
        "scenario_passenger_transport_demand_modal_share_option_3_me": 1,
    },
)
def model_explorer_passenger_transport_demand_modal_share():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: initial_passenger_transport_demand_share_exogenous(),
        lambda: if_then_else(
            select_passenger_transport_demand_modal_share_me() == 1,
            lambda: initial_passenger_transport_demand_share_exogenous()
            + ramp(
                __data["time"],
                (
                    scenario_passenger_transport_demand_modal_share_option_1_me()
                    - initial_passenger_transport_demand_share_exogenous()
                )
                / (final_year_model_explorer() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_model_explorer(),
            ),
            lambda: if_then_else(
                select_passenger_transport_demand_modal_share_me() == 2,
                lambda: initial_passenger_transport_demand_share_exogenous()
                + ramp(
                    __data["time"],
                    (
                        scenario_passenger_transport_demand_modal_share_option_2_me()
                        - initial_passenger_transport_demand_share_exogenous()
                    )
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_model_explorer(),
                ),
                lambda: if_then_else(
                    select_passenger_transport_demand_modal_share_me() == 3,
                    lambda: initial_passenger_transport_demand_share_exogenous()
                    + ramp(
                        __data["time"],
                        (
                            scenario_passenger_transport_demand_modal_share_option_3_me()
                            - initial_passenger_transport_demand_share_exogenous()
                        )
                        / (final_year_model_explorer() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "TRANSPORT POWER TRAIN I": _subscript_dict[
                                "TRANSPORT POWER TRAIN I"
                            ],
                            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                                "PASSENGERS TRANSPORT MODE I"
                            ],
                        },
                        [
                            "REGIONS 35 I",
                            "TRANSPORT POWER TRAIN I",
                            "PASSENGERS TRANSPORT MODE I",
                        ],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="model explorer reduction passenger transport demand",
    units="DMNL",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 4,
        "initial_year_model_explorer": 7,
<<<<<<< HEAD
        "scenario_passenger_transport_demand_option_1_me": 1,
        "scenario_passenger_transport_demand_option_3_me": 1,
        "select_reduction_passenger_transport_demand_me": 3,
        "final_year_model_explorer": 6,
        "scenario_passenger_transport_demand_option_2_me": 1,
=======
        "final_year_model_explorer": 6,
        "scenario_passenger_transport_demand_option_1_me": 1,
        "select_reduction_passenger_transport_demand_me": 3,
        "scenario_passenger_transport_demand_option_2_me": 1,
        "scenario_passenger_transport_demand_option_3_me": 1,
>>>>>>> parent of 9b91d70 (Executed runs that were interrupted + change run.py)
    },
)
def model_explorer_reduction_passenger_transport_demand():
    """
    Policy government deficit of surplus for model explorer.
    """
    return if_then_else(
        time() < initial_year_model_explorer(),
        lambda: xr.DataArray(
            1,
            {
                "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
                "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                    "PASSENGERS TRANSPORT MODE I"
                ],
            },
            ["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
        ),
        lambda: if_then_else(
            select_reduction_passenger_transport_demand_me() == 1,
            lambda: 1
            + ramp(
                __data["time"],
                (scenario_passenger_transport_demand_option_1_me() - 1)
                / (final_year_model_explorer() - initial_year_model_explorer()),
                initial_year_model_explorer(),
                final_year_model_explorer(),
            ),
            lambda: if_then_else(
                select_reduction_passenger_transport_demand_me() == 2,
                lambda: 1
                + ramp(
                    __data["time"],
                    (scenario_passenger_transport_demand_option_2_me() - 1)
                    / (final_year_model_explorer() - initial_year_model_explorer()),
                    initial_year_model_explorer(),
                    final_year_model_explorer(),
                ),
                lambda: if_then_else(
                    select_reduction_passenger_transport_demand_me() == 3,
                    lambda: 1
                    + ramp(
                        __data["time"],
                        (scenario_passenger_transport_demand_option_3_me() - 1)
                        / (final_year_model_explorer() - initial_year_model_explorer()),
                        initial_year_model_explorer(),
                        final_year_model_explorer(),
                    ),
                    lambda: xr.DataArray(
                        1,
                        {
                            "TRANSPORT POWER TRAIN I": _subscript_dict[
                                "TRANSPORT POWER TRAIN I"
                            ],
                            "PASSENGERS TRANSPORT MODE I": _subscript_dict[
                                "PASSENGERS TRANSPORT MODE I"
                            ],
                        },
                        ["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="OBJECTIVE FUEL CONSUMPTION EFFICIENCY CHANGE SP",
    units="DMNL",
    subscripts=["TRANSPORT POWER TRAIN I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_fuel_consumption_efficiency_change_sp"
    },
)
def objective_fuel_consumption_efficiency_change_sp():
    return _ext_constant_objective_fuel_consumption_efficiency_change_sp()


_ext_constant_objective_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "TRANSPORT POWER TRAIN I": _subscript_dict["TRANSPORT POWER TRAIN I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_objective_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="OBJECTIVE LOAD FACTOR CHANGE SP",
    units="DMNL",
    subscripts=["REGIONS 35 I", "PRIVATE TRANSPORT I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_objective_load_factor_change_sp"},
)
def objective_load_factor_change_sp():
    """
    Objective value of the load factor variation measure. 1: no variation 2: double the initial load factor 0.5: half of the initial value
    """
    return _ext_constant_objective_load_factor_change_sp()


_ext_constant_objective_load_factor_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_LOAD_FACTOR_CHANGE_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PRIVATE TRANSPORT I": _subscript_dict["PRIVATE TRANSPORT I"],
    },
    "_ext_constant_objective_load_factor_change_sp",
)


@component.add(
    name="OBJECTIVE REDUCTION PASSENGER TRANSPORT DEMAND SP",
    units="1",
    subscripts=["REGIONS 35 I", "PASSENGERS TRANSPORT MODE I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_objective_reduction_passenger_transport_demand_sp"
    },
)
def objective_reduction_passenger_transport_demand_sp():
    return _ext_constant_objective_reduction_passenger_transport_demand_sp()


_ext_constant_objective_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "OBJECTIVE_REDUCTION_TRANSPORT_DEMAND_SP",
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    _root,
    {
        "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
        "PASSENGERS TRANSPORT MODE I": _subscript_dict["PASSENGERS TRANSPORT MODE I"],
    },
    "_ext_constant_objective_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="POLICY COMMON RR MINERALS VARIATION SP W base metals",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_policy_common_rr_minerals_variation_sp_w_base_metals"
    },
)
def policy_common_rr_minerals_variation_sp_w_base_metals():
    """
    Annual recycling rate improvement per mineral for the rest of the economy.
    """
    return _ext_constant_policy_common_rr_minerals_variation_sp_w_base_metals()


_ext_constant_policy_common_rr_minerals_variation_sp_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "annual_recycling_rate_variation_base_metals",
    {},
    _root,
    {},
    "_ext_constant_policy_common_rr_minerals_variation_sp_w_base_metals",
)


@component.add(
    name="POPULATION 2004 9 REGIONS",
    units="people",
    subscripts=["REGIONS 9 I", "SEX I", "AGE CHAIN I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_2004": 9},
)
def population_2004_9_regions():
    """
    Population in 2004 for 9 regions (EU-27 is aggregated)
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SEX I": _subscript_dict["SEX I"],
            "AGE CHAIN I": _subscript_dict["AGE CHAIN I"],
        },
        ["REGIONS 9 I", "SEX I", "AGE CHAIN I"],
    )
    value.loc[["EU27"], :, :] = (
        sum(
            population_2004()
            .loc[_subscript_dict["REGIONS EU27 I"], :, _subscript_dict["AGE CHAIN I"]]
            .rename(
                {"REGIONS 35 I": "REGIONS EU27 I!", "AGE COHORTS I": "AGE CHAIN I"}
            ),
            dim=["REGIONS EU27 I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    value.loc[["UK"], :, :] = (
        population_2004()
        .loc["UK", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["UK"]}, 0)
        .values
    )
    value.loc[["CHINA"], :, :] = (
        population_2004()
        .loc["CHINA", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["CHINA"]}, 0)
        .values
    )
    value.loc[["EASOC"], :, :] = (
        population_2004()
        .loc["EASOC", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["EASOC"]}, 0)
        .values
    )
    value.loc[["INDIA"], :, :] = (
        population_2004()
        .loc["INDIA", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["INDIA"]}, 0)
        .values
    )
    value.loc[["LATAM"], :, :] = (
        population_2004()
        .loc["LATAM", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["LATAM"]}, 0)
        .values
    )
    value.loc[["RUSSIA"], :, :] = (
        population_2004()
        .loc["RUSSIA", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["RUSSIA"]}, 0)
        .values
    )
    value.loc[["USMCA"], :, :] = (
        population_2004()
        .loc["USMCA", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["USMCA"]}, 0)
        .values
    )
    value.loc[["LROW"], :, :] = (
        population_2004()
        .loc["LROW", :, _subscript_dict["AGE CHAIN I"]]
        .reset_coords(drop=True)
        .rename({"AGE COHORTS I": "AGE CHAIN I"})
        .expand_dims({"REGIONS 35 I": ["LROW"]}, 0)
        .values
    )
    return value


@component.add(
    name="required capacity expansion flexibility options",
    units="TW/Year",
    subscripts=["REGIONS 9 I", "NRG COMMODITIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "curtailement_to_elec_power_system": 1,
        "unit_conversion_hours_year": 1,
        "one_year": 1,
    },
)
def required_capacity_expansion_flexibility_options():
    """
    Equivalent capacity to the curtailed energy per year. This is the trigger variable to expand the installed capacities of flexible power plants. EnergyPLAN --> equivalent to the CEEP before strategy decisions. MAX(SUM(PROTRA_capacity_stock[REGIONS_9_I,TO_elec,NRG_PROTRA_I!] * UNIT_CONVERSION_TW_PER_EJ_PER_YEAR * (protra_max_full_load_hours_curtailed[REGIONS_9_I,NRG_PROTRA_I!] - protra_max_full_load_hours_after_constraints[REGIONS_9_I ,NRG_PROTRA_I!]) ) * UNIT_CONVERSION_TWh_EJ / UNIT_CONVERSION_HOURS_YEAR, 0)
    """
    return (
        curtailement_to_elec_power_system() / unit_conversion_hours_year() / one_year()
    ).expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)


@component.add(
    name="SELECT MARK UP SP 0",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_mark_up_sp_0"},
)
def select_mark_up_sp_0():
    """
    Switch mark-up 0: Default 1: User defined
    """
    return _ext_constant_select_mark_up_sp_0()


_ext_constant_select_mark_up_sp_0 = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "economy",
    "SELECT_MARK_UP_VARIATION_SP",
    {},
    _root,
    {},
    "_ext_constant_select_mark_up_sp_0",
)


@component.add(
    name="SELECT MINERAL RR TARGETS SP W base metals",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_mineral_rr_targets_sp_w_base_metals"
    },
)
def select_mineral_rr_targets_sp_w_base_metals():
    """
    1- Disaggregated by mineral. 2- Common annual variation for all minerals.
    """
    return _ext_constant_select_mineral_rr_targets_sp_w_base_metals()


_ext_constant_select_mineral_rr_targets_sp_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Disaggregated_by_mineral_1_or_common_annual_variation_for_all_minerals_2_base_metals",
    {},
    _root,
    {},
    "_ext_constant_select_mineral_rr_targets_sp_w_base_metals",
)


@component.add(
    name="SELECT URANIUM MAXIMUM SUPPLY CURVE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_uranium_maximum_supply_curve_sp"},
)
def select_uranium_maximum_supply_curve_sp():
    """
    Select uranium maximum supply curve from literature, or user-defined.
    """
    return _ext_constant_select_uranium_maximum_supply_curve_sp()


_ext_constant_select_uranium_maximum_supply_curve_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "SELECT_URANIUM_MAX_SUPPLY_CURVE_SP",
    {},
    _root,
    {},
    "_ext_constant_select_uranium_maximum_supply_curve_sp",
)


@component.add(
    name="START YEAR P COMMON RR MINERALS W base metals",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_start_year_p_common_rr_minerals_w_base_metals"
    },
)
def start_year_p_common_rr_minerals_w_base_metals():
    """
    Start year of variation recycling rate of minerals of the rest of the economy.
    """
    return _ext_constant_start_year_p_common_rr_minerals_w_base_metals()


_ext_constant_start_year_p_common_rr_minerals_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_starting_year_base_metals",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_common_rr_minerals_w_base_metals",
)


@component.add(
    name="START YEAR P RR MINERALS W base metals",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_start_year_p_rr_minerals_w_base_metals"},
)
def start_year_p_rr_minerals_w_base_metals():
    """
    Start year of variation recycling rate of minerals for the rest of the economy.
    """
    return _ext_constant_start_year_p_rr_minerals_w_base_metals()


_ext_constant_start_year_p_rr_minerals_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_starting_year_base_metals",
    {},
    _root,
    {},
    "_ext_constant_start_year_p_rr_minerals_w_base_metals",
)


@component.add(
    name="SWITCH ECO2NRG MODAL SHARES PASSENGERS ENDOGENOUS",
    units="1",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_eco2nrg_modal_shares_passengers_endogenous"
    },
)
def switch_eco2nrg_modal_shares_passengers_endogenous():
    """
    =0 the model runs with exogenous modal shares defined in the energy module =1 the model runs with endogenous modal shares driven by prices
    """
    return _ext_constant_switch_eco2nrg_modal_shares_passengers_endogenous()


_ext_constant_switch_eco2nrg_modal_shares_passengers_endogenous = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_MODAL_SHARES_PASSENGERS_ENDOGENOUS",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_modal_shares_passengers_endogenous",
)


@component.add(
    name="SWITCH FUEL CONSUMPTION EFFICIENCY CHANGE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_fuel_consumption_efficiency_change_sp"
    },
)
def switch_fuel_consumption_efficiency_change_sp():
    return _ext_constant_switch_fuel_consumption_efficiency_change_sp()


_ext_constant_switch_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="SWITCH LOAD FACTOR CHANGE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_load_factor_change_sp"},
)
def switch_load_factor_change_sp():
    """
    1: deactivate the scenario parameter measure 0: Activate the scenario parameter measure
    """
    return _ext_constant_switch_load_factor_change_sp()


_ext_constant_switch_load_factor_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_LOAD_FACTOR_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_load_factor_change_sp",
)


@component.add(
    name="SWITCH MODEL EXPLORER",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_model_explorer"},
)
def switch_model_explorer():
    """
    Switch for the model explorer. OFF=0 ON=1
    """
    return _ext_constant_switch_model_explorer()


_ext_constant_switch_model_explorer = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "inputs_model_explorer",
    "SWITCH_MODEL_EXPLORER",
    {},
    _root,
    {},
    "_ext_constant_switch_model_explorer",
)


@component.add(
    name="SWITCH PASSENGER TRANSPORT MODAL SHARE SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_passenger_transport_modal_share_sp"
    },
)
def switch_passenger_transport_modal_share_sp():
    return _ext_constant_switch_passenger_transport_modal_share_sp()


_ext_constant_switch_passenger_transport_modal_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_passenger_transport_modal_share_sp",
)


@component.add(
    name="SWITCH REDUCTION PASSENGER TRANSPORT DEMAND SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_reduction_passenger_transport_demand_sp"
    },
)
def switch_reduction_passenger_transport_demand_sp():
    return _ext_constant_switch_reduction_passenger_transport_demand_sp()


_ext_constant_switch_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "SWITCH_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_switch_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="TARGET RR REST SP W base metals",
    units="DMNL",
    subscripts=["METALS W I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_target_rr_rest_sp_w_base_metals"},
)
def target_rr_rest_sp_w_base_metals():
    """
    Rest_of_the_economy_current_rates
    """
    return _ext_constant_target_rr_rest_sp_w_base_metals()


_ext_constant_target_rr_rest_sp_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Rest_of_the_base_metals_current_rates*",
    {"METALS W I": _subscript_dict["METALS W I"]},
    _root,
    {"METALS W I": _subscript_dict["METALS W I"]},
    "_ext_constant_target_rr_rest_sp_w_base_metals",
)


@component.add(
    name="TARGET YEAR P RR MINERALS REST W base metals",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_target_year_p_rr_minerals_rest_w_base_metals"
    },
)
def target_year_p_rr_minerals_rest_w_base_metals():
    """
    Target year of variation recycling rate of minerals for the rest of the economy.
    """
    return _ext_constant_target_year_p_rr_minerals_rest_w_base_metals()


_ext_constant_target_year_p_rr_minerals_rest_w_base_metals = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "materials",
    "Recycling_rates_by_mineral_target_year_base_metals",
    {},
    _root,
    {},
    "_ext_constant_target_year_p_rr_minerals_rest_w_base_metals",
)


@component.add(
    name="VARIATION POPULATION 2005 2015",
    units="people",
    subscripts=["REGIONS EU27 I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_variation_population_2005_2015"},
)
def variation_population_2005_2015():
    """
    Variation of population between 2005 and 2015
    """
    return _ext_constant_variation_population_2005_2015()


_ext_constant_variation_population_2005_2015 = ExtConstant(
    "model_parameters/demography/demography.xlsx",
    "Calibration",
    "VARIATION_POPULATION_2005_2015*",
    {"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]},
    _root,
    {"REGIONS EU27 I": _subscript_dict["REGIONS EU27 I"]},
    "_ext_constant_variation_population_2005_2015",
)


@component.add(
    name="YEAR FINAL FUEL CONSUMPTION EFFICIENCY CHANGE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_fuel_consumption_efficiency_change_sp"
    },
)
def year_final_fuel_consumption_efficiency_change_sp():
    return _ext_constant_year_final_fuel_consumption_efficiency_change_sp()


_ext_constant_year_final_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="YEAR FINAL LOAD FACTOR CHANGE SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_final_load_factor_change_sp"},
)
def year_final_load_factor_change_sp():
    """
    Year of full implementation of the load factor variation measure.
    """
    return _ext_constant_year_final_load_factor_change_sp()


_ext_constant_year_final_load_factor_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_LOAD_FACTOR_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_load_factor_change_sp",
)


@component.add(
    name="YEAR FINAL PASSENGER TRANSPORT SHARE SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_passenger_transport_share_sp"
    },
)
def year_final_passenger_transport_share_sp():
    return _ext_constant_year_final_passenger_transport_share_sp()


_ext_constant_year_final_passenger_transport_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_passenger_transport_share_sp",
)


@component.add(
    name="YEAR FINAL REDUCTION PASSENGER TRANSPORT DEMAND SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_final_reduction_passenger_transport_demand_sp"
    },
)
def year_final_reduction_passenger_transport_demand_sp():
    return _ext_constant_year_final_reduction_passenger_transport_demand_sp()


_ext_constant_year_final_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_FINAL_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_year_final_reduction_passenger_transport_demand_sp",
)


@component.add(
    name="YEAR INITIAL FUEL CONSUMPTION EFFICIENCY CHANGE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_fuel_consumption_efficiency_change_sp"
    },
)
def year_initial_fuel_consumption_efficiency_change_sp():
    return _ext_constant_year_initial_fuel_consumption_efficiency_change_sp()


_ext_constant_year_initial_fuel_consumption_efficiency_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_FUEL_CONSUMPTION_EFFICIENCY_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_fuel_consumption_efficiency_change_sp",
)


@component.add(
    name="YEAR INITIAL LOAD FACTOR CHANGE SP",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_year_initial_load_factor_change_sp"},
)
def year_initial_load_factor_change_sp():
    """
    Initial year of the load fcator variation measure
    """
    return _ext_constant_year_initial_load_factor_change_sp()


_ext_constant_year_initial_load_factor_change_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_LOAD_FACTOR_CHANGE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_load_factor_change_sp",
)


@component.add(
    name="YEAR INITIAL PASSENGER TRANSPORT SHARE SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_passenger_transport_share_sp"
    },
)
def year_initial_passenger_transport_share_sp():
    """
    Start year of the modal share modification policy
    """
    return _ext_constant_year_initial_passenger_transport_share_sp()


_ext_constant_year_initial_passenger_transport_share_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_TRANSPORT_SHARE_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_passenger_transport_share_sp",
)


@component.add(
    name="YEAR INITIAL REDUCTION PASSENGER TRANSPORT DEMAND SP",
    units="Year",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_year_initial_reduction_passenger_transport_demand_sp"
    },
)
def year_initial_reduction_passenger_transport_demand_sp():
    return _ext_constant_year_initial_reduction_passenger_transport_demand_sp()


_ext_constant_year_initial_reduction_passenger_transport_demand_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy-transport",
    "YEAR_INITIAL_REDUCTION_TRANSPORT_DEMAND_SP",
    {},
    _root,
    {},
    "_ext_constant_year_initial_reduction_passenger_transport_demand_sp",
)
