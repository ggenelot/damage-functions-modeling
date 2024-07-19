import pandas as pd

def all_variables(): 
    variables = pd.read_csv('variables.csv')
    return variables

def modeled_variables_list(): 
    variables = pd.read_csv('variables.csv')
    return variables[variables['Model'].notnull()]

def usefull_variables_list():
    interest_variables = [
    "gini_gdppc_regions", 
    "gini_gdppc_eu27", 
    "temperature_change", 
    "temperature_change_in_35regions", 
    "total_population", 
    "population_35_regions", 
    "total_radiative_forcing", 
    "gross_domestic_product_nominal"
    ]

    return interest_variables

def rcp_variables():
    variables = pd.read_csv('variables.csv')
    variables = variables[variables['Subscripts'].fillna('').str.contains('RCP')]
    variables = variables['Py Name'].values

    return variables

def variables_FUND():
    variables = pd.read_csv('variables.csv')
    variables = variables[variables['Model'] == 'FUND']
    variables = variables['Py Name'].values
    return variables

def variables_DICE():
    variables = pd.read_csv('variables.csv')
    variables = variables[variables['Model'] == 'DICE']
    variables = variables['Py Name'].values
    return variables

def isInterest(variable):


    return variable in interest_variables