"""Consider below task
    1. Train linear regression model
    2. Predict salary for 6 years of experience
    3. Plot regression line using matplotlib

Dataset:
Experience  Salary
1           20000
2           25000
3           30000
4           35000
5           40000

Expected output:
Predicted salary for 6 years experience: Rs 45000

Graph should display
    Data point
    Regression line
"""


# import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression():

    Border = "-"*40

    #Step 1: Load the Data
    print(Border)
    print("Step 1: Load the Data")
    print(Border)
    
    Experience = [1,2,3,4,5]
    Salary = [20000,25000,30000,35000,40000]

    X = [[value] for value in Experience]
    Y = Salary
    print(X)
    print(Y)
 
    #Step 2: Split the dataset
    print(Border)
    print("Step 2: Split the dataset")
    print(Border) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Training data: ",X_train)
    print("Testing data: ",X_test)

    #Step 3: Train the model
    print(Border)
    print("Step 3: Train the model")
    print(Border) 


    model = LinearRegression()
    model = model.fit(X_train, Y_train)

    print("Model trained successfully..")

    #Step 4: Test the model
    print(Border)
    print("Step 4: Test the model")
    print(Border)    

    Y_pred = model.predict(X_test)

    print("Expected answers: ")
    print(Y_test[:3])

    print("Predicted answers")
    print(Y_pred[:3])

    new_experience = [[6]]
    new_experience_sal_pred = model.predict(new_experience)

    print("Salary for 6 years experience is: ", new_experience_sal_pred)

    # Predict salary for existing experience values
    Y_pred = model.predict(X)

    #Step 5: Plot the graph
    print(Border)
    print("Step 5: Plot the graph")
    print(Border)

    # Plot actual data points
    plt.scatter(X, Y, label="Data Points")

    # Plot regression line
    plt.plot(X, Y_pred, label="Regression Line")

    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary (Rs)")
    plt.title("Experience vs Salary")

    plt.legend()
    plt.grid()

    plt.show()


def main():
    MarvellousRegression()


if __name__ == "__main__":
    main()


