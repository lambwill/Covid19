#!/usr/bin/env python
# coding: utf-8
import pandas as pd

filepath = '''C:/Users/lambw/OneDrive/Documents/COVID19/'''
datafolder = '''data/'''
timeseries_file_name = 'county_cases_timeseries.csv'
daily_file_prefix = 'county_cases_daily'
timestamp = pd.Timestamp.now()

# Load CountyUAs_cases_table data from https://www.arcgis.com/home/item.html?id=b684319181f94875a6879bbc833ca3a6
data_url = 'https://www.arcgis.com/sharing/rest/content/items/b684319181f94875a6879bbc833ca3a6/data'
df_county_cases_daily = pd.read_csv(data_url)

# Add a timestamp column to the data
df_county_cases_daily['time_stamp'] = str(timestamp)

# Make the timestamp into a string that can be used in the filename
date = str(timestamp.date())

hours = str(timestamp.hour)
if len(hours) == 1:
    hours = '0' + hours

minutes = str(timestamp.minute)
if len(minutes) == 1:
    minutes = '0' + minutes

seconds = str(timestamp.second)
if len(seconds) == 1:
    seconds = '0' + seconds

str_timestamp = date + '_' + hours + minutes + seconds

# Save the data
daily_file_name= daily_file_prefix + '_' + str_timestamp + '.csv'
df_county_cases_daily.to_csv(filepath + datafolder + daily_file_name)



# Load in the previous timeseries data from the existing csv
try:
	df_county_cases = pd.read_csv(filepath+timeseries_file_name,index_col=0)
except:
	df_county_cases = pd.DataFrame()

# Combine the downloaded data with the previous data
df_county_cases = pd.concat([df_county_cases,df_county_cases_daily])
df_county_cases.reindex()

# Save the combined data
df_county_cases.to_csv(filepath+timeseries_file_name)
