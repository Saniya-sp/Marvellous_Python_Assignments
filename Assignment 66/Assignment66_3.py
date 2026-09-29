"""WAP to calculate loss manually
Tasks:
    1. Implement mean squared error
    2. Implement binary cross entropy
    3. Take actual and predicted values
    4. Display the calculated loss
    5. Explain which loss function is used for regression and classififctaion"""

import math

# Actual values
actual = [1, 0, 1, 1, 0]

# Predicted values
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]


# Mean Squared Error
def mean_squared_error(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += (a - p) ** 2

    return total / len(actual)


# Binary Cross Entropy
def binary_cross_entropy(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += -(a * math.log(p) + (1 - a) * math.log(1 - p))

    return total / len(actual)


# Calculate losses
mse = mean_squared_error(actual, predicted)
bce = binary_cross_entropy(actual, predicted)


# Display results
print("Actual Values:   ", actual)
print("Predicted Values:", predicted)

print("\nMean Squared Error:", mse)
print("Binary Cross Entropy:", bce)


# Explaination: 
#     MSE is commonly used for regression problems, where the target is a continuous numerical value.

#         Examples:
    #         House price prediction
    #         Temperature prediction
    #         Salary prediction
    #         Sales prediction

#     BCE is commonly used for binary classification problems.
        # Examples:
        #     Spam / Not Spam
        #     Fraud / Not Fraud
        #     Disease / No Disease
        #     Pass / Fail