from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousClassifier(DataPath):
    border = "-"*40
    print(border)
    ##########################################
    #Step 1: Load the Dataset from csv file
    #all steps = MLOp pipeline
    ##########################################
    print(border)
    print("Step 1: Load the Dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset")
    print(border)

    print(df.head())
    print(border)

    ##########################################
    #Step 2 : CLean the dataset
    ##########################################
    print(border)
    print("Step 2: Clean the dataset")
    print(border)

    print("Total record:", df.shape[0])
    print("Total columns:", df.shape[1])

    df.dropna(inplace=True)
    print("Shape of dataset: ", df.shape)

    print("Total record:", df.shape[0])
    print("Total columns:", df.shape[1])
    print(border)

    ##########################################
    #Step 3 : Seperate independent and dependent variables
    ##########################################
    
    print(border)
    print("Step 3 : Seperate independent and dependent variables")
    print(border)  

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of x: ",X.shape)   #(178,13)
    print("Shape of y: ",Y.shape)#(178,1)

    print(border)
    print("Input columns: ",X.columns.to_list())
    print("Output columns: Class")

    ##########################################
    #Step 4 : Split the data set for training and testing
    ##########################################
    
    print(border)
    print("Step 4 : Seperate independent and dependent variables")
    print(border) 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    print(border)
    print("Details of trainig and testing data")

    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)

    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)

    print(border)

    ##########################################
    #Step 5: Feature scaling
    ##########################################
    
    print(border)
    print("Step 5 : Feature scaling")
    print(border) 

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)#used to scale data diff in values in hight  
    X_test_scaled = scaler.fit_transform(X_test)#used to scale data diff in values in hight 

    print("Feature scaling done")
    print(border)

    #Hyper param tuning

    ##########################################
    #Step 6: Hyper param tuning
    ##########################################
    
    print(border)
    print("Step 6: Hyper param tuning")
    print(border) 

    
    model = KNeighborsClassifier(n_neighbors=9)
    model = model.fit(X_train_scaled, Y_train)
    Y_pred = model.predict(X_test_scaled)
    
    print("accuracy: ",accuracy_score(Y_test, Y_pred) * 100)
    print(border) 



def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()