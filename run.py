import pysd
import xarray as xr
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pandas as pd

print('Executing run.py')

print('Loading model...')

# Load model
model = pysd.read_vensim('WILIAM_v1.3/WILIAM.mdl',
                         split_views=True, 
                         subview_sep=["."])

print('Model loaded')

# Choose FUND variables 
variables = model.doc
variables.to_csv('variables.csv')
variables_FUND = variables[variables['Real Name'].str.contains('FUND')]
variables_FUND_names = variables_FUND['Py Name'].values

initial_time = 2005
final_time = 2060

# Suppress specific warnings to avoid cluttering the output
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# Run the model
print('Running model...')
run = model.run(progress=True, 
                return_columns=variables_FUND_names,
                final_time=final_time,  
                output_file=f'results/results_run_{final_time}.nc'
                )

warnings.resetwarnings()

print('Model run')
