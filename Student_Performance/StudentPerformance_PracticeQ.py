import numpy as np
import pandas as pd


# Importing and loading the Dataset
Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)
print("")
print("Dataset Loaded Successfully!")
print("")

"""
Q1 : Load the dataset and display : 
a. First 5 records
b. Last 5 records
c. Total Number of rows and columns
d. List of Column names
e. Data types of each column
"""

# a. First 5 records
print("The first 5 records are : ")
print(df.head())
print("")

# b. Last 5 records
print("The last 5 records are : ")
print(df.tail())
print("")

# c. Total number of rows and columns
print("Total number of rows and colums are : ")
print(df.shape)
print("")

# d. List of column names
col_names = list(df.columns)
print("List of Column Names : ")
print(col_names)
print("")

# e. Data types of each column
print("Data types of each column : ")
print(df.dtypes)



"""
Q2 : Write a program for  : 
a. Total number of students in dataset
b. Count how many students passed (FinalResult = 1)
c. Count how many students failed (FinalResult = 0)
"""

# a. Total number of students in dataset
print("")
print("Total Number of Students in Dataset : ")
print(df["Attendance"].count())
print("")

# b. Count how many students passed (FinalResult = 1)
countpass = 0
for result in df["FinalResult"]:
    if result == 1:
        countpass += 1

print("Total Number of Students Passed : ",countpass)
print("")

# c. Count how many students failed (FinalResult = 0)
countfail = 0
for result in df["FinalResult"]:
    if result == 0:
        countfail += 1

print("Total Number of Students Passed : ",countfail)
print("")