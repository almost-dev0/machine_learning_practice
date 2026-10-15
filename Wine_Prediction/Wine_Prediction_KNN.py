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

def main():
    KNN_Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()