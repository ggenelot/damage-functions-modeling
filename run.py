import pysd
import xarray as xr
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import numpy as np

# Load model
model = pysd.read_vensim('WILIAM_v1.3/WILIAM.mdl',
                         split_views=True, 
                         subview_sep=["."])


# Saving the variables 
variables = model.doc

# Cleaning the variables and identifiying the model and equation 
variables['Real Name'] = variables['Real Name'].str.replace('"', '')
variables['Model'] = variables['Real Name'].str.split(':').str[0]
variables['Equation'] = variables['Real Name'].str.split(':').str[1]
variables.loc[variables['Equation'].isnull(), 'Model'] = np.nan


variables.to_csv('variables.csv')
variables_modelled = variables[variables['Model'].notna()]
variables_modelled_names = variables_modelled['Py Name'].values

initial_time = 2005
final_time = 2040

# Suppress specific warnings to avoid cluttering the output
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# Run the model
run = model.run(progress=True, 
                return_columns=variables_modelled_names,
                final_time=final_time,  
                output_file=f'results/results_run_{final_time}.nc'
                )

warnings.resetwarnings()
