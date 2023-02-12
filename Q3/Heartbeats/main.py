#pandas program to read a csv file and convert it into a dataframe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the CSV file and creating a dataframe
dataframe = pd.read_csv('Q3/Heartbeats/ecg_csv.csv')
dataframe = dataframe.dropna()

# remove rows with null or non-numeric values in QTc column
dataframe = dataframe[pd.to_numeric(dataframe['QTc'], errors='coerce').notnull()]
dataframe = dataframe[pd.to_numeric(dataframe['RR'], errors='coerce').notnull()]

# convert QTc column to numeric data type
dataframe['QTc'] = pd.to_numeric(dataframe['QTc'], errors='coerce')
dataframe['RR'] = pd.to_numeric(dataframe['RR'], errors='coerce')

# remove rows with negative values in QTc column
dataframe = dataframe[dataframe['QTc'] >= 0]
print(dataframe)

# calculate number and percentage of unique patients with QTc > 500
num_patients_QTc_gt_500 = len(dataframe[dataframe['QTc'] > 500]['personid'].unique())
percent_QTc_gt_500 = (num_patients_QTc_gt_500 / len(dataframe['personid'].unique())) * 100

# calculate number and percentage of unique patients with QTc < 350
num_patients_QTc_lt_350 = len(dataframe[dataframe['QTc'] < 350]['personid'].unique())
percent_QTc_lt_350 = (num_patients_QTc_lt_350 / len(dataframe['personid'].unique())) * 100

# calculate number and percentage of unique patients with abnormal QTc values
num_patients_abnormal_QTc = len(dataframe[(dataframe['QTc'] >= 0.5*dataframe['RR']) & (dataframe['QTc'] <= 500)]['personid'].unique())
percent_abnormal_QTc = (num_patients_abnormal_QTc / len(dataframe['personid'].unique())) * 100

# print the results
print('Number of patients with QTc > 500: ', num_patients_QTc_gt_500, ' ({:.2f}%)'.format(percent_QTc_gt_500))
print('Number of patients with QTc < 350: ', num_patients_QTc_lt_350, ' ({:.2f}%)'.format(percent_QTc_lt_350))
print('Number of patients with abnormal QTc values: ', num_patients_abnormal_QTc, ' ({:.2f}%)'.format(percent_abnormal_QTc))

# calculate number and percentage of unique patients with normal QTc values
num_patients_normal_QTc = len(dataframe['personid'].unique()) - (num_patients_QTc_gt_500 + num_patients_QTc_lt_350 + num_patients_abnormal_QTc)
percent_normal_QTc = (num_patients_normal_QTc / len(dataframe['personid'].unique())) * 100

# select rows where QTc < 350 and group by personid
qtcs_lt_350 = dataframe[dataframe['QTc'] < 350].groupby('personid')

# loop over each person and print out their personid and lowest QTc value
for personid, group in qtcs_lt_350:
    qtcs = group['QTc']
    lowest_qtc = qtcs.min()
    print("Person ID: {}, Lowest QTc Value: {}".format(personid, lowest_qtc))

# create the pie chart
labels = ['QTc > 500', 'QTc < 350', 'Abnormal QTc', 'Normal QTc']
sizes = [percent_QTc_gt_500, percent_QTc_lt_350, percent_abnormal_QTc, percent_normal_QTc]
colors = ['yellowgreen', 'lightcoral', 'gold', 'lightskyblue']
explode = (0.1, 0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('Percentage of Patients with Abnormal ECG Readings')
plt.show()