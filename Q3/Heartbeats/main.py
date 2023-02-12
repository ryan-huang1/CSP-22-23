#pandas program to read a csv file and convert it into a dataframe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the CSV file and creating a dataframe
dataframe = pd.read_csv('Q3/Heartbeats/ecg_csv.csv')
dataframe = dataframe.dropna()

# remove rows with null or non-numeric values in QTc column
dataframe = dataframe[pd.to_numeric(dataframe['QTc'], errors='coerce').notnull()]

# convert QTc column to numeric data type
dataframe['QTc'] = pd.to_numeric(dataframe['QTc'], errors='coerce')

# remove rows with negative values in QTc column
dataframe = dataframe[dataframe['QTc'] >= 0]
print(dataframe)

# select rows with QTc > 500 and get number of unique patients
num_patients = len(dataframe[dataframe['QTc'] > 500]['personid'].unique())

# print the result
print('Number of unique patients with a QTc > 500: ', num_patients)

# select rows with QTc < 350 and get number of unique patients
num_patients = len(dataframe[dataframe['QTc'] < 350]['personid'].unique())

# print the result
print('Number of unique patients with a QTc < 350: ', num_patients)