"""The value of K plays important role in KNN algo.
WAP that demonstrates how prediction changes when K changes
Task:
    Predict the class of same new point with
        K=1
        K=3
        K=5 
O/P:
Red
Red
Blue
Explain why prediction changes when K changes 

Explaination: Value of K allows you to check the K nearest point from the input point. If K changes the number of points also changes.
    Based on these point you can predict the class of the input point.

Note: below code doesnt give expected op. 
Current op is Red, Red, Red"""

import math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#convert into OOP
#linux creator git repo

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) **2 +(P1['Y'] - P2['Y'] )** 2)
    return Ans
    
def MarvellousKNNClassifier():

    border = "-"*30
    Data = [
        {'point': 'A', 'X':1, 'Y':2, 'label':'Red'},
        {'point': 'B', 'X':2, 'Y':3, 'label':'Red'},
        {'point': 'C', 'X':3, 'Y':1, 'label':'Blue'},
        {'point': 'D', 'X':6, 'Y':5, 'label':'Blue'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    new_x = int(input("Enter X coordinate: "))
    new_y = int(input("Enter Y coordinate: "))

    new_point = {'X':new_x, 'Y':new_y}

    print("Distances of all points")
    print(border)
    X_points = []

    for X in Data:
        X_points.append([X['X'], X['Y']])

    Y_points = []
    for Y in Data:
        Y_points.append(Y['label'])

    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)     #d['distance']  - new key created

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(Data, key=lambda item: item['distance'])

    print(border)

    print("Sorted data:")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    for k in [1,3,5]:
        nearest = sorted_data[:k]

        print(border)
        print(f"Nearest {k} members are:")
        print(border)

        for d in nearest:
            print(d)

        print(border)

        #Voting
        votes = {}
        for neighbours in nearest:
            label = neighbours['label']
            votes[label] = votes.get(label, 0) + 1

        print(border)
        print("Voting Result is:")
        print(border)

        for d in votes:
            print("Name: ", d," | " "Number of votes:", votes[d])

        print(border)

        iMax = 0

        Name = ""

        for d in votes:
            if (votes[d]>iMax):
                iMax = votes[d]
                Name = d

        print("Final prediction is:", Name)
        print(border)

    # for k in [1, 3, 5]:

    #     model = KNeighborsClassifier(n_neighbors=k)

    #     model.fit(X_points, Y_points)

    #     prediction = model.predict([[2, 2]])

    #     print("K =", k, "Prediction =", prediction[0])

def main():
    
    MarvellousKNNClassifier()
    

if __name__ == "__main__":
    main()
