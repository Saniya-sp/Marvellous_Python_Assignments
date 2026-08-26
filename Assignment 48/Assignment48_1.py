"""Implement Simple Linear Regression without using ML library.
Dataset:
X = [1,2,3,4,5]
Y = [3,4,2,4,5]
Tasks:
    calculate:
        Mean of X(X bar)
        Mean of Y(Y bar)
        Slope m
        Intercept c
Expected op:
    mean of x = 3
    mean of y = 3.6
    slope (m) = 0.4
    intercept = 2.4
    
    Regression equation:
    Y = 0.4X + 2.4
    Predicted Y for X = 6: """


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def MarvellousPredictor():
    border = "-"*40
    ###############################################
    # Step 1: Load the data
    ###############################################
    print(border)
    print("Step 1: Load the data")
    print(border)

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variables X: ",X)
    print("Values of dependent variables Y: ",Y)

    ###############################################
    # Step 2 : Calculate mean: (X bar) and (Y bar)
    ###############################################

    print(border)
    print("Step 2 : Calculate mean: (X bar) and (Y bar)")
    print(border)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    Xbar = sum_x / len(X)       #mean of X
    Ybar = sum_y / len(Y)       #mean of Y

    print("mean_x is:", Xbar)
    print("mean_y is:", Ybar)

    ###############################################
    # Step 3 : Calculate slope (m)
    ###############################################

    print(border)
    print("Step 3 : Calculate slope (m)")
    print(border)

    n = len(X)  #5

    numerator = 0
    denomenator = 0

    #formula:  m = Sum(X-Xbar)(Y-Ybar)/ Sum(X-Xbar)**2
    # Calculate slope (m)
    for i in range(n):
        numerator = numerator + ((X[i] - Xbar) * (Y[i] - Ybar))
        denomenator = denomenator + ((X[i] - Xbar)**2)

    m = numerator/denomenator

    print("Slope of line m: ",m)

    ###############################################
    # Step 4 : Calculate intercept (c: (Y intercept))
    ###############################################

    print(border)
    print("Step 4 : Calculate intercept (c: (Y intercept))")
    print(border)

    #y=mx+c 
    #c=ymean - m * xmean

    c = Ybar - m * Xbar

    print("Value of c is: ",c)

    print(border)

    ###############################################
    # Step 5 : Predict Y for X = 6
    ###############################################

    print(border)
    print("Step 5 : Predict Y for X = 6")
    print(border)

    y= m * 6 + c 

    print("value of Y for X=6 is :", y)
    print(border)


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()
