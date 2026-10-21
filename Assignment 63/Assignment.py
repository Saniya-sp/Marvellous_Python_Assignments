"""
Build a Loan Default Prediction System using multi-layer perceptron.
The system should accept employee information and predict:
0 -> Low default risk
1 -> High default risk
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier  
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score

#=======================================================================================
# 1. Load the dataset using Pandas
#=======================================================================================

print("1. Read the data from csv")

df = pd.read_csv("Loan_Default.csv")

# print("Complete dataset:")
# print(df)

#=======================================================================================
# 2. Exploratory Data analysis
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
print("Missing values :", df.isna().sum())
# print(df[df.isna()])
print(df.value_counts(dropna=False))

df = df.dropna(subset=["Default"]).copy()

print("lenght: ", len(df))

#=======================================================================================
# 4. Check whether the target classes are balanced
#=======================================================================================

#Target classes are balanced

# df["Default"] = df["Default"].map({
#                             "No": 0,
#                             "Yes": 1
#                         })

# print("\nEncoded dataset:")
# print(df.head())

# print("\nDefault class counts:")
# print(df["Default"].value_counts())


#=======================================================================================
# 5. Encode catagorical features such as OverTime into numerical representation.
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
df["PreviousDefault"] = df["PreviousDefault"].map({
            "No": 0,
            "Yes": 1
        })

df["HomeOwnership"] = df["HomeOwnership"].map({
            "Own": 0,
            "Rent": 1,
            "Mortgage": 2
        })


#=======================================================================================
# 6. Seperate independent and dependent variables
#=======================================================================================

X = df.drop("Default", axis=1)
y = df["Default"]

print("\nIndependent variables shape:", X.shape)
print("Dependent variable shape:", y.shape)

#=======================================================================================
# 7. Divide the dataset into training and testing data.
#=======================================================================================

X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y,
                                        test_size=0.20,
                                        random_state=42,
                                        stratify=y
                                    )

print("\nTraining records:", X_train.shape[0])
print("Testing records:", X_test.shape[0])

#=======================================================================================
# 8. Explaing whether stratified spliting should be used.
#=======================================================================================

# Stratified spliting is applied to maintain the balance in data spliting as the dependent feature has two classes

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
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    # learning_rate_init=0.001,
    max_iter=1000,
    # early_stopping=False,
    random_state=42
)

#=======================================================================================
# 11. Train the model.
#=======================================================================================

model.fit(X_train_scaled, y_train)

print("\nMLP model training completed.")


#=======================================================================================
# 12. Calculate training accuracy.
#=======================================================================================

y_train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(y_train, y_train_pred)

print(f"\nTraining Accuracy: {train_accuracy * 100:.2f}%")

y_test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")

#=======================================================================================
# 13. Generate a confusion matrix.
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

#=======================================================================================
# 14. Classification Report.
#=======================================================================================

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_test_pred,
        labels=[0, 1],
        target_names=["No Attrition", "Attrition"],
        zero_division=0
    )
)

#=======================================================================================
# 15. Calculate precision, recall, F1 score.
#=======================================================================================

precision = precision_score(y_test, y_test_pred, pos_label=1, zero_division=0)
recall = recall_score(y_test, y_test_pred, pos_label=1, zero_division=0)
f1 = f1_score(y_test, y_test_pred, pos_label=1, zero_division=0)

print('-'*40)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print('-'*40)

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

def PredictDefault(employee_data):
    """
    Loan Default Prediction.

    data can be a dictionary containing
    the some input features or a DataFrame with those features.
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
        "Age": 26, "Income": 30000,
        "LoanAmount": 100000, "CreditScore": 700,
        "EmploymentYears": 3, "ExistingLoans": 1,
        "MonthlyDebt": 10000, "LoanTerm": 10,
        "PreviousDefault": 0, "HomeOwnership": 0
    },
    {
        "Age": 35, "Income": 45000,
        "LoanAmount": 90000, "CreditScore": 755,
        "EmploymentYears": 35, "ExistingLoans": 2,
        "MonthlyDebt": 8000, "LoanTerm": 11,
        "PreviousDefault": 1, "HomeOwnership": 1
    },
    {
        "Age": 55, "Income": 5000,
        "LoanAmount": 58000, "CreditScore": 777,
        "EmploymentYears": 35, "ExistingLoans": 4,
        "MonthlyDebt": 5500, "LoanTerm": 11,
        "PreviousDefault": 1, "HomeOwnership": 1
    }
])

predictions = PredictDefault(new_employees)

print("\nPredictions for five new employees:")
print(predictions.to_string(index=False))


#=======================================================================================
# HYPERPARAMETER EXPERIMENT 
#=======================================================================================


# Store all experiment results
results = []

# Function to train and evaluate the model
def run_experiment(experiment_name, parameter_name,
                   parameter_value, **params):

    # Default configuration
    config = {
        "hidden_layer_sizes": (16, 8),
        "activation": "relu",
        "solver": "adam",
        "learning_rate_init": 0.001,
        "max_iter": 2000,
        "random_state": 42
    }

    # Change only the parameter being tested
    config.update(params)

    model = MLPClassifier(**config)

    # Train the model
    model.fit(X_train_scaled, y_train)

    # Make predictions
    train_pred = model.predict(X_train_scaled)
    test_pred = model.predict(X_test_scaled)

    # Calculate accuracy
    train_accuracy = accuracy_score(y_train, train_pred)
    test_accuracy = accuracy_score(y_test, test_pred)

    # Save results
    results.append({
        "Experiment": experiment_name,
        "Parameter": parameter_name,
        "Value": str(parameter_value),
        "Training Accuracy (%)": round(train_accuracy * 100, 2),
        "Testing Accuracy (%)": round(test_accuracy * 100, 2),
        "Iterations": model.n_iter_,
        "Final Loss": round(model.loss_, 4)
    })

    print(
        f"{experiment_name} | {parameter_name}={parameter_value} | "
        f"Train Accuracy={train_accuracy * 100:.2f}% | "
        f"Test Accuracy={test_accuracy * 100:.2f}% | "
        f"Iterations={model.n_iter_}"
    )


# --------------------------------------------------
# EXPERIMENT 1: Activation functions
# --------------------------------------------------

print("\nEXPERIMENT 1: ACTIVATION FUNCTIONS")

for activation in ["identity", "logistic", "tanh", "relu"]:
    run_experiment(
        "Activation",
        "activation",
        activation,
        activation=activation
    )


# --------------------------------------------------
# EXPERIMENT 2: Hidden-layer configurations
# --------------------------------------------------

print("\nEXPERIMENT 2: HIDDEN LAYERS")

for layers in [(10,), (20, 10), (50, 25), (100, 50, 25)]:
    run_experiment(
        "Hidden Layers",
        "hidden_layer_sizes",
        layers,
        hidden_layer_sizes=layers
    )


# --------------------------------------------------
# EXPERIMENT 3: Learning rates
# --------------------------------------------------

print("\nEXPERIMENT 3: LEARNING RATE")

for rate in [0.1, 0.01, 0.001, 0.0001]:
    run_experiment(
        "Learning Rate",
        "learning_rate_init",
        rate,
        learning_rate_init=rate
    )


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

results_df = pd.DataFrame(results)

print("\nCOMPLETE HYPERPARAMETER COMPARISON")
print(results_df.to_string(index=False))


# --------------------------------------------------
# PLOT TESTING ACCURACY
# --------------------------------------------------

for experiment in results_df["Experiment"].unique():

    subset = results_df[
        results_df["Experiment"] == experiment
    ]

    plt.figure(figsize=(9, 5))

    plt.bar(
        subset["Value"],
        subset["Testing Accuracy (%)"]
    )

    plt.title(f"Testing Accuracy - {experiment}")
    plt.xlabel("Hyperparameter Value")
    plt.ylabel("Testing Accuracy (%)")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


# --------------------------------------------------
# FIND THE BEST RESULT IN EACH EXPERIMENT
# --------------------------------------------------

print("\nBEST CONFIGURATION IN EACH EXPERIMENT")

for experiment in results_df["Experiment"].unique():

    subset = results_df[
        results_df["Experiment"] == experiment
    ]

    best_result = subset.loc[
        subset["Testing Accuracy (%)"].idxmax()
    ]

    print(
        f"{experiment}: Best value = {best_result['Value']}, "
        f"Testing Accuracy = {best_result['Testing Accuracy (%)']}%"
    )
