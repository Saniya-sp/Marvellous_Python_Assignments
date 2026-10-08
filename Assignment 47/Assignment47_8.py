"""Using the regression model created in the previous question, write a Python program to predict marks 
for 6 study hours and display the predicted value."""


from sklearn.linear_model import LinearRegression
import numpy as np

# Input data
# Study Hours
X = np.array([[1], [2], [3], [4], [5]])

# Target data
# Marks
y = np.array([50, 55, 60, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Print coefficient and intercept
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

x_pred = np.array([[6]])

y_pred = model.predict(x_pred)

print("Prediction marks are :", y_pred[0])