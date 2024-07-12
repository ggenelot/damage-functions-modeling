"""
Module economytrade
Translated using PySD version 3.14.0
"""

@component.add(
    name="delayed TS import shares final demand",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_import_shares_final_demand": 1},
    other_deps={
        "_delayfixed_delayed_ts_import_shares_final_demand": {
            "initial": {"initial_import_shares_final_demand": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_import_shares_final_demand": 1,
                "import_shares_final_demand_constrained": 1,
            },
        }
    },
)
def delayed_ts_import_shares_final_demand():
    """
    Delayed import shares for final demand
    """
    return _delayfixed_delayed_ts_import_shares_final_demand()


_delayfixed_delayed_ts_import_shares_final_demand = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_import_shares_final_demand(),
        lambda: import_shares_final_demand_constrained(),
    ),
    lambda: time_step(),
    lambda: initial_import_shares_final_demand(),
    time_step,
    "_delayfixed_delayed_ts_import_shares_final_demand",
)


@component.add(
    name="delayed TS import shares intermediates",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Stateful",
    comp_subtype="DelayFixed",
    depends_on={"_delayfixed_delayed_ts_import_shares_intermediates": 1},
    other_deps={
        "_delayfixed_delayed_ts_import_shares_intermediates": {
            "initial": {"initial_import_shares_intermediates": 1, "time_step": 1},
            "step": {
                "time": 1,
                "initial_import_shares_intermediates": 1,
                "import_shares_intermediates_constrained": 1,
            },
        }
    },
)
def delayed_ts_import_shares_intermediates():
    """
    Delayed import shares for intermediates
    """
    return _delayfixed_delayed_ts_import_shares_intermediates()


_delayfixed_delayed_ts_import_shares_intermediates = DelayFixed(
    lambda: if_then_else(
        time() <= 2015,
        lambda: initial_import_shares_intermediates(),
        lambda: import_shares_intermediates_constrained(),
    ),
    lambda: time_step(),
    lambda: initial_import_shares_intermediates(),
    time_step,
    "_delayfixed_delayed_ts_import_shares_intermediates",
)


@component.add(
    name="import shares final demand",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fixed_import_shares": 1,
        "initial_import_shares_final_demand": 2,
        "beta_import_shares_final_demand": 1,
        "delayed_ts_price_ratio_households": 1,
        "epsilon_import_shares_final_demand": 1,
        "delayed_ts_import_shares_final_demand": 4,
        "constant_import_shares_final_demand": 1,
    },
)
def import_shares_final_demand():
    """
    Import shares for final demand
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "FINAL DEMAND I": _subscript_dict["FINAL DEMAND I"],
        },
        ["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    )
    value.loc[:, :, ["CONSUMPTION W"]] = (
        if_then_else(
            switch_fixed_import_shares() == 0,
            lambda: initial_import_shares_final_demand()
            .loc[:, :, "CONSUMPTION W"]
            .reset_coords(drop=True),
            lambda: np.minimum(
                1,
                np.maximum(
                    0,
                    if_then_else(
                        delayed_ts_import_shares_final_demand()
                        .loc[:, :, "CONSUMPTION W"]
                        .reset_coords(drop=True)
                        == 1,
                        lambda: xr.DataArray(
                            1,
                            {
                                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                                "SECTORS I": _subscript_dict["SECTORS I"],
                            },
                            ["REGIONS 35 I", "SECTORS I"],
                        ),
                        lambda: if_then_else(
                            delayed_ts_import_shares_final_demand()
                            .loc[:, :, "CONSUMPTION W"]
                            .reset_coords(drop=True)
                            == 0,
                            lambda: xr.DataArray(
                                0,
                                {
                                    "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                                    "SECTORS I": _subscript_dict["SECTORS I"],
                                },
                                ["REGIONS 35 I", "SECTORS I"],
                            ),
                            lambda: (
                                1
                                - delayed_ts_import_shares_final_demand()
                                .loc[:, :, "CONSUMPTION W"]
                                .reset_coords(drop=True)
                                + 1e-07
                            )
                            * np.exp(
                                constant_import_shares_final_demand()
                                .loc[:, :, "CONSUMPTION W"]
                                .reset_coords(drop=True)
                                + (
                                    beta_import_shares_final_demand()
                                    .loc[:, "CONSUMPTION W"]
                                    .reset_coords(drop=True)
                                    * np.log(
                                        delayed_ts_import_shares_final_demand()
                                        .loc[:, :, "CONSUMPTION W"]
                                        .reset_coords(drop=True)
                                        + 1e-07
                                    ).transpose("SECTORS I", "REGIONS 35 I")
                                ).transpose("REGIONS 35 I", "SECTORS I")
                                + (
                                    epsilon_import_shares_final_demand()
                                    .loc[:, "CONSUMPTION W"]
                                    .reset_coords(drop=True)
                                    * np.log(
                                        delayed_ts_price_ratio_households() + 1e-07
                                    ).transpose("SECTORS I", "REGIONS 35 I")
                                ).transpose("REGIONS 35 I", "SECTORS I")
                            ),
                        ),
                    ),
                ),
            ),
        )
        .expand_dims(
            {"FINAL DEMAND CONSUMPTION INVESTMENT GOVERNMENT I": ["CONSUMPTION W"]}, 2
        )
        .values
    )
    value.loc[:, :, _subscript_dict["FINAL DEMAND EXCEPT HOUSEHOLDS"]] = (
        initial_import_shares_final_demand()
        .loc[:, :, _subscript_dict["FINAL DEMAND EXCEPT HOUSEHOLDS"]]
        .rename({"FINAL DEMAND I": "FINAL DEMAND EXCEPT HOUSEHOLDS"})
        .values
    )
    return value


@component.add(
    name="import shares final demand constrained",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "import_shares_final_demand": 3,
        "delayed_ts_import_shares_final_demand": 4,
    },
)
def import_shares_final_demand_constrained():
    """
    Import shares by origin for final demand constrined: change in each time step limited to +- 5%
    """
    return if_then_else(
        zidz(import_shares_final_demand(), delayed_ts_import_shares_final_demand())
        > 1.05,
        lambda: delayed_ts_import_shares_final_demand(),
        lambda: if_then_else(
            zidz(import_shares_final_demand(), delayed_ts_import_shares_final_demand())
            < 0.95,
            lambda: delayed_ts_import_shares_final_demand(),
            lambda: import_shares_final_demand(),
        ),
    )


@component.add(
    name="import shares intermediates",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_fixed_import_shares": 1,
        "initial_import_shares_intermediates": 4,
        "constant_import_shares_intermediates": 1,
        "delayed_ts_price_ratio_sectors": 1,
        "epsilon_import_shares_intermediates": 1,
        "delayed_ts_import_shares_intermediates": 4,
        "beta_import_shares_intermediates": 1,
    },
)
def import_shares_intermediates():
    """
    Import shares for intermediates
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "SECTORS I": _subscript_dict["SECTORS I"],
            "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
        },
        ["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    )
    except_subs = xr.zeros_like(value, dtype=bool)
    except_subs.loc[:, _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :] = True
    except_subs.loc[
        ["MALTA"], _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :
    ] = False
    except_subs.loc[
        ["CYPRUS"], _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :
    ] = False
    value.values[except_subs.values] = if_then_else(
        switch_fixed_import_shares() == 1,
        lambda: initial_import_shares_intermediates()
        .loc[:, _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"]]
        .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
        .expand_dims({"SECTORS MAP I": _subscript_dict["SECTORS MAP I"]}, 2),
        lambda: np.minimum(
            1,
            np.maximum(
                0,
                if_then_else(
                    delayed_ts_import_shares_intermediates()
                    .loc[:, _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :]
                    .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
                    == 1,
                    lambda: xr.DataArray(
                        1,
                        {
                            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                            "SECTORS VARIABLE IMPORT SHARES I": _subscript_dict[
                                "SECTORS VARIABLE IMPORT SHARES I"
                            ],
                            "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
                        },
                        [
                            "REGIONS 35 I",
                            "SECTORS VARIABLE IMPORT SHARES I",
                            "SECTORS MAP I",
                        ],
                    ),
                    lambda: if_then_else(
                        delayed_ts_import_shares_intermediates()
                        .loc[:, _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :]
                        .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
                        == 0,
                        lambda: xr.DataArray(
                            0,
                            {
                                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                                "SECTORS VARIABLE IMPORT SHARES I": _subscript_dict[
                                    "SECTORS VARIABLE IMPORT SHARES I"
                                ],
                                "SECTORS MAP I": _subscript_dict["SECTORS MAP I"],
                            },
                            [
                                "REGIONS 35 I",
                                "SECTORS VARIABLE IMPORT SHARES I",
                                "SECTORS MAP I",
                            ],
                        ),
                        lambda: (
                            1
                            - delayed_ts_import_shares_intermediates()
                            .loc[
                                :,
                                _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"],
                                :,
                            ]
                            .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
                            + 1e-07
                        )
                        * np.exp(
                            constant_import_shares_intermediates()
                            .loc[
                                :,
                                _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"],
                                :,
                            ]
                            .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
                            + (
                                beta_import_shares_intermediates()
                                .loc[
                                    _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"],
                                    :,
                                ]
                                .rename(
                                    {"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"}
                                )
                                * np.log(
                                    1e-07
                                    + delayed_ts_import_shares_intermediates()
                                    .loc[
                                        :,
                                        _subscript_dict[
                                            "SECTORS VARIABLE IMPORT SHARES I"
                                        ],
                                        :,
                                    ]
                                    .rename(
                                        {
                                            "SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"
                                        }
                                    )
                                ).transpose(
                                    "SECTORS VARIABLE IMPORT SHARES I",
                                    "SECTORS MAP I",
                                    "REGIONS 35 I",
                                )
                            ).transpose(
                                "REGIONS 35 I",
                                "SECTORS VARIABLE IMPORT SHARES I",
                                "SECTORS MAP I",
                            )
                            + (
                                epsilon_import_shares_intermediates()
                                .loc[
                                    _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"],
                                    :,
                                ]
                                .rename(
                                    {"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"}
                                )
                                * np.log(
                                    1e-07
                                    + delayed_ts_price_ratio_sectors()
                                    .loc[
                                        :,
                                        _subscript_dict[
                                            "SECTORS VARIABLE IMPORT SHARES I"
                                        ],
                                        :,
                                    ]
                                    .rename(
                                        {
                                            "SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"
                                        }
                                    )
                                ).transpose(
                                    "SECTORS VARIABLE IMPORT SHARES I",
                                    "SECTORS MAP I",
                                    "REGIONS 35 I",
                                )
                            ).transpose(
                                "REGIONS 35 I",
                                "SECTORS VARIABLE IMPORT SHARES I",
                                "SECTORS MAP I",
                            )
                        ),
                    ),
                ),
            ),
        ),
    ).values[
        except_subs.loc[
            :, _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :
        ].values
    ]
    value.loc[:, _subscript_dict["SECTORS FIXED IMPORT SHARES I"], :] = (
        initial_import_shares_intermediates()
        .loc[:, _subscript_dict["SECTORS FIXED IMPORT SHARES I"], :]
        .rename({"SECTORS I": "SECTORS FIXED IMPORT SHARES I"})
        .values
    )
    value.loc[["MALTA"], _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :] = (
        initial_import_shares_intermediates()
        .loc["MALTA", _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :]
        .reset_coords(drop=True)
        .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
        .expand_dims({"REGIONS 35 I": ["MALTA"]}, 0)
        .values
    )
    value.loc[["CYPRUS"], _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :] = (
        initial_import_shares_intermediates()
        .loc["CYPRUS", _subscript_dict["SECTORS VARIABLE IMPORT SHARES I"], :]
        .reset_coords(drop=True)
        .rename({"SECTORS I": "SECTORS VARIABLE IMPORT SHARES I"})
        .expand_dims({"REGIONS 35 I": ["CYPRUS"]}, 0)
        .values
    )
    return value


@component.add(
    name="import shares intermediates constrained",
    units="DMNL",
    subscripts=["REGIONS 35 I", "SECTORS I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "import_shares_intermediates": 3,
        "delayed_ts_import_shares_intermediates": 4,
    },
)
def import_shares_intermediates_constrained():
    """
    Import shares by origin for intermediates constrined: change in each time step limited to +- 5%
    """
    return if_then_else(
        zidz(import_shares_intermediates(), delayed_ts_import_shares_intermediates())
        > 1.05,
        lambda: delayed_ts_import_shares_intermediates(),
        lambda: if_then_else(
            zidz(
                import_shares_intermediates(), delayed_ts_import_shares_intermediates()
            )
            < 0.95,
            lambda: delayed_ts_import_shares_intermediates(),
            lambda: import_shares_intermediates(),
        ),
    )


@component.add(
    name="import shares origin final demand",
    units="DMNL",
    subscripts=["REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "FINAL DEMAND I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_import_shares_origin_final_demand": 1},
)
def import_shares_origin_final_demand():
    """
    Import shares by origin for final demand
    """
    return initial_import_shares_origin_final_demand()


@component.add(
    name="import shares origin intermediates",
    units="DMNL",
    subscripts=["REGIONS 35 MAP I", "SECTORS I", "REGIONS 35 I", "SECTORS MAP I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"initial_import_shares_origin_intermediates": 1},
)
def import_shares_origin_intermediates():
    """
    Import shares by origin for intermediates.
    """
    return initial_import_shares_origin_intermediates()


@component.add(
    name="SWITCH FIXED IMPORT SHARES", comp_type="Constant", comp_subtype="Normal"
)
def switch_fixed_import_shares():
    return 0


@component.add(
    name="total exports real by product",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_intermediate_exports_real": 1, "final_exports_real": 1},
)
def total_exports_real_by_product():
    """
    Total exports in real terms by product
    """
    return total_intermediate_exports_real() + final_exports_real()


@component.add(
    name="total imports real by product",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "final_demand_imports_in_basic_prices_real": 1,
        "total_intermediate_imports_real": 1,
    },
)
def total_imports_real_by_product():
    """
    Total imports in real terms by product
    """
    return (
        sum(
            final_demand_imports_in_basic_prices_real().rename(
                {
                    "REGIONS 35 I": "REGIONS 35 I!",
                    "REGIONS 35 MAP I": "REGIONS 35 I",
                    "FINAL DEMAND I": "FINAL DEMAND I!",
                }
            ),
            dim=["REGIONS 35 I!", "FINAL DEMAND I!"],
        )
        + total_intermediate_imports_real()
        .rename({"REGIONS 35 MAP I": "REGIONS 35 I", "SECTORS MAP I": "SECTORS I"})
        .transpose("SECTORS I", "REGIONS 35 I")
    ).transpose("REGIONS 35 I", "SECTORS I")


@component.add(
    name="trade balance real by product",
    units="Mdollars 2015/Year",
    subscripts=["REGIONS 35 I", "SECTORS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_exports_real_by_product": 1, "total_imports_real_by_product": 1},
)
def trade_balance_real_by_product():
    """
    Trade balance in rela terms
    """
    return total_exports_real_by_product() - total_imports_real_by_product()
