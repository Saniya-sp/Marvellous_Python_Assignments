"""WAP to simulate a single artificial neuron
I/p:
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5
Task:
    -Calculate weighted sum
    -Apply sigmoid activation function
    -Display output
    -Explain whether output is close to 0 or 1
 """

import tensorflow as tf
import math

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

# Calculate weighted sum
weighted_sum = (x1 * w1) + (x2 * w2) + bias

# Sigmoid activation function
output = 1 / (1 + math.exp(-weighted_sum))

# Display results
print("Sigmoid Output is :",output) 

# Explain output
if output >= 0.5:
    print("Output is close to 1 (Neuron is activated)")
else:
    print("Output is close to 0 (Neuron is not activated)")
