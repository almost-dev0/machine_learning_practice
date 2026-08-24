import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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


"""
Q2. Use the trained model to predict results for X_test.
    Display predicted values along with actual values.
"""

# Testing the Model

Y_pred = model.predict(X_test)
print("")
print("MODEL TESTED SUCCESSFULLY!")


# Display predicted values along with actual values

print("")
print ("Predicted : Actual")
# used .iloc[i] to traverse Y_test
# since y_test is a pandas series, we cannot traverse it normmally because indexes in a series are not serial (0,1,2,...) because the data
# selected for y_test is randomly selected. Hence, we need .iloc[i] so it accesses the data by its position rather than its actual index label.
for i in range(len(Y_test)):
    print(f"    {Y_pred[i]}     :     {Y_test.iloc[i]} ")



"""
Q3. Calculate model accuracy using accuracy_score.
    Display the result in percentage format.
"""

# Calculating model accuracy

accuracy = accuracy_score(Y_pred, Y_test)
print("")
print("Model Accuracy is : "+ str(accuracy*100) + "%")


"""
Q4. Generate confusion matrix using sklearn.
    Display it using ConfusionMatrixDisplay.
    Explain clearly:
        • True Positive
        • True Negative
        • False Positive
        • False Negative
"""
cm = confusion_matrix(Y_test, Y_pred)
print("")
print("Confusion Matrix is : ") 
print(cm)

cmplot = ConfusionMatrixDisplay(cm)
cmplot.plot()
display_labels = [0,1]
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("")
print("Plotting 0 = Negative and 1 = Postive, ")
print("True Positive  : 2 ")
print("True Negative  : 5 ")
print("False Positive : 0 ")
print("False Negative : 1 ")