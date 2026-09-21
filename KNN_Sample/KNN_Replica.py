import pandas as pd
import math 

def EucDistance(P1, P2):
    Data = pd.read_csv("KNN_Replica_Dataset.csv")

    Ans = math.sqrt((P1['X'] - P2['X'])**2  +  (P1['Y'] - P2['Y'])**2)
    return Ans


def KNNReplica():
    border = "-" * 30

    Data = pd.read_csv("KNN_Replica_Dataset.csv")

    print(border)
    print("KNN Practice Replica")
    print(border)

    print(Data)
    print(border)

    new_point = {'X' : 3, 'Y' : 3}

    print("Distances of newpoint from all points : ")

    for i in range(len(Data)):
        Result = EucDistance(Data.iloc[i], new_point)
        print("Distance is : ",Result)

    print(border)

def main():
    KNNReplica()

if __name__ == "__main__":
    main()