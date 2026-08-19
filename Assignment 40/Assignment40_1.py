"""After training the decision tree model, use:
model.feature_importances_
    -Display importance score of each feature
    -Which feature contributes the most in predicting FinalResult?
    -Which feature contributes the least?
"""


from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def main():
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

    print(border)

    ###################################
    #Step 4: Train the model
    ###################################

    print(border)
    print("Step 4: Train the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=5)

    print("Model gets created successfully")

    print(border)

    model = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    # Get feature importance
    importance = model.feature_importances_

    # Display importance of each feature
    for feature, score in zip(X.columns, importance):
        print(feature, ":", score)

    # Find most and least important features
    most_important = X.columns[importance.argmax()]
    least_important = X.columns[importance.argmin()]

    print("\nMost important feature:", most_important)
    print("Least important feature:", least_important)


    
if __name__ == "__main__":
    main()
    
