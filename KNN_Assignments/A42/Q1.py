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

def EuclideanDistance(x1,y1):
    pass

def main():
    x1 = int(input("Enter X Co-ordinate of Your Point : "))
    y1 = int(input("Enter Y Co-ordinate of Your Point : "))

if __name__ == "__main__":
    main()