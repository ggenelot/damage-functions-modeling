print('Executing run.py')

import pysd
import xarray as xr
import warnings
import pandas as pd
import numpy as np


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

run_num =  20 #len(runs)
ds = ds.expand_dims({"Run": run_num}).assign_coords({"Run": range(0, run_num)})


# Reducing the number of runs to test the model
runs = runs.head(run_num)


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
    
    exponent = np.random.normal(0, 2, 1)[0]
    norm_constant = np.random.uniform(10000, 50000, 1)[0]

    print(f"Running model for run {run['run_number']} with RCP {rcp}, exponent {exponent} and norm_constant {norm_constant}")

    # Run the model
    run = model.run(progress=True,
                    params={'total radiative forcing': total_forcing, 
                            '"EXTRA: EXTRA: exponent"' : exponent,
                            '"EXTRA: EXTRA: normalisation constant"': norm_constant
                            },
                    return_columns=output_variables,
                    final_time=2050)

    result_variables = run.columns 

    extra_extra_exponent_copy = ds["extra_extra_exponent"].copy()
    extra_extra_exponent_copy.loc[dict(Run = index)] = exponent
    ds["extra_extra_exponent"] = extra_extra_exponent_copy

    extra_extra_normalisation_constant_copy = ds["extra_extra_normalisation_constant"].copy()
    extra_extra_normalisation_constant_copy.loc[dict(Run = index)] = norm_constant
    ds["extra_extra_normalisation_constant"] = extra_extra_normalisation_constant_copy


    for variable in result_variables: 
        try:   
                ds[variable].loc[dict(Run = index)] = run[variable].values
                print(f"Added variable {variable} to the dataset.")
        except:
                pass
        
ds.to_netcdf('results/batch/run_with_1200.nc')
ds.close()
warnings.resetwarnings()

print('Done every run')

