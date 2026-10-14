import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def KNN_Classifier(Datapath):
    border = "--"*38

    print(border)
    print("Step 1 : Load the Dataset from CSV File")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Initial Entries from Dataset : ")
    print(df.head())
    print(border)


def main():
    KNN_Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()