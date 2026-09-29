"""WAP to show how weights are updated in ANN
Tasks: 
    1. Take input, weight, bias, target output and learning rate
    2. Calculate prediction
    3. Calculate error
    4. Update weight using gradient descent logic
    5. Display old weight and updated weight
"""

# Input
x = 2

# Initial weight
weight = 0.5

# Bias
bias = 0.1

# Target output
target = 1

# Learning rate
learning_rate = 0.1


# Step 1: Calculate prediction
prediction = (x * weight) + bias

# Step 2: Calculate error
error = target - prediction

# Store old weight
old_weight = weight

# Step 3: Calculate gradient
gradient = error * x

# Step 4: Update weight
weight = weight + (learning_rate * gradient)


# Display results
print("Input:", x)
print("Target Output:", target)
print("Learning Rate:", learning_rate)

print("\nPrediction:", prediction)
print("Error:", error)

print("\nOld Weight:", old_weight)
print("Updated Weight:", weight)

