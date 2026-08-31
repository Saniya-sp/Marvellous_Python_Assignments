
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt


def MarvellousBreastCancer():

    ########################################################
    # Step 1 : Load and explore the data set
    ########################################################
    
    border = '-'*40
    print(border)
    print("Step 1: Load and explore the data set")
    print(border)

    DataSet = load_breast_cancer()

    print("Available keys:")
    print(DataSet.keys())

    #MetaData of dataset
    print("Independent variables are: ")    #Labels
    print(DataSet.feature_names)
    print("Length of independent variable: ",len(DataSet.feature_names))

    print("Dependent variables are: ")
    print(DataSet.target_names)
    print("Length of dependent variable: ",len(DataSet.target_names))

    ########################################################
    # #Step 2 : Perform data preprocessing steps
    ########################################################
    print(border)
    print("Step 2 : Perform data preprocessing steps")
    print(border)

    df = pd.DataFrame(
        DataSet.data,
        columns=DataSet.feature_names
    )

    df["target"] = DataSet.target

    print("First 5 records are:")
    print(df.head())

    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])

    #Check missing values
    print("Missing Values:")
    print(df.isnull().sum())

    #Create X and Y

    X = df.drop(columns=["target"])
    Y = df["target"]

    print("X Shape:", X.shape)
    print("Y Shape:", Y.shape)

    print(border)
    print("Step 3: Perform exploratory data analysis (EDA)")
    print(border)

    #Summary statistics
    print(df.describe())

    ########################################################
    #Step 3: Visualization of feature correlation
    ########################################################
    print(border)
    print("Step 3 :Visualization of feature correlation")
    print(border)

    plt.figure(figsize=(8, 6))

    plt.scatter(
        df[df["target"] == 0]["mean radius"],
        df[df["target"] == 0]["mean texture"],
        label="Malignant"
    )

    plt.scatter(
        df[df["target"] == 1]["mean radius"],
        df[df["target"] == 1]["mean texture"],
        label="Benign"
    )

    plt.xlabel("Mean Radius")
    plt.ylabel("Mean Texture")
    plt.title("Mean Radius vs Mean Texture")

    plt.legend()
    plt.show()


    ########################################################
    # # Step 4: Split dataset for training and testing
    ########################################################
    print(border)
    print("Step 4:Split dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    #Feature scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.fit_transform(X_test)

    ########################################################
    # Step 5: Creat Classification model
    ########################################################
    print(border)
    print("Step 5: Creat Classification model")
    print(border)


    model = LogisticRegression(
        max_iter=1000
    )

    print(
        "Logistic Regression model created successfully"
    )

    ########################################################
    # Step 6: Train the model
    ########################################################
    print(border)
    print("Step 6: Train the model")
    print(border)

    model.fit(
            X_train,
            Y_train
        )

    print("Model trained successfully")

    ########################################################
    # Step 7: Test  the model
    ########################################################
    print(border)
    print("Step 7: Test the model")
    print(border)

    Y_pred = model.predict(X_test)

    ########################################################
    # Step 8:  Calculate the model accuracy
    ########################################################
    print(border)
    print("Step 8: Calculate the model accuracy")
    print(border)

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print( "Accuracy:", accuracy)

    print("Accuracy Percentage:", accuracy * 100)

    ########################################################
    # Step 9: Confusion Matrix
    ########################################################
    print(border)
    print("Step 9: Confusion Matrix")
    print(border)

    cm = confusion_matrix( Y_test, Y_pred)

    print("Confusion Matrix:")
    print(cm)


    ########################################################
    # Step 10 : Classification Report (Precision, recall, F1 score)
    ########################################################

    print(border)
    print("Step 10 : Classification Report (Precision, recall, F1 score)")
    print(border)

    report = classification_report(
        Y_test,
        Y_pred,
        target_names=DataSet.target_names
    )

    print(report)


def main():

    MarvellousBreastCancer()


if __name__ == "__main__":

    main()