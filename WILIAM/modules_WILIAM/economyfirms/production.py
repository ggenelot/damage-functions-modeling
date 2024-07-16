"""
Module economyfirms.production
Translated using PySD version 3.14.0
"""

@component.add(
    name="change technical coefficients",
    units="DMNL",
    subscripts=["REGIONS 36 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "time": 5,
        "switch_economy": 5,
        "switch_nrg2eco_a_matrix_energy_intensities": 1,
        "energy_intensities_variation_economic_module_classification": 1,
        "material_intensities_variation": 4,
        "switch_mat2eco_a_matrix_material_intensity": 4,
    },
)
def change_technical_coefficients():
    """
    Change in technical coefficients.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
        },
        ["REGIONS 36 I", "SECTORS I", "SECTORS MAP I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[_subscript_dict["REGIONS 35 I"], :, :] = True
    except_subs.loc[
        _subscript_dict["REGIONS 35 I"], _subscript_dict["SECTORS FINAL ENERGY I"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS 35 I"], ["MINING AND MANUFACTURING COPPER"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS 35 I"], ["MINING AND MANUFACTURING ALUMINIUM"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS 35 I"], ["MINING AND MANUFACTURING IRON"], :
    ] = False
    except_subs.loc[
        _subscript_dict["REGIONS 35 I"], ["MINING AND MANUFACTURING NICKEL"], :
    ] = False
    value.values[except_subs.values] = 0
    value.loc[
        _subscript_dict["REGIONS 35 I"], _subscript_dict["SECTORS FINAL ENERGY I"], :
    ] = if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
                "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
            },
            ["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS MAP I"],
        ),
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_nrg2eco_a_matrix_energy_intensities() == 0
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
                    "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
                },
                ["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS MAP I"],
            ),
            lambda: energy_intensities_variation_economic_module_classification().rename(
                {"SECTORS I": "SECTORS MAP I"}
            ),
        ),
    ).values
    value.loc[:, ["MINING AND MANUFACTURING COPPER"], :] = if_then_else(
        time() <= 2015,
        lambda: 0,
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_mat2eco_a_matrix_material_intensity() == 0
            ),
            lambda: 0,
            lambda: float(material_intensities_variation().loc["Cu W"]),
        ),
    )
    value.loc[:, ["MINING AND MANUFACTURING ALUMINIUM"], :] = if_then_else(
        time() <= 2015,
        lambda: 0,
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_mat2eco_a_matrix_material_intensity() == 0
            ),
            lambda: 0,
            lambda: float(material_intensities_variation().loc["Al W"]),
        ),
    )
    value.loc[:, ["MINING AND MANUFACTURING IRON"], :] = if_then_else(
        time() <= 2015,
        lambda: 0,
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_mat2eco_a_matrix_material_intensity() == 0
            ),
            lambda: 0,
            lambda: float(material_intensities_variation().loc["Fe W"]),
        ),
    )
    value.loc[:, ["MINING AND MANUFACTURING NICKEL"], :] = if_then_else(
        time() <= 2015,
        lambda: 0,
        lambda: if_then_else(
            np.logical_or(
                switch_economy() == 0, switch_mat2eco_a_matrix_material_intensity() == 0
            ),
            lambda: 0,
            lambda: float(material_intensities_variation().loc["Ni W"]),
        ),
    )
    return value


@component.add(
    name="delayed TS 2 final energy intensities by sector and FE",
    units="TJ/million$/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={
        "_delayfixed_delayed_ts_2_final_energy_intensities_by_sector_and_fe": 1
    },
    other_deps={
        "_delayfixed_delayed_ts_2_final_energy_intensities_by_sector_and_fe": {
            "initial": {"time_step": 1},
            "step": {"delayed_ts_final_energy_intensities_by_sector_and_fe": 1},
        }
    },
)
def delayed_ts_2_final_energy_intensities_by_sector_and_fe():
    """
    Delated (2 Time step) final energy intensities by sector and final energy estimated with a top-down approach.
    """
    return _delayfixed_delayed_ts_2_final_energy_intensities_by_sector_and_fe()


_delayfixed_delayed_ts_2_final_energy_intensities_by_sector_and_fe = DelayFixed(
    lambda: delayed_ts_final_energy_intensities_by_sector_and_fe(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_2_final_energy_intensities_by_sector_and_fe",
)


@component.add(
    name="delayed TS final energy intensities by sector and FE",
    units="TJ/million$/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Stateful, Constant",
    comp_subtype="Normal, DelayFixed",
    depends_on={"_delayfixed_delayed_ts_final_energy_intensities_by_sector_and_fe": 1},
    other_deps={
        "_delayfixed_delayed_ts_final_energy_intensities_by_sector_and_fe": {
            "initial": {"time_step": 1},
            "step": {"final_energy_intensities_by_sector_and_fe": 1},
        }
    },
)
def delayed_ts_final_energy_intensities_by_sector_and_fe():
    """
    Delated (Time step) final energy intensities by sector and final energy estimated with a top-down approach.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    )
    value.loc[:, _subscript_dict["SECTORS NON ENERGY I"], :] = (
        _delayfixed_delayed_ts_final_energy_intensities_by_sector_and_fe().values
    )
    value.loc[:, _subscript_dict["SECTORS ENERGY I"], :] = 0
    return value


_delayfixed_delayed_ts_final_energy_intensities_by_sector_and_fe = DelayFixed(
    lambda: final_energy_intensities_by_sector_and_fe(),
    lambda: time_step(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS NON ENERGY I": _subscript_dict["SECTORS NON ENERGY I"],
            "NRG FE I": _subscript_dict["NRG FE I"],
        },
        ["REGIONS 35 I", "SECTORS NON ENERGY I", "NRG FE I"],
    ),
    time_step,
    "_delayfixed_delayed_ts_final_energy_intensities_by_sector_and_fe",
)


@component.add(
    name="delayed TS output real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_output_real": 1},
    other_deps={
        "_delayfixed_delayed_ts_output_real": {
            "initial": {"base_output_real": 1, "time_step": 1},
            "step": {"time": 1, "base_output_real": 1, "output_real": 1},
        }
    },
)
def delayed_ts_output_real():
    """
    Delayed production in basic prices and real terms.
    """
    return _delayfixed_delayed_ts_output_real()


_delayfixed_delayed_ts_output_real = DelayFixed(
    lambda: if_then_else(
        time() <= 2015, lambda: base_output_real(), lambda: output_real()
    ),
    lambda: time_step(),
    lambda: base_output_real(),
    time_step,
    "_delayfixed_delayed_ts_output_real",
)


@component.add(
    name="delayed TS technical coefficients total",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_technical_coefficients_total": 1},
    other_deps={
        "_delayfixed_delayed_ts_technical_coefficients_total": {
            "initial": {
                "initial_delayed_technical_coefficients_total": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "initial_delayed_technical_coefficients_total": 1,
                "technical_coefficients_total": 1,
            },
        }
    },
)
def delayed_ts_technical_coefficients_total():
    """
    Delayed technical coeffcients: total
    """
    return _delayfixed_delayed_ts_technical_coefficients_total()


_delayfixed_delayed_ts_technical_coefficients_total = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_delayed_technical_coefficients_total(),
        lambda: technical_coefficients_total(),
    ),
    lambda: time_step(),
    lambda: initial_delayed_technical_coefficients_total(),
    time_step,
    "_delayfixed_delayed_ts_technical_coefficients_total",
)


@component.add(
    name="delayed TS total intermediate exports real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_total_intermediate_exports_real": 1},
    other_deps={
        "_delayfixed_delayed_ts_total_intermediate_exports_real": {
            "initial": {
                "sum_initial_total_intermediate_exports_real": 1,
                "time_step": 1,
            },
            "step": {
                "time": 1,
                "sum_initial_total_intermediate_exports_real": 1,
                "total_intermediate_exports_real": 1,
            },
        }
    },
)
def delayed_ts_total_intermediate_exports_real():
    """
    Delayed total intermediate exports in real terms.
    """
    return _delayfixed_delayed_ts_total_intermediate_exports_real()


_delayfixed_delayed_ts_total_intermediate_exports_real = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: sum_initial_total_intermediate_exports_real(),
        lambda: total_intermediate_exports_real(),
    ),
    lambda: time_step(),
    lambda: sum_initial_total_intermediate_exports_real(),
    time_step,
    "_delayfixed_delayed_ts_total_intermediate_exports_real",
)


@component.add(
    name="energy intensities variation economic module classification",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={"energy_intensity_variation": 6},
)
def energy_intensities_variation_economic_module_classification():
    """
    Change in energy intensities in economic classification. COKE, SOLID BIOMASS are missing.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS FINAL ENERGY I": _subscript_dict["SECTORS FINAL ENERGY I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 35 I", "SECTORS FINAL ENERGY I", "SECTORS I"],
    )
    value.loc[:, ["REFINING"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE liquid"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER REFINERY": _subscript_dict["CLUSTER REFINERY"]}, 1)
        .values
    )
    value.loc[:, ["MINING COAL"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE solid fossil"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER MINNING": ["MINING COAL"]}, 1)
        .values
    )
    value.loc[:, ["COKE"], :] = 0
    value.loc[:, ["DISTRIBUTION ELECTRICITY"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE elec"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "CLUSTER ELECTRICITY TRANSPORT": _subscript_dict[
                    "CLUSTER ELECTRICITY TRANSPORT"
                ]
            },
            1,
        )
        .values
    )
    value.loc[:, ["DISTRIBUTION GAS"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE gas"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["DISTRIBUTION GAS"]}, 1)
        .values
    )
    value.loc[:, ["STEAM HOT WATER"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE heat"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER OTHER ENERGY ACTIVITIES": ["STEAM HOT WATER"]}, 1)
        .values
    )
    value.loc[:, ["HYDROGEN PRODUCTION"], :] = (
        energy_intensity_variation()
        .loc[:, :, "FE hydrogen"]
        .reset_coords(drop=True)
        .expand_dims({"CLUSTER HYDROGEN": _subscript_dict["CLUSTER HYDROGEN"]}, 1)
        .values
    )
    return value


@component.add(
    name="energy intensity variation",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "NRG FE I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 1,
        "delayed_ts_2_final_energy_intensities_by_sector_and_fe": 2,
        "delayed_ts_final_energy_intensities_by_sector_and_fe": 2,
    },
)
def energy_intensity_variation():
    """
    Energy intensity growth by time step.
    """
    return if_then_else(
        time() <= 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "SECTORS I": _subscript_dict["SECTORS I"],
                "NRG FE I": _subscript_dict["NRG FE I"],
            },
            ["REGIONS 35 I", "SECTORS I", "NRG FE I"],
        ),
        lambda: if_then_else(
            np.logical_or(
                delayed_ts_2_final_energy_intensities_by_sector_and_fe() == 0,
                delayed_ts_final_energy_intensities_by_sector_and_fe() == 0,
            ),
            lambda: xr.DataArray(
                0,
                {
                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                    "SECTORS I": _subscript_dict["SECTORS I"],
                    "NRG FE I": _subscript_dict["NRG FE I"],
                },
                ["REGIONS 35 I", "SECTORS I", "NRG FE I"],
            ),
            lambda: zidz(
                delayed_ts_final_energy_intensities_by_sector_and_fe(),
                delayed_ts_2_final_energy_intensities_by_sector_and_fe(),
            )
            - 1,
        ),
    )


@component.add(
    name="final exports real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"final_demand_imports_in_basic_prices_real": 1},
)
def final_exports_real():
    """
    Final exports in basic prices and real terms.
    """
    return sum(
        final_demand_imports_in_basic_prices_real().rename(
            {
                "REGIONS 35 MAP I": "REGIONS 35 MAP I!",
                "FINAL DEMAND I": "FINAL DEMAND I!",
            }
        ),
        dim=["REGIONS 35 MAP I!", "FINAL DEMAND I!"],
    )


@component.add(
    name="identity minus technical coefficients domestic",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"identity_matrix": 1, "technical_coefficients_domestic": 1},
)
def identity_minus_technical_coefficients_domestic():
    """
    Leomntief matrix: Identity matrix minus matrix of technical coeffcients.
    """
    return (
        identity_matrix()
        - technical_coefficients_domestic().transpose(
            "SECTORS I", "SECTORS MAP I", "REGIONS 35 I"
        )
    ).transpose("REGIONS 35 I", "SECTORS I", "SECTORS MAP I")


@component.add(
    name="intermediate imports and exports real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_import": 1, "output_real": 1},
)
def intermediate_imports_and_exports_real():
    """
    Total intermediate exports and imports in real terms.
    """
    return technical_coefficients_import().rename(
        {"REGIONS 35 MAP I": "REGIONS 35 I", "REGIONS 35 I": "REGIONS 35 MAP I"}
    ) * output_real().rename(
        {"REGIONS 35 I": "REGIONS 35 MAP I", "SECTORS I": "SECTORS MAP I"}
    )


@component.add(
    name="intermediates domestic real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "technical_coefficients_domestic": 1},
)
def intermediates_domestic_real():
    """
    Demand of domestic intermediate goods in basic prices and real terms.
    """
    return (
        output_real().rename({"SECTORS I": "SECTORS MAP I"})
        * technical_coefficients_domestic().transpose(
            "REGIONS 35 I", "SECTORS MAP I", "SECTORS I"
        )
    ).transpose("REGIONS 35 I", "SECTORS I", "SECTORS MAP I")


@component.add(
    name="intermediates total real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"technical_coefficients_total": 1, "output_real": 1},
)
def intermediates_total_real():
    """
    Total demand intermediates in real terms
    """
    return technical_coefficients_total() * output_real().rename(
        {"SECTORS I": "SECTORS MAP I"}
    )


@component.add(
    name="leontief inverse",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "identity_minus_technical_coefficients_domestic": 1,
        "year_compute_leontief_inverse": 1,
    },
)
def leontief_inverse():
    """
    Leontief inverse matrix.
    """
    return invert_matrix(identity_minus_technical_coefficients_domestic())


@component.add(
    name="output real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"leontief_inverse": 1, "total_demand_domestic_produced_goods_real": 1},
)
def output_real():
    """
    Total production by sector in basic prices and real terms.
    """
    return sum(
        leontief_inverse().rename({"SECTORS MAP I": "SECTORS MAP I!"})
        * total_demand_domestic_produced_goods_real().rename(
            {"SECTORS I": "SECTORS MAP I!"}
        ),
        dim=["SECTORS MAP I!"],
    )


@component.add(
    name="output real 9R",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 9 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1, "output_real_eu27": 1},
)
def output_real_9r():
    """
    Total production by sector in basic prices and real terms: 9 regions
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
        },
        ["REGIONS 9 I", "SECTORS I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = (
        output_real()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 35 I": "REGIONS 8 I"})
        .values
    )
    value.loc[["EU27"], :] = (
        output_real_eu27().expand_dims({"REGIONS 36 I": ["EU27"]}, 0).values
    )
    return value


@component.add(
    name="output real EU27",
    units="Mdollars 2015/Year",
    subscripts=["SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"output_real": 1},
)
def output_real_eu27():
    """
    Total production by sector in basic prices and real terms: EU27
    """
    return sum(
        output_real()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )


@component.add(
    name="SWITCH MAT2ECO A MATRIX MATERIAL INTENSITY",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_mat2eco_a_matrix_material_intensity"
    },
)
def switch_mat2eco_a_matrix_material_intensity():
    """
    This switch can take two values: 0: Material input intensity coefficient do not change with changes in material intensities. 1: Material input intensity coefficient change with changes in material intensities.
    """
    return _ext_constant_switch_mat2eco_a_matrix_material_intensity()


_ext_constant_switch_mat2eco_a_matrix_material_intensity = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_MAT2ECO_A_MATRIX_MATERIAL_INTENSITY",
    {},
    _root,
    {},
    "_ext_constant_switch_mat2eco_a_matrix_material_intensity",
)


@component.add(
    name="SWITCH NRG2ECO A MATRIX ENERGY INTENSITIES",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={
        "__external__": "_ext_constant_switch_nrg2eco_a_matrix_energy_intensities"
    },
)
def switch_nrg2eco_a_matrix_energy_intensities():
    """
    SWICHT values: 0: Final energy input coefficients do not change with the variation in sectoral final energy intensities 1: Final energy input coefficients change with the variation of sectoral final energy intensities
    """
    return _ext_constant_switch_nrg2eco_a_matrix_energy_intensities()


_ext_constant_switch_nrg2eco_a_matrix_energy_intensities = ExtConstant(
    "scenario_parameters/switches.xlsx",
    "SWITCHES",
    "SWITCH_NRG2ECO_A_MATRIX_ENERGY_INTENSITIES",
    {},
    _root,
    {},
    "_ext_constant_switch_nrg2eco_a_matrix_energy_intensities",
)


@component.add(
    name="technical coefficients domestic",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "technical_coefficients_total": 1,
        "import_shares_intermediates_constrained": 1,
        "initial_import_shares_intermediates": 1,
        "switch_eco_trade": 1,
    },
)
def technical_coefficients_domestic():
    """
    Technical coeffcients: domestic. Domestic intermediate inputs required to produce one unit of output.
    """
    return technical_coefficients_total() * (
        1
        - if_then_else(
            switch_eco_trade() == 0,
            lambda: initial_import_shares_intermediates(),
            lambda: import_shares_intermediates_constrained(),
        )
    )


@component.add(
    name="technical coefficients import",
    units="DMNL",
    subscripts=["REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_eco_trade": 1,
        "initial_import_shares_intermediates": 1,
        "import_shares_intermediates_constrained": 1,
        "technical_coefficients_total": 1,
        "import_shares_origin_intermediates": 1,
    },
)
def technical_coefficients_import():
    """
    Technical coefficients: imports. Imported intermediate inputs required to produce one unit of output.
    """
    return (
        if_then_else(
            switch_eco_trade() == 0,
            lambda: initial_import_shares_intermediates(),
            lambda: import_shares_intermediates_constrained(),
        )
        * (
            technical_coefficients_total()
            * import_shares_origin_intermediates().transpose(
                "REGIONS 35 I", "SECTORS I", "SECTORS MAP I", "REGIONS 35 MAP I"
            )
        )
    ).transpose("REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "SECTORS MAP I")


@component.add(
    name="technical coefficients total",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "delayed_ts_technical_coefficients_total": 1,
        "change_technical_coefficients": 1,
    },
)
def technical_coefficients_total():
    """
    Technical coefficients: total. Total intermediate inputs required to produce one unit of output.
    """
    return delayed_ts_technical_coefficients_total() * (
        1
        + change_technical_coefficients()
        .loc[_subscript_dict["REGIONS 35 I"], :, :]
        .rename({"REGIONS 36 I": "REGIONS 35 I"})
    )


@component.add(
    name="total demand domestic produced goods real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_final_demand_domestic_produced_goods_basic_prices_real": 1,
        "delayed_ts_total_intermediate_exports_real": 1,
    },
)
def total_demand_domestic_produced_goods_real():
    """
    Total demand including exports of intermediate goods in real terms.
    """
    return (
        total_final_demand_domestic_produced_goods_basic_prices_real()
        + delayed_ts_total_intermediate_exports_real()
    )


@component.add(
    name="total final demand domestic produced goods basic prices real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_domestic_in_basic_prices_real": 1,
        "final_exports_real": 1,
    },
)
def total_final_demand_domestic_produced_goods_basic_prices_real():
    """
    Total final demand of domestic produced goods in basic prices and real terms.
    """
    return (
        sum(
            final_demand_domestic_in_basic_prices_real().rename(
                {"FINAL DEMAND I": "FINAL DEMAND I!"}
            ),
            dim=["FINAL DEMAND I!"],
        )
        + final_exports_real()
    )


@component.add(
    name="total intermediate exports real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"intermediate_imports_and_exports_real": 1},
)
def total_intermediate_exports_real():
    """
    Total intermediate exports in real terms.
    """
    return sum(
        intermediate_imports_and_exports_real().rename(
            {"REGIONS 35 MAP I": "REGIONS 35 MAP I!", "SECTORS MAP I": "SECTORS MAP I!"}
        ),
        dim=["REGIONS 35 MAP I!", "SECTORS MAP I!"],
    )


@component.add(
    name="total intermediate imports real",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 MAP I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"intermediate_imports_and_exports_real": 1},
)
def total_intermediate_imports_real():
    """
    Total intermediate imports in real terms.
    """
    return sum(
        intermediate_imports_and_exports_real().rename(
            {"REGIONS 35 I": "REGIONS 35 I!", "SECTORS I": "SECTORS I!"}
        ),
        dim=["REGIONS 35 I!", "SECTORS I!"],
    )


@component.add(
    name="year compute leontief inverse",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 2},
)
def year_compute_leontief_inverse():
    return if_then_else(time() == integer(time()), lambda: 62, lambda: 0)
