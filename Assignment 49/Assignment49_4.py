"""WAP to calculate Euclidean distance between two points before and after applying future scaling, and explain the 
difference in result

Answer
Observation: Dua to a large diffrence in values of two columns the one column becoms negligible infront of another column. The distance
calculated without scaling is large while after scaling it fall near the ranges of of columns values that got after scaling."""


import numpy as np
from sklearn.preprocessing import StandardScaler

def MarvellousCalculate():

    data = [[25,20000],
            [30,40000],
            [35,80000]]

    X = data[0]
    Y = data[1]

    X1, X2 = X[0], X[1]
    Y1, Y2 = Y[0], Y[1]
    # -----------------------------------------
    # Distance BEFORE scaling
    # -----------------------------------------

    print("\nDistance Before Scaling")

    distance_before = np.sqrt(
        ((X1 - Y1) ** 2 +
        (X2 - Y2) ** 2)
    )

    print("Point 1:", X)
    print("Point 2:", Y)

    print("Euclidean Distance:", distance_before)

    # -----------------------------------------
    # Apply Feature Scaling
    # -----------------------------------------

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    print("\nData After Scaling:")
    print(scaled_data)

    # Select scaled points
    scaled_point1 = scaled_data[0]
    scaled_point2 = scaled_data[1]

    # -----------------------------------------
    # Distance AFTER scaling
    # -----------------------------------------

    print("\nDistance After Scaling")

    distance_after = np.sqrt(
        (scaled_point1[0] - scaled_point2[0]) ** 2 +
        (scaled_point1[1] - scaled_point2[1]) ** 2
    )

    print("Scaled Point 1:", scaled_point1)
    print("Scaled Point 2:", scaled_point2)

    print("Euclidean Distance:", distance_after)

    # -----------------------------------------
    # Difference
    # -----------------------------------------

    print("\nDifference:")
    print(
        "Distance before scaling:",
        distance_before
    )

    print(
        "Distance after scaling:",
        distance_after
    )
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(data)

    print(X_scaled)


def main():
    MarvellousCalculate()
if __name__ == "__main__":
    main()