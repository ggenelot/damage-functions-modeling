"""
Module societyinequality
Translated using PySD version 3.14.0
"""

@component.add(
    name="Cumulative Lorenz GDP EU27",
    units="DMNL",
    subscripts=["SGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_eu27_ordered": 378},
)
def cumulative_lorenz_gdp_eu27():
    value = xr.DataArray(
        np.nan, {"SGINI EU I": _subscript_dict["SGINI EU I"]}, ["SGINI EU I"]
    )
    value.loc[["SGINI EU1"]] = float(gdp_share_eu27_ordered().loc["SGINI EU1"])
    value.loc[["SGINI EU2"]] = float(gdp_share_eu27_ordered().loc["SGINI EU1"]) + float(
        gdp_share_eu27_ordered().loc["SGINI EU2"]
    )
    value.loc[["SGINI EU3"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
    )
    value.loc[["SGINI EU4"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
    )
    value.loc[["SGINI EU5"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
    )
    value.loc[["SGINI EU6"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
    )
    value.loc[["SGINI EU7"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
    )
    value.loc[["SGINI EU8"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
    )
    value.loc[["SGINI EU9"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
    )
    value.loc[["SGINI EU10"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
    )
    value.loc[["SGINI EU11"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
    )
    value.loc[["SGINI EU12"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
    )
    value.loc[["SGINI EU13"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
    )
    value.loc[["SGINI EU14"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
    )
    value.loc[["SGINI EU15"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
    )
    value.loc[["SGINI EU16"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
    )
    value.loc[["SGINI EU17"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
    )
    value.loc[["SGINI EU18"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
    )
    value.loc[["SGINI EU19"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
    )
    value.loc[["SGINI EU20"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
    )
    value.loc[["SGINI EU21"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
    )
    value.loc[["SGINI EU22"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
    )
    value.loc[["SGINI EU23"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU23"])
    )
    value.loc[["SGINI EU24"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU24"])
    )
    value.loc[["SGINI EU25"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU25"])
    )
    value.loc[["SGINI EU26"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU25"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU26"])
    )
    value.loc[["SGINI EU27"]] = (
        float(gdp_share_eu27_ordered().loc["SGINI EU1"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU2"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU3"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU4"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU5"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU6"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU7"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU8"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU9"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU10"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU11"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU12"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU13"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU14"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU15"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU16"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU17"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU18"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU19"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU20"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU21"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU22"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU23"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU24"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU25"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU26"])
        + float(gdp_share_eu27_ordered().loc["SGINI EU27"])
    )
    return value


@component.add(
    name="Cumulative Lorenz GDP regions",
    units="DMNL",
    subscripts=["SGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_regions_ordered": 45},
)
def cumulative_lorenz_gdp_regions():
    """
    construct new vector which includes cumulated GDP: region1 (poorest) has only the GDP share corresponding to it. Region2 has its own GDP share + the one of region 1. The next richest region has its own GDP share + the share of the previous poorer regions and so on.
    """
    value = xr.DataArray(
        np.nan,
        {"SGINI REGIONS I": _subscript_dict["SGINI REGIONS I"]},
        ["SGINI REGIONS I"],
    )
    value.loc[["SGINI REGION1"]] = float(
        gdp_share_regions_ordered().loc["SGINI REGION1"]
    )
    value.loc[["SGINI REGION2"]] = float(
        gdp_share_regions_ordered().loc["SGINI REGION1"]
    ) + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
    value.loc[["SGINI REGION3"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
    )
    value.loc[["SGINI REGION4"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
    )
    value.loc[["SGINI REGION5"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION5"])
    )
    value.loc[["SGINI REGION6"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION6"])
    )
    value.loc[["SGINI REGION7"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION7"])
    )
    value.loc[["SGINI REGION8"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION7"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION8"])
    )
    value.loc[["SGINI REGION9"]] = (
        float(gdp_share_regions_ordered().loc["SGINI REGION1"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION2"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION3"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION4"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION5"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION6"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION7"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION8"])
        + float(gdp_share_regions_ordered().loc["SGINI REGION9"])
    )
    return value


@component.add(
    name="GDP pc EU27 gini",
    units="Mdollars 2015/(Year*person)",
    subscripts=["FGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_per_capita_eu27": 27},
)
def gdp_pc_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI EU I": _subscript_dict["FGINI EU I"]}, ["FGINI EU I"]
    )
    value.loc[["FGINI EU1"]] = float(gdp_per_capita_eu27().loc["AUSTRIA"])
    value.loc[["FGINI EU2"]] = float(gdp_per_capita_eu27().loc["BELGIUM"])
    value.loc[["FGINI EU3"]] = float(gdp_per_capita_eu27().loc["BULGARIA"])
    value.loc[["FGINI EU4"]] = float(gdp_per_capita_eu27().loc["CROATIA"])
    value.loc[["FGINI EU5"]] = float(gdp_per_capita_eu27().loc["CYPRUS"])
    value.loc[["FGINI EU6"]] = float(gdp_per_capita_eu27().loc["CZECH REPUBLIC"])
    value.loc[["FGINI EU7"]] = float(gdp_per_capita_eu27().loc["DENMARK"])
    value.loc[["FGINI EU8"]] = float(gdp_per_capita_eu27().loc["ESTONIA"])
    value.loc[["FGINI EU9"]] = float(gdp_per_capita_eu27().loc["FINLAND"])
    value.loc[["FGINI EU10"]] = float(gdp_per_capita_eu27().loc["FRANCE"])
    value.loc[["FGINI EU11"]] = float(gdp_per_capita_eu27().loc["GERMANY"])
    value.loc[["FGINI EU12"]] = float(gdp_per_capita_eu27().loc["GREECE"])
    value.loc[["FGINI EU13"]] = float(gdp_per_capita_eu27().loc["HUNGARY"])
    value.loc[["FGINI EU14"]] = float(gdp_per_capita_eu27().loc["IRELAND"])
    value.loc[["FGINI EU15"]] = float(gdp_per_capita_eu27().loc["ITALY"])
    value.loc[["FGINI EU16"]] = float(gdp_per_capita_eu27().loc["LATVIA"])
    value.loc[["FGINI EU17"]] = float(gdp_per_capita_eu27().loc["LITHUANIA"])
    value.loc[["FGINI EU18"]] = float(gdp_per_capita_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI EU19"]] = float(gdp_per_capita_eu27().loc["MALTA"])
    value.loc[["FGINI EU20"]] = float(gdp_per_capita_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI EU21"]] = float(gdp_per_capita_eu27().loc["POLAND"])
    value.loc[["FGINI EU22"]] = float(gdp_per_capita_eu27().loc["PORTUGAL"])
    value.loc[["FGINI EU23"]] = float(gdp_per_capita_eu27().loc["ROMANIA"])
    value.loc[["FGINI EU24"]] = float(gdp_per_capita_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI EU25"]] = float(gdp_per_capita_eu27().loc["SLOVENIA"])
    value.loc[["FGINI EU26"]] = float(gdp_per_capita_eu27().loc["SPAIN"])
    value.loc[["FGINI EU27"]] = float(gdp_per_capita_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="GDP pc EU27 ordered",
    units="Mdollars 2015/people",
    subscripts=["FGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_pc_eu27_gini": 1},
)
def gdp_pc_eu27_ordered():
    return vector_sort_order(gdp_pc_eu27_gini(), 1)


@component.add(
    name="GDP per capita EU27",
    units="Mdollars 2015/(Year*person)",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "gross_domestic_product_real_supply_side": 1,
        "population_35_regions": 1,
    },
)
def gdp_per_capita_eu27():
    return gross_domestic_product_real_supply_side().loc[
        _subscript_dict["REGIONS EU27 I"]
    ].rename({"REGIONS 35 I": "REGIONS EU27 I"}) / population_35_regions().loc[
        _subscript_dict["REGIONS EU27 I"]
    ].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    )


@component.add(
    name="GDP share EU27",
    units="1",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gross_domestic_product_real_supply_side": 2},
)
def gdp_share_eu27():
    return gross_domestic_product_real_supply_side().loc[
        _subscript_dict["REGIONS EU27 I"]
    ].rename({"REGIONS 35 I": "REGIONS EU27 I"}) / sum(
        gross_domestic_product_real_supply_side()
        .loc[_subscript_dict["REGIONS EU27 I"]]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )


@component.add(
    name="GDP share EU27 ordered",
    units="1",
    subscripts=["SGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_shares_eu27_gini": 1, "gdp_pc_eu27_ordered": 1},
)
def gdp_share_eu27_ordered():
    return vector_reorder(
        xr.DataArray(
            gdp_shares_eu27_gini().values,
            {"SGINI EU I": _subscript_dict["SGINI EU I"]},
            ["SGINI EU I"],
        ),
        xr.DataArray(
            gdp_pc_eu27_ordered().values,
            {"SGINI EU I": _subscript_dict["SGINI EU I"]},
            ["SGINI EU I"],
        ),
    )


@component.add(
    name="GDP share regions",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_real_9r": 2},
)
def gdp_share_regions():
    """
    calculate each region's share of GDP of the world
    """
    return gdp_real_9r() / sum(
        gdp_real_9r().rename({"REGIONS 9 I": "REGIONS 9 I!"}), dim=["REGIONS 9 I!"]
    )


@component.add(
    name="GDP share regions ordered",
    units="1",
    subscripts=["SGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_shares_regions_gini": 1, "gdppc_region_ordered": 1},
)
def gdp_share_regions_ordered():
    """
    order region according to smallest GDP p.c.
    """
    return vector_reorder(
        xr.DataArray(
            gdp_shares_regions_gini().values,
            {"SGINI REGIONS I": _subscript_dict["SGINI REGIONS I"]},
            ["SGINI REGIONS I"],
        ),
        xr.DataArray(
            gdppc_region_ordered().values,
            {"SGINI REGIONS I": _subscript_dict["SGINI REGIONS I"]},
            ["SGINI REGIONS I"],
        ),
    )


@component.add(
    name="GDP shares EU27 gini",
    units="1",
    subscripts=["FGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_eu27": 27},
)
def gdp_shares_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI EU I": _subscript_dict["FGINI EU I"]}, ["FGINI EU I"]
    )
    value.loc[["FGINI EU1"]] = float(gdp_share_eu27().loc["AUSTRIA"])
    value.loc[["FGINI EU2"]] = float(gdp_share_eu27().loc["BELGIUM"])
    value.loc[["FGINI EU3"]] = float(gdp_share_eu27().loc["BULGARIA"])
    value.loc[["FGINI EU4"]] = float(gdp_share_eu27().loc["CROATIA"])
    value.loc[["FGINI EU5"]] = float(gdp_share_eu27().loc["CYPRUS"])
    value.loc[["FGINI EU6"]] = float(gdp_share_eu27().loc["CZECH REPUBLIC"])
    value.loc[["FGINI EU7"]] = float(gdp_share_eu27().loc["DENMARK"])
    value.loc[["FGINI EU8"]] = float(gdp_share_eu27().loc["ESTONIA"])
    value.loc[["FGINI EU9"]] = float(gdp_share_eu27().loc["FINLAND"])
    value.loc[["FGINI EU10"]] = float(gdp_share_eu27().loc["FRANCE"])
    value.loc[["FGINI EU11"]] = float(gdp_share_eu27().loc["GERMANY"])
    value.loc[["FGINI EU12"]] = float(gdp_share_eu27().loc["GREECE"])
    value.loc[["FGINI EU13"]] = float(gdp_share_eu27().loc["HUNGARY"])
    value.loc[["FGINI EU14"]] = float(gdp_share_eu27().loc["IRELAND"])
    value.loc[["FGINI EU15"]] = float(gdp_share_eu27().loc["ITALY"])
    value.loc[["FGINI EU16"]] = float(gdp_share_eu27().loc["LATVIA"])
    value.loc[["FGINI EU17"]] = float(gdp_share_eu27().loc["LITHUANIA"])
    value.loc[["FGINI EU18"]] = float(gdp_share_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI EU19"]] = float(gdp_share_eu27().loc["MALTA"])
    value.loc[["FGINI EU20"]] = float(gdp_share_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI EU21"]] = float(gdp_share_eu27().loc["POLAND"])
    value.loc[["FGINI EU22"]] = float(gdp_share_eu27().loc["PORTUGAL"])
    value.loc[["FGINI EU23"]] = float(gdp_share_eu27().loc["ROMANIA"])
    value.loc[["FGINI EU24"]] = float(gdp_share_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI EU25"]] = float(gdp_share_eu27().loc["SLOVENIA"])
    value.loc[["FGINI EU26"]] = float(gdp_share_eu27().loc["SPAIN"])
    value.loc[["FGINI EU27"]] = float(gdp_share_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="GDP shares regions gini",
    units="1",
    subscripts=["FGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdp_share_regions": 9},
)
def gdp_shares_regions_gini():
    """
    constructing a new vector including the region's GDP shares
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI REGIONS I": _subscript_dict["FGINI REGIONS I"]},
        ["FGINI REGIONS I"],
    )
    value.loc[["FGINI REGION1"]] = float(gdp_share_regions().loc["EU27"])
    value.loc[["FGINI REGION2"]] = float(gdp_share_regions().loc["UK"])
    value.loc[["FGINI REGION3"]] = float(gdp_share_regions().loc["CHINA"])
    value.loc[["FGINI REGION4"]] = float(gdp_share_regions().loc["EASOC"])
    value.loc[["FGINI REGION5"]] = float(gdp_share_regions().loc["INDIA"])
    value.loc[["FGINI REGION6"]] = float(gdp_share_regions().loc["LATAM"])
    value.loc[["FGINI REGION7"]] = float(gdp_share_regions().loc["RUSSIA"])
    value.loc[["FGINI REGION8"]] = float(gdp_share_regions().loc["USMCA"])
    value.loc[["FGINI REGION9"]] = float(gdp_share_regions().loc["LROW"])
    return value


@component.add(
    name="GDPpc region ordered",
    units="Mdollars 2015/people",
    subscripts=["FGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdppc_regions_gini": 1},
)
def gdppc_region_ordered():
    """
    sorting the vector FGINI_REGIONS, begin with smallest value (=poorest region)
    """
    return vector_sort_order(gdppc_regions_gini(), 1)


@component.add(
    name="GDPpc regions gini",
    units="Mdollars 2015/(Year*person)",
    subscripts=["FGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"gdppc_9r_real": 9},
)
def gdppc_regions_gini():
    """
    constructing a new vector with the GDP p.c. for each region
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI REGIONS I": _subscript_dict["FGINI REGIONS I"]},
        ["FGINI REGIONS I"],
    )
    value.loc[["FGINI REGION1"]] = float(gdppc_9r_real().loc["EU27"])
    value.loc[["FGINI REGION2"]] = float(gdppc_9r_real().loc["UK"])
    value.loc[["FGINI REGION3"]] = float(gdppc_9r_real().loc["CHINA"])
    value.loc[["FGINI REGION4"]] = float(gdppc_9r_real().loc["EASOC"])
    value.loc[["FGINI REGION5"]] = float(gdppc_9r_real().loc["INDIA"])
    value.loc[["FGINI REGION6"]] = float(gdppc_9r_real().loc["LATAM"])
    value.loc[["FGINI REGION7"]] = float(gdppc_9r_real().loc["RUSSIA"])
    value.loc[["FGINI REGION8"]] = float(gdppc_9r_real().loc["USMCA"])
    value.loc[["FGINI REGION9"]] = float(gdppc_9r_real().loc["LROW"])
    return value


@component.add(
    name="GINI disposable income by region",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_shares_ordered": 61,
        "households_disposable_income_cumulate_ordered": 121,
    },
)
def gini_disposable_income_by_region():
    """
    GINI of disposable income by region
    """
    return 1 - (
        households_shares_ordered().loc[:, "gini1"].reset_coords(drop=True)
        * households_disposable_income_cumulate_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini2"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini3"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini4"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini5"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini6"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini7"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini8"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini9"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini10"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini11"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini12"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini13"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini14"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini15"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini16"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini17"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini18"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini19"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini20"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini21"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini22"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini23"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini24"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini25"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini26"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini27"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini28"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini29"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini30"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini31"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini32"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini33"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini34"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini35"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini36"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini37"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini38"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini39"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini40"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini41"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini42"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini43"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini44"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini45"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini46"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini47"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini48"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini49"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini50"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini51"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini52"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini53"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini54"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini55"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini56"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini57"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini58"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini59"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini60"].reset_coords(drop=True)
        + (
            households_disposable_income_cumulate_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
            + households_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        * households_shares_ordered().loc[:, "gini61"].reset_coords(drop=True)
    )


@component.add(
    name="Gini GDPpc EU27",
    units="Dnml",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_lorenz_gdp_eu27": 53, "pop_shares_eu27_ordered": 27},
)
def gini_gdppc_eu27():
    """
    The Gini GDPpc index measures the extent to which the distribution of GDP between WILIAM regions deviates from a perfectly equal distribution. A Gini index of 0 represents perfect equality, while an index of 1 implies perfect inequality. Formula for calculating Gini: 1 - 2*the area under the lorentz curve (=cumulated GDP). This translates into the above form.
    """
    return 1 - (
        float(cumulative_lorenz_gdp_eu27().loc["SGINI EU1"])
        * float(pop_shares_eu27_ordered().loc["SGINI EU1"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU1"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU2"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU2"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU2"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU3"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU3"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU3"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU4"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU4"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU4"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU5"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU5"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU5"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU6"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU6"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU6"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU7"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU7"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU7"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU8"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU8"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU8"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU9"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU9"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU9"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU10"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU10"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU10"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU11"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU11"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU11"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU12"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU12"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU12"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU13"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU13"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU13"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU14"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU14"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU14"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU15"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU15"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU15"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU16"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU16"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU16"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU17"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU17"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU17"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU18"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU18"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU18"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU19"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU19"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU19"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU20"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU20"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU20"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU21"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU21"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU21"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU22"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU22"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU22"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU23"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU23"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU23"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU24"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU24"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU24"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU25"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU25"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU25"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU26"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU26"])
        + (
            float(cumulative_lorenz_gdp_eu27().loc["SGINI EU26"])
            + float(cumulative_lorenz_gdp_eu27().loc["SGINI EU27"])
        )
        * float(pop_shares_eu27_ordered().loc["SGINI EU27"])
    )


@component.add(
    name="GINI GDPpc regions",
    units="DMNL",
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"cumulative_lorenz_gdp_regions": 17, "pop_shares_regions_ordered": 9},
)
def gini_gdppc_regions():
    """
    The Gini GDPpc index measures the extent to which the distribution of GDP between WILIAM regions deviates from a perfectly equal distribution. A Gini index of 0 represents perfect equality, while an index of 1 implies perfect inequality. Formula for calculating Gini: 1 - 2*the area under the lorentz curve (=cumulated GDP). This translates into the above form.
    """
    return 1 - (
        float(cumulative_lorenz_gdp_regions().loc["SGINI REGION1"])
        * float(pop_shares_regions_ordered().loc["SGINI REGION1"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION1"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION2"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION2"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION2"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION3"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION3"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION3"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION4"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION4"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION4"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION5"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION5"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION5"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION6"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION6"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION6"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION7"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION7"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION7"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION8"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION8"])
        + (
            float(cumulative_lorenz_gdp_regions().loc["SGINI REGION8"])
            + float(cumulative_lorenz_gdp_regions().loc["SGINI REGION9"])
        )
        * float(pop_shares_regions_ordered().loc["SGINI REGION9"])
    )


@component.add(
    name="GINI personal disposable income by region",
    units="DMNL",
    subscripts=["REGIONS 35 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "people_shares_ordered": 61,
        "personal_disposable_income_cumulate_ordered": 121,
    },
)
def gini_personal_disposable_income_by_region():
    """
    GINI of disposable income by region
    """
    return 1 - (
        people_shares_ordered().loc[:, "gini1"].reset_coords(drop=True)
        * personal_disposable_income_cumulate_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini2"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini3"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini4"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini5"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini6"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini7"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini8"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini9"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini10"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini11"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini12"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini13"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini14"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini15"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini16"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini17"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini18"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini19"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini20"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini21"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini22"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini23"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini24"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini25"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini26"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini27"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini28"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini29"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini30"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini31"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini32"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini33"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini34"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini35"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini36"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini37"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini38"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini39"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini40"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini41"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini42"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini43"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini44"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini45"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini46"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini47"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini48"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini49"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini50"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini51"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini52"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini53"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini54"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini55"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini56"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini57"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini58"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini59"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini60"].reset_coords(drop=True)
        + (
            personal_disposable_income_cumulate_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
            + personal_disposable_income_cumulate_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        * people_shares_ordered().loc[:, "gini61"].reset_coords(drop=True)
    )


@component.add(
    name="households disposable income cumulate ordered",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_disposable_income_share_ordered": 1891},
)
def households_disposable_income_cumulate_ordered():
    """
    cumulative ordered share of households disposable income
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "GINI ORDER I": _subscript_dict["GINI ORDER I"],
        },
        ["REGIONS 35 I", "GINI ORDER I"],
    )
    value.loc[:, ["gini1"]] = (
        households_disposable_income_share_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        .expand_dims({"GINI ORDER I": ["gini1"]}, 1)
        .values
    )
    value.loc[:, ["gini2"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini2"]}, 1)
        .values
    )
    value.loc[:, ["gini3"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini3"]}, 1)
        .values
    )
    value.loc[:, ["gini4"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini4"]}, 1)
        .values
    )
    value.loc[:, ["gini5"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini5"]}, 1)
        .values
    )
    value.loc[:, ["gini6"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini6"]}, 1)
        .values
    )
    value.loc[:, ["gini7"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini7"]}, 1)
        .values
    )
    value.loc[:, ["gini8"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini8"]}, 1)
        .values
    )
    value.loc[:, ["gini9"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini9"]}, 1)
        .values
    )
    value.loc[:, ["gini10"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini10"]}, 1)
        .values
    )
    value.loc[:, ["gini11"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini11"]}, 1)
        .values
    )
    value.loc[:, ["gini12"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini12"]}, 1)
        .values
    )
    value.loc[:, ["gini13"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini13"]}, 1)
        .values
    )
    value.loc[:, ["gini14"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini14"]}, 1)
        .values
    )
    value.loc[:, ["gini15"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini15"]}, 1)
        .values
    )
    value.loc[:, ["gini16"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini16"]}, 1)
        .values
    )
    value.loc[:, ["gini17"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini17"]}, 1)
        .values
    )
    value.loc[:, ["gini18"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini18"]}, 1)
        .values
    )
    value.loc[:, ["gini19"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini19"]}, 1)
        .values
    )
    value.loc[:, ["gini20"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini20"]}, 1)
        .values
    )
    value.loc[:, ["gini21"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini21"]}, 1)
        .values
    )
    value.loc[:, ["gini22"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini22"]}, 1)
        .values
    )
    value.loc[:, ["gini23"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini23"]}, 1)
        .values
    )
    value.loc[:, ["gini24"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini24"]}, 1)
        .values
    )
    value.loc[:, ["gini25"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini25"]}, 1)
        .values
    )
    value.loc[:, ["gini26"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini26"]}, 1)
        .values
    )
    value.loc[:, ["gini27"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini27"]}, 1)
        .values
    )
    value.loc[:, ["gini28"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini28"]}, 1)
        .values
    )
    value.loc[:, ["gini29"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini29"]}, 1)
        .values
    )
    value.loc[:, ["gini30"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini30"]}, 1)
        .values
    )
    value.loc[:, ["gini31"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini31"]}, 1)
        .values
    )
    value.loc[:, ["gini32"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini32"]}, 1)
        .values
    )
    value.loc[:, ["gini33"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini33"]}, 1)
        .values
    )
    value.loc[:, ["gini34"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini34"]}, 1)
        .values
    )
    value.loc[:, ["gini35"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini35"]}, 1)
        .values
    )
    value.loc[:, ["gini36"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini36"]}, 1)
        .values
    )
    value.loc[:, ["gini37"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini37"]}, 1)
        .values
    )
    value.loc[:, ["gini38"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini38"]}, 1)
        .values
    )
    value.loc[:, ["gini39"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini39"]}, 1)
        .values
    )
    value.loc[:, ["gini40"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini40"]}, 1)
        .values
    )
    value.loc[:, ["gini41"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini41"]}, 1)
        .values
    )
    value.loc[:, ["gini42"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini42"]}, 1)
        .values
    )
    value.loc[:, ["gini43"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini43"]}, 1)
        .values
    )
    value.loc[:, ["gini44"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini44"]}, 1)
        .values
    )
    value.loc[:, ["gini45"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini45"]}, 1)
        .values
    )
    value.loc[:, ["gini46"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini46"]}, 1)
        .values
    )
    value.loc[:, ["gini47"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini47"]}, 1)
        .values
    )
    value.loc[:, ["gini48"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini48"]}, 1)
        .values
    )
    value.loc[:, ["gini49"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini49"]}, 1)
        .values
    )
    value.loc[:, ["gini50"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini50"]}, 1)
        .values
    )
    value.loc[:, ["gini51"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini51"]}, 1)
        .values
    )
    value.loc[:, ["gini52"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini52"]}, 1)
        .values
    )
    value.loc[:, ["gini53"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini53"]}, 1)
        .values
    )
    value.loc[:, ["gini54"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini54"]}, 1)
        .values
    )
    value.loc[:, ["gini55"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini55"]}, 1)
        .values
    )
    value.loc[:, ["gini56"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini56"]}, 1)
        .values
    )
    value.loc[:, ["gini57"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini57"]}, 1)
        .values
    )
    value.loc[:, ["gini58"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini58"]}, 1)
        .values
    )
    value.loc[:, ["gini59"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini59"]}, 1)
        .values
    )
    value.loc[:, ["gini60"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini60"]}, 1)
        .values
    )
    value.loc[:, ["gini61"]] = (
        (
            households_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + households_disposable_income_share_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini61"]}, 1)
        .values
    )
    return value


@component.add(
    name="households disposable income ordered",
    units="$/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_disposable_income": 1},
)
def households_disposable_income_ordered():
    """
    households disposable income ordered
    """
    return vector_sort_order(households_disposable_income(), 1)


@component.add(
    name="households disposable income share ordered",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income_shares": 1,
        "households_disposable_income_ordered": 1,
    },
)
def households_disposable_income_share_ordered():
    """
    share of disposable income of each households type on total disposable income, ordered
    """
    return vector_reorder(
        xr.DataArray(
            households_disposable_income_shares().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
        xr.DataArray(
            households_disposable_income_ordered().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
    )


@component.add(
    name="households disposable income shares",
    units="DMNL",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 2,
        "number_of_households_by_income_and_type": 2,
    },
)
def households_disposable_income_shares():
    return zidz(
        households_disposable_income() * number_of_households_by_income_and_type(),
        sum(
            households_disposable_income().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_households_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        ).expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1),
    )


@component.add(
    name="households shares",
    units="DMNL",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_households_by_income_and_type": 2},
)
def households_shares():
    """
    share of each household type on total households by region
    """
    return number_of_households_by_income_and_type() / sum(
        number_of_households_by_income_and_type().rename(
            {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
        ),
        dim=["HOUSEHOLDS I!"],
    )


@component.add(
    name="households shares ordered",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"households_shares": 1, "households_disposable_income_ordered": 1},
)
def households_shares_ordered():
    """
    share of each household type ordered according to income level
    """
    return vector_reorder(
        xr.DataArray(
            households_shares().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
        xr.DataArray(
            households_disposable_income_ordered().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
    )


@component.add(
    name="number of people by income and type",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "number_of_households_by_income_and_type": 1,
        "people_per_household_by_income_and_type": 1,
    },
)
def number_of_people_by_income_and_type():
    return (
        number_of_households_by_income_and_type()
        * people_per_household_by_income_and_type()
    )


@component.add(
    name="people shares by income and type",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"number_of_people_by_income_and_type": 2},
)
def people_shares_by_income_and_type():
    return zidz(
        number_of_people_by_income_and_type(),
        sum(
            number_of_people_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        ).expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1),
    )


@component.add(
    name="people shares ordered",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "people_shares_by_income_and_type": 1,
        "personal_disposable_income_ordered": 1,
    },
)
def people_shares_ordered():
    return vector_reorder(
        xr.DataArray(
            people_shares_by_income_and_type().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
        xr.DataArray(
            personal_disposable_income_ordered().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
    )


@component.add(
    name="personal disposable income",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "households_disposable_income": 1,
        "people_per_household_by_income_and_type": 1,
    },
)
def personal_disposable_income():
    return zidz(
        households_disposable_income(), people_per_household_by_income_and_type()
    )


@component.add(
    name="personal disposable income cumulate ordered",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"personal_disposable_income_share_ordered": 1891},
)
def personal_disposable_income_cumulate_ordered():
    """
    cumulative ordered share of households disposable income
    """
    value = xr.DataArray(
        np.nan,
        {
            "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
            "GINI ORDER I": _subscript_dict["GINI ORDER I"],
        },
        ["REGIONS 35 I", "GINI ORDER I"],
    )
    value.loc[:, ["gini1"]] = (
        personal_disposable_income_share_ordered()
        .loc[:, "gini1"]
        .reset_coords(drop=True)
        .expand_dims({"GINI ORDER I": ["gini1"]}, 1)
        .values
    )
    value.loc[:, ["gini2"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini2"]}, 1)
        .values
    )
    value.loc[:, ["gini3"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini3"]}, 1)
        .values
    )
    value.loc[:, ["gini4"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini4"]}, 1)
        .values
    )
    value.loc[:, ["gini5"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini5"]}, 1)
        .values
    )
    value.loc[:, ["gini6"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini6"]}, 1)
        .values
    )
    value.loc[:, ["gini7"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini7"]}, 1)
        .values
    )
    value.loc[:, ["gini8"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini8"]}, 1)
        .values
    )
    value.loc[:, ["gini9"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini9"]}, 1)
        .values
    )
    value.loc[:, ["gini10"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini10"]}, 1)
        .values
    )
    value.loc[:, ["gini11"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini11"]}, 1)
        .values
    )
    value.loc[:, ["gini12"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini12"]}, 1)
        .values
    )
    value.loc[:, ["gini13"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini13"]}, 1)
        .values
    )
    value.loc[:, ["gini14"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini14"]}, 1)
        .values
    )
    value.loc[:, ["gini15"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini15"]}, 1)
        .values
    )
    value.loc[:, ["gini16"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini16"]}, 1)
        .values
    )
    value.loc[:, ["gini17"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini17"]}, 1)
        .values
    )
    value.loc[:, ["gini18"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini18"]}, 1)
        .values
    )
    value.loc[:, ["gini19"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini19"]}, 1)
        .values
    )
    value.loc[:, ["gini20"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini20"]}, 1)
        .values
    )
    value.loc[:, ["gini21"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini21"]}, 1)
        .values
    )
    value.loc[:, ["gini22"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini22"]}, 1)
        .values
    )
    value.loc[:, ["gini23"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini23"]}, 1)
        .values
    )
    value.loc[:, ["gini24"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini24"]}, 1)
        .values
    )
    value.loc[:, ["gini25"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini25"]}, 1)
        .values
    )
    value.loc[:, ["gini26"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini26"]}, 1)
        .values
    )
    value.loc[:, ["gini27"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini27"]}, 1)
        .values
    )
    value.loc[:, ["gini28"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini28"]}, 1)
        .values
    )
    value.loc[:, ["gini29"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini29"]}, 1)
        .values
    )
    value.loc[:, ["gini30"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini30"]}, 1)
        .values
    )
    value.loc[:, ["gini31"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini31"]}, 1)
        .values
    )
    value.loc[:, ["gini32"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini32"]}, 1)
        .values
    )
    value.loc[:, ["gini33"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini33"]}, 1)
        .values
    )
    value.loc[:, ["gini34"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini34"]}, 1)
        .values
    )
    value.loc[:, ["gini35"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini35"]}, 1)
        .values
    )
    value.loc[:, ["gini36"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini36"]}, 1)
        .values
    )
    value.loc[:, ["gini37"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini37"]}, 1)
        .values
    )
    value.loc[:, ["gini38"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini38"]}, 1)
        .values
    )
    value.loc[:, ["gini39"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini39"]}, 1)
        .values
    )
    value.loc[:, ["gini40"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini40"]}, 1)
        .values
    )
    value.loc[:, ["gini41"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini41"]}, 1)
        .values
    )
    value.loc[:, ["gini42"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini42"]}, 1)
        .values
    )
    value.loc[:, ["gini43"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini43"]}, 1)
        .values
    )
    value.loc[:, ["gini44"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini44"]}, 1)
        .values
    )
    value.loc[:, ["gini45"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini45"]}, 1)
        .values
    )
    value.loc[:, ["gini46"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini46"]}, 1)
        .values
    )
    value.loc[:, ["gini47"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini47"]}, 1)
        .values
    )
    value.loc[:, ["gini48"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini48"]}, 1)
        .values
    )
    value.loc[:, ["gini49"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini49"]}, 1)
        .values
    )
    value.loc[:, ["gini50"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini50"]}, 1)
        .values
    )
    value.loc[:, ["gini51"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini51"]}, 1)
        .values
    )
    value.loc[:, ["gini52"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini52"]}, 1)
        .values
    )
    value.loc[:, ["gini53"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini53"]}, 1)
        .values
    )
    value.loc[:, ["gini54"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini54"]}, 1)
        .values
    )
    value.loc[:, ["gini55"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini55"]}, 1)
        .values
    )
    value.loc[:, ["gini56"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini56"]}, 1)
        .values
    )
    value.loc[:, ["gini57"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini57"]}, 1)
        .values
    )
    value.loc[:, ["gini58"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini58"]}, 1)
        .values
    )
    value.loc[:, ["gini59"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini59"]}, 1)
        .values
    )
    value.loc[:, ["gini60"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini60"]}, 1)
        .values
    )
    value.loc[:, ["gini61"]] = (
        (
            personal_disposable_income_share_ordered()
            .loc[:, "gini1"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini2"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini3"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini4"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini5"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini6"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini7"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini8"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini9"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini10"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini11"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini12"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini13"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini14"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini15"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini16"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini17"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini18"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini19"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini20"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini21"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini22"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini23"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini24"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini25"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini26"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini27"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini28"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini29"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini30"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini31"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini32"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini33"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini34"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini35"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini36"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini37"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini38"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini39"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini40"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini41"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini42"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini43"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini44"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini45"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini46"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini47"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini48"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini49"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini50"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini51"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini52"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini53"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini54"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini55"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini56"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini57"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini58"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini59"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini60"]
            .reset_coords(drop=True)
            + personal_disposable_income_share_ordered()
            .loc[:, "gini61"]
            .reset_coords(drop=True)
        )
        .expand_dims({"GINI ORDER I": ["gini61"]}, 1)
        .values
    )
    return value


@component.add(
    name="personal disposable income ordered",
    units="$/Year",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"personal_disposable_income": 1},
)
def personal_disposable_income_ordered():
    """
    households disposable income ordered
    """
    return vector_sort_order(personal_disposable_income(), 1)


@component.add(
    name="personal disposable income share ordered",
    units="DMNL",
    subscripts=["REGIONS 35 I", "GINI ORDER I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "personal_disposable_income_shares": 1,
        "personal_disposable_income_ordered": 1,
    },
)
def personal_disposable_income_share_ordered():
    """
    share of disposable income of each households type on total disposable income, ordered
    """
    return vector_reorder(
        xr.DataArray(
            personal_disposable_income_shares().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
        xr.DataArray(
            personal_disposable_income_ordered().values,
            {
                "REGIONS 35 I": _subscript_dict["REGIONS 35 I"],
                "GINI ORDER I": _subscript_dict["GINI ORDER I"],
            },
            ["REGIONS 35 I", "GINI ORDER I"],
        ),
    )


@component.add(
    name="personal disposable income shares",
    subscripts=["REGIONS 35 I", "HOUSEHOLDS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={
        "personal_disposable_income": 2,
        "number_of_people_by_income_and_type": 2,
    },
)
def personal_disposable_income_shares():
    return zidz(
        personal_disposable_income() * number_of_people_by_income_and_type(),
        sum(
            personal_disposable_income().rename({"HOUSEHOLDS I": "HOUSEHOLDS I!"})
            * number_of_people_by_income_and_type().rename(
                {"HOUSEHOLDS I": "HOUSEHOLDS I!"}
            ),
            dim=["HOUSEHOLDS I!"],
        ).expand_dims({"HOUSEHOLDS I": _subscript_dict["HOUSEHOLDS I"]}, 1),
    )


@component.add(
    name="pop shares eu27",
    units="1",
    subscripts=["REGIONS EU27 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_35_regions": 2},
)
def pop_shares_eu27():
    return population_35_regions().loc[_subscript_dict["REGIONS EU27 I"]].rename(
        {"REGIONS 35 I": "REGIONS EU27 I"}
    ) / sum(
        population_35_regions()
        .loc[_subscript_dict["REGIONS EU27 I"]]
        .rename({"REGIONS 35 I": "REGIONS EU27 I!"}),
        dim=["REGIONS EU27 I!"],
    )


@component.add(
    name="pop shares eu27 gini",
    units="1",
    subscripts=["FGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_eu27": 27},
)
def pop_shares_eu27_gini():
    value = xr.DataArray(
        np.nan, {"FGINI EU I": _subscript_dict["FGINI EU I"]}, ["FGINI EU I"]
    )
    value.loc[["FGINI EU1"]] = float(pop_shares_eu27().loc["AUSTRIA"])
    value.loc[["FGINI EU2"]] = float(pop_shares_eu27().loc["BELGIUM"])
    value.loc[["FGINI EU3"]] = float(pop_shares_eu27().loc["BULGARIA"])
    value.loc[["FGINI EU4"]] = float(pop_shares_eu27().loc["CROATIA"])
    value.loc[["FGINI EU5"]] = float(pop_shares_eu27().loc["CYPRUS"])
    value.loc[["FGINI EU6"]] = float(pop_shares_eu27().loc["CZECH REPUBLIC"])
    value.loc[["FGINI EU7"]] = float(pop_shares_eu27().loc["DENMARK"])
    value.loc[["FGINI EU8"]] = float(pop_shares_eu27().loc["ESTONIA"])
    value.loc[["FGINI EU9"]] = float(pop_shares_eu27().loc["FINLAND"])
    value.loc[["FGINI EU10"]] = float(pop_shares_eu27().loc["FRANCE"])
    value.loc[["FGINI EU11"]] = float(pop_shares_eu27().loc["GERMANY"])
    value.loc[["FGINI EU12"]] = float(pop_shares_eu27().loc["GREECE"])
    value.loc[["FGINI EU13"]] = float(pop_shares_eu27().loc["HUNGARY"])
    value.loc[["FGINI EU14"]] = float(pop_shares_eu27().loc["IRELAND"])
    value.loc[["FGINI EU15"]] = float(pop_shares_eu27().loc["ITALY"])
    value.loc[["FGINI EU16"]] = float(pop_shares_eu27().loc["LATVIA"])
    value.loc[["FGINI EU17"]] = float(pop_shares_eu27().loc["LITHUANIA"])
    value.loc[["FGINI EU18"]] = float(pop_shares_eu27().loc["LUXEMBOURG"])
    value.loc[["FGINI EU19"]] = float(pop_shares_eu27().loc["MALTA"])
    value.loc[["FGINI EU20"]] = float(pop_shares_eu27().loc["NETHERLANDS"])
    value.loc[["FGINI EU21"]] = float(pop_shares_eu27().loc["POLAND"])
    value.loc[["FGINI EU22"]] = float(pop_shares_eu27().loc["PORTUGAL"])
    value.loc[["FGINI EU23"]] = float(pop_shares_eu27().loc["ROMANIA"])
    value.loc[["FGINI EU24"]] = float(pop_shares_eu27().loc["SLOVAKIA"])
    value.loc[["FGINI EU25"]] = float(pop_shares_eu27().loc["SLOVENIA"])
    value.loc[["FGINI EU26"]] = float(pop_shares_eu27().loc["SPAIN"])
    value.loc[["FGINI EU27"]] = float(pop_shares_eu27().loc["SWEDEN"])
    return value


@component.add(
    name="pop shares EU27 ordered",
    units="1",
    subscripts=["SGINI EU I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_eu27_gini": 1, "gdp_pc_eu27_ordered": 1},
)
def pop_shares_eu27_ordered():
    return vector_reorder(
        xr.DataArray(
            pop_shares_eu27_gini().values,
            {"SGINI EU I": _subscript_dict["SGINI EU I"]},
            ["SGINI EU I"],
        ),
        xr.DataArray(
            gdp_pc_eu27_ordered().values,
            {"SGINI EU I": _subscript_dict["SGINI EU I"]},
            ["SGINI EU I"],
        ),
    )


@component.add(
    name="pop shares regions",
    units="1",
    subscripts=["REGIONS 9 I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"population_9_regions": 2},
)
def pop_shares_regions():
    """
    calculating each region's share of world population
    """
    return population_9_regions() / sum(
        population_9_regions().rename({"REGIONS 9 I": "REGIONS 9 I!"}),
        dim=["REGIONS 9 I!"],
    )


@component.add(
    name="pop shares regions gini",
    units="1",
    subscripts=["FGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_regions": 9},
)
def pop_shares_regions_gini():
    """
    constructing a new vector with the population shares
    """
    value = xr.DataArray(
        np.nan,
        {"FGINI REGIONS I": _subscript_dict["FGINI REGIONS I"]},
        ["FGINI REGIONS I"],
    )
    value.loc[["FGINI REGION1"]] = float(pop_shares_regions().loc["EU27"])
    value.loc[["FGINI REGION2"]] = float(pop_shares_regions().loc["UK"])
    value.loc[["FGINI REGION3"]] = float(pop_shares_regions().loc["CHINA"])
    value.loc[["FGINI REGION4"]] = float(pop_shares_regions().loc["EASOC"])
    value.loc[["FGINI REGION5"]] = float(pop_shares_regions().loc["INDIA"])
    value.loc[["FGINI REGION6"]] = float(pop_shares_regions().loc["LATAM"])
    value.loc[["FGINI REGION7"]] = float(pop_shares_regions().loc["RUSSIA"])
    value.loc[["FGINI REGION8"]] = float(pop_shares_regions().loc["USMCA"])
    value.loc[["FGINI REGION9"]] = float(pop_shares_regions().loc["LROW"])
    return value


@component.add(
    name="pop shares regions ordered",
    units="1",
    subscripts=["SGINI REGIONS I"],
    comp_type="Auxiliary",
    comp_subtype="Normal",
    depends_on={"pop_shares_regions_gini": 1, "gdppc_region_ordered": 1},
)
def pop_shares_regions_ordered():
    """
    order vector containing the population shares, beginning with the region with the smallest GDP p.c.
    """
    return vector_reorder(
        xr.DataArray(
            pop_shares_regions_gini().values,
            {"SGINI REGIONS I": _subscript_dict["SGINI REGIONS I"]},
            ["SGINI REGIONS I"],
        ),
        xr.DataArray(
            gdppc_region_ordered().values,
            {"SGINI REGIONS I": _subscript_dict["SGINI REGIONS I"]},
            ["SGINI REGIONS I"],
        ),
    )
