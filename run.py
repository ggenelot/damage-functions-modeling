import pysd
import xarray as xr
import warnings
import pandas as pd
import numpy as np

print('Executing run.py')

print('Loading model...')

# Suppress specific warnings to avoid cluttering the output
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# Load model
model = pysd.read_vensim('WILIAM/WILIAM.mdl',
                         split_views=True, 
                         subview_sep=["."], 
                         errors='ignore')

print('Model loaded')

# Saving the variables 
variables = model.doc

# Cleaning the variables and identifiying the model and equation 
variables['Real Name'] = variables['Real Name'].str.replace('"', '')
variables['Model'] = variables['Real Name'].str.split(':').str[0]
variables['Equation'] = variables['Real Name'].str.split(':').str[1]
variables['isEquation'] = variables['Real Name'].str.split(':').str[2].str.strip().str.startswith('EQ')
variables.loc[variables['Equation'].isnull(), 'Model'] = np.nan


variables.to_csv('variables.csv')
variables_modelled = variables[variables['Model'].notna()]
variables_modelled_names = variables_modelled['Py Name'].values


# Adding other variables of interest

interest_variables = [
    "gini_gdppc_regions", 
    "gini_gdppc_eu27", 
    "temperature_change", 
    "temperature_change_in_35regions", 
    "total_population", 
    "population_35_regions", 
    "total_radiative_forcing"
]

output_variables = np.concatenate([variables_modelled_names, interest_variables])


runs = pd.read_csv('run_manager.csv')



## Preparing the dataset 

ds_path = 'results/batch/run_0.nc'

ds = xr.open_dataset(ds_path)

# Add missing dimensions if they don't exist
for dim in ['RCP', 'exponent', 'norm_constant']:
    if dim not in ds.dims:
        ds = ds.expand_dims({dim: runs[dim].unique()})

# Create or update coordinates
ds = ds.assign_coords({
    'RCP': runs['RCP'].unique(),
    'exponent': runs['exponent'].unique(),
    'norm_constant': runs['norm_constant'].unique()
})


# Reducing the number of runs to test the model
runs = runs.head(5)


## Preparing to vary the radiative forcing

# Load the basic radiative forcing 


forcing = pd.read_csv('full_rcp.csv')



# Iterate over the rows of the run manager
for index, run in runs.iterrows():

    print("Initializing forcing... ")
    rcp = run['RCP']
    forcing_columns = [rcp,  'time']
    total_forcing = forcing[forcing_columns]
    total_forcing = pd.Series(index=total_forcing['time'], data=total_forcing[rcp].values)
    print("Forcing initialized")
    exponent = run['exponent']
    norm_constant = run['norm_constant']

    print(f"Running model for run {run['run_number']} with RCP {rcp}, exponent {exponent} and norm_constant {norm_constant}")

    # Run the model
    run = model.run(progress=True,
                    params={'total radiative forcing': total_forcing, 
                            '"EXTRA: EXTRA: exponent"' : exponent,
                            '"EXTRA: EXTRA: normalisation constant"': norm_constant
                            },
                    return_columns=output_variables,
                    final_time=run['final_time'])

    result_variables = run.columns 

    for variable in result_variables: 
        try:   
                ds[variable].loc[dict(RCP=rcp, exponent = exponent, norm_constant = norm_constant)]
                print(f"Added variable {variable} to the dataset")
        except:
                pass
        
ds.to_netcdf('results/batch/run_with_results.nc')

warnings.resetwarnings()

print('Done every run')

