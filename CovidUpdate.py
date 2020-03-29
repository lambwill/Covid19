#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os


root_folder = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join(root_folder,'data')
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
daily_file_name = daily_file_prefix + '_' + str_timestamp + '.csv'
df_county_cases_daily.to_csv(os.path.join(data_folder, daily_file_name))

