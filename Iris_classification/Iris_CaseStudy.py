import pandas as pd

Border = "-" * 40

#######################################
# Step 1 : LOAD THE DATASET
#######################################

print("Border")
print("Step 1 : Load the Dataset")
print("Border")

Datapath = "iris.csv"   # if the dataset would have been in any other location other than the same directory, we would have given its absolute path

df = pd.read_csv(Datapath)

print("Dataset Loaded Successfully")
print("Initial Entries are :")
print(df.head())