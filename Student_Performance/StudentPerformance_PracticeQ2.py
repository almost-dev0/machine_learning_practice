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

"""
Q5. Calculate:
    • Training accuracy
    • Testing accuracy
    Compare both and comment whether the model is overfitting or underfitting.
"""

# calculating training accuracy

Y_train_pred = model.predict(X_train)

train_acc = accuracy_score(Y_train_pred, Y_train)

print("")
print("Training accuracy : "+ str(train_acc*100) + "%")


# calculating testing accuracy

Y_pred = model.predict(X_test)

test_acc = accuracy_score(Y_pred, Y_test)

print("Testing accuracy : "+ str(test_acc*100) + "%")

print("Training accuracy of 100% suggests that model has memorised the training data and won't perform well on new data")
print("Testing accuracy of 87.5% is realatively low than training accuracy")
print("This makes the model OVERFITTED")

"""
Q6. Train three Decision Tree models with:
    • max_depth = 1
    • max_depth = 3
    • max_depth = None
    Compare their testing accuracies and write your observations.
"""

# creating three Decision Tree Models

model1 = DecisionTreeClassifier(max_depth = 1, random_state = 42)
model2 = DecisionTreeClassifier(max_depth = 3, random_state = 42)
model3 = DecisionTreeClassifier(max_depth = None, random_state = 42)


# training the models

model1 = model1.fit(X_train, Y_train)
model2 = model2.fit(X_train, Y_train)
model3 = model3.fit(X_train, Y_train)


# testing the models

Y_pred1 = model1.predict(X_test)
Y_pred2 = model2.predict(X_test)
Y_pred3 = model3.predict(X_test)


# evaluating the models

print("")

acc1 = accuracy_score(Y_test, Y_pred1)
print("Accuracy of tree with max depth 1 : "+ str(acc1*100) + "%")
acc2 = accuracy_score(Y_test, Y_pred2)
print("Accuracy of tree with max depth 3 : "+ str(acc2*100) + "%")
acc3 = accuracy_score(Y_test, Y_pred3)
print("Accuracy of tree with max depth None : "+ str(acc3*100) + "%")

print("")
print("The accuracy score of all three DecisionTrees is same.")
print("However, when I did the same process on breast-cancer-wisconsin.csv dataset, accuracy increased as max depth increased.")
print("So, to conclude, it can be said that difference in accuracies (if any) can be observed with larger datasets as compared to this one.")