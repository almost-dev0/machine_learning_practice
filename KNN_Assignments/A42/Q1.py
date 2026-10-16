"""
1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
The algorithm should be implemented manually without using any machine learning library.
The program should:
• Calculate Euclidean distance
• Sort distances
• Select K nearest neighbors
• Predict the class based on majority voting
Dataset
-------------------------
| Point | X | Y | Label |
-------------------------
|   A   | 1 | 2 |  Red  |
-------------------------
|   B   | 2 | 3 |  Red  |
-------------------------
|   C   | 3 | 1 |  Blue |
-------------------------
|   D   | 6 | 5 |  Blue |
-------------------------
Tasks
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.
Input Format
Enter X coordinate: 2
Enter Y coordinate: 2
Expected Output
Nearest Neighbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41
Predicted Class: Red
"""
import math

def EuclideanDistance(x1,y1):

    points = {                      # dictionary
        "A" : ((1,2), "Red"),
        "B" : ((2,3), "Red"),
        "C" : ((3,1), "Blue"),
        "D" : ((6,5), "Blue")
        }

    distances_list = []

    for name, ((x2,y2),label) in points.items():
        distance = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )
        distances_list.append((name,distance,label))    

    return distances_list

# RAW LOGIC
    # Ax2 = 1 
    # Ay2 = 2
    # Bx2 = 2 
    # By2 = 3
    # Cx2 = 3 
    # Cy2 = 1
    # Dx2 = 6 
    # Dy2 = 5
    
    # dwA = math.sqrt( ((Ax2 - x1)**2) + ((Ay2 - y1)**2) )
    # dwB = math.sqrt( ((Bx2 - x1)**2) + ((By2 - y1)**2) )
    # dwC = math.sqrt( ((Cx2 - x1)**2) + ((Cy2 - y1)**2) )
    # dwD = math.sqrt( ((Dx2 - x1)**2) + ((Dy2 - y1)**2) )

    #return dwA, dwB, dwC, dwD

def Voting(distances_list):

    color_prediction = []
    prediction = None

    for name, distance, label in distances_list[:3]:
        color_prediction.append(label)

    if color_prediction.count("Red") > color_prediction.count("Blue"):
        prediction = "Red"
    else:
        prediction = "Blue"
    
    return prediction

def main():
    x1 = int(input("Enter X Co-ordinate of Your Point : "))
    y1 = int(input("Enter Y Co-ordinate of Your Point : "))
    print()

    distances = EuclideanDistance(x1,y1)
    distances.sort(key = lambda item : item[1])         
    #since our distances has three items, item[0] is point name, item[1] is distance and item[2] is label(color), 
    #we have sorted it wrt item[1], i.e., distance
    
    print("Nearest Neighbors : ")
    print(distances[0])
    print(distances[1])
    print(distances[2])

    print("")

    prediction = Voting(distances)
    print("Considering K = 3, Predicted Class : ",prediction)

if __name__ == "__main__":
    main()