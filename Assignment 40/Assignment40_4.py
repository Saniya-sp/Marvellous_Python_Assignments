"""Create a new Dataframe with details of 5 students. Use the trained model to predict their results.
Display predictions clearly."""


from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt
# import seaborn as sns

def DecisionClassifierClass():

    border = '-'*30

    print(border)
    print("Students Performance Analysis")
    print(border)

    ###################################
    #Step 1 : Data loading
    ###################################
    df = pd.read_csv("student_performance_ml.csv")
    print("Data from CSV loaded successfully")

    ###################################
    #Step 2 : Data Analysis
    ###################################

    print(border)
    print("Step 2: Data Analysis")
    print(border)

    print("Total record:", df.shape[0])
    print("Total columns:", df.shape[1])

    df.dropna(inplace=True)
    print("Shape of dataset: ", df.shape)

    print(border)
    print("Seperate independent and dependent variables")
    print(border)  

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']

   
    ###################################
    #Step 3 : Split the data set for training and testing
    ###################################

    print(border)
    print("Step 3 : Split the data set for training and testing")
    print(border) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
    
    print(border)
    print("Details of trainig and testing data")

    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)

    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)
    
    ###################################
    #Step 4: Train the model
    ###################################

    print(border)
    print("Step 4: Train the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=5)

    print("Model gets created successfully")

    print(border)

    model_old = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    Y_pred = model_old.predict(X_test)

    print("Expected answers: ")
    print(Y_test)

    print("Predicted answers :")
    print(Y_pred)

    ###################################
    #Step 4: Evaluate/Test the model performance
    ###################################

    print(border)
    print("Step 4: Evaluate/Test the model performance")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model accurecy is:", accuracy*100,"%")

    new_students = pd.DataFrame({
        "StudyHours": [6, 3, 8, 4, 7],
        "Attendance": [85, 70, 92, 75, 90],
        "PreviousScore": [66, 50, 78, 55, 72],
        "AssignmentsCompleted": [7, 4, 9, 5, 8],
        "SleepHours": [7, 6, 8, 6, 7]
    })

    # Predict results
    Y_pred_new = model.predict(new_students)

    # Add predictions to DataFrame
    new_students["PredictedResult"] = Y_pred_new

    # Convert 0/1 into Fail/Pass
    new_students["PredictedResult"] = new_students["PredictedResult"].map({
        0: "Fail",
        1: "Pass"
    })

    # Display predictions
    print("Predictions for New Students:")
    print(new_students)

def main():
    DecisionClassifierClass()
    
if __name__ == "__main__":
    main()

    