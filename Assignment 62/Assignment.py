"""
Build a DL-based Employee Attrition Prediction System using MLPClassifier.
The system should accept employee information and predict:
0 -> Employee is likely to stay
1 -> Employee is likely to leave
"""


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier  
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#=======================================================================================
# 1. Load the dataset using Pandas
#=======================================================================================

print("1. Read the data from csv")

df = pd.read_csv("Employee_Attrition.csv")

# print("Complete dataset:")
# print(df)

#=======================================================================================
# 2. Display the Shape, columns and first five recordsData analysis
#=======================================================================================
print("2. Data analysis")

print("Shape of dataset:")
print(df.shape)

print("Column names:")
print(df.columns)

print("First five rows")
print(df.head())

# print("Statistical summary:")
# print(Data.describe())
#=======================================================================================
# 3. Check for missing values
#=======================================================================================

print("Missing values are:")
print(df.isnull().sum())

#=======================================================================================
# 4. Identify Numerical and categorical features
#=======================================================================================

print("4. Preprocessing")

numerical_features = df.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("\nNumerical columns:", numerical_features)
print("Categorical columns:", categorical_features)

# X = df[["Age","MonthlyIncome","YearsAtCompany","TotalWorkingYears","DistanceFromHome","JobSatisfaction","WorkLifeBalance","OverTime","NumCompaniesWorked","TrainingTimesLastYear"]]
# Y = df['Attrition']

# print("Input features:")
# print(X.head())

# print("Tartget:")
# print(Y.head())

#=======================================================================================
# 5. Convert catagorical features such as OverTime into numerical representation.
#=======================================================================================
df["OverTime"] = df["OverTime"].map({
            "No": 0,
            "Yes": 1
        })


#=======================================================================================
# 6. Convert the target Attrition into 0 and 1
#=======================================================================================
df["Attrition"] = df["Attrition"].map({
                            "No": 0,
                            "Yes": 1
                        })

print("\nEncoded dataset:")
print(df.head())

print("\nAttrition class counts:")
print(df["Attrition"].value_counts())

#=======================================================================================
# 7. Seperate independent and dependent variables
#=======================================================================================

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

print("\nIndependent variables shape:", X.shape)
print("Dependent variable shape:", y.shape)

#=======================================================================================
# 8. Divide the dataset into training and testing data.
#=======================================================================================

X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y,
                                        test_size=0.20,
                                        random_state=42,
                                        # stratify=y
                                    )

print("\nTraining records:", X_train.shape[0])
print("Testing records:", X_test.shape[0])

#=======================================================================================
# 9. Apply appropriate feature scaling.
#=======================================================================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")

#=======================================================================================
# 10. Design an MLP with at least two hidden layers.
#=======================================================================================

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=2000,
    early_stopping=False,
    random_state=42
)

#=======================================================================================
# 11. Train the network.
#=======================================================================================

model.fit(X_train_scaled, y_train)

print("\nMLP model training completed.")

#=======================================================================================
# 12. Display the number of iterations required for training.
#=======================================================================================

print("Iterations required:", model.n_iter_)
print("Maximum iterations allowed:", model.max_iter)

#=======================================================================================
# 13. Calculate training accuracy.
#=======================================================================================

y_train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(y_train, y_train_pred)

print(f"\nTraining Accuracy: {train_accuracy * 100:.2f}%")

#=======================================================================================
# 14. Calculate testing accuracy.
#=======================================================================================

y_test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

#=======================================================================================
# 15. Generate a confusion matrix.
#=======================================================================================

cm = confusion_matrix(
    y_test,
    y_test_pred,
    labels=[0, 1]
)

print("\nConfusion Matrix:")
print(cm)

# display = ConfusionMatrixDisplay(
#     confusion_matrix=cm,
#     display_labels=["No Attrition", "Attrition"]
# )

# display.plot()
# plt.title("Employee Attrition - Confusion Matrix")
# plt.tight_layout()
# plt.show()

# print("\nClassification Report:")
# print(
#     classification_report(
#         y_test,
#         y_test_pred,
#         labels=[0, 1],
#         target_names=["No Attrition", "Attrition"],
#         zero_division=0
#     )
# )

#=======================================================================================
# 16. Plot the loss curve.
#=======================================================================================

plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_)
plt.title("MLP Training Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.grid(True)
plt.tight_layout()
plt.show()

#=======================================================================================
# 17. Create a function: PredictAttrition(employee_data)
#=======================================================================================

def PredictAttrition(employee_data):
    """
    Predict whether an employee is likely to leave.

    employee_data can be a dictionary containing
    the 10 input features or a DataFrame with those features.
    """

    if isinstance(employee_data, dict):
        employee_df = pd.DataFrame([employee_data])
    elif isinstance(employee_data, pd.DataFrame):
        employee_df = employee_data.copy()
    else:
        raise TypeError(
            "Input must be a dictionary or a Pandas DataFrame."
        )

    required_columns = X.columns.tolist()

    missing_columns = [
        col for col in required_columns
        if col not in employee_df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required features: {missing_columns}"
        )

    # Keep the same feature order as the training data.
    employee_df = employee_df[required_columns].copy()

    # Support either Yes/No or 1/0 for OverTime.
    employee_df["OverTime"] = employee_df["OverTime"].replace({
        "No": 0,
        "Yes": 1
    })

    # Check that all inputs are numeric and valid.
    employee_df = employee_df.apply(
        pd.to_numeric, errors="raise"
    )

    if employee_df.isnull().any().any():
        raise ValueError("Input contains missing values.")

    # Apply the scaler fitted on training data.
    employee_scaled = scaler.transform(employee_df)

    predictions = model.predict(employee_scaled)
    probabilities = model.predict_proba(employee_scaled)

    results = []

    for i, prediction in enumerate(predictions):
        results.append({
            "Predicted_Attrition": int(prediction),
            "Prediction": (
                "Yes - Likely to Leave"
                if prediction == 1
                else "No - Likely to Stay"
            ),
            "Attrition_Probability": round(
                float(probabilities[i, 1]), 4
            )
        })

    return pd.DataFrame(results)


#=======================================================================================
# 18. Test the system using at least five new employee records.
#=======================================================================================

new_employees = pd.DataFrame([
    {
        "Age": 26, "MonthlyIncome": 30000,
        "YearsAtCompany": 1, "TotalWorkingYears": 3,
        "DistanceFromHome": 35, "JobSatisfaction": 1,
        "WorkLifeBalance": 1, "OverTime": "Yes",
        "NumCompaniesWorked": 4, "TrainingTimesLastYear": 0
    },
    {
        "Age": 45, "MonthlyIncome": 120000,
        "YearsAtCompany": 12, "TotalWorkingYears": 20,
        "DistanceFromHome": 5, "JobSatisfaction": 4,
        "WorkLifeBalance": 4, "OverTime": "No",
        "NumCompaniesWorked": 2, "TrainingTimesLastYear": 4
    },
    {
        "Age": 32, "MonthlyIncome": 45000,
        "YearsAtCompany": 2, "TotalWorkingYears": 7,
        "DistanceFromHome": 25, "JobSatisfaction": 2,
        "WorkLifeBalance": 2, "OverTime": "Yes",
        "NumCompaniesWorked": 5, "TrainingTimesLastYear": 1
    },
    {
        "Age": 50, "MonthlyIncome": 150000,
        "YearsAtCompany": 15, "TotalWorkingYears": 28,
        "DistanceFromHome": 8, "JobSatisfaction": 4,
        "WorkLifeBalance": 3, "OverTime": "No",
        "NumCompaniesWorked": 3, "TrainingTimesLastYear": 3
    },
    {
        "Age": 29, "MonthlyIncome": 55000,
        "YearsAtCompany": 3, "TotalWorkingYears": 6,
        "DistanceFromHome": 40, "JobSatisfaction": 1,
        "WorkLifeBalance": 2, "OverTime": "Yes",
        "NumCompaniesWorked": 6, "TrainingTimesLastYear": 0
    }
])

predictions = PredictAttrition(new_employees)

print("\nPredictions for five new employees:")
print(predictions.to_string(index=False))


#=======================================================================================
# 19. Explain whether the model is suffering from overfitting or underfitting.
#=======================================================================================

accuracy_gap = train_accuracy - test_accuracy

print("\nModel Fit Analysis:")
print(f"Training accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing accuracy:  {test_accuracy * 100:.2f}%")
print(f"Accuracy gap:      {accuracy_gap * 100:.2f} percentage points")

if train_accuracy >= 0.90 and accuracy_gap > 0.15:
    print("Possible overfitting: training accuracy is high, "
          "but testing accuracy is much lower.")
elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Possible underfitting: performance is low on "
          "both training and testing data.")
elif abs(accuracy_gap) <= 0.10:
    print("Training and testing accuracy are relatively close. "
          "Check the absolute scores and other metrics before "
          "concluding that the model generalizes well.")
else:
    print("The fit is inconclusive. Inspect the confusion matrix, "
          "class-wise metrics, and results on more data.")

