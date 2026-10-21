"""
3. Use KNN to predict whether a student passes or fails based on study hours and          attendance.
Dataset
-------------------------------------
| Study Hours | Attendance | Result |
-------------------------------------
|      2      |     60     |  Fail  |
-------------------------------------
|      5      |     80     |  Pass  |
-------------------------------------
|      6      |     85     |  Pass  |
-------------------------------------
|      1      |     50     |  Fail  |
-------------------------------------
Tasks
1. Accept input from user:
◦ Study hours
◦ Attendance percentage
2. Apply KNN algorithm
3. Predict whether the student Passes or Fails
Input Example
Enter Study Hours: 4
Enter Attendance: 70
Expected Output
Predicted Result: Pass
"""

import math

def EuclideanDistance(x1,y1):

    distances = {
        "A" : ((2,60), "Fail"),
        "B" : ((5,80), "Pass"),
        "C" : ((6,85), "Pass"),
        "D" : ((1,50), "Fail"),
    }



    distances_list = []

    for name, ((x2,y2),label) in distances.items():
        distance = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )
        distances_list.append((name,distance,label))    

    return distances_list

def Voting(distances_list):

    result_prediction = []
    prediction = None

    for name, distance, label in distances_list[:3]:
        result_prediction.append(label)

    if result_prediction.count("Pass") > result_prediction.count("Fail"):
        prediction = "Pass"
    else:
        prediction = "Fail"
    
    return prediction

def main():
    x1 = int(input("Enter Study Hours : "))
    y1 = int(input("Enter Attendence  : "))
    print()

    distances = EuclideanDistance(x1,y1)
    distances.sort(key = lambda item : item[1])         
    #since our distances has three items, item[0] is point name, item[1] is distance and item[2] is label(color), 
    #we have sorted it wrt item[1], i.e., distance
    

    print("")

    prediction = Voting(distances)
    print("Predicted Class : ",prediction)

if __name__ == "__main__":
    main()