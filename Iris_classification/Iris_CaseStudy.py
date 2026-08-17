import pandas as pd
import matplotlib.pyplot as plt

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

print("")
print("Column names : ",list(df.columns))

print("")
print("Missing Values per Column")
print(df.isnull().sum())

print("")
print("Class Distribution (species count) :")
print(df["species"].value_counts())

print("")
print("Statistical report of Dataset : ")
print(df.describe())


print("")
#######################################
# Step 3 : DECIDE INDEPENDENT AND DEPENDENT VARIABLES
#######################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X = Independent Variable / Features
# Y = Dependent Variable / Labels

feature_cols = [
    "sepal length (cm)", 
    "sepal width (cm)", 
    "petal length (cm)", 
    "petal width (cm)"
    ]

X = df[feature_cols]
print("")
Y = df["species"]

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)


print("")
#######################################
# Step 4 : VISUALISATION OF DATASET
#######################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize = (20,5))        #(width,length)

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], 
                temp["petal width (cm)"],label = sp)

plt.title("Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()