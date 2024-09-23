#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:12:03 2024

@author: njoku
"""

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read dataset in 
df = pd.read_excel('data/mof_data_set_original.xlsx')

# inspect first five enteries
df.head(5)

# inspect last five entries
df.tail(5)


# Rename the features to minimize typing
columns = df.columns
new_columns = ['sbet', 'sl', 'vt', 'p', 't','metal_center', 'update']
df = df.rename(columns = {'SBET(m2/g)':"sbet", 'SL(m2/g)':'sl', 'VT(cm3/g)':'vt', 'P(kPa)':'p', 'T(K)':'t','Mental center':'metal_center', 'Uptake':'update'})


# dataframe information
print(df.info())

# describe the dataset 
print(df.describe())

# checking null values
print(df.isnull().any())

# functions
def missing_values_table(df):
    # total missing values
    mis_val = df.isnull().sum()

    # percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(columns = {0:'Missing values', 1:'% of total values' })

    # sort the table by percentage of missing descending
#    mis_val_table_ren_columns = [mis_val_table_ren_columns.iloc[:,1] != 0].sort_value('% of total values', ascending=False).round(1)

    # print some summary information 
    print('Your selected dataframe has ' + str(df.shape[1]) + 'columns \n There are ' + str(mis_val_table_ren_columns.shape[0]) + "columns have missing values.")

    # return the dataframe with missing information 
    return mis_val_table_ren_columns 

print(missing_values_table(df))

# investigage sbet
# from the describe above, it is evident that there could be an 
# outlier in df['sbet'] given max value 5290 and 75% being 1859
# missing values will be filled with the mode that is not affected by outlier
df['sbet'] = df['sbet'].fillna(value = df['sbet'].mode()[0])
df['vt'] = df['vt'].fillna(value = df['vt'].mode()[0])
df['sl'] = df['sl'].fillna(value = df['sl'].mode()[0])

# confirm missing values filled
print(missing_values_table(df))

# Exploratory Data Analysis
## Mononvariate analysis

df.isnull().any()