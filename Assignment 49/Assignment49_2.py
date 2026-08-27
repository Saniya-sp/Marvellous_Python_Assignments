"""WAP that calculates the variance and standard deviation of a dataset using NumPy for the following values
[6,7,8,9,10,11,12]
"""

import numpy as np

def CalculateMean():

    data = [6,7,8,9,10,11,12]
    mean = np.mean(data)

    print(mean)

    sum = 0
    for n in data:
        sum = sum + (n - mean)**2

    print("sum of squares: ",sum)

    # variance = sum of squares of (num - mean)/n-1
    variance = sum/len(data)

    print("Variance= ", variance)
    # standard deviation = square of variance
    print("standard deviation:", variance*variance)

def main():
    CalculateMean()
if __name__ == "__main__":
    main()