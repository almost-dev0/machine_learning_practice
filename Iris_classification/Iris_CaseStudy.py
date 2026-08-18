import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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
plt.figure(figsize = (7,5))        #(width,length)

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], 
                temp["petal width (cm)"],label = sp)
'''
how the Iris species loop works:
- df[\"species\"] accesses the species column
- .unique() finds the different categories in the species column
- The unique result contains setosa, versicolor, and virginica
- for starts a loop
- sp is the loop variable
- The loop assigns one species to sp during each iteration
- First iteration: sp = setosa
- Second iteration: sp = versicolor
- Third iteration: sp = virginica
- df[\"species\"] == sp checks which rows match the current species
- == is the comparison operator and returns True or False
- df[...] uses the True/False results to filter matching rows
- temp stores the filtered rows for the current species
- plt.scatter() plots the filtered species
- label=sp gives each plotted species a name for the legend
- plt.legend() displays those species names"
'''

plt.title("Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

print("")
#######################################
# Step 5 : SPLIT THE DATASET FOR TRAINING AND TESTING
#######################################

print(Border)
print("Step 5 : Split the Dataset for Training and Testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42)

print("Dataset Splitting Successful !")

print("")
print("Shapes after splitting : ")
print("X : ", X.shape)
print("Y : ", Y.shape)

print("X_train : ", X_train.shape)
print("X_test : ", X_test.shape)

print("Y_train : ", Y_train.shape)
print("Y_test : ", Y_test.shape)

print("")
#######################################
# Step 6 : BUILD THE MODEL
#######################################

print(Border)
print("Step 6 : Build the Model")
print(Border)

model = DecisionTreeClassifier(max_depth = 5)

print("")
print("Model Created Successfully!")


print("")
#######################################
# Step 7 : TRAIN THE MODEL
#######################################
print(Border)
print("Step 7 : Train the Model")
print(Border)

model = model.fit(X_train,Y_train)

print("Model Trained Successfully!")


print("")
#######################################
# Step 8 : EVALUATE (TEST) THE MODEL
#######################################
print(Border)
print("Step 8 : Evaluate the Model")
print(Border)

Y_pred = model.predict(X_test)
print("Model Evaluated (Tested) Successfully !")

print("Expected Answers : ")
print(Y_test)
print("")

print("Predicted Answers : ")
print(Y_pred)
print("")
