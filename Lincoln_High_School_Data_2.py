import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/sammy/Documents/Lincoln_HS_DataCSV.csv')

#df = df.pivot_table(index = ['Gender','Race', 'Status'], columns = 'Year', values = 'Count', aggfunc = 'sum')
#df = df.reset_index()

df_gender = df.pivot_table(index = 'Gender', columns = 'Year', values = 'Count', aggfunc = 'sum')
df_gender = df_gender.reset_index()

df_gender_status = df.pivot_table(index = ['Gender', 'Status'], columns = 'Year', values = 'Count', aggfunc = 'sum')
df_gender_status = df_gender_status.reset_index()

df_race = df.pivot_table(index = 'Race', columns = 'Year', values = 'Count', aggfunc = 'sum')
df_race = df_race.reset_index()

df_race_status = df.pivot_table(index = ['Race', 'Status'], columns = 'Year', values = 'Count', aggfunc = 'sum')
df_race_status = df_race_status.reset_index()

df_status = df.pivot_table(index = 'Status', columns = 'Year', values = 'Count', aggfunc = 'sum')
df_status = df_status.reset_index()

# list = [[df_gender, df_race, df_status], [2015,2016,2017], ['2015_percent', '2016_percent', '2017_percent']]

df_gender['2015_percent'] = df_gender[2015]/df_gender[2015].sum() * 100
df_gender['2016_percent'] = df_gender[2016]/df_gender[2016].sum() * 100
df_gender['2017_percent'] = df_gender[2017]/df_gender[2017].sum() * 100

df_gender = df_gender[['Gender', 2015, '2015_percent', 2016, '2016_percent', 2017, '2017_percent']]

df_race['2015_percent'] = df_race[2015]/df_race[2015].sum() * 100
df_race['2016_percent'] = df_race[2016]/df_race[2016].sum() * 100
df_race['2017_percent'] = df_race[2017]/df_race[2017].sum() * 100

df_race = df_race[['Race', 2015, '2015_percent', 2016, '2016_percent', 2017, '2017_percent']]

df_status['2015_percent'] = df_status[2015]/df_status[2015].sum() * 100
df_status['2016_percent'] = df_status[2016]/df_status[2016].sum() * 100
df_status['2017_percent'] = df_status[2017]/df_status[2017].sum() * 100

df_status = df_status[['Status', 2015, '2015_percent', 2016, '2016_percent', 2017, '2017_percent']]

def percent_gender_status_15(row):
    if row['Gender'] == 'F':
        return row[2015] / df_gender.loc[0,2015] * 100
    if row['Gender'] == 'M':
        return row[2015] / df_gender.loc[1,2015] * 100

df_gender_status['2015_percent'] = df_gender_status.apply(percent_gender_status_15, axis=1)

def percent_gender_status_16(row):
    if row['Gender'] == 'F':
        return row[2016] / df_gender.loc[0,2016] * 100
    if row['Gender'] == 'M':
        return row[2016] / df_gender.loc[1,2016] * 100

df_gender_status['2016_percent'] = df_gender_status.apply(percent_gender_status_16, axis=1)

def percent_gender_status_17(row):
    if row['Gender'] == 'F':
        return row[2017] / df_gender.loc[0,2017] * 100
    if row['Gender'] == 'M':
        return row[2017] / df_gender.loc[1,2017] * 100

df_gender_status['2017_percent'] = df_gender_status.apply(percent_gender_status_17, axis=1)

def percent_race_status_15(row):
    if row['Race'] == 'Black':
        return row[2015] / df_race.loc[1,2015] * 100
    if row['Race'] == 'White':
        return row[2015] / df_race.loc[5,2015] * 100
    if row['Race'] == 'Hispanic':
        return row[2015] / df_race.loc[2,2015] * 100
    if row['Race'] == 'Asian':
        return row[2015] / df_race.loc[0,2015] * 100
    if row['Race'] == 'Multi-Racial':
        return row[2015] / df_race.loc[3,2015] * 100
    if row['Race'] == 'Native American':
        return row[2015] / df_race.loc[4,2015] * 100

df_race_status['2015_percent'] = df_race_status.apply(percent_race_status_15, axis=1)

def percent_race_status_16(row):
    if row['Race'] == 'Black':
        return row[2016] / df_race.loc[1,2016] * 100
    if row['Race'] == 'White':
        return row[2016] / df_race.loc[5,2016] * 100
    if row['Race'] == 'Hispanic':
        return row[2016] / df_race.loc[2,2016] * 100
    if row['Race'] == 'Asian':
        return row[2016] / df_race.loc[0,2016] * 100
    if row['Race'] == 'Multi-Racial':
        return row[2016] / df_race.loc[3,2016] * 100
    if row['Race'] == 'Native American':
        return row[2016] / df_race.loc[4,2016] * 100

df_race_status['2016_percent'] = df_race_status.apply(percent_race_status_16, axis=1)

def percent_race_status_17(row):
    if row['Race'] == 'Black':
        return row[2017] / df_race.loc[1,2017] * 100
    if row['Race'] == 'White':
        return row[2017] / df_race.loc[5,2017] * 100
    if row['Race'] == 'Hispanic':
        return row[2017] / df_race.loc[2,2017] * 100
    if row['Race'] == 'Asian':
        return row[2017] / df_race.loc[0,2017] * 100
    if row['Race'] == 'Multi-Racial':
        return row[2017] / df_race.loc[3,2017] * 100
    if row['Race'] == 'Native American':
        return row[2017] / df_race.loc[4,2017] * 100

df_race_status['2017_percent'] = df_race_status.apply(percent_race_status_17, axis=1)

df_gender_status = df_gender_status[['Gender','Status', 2015, '2015_percent', 2016, '2016_percent', 2017, '2017_percent']]
df_race_status = df_race_status[['Race','Status', 2015, '2015_percent', 2016, '2016_percent', 2017, '2017_percent']]


# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('Lincoln_HS_Data_Stats.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet
df.to_excel(writer, sheet_name='Summary')
df_gender.to_excel(writer, sheet_name='By Gender')
df_race.to_excel(writer, sheet_name='By Race')
df_status.to_excel(writer, sheet_name='By Status')
df_gender_status.to_excel(writer, sheet_name='By Gender_Status')
df_race_status.to_excel(writer, sheet_name='By Race_Status')

# Close the Pandas Excel writer and output the Excel file
writer.save()