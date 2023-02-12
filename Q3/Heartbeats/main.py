#pandas program to read a csv file and convert it into a dataframe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading the csv file
df = pd.read_csv('Q3/Heartbeats/ecg_csv.csv')

#converting the csv file into a dataframe
df = pd.DataFrame(df)

#print each column of the dataframe
print(df['personid'])