import pysd
import warnings
import pandas as pd
import numpy as np

print('Executing run.py')

print('Loading model...')

# Suppress specific warnings to avoid cluttering the output
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# Load model
model = pysd.read_vensim('WILIAM_v1.3/WILIAM.mdl',
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

initial_time = 2005
final_time = 2030



# Run the model
print('Running model...')
run = model.run(progress=True, 
                return_columns=variables_modelled_names,
                final_time=final_time,  
                output_file=f'results/results_run_{final_time}.nc'
                )

warnings.resetwarnings()

print('Model run')
