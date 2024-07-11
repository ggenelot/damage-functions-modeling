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

# Reducing the number of runs to test the model

runs = runs.head(5)

## Preparing to vary the radiative forcing

# Load the basic radiative forcing 

rcps = ['RCP6.0', 'RCP4.5', 'RCP2.6', 'RCP8.5']

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

    print{f"Running model for run {run['run_number']} with RCP {rcp}, exponent {exponent} and norm_constant {norm_constant}"}

    # Run the model
    run = model.run(progress=True,
                    params={'total radiative forcing': total_forcing, 
                            '"EXTRA: EXTRA: exponent"' : exponent,
                            '"EXTRA: EXTRA: normalisation constant"': norm_constant
                            },
                    return_columns=output_variables,
                    final_time=run['final_time'],  
                    output_file=f'results/batch/run_{str(run["run_number"])}.nc')


warnings.resetwarnings()

print('Done every run')

