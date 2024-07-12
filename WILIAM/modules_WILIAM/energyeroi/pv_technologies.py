"""
Module energyeroi.pv_technologies
Translated using PySD version 3.14.0
"""

@component.add(
    name="decomissioning FE intensity PV technologies",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "share_energy_requirements_for_decomm_protra": 1,
        "fenust_pv": 1,
        "fe_intensity_manufacturing_pv_panels": 1,
        "machining_fe_intensity_pv": 1,
    },
)
def decomissioning_fe_intensity_pv_technologies():
    """
    Decomissioning energy of photovoltaic instalations
    """
    return (
        share_energy_requirements_for_decomm_protra()
        .loc[_subscript_dict["PROTRA PP SOLAR PV I"]]
        .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        * (
            fenust_pv()
            + machining_fe_intensity_pv()
            + fe_intensity_manufacturing_pv_panels()
        ).transpose(
            "PROTRA PP SOLAR PV I",
            "REGIONS 9 I",
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
        )
    ).transpose(
        "REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
    )


@component.add(
    name="EROIfinal PV technologies",
    units="DMNL",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_delivered_at_consumer_phase_pv": 1,
        "total_fe_embodied_pv_technology": 1,
        "fe_delivered_at_plant_phase_pv": 1,
        "share_total_transmission_loss": 1,
        "fe_intensity_current_grids_om": 1,
        "share_self_electricity_consumption_protra": 1,
    },
)
def eroifinal_pv_technologies():
    """
    EROIfinal of photovoltaic technology per type of panel
    """
    return zidz(
        fe_delivered_at_consumer_phase_pv().expand_dims(
            {
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ]
            },
            2,
        ),
        total_fe_embodied_pv_technology()
        + fe_intensity_current_grids_om()
        + (
            fe_delivered_at_plant_phase_pv()
            .loc[:, "TO elec", :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * share_self_electricity_consumption_protra()
            .loc[_subscript_dict["PROTRA PP SOLAR PV I"]]
            .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
            * (
                1
                + share_total_transmission_loss()
                .loc[:, "TO elec"]
                .reset_coords(drop=True)
            )
        ),
    )


@component.add(
    name="EROIst PV technologies",
    units="DMNL",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fe_delivered_at_plant_phase_pv": 2,
        "share_self_electricity_consumption_protra": 1,
        "total_fe_embodied_pv_technology": 1,
    },
)
def eroist_pv_technologies():
    """
    EROIst of photovoltaic technology per type of panel
    """
    return zidz(
        fe_delivered_at_plant_phase_pv()
        .loc[:, "TO elec", :, "PROTRA PP solar open space PV"]
        .reset_coords(drop=True)
        .expand_dims(
            {
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
                ]
            },
            2,
        ),
        total_fe_embodied_pv_technology()
        + (
            fe_delivered_at_plant_phase_pv()
            .loc[:, "TO elec", :, "PROTRA PP solar open space PV"]
            .reset_coords(drop=True)
            * share_self_electricity_consumption_protra()
            .loc[_subscript_dict["PROTRA PP SOLAR PV I"]]
            .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        ),
    )


@component.add(
    name="FE delivered at consumer phase PV",
    units="MJ",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "cf_protra": 1,
        "mw_1_year_to_mj": 1,
        "protra_lifetime": 1,
        "ol_pv": 1,
        "share_total_transmission_loss": 1,
    },
)
def fe_delivered_at_consumer_phase_pv():
    """
    Energy delivered throughout his life at consumer phase os a PV system
    """
    return (
        cf_protra()
        .loc[:, "TO elec", _subscript_dict["PROTRA PP SOLAR PV I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        * mw_1_year_to_mj()
        * protra_lifetime()
        .loc["EU27", _subscript_dict["PROTRA PP SOLAR PV I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        * (1 - ol_pv())
        * (
            1
            - share_total_transmission_loss().loc[:, "TO elec"].reset_coords(drop=True)
        )
    )


@component.add(
    name="FE delivered at plant phase PV",
    units="MJ",
    subscripts=[
        "REGIONS 9 I",
        "NRG COMMODITIES I",
        "PROTRA PP SOLAR PV I",
        "NRG PRO I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cf_protra": 1, "mw_1_year_to_mj": 1, "protra_lifetime": 1, "ol_pv": 1},
)
def fe_delivered_at_plant_phase_pv():
    """
    Energy delivered throughout his life at plant phase os a PV system
    """
    return (
        (
            cf_protra()
            .loc[:, "TO elec", _subscript_dict["PROTRA PP SOLAR PV I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
            * mw_1_year_to_mj()
            * protra_lifetime()
            .loc["EU27", _subscript_dict["PROTRA PP SOLAR PV I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
            * (1 - ol_pv())
        )
        .expand_dims({"NRG COMMODITIES I": ["TO elec"]}, 1)
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 3)
    )


@component.add(
    name="FE INTENSITY CURRENT GRIDS OM",
    units="MJ/MW",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_intensity_current_grids_om": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def fe_intensity_current_grids_om():
    return (
        pe_intensity_current_grids_om() * final_to_primary_energy_by_region_until_2015()
    )


@component.add(
    name="FE INTENSITY MANUFACTURING PV PANELS",
    units="MJ/MW",
    subscripts=["REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "pe_intensity_manufacturing_pv_panels": 1,
        "final_to_primary_energy_by_region_until_2015": 1,
    },
)
def fe_intensity_manufacturing_pv_panels():
    return (
        pe_intensity_manufacturing_pv_panels()
        * final_to_primary_energy_by_region_until_2015()
    ).transpose("REGIONS 9 I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I")


@component.add(
    name="FEnUst PV",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_fe_intensity_materials_36r": 1,
        "total_material_intensity_pv_by_technology": 1,
    },
)
def fenust_pv():
    """
    Total energy embodied energy of mineral requirements per MW of a photovoltaic system.
    """
    return sum(
        embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I", "MATERIALS I": "MATERIALS I!"})
        * total_material_intensity_pv_by_technology().rename(
            {"MATERIALS I": "MATERIALS I!"}
        ),
        dim=["MATERIALS I!"],
    )


@component.add(
    name="machining FE intensity PV",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"fenust_pv": 1, "machining_rate_pv": 1},
)
def machining_fe_intensity_pv():
    """
    Machining energy per MW of a photovoltaic installation
    """
    return fenust_pv() * machining_rate_pv()


@component.add(
    name="MACHINING RATE PV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_machining_rate_pv"},
)
def machining_rate_pv():
    """
    Machining energy rate for PV technology take from Carlos de Castro et al (2020) paper
    """
    return _ext_constant_machining_rate_pv()


_ext_constant_machining_rate_pv = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Efficiency_improvements",
    "MACHINING_RATE_PV*",
    {},
    _root,
    {},
    "_ext_constant_machining_rate_pv",
)


@component.add(
    name="OL PV",
    units="DMNL",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_ol_pv"},
)
def ol_pv():
    """
    Operational losses of PV system. Taken from De Castro et al 2020.
    """
    return _ext_constant_ol_pv()


_ext_constant_ol_pv = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Efficiency_improvements",
    "OL_PV*",
    {},
    _root,
    {},
    "_ext_constant_ol_pv",
)


@component.add(
    name="OM FE intensity PV",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_fe_intensity_materials_36r": 2,
        "material_intensity_om_pv_by_technology": 2,
        "protra_lifetime": 2,
    },
)
def om_fe_intensity_pv():
    """
    Energy embodied of materials requirements per MW for Operation and Maintenance (O&M) of solar PV.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = (
        sum(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 8 I", "MATERIALS I": "MATERIALS I!"})
            * material_intensity_om_pv_by_technology().rename(
                {"MATERIALS I": "MATERIALS I!"}
            ),
            dim=["MATERIALS I!"],
        )
        * protra_lifetime()
        .loc["EU27", _subscript_dict["PROTRA PP SOLAR PV I"]]
        .reset_coords(drop=True)
        .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
    ).values
    value.loc[["EU27"], :, :] = (
        (
            sum(
                embodied_fe_intensity_materials_36r()
                .loc["EU27", :]
                .reset_coords(drop=True)
                .rename({"MATERIALS I": "MATERIALS I!"})
                * material_intensity_om_pv_by_technology().rename(
                    {"MATERIALS I": "MATERIALS I!"}
                ),
                dim=["MATERIALS I!"],
            )
            * protra_lifetime()
            .loc["EU27", _subscript_dict["PROTRA PP SOLAR PV I"]]
            .reset_coords(drop=True)
            .rename({"NRG PROTRA I": "PROTRA PP SOLAR PV I"})
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="PE INTENSITY CURRENT GRIDS OM",
    units="MJ/MW",
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pe_intensity_current_grids_om"},
)
def pe_intensity_current_grids_om():
    """
    Primary energy per MW for O&M the current grids for PV technologies. Taken from De Castro et al 2020
    """
    return _ext_constant_pe_intensity_current_grids_om()


_ext_constant_pe_intensity_current_grids_om = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Efficiency_improvements",
    "CURRENT_GRIDS_O_AND_M_PV_TECHNOLOGIES_ENERGY*",
    {},
    _root,
    {},
    "_ext_constant_pe_intensity_current_grids_om",
)


@component.add(
    name="PE INTENSITY MANUFACTURING PV PANELS",
    units="MJ/MW",
    subscripts=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Constant",
    comp_subtype="External",
    depends_on={"__external__": "_ext_constant_pe_intensity_manufacturing_pv_panels"},
)
def pe_intensity_manufacturing_pv_panels():
    """
    Manufacturing energy per MW of photovoltaic panels according to their type. In the case of the panels, the manufacturing energy of each technology has been taken from the reference (Frischknecht et al., 2015) (using g=0.737 in the electrical energy conversion).
    """
    return _ext_constant_pe_intensity_manufacturing_pv_panels()


_ext_constant_pe_intensity_manufacturing_pv_panels = ExtConstant(
    "model_parameters/energy/energy-transformation.xlsm",
    "Efficiency_improvements",
    "MANUFACTURING_ENERGY_OF_PV_PANELS*",
    {
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
        ]
    },
    _root,
    {
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
        ]
    },
    "_ext_constant_pe_intensity_manufacturing_pv_panels",
)


@component.add(
    name="scrap FE intensity PV",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_fe_intensity_materials_36r": 2,
        "scrap_material_intensity_pv": 2,
    },
)
def scrap_fe_intensity_pv():
    """
    Scrap materials energy embodied per MW of a photovoltaic installation
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
            "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": _subscript_dict[
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"
            ],
        },
        ["REGIONS 9 I", "PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :, :] = sum(
        embodied_fe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 8 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 8 I", "MATERIALS I": "MATERIALS I!"})
        * scrap_material_intensity_pv().rename({"MATERIALS I": "MATERIALS I!"}),
        dim=["MATERIALS I!"],
    ).values
    value.loc[["EU27"], :, :] = (
        sum(
            embodied_fe_intensity_materials_36r()
            .loc["EU27", :]
            .reset_coords(drop=True)
            .rename({"MATERIALS I": "MATERIALS I!"})
            * scrap_material_intensity_pv().rename({"MATERIALS I": "MATERIALS I!"}),
            dim=["MATERIALS I!"],
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value


@component.add(
    name="scrap material intensity PV",
    units="kg/MW",
    subscripts=[
        "MATERIALS I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_material_intensity_pv_by_technology": 1, "scrap_rate": 1},
)
def scrap_material_intensity_pv():
    """
    Scrap materials requirements per MW of a photovoltaic installation
    """
    return total_material_intensity_pv_by_technology() * scrap_rate()


@component.add(
    name="total FE embodied PV technology",
    units="MJ/MW",
    subscripts=[
        "REGIONS 9 I",
        "PROTRA PP SOLAR PV I",
        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I",
    ],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "fenust_pv": 1,
        "decomissioning_fe_intensity_pv_technologies": 1,
        "machining_fe_intensity_pv": 1,
        "om_fe_intensity_pv": 1,
        "scrap_fe_intensity_pv": 1,
        "transport_materials_fe_intensity_pv_technologies": 1,
        "fe_intensity_manufacturing_pv_panels": 1,
    },
)
def total_fe_embodied_pv_technology():
    """
    Total energy embodied per MW of photovoltaic technology.
    """
    return (
        fenust_pv()
        + decomissioning_fe_intensity_pv_technologies()
        + machining_fe_intensity_pv()
        + om_fe_intensity_pv()
        + scrap_fe_intensity_pv()
        + (2 * transport_materials_fe_intensity_pv_technologies())
        + fe_intensity_manufacturing_pv_panels()
    )


@component.add(
    name="total local material intensity PV",
    units="kg/MW",
    subscripts=["PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"total_material_intensity_pv_by_technology": 3},
)
def total_local_material_intensity_pv():
    """
    Total local materials which we assume that do not travel: cement, gravel and site preparation requirements per MW of a photovoltaic system
    """
    return (
        total_material_intensity_pv_by_technology()
        .loc["Cement", :, :]
        .reset_coords(drop=True)
        + total_material_intensity_pv_by_technology()
        .loc["Site preparation", :, :]
        .reset_coords(drop=True)
        + total_material_intensity_pv_by_technology()
        .loc["gravel", :, :]
        .reset_coords(drop=True)
    )


@component.add(
    name="total material transported PV",
    units="kg/MW",
    subscripts=["PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_material_intensity_pv_by_technology": 1,
        "total_local_material_intensity_pv": 1,
    },
)
def total_material_transported_pv():
    """
    Total mineral requirements per MW of a photovoltaic system without taking account those that we assume that do not travel (cement, gravel and site preparation).
    """
    return (
        sum(
            total_material_intensity_pv_by_technology().rename(
                {"MATERIALS I": "MATERIALS I!"}
            ),
            dim=["MATERIALS I!"],
        )
        - total_local_material_intensity_pv()
    )


@component.add(
    name="transport materials FE intensity PV technologies",
    units="MJ/MW",
    subscripts=["PROTRA PP SOLAR PV I", "PROTRA PP SOLAR PV SUBTECHNOLOGIES I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "total_material_transported_pv": 2,
        "total_local_material_intensity_pv": 1,
    },
)
def transport_materials_fe_intensity_pv_technologies():
    """
    Energy required for the transport of photovoltaic ground technology materials per type of panel
    """
    return (
        1.19 * 500 * 3.5 * total_material_transported_pv()
        + 1.09 * 10000 * 0.2 * total_material_transported_pv()
        + 1.19 * total_local_material_intensity_pv() * 3.5 * 250
    ) / 1000
