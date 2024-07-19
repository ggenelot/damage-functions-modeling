"""
Module land_and_waterland.forest_carbon
Translated using PySD version 3.13.4
"""

@component.add(
    name="forest above ground biomass stock",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_forest_above_ground_biomass_stock": 1},
    other_deps={
        "_integ_forest_above_ground_biomass_stock": {
            "initial": {"initial_forest_above_ground_biomass_stock": 1},
            "step": {"variation_of_forest_above_ground_biomass_stock": 1},
        }
    },
)
def forest_above_ground_biomass_stock():
    """
    forest above ground biomass stock
    """
    return _integ_forest_above_ground_biomass_stock()


_integ_forest_above_ground_biomass_stock = Integ(
    lambda: variation_of_forest_above_ground_biomass_stock(),
    lambda: initial_forest_above_ground_biomass_stock(),
    "_integ_forest_above_ground_biomass_stock",
)


@component.add(
    name="forest below ground biomass stock",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_forest_below_ground_biomass_stock": 1},
    other_deps={
        "_integ_forest_below_ground_biomass_stock": {
            "initial": {"initial_forest_below_ground_biomass_stock": 1},
            "step": {"variation_of_forest_below_ground_biomass_stock": 1},
        }
    },
)
def forest_below_ground_biomass_stock():
    """
    forest below ground biomass stock
    """
    return _integ_forest_below_ground_biomass_stock()


_integ_forest_below_ground_biomass_stock = Integ(
    lambda: variation_of_forest_below_ground_biomass_stock(),
    lambda: initial_forest_below_ground_biomass_stock(),
    "_integ_forest_below_ground_biomass_stock",
)


@component.add(
    name="forest carbon dioxide in above ground biomass flow",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"variation_of_forest_carbon_in_above_ground_biomass_stock": 1},
)
def forest_carbon_dioxide_in_above_ground_biomass_flow():
    """
    forest carbon dioxide in above ground biomass flow test test
    """
    return variation_of_forest_carbon_in_above_ground_biomass_stock() * 44 / 12


@component.add(
    name="forest carbon dioxide in below ground biomass flow",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"variation_of_forest_carbon_in_below_ground_biomass_stock": 1},
)
def forest_carbon_dioxide_in_below_ground_biomass_flow():
    """
    forest carbon dioxide in below ground biomass flow
    """
    return variation_of_forest_carbon_in_below_ground_biomass_stock() * 44 / 12


@component.add(
    name="forest carbon dioxide total flow by region",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forest_carbon_dioxide_in_above_ground_biomass_flow": 1,
        "forest_carbon_dioxide_in_below_ground_biomass_flow": 1,
    },
)
def forest_carbon_dioxide_total_flow_by_region():
    """
    forest carbon dioxide total flow by region
    """
    return (
        forest_carbon_dioxide_in_above_ground_biomass_flow()
        + forest_carbon_dioxide_in_below_ground_biomass_flow() * 0
    )


@component.add(
    name="forest carbon dioxide total flow global",
    units="t/Year",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"forest_carbon_dioxide_total_flow_by_region": 1},
)
def forest_carbon_dioxide_total_flow_global():
    """
    forest carbon dioxide total flow global
    """
    return sum(
        forest_carbon_dioxide_total_flow_by_region().rename(
            {"REGIONS 9 I": "REGIONS 9 I!"}
        ),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="forest carbon in above ground biomass stock",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_forest_carbon_in_above_ground_biomass_stock": 1},
    other_deps={
        "_integ_forest_carbon_in_above_ground_biomass_stock": {
            "initial": {"initial_forest_carbon_in_above_ground_biomass_stock": 1},
            "step": {"variation_of_forest_carbon_in_above_ground_biomass_stock": 1},
        }
    },
)
def forest_carbon_in_above_ground_biomass_stock():
    """
    forest carbon in above ground biomass stock
    """
    return _integ_forest_carbon_in_above_ground_biomass_stock()


_integ_forest_carbon_in_above_ground_biomass_stock = Integ(
    lambda: variation_of_forest_carbon_in_above_ground_biomass_stock(),
    lambda: initial_forest_carbon_in_above_ground_biomass_stock(),
    "_integ_forest_carbon_in_above_ground_biomass_stock",
)


@component.add(
    name="forest carbon in below ground biomass stock",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Stateful",
    comp_subtype="Integ",
    depends_on={"_integ_forest_carbon_in_below_ground_biomass_stock": 1},
    other_deps={
        "_integ_forest_carbon_in_below_ground_biomass_stock": {
            "initial": {"initial_forest_carbon_in_below_ground_biomass_stock": 1},
            "step": {"variation_of_forest_carbon_in_below_ground_biomass_stock": 1},
        }
    },
)
def forest_carbon_in_below_ground_biomass_stock():
    """
    forest carbon in below ground biomass stock
    """
    return _integ_forest_carbon_in_below_ground_biomass_stock()


_integ_forest_carbon_in_below_ground_biomass_stock = Integ(
    lambda: variation_of_forest_carbon_in_below_ground_biomass_stock(),
    lambda: initial_forest_carbon_in_below_ground_biomass_stock(),
    "_integ_forest_carbon_in_below_ground_biomass_stock",
)


@component.add(
    name="forest carbon total flow",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "variation_of_forest_carbon_in_above_ground_biomass_stock": 1,
        "variation_of_forest_carbon_in_below_ground_biomass_stock": 1,
    },
)
def forest_carbon_total_flow():
    """
    forest carbon total flow
    """
    return (
        variation_of_forest_carbon_in_above_ground_biomass_stock()
        + variation_of_forest_carbon_in_below_ground_biomass_stock()
    )


@component.add(
    name="forest carbon total stock",
    units="t",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forest_carbon_in_above_ground_biomass_stock": 1,
        "forest_carbon_in_below_ground_biomass_stock": 1,
    },
)
def forest_carbon_total_stock():
    """
    forest carbon total stock
    """
    return (
        forest_carbon_in_above_ground_biomass_stock()
        + forest_carbon_in_below_ground_biomass_stock()
    )


@component.add(
    name="variation of forest above ground biomass stock",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "forest_volume_stock_changes": 1,
        "wbs_plus_biomass_exansion_factor_forest": 1,
    },
)
def variation_of_forest_above_ground_biomass_stock():
    """
    variation of forest above ground biomass stock
    """
    return forest_volume_stock_changes() * wbs_plus_biomass_exansion_factor_forest()


@component.add(
    name="variation of forest below ground biomass stock",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "root_to_shoot_ratio_forest": 1,
        "variation_of_forest_above_ground_biomass_stock": 1,
    },
)
def variation_of_forest_below_ground_biomass_stock():
    """
    variation of forest below ground biomass stock
    """
    return (
        root_to_shoot_ratio_forest() * variation_of_forest_above_ground_biomass_stock()
    )


@component.add(
    name="variation of forest carbon in above ground biomass stock",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_fraction_of_dry_matter_forest": 1,
        "variation_of_forest_above_ground_biomass_stock": 1,
    },
)
def variation_of_forest_carbon_in_above_ground_biomass_stock():
    """
    variation of forest carbon in above ground biomass stock
    """
    return (
        carbon_fraction_of_dry_matter_forest()
        * variation_of_forest_above_ground_biomass_stock()
    )


@component.add(
    name="variation of forest carbon in below ground biomass stock",
    units="t/Year",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "carbon_fraction_of_dry_matter_forest": 1,
        "variation_of_forest_below_ground_biomass_stock": 1,
    },
)
def variation_of_forest_carbon_in_below_ground_biomass_stock():
    """
    variation of forest carbon in below ground biomass stock
    """
    return (
        carbon_fraction_of_dry_matter_forest()
        * variation_of_forest_below_ground_biomass_stock()
    )
