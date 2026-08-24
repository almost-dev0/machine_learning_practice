import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

"""
Q1 : Import DecisionTreeClassifier from sklearn
     Create A Model object and train it using fit()
"""

df = pd.read_csv("student_performance_ml.csv")

print("")
print("DATASET LOADED SUCCESSFULLY!")
print("")
print("First Few records are : ")
print("")
print(df.head())

# Deciding Dependent and Independent Varibles

X = df.drop("FinalResult", axis = 1)            # axis = 1 specifies we have to remove the COLUMN (0 specifies row)
Y = df["FinalResult"]


# Splitting the Data into Training and Testing

X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size = 0.25, random_state = 42 )


# Creating the model of object of DecisionTreeClassifier

model = DecisionTreeClassifier()
print("")
print("MODEL BUILT SUCCESSFULLY!")


# Training the Model

model = model.fit(X_train, Y_train)
print("")
print("MODEL TRAINED SUCCESSFULLY!")
