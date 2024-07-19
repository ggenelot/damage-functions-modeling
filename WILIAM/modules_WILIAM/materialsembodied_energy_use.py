"""
Module materialsembodied_energy_use
Translated using PySD version 3.13.4
"""

@component.add(
    name="dynamic embodied PE intensity materials 36R",
    units="MJ/kg",
    subscripts=["REGIONS 35 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "time": 2,
        "final_to_primary_energy_by_region_until_2015": 2,
        "embodied_fe_intensity_materials_36r": 4,
        "final_to_primary_energy_by_region": 2,
    },
)
def dynamic_embodied_pe_intensity_materials_36r():
    """
    Dynamic embodied primary energy intensity of materials.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 35 I", "MATERIALS I"],
    )
    value.loc[_subscript_dict["REGIONS 8 I"], :] = if_then_else(
        time() < 2015,
        lambda: zidz(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 8 I"}),
            final_to_primary_energy_by_region_until_2015()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            .expand_dims({"MATERIALS I": _subscript_dict["MATERIALS I"]}, 1),
        ),
        lambda: zidz(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS 8 I"], :]
            .rename({"REGIONS 36 I": "REGIONS 8 I"}),
            final_to_primary_energy_by_region()
            .loc[_subscript_dict["REGIONS 8 I"]]
            .rename({"REGIONS 9 I": "REGIONS 8 I"})
            .expand_dims({"MATERIALS I": _subscript_dict["MATERIALS I"]}, 1),
        ),
    ).values
    value.loc[_subscript_dict["REGIONS EU27 I"], :] = if_then_else(
        time() < 2015,
        lambda: zidz(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
            float(final_to_primary_energy_by_region_until_2015().loc["EU27"]),
        ),
        lambda: zidz(
            embodied_fe_intensity_materials_36r()
            .loc[_subscript_dict["REGIONS EU27 I"], :]
            .rename({"REGIONS 36 I": "REGIONS EU27 I"}),
            float(final_to_primary_energy_by_region().loc["EU27"]),
        ),
    ).values
    return value


@component.add(
    name="embodied FE intensity materials 36R",
    units="MJ/kg",
    subscripts=["REGIONS 36 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "embodied_pe_intensity_materials_36r": 2,
        "final_to_primary_energy_by_region_until_2015": 2,
    },
)
def embodied_fe_intensity_materials_36r():
    """
    Embodied final energy intensity of materials taking as reference the recycling rates of minerals and the final-to-primary ratio of the year 2015.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 36 I", "MATERIALS I"],
    )
    value.loc[_subscript_dict["REGIONS 9 I"], :] = (
        embodied_pe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS 9 I"], :]
        .rename({"REGIONS 36 I": "REGIONS 9 I"})
        * final_to_primary_energy_by_region_until_2015()
    ).values
    value.loc[_subscript_dict["REGIONS EU27 I"], :] = (
        embodied_pe_intensity_materials_36r()
        .loc[_subscript_dict["REGIONS EU27 I"], :]
        .rename({"REGIONS 36 I": "REGIONS EU27 I"})
        * float(final_to_primary_energy_by_region_until_2015().loc["EU27"])
    ).values
    return value


@component.add(
    name="embodied PE intensity materials 36R",
    units="MJ/kg",
    subscripts=["REGIONS 36 I", "MATERIALS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "switch_mat_embodied_energy_of_material_use": 2,
        "embodied_pe_intensity_recycled_materials": 2,
        "embodied_pe_intensity_virgin_materials": 2,
        "rc_rate_mineral_35r": 2,
        "rc_rate_mineral": 2,
    },
)
def embodied_pe_intensity_materials_36r():
    """
    Embodied primary energy intensity of materials taking as reference the recycling rates of minerals.
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 36 I": _subscript_dict["REGIONS 36 I"],
            "MATERIALS I": _subscript_dict["MATERIALS I"],
        },
        ["REGIONS 36 I", "MATERIALS I"],
    )
    value.loc[_subscript_dict["REGIONS 35 I"], :] = if_then_else(
        switch_mat_embodied_energy_of_material_use() == 0,
        lambda: xr.DataArray(
            0,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "MATERIALS I": _subscript_dict["MATERIALS I"],
            },
            ["REGIONS 35 I", "MATERIALS I"],
        ),
        lambda: rc_rate_mineral_35r() * embodied_pe_intensity_recycled_materials()
        + (1 - rc_rate_mineral_35r()) * embodied_pe_intensity_virgin_materials(),
    ).values
    value.loc[["EU27"], :] = (
        if_then_else(
            switch_mat_embodied_energy_of_material_use() == 0,
            lambda: xr.DataArray(
                0, {"MATERIALS I": _subscript_dict["MATERIALS I"]}, ["MATERIALS I"]
            ),
            lambda: rc_rate_mineral().loc["EU27", :].reset_coords(drop=True)
            * embodied_pe_intensity_recycled_materials()
            + (1 - rc_rate_mineral().loc["EU27", :].reset_coords(drop=True))
            * embodied_pe_intensity_virgin_materials(),
        )
        .expand_dims({"REGIONS 36 I": ["EU27"]}, 0)
        .values
    )
    return value
