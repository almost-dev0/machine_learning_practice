import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def KNN_Classifier(Datapath):
    border = "--"*38

# Step 1 : Load the dataset from CSV file
    print(border)
    print("Step 1 : Load the Dataset from CSV File")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Initial Entries from Dataset : ")
    print(df.head())
    print(border)

# Step 2 : Clean the Dataset
    print(border)
    print("Step 2 : Clean the Dataset")
    print(border)

    df.dropna(inplace = True)               # inplace = True means values will be changed and changes will be saved to dataframe, like we modify the original df

    print("Shape of Dataset : ",df.shape)

    # since df.shape returns a tuple (no(rows), no(columns)), df.shape[0] is rows and df.shape[1] is columns by default
    print("Total Records : ",df.shape[0])   
    print("Total Columns : ",df.shape[1])
    print(border)

# Step 3 : Seperate Independent and Dependent Variables
    print(border)
    print("Step 3 : Seperate Independent and Dependent Variables")
    print(border)

    X = df.drop(columns = ['Class'])        # this means everything except 'Class' column is included in X
    Y = df['Class']

    print("Shape of X : ", X.shape)     # independent
    print("Shape of Y : ", Y.shape)     # dependent

    print(border)
    print("Input Columns : ", X.columns.tolist())       # .tolist() compiles the data into a list
    print("Output Column : Class")
    print(border)

# Step 4 : Split the Dataset for Training and Testing
    print(border)
    print("Step 4 : Split the Dataset for Training and Testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42, stratify = Y)
    # stratify = Y preserves class proportions in training and testing sets.
    # Example: If Y has 70% Class A and 30% Class B, both sets will maintain approximately the same 70:30 ratio.
    
    print(border)
    print("Details of Training and Testing Data")

    print("Shape of X_train :", X_train.shape)
    print("Shape of X_test  :", X_test.shape)

    print("Shape of Y_train :", Y_train.shape)
    print("Shape of Y_test  :", Y_test.shape)

    print(border)

# Step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature Scaling Successful!")

    print(border)

# Step 6 : Build the Model
    print(border)
    print("Step 6 : Build the Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors = 9)

    print("Model Build Successful")

# Step 7 : Train the Model
    print(border)
    print("Step 7 : Train the Model")
    print(border)

    model = model.fit(X_train_scaled,Y_train)

    print("Model Training Successful")
    print(border)

def main():
    KNN_Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()