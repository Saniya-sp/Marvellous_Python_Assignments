"""Decision tree visualization
use: from sklern.tree import plot_tree
Visualise the trained decision tree:
    WHICH FEATURE appears at the root node?
    Why do you think that feature was selected first
"""


from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


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
    print("Shape of X_test:",X_test.shape, X_test)

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

    model = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    Y_pred = model.predict(X_test)

    print("Expected answers: ")
    print(Y_test)

    print("Predicted answers :")
    print(Y_pred)


    #Visualization
    plt.figure(figsize=(12, 8))

    plot_tree(
        model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True,
        rounded=True,
        fontsize=8
    )
    plt.title("Marvellous Decision Tree Classifier")

    plt.show()

    root_index = model.tree_.feature[0]

    root_feature = X.columns[root_index]

    print("Root Feature:", root_feature)

def main():
    DecisionClassifierClass()
    
if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------------------------------------------------
# WHICH FEATURE appears at the root node?
    # Root Feature: Attendance
    # then Attendance is the first feature used by tree.
    
# Why do you think that feature was selected first
    # The feature appearing at the root node is selected because it provides the best split for separating Pass and Fail students 
    # in the training data. It gives the maximum reduction in impurity among the available features at the root.
    