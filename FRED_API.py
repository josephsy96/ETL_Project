"""
Author: Joseph Yi
Abstract:
Purpose of this script is to pull US Economic Data to present an interactive chart of economic data over a given time-series 
"""

#Import Dependencies 
import os
import pandas as pd 
#pip install fredapi
from fredapi import Fred
from pprint import pprint 


#Import API Key
from config import api_key

fred = Fred(api_key)
#This is to set the directory for the script
#Comment the line below out, I'm too lazy to manually type to change my directory
os.chdir('/Users/josephyi/Documents/VSCODE/FED API Data')

#create parameters for requests
#param = {'':''}

#Codes to pull: GDP, UNRATE
print('---' * 20 + '\nWelcome\n' + '---' * 20)
eco_code = input("Please input the economic code to pull:")


#Pull Monetary Data from the FRED API, specifically M1 Data 
try:
    eco = fred.get_series_all_releases(eco_code)
    print('---' * 20)
    pprint(eco)
    eco_df = pd.DataFrame(eco)
    eco_df.to_csv(f'{eco_code}.csv')
except:
    print("it's not working...")

print("Done pulling M1 Data")
