"""Train model with
    max_depth = None
Calculate;
    Training accuracy
    Testing accuracy

If training accuracy is 100 and testing accuracy is lower explain why this happens.
"""

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

    new_col = {}

    # --------------------------------------------------
    # Create new feature
    # --------------------------------------------------

    df["PerformanceIndex"] = (
        (df["StudyHours"] * 2) + df["Attendance"]
    )

    print("Dataset with PerformanceIndex:")
    print(df)

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
    print("Shape of X_test:",X_test.shape, X_test)

    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)
    
    ###################################
    #Step 4: Train the model
    ###################################

    print(border)
    print("Step 4: Train the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=None)

    print("Model gets created successfully")

    print(border)

    model_old = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    Y_train_pred = model_old.predict(X_train)
    # Prediction on testing data
    Y_test_pred = model.predict(X_test)

    # Calculate accuracies
    training_accuracy = accuracy_score(Y_train, Y_train_pred)
    testing_accuracy = accuracy_score(Y_test, Y_test_pred)

    print("Training Accuracy:", training_accuracy * 100, "%")
    print("Testing Accuracy:", testing_accuracy * 100, "%")

def main():
    DecisionClassifierClass()

if __name__ == "__main__":
    main()

#Observation: No changes in accuracies. Both the accuracy are 100%

