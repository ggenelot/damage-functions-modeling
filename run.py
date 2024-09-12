print('Executing run.py')

# This script : 
# 1 - loads the VENSIM model into a python model with PySD,
# 2 - launches a run to initialize the variables. Output variables are stored in a xarray dataset
# 3 - Runs the model as many times as required, stores the output variable in the dataset with index 'Run'
# 4 - Saves the dataset to a netCDF file that can be used for the later analysis

import pysd
import xarray as xr
import warnings
import pandas as pd
import numpy as np
import datetime
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



#variables["Interest"] = variables["Py Name"].apply(lambda x: vr.isInterest(x))
#interest_variables = variables[variables["Interest"] == True]["Py Name"].values
interest_variables = [
    "gini_gdppc_regions", 
    "gini_gdppc_eu27", 
    "temperature_change", 
    "temperature_change_in_35regions", 
    "total_population", 
    "population_35_regions", 
    "total_radiative_forcing", 
    "gross_domestic_product_nominal", 
    "average_disposable_income_per_capita", 
    "extra_extra_gdp_modifyer"
    ]

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
output_ds_path = 'results/final_test.nc'

initial_time = 2005
final_time = 2070
time_step = 1 
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
                final_time=final_time)


## Preparing the dataset 

ds = xr.open_dataset(output_ds_path)

run_num =  50 #len(runs)
ds = ds.expand_dims({"Run": run_num}).assign_coords({"Run": range(0, run_num)})
ds = ds.rename({'REGIONS 35 I': 'region'})


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
    run_result = model.run(progress=True,
                    params={'total radiative forcing': total_forcing, 
                            '"EXTRA: EXTRA: exponent"' : exponent,
                            '"EXTRA: EXTRA: normalisation constant"': norm_constant
                            },
                    return_columns=output_variables,
                    final_time=final_time)
    
    # Store the simulation results in a dataframe

    result_variables = run_result.columns 

    

    extra_extra_exponent_copy = ds["extra_extra_exponent"].copy()
    extra_extra_exponent_copy.loc[dict(Run = index)] = exponent
    ds["extra_extra_exponent"] = extra_extra_exponent_copy

    extra_extra_normalisation_constant_copy = ds["extra_extra_normalisation_constant"].copy()
    extra_extra_normalisation_constant_copy.loc[dict(Run = index)] = norm_constant
    ds["extra_extra_normalisation_constant"] = extra_extra_normalisation_constant_copy


    run_result = run_result.reset_index()
    
    for i in range(0, len(run_result.columns)):

        try: 
                column_name = run_result.columns.to_list()[i].strip()
                #print(column_name)
                variable_name = column_name.split('[')[0].strip()
                region = column_name.split('[')[1].split(']')[0].strip()
                #print(f'Variable : {variable_name}, region {region}')
                variable_copy = ds[variable_name].copy()
                #print('Before adding')
                #print(run[column_name].values)
                variable_copy.loc[dict(Run = index,  region=region)] = run_result[column_name].values
                #print('After copying')
                ds[variable_name] = variable_copy
                #print(f"Added variable {variable_name} in region {region} to the dataset.")
                
        except:      
                try: 
                        variable_name = run_result.columns.to_list()[i].strip()
                        variable_copy = ds[variable_name].copy()
                        variable_copy.loc[dict(Run = index)] = run_result[variable_name].values
                        ds[variable_name] = variable_copy
                        print(f"NO REGION - Added variable {variable_name} to the dataset.")
                except:
                        print(f'FAILED to add variable {run_result.columns.to_list()[i]}')

# Add a message to a text file

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"\n Executed run {index} at {current_datetime}"
file_path = "log.txt"

with open(file_path, "w") as file:
        file.write(message)

print("Message saved to", file_path)

ds.to_netcdf(output_ds_path)
ds.close()




warnings.resetwarnings()

print('Done every run')