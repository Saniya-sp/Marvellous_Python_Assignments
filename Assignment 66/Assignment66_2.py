"""WAP to demonstrate different activation functions

Functions to implement:
    1. Sigmoid
    2. ReLU
    3. Tanh

Tasks:
 Accept input values from -10 to 10
 Plot all activation functions using matplotlib
 Explain the use of all activation function

"""
import numpy as np
import matplotlib.pyplot as plt


# Activation Functions

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


# Accept input values from -10 to 10
x = np.linspace(-10, 10, 100)


# Calculate activation values
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)


# Plot all activation functions
plt.figure(figsize=(10, 6))

plt.plot(x, sigmoid_output, label="Sigmoid")
plt.plot(x, relu_output, label="ReLU")
plt.plot(x, tanh_output, label="Tanh")

plt.title("Different Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True)
plt.legend()

plt.show()

