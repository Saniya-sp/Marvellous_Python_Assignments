"""Create a neural network model to predict whether a customer will leave a service
Features:
    1. AGe
    2. Monthly charges
    3. Tenure
    4. Number of complaints
    5. CUstomer support calls
     
X = [
[25,500,12,1,2],
[30,700,24,0,1],
[45,1200,6,5,8],
[50,1500,5,6,10],
[28,600,18,1,1],
[35,800,30,0,0],
[48,1400,4,7,9],
[52,1600,3,8,12],
[27,550,20,0,1],
[42,1300,8,4,7]
]

y=[
0,0,1,1,0
0,1,1,0,1
]

Output:
0 = Customer will stay
1 = Customer will leave

Tasks:
    1. Load or create dataset
    2. Clean the dataset
    3. Apply StandardScaler
    4. Train FNN model
    5. Evaluate accuracy
     
Feature Meaning
[Age, Monthly Charges, Tenure, Complaints, Support Calls]

Output Meaning
0 = Customer will stay
1 = Customer will leave

Test Input
new_customer = [[46, 1450, 5, 6, 9]]

Expected Output
Prediction: Customer may leave

"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# Output:
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([
    0, 0, 1, 1, 0,
    1, 1, 1, 0, 1
])


# --------------------------------------------------
# 2. Check and Clean Dataset
# --------------------------------------------------

print("Missing values in X:", np.isnan(X).sum())
print("Missing values in y:", np.isnan(y).sum())

# Check duplicate rows
print("Duplicate rows:", len(X) - len(np.unique(X, axis=0)))

# Check dataset shape
print("Dataset shape:", X.shape)


# --------------------------------------------------
# 3. Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 4. Apply StandardScaler
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --------------------------------------------------
# 5. Create Feedforward Neural Network
# --------------------------------------------------

model = Sequential([
    Dense(16, activation="relu", input_shape=(5,)),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])


# --------------------------------------------------
# 6. Compile Model
# --------------------------------------------------

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# --------------------------------------------------
# 7. Train Model
# --------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=0
)

# --------------------------------------------------
# 8. Evaluate Model
# --------------------------------------------------

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy)

# --------------------------------------------------
# 9. Predict New Customer
# --------------------------------------------------

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

# IMPORTANT:
# Use the same scaler that was fitted on training data.
new_customer_scaled = scaler.transform(new_customer)

prediction_probability = model.predict(
    new_customer_scaled,
    verbose=0
)[0][0]

print("\nPrediction Probability:", prediction_probability)

if prediction_probability >= 0.5:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")

