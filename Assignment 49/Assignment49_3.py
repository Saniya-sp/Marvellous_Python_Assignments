"""WAP using StandardScaler to perform feature scaling on the following dataset
[[25,20000],
[30,40000],
[35,80000]]
"""

import numpy as np
from sklearn.preprocessing import StandardScaler

def MarvellousCalculate():

    data = [[25,20000],
            [30,40000],
            [35,80000]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(data)

    print(X_scaled)


def main():
    MarvellousCalculate()
if __name__ == "__main__":
    main()