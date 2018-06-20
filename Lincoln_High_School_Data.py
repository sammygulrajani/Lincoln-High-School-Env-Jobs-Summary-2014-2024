# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 03:08:16 2018

@author: sammy
"""

df_pivot_gender['2015_Percent'] = ((df_pivot_gender['2015']) / (df_pivot_gender[df_pivot_gender['Gender'] == 'F']['2015'].sum())) * 100
df_pivot_gender['2015_Percent'] = ((df_pivot_gender['2015']) / (df_pivot_gender[df_pivot_gender['Gender'] == 'F']['2015'].sum())) * 100
df_pivot_gender['2015_Percent'] = ((df_pivot_gender['2015']) / (df_pivot_gender[df_pivot_gender['Gender'] == 'F']['2015'].sum())) * 100



  
df_pivot_gender['2015_Percent'] = ((df_pivot_gender['2015']) / (df_pivot_gender.loc[('F'), '2015'].sum())) * 100
df_pivot_gender['2016_Percent'] = ((df_pivot_gender['2016']) / (df_pivot_gender.loc[('F'), '2016'].sum())) * 100
df_pivot_gender['2017_Percent'] = ((df_pivot_gender['2017']) / (df_pivot_gender.loc[('F'), '2017'].sum())) * 100

df_pivot_gender = df_pivot_gender[['2015','2015_Percent','2016','2016_Percent','2017','2017_Percent']]