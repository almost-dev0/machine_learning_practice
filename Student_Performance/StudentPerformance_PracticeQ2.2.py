"""
the last remaining question from Practice set Q2

Q8. Write a single structured Python program that performs:
    1. Dataset loading
    2. Data analysis
    3. Visualization
    4. Train-test split
    5. Model training
    6. Prediction
    7. Accuracy calculation
    8. Confusion matrix generation
    9. Final conclusion
    Your code should include proper comments explaining each step.
"""

import pandas as pd

# 1. Dataset Loading

df = pd.read_csv("student_performance_ml.csv")

print("")
print("DATASET LOADED SUCCESSFULLY!")
print("")