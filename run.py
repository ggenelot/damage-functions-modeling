import pysd
import xarray as xr
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import http.client
import json
from datetime import datetime

# Prepare the API to store the results in the database

api_token = api_token

conn = http.client.HTTPSConnection("app.nocodb.com")

headers = {
    'xc-token': api_token,
    'Content-Type': 'application/json'
}




# Load model
model = pysd.read_vensim('WILIAM_v1.3/WILIAM.mdl',
                         split_views=True, 
                         subview_sep=["."])


# Choose FUND variables 
variables = model.doc
variables.to_csv('variables.csv')
variables_FUND = variables[variables['Real Name'].str.contains('FUND')]
variables_FUND_names = variables_FUND['Py Name'].values

initial_time = 2005
final_time = 2040
time_step = 0.25

# Suppress specific warnings to avoid cluttering the output
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# Run the model
run = model.run(progress=True, 
                return_columns=variables_FUND_names,
                final_time=final_time,  
                output_file=f'results/results_run_{final_time}.nc'
                )

warnings.resetwarnings()




# Store the run in the database

# JSON payload for the new record
new_record_data = {
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Example timestamp format
    "End_year": initial_time,
    "Name_of_the_run": f'run {initial_time} to {final_time}',
    "Start_year": final_time,
    "Stored_variables": "variable1, variable2",
    "Timestep": time_step,
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "created_by": "user_id",
    "updated_at": None,  # Replace with actual value if needed
    "updated_by": None  # Replace with actual value if needed
}

# Convert new_record_data to JSON format
json_data = json.dumps(new_record_data)

# API endpoint for adding records
endpoint = "/api/v2/tables/myi4g8i6dsl36by/records"

# Send POST request
conn.request("POST", endpoint, json_data, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))