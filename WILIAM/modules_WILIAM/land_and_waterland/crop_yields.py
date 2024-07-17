"""
Module land_and_waterland.crop_yields
Translated using PySD version 3.14.0
"""

@component.add(
    name="aux average management",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"effect_of_management_on_crops": 1, "mask_crops": 1},
)
def aux_average_management():
    """
    auximiar variable to calculate average management of croplands
    """
    return effect_of_management_on_crops() * mask_crops()


@component.add(
    name="aux trends of yield change R and I",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "trends_of_yield_change_r_and_i": 2,
    },
)
def aux_trends_of_yield_change_r_and_i():
    """
    This variable is to avoid that yields decrease after the historical perior. Some crops like tubers in some regions show a trend that goes down but the historical data is not clear to show that this is a real decrease, we leave it constant.
    """
    return if_then_else(
        time() <= time_historical_data_land_module(),
        lambda: trends_of_yield_change_r_and_i(),
        lambda: np.maximum(0, trends_of_yield_change_r_and_i()),
    )


@component.add(
    name="average effect of management on crops",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"aux_average_management": 1},
)
def average_effect_of_management_on_crops():
    """
    average management of croplands per region, all land products
    """
    return sum(
        aux_average_management().rename({"LAND PRODUCTS I": "LAND PRODUCTS I!"}),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 4
    )


@component.add(
    name="average share of agriculture in transition",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_agriculture_in_transition": 1},
)
def average_share_of_agriculture_in_transition():
    """
    average share of management in transition per region, all land products
    """
    return sum(
        share_of_agriculture_in_transition().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 3
    )


@component.add(
    name="average share of industrial agriculture",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_industrial_agriculture": 1},
)
def average_share_of_industrial_agriculture():
    return sum(
        share_of_industrial_agriculture().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 3
    )


@component.add(
    name="average share of low input agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_low_input_agriculture": 1},
)
def average_share_of_low_input_agriculture():
    """
    average share of management low input per region, all land products
    """
    return sum(
        share_of_low_input_agriculture().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 3
    )


@component.add(
    name="average share of regenerative agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_regenerative_agriculture": 1},
)
def average_share_of_regenerative_agriculture():
    """
    average share of management regenerative per region, all land products
    """
    return sum(
        share_of_regenerative_agriculture().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 3
    )


@component.add(
    name="average share of traditional agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"share_of_traditional_agriculture": 1},
)
def average_share_of_traditional_agriculture():
    """
    average share of management traditional per region, all land products
    """
    return sum(
        share_of_traditional_agriculture().rename(
            {"LAND PRODUCTS I": "LAND PRODUCTS I!"}
        ),
        dim=["LAND PRODUCTS I!"],
    ) / (
        len(
            xr.DataArray(
                np.arange(1, len(_subscript_dict["LAND PRODUCTS I"]) + 1),
                {"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
                ["LAND PRODUCTS I"],
            )
        )
        - 3
    )


@component.add(
    name="average yields world",
    units="t/(km2*Year)",
    subscripts=["LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"yields_of_crops_all_managements": 1},
)
def average_yields_world():
    return (
        sum(
            yields_of_crops_all_managements().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
            dim=["REGIONS 9 I!"],
        )
        / 9
    )


@component.add(
    name="change to regenerative agriculture sp",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_model_explorer": 1,
        "model_explorer_change_to_regenerative_agriculture": 1,
        "time": 2,
        "year_final_regenerative_agriculture_sp": 2,
        "initial_share_of_regenerative_agriculture": 1,
        "year_initial_regenerative_agriculture_sp": 2,
        "objective_regenerative_agriculture_sp": 1,
        "switch_regenerative_agriculture_sp": 1,
    },
)
def change_to_regenerative_agriculture_sp():
    """
    Change to regenerative agroecological techniques with no dependence on fossil fuel inputs. It is applied to all kinds of managements.
    """
    return if_then_else(
        switch_model_explorer() == 1,
        lambda: model_explorer_change_to_regenerative_agriculture(),
        lambda: if_then_else(
            np.logical_and(
                switch_regenerative_agriculture_sp() == 1,
                np.logical_and(
                    time() > year_initial_regenerative_agriculture_sp(),
                    time() < year_final_regenerative_agriculture_sp(),
                ),
            ).expand_dims({"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1),
            lambda: (
                objective_regenerative_agriculture_sp()
                - initial_share_of_regenerative_agriculture()
            )
            / (
                year_final_regenerative_agriculture_sp()
                - year_initial_regenerative_agriculture_sp()
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                    "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
                },
                ["REGIONS 9 I", "LAND PRODUCTS I"],
            ),
        ),
    )


@component.add(
    name="crop yields impacts ccsm4 model 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_ccsm4_model_rcp_45": 1},
)
def crop_yields_impacts_ccsm4_model_45():
    """
    ccsm4_model_45
    """
    return crop_yields_impacts_data_ccsm4_model_rcp_45(time())


@component.add(
    name="crop yields impacts ccsm4 model 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_ccsm4_model_rcp_85": 1},
)
def crop_yields_impacts_ccsm4_model_85():
    """
    ccsm4_model_85
    """
    return crop_yields_impacts_data_ccsm4_model_rcp_85(time())


@component.add(
    name="CROP YIELDS IMPACTS DATA CCSM4 MODEL RCP 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45",
    },
)
def crop_yields_impacts_data_ccsm4_model_rcp_45(x, final_subs=None):
    """
    CCSM4_MODEL_RCP_45
    """
    return _ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45(x, final_subs)


_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45",
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_4p5",
    "TIME_YIELDS_6",
    "YIELD_IMPACT_CCSM4_4P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="CROP YIELDS IMPACTS DATA CCSM4 MODEL RCP 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85",
    },
)
def crop_yields_impacts_data_ccsm4_model_rcp_85(x, final_subs=None):
    """
    CCSM4_MODEL_RCP_85
    """
    return _ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85(x, final_subs)


_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85",
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_ccsm4_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_ccsm4_8p5",
    "TIME_YIELDS_5",
    "YIELD_IMPACT_CCSM4_8P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="CROP YIELDS IMPACTS DATA GFDL MODEL RCP 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45",
    },
)
def crop_yields_impacts_data_gfdl_model_rcp_45(x, final_subs=None):
    """
    GFDL_MODEL_RCP_45
    """
    return _ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45(x, final_subs)


_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45",
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_4p5",
    "TIME_YIELDS_4",
    "YIELD_IMPACT_GFDL_4P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="CROP YIELDS IMPACTS DATA GFDL MODEL RCP 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85",
    },
)
def crop_yields_impacts_data_gfdl_model_rcp_85(x, final_subs=None):
    """
    GFDL_MODEL_RCP_85
    """
    return _ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85(x, final_subs)


_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85",
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_gfdl_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_gfdl_8p5",
    "TIME_YIELDS_3",
    "YIELD_IMPACT_GFDL_8P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="CROP YIELDS IMPACTS DATA HADGEMES MODEL RCP 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45",
    },
)
def crop_yields_impacts_data_hadgemes_model_rcp_45(x, final_subs=None):
    """
    HADGEMES_MODEL_RCP_45
    """
    return _ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45(x, final_subs)


_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45",
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_45.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_4p5",
    "TIME_YIELDS_2",
    "YIELDS_IMPACTS_HADGEMES_4P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="CROP YIELDS IMPACTS DATA HADGEMES MODEL RCP 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Lookup",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85",
        "__lookup__": "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85",
    },
)
def crop_yields_impacts_data_hadgemes_model_rcp_85(x, final_subs=None):
    """
    HADGEMES_MODEL_RCP_85
    """
    return _ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85(x, final_subs)


_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85 = ExtLookup(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_EU27",
    {"REGIONS 9 I": ["EU27"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
    _root,
    {
        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
        "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
    },
    "_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85",
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_UK",
    {"REGIONS 9 I": ["UK"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_CHINA",
    {"REGIONS 9 I": ["CHINA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_EASOC",
    {"REGIONS 9 I": ["EASOC"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_INDIA",
    {"REGIONS 9 I": ["INDIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_LATAM",
    {"REGIONS 9 I": ["LATAM"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_RUSSIA",
    {"REGIONS 9 I": ["RUSSIA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_USMCA",
    {"REGIONS 9 I": ["USMCA"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)

_ext_lookup_crop_yields_impacts_data_hadgemes_model_rcp_85.add(
    "model_parameters/land_and_water/land_and_water.xlsx",
    "Yield_impact_Hadgemes_8p5",
    "TIME_YIELDS",
    "YIELDS_IMPACTS_HADGEMES_8P5_LROW",
    {"REGIONS 9 I": ["LROW"], "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]},
)


@component.add(
    name="crop yields impacts gfdl model 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_gfdl_model_rcp_45": 1},
)
def crop_yields_impacts_gfdl_model_45():
    """
    gfdl_model_45
    """
    return crop_yields_impacts_data_gfdl_model_rcp_45(time())


@component.add(
    name="crop yields impacts gfdl model 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_gfdl_model_rcp_85": 1},
)
def crop_yields_impacts_gfdl_model_85():
    """
    gfdl_model_85
    """
    return crop_yields_impacts_data_gfdl_model_rcp_85(time())


@component.add(
    name="crop yields impacts hadgemes model 45",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_hadgemes_model_rcp_45": 1},
)
def crop_yields_impacts_hadgemes_model_45():
    """
    hadgemes_model_45
    """
    return crop_yields_impacts_data_hadgemes_model_rcp_45(time())


@component.add(
    name="crop yields impacts hadgemes model 85",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "crop_yields_impacts_data_hadgemes_model_rcp_85": 1},
)
def crop_yields_impacts_hadgemes_model_85():
    """
    hadgemes_model_85
    """
    return crop_yields_impacts_data_hadgemes_model_rcp_85(time())


@component.add(
    name="effect of climate change on crop yields by policy",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_cli2law_cc_effects": 1,
        "switch_climate_change_damage": 1,
        "crop_yields_impacts_gfdl_model_85": 1,
        "crop_yields_impacts_hadgemes_model_45": 1,
        "crop_yields_impacts_ccsm4_model_85": 1,
        "crop_yields_impacts_ccsm4_model_45": 1,
        "crop_yields_impacts_gfdl_model_45": 1,
        "select_climate_model_and_rcp": 6,
        "crop_yields_impacts_hadgemes_model_85": 1,
    },
)
def effect_of_climate_change_on_crop_yields_by_policy():
    """
    effect_of_climate_change_on_crop_yields
    """
    return if_then_else(
        np.logical_or(
            switch_cli2law_cc_effects() == 0, switch_climate_change_damage() == 0
        ),
        lambda: xr.DataArray(
            1,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
        lambda: if_then_else(
            select_climate_model_and_rcp() == 0,
            lambda: crop_yields_impacts_hadgemes_model_85(),
            lambda: if_then_else(
                select_climate_model_and_rcp() == 1,
                lambda: crop_yields_impacts_hadgemes_model_45(),
                lambda: if_then_else(
                    select_climate_model_and_rcp() == 2,
                    lambda: crop_yields_impacts_gfdl_model_85(),
                    lambda: if_then_else(
                        select_climate_model_and_rcp() == 3,
                        lambda: crop_yields_impacts_gfdl_model_45(),
                        lambda: if_then_else(
                            select_climate_model_and_rcp() == 5,
                            lambda: crop_yields_impacts_ccsm4_model_85(),
                            lambda: if_then_else(
                                select_climate_model_and_rcp() == 5,
                                lambda: crop_yields_impacts_ccsm4_model_45(),
                                lambda: xr.DataArray(
                                    0,
                                    {
                                        "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                                        "LAND PRODUCTS I": _subscript_dict[
                                            "LAND PRODUCTS I"
                                        ],
                                    },
                                    ["REGIONS 9 I", "LAND PRODUCTS I"],
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )


@component.add(
    name="effect of irrigation of yield",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"effect_of_irrigation_on_yields": 1},
)
def effect_of_irrigation_of_yield():
    """
    not used
    """
    return effect_of_irrigation_on_yields().transpose("LAND PRODUCTS I", "REGIONS 9 I")


@component.add(
    name="effect of management on crops",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_industrial_agriculture": 1,
        "effect_of_soil_degradation_on_yields": 2,
        "share_of_low_input_agriculture": 1,
        "share_of_agriculture_in_transition": 1,
        "share_of_traditional_agriculture": 1,
        "effect_of_low_input_agriculture": 1,
        "effect_of_regenerative_agriculture": 1,
        "share_of_regenerative_agriculture": 1,
    },
)
def effect_of_management_on_crops():
    """
    Effect of management (traditional, industrial, regeneretive or low input) on agricultura yields.
    """
    return (
        share_of_industrial_agriculture() * effect_of_soil_degradation_on_yields()
        + (
            share_of_agriculture_in_transition()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
        * effect_of_low_input_agriculture()
        * effect_of_soil_degradation_on_yields()
        + share_of_regenerative_agriculture() * effect_of_regenerative_agriculture()
    )


@component.add(
    name="effect of soil degradation on yields",
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_effect_of_soil_degradation_on_yields": 1},
    other_deps={
        "_integ_effect_of_soil_degradation_on_yields": {
            "initial": {},
            "step": {"soil_degradation": 1},
        }
    },
)
def effect_of_soil_degradation_on_yields():
    """
    As stated in FAO The State of the World's Land and Water Resources for Food and Agriculture 2022. "If there is no action to reduce erosion, by 2050, cereal losses are expected to exceed 253 million tonnes (FAO and ITPS, 2015). This is equivalent to removing 1.5 million km2 of land – equal to the total area of arable land in India – from crop production... The extent and impact of land degradation cannot be overemphasized." This is equivalent to the gross loss of 10% of the agricultural production worldwide. This is the asumption of this variable a progresive loss of fertility (instead of loss of cropland itself) unless regenerative techniques are applied
    """
    return _integ_effect_of_soil_degradation_on_yields()


_integ_effect_of_soil_degradation_on_yields = Integ(
    lambda: soil_degradation(), lambda: 1, "_integ_effect_of_soil_degradation_on_yields"
)


@component.add(
    name="EFFECT OF TRADITIONAL AGRICULTURE",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"effect_of_low_input_agriculture": 1},
)
def effect_of_traditional_agriculture():
    return effect_of_low_input_agriculture()


@component.add(
    name="fertilizers demanded",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "chemical_fertilizers_per_cropland_area": 1,
        "average_share_of_industrial_agriculture": 1,
        "land_use_area_by_region": 2,
    },
)
def fertilizers_demanded():
    """
    Fertilizers demanded depending of the type of cropland management (share of industrial agriculture) **NOTES-TODO: potential improvement: demand of fertilizers or fertilizers quantity applied based on type of crop management be better quantified (include more data about management--> excel noelia_marga calibrate "industrial area vs tradictional and agricological?) We could use this information to calibrate Nitrogen demand.
    """
    return (
        chemical_fertilizers_per_cropland_area()
        * average_share_of_industrial_agriculture()
        * (
            land_use_area_by_region().loc[:, "CROPLAND RAINFED"].reset_coords(drop=True)
            + land_use_area_by_region()
            .loc[:, "CROPLAND IRRIGATED"]
            .reset_coords(drop=True)
        )
    )


@component.add(
    name="from industrial to low input agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_effect_oil_and_gas_on_agriculture_sp": 1,
        "time": 2,
        "year_initial_effect_of_oil_and_gas_on_agriculture_sp": 2,
        "year_final_effect_of_oil_and_gas_on_agriculture_sp": 2,
        "share_of_industrial_agriculture": 2,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
        "objective_effect_of_oil_and_gas_on_agriculture_sp": 1,
    },
)
def from_industrial_to_low_input_agriculture():
    """
    change from industrial to low input agriculture
    """
    return if_then_else(
        np.logical_and(
            (switch_effect_oil_and_gas_on_agriculture_sp() == 1),
            np.logical_and(
                (time() > year_initial_effect_of_oil_and_gas_on_agriculture_sp()),
                np.logical_and(
                    (time() < year_final_effect_of_oil_and_gas_on_agriculture_sp()),
                    np.logical_and(
                        share_of_industrial_agriculture() > 0,
                        share_of_industrial_agriculture() < 1,
                    ),
                ),
            ),
        ),
        lambda: zidz(
            objective_effect_of_oil_and_gas_on_agriculture_sp()
            * initial_share_of_industrial_agriculture_r_and_i(),
            (
                year_final_effect_of_oil_and_gas_on_agriculture_sp()
                - year_initial_effect_of_oil_and_gas_on_agriculture_sp()
            ).expand_dims({"LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"]}, 1),
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="from industrial to regenerative agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_industrial_agriculture": 2,
        "share_of_low_input_agriculture": 1,
        "share_of_traditional_agriculture": 1,
    },
)
def from_industrial_to_regenerative_agriculture():
    """
    change from industrial to transition to regenerative agriculture
    """
    return change_to_regenerative_agriculture_sp() * (
        share_of_industrial_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from low input to regenerative agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 2,
        "share_of_traditional_agriculture": 1,
    },
)
def from_low_input_to_regenerative_agriculture():
    """
    change from low input to regenerative agriculture
    """
    return change_to_regenerative_agriculture_sp() * (
        share_of_low_input_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from traditional to industrial agriculture sp",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_industrial_agriculture_sp": 1,
        "time": 2,
        "year_initial_industrial_agriculture_sp": 2,
        "year_final_industrial_agriculture_sp": 2,
        "share_of_traditional_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
        "objective_industrial_agriculture_sp": 1,
    },
)
def from_traditional_to_industrial_agriculture_sp():
    """
    change from traditional to industrial agriculture
    """
    return if_then_else(
        np.logical_and(
            (switch_industrial_agriculture_sp() == 1),
            np.logical_and(
                (time() > year_initial_industrial_agriculture_sp()),
                np.logical_and(
                    (time() < year_final_industrial_agriculture_sp()),
                    share_of_traditional_agriculture() >= 0,
                ),
            ),
        ),
        lambda: np.maximum(
            objective_industrial_agriculture_sp()
            - initial_share_of_traditional_agriculture(),
            0,
        )
        / (
            year_final_industrial_agriculture_sp()
            - year_initial_industrial_agriculture_sp()
        ),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="from traditional to regenerative agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "change_to_regenerative_agriculture_sp": 1,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 1,
        "share_of_traditional_agriculture": 2,
    },
)
def from_traditional_to_regenerative_agriculture():
    """
    change from traditional to regenerative agriculture
    """
    return change_to_regenerative_agriculture_sp() * (
        share_of_traditional_agriculture()
        / (
            share_of_industrial_agriculture()
            + share_of_low_input_agriculture()
            + share_of_traditional_agriculture()
        )
    )


@component.add(
    name="from transition to regenerative agriculture",
    units="DMNL/Year",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_agriculture_in_transition": 1,
        "time_of_transition_to_regenerative_agriculture": 1,
    },
)
def from_transition_to_regenerative_agriculture():
    """
    evolution from transition to regenerative agriculture
    """
    return share_of_agriculture_in_transition() * (
        1 / time_of_transition_to_regenerative_agriculture()
    )


@component.add(
    name="historical yields of crops all managements",
    units="t/(km2*Year)",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "historical_crops_production_fao": 1,
        "historical_area_of_crops_all_management": 1,
    },
)
def historical_yields_of_crops_all_managements():
    """
    historical yields crops all managements FAO data
    """
    return zidz(
        historical_crops_production_fao(time()),
        historical_area_of_crops_all_management(time()),
    )


@component.add(
    name="increase of yields all managements trends",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"trends_of_yield_change_r_and_i": 1},
)
def increase_of_yields_all_managements_trends():
    """
    increment of yields all managements, for testing
    """
    return trends_of_yield_change_r_and_i()


@component.add(
    name="increase of yields industrial R and I",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "yields_industrial_crops_r_and_i": 1,
        "maximum_yields_r_and_i_industrial": 1,
        "aux_trends_of_yield_change_r_and_i": 1,
    },
)
def increase_of_yields_industrial_r_and_i():
    """
    increase of yields mixing irrigated and rainfed crops, estimated past and future trends
    """
    return if_then_else(
        yields_industrial_crops_r_and_i() < maximum_yields_r_and_i_industrial(),
        lambda: aux_trends_of_yield_change_r_and_i(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="increase of yields rainfed industrial",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "yields_rainfed_industrial": 1,
        "maximum_yields_rainfed_industrial": 1,
        "trends_of_industrial_rainfed_yields": 1,
    },
)
def increase_of_yields_rainfed_industrial():
    """
    increase of yields of rainfed industrial crops, estimation. only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return if_then_else(
        yields_rainfed_industrial() < maximum_yields_rainfed_industrial(),
        lambda: trends_of_industrial_rainfed_yields(),
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
            },
            ["REGIONS 9 I", "LAND PRODUCTS I"],
        ),
    )


@component.add(
    name="INITIAL SHARE OF INDUSTRIAL AGRICULTURE R AND I",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_share_of_low_input_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
    },
)
def initial_share_of_industrial_agriculture_r_and_i():
    """
    Initial share of crops production cultivated with industrialized-high input agriculture, rainfed and irrigated mixed
    """
    return np.maximum(
        0,
        1
        - initial_share_of_low_input_agriculture()
        - initial_share_of_regenerative_agriculture()
        - initial_share_of_traditional_agriculture(),
    )


@component.add(
    name="INITIAL YIELDS OF INDUSTRIAL R AND I CROPS",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_yields_all_managements": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
        "effect_of_low_input_agriculture": 1,
    },
)
def initial_yields_of_industrial_r_and_i_crops():
    """
    Initial agricultura yields estimated as if all the crops of the regions were under industrial management
    """
    return initial_yields_all_managements() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="initial yields of industrial rainfed crops",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "initial_yields_all_managements": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "effect_of_irrigation_of_yield": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_share_of_irrigation": 1,
        "initial_time": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
        "effect_of_low_input_agriculture": 1,
    },
)
def initial_yields_of_industrial_rainfed_crops():
    """
    Combined yields based on all managements. They fit the historical values of agregated yields per region (production/area)
    """
    return initial_yields_all_managements() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + (
            initial_share_of_irrigation(initial_time())
            * effect_of_irrigation_of_yield()
        ).transpose("REGIONS 9 I", "LAND PRODUCTS I")
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="land products available all managements trends",
    units="t/Year",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "historical_area_of_crops_all_managements": 1,
        "yields_crops_all_mangements_trends": 1,
    },
)
def land_products_available_all_managements_trends():
    """
    land products, for testing calibration of yileds
    """
    return (
        historical_area_of_crops_all_managements()
        * yields_crops_all_mangements_trends().transpose(
            "LAND PRODUCTS I", "REGIONS 9 I"
        )
    )


@component.add(
    name="percent increase of yields all managements",
    units="DMNL",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "increase_of_yields_all_managements_trends": 1,
        "yields_crops_all_mangements_trends": 1,
    },
)
def percent_increase_of_yields_all_managements():
    """
    percent increase yields, for testing data historical
    """
    return zidz(
        increase_of_yields_all_managements_trends(),
        yields_crops_all_mangements_trends(),
    ).transpose("LAND PRODUCTS I", "REGIONS 9 I")


@component.add(
    name="SELECT CLIMATE MODEL AND RCP",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_select_climate_model_and_rcp"},
)
def select_climate_model_and_rcp():
    """
    0: APPLICATION OF HADGEMES CLIMATE MODEL WITH RCP 8.5 1: APPLICATION OF HADGEMES CLIMATE MODEL WITH RCP 4.5 2: APPLICATION OF GFDL CLIMATE MODEL WITH RCP 8.5 3: APPLICATION OF GFDL CLIMATE MODEL WITH RCP 4.5 4: APPLICATION OF CCSM4 CIMATE MODEL WITH RCP 8.5 5: APPLICATION OF CCSM4 CIMATE MODEL WITH RCP 4.5
    """
    return _ext_constant_select_climate_model_and_rcp()


_ext_constant_select_climate_model_and_rcp = ExtConstant(
    "scenario_parameters/scenario_parameters.xlsx",
    "Land_and_water",
    "SELECT_CLIMATE_MODEL_AND_RCP",
    {},
    _root,
    {},
    "_ext_constant_select_climate_model_and_rcp",
)


@component.add(
    name="share of agriculture in transition",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_agriculture_in_transition": 1},
    other_deps={
        "_integ_share_of_agriculture_in_transition": {
            "initial": {},
            "step": {
                "from_industrial_to_regenerative_agriculture": 1,
                "from_low_input_to_regenerative_agriculture": 1,
                "from_traditional_to_regenerative_agriculture": 1,
                "from_transition_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_agriculture_in_transition():
    """
    share of land in the transition between industrial and regenerative managements
    """
    return _integ_share_of_agriculture_in_transition()


_integ_share_of_agriculture_in_transition = Integ(
    lambda: from_industrial_to_regenerative_agriculture()
    + from_low_input_to_regenerative_agriculture()
    + from_traditional_to_regenerative_agriculture()
    - from_transition_to_regenerative_agriculture(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "LAND PRODUCTS I": _subscript_dict["LAND PRODUCTS I"],
        },
        ["REGIONS 9 I", "LAND PRODUCTS I"],
    ),
    "_integ_share_of_agriculture_in_transition",
)


@component.add(
    name="share of industrial agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_industrial_agriculture": 1},
    other_deps={
        "_integ_share_of_industrial_agriculture": {
            "initial": {"initial_share_of_industrial_agriculture_r_and_i": 1},
            "step": {
                "from_traditional_to_industrial_agriculture_sp": 1,
                "from_industrial_to_regenerative_agriculture": 1,
                "from_industrial_to_low_input_agriculture": 1,
            },
        }
    },
)
def share_of_industrial_agriculture():
    """
    share of crops production cultivated with industrialized-high input agriculture
    """
    return _integ_share_of_industrial_agriculture()


_integ_share_of_industrial_agriculture = Integ(
    lambda: from_traditional_to_industrial_agriculture_sp()
    - from_industrial_to_regenerative_agriculture()
    - from_industrial_to_low_input_agriculture(),
    lambda: initial_share_of_industrial_agriculture_r_and_i(),
    "_integ_share_of_industrial_agriculture",
)


@component.add(
    name="share of low input agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_low_input_agriculture": 1},
    other_deps={
        "_integ_share_of_low_input_agriculture": {
            "initial": {"initial_share_of_low_input_agriculture": 1},
            "step": {
                "from_industrial_to_low_input_agriculture": 1,
                "from_low_input_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_low_input_agriculture():
    """
    Share of agriculture under management based on low input of fertilizers and agrochemicals. It is used to simulate oil and gas shortage effects on agriculture. Its yields are similar to traditional agriculture.
    """
    return _integ_share_of_low_input_agriculture()


_integ_share_of_low_input_agriculture = Integ(
    lambda: from_industrial_to_low_input_agriculture()
    - from_low_input_to_regenerative_agriculture(),
    lambda: initial_share_of_low_input_agriculture(),
    "_integ_share_of_low_input_agriculture",
)


@component.add(
    name="share of regenerative agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_regenerative_agriculture": 1},
    other_deps={
        "_integ_share_of_regenerative_agriculture": {
            "initial": {"initial_share_of_regenerative_agriculture": 1},
            "step": {"from_transition_to_regenerative_agriculture": 1},
        }
    },
)
def share_of_regenerative_agriculture():
    """
    INITIAL_SHARE_OF_REGENERATIVE_AGRICULTURE, regenerative is the land under advanced agroecological methods with no use of agrochemical inputs
    """
    return _integ_share_of_regenerative_agriculture()


_integ_share_of_regenerative_agriculture = Integ(
    lambda: from_transition_to_regenerative_agriculture(),
    lambda: initial_share_of_regenerative_agriculture(),
    "_integ_share_of_regenerative_agriculture",
)


@component.add(
    name="share of traditional agriculture",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_share_of_traditional_agriculture": 1},
    other_deps={
        "_integ_share_of_traditional_agriculture": {
            "initial": {"initial_share_of_traditional_agriculture": 1},
            "step": {
                "from_traditional_to_industrial_agriculture_sp": 1,
                "from_traditional_to_regenerative_agriculture": 1,
            },
        }
    },
)
def share_of_traditional_agriculture():
    """
    Share of agriculture under traditional agricultural methods with low input of fertilizers and agrochemicals, low yields and labor intensive.
    """
    return _integ_share_of_traditional_agriculture()


_integ_share_of_traditional_agriculture = Integ(
    lambda: -from_traditional_to_industrial_agriculture_sp()
    - from_traditional_to_regenerative_agriculture(),
    lambda: initial_share_of_traditional_agriculture(),
    "_integ_share_of_traditional_agriculture",
)


@component.add(
    name="soil degradation",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "time_historical_data_land_module": 2},
)
def soil_degradation():
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: 0,
        lambda: -0.1 / (2050 - time_historical_data_land_module()),
    )


@component.add(
    name="sum of all agriculture share",
    units="DMNL",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_of_agriculture_in_transition": 1,
        "share_of_industrial_agriculture": 1,
        "share_of_low_input_agriculture": 1,
        "share_of_regenerative_agriculture": 1,
        "share_of_traditional_agriculture": 1,
    },
)
def sum_of_all_agriculture_share():
    """
    check summ of all shares of management
    """
    return (
        share_of_agriculture_in_transition()
        + share_of_industrial_agriculture()
        + share_of_low_input_agriculture()
        + share_of_regenerative_agriculture()
        + share_of_traditional_agriculture()
    )


@component.add(
    name="SWITCH CLI2LAW CC EFFECTS",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_switch_cli2law_cc_effects"},
)
def switch_cli2law_cc_effects():
    """
    if =0 not activated the effect of climate change on crop yields, 1= activated
    """
    return _ext_constant_switch_cli2law_cc_effects()


_ext_constant_switch_cli2law_cc_effects = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_CLI2LAW_CC_EFFECTS",
    {},
    _root,
    {},
    "_ext_constant_switch_cli2law_cc_effects",
)


@component.add(
    name="trends of industrial rainfed yields",
    units="t/(km2*Year*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "trends_of_yield_change_r_and_i": 1,
        "effect_of_regenerative_agriculture": 1,
        "initial_share_of_regenerative_agriculture": 1,
        "effect_of_irrigation_of_yield": 1,
        "initial_share_of_traditional_agriculture": 1,
        "initial_share_of_irrigation": 1,
        "initial_time": 1,
        "initial_share_of_industrial_agriculture_r_and_i": 1,
        "effect_of_low_input_agriculture": 1,
    },
)
def trends_of_industrial_rainfed_yields():
    """
    Estimated trends of evolution of the industrial rainfed cultivation. Only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return trends_of_yield_change_r_and_i() / (
        initial_share_of_industrial_agriculture_r_and_i()
        + (
            initial_share_of_irrigation(initial_time())
            * effect_of_irrigation_of_yield()
        ).transpose("REGIONS 9 I", "LAND PRODUCTS I")
        + initial_share_of_traditional_agriculture() * effect_of_low_input_agriculture()
        + initial_share_of_regenerative_agriculture()
        * effect_of_regenerative_agriculture()
    )


@component.add(
    name="yields crops all mangements trends",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_crops_all_mangements_trends": 1},
    other_deps={
        "_integ_yields_crops_all_mangements_trends": {
            "initial": {"initial_time": 1, "historical_yields_fao": 1},
            "step": {"increase_of_yields_all_managements_trends": 1},
        }
    },
)
def yields_crops_all_mangements_trends():
    """
    yields all managements, for testing historical fit
    """
    return _integ_yields_crops_all_mangements_trends()


_integ_yields_crops_all_mangements_trends = Integ(
    lambda: increase_of_yields_all_managements_trends(),
    lambda: historical_yields_fao(initial_time()).transpose(
        "REGIONS 9 I", "LAND PRODUCTS I"
    ),
    "_integ_yields_crops_all_mangements_trends",
)


@component.add(
    name="yields FAO",
    units="t/(km2*Year)",
    subscripts=["LAND PRODUCTS I", "REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "historical_yields_fao": 1},
)
def yields_fao():
    """
    historical yields, FAO data, all managements
    """
    return historical_yields_fao(time())


@component.add(
    name="yields industrial crops R and I",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_industrial_crops_r_and_i": 1},
    other_deps={
        "_integ_yields_industrial_crops_r_and_i": {
            "initial": {"initial_yields_of_industrial_r_and_i_crops": 1},
            "step": {"increase_of_yields_industrial_r_and_i": 1},
        }
    },
)
def yields_industrial_crops_r_and_i():
    """
    Yields of crops cultivated with industrialized-high input agriculture. Historical trends of evolution (lineal fit) and estimated evolution. Yields continue trends of growth until they reach the limit only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=1
    """
    return _integ_yields_industrial_crops_r_and_i()


_integ_yields_industrial_crops_r_and_i = Integ(
    lambda: increase_of_yields_industrial_r_and_i(),
    lambda: initial_yields_of_industrial_r_and_i_crops(),
    "_integ_yields_industrial_crops_r_and_i",
)


@component.add(
    name="yields of crops all managements",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "time_historical_data_land_module": 1,
        "yields_fao": 1,
        "yields_industrial_crops_r_and_i": 1,
        "effect_of_climate_change_on_crop_yields_by_policy": 1,
        "effect_of_management_on_crops": 1,
    },
)
def yields_of_crops_all_managements():
    """
    Agricultural yields. It combines the effect of the change of management (traditional, industrial, regenerative, etc.) used when SWITCH_SEPARATE_IRRIGATED_RAINFED=1
    """
    return if_then_else(
        time() < time_historical_data_land_module(),
        lambda: yields_fao(),
        lambda: (
            yields_industrial_crops_r_and_i()
            * effect_of_management_on_crops()
            * effect_of_climate_change_on_crop_yields_by_policy()
        ).transpose("LAND PRODUCTS I", "REGIONS 9 I"),
    ).transpose("REGIONS 9 I", "LAND PRODUCTS I")


@component.add(
    name="yields of irrigated crops",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "yields_rainfed_industrial": 1,
        "effect_of_irrigation_of_yield": 1,
        "effect_of_management_on_crops": 1,
    },
)
def yields_of_irrigated_crops():
    """
    yields of irrigated crops only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return (
        yields_rainfed_industrial()
        * effect_of_irrigation_of_yield().transpose("REGIONS 9 I", "LAND PRODUCTS I")
        * effect_of_management_on_crops()
    )


@component.add(
    name="yields of rainfed crops",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"yields_rainfed_industrial": 1, "effect_of_management_on_crops": 1},
)
def yields_of_rainfed_crops():
    """
    yields of rainfed crops only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return yields_rainfed_industrial() * effect_of_management_on_crops()


@component.add(
    name="yields rainfed industrial",
    units="t/(km2*Year)",
    subscripts=["REGIONS 9 I", "LAND PRODUCTS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_yields_rainfed_industrial": 1},
    other_deps={
        "_integ_yields_rainfed_industrial": {
            "initial": {"initial_yields_of_industrial_rainfed_crops": 1},
            "step": {"increase_of_yields_rainfed_industrial": 1},
        }
    },
)
def yields_rainfed_industrial():
    """
    yields of rainfed industrial crops, estimation. only used when SWITCH_SEPARATE_IRRIGATED_RAINFED=0
    """
    return _integ_yields_rainfed_industrial()


_integ_yields_rainfed_industrial = Integ(
    lambda: increase_of_yields_rainfed_industrial(),
    lambda: initial_yields_of_industrial_rainfed_crops(),
    "_integ_yields_rainfed_industrial",
)
