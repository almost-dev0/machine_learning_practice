"""
the last remaining question from Practice set Q2

Q8. Write a single structured Python program that performs:
    1. Dataset loading
    2. Data analysis
    3. Visualization
    4. Train-test split
    5. Model training
    6. Prediction
    7. Accuracy calculation
    8. Confusion matrix generation
    9. Final conclusion
    Your code should include proper comments explaining each step.
"""

import pandas as pd

Border = "-" * 30

###########################################
# STEP 1 : LOAD THE DATASET
###########################################

print(Border)
print("Step 1 :Load the Dataset")
print(Border)

DataPath = "student_performance_ml.csv"

# df = data frame
df = pd.read_csv(DataPath)

print("")
print("Dataset Loaded Successfully!")
print("")

print("Initial Entries from Dataset are : ")
# prints first 5 records, by default value of df.head() is 5, df.head(n) gives first n records, similar is df.tail() for last records
print(df.head())        

print("")
print("")

###########################################
# STEP 2 : DATA ANALYSIS (EXPLORATORY DATA ANALYSIS)
###########################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)

print("Column Names : ",list(df.columns))

print("Missing Values per Column : ")
print(df.isnull().sum())    

print("Class distribution (Final Result) : ")
print(df["FinalResult"].value_counts())

print("Statistical Report of Dataset : ")
print(df.describe())

print("")
print("")