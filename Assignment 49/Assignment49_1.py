"""WAP that calculates the mean of a dataset using NumPy for the following values
[6,7,8,9,10,11,12]
"""

import numpy as np

def CalculateMean():

    data = [6,7,8,9,10,11,12]
    mean = np.mean(data)
    print(mean)


def main():
    CalculateMean()
if __name__ == "__main__":
    main()