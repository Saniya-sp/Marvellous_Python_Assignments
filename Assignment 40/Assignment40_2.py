"""Remove the column SleepHours from dataset.
Train the model again
Compare new accuracy with previous accuracy
Does removing this feature affect performance?
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
    X_new = df.drop(columns=['SleepHours','FinalResult'])
    Y = df['FinalResult']

    print("Shape of new X:",X_new.shape)
    

    ###################################
    #Step 3 : Split the data set for training and testing
    ###################################

    print(border)
    print("Step 3 : Split the data set for training and testing")
    print(border) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42, stratify=Y)
    X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(X_new, Y, test_size=0.2, random_state=42, stratify=Y)

    print(border)
    print("Details of trainig and testing data")

    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)

    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)
    
    print(border)

    print("Shape of X_train_new:",X_train_new.shape)
    print("Shape of X_test_new:",X_test_new.shape)

    print("Shape of Y_train_new:",Y_train_new.shape)
    print("Shape of Y_test_new:",Y_test_new.shape)

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

    ## Train and Prediction with new X
    model_new = model.fit(X_train_new, Y_train_new)
    print("Model trained successfully.")

    Y_pred_new = model_new.predict(X_test_new)

    print("Expected answers: ")
    print(Y_test_new)

    print("Predicted answers :")
    print(Y_pred_new)
    ###################################
    #Step 7: Evaluate/Test the model performance
    ###################################

    print(border)
    print("Step 7: Evaluate/Test the model performance")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model accurecy is:", accuracy*100,"%")

    accuracy_new = accuracy_score(Y_test_new, Y_pred_new)
    
    print("New Model accurecy is:", accuracy_new*100,"%")
    

    
if __name__ == "__main__":
    main()
    

#--------------------------------------------------

# Observation:
#     There is no change in accuracy score befor and after removing the SleepHours column

