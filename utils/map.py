import geopandas as gpd
import matplotlib.pyplot as plt


def map_variable(data, year, europe=True, cmap="cividis", shapefile_location='../../../WILIAM_v1.3/geography/output_countries/countries.shp'):

    # Load variable name from the df
    variable = data.columns[2]

    # Load map
    map = gpd.read_file(shapefile_location)  

    if europe:
    # Define the bounding box coordinates for continental European Union
        x_min = -15
        x_max = 40
        y_min = 30
        y_max = 70

        map = map.cx[x_min:x_max, y_min:y_max]
        #map = map.to_crs(epsg=3035)

    data_map = data[data['time'] == year]

    map_phenomenon = map.merge(data_map, left_on='Region_WIL', right_on='REGIONS 35 I', how='left')

    # Plot the map
    fig, ax = plt.subplots(figsize=(10, 10))
    map.plot(ax=ax, color='white', edgecolor='lightgray')
    map_phenomenon.plot(ax=ax, 
                        cmap=cmap,
                        column=variable, 
                        legend=True, 
                        legend_kwds={'label': "Agricultural damage in FUND (% of agricultural production)", 
                                    'orientation': "horizontal"})

    # Set the title and axis labels
    ax.set_title(f'European Union Map of {variable} in {year}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    ax.set_axis_off()

    if europe:
        # Set the x and y limits of the plot
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

    # Show the plot
    plt.show()
