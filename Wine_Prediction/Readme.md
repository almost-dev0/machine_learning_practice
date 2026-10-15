# Wine Classification using KNN

# Description
This case study uses the K-Nearest Neighbors (KNN) algorithm to classify wine samples based on their features.

# Features
- Loads the dataset from a CSV file.
- Cleans the dataset by removing missing values.
- Separates input features (`X`) and target variable (`Class`).
- Splits the data into training and testing sets.
- Applies feature scaling using `StandardScaler`.
- Tests different K values from 1 to 20.
- Calculates accuracy for each K value.
- Plots a graph of K values vs. accuracy.

# Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn

# How to Run
1. Install the required libraries: pip install pandas matplotlib scikit-learn
2. Place "WinePredictor.csv" in the project directory.
3. Run the Python script: python Wine_Prediction_KNN.py

# Output
- Accuracy scores for K values from 1 to 20.
- A graph showing the relationship between K values and classification accuracy.

# Purpose
To understand KNN classification, feature scaling, and how the choice of K affects model accuracy.