# Hard Voting
#   Heterogeneious models used
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


def VotingClassification():
    border = '*'*40
    #-----------------------------------------------------
    # Step 1 : Load the data set
    #-----------------------------------------------------
    print(border)
    print("Step 1 : Load the data set")
    print(border)
    df = pd.read_csv("Customer_Loan_Approval.csv")

    print("Shape of dataset:", df.shape)
    print("First 5 records")
    print(df.head())

    #-----------------------------------------------------
    #Step 2 : Check for missing values
    #-----------------------------------------------------
    print(border)
    print("Step 2 : Check for missing values")
    print(border)

    print("Check for missing values")
    print(df.isnull().sum())

    #-----------------------------------------------------
    #Step 3 : Seperate features and labels (Input/Output)
    #-----------------------------------------------------
    print(border)
    print("Step 3 : Seperate features and labels (Input/Output)")
    print(border)

    X = df.drop("LoanApproved", axis=1)
    Y = df["LoanApproved"]

    print("X share:", X.shape)
    print("Y share:", Y.shape)

    #-----------------------------------------------------
    # Step 4: Split dataset for training and testing
    #-----------------------------------------------------
    print(border)
    print("Step 4: Split dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # #-----------------------------------------------------
    # # Step 5: Scale the features
    # #-----------------------------------------------------

    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)     #scale the data to maintain in same form 
    # X_test = scaler.fit_transform(X_test)   

    #-----------------------------------------------------
    # Step 5 :Train Logistic Regression
    #-----------------------------------------------------
    print(border)
    print("Step 5 :Train Logistic Regression")
    print(border)

    model_log = LogisticRegression(max_iter=100) 
    model_log = model_log.fit(X_train,Y_train)
    Y_pred_log = model_log.predict(X_test)

    #-----------------------------------------------------
    # Step 6 :Train Decision Tree
    #-----------------------------------------------------
    print(border)
    print("Step 6 :Train Decision Tree")
    print(border)

    model_det = DecisionTreeClassifier(random_state=42)
    model_det = model_det.fit(X_train,Y_train)
    Y_pred_det = model_det.predict(X_test)

    #-----------------------------------------------------
    # Step 7 :Train KNN
    #-----------------------------------------------------
    print(border)
    print("Step 7 :Train KNN")
    print(border)

    model_knn = KNeighborsClassifier(n_neighbors=5)
    model_knn = model_knn.fit(X_train,Y_train)
    Y_pred_knn = model_knn.predict(X_test)

    #-----------------------------------------------------
    # Step 8 : Calculate the individual accuracy of all three algorithms
    #-----------------------------------------------------
    print(border)
    print("Step 8 : Calculate the individual accuracy of all three algorithms")
    print(border)

    print("Accuracy of LR: ", accuracy_score(Y_test, Y_pred_log))
    print("Accuracy of DT: ", accuracy_score(Y_test, Y_pred_det))
    print("Accuracy of KNN: ", accuracy_score(Y_test, Y_pred_knn))

    #-----------------------------------------------------
    # Step 9 :Create the hard voting classifier
    #-----------------------------------------------------
    print(border)
    print("Step 9 :Create the hard voting classifier")
    print(border)

    model = VotingClassifier(
        estimators=[
            ('logistic',model_log),         #model names (logistic) are fixed 
            ('decision_tree',model_det), 
            ('knn',model_knn) 
            ], 
        voting="hard"
    )

    model  = model.fit(X_train, Y_train)

    Y_pred_hard  = model.predict(X_test)

    #-----------------------------------------------------
    # Step 10 : Calculate its accuracy
    #-----------------------------------------------------

    print(border)
    print("Step 10 : Calculate its accuracy")
    print(border)

    print("Accuracy is: ", accuracy_score(Y_test, Y_pred_hard) * 100 , "%")
    print("COnfusion matrix:", confusion_matrix(Y_test, Y_pred_hard))

    #-----------------------------------------------------
    # Step 11 :Create the soft voting classifier
    #-----------------------------------------------------
    print(border)
    print("Step  11 :Create the soft voting classifier")
    print(border)

    model = VotingClassifier(
        estimators=[
            ('logistic',model_log),         #model names (logistic) are fixed 
            ('decision_tree',model_det), 
            ('knn',model_knn) 
            ], 
        voting="soft"
    )

    model  = model.fit(X_train, Y_train)

    Y_pred_soft  = model.predict(X_test)

    #-----------------------------------------------------
    # Step 12 : Calculate its accuracy
    #-----------------------------------------------------
    print(border)
    print("Step 12 : Calculate its accuracy")
    print(border)

    print("Accuracy is: ", accuracy_score(Y_test, Y_pred_soft) * 100 , "%")
    print("COnfusion matrix:", confusion_matrix(Y_test, Y_pred_soft))

def main():
    VotingClassification()

if __name__ == "__main__":
    main()
