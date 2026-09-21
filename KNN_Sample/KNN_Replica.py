import pandas as pd

def KNNReplica():
    border = "-" * 30

    Data = pd.read_csv("KNN_Replica_Dataset.csv")

    print(border)
    print("KNN Practice Replica")
    print(border)

    print(Data)
    print(border)

def main():
    KNNReplica()

if __name__ == "__main__":
    main()