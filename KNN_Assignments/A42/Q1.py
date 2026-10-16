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
        "A" : (1,2),
        "B" : (2,3),
        "C" : (3,1),
        "D" : (6,5),
        }

    distances_list = []

    for name, (x2,y2) in points.items():
        distance = math.sqrt( ((x2 - x1)**2) + ((y2 - y1)**2) )
        distances_list.append(distance)    

    return distances_list

# RAW LOGIC
    # Ax2 = 1 c
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

def main():
    x1 = int(input("Enter X Co-ordinate of Your Point : "))
    y1 = int(input("Enter Y Co-ordinate of Your Point : "))


if __name__ == "__main__":
    main()