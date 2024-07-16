print('Executing run.py')

import pysd
import xarray as xr
import warnings
import pandas as pd
import numpy as np
import utils.variables as vr


#############################################################
# Load the model and the variables
#############################################################

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



variables["Interest"] = variables["Py Name"].apply(lambda x: vr.isInterest(x))
interest_variables = variables[variables["Interest"] == True]["Py Name"].values

variables.to_csv('variables.csv')
variables_modelled = variables[variables['Model'].notna()]
variables_modelled_names = variables_modelled['Py Name'].values


# Adding other variables of interest



output_variables = np.concatenate([variables_modelled_names, interest_variables])


runs = pd.read_csv('run_manager.csv')



## Preparing to vary the radiative forcing

# Load the basic radiative forcing 
forcing = pd.read_csv('full_rcp.csv')

# Run the model a first time to initialize the dataset
output_ds_path = 'results/batch/run_ds_16_07.nc'

initial_time = 2005
final_time = 2050
time_step = 5 
time_span = time = np.linspace(initial_time, final_time, num=(final_time - initial_time)//time_step + 1)


exponent_values = np.random.normal(0, 1, len(time_span))
exponent = pd.Series(index=time_span, data=exponent_values)

norm_constant_values = np.random.uniform(10000, 50000, len(time_span))
norm_constant = pd.Series(index=time_span, data=norm_constant_values)





############################################################################################################
# Initial run
############################################################################################################


print(f"Initializing the model for the first run")


# Run the model
run = model.run(progress=True,
                params={'"EXTRA: EXTRA: exponent"' : exponent,
                        '"EXTRA: EXTRA: normalisation constant"': norm_constant
                        }, 
                output_file=output_ds_path,
                return_columns=output_variables,
                final_time=final_time, 
                time_step=time_step)


## Preparing the dataset 

ds = xr.open_dataset(output_ds_path)

run_num =  3 #len(runs)
ds = ds.expand_dims({"Run": run_num}).assign_coords({"Run": range(0, run_num)})

runs = runs.head(run_num)



############################################################################################################
# Other runs
############################################################################################################

# Iterate over the rows of the run manager
for index, run in runs.iterrows():
    
    first_run = True

    print("Initializing forcing... ")
    rcp = run['RCP']
    forcing_columns = [rcp,  'time']
    total_forcing = forcing[forcing_columns]
    total_forcing = pd.Series(index=total_forcing['time'], data=total_forcing[rcp].values)
    print("Forcing initialized")
    
    exponent_values = np.random.normal(0, 1, len(time_span))
    exponent = pd.Series(index=time_span, data=exponent_values)

    norm_constant_values = np.random.uniform(10000, 50000, len(time_span))
    norm_constant = pd.Series(index=time_span, data=norm_constant_values)

    print(f"Running model for run {run['run_number']}")


    # Run the model
    run = model.run(progress=True,
                    params={'total radiative forcing': total_forcing, 
                            '"EXTRA: EXTRA: exponent"' : exponent,
                            '"EXTRA: EXTRA: normalisation constant"': norm_constant
                            },
                    return_columns=output_variables,
                    final_time=final_time, 
                    time_step=time_step)
    
    # Store the simulation results in a dataframe

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
        
    first_run = False

ds.to_netcdf(output_ds_path)
ds.close()




warnings.resetwarnings()

print('Done every run')

