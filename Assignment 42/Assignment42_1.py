"""WAP that classifies a new data point using a K-Nearest Neighbours algorithm. The algorithm should be implemented manually 
without using any machine learning library. 
The program should calculate Euclidean Distance
    Sort distances
    Select K nearest neighbour
    Predict the class based on majority voting
Dataset:

Point    X   Y      Label
A        1   2       Red
B        2   3       Red
C        3   1       Blue
D        6   5       Blue

Tasks: 
    1. Accept X and Y coordinates of a new point from the user
    2. Compute Euclidean distance from all dataset points
    3. Sort the distance
    4. Select K=3 nearest neighbour
    5.Predict the class label

I/P: Enter X coordinate: 2
     Enter Y coordinate: 2

O/P: Nearest Neighbours:
        A Distance 1.0
        B Distance 1.0
        C Distance 1.41
    Predicted class: Red

"""

import math
import numpy as np

#convert into OOP
#linux creator git repo

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) **2 +(P1['Y'] - P2['Y'] )** 2)
    return Ans
    
def MarvellousKNNClassifier(k = 3):

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


    nearest = sorted_data[:k]
    print(border)
    print("Nearest 3 members are:")
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
        print("Name: ", d, "Number of votes:", votes[d])

    print(border)

    iMax = 0

    Name = ""

    for d in votes:
        if (votes[d]>iMax):
            iMax = votes[d]
            Name = d

    print("Final prediction is:", Name)
    print(border)


def main():
    MarvellousKNNClassifier(5)
    

if __name__ == "__main__":
    main()
