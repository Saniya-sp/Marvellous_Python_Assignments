"""Use the KNN to predict whether the student passes or fails based on studyHours and attendance.
Dataset:

Study Hours  Attendence     Result
2               60          Fail
5               80          Pass
6               85          Pass
1               50          Fail

Task:
    Accept ip from user
        -Study hours
        -Attendence percentage
    Apply KNN
    Predict whether the student passes or fails

ip: 4
    70
op: pass
"""

import math
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#convert into OOP
#linux creator git repo

def MarvellousKNNClassifier():

    border = "-"*30
    Data = [
        {'Study Hours': 2, 'Attendence':60, 'Result':'Fail'},
        {'Study Hours': 5, 'Attendence':80, 'Result':'Pass'},
        {'Study Hours': 6, 'Attendence':85, 'Result':'Pass'},
        {'Study Hours': 1, 'Attendence':50, 'Result':'Fail'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    # Training data
    X = [
        [2, 60],
        [5, 80],
        [6, 85],
        [1, 50]
    ]

    # Results
    Y = [
        "Fail",
        "Pass",
        "Pass",
        "Fail"
    ]

    study_hours = int(input("Enter study hours: "))
    attendance = int(input("Enter attendence: "))

    student = [[study_hours, attendance]]

    print("Distances of all points")
    print(border)
    X_points = []


    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    prediction = model.predict(student)

    print("Prediction =", prediction[0])


def main():
    
    MarvellousKNNClassifier()
    

if __name__ == "__main__":
    main()
