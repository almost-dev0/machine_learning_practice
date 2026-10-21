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
from sklearn.neighbors import KNeighborsClassifier

def main():
    df = {
        "A" : ((2,60), "Fail"),
        "B" : ((5,80), "Pass"),
        "C" : ((6,85), "Pass"),
        "D" : ((1,50), "Fail"),
    }

    X = [features for features,result in df]    
    Y = [result for features,result in df]
    # here, df has (study hours, attendence) as features and result and label,
    # so the for stores either feature or result out of that group in X and y

    
if __name__ == "__main__":
    main()