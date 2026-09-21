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
        Data.loc[i, 'Distance'] = EucDistance(Data.iloc[i], new_point)
        # this here means, calculate the EucDistance between ith iteration point and new point,
        # and store the result of that ith iteration in 'Distance'
    
    print(Data)

    print(border)

    # this means sort the values of "distance" column 
    sorted_data = Data.sort_values('Distance')
    print(sorted_data)

    print(border)

def main():
    KNNReplica()

if __name__ == "__main__":
    main()