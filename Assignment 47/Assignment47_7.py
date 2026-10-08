"""7. Write a Python program using Linear Regression to train a regression model using the dataset below.
Study Hours Marks
1           50
2           55
3           60
4           65
5           70
Your program should:
    Train the regression model
    Print the coefficient
    Print the intercept

"""


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


