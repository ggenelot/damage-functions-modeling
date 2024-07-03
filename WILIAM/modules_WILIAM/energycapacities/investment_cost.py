"""
Module energycapacities.investment_cost
Translated using PySD version 3.14.0
"""

@component.add(
    name="CAPACITY INVESTMENT COST PRO FLEXOPT HIGH DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_high_development():
    """
    Assumption of higher development (lower costs) future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_high_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_high_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_HIGH",
    "interpolate",
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    _root,
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_high_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PRO FLEXOPT LOW DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_low_development():
    """
    Assumption of lower development (higher costs) future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_low_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_low_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_LOW",
    "interpolate",
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    _root,
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_low_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PRO FLEXOPT MEDIUM DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_medium_development():
    """
    Assumption of medium future capacity costs for PRO FLEXOPT with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_medium_development(time())


_ext_data_capacity_investment_cost_pro_flexopt_medium_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "time_PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_MEDIUM",
    "interpolate",
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    _root,
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_medium_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PRO FLEXOPT USER DEFINED SP",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
        "__data__": "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
        "time": 1,
    },
)
def capacity_investment_cost_pro_flexopt_user_defined_sp():
    """
    Assumption from model user for future capacity costs for PROFLEX.
    """
    return _ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp(time())


_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "time",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_USER_DEFINED_SP",
    "interpolate",
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    _root,
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    "_ext_data_capacity_investment_cost_pro_flexopt_user_defined_sp",
)


@component.add(
    name="CAPACITY INVESTMENT COST PROFLEX DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_capacity_investment_cost_development_sp": 4,
        "pro_flexopt_capacity_investment_cost_2015": 1,
        "capacity_investment_cost_pro_flexopt_low_development": 1,
        "capacity_investment_cost_pro_flexopt_user_defined_sp": 1,
        "capacity_investment_cost_pro_flexopt_high_development": 1,
        "capacity_investment_cost_pro_flexopt_medium_development": 1,
    },
)
def capacity_investment_cost_proflex_development():
    """
    Investment cost depending on assumption of their exogenous future evolution.
    """
    return if_then_else(
        select_capacity_investment_cost_development_sp() == 0,
        lambda: pro_flexopt_capacity_investment_cost_2015(),
        lambda: if_then_else(
            select_capacity_investment_cost_development_sp() == 1,
            lambda: capacity_investment_cost_pro_flexopt_low_development(),
            lambda: if_then_else(
                select_capacity_investment_cost_development_sp() == 2,
                lambda: capacity_investment_cost_pro_flexopt_medium_development(),
                lambda: if_then_else(
                    select_capacity_investment_cost_development_sp() == 3,
                    lambda: capacity_investment_cost_pro_flexopt_high_development(),
                    lambda: capacity_investment_cost_pro_flexopt_user_defined_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="CAPACITY INVESTMENT COST PROTRA DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "select_capacity_investment_cost_development_sp": 4,
        "protra_capacity_investment_cost_2015": 1,
        "capacity_investment_cost_protra_high_development": 1,
        "capacity_investment_cost_protra_user_defined_sp": 1,
        "capacity_investment_cost_protra_low_development": 1,
        "capacity_investment_cost_protra_medium_development": 1,
    },
)
def capacity_investment_cost_protra_development():
    """
    Investment cost depending on assumption of their exogenous future evolution.
    """
    return if_then_else(
        select_capacity_investment_cost_development_sp() == 0,
        lambda: protra_capacity_investment_cost_2015(),
        lambda: if_then_else(
            select_capacity_investment_cost_development_sp() == 1,
            lambda: capacity_investment_cost_protra_low_development(),
            lambda: if_then_else(
                select_capacity_investment_cost_development_sp() == 2,
                lambda: capacity_investment_cost_protra_medium_development(),
                lambda: if_then_else(
                    select_capacity_investment_cost_development_sp() == 3,
                    lambda: capacity_investment_cost_protra_high_development(),
                    lambda: capacity_investment_cost_protra_user_defined_sp(),
                ),
            ),
        ),
    )


@component.add(
    name="CAPACITY INVESTMENT COST PROTRA HIGH DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_high_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_high_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_high_development():
    """
    Assumption of higher development (reduced costs) future capacity costs for PROTRA with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_protra_high_development(time())


_ext_data_capacity_investment_cost_protra_high_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_HIGH_DEVELOPMENT",
    "interpolate",
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    _root,
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    "_ext_data_capacity_investment_cost_protra_high_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PROTRA LOW DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_low_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_low_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_low_development():
    """
    Assumption of lower development (higher costs) future capacity costs for PROTRA with relation to the medium-reference scenario.
    """
    return _ext_data_capacity_investment_cost_protra_low_development(time())


_ext_data_capacity_investment_cost_protra_low_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_LOW_DEVELOPMENT",
    "interpolate",
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    _root,
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    "_ext_data_capacity_investment_cost_protra_low_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PROTRA MEDIUM DEVELOPMENT",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_medium_development",
        "__data__": "_ext_data_capacity_investment_cost_protra_medium_development",
        "time": 1,
    },
)
def capacity_investment_cost_protra_medium_development():
    return _ext_data_capacity_investment_cost_protra_medium_development(time())


_ext_data_capacity_investment_cost_protra_medium_development = ExtData(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_MEDIUM_DEVELOPMENT",
    "interpolate",
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    _root,
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    "_ext_data_capacity_investment_cost_protra_medium_development",
)


@component.add(
    name="CAPACITY INVESTMENT COST PROTRA USER DEFINED SP",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Data",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_data_capacity_investment_cost_protra_user_defined_sp",
        "__data__": "_ext_data_capacity_investment_cost_protra_user_defined_sp",
        "time": 1,
    },
)
def capacity_investment_cost_protra_user_defined_sp():
    """
    Assumption from model user for future capacity costs for PROTRA.
    """
    return _ext_data_capacity_investment_cost_protra_user_defined_sp(time())


_ext_data_capacity_investment_cost_protra_user_defined_sp = ExtData(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "time",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_USER_DEFINED",
    "interpolate",
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    _root,
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    "_ext_data_capacity_investment_cost_protra_user_defined_sp",
)


@component.add(
    name="capital decommissioning by PROTRA",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_decommissioning_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def capital_decommissioning_by_protra():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_decommissioning_35r()
            .loc[:, :, _subscript_dict["PROTRA PP CHP HP I"]]
            .rename({"NRG TO I": "NRG TO I!", "NRG PROTRA I": "PROTRA PP CHP HP I"}),
            dim=["NRG TO I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="capital decommissioning PROTRA sectors",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capital_decommissioning_by_protra": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def capital_decommissioning_protra_sectors():
    """
    Capita stock of PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        capital_decommissioning_by_protra().rename(
            {"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}
        )
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}
        ),
        dim=["PROTRA PP CHP HP I!"],
    )


@component.add(
    name="capital stock by PROTRA",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_stock_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def capital_stock_by_protra():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_stock_35r()
            .loc[:, :, _subscript_dict["PROTRA PP CHP HP I"]]
            .rename({"NRG TO I": "NRG TO I!", "NRG PROTRA I": "PROTRA PP CHP HP I"}),
            dim=["NRG TO I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="capital stock PROTRA sectors",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "capital_stock_by_protra": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def capital_stock_protra_sectors():
    """
    Capita stock of PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        capital_stock_by_protra().rename({"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"})
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}
        ),
        dim=["PROTRA PP CHP HP I!"],
    )


@component.add(
    name="CORRESPONDENCE MATRIX PROFLEX SECTORS",
    units="DMNL",
    subscripts=["PRO FLEXOPT I", "SECTORS ENERGY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_correspondence_matrix_proflex_sectors"},
)
def correspondence_matrix_proflex_sectors():
    """
    Correspondence matrix to assign technologies of flexibility management to economic sectors.
    """
    return _ext_constant_correspondence_matrix_proflex_sectors()


_ext_constant_correspondence_matrix_proflex_sectors = ExtConstant(
    "model_parameters/economy/correspondence_matrixes.xlsx",
    "economy_energy",
    "CORRESPONDENCE_MATRIX_FLEXOPT_SECTORS",
    {
        "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
        "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
    },
    _root,
    {
        "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
        "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
    },
    "_ext_constant_correspondence_matrix_proflex_sectors",
)


@component.add(
    name="CORRESPONDENCE MATRIX PROTRA SECTORS",
    units="DMNL",
    subscripts=["PROTRA PP CHP HP I", "SECTORS ENERGY I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_correspondence_matrix_protra_sectors"},
)
def correspondence_matrix_protra_sectors():
    """
    Correspondence matrix to assign PROTRA to economic sectors.
    """
    return _ext_constant_correspondence_matrix_protra_sectors()


_ext_constant_correspondence_matrix_protra_sectors = ExtConstant(
    "model_parameters/economy/correspondence_matrixes.xlsx",
    "economy_energy",
    "CORRESPONDENCE_PROTRA_SECTORS",
    {
        "PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"],
        "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
    },
    _root,
    {
        "PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"],
        "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
    },
    "_ext_constant_correspondence_matrix_protra_sectors",
)


@component.add(
    name="CORRESPONDENCE MATRIX SECTORS PROFLEX",
    units="DMNL",
    subscripts=["SECTORS ENERGY I", "PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"correspondence_matrix_proflex_sectors": 15},
)
def correspondence_matrix_sectors_proflex():
    """
    Correspondence matrix to assign economic sectors to PROFLEX. Transpose 'CORRESPONDENCE_MATRIX_PROFLEX_SECTORS'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
            "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
        },
        ["SECTORS ENERGY I", "PRO FLEXOPT I"],
    )
    value.loc[["COKE"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "COKE"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINED PRODUCTS INDUSTRY": ["COKE"]}, 0)
        .values
    )
    value.loc[["REFINING"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "REFINING"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 0)
        .values
    )
    value.loc[["HYDROGEN PRODUCTION"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "HYDROGEN PRODUCTION"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY COAL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY COAL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER COAL POWER PLANTS": _subscript_dict["CLUSTER COAL POWER PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY GAS"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY GAS"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER GAS POWER PLANTS": _subscript_dict["CLUSTER GAS POWER PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY NUCLEAR"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY NUCLEAR"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER NUCLEAR POWER PLANTS": _subscript_dict[
                    "CLUSTER NUCLEAR POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY HYDRO"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY HYDRO"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER HYDRO POWER PLANTS": _subscript_dict[
                    "CLUSTER HYDRO POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY WIND"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY WIND"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER WIND POWER PLANTS": _subscript_dict["CLUSTER WIND POWER PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY OIL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY OIL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER OIL POWER PLANTS": _subscript_dict["CLUSTER OIL POWER PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY SOLAR PV"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY SOLAR PV"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER SOLAR POWER PLANTS": ["ELECTRICITY SOLAR PV"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY SOLAR THERMAL"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY SOLAR THERMAL"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER SOLAR POWER PLANTS": ["ELECTRICITY SOLAR THERMAL"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY OTHER"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "ELECTRICITY OTHER"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER BIOMASS POWER PLANTS": _subscript_dict[
                    "CLUSTER BIOMASS POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION ELECTRICITY"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "DISTRIBUTION ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER ELECTRICITY TRANSPORT": _subscript_dict[
                    "CLUSTER ELECTRICITY TRANSPORT"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION GAS"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "DISTRIBUTION GAS"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 0)
        .values
    )
    value.loc[["STEAM HOT WATER"], :] = (
        correspondence_matrix_proflex_sectors()
        .loc[:, "STEAM HOT WATER"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 0)
        .values
    )
    return value


@component.add(
    name="CORRESPONDENCE MATRIX SECTORS PROTRA",
    units="DMNL",
    subscripts=["SECTORS ENERGY I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"correspondence_matrix_protra_sectors": 15},
)
def correspondence_matrix_sectors_protra():
    """
    Correspondence matrix to assign economic sectors to PROTRA. Transpose 'CORRESPONDENCE_MATRIX_PROTRA_SECTORS'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
            "PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"],
        },
        ["SECTORS ENERGY I", "PROTRA PP CHP HP I"],
    )
    value.loc[["COKE"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "COKE"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINED PRODUCTS INDUSTRY": ["COKE"]}, 0)
        .values
    )
    value.loc[["REFINING"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "REFINING"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 0)
        .values
    )
    value.loc[["HYDROGEN PRODUCTION"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "HYDROGEN PRODUCTION"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY COAL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY COAL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER COAL POWER PLANTS": _subscript_dict["CLUSTER COAL POWER PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY GAS"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY GAS"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER GAS POWER PLANTS": _subscript_dict["CLUSTER GAS POWER PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY NUCLEAR"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY NUCLEAR"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER NUCLEAR POWER PLANTS": _subscript_dict[
                    "CLUSTER NUCLEAR POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY HYDRO"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY HYDRO"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER HYDRO POWER PLANTS": _subscript_dict[
                    "CLUSTER HYDRO POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY WIND"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY WIND"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER WIND POWER PLANTS": _subscript_dict["CLUSTER WIND POWER PLANTS"]},
            0,
        )
        .values
    )
    value.loc[["ELECTRICITY OIL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY OIL"]
        .reset_coords(drop=True)
        .expand_dims(
            {"CLUSTER OIL POWER PLANTS": _subscript_dict["CLUSTER OIL POWER PLANTS"]}, 0
        )
        .values
    )
    value.loc[["ELECTRICITY SOLAR PV"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY SOLAR PV"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER SOLAR POWER PLANTS": ["ELECTRICITY SOLAR PV"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY SOLAR THERMAL"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY SOLAR THERMAL"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER SOLAR POWER PLANTS": ["ELECTRICITY SOLAR THERMAL"]}, 0)
        .values
    )
    value.loc[["ELECTRICITY OTHER"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "ELECTRICITY OTHER"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER BIOMASS POWER PLANTS": _subscript_dict[
                    "CLUSTER BIOMASS POWER PLANTS"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION ELECTRICITY"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "DISTRIBUTION ELECTRICITY"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER ELECTRICITY TRANSPORT": _subscript_dict[
                    "CLUSTER ELECTRICITY TRANSPORT"
                ]
            },
            0,
        )
        .values
    )
    value.loc[["DISTRIBUTION GAS"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "DISTRIBUTION GAS"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 0)
        .values
    )
    value.loc[["STEAM HOT WATER"], :] = (
        correspondence_matrix_protra_sectors()
        .loc[:, "STEAM HOT WATER"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 0)
        .values
    )
    return value


@component.add(
    name="delayed TS GFCF PROTRA sectors 35R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS ENERGY I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_gfcf_protra_sectors_35r": 1},
    other_deps={
        "_delayfixed_delayed_ts_gfcf_protra_sectors_35r": {
            "initial": {"time_step": 1},
            "step": {"investment_cost_protra_sectors_35r": 1},
        }
    },
)
def delayed_ts_gfcf_protra_sectors_35r():
    """
    DELAY to avoid feedback problems.
    """
    return _delayfixed_delayed_ts_gfcf_protra_sectors_35r()


_delayfixed_delayed_ts_gfcf_protra_sectors_35r = DelayFixed(
    lambda: investment_cost_protra_sectors_35r(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
        },
        ["REGIONS 35 I", "SECTORS ENERGY I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_gfcf_protra_sectors_35r",
)


@component.add(
    name="dynamic capacity investment cost PROFLEX development",
    units="Mdollars 2015/MW",
    subscripts=["REGIONS 9 I", "PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 2,
        "capacity_investment_cost_proflex_development": 4,
        "price_gfcf": 2,
        "correspondence_matrix_sectors_proflex": 2,
    },
)
def dynamic_capacity_investment_cost_proflex_development():
    """
    Capacity investment cost dynamized by the price of investments (price_GFCF) from economy module. Can be compared with the exogenous values in 'CAPACITY INVESTMENT COST PROFLEX DEVELOPMENT'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"],
        },
        ["REGIONS 9 I", "PRO FLEXOPT I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: capacity_investment_cost_proflex_development().expand_dims(
                {"REGIONS 8 I": _subscript_dict["REGIONS 8 I"]}, 1
            ),
            lambda: capacity_investment_cost_proflex_development()
            * sum(
                price_gfcf()
                .loc[
                    _subscript_dict["REGIONS 8 I"], _subscript_dict["SECTORS ENERGY I"]
                ]
                .rename(
                    {
                        "REGIONS 35 I": "REGIONS 8 I",
                        "SECTORS MAP I": "SECTORS ENERGY I!",
                    }
                )
                * correspondence_matrix_sectors_proflex().rename(
                    {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
                )
                / 100,
                dim=["SECTORS ENERGY I!"],
            ).transpose("PRO FLEXOPT I", "REGIONS 8 I"),
        )
        .transpose("REGIONS 8 I", "PRO FLEXOPT I")
        .values
    )
    value.loc[["EU27"], :] = (
        if_then_else(
            switch_energy() == 0,
            lambda: capacity_investment_cost_proflex_development(),
            lambda: capacity_investment_cost_proflex_development()
            * sum(
                price_gfcf()
                .loc["GERMANY", _subscript_dict["SECTORS ENERGY I"]]
                .reset_coords(drop=True)
                .rename({"SECTORS MAP I": "SECTORS ENERGY I!"})
                * correspondence_matrix_sectors_proflex().rename(
                    {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
                )
                / 100,
                dim=["SECTORS ENERGY I!"],
            ),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="dynamic capacity investment cost PROTRA development",
    units="Mdollars 2015/MW",
    subscripts=["REGIONS 35 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_energy": 1,
        "switch_eco2nrg_price_gfcf": 1,
        "capacity_investment_cost_protra_development": 2,
        "price_gfcf_by_protra": 1,
    },
)
def dynamic_capacity_investment_cost_protra_development():
    """
    Capacity investment cost dynamized by the price of investments (price_GFCF) from economy module. Can be compared with the exogenous values in 'CAPACITY INVESTMENT COST PROTRA DEVELOPMENT'.
    """
    return if_then_else(
        np.logical_or(switch_energy() == 0, switch_eco2nrg_price_gfcf() == 0),
        lambda: capacity_investment_cost_protra_development().expand_dims(
            {"REGIONS 35 I": _subscript_dict["REGIONS 35 I"]}, 1
        ),
        lambda: capacity_investment_cost_protra_development()
        * price_gfcf_by_protra().transpose("PROTRA PP CHP HP I", "REGIONS 35 I")
        / 100,
    ).transpose("REGIONS 35 I", "PROTRA PP CHP HP I")


@component.add(
    name="dynamic capacity investment cost PROTRA development 36R",
    units="Mdollars 2015/MW",
    subscripts=["REGIONS 36 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "dynamic_capacity_investment_cost_protra_development": 1,
        "dynamic_capacity_investment_cost_protra_development_eu27": 1,
    },
)
def dynamic_capacity_investment_cost_protra_development_36r():
    """
    Capacity investment cost dynamized by the price of investments (price_GFCF) from economy module for 36 regions. Can be compared with the exogenous values in 'CAPACITY INVESTMENT COST PROTRA DEVELOPMENT'.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"],
        },
        ["REGIONS 36 I", "PROTRA PP CHP HP I"],
    )
    value.loc[_subscript_dict["REGIONS 35 I"], :] = (
        dynamic_capacity_investment_cost_protra_development().values
    )
    value.loc[["EU27"], :] = (
        dynamic_capacity_investment_cost_protra_development_eu27()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="dynamic capacity investment cost PROTRA development EU27",
    units="Mdollars 2015/MW",
    subscripts=["REGIONS 36 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"dynamic_capacity_investment_cost_protra_development": 1},
)
def dynamic_capacity_investment_cost_protra_development_eu27():
    """
    Dynamic capacity investment cost downscaled for the 27 EU countries.
    """
    return (
        sum(
            dynamic_capacity_investment_cost_protra_development()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
            dim=["REGIONS EU27 I!"],
        )
        / 27
    ).expand_dims({"REGIONS 36 I": ["EU27"]}, 0)


@component.add(
    name="investment cost PROFLEX",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I", "PRO FLEXOPT I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "proflex_capacity_expansion": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_proflex_development": 1,
    },
)
def investment_cost_proflex():
    """
    Investment costs by FLEXOPT, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        proflex_capacity_expansion()
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_proflex_development()
    )


@component.add(
    name="investment cost PROFLEX sectors",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_proflex": 1,
        "correspondence_matrix_proflex_sectors": 1,
    },
)
def investment_cost_proflex_sectors():
    """
    Investments costs FLEXOPT using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        investment_cost_proflex().rename({"PRO FLEXOPT I": "PRO FLEXOPT I!"})
        * correspondence_matrix_proflex_sectors().rename(
            {"PRO FLEXOPT I": "PRO FLEXOPT I!"}
        ),
        dim=["PRO FLEXOPT I!"],
    )


@component.add(
    name="investment cost PROTRA 35R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "protra_capacity_expansion_35r": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_protra_development": 1,
    },
)
def investment_cost_protra_35r():
    """
    Investment costs by PROTRA, calculated as the new capacity addition times the unitary cost ($/MW) in real terms.
    """
    return (
        sum(
            protra_capacity_expansion_35r()
            .loc[:, :, _subscript_dict["PROTRA PP CHP HP I"]]
            .rename({"NRG TO I": "NRG TO I!", "NRG PROTRA I": "PROTRA PP CHP HP I"}),
            dim=["NRG TO I!"],
        )
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_protra_development()
    )


@component.add(
    name="investment cost PROTRA sectors 35R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_protra_35r": 1,
        "correspondence_matrix_protra_sectors": 1,
    },
)
def investment_cost_protra_sectors_35r():
    """
    Investments costs PROTRA using projection of investments costs up to 2050, by economic sector (SECTORS_ENERGY_I is a subrange of the vector SECTORS_I).
    """
    return sum(
        investment_cost_protra_35r().rename(
            {"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}
        )
        * correspondence_matrix_protra_sectors().rename(
            {"PROTRA PP CHP HP I": "PROTRA PP CHP HP I!"}
        ),
        dim=["PROTRA PP CHP HP I!"],
    )


@component.add(
    name="investment cost PROTRA sectors 9R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_protra_sectors_35r": 1,
        "investment_cost_protra_sectors_eu27": 1,
    },
)
def investment_cost_protra_sectors_9r():
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS ENERGY I": _subscript_dict["SECTORS ENERGY I"],
        },
        ["REGIONS 9 I", "SECTORS ENERGY I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        investment_cost_protra_sectors_35r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"], :] = (
        investment_cost_protra_sectors_eu27()
        .loc["EU27", :]
        .reset_coords(drop=True)
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="investment cost PROTRA sectors EU27",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 36 I", "SECTORS ENERGY I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_protra_sectors_35r": 1},
)
def investment_cost_protra_sectors_eu27():
    return sum(
        investment_cost_protra_sectors_35r()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    ).expand_dims({"REGIONS 36 I": ["EU27"]}, 0)


@component.add(
    name="investment cost stationary electrolysers",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "stationary_electrolyzers_capacity_expansion": 1,
        "unit_conversion_mw_tw": 1,
        "dynamic_capacity_investment_cost_proflex_development": 1,
    },
)
def investment_cost_stationary_electrolysers():
    """
    Investment costs if stationary electrolysers, assuming same cost than flexible electrolysers.
    """
    return (
        stationary_electrolyzers_capacity_expansion()
        * unit_conversion_mw_tw()
        * dynamic_capacity_investment_cost_proflex_development()
        .loc[:, "PROSUP elec 2 hydrogen"]
        .reset_coords(drop=True)
    )


@component.add(
    name="investment cost stationary electrolysers sectors",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I", "CLUSTER HYDROGEN"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_stationary_electrolysers": 1},
)
def investment_cost_stationary_electrolysers_sectors():
    return investment_cost_stationary_electrolysers().expand_dims(
        {"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 1
    )


@component.add(
    name="price GFCF by PROTRA",
    units="DMNL",
    subscripts=["REGIONS 35 I", "PROTRA PP CHP HP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"price_gfcf": 1, "correspondence_matrix_sectors_protra": 1},
)
def price_gfcf_by_protra():
    """
    Allocation of the price of investments (GFCF) by PROTRA technology. Base 100.
    """
    return sum(
        price_gfcf()
        .loc[:, _subscript_dict["SECTORS ENERGY I"]]
        .rename({"SECTORS MAP I": "SECTORS ENERGY I!"})
        * correspondence_matrix_sectors_protra().rename(
            {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
        ),
        dim=["SECTORS ENERGY I!"],
    )


@component.add(
    name="PRO FLEXOPT CAPACITY INVESTMENT COST 2015",
    units="Mdollars 2015/MW",
    subscripts=["PRO FLEXOPT I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_pro_flexopt_capacity_investment_cost_2015"
    },
)
def pro_flexopt_capacity_investment_cost_2015():
    """
    Since the cost of electrolyzers does not have a defined value (it is defined in a range) MIN, MEDIUM and HIGH INVESTMENT COST do not coincide in 2015; the value corresponding to CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_MEDIUM for PRO_FLEXOPT elec 2 hydrogen will be taken.
    """
    return _ext_constant_pro_flexopt_capacity_investment_cost_2015()


_ext_constant_pro_flexopt_capacity_investment_cost_2015 = ExtConstant(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PRO_FLEXOPT",
    "CAPACITY_INVESTMENT_COST_PRO_FLEXOPT_2015*",
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    _root,
    {"PRO FLEXOPT I": _subscript_dict["PRO FLEXOPT I"]},
    "_ext_constant_pro_flexopt_capacity_investment_cost_2015",
)


@component.add(
    name="PROTRA CAPACITY INVESTMENT COST 2015",
    units="Mdollars 2015/MW",
    subscripts=["PROTRA PP CHP HP I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_protra_capacity_investment_cost_2015"},
)
def protra_capacity_investment_cost_2015():
    return _ext_constant_protra_capacity_investment_cost_2015()


_ext_constant_protra_capacity_investment_cost_2015 = ExtConstant(
    "model_parameters/energy/energy-capacity_investment_cost.xlsx",
    "PROTRA",
    "CAPACITY_INVESTMENT_COST_PROTRA_CHP_HP_PP_2015*",
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    _root,
    {"PROTRA PP CHP HP I": _subscript_dict["PROTRA PP CHP HP I"]},
    "_ext_constant_protra_capacity_investment_cost_2015",
)


@component.add(
    name="SELECT CAPACITY INVESTMENT COST DEVELOPMENT SP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_select_capacity_investment_cost_development_sp"
    },
)
def select_capacity_investment_cost_development_sp():
    """
    0: constant 2015 values 1: low cost improvement development 2: medium cost improvement development 3: high cost improvement development 4: user-defined
    """
    return _ext_constant_select_capacity_investment_cost_development_sp()


_ext_constant_select_capacity_investment_cost_development_sp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "energy",
    "SELECT_CAPACITY_INVESTMENT_COST_DEVELOPMENT_SP",
    {},
    _root,
    {},
    "_ext_constant_select_capacity_investment_cost_development_sp",
)


@component.add(
    name="SWITCH ECO2NRG PRICE GFCF",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_eco2nrg_price_gfcf"},
)
def switch_eco2nrg_price_gfcf():
    """
    This switch can take two values: =0: the capacity investment costs in energy module are fully exogenous. =1: the capacity investment costs in energy module are also affected by the price of investments from economy module (price_GFCF).
    """
    return _ext_constant_switch_eco2nrg_price_gfcf()


_ext_constant_switch_eco2nrg_price_gfcf = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_ECO2NRG_PRICE_GFCF",
    {},
    _root,
    {},
    "_ext_constant_switch_eco2nrg_price_gfcf",
)


@component.add(
    name="total energy capacities investment cost",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "investment_cost_stationary_electrolysers_sectors": 1,
        "total_proflex_investment_cost": 1,
        "investment_cost_protra_sectors_9r": 1,
    },
)
def total_energy_capacities_investment_cost():
    """
    Total investment cost of new energy capacities for PROTRAs, electrolysers for H2 and synthetic fuels, and PROFLEX.
    """
    return (
        investment_cost_stationary_electrolysers_sectors()
        .loc[:, "HYDROGEN PRODUCTION"]
        .reset_coords(drop=True)
        + total_proflex_investment_cost()
        + sum(
            investment_cost_protra_sectors_9r().rename(
                {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
            ),
            dim=["SECTORS ENERGY I!"],
        )
    )


@component.add(
    name="total PROFLEX investment cost",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_proflex_sectors": 1},
)
def total_proflex_investment_cost():
    return sum(
        investment_cost_proflex_sectors().rename(
            {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
        ),
        dim=["SECTORS ENERGY I!"],
    )


@component.add(
    name="total PROTRA investment cost 35R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"investment_cost_protra_sectors_35r": 1},
)
def total_protra_investment_cost_35r():
    return sum(
        investment_cost_protra_sectors_35r().rename(
            {"SECTORS ENERGY I": "SECTORS ENERGY I!"}
        ),
        dim=["SECTORS ENERGY I!"],
    )
