"""
Module materialsrequirements.protra
Translated using PySD version 3.13.4
"""

@component.add(
    name="cum materials requirements for PROTRA from initial year",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_requirements_for_protra_from_initial_year": 1},
    other_deps={
        "_integ_cum_materials_requirements_for_protra_from_initial_year": {
            "initial": {},
            "step": {"materials_required_for_protra": 1},
        }
    },
)
def cum_materials_requirements_for_protra_from_initial_year():
    """
    Total cumulative materials requirements for the installation and O&M by PROTRA technology.
    """
    return _integ_cum_materials_requirements_for_protra_from_initial_year()


_integ_cum_materials_requirements_for_protra_from_initial_year = Integ(
    lambda: materials_required_for_protra(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    ),
    "_integ_cum_materials_requirements_for_protra_from_initial_year",
)


@component.add(
    name="cum materials to extract for PROTRA from initial year",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_to_extract_for_protra_from_initial_year": 1},
    other_deps={
        "_integ_cum_materials_to_extract_for_protra_from_initial_year": {
            "initial": {},
            "step": {"materials_extracted_for_protra": 1},
        }
    },
)
def cum_materials_to_extract_for_protra_from_initial_year():
    """
    Cumulative materials to be mined for the installation and O&M of PROTRA.
    """
    return _integ_cum_materials_to_extract_for_protra_from_initial_year()


_integ_cum_materials_to_extract_for_protra_from_initial_year = Integ(
    lambda: materials_extracted_for_protra(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    ),
    "_integ_cum_materials_to_extract_for_protra_from_initial_year",
)


@component.add(
    name="cum materials xtracted for PROTRA from 2015",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_cum_materials_xtracted_for_protra_from_2015": 1},
    other_deps={
        "_integ_cum_materials_xtracted_for_protra_from_2015": {
            "initial": {},
            "step": {"materials_extracted_for_protra_from_2015": 1},
        }
    },
)
def cum_materials_xtracted_for_protra_from_2015():
    """
    Cumulative materials to be mined for the installation and O&M by PROTRA technology.
    """
    return _integ_cum_materials_xtracted_for_protra_from_2015()


_integ_cum_materials_xtracted_for_protra_from_2015 = Integ(
    lambda: materials_extracted_for_protra_from_2015(),
    lambda: xr.DataArray(
        0,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    ),
    "_integ_cum_materials_xtracted_for_protra_from_2015",
)


@component.add(
    name="cumulated extracted materials all PROTRAs from 2015",
    units="Mt",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cum_materials_xtracted_for_protra_from_2015": 1},
)
def cumulated_extracted_materials_all_protras_from_2015():
    """
    Cumulatd materials to extrac for all PROTRA technologies from 2015.
    """
    return sum(
        cum_materials_xtracted_for_protra_from_2015().rename(
            {"NRG PROTRA I": "NRG PROTRA I!"}
        ),
        dim=["NRG PROTRA I!"],
    )


@component.add(
    name="material intensities for new PROTRA",
    units="kg/MW",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_new_capacity_csp_regional": 1,
        "material_intensity_weighted_average_new_pv": 1,
        "material_intensity_new_capacity_wind_offshore_regional": 1,
        "material_intensity_new_capacity_wind_onshore_regional": 1,
    },
)
def material_intensities_for_new_protra():
    """
    Material intensities for new capacities of transformation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA PP solar CSP"], :] = False
    except_subs.loc[:, _subscript_dict["PROTRA PP SOLAR PV I"], :] = False
    except_subs.loc[:, ["PROTRA PP wind offshore"], :] = False
    except_subs.loc[:, ["PROTRA PP wind onshore"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["PROTRA PP solar CSP"], :] = (
        material_intensity_new_capacity_csp_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA PP SOLAR PV I"], :] = (
        material_intensity_weighted_average_new_pv()
        .transpose("REGIONS 9 I", "PROTRA PP SOLAR PV I", "MATERIALS I")
        .values
    )
    value.loc[:, ["PROTRA PP wind offshore"], :] = (
        material_intensity_new_capacity_wind_offshore_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP wind offshore"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP wind onshore"], :] = (
        material_intensity_new_capacity_wind_onshore_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP wind onshore"]}, 1)
        .values
    )
    return value


@component.add(
    name="material intensities OM PROTRA",
    units="kg/(MW*Year)",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary, Constant",
    comp_subtype="Normal",
    depends_on={
        "material_intensity_om_csp_regional": 1,
        "material_intensity_weigthed_average_om_pv": 1,
        "material_intensity_om_wind_offshore_regional": 1,
        "material_intensity_om_wind_onshore_regional": 1,
    },
)
def material_intensities_om_protra():
    """
    Material intensities for the operation & maintenance of process transformation capacities in operation.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    )
    except_subs = xr.ones_like(value, dtype=bool)
    except_subs.loc[:, ["PROTRA PP solar CSP"], :] = False
    except_subs.loc[:, _subscript_dict["PROTRA PP SOLAR PV I"], :] = False
    except_subs.loc[:, ["PROTRA PP wind offshore"], :] = False
    except_subs.loc[:, ["PROTRA PP wind onshore"], :] = False
    value.values[except_subs.values] = 0
    value.loc[:, ["PROTRA PP solar CSP"], :] = (
        material_intensity_om_csp_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP solar CSP"]}, 1)
        .values
    )
    value.loc[:, _subscript_dict["PROTRA PP SOLAR PV I"], :] = (
        material_intensity_weigthed_average_om_pv()
        .transpose("REGIONS 9 I", "PROTRA PP SOLAR PV I", "MATERIALS I")
        .values
    )
    value.loc[:, ["PROTRA PP wind offshore"], :] = (
        material_intensity_om_wind_offshore_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP wind offshore"]}, 1)
        .values
    )
    value.loc[:, ["PROTRA PP wind onshore"], :] = (
        material_intensity_om_wind_onshore_regional()
        .expand_dims({"NRG PRO I": ["PROTRA PP wind onshore"]}, 1)
        .values
    )
    return value


@component.add(
    name="MATERIAL INTENSITY NEW CAPACITY CSP REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_csp": 1},
)
def material_intensity_new_capacity_csp_regional():
    return material_intensity_new_capacity_csp().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="MATERIAL INTENSITY NEW CAPACITY WIND OFFSHORE REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_wind_offshore": 1},
)
def material_intensity_new_capacity_wind_offshore_regional():
    return material_intensity_new_capacity_wind_offshore().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="MATERIAL INTENSITY NEW CAPACITY WIND ONSHORE REGIONAL",
    units="kg/MW",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_new_capacity_wind_onshore": 1},
)
def material_intensity_new_capacity_wind_onshore_regional():
    return material_intensity_new_capacity_wind_onshore().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="MATERIAL INTENSITY OM CSP REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_csp": 1},
)
def material_intensity_om_csp_regional():
    return material_intensity_om_csp().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="MATERIAL INTENSITY OM WIND OFFSHORE REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_wind_offshore": 1},
)
def material_intensity_om_wind_offshore_regional():
    return material_intensity_om_wind_offshore().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="MATERIAL INTENSITY OM WIND ONSHORE REGIONAL",
    units="kg/(MW*Year)",
    subscripts=["REGIONS 9 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"material_intensity_om_wind_onshore": 1},
)
def material_intensity_om_wind_onshore_regional():
    return material_intensity_om_wind_onshore().expand_dims(
        {"REGIONS 9 I": _subscript_dict["REGIONS 9 I"]}, 0
    )


@component.add(
    name="material intensity weighted average new PV",
    units="kg/MW",
    subscripts=["REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 2,
        "scrap_rate": 4,
        "initial_share_new_pv_subtechn_land": 1,
        "total_material_intensity_pv_by_technology": 4,
        "share_new_pv_subtechn_land": 1,
        "initial_share_new_pv_subtechn_urban": 1,
        "share_new_pv_subtechn_urban": 1,
    },
)
def material_intensity_weighted_average_new_pv():
    """
    Total material intensity of new PV instalations as a weighted average of the different subtechnologies.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
            "PROTRA PP SOLAR PV I": _subscript_dict["PROTRA PP SOLAR PV I"],
        },
        ["REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV I"],
    )
    value.loc[:, :, ["PROTRA PP solar open space PV"]] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA PP solar open space PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                .transpose("PROTRA PP SOLAR PV SUBTECHNOLOGIES I!", "MATERIALS I"),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * (1 + scrap_rate()),
            lambda: sum(
                share_new_pv_subtechn_land().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA PP solar open space PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                .transpose("PROTRA PP SOLAR PV SUBTECHNOLOGIES I!", "MATERIALS I"),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * (1 + scrap_rate()),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar open space PV"]}, 2)
        .values
    )
    value.loc[:, :, ["PROTRA PP solar urban PV"]] = (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA PP solar urban PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                .transpose("PROTRA PP SOLAR PV SUBTECHNOLOGIES I!", "MATERIALS I"),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * (1 + scrap_rate()),
            lambda: sum(
                share_new_pv_subtechn_urban().rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                * total_material_intensity_pv_by_technology()
                .loc[:, "PROTRA PP solar urban PV", :]
                .reset_coords(drop=True)
                .rename(
                    {
                        "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                    }
                )
                .transpose("PROTRA PP SOLAR PV SUBTECHNOLOGIES I!", "MATERIALS I"),
                dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
            )
            * (1 + scrap_rate()),
        )
        .expand_dims({"NRG PRO I": ["PROTRA PP solar urban PV"]}, 2)
        .values
    )
    return value


@component.add(
    name="material intensity weigthed average OM PV",
    units="kg/(MW*Year)",
    subscripts=["REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "initial_share_pv_capacity_by_subtechnology": 1,
        "material_intensity_om_pv_by_technology": 2,
        "share_capacity_stock_protra_pp_solar_pv_by_subtechnology": 1,
    },
)
def material_intensity_weigthed_average_om_pv():
    """
    Total OM material intensity of PV instalations stock as a weighted average of the different subtechnologies.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: sum(
            initial_share_pv_capacity_by_subtechnology().rename(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                }
            )
            * material_intensity_om_pv_by_technology()
            .rename(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                }
            )
            .transpose(
                "PROTRA PP SOLAR PV I",
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!",
                "MATERIALS I",
            ),
            dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
        ),
        lambda: sum(
            share_capacity_stock_protra_pp_solar_pv_by_subtechnology().rename(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                }
            )
            * material_intensity_om_pv_by_technology()
            .rename(
                {
                    "PROTRA PP SOLAR PV SUBTECHNOLOGIES I": "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"
                }
            )
            .transpose(
                "PROTRA PP SOLAR PV I",
                "PROTRA PP SOLAR PV SUBTECHNOLOGIES I!",
                "MATERIALS I",
            ),
            dim=["PROTRA PP SOLAR PV SUBTECHNOLOGIES I!"],
        ),
    ).transpose("REGIONS 9 I", "MATERIALS I", "PROTRA PP SOLAR PV I")


@component.add(
    name="Materials extracted for PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"materials_required_for_protra": 1, "rc_rate_mineral": 1},
)
def materials_extracted_for_protra():
    """
    Annual materials to be mined for the construction and O&M by PROTRA technology..
    """
    return materials_required_for_protra() * (1 - rc_rate_mineral())


@component.add(
    name="Materials extracted for PROTRA from 2015",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"time": 1, "materials_extracted_for_protra": 1},
)
def materials_extracted_for_protra_from_2015():
    """
    Annual materials to be mined for the installation and O&M by PROTRA technology from 2015.
    """
    return if_then_else(
        time() < 2015,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 9 I": _subscript_dict["REGIONS 9 I"],
                "NRG PROTRA I": _subscript_dict["NRG PROTRA I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
        ),
        lambda: materials_extracted_for_protra(),
    )


@component.add(
    name="materials required for new PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "initial_protra_capacity_expansion": 1,
        "protra_capacity_expansion_selected": 1,
        "material_intensities_for_new_protra": 1,
        "unit_conversion_mw_tw": 1,
        "unit_conversion_kg_mt": 1,
    },
)
def materials_required_for_new_protra():
    """
    Annual materials required for the installation of new capacity by PROTRA technology.
    """
    return (
        if_then_else(
            switch_materials() == 0,
            lambda: sum(
                initial_protra_capacity_expansion().rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            ),
            lambda: sum(
                protra_capacity_expansion_selected().rename({"NRG TO I": "NRG TO I!"}),
                dim=["NRG TO I!"],
            ),
        )
        * material_intensities_for_new_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt()
    )


@component.add(
    name="Materials required for OM PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_materials": 1,
        "initial_protra_capacity_stock": 1,
        "unit_conversion_mw_tw": 2,
        "material_intensities_om_protra": 2,
        "unit_conversion_kg_mt": 2,
        "protra_operative_capacity_stock_selected": 1,
    },
)
def materials_required_for_om_protra():
    """
    Annual materials required for the operation and maintenance of the capacity of PROTRA in operation by technology.
    """
    return if_then_else(
        switch_materials() == 0,
        lambda: sum(
            initial_protra_capacity_stock()
            .loc[_subscript_dict["REGIONS 9 I"], :, :]
            .rename({"REGIONS 36 I": "REGIONS 9 I", "NRG TO I": "NRG TO I!"}),
            dim=["NRG TO I!"],
        )
        * material_intensities_om_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
        lambda: sum(
            protra_operative_capacity_stock_selected().rename(
                {"NRG TO I": "NRG TO I!"}
            ),
            dim=["NRG TO I!"],
        )
        * material_intensities_om_protra()
        * unit_conversion_mw_tw()
        / unit_conversion_kg_mt(),
    )


@component.add(
    name="materials required for PROTRA",
    units="Mt/Year",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_new_protra": 1,
        "materials_required_for_om_protra": 1,
    },
)
def materials_required_for_protra():
    """
    Annual materials requirements for the construction and O&M of PROTRA.
    """
    return materials_required_for_new_protra() + materials_required_for_om_protra()


@component.add(
    name="Total recycled materials for PROTRA",
    units="Mt",
    subscripts=["REGIONS 9 I", "NRG PROTRA I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "materials_required_for_protra": 1,
        "materials_extracted_for_protra": 1,
    },
)
def total_recycled_materials_for_protra():
    """
    Total recycled materials for PROTRA.
    """
    return materials_required_for_protra() - materials_extracted_for_protra()
