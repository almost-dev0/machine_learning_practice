import pandas as pd

Border = "-" * 40

#######################################
# Step 1 : LOAD THE DATASET
#######################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

Datapath = "iris.csv"   # if the dataset would have been in any other location other than the same directory, we would have given its absolute path

df = pd.read_csv(Datapath)

print("Dataset Loaded Successfully")
print("")
print("Initial Entries are :")
print(df.head())

print("")
#######################################
# Step 2 : EXPLORATORY DATA ANALYSIS
#######################################

print(Border)
print("Step 2 : Exploratory Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing Values per Column")
print(df.isnull().sum())

print("Class Distribution (species count) :")
print(df["species"].value_counts())

print("Statistical report of Dataset : ")
print(df.describe())