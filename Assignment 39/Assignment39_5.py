"""Calculate 
-Training Accuracy
-Testing Accuracy
Compare both and comment whether the model is overfitting or underfitting
"""

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt


def main():
    border = '-'*30

    print(border)
    print("Students Performance Analysis")
    print(border)

    df = pd.read_csv("student_performance_ml.csv")

    #Step 1 : CLean the dataset
    print(border)
    print("Step 2: Clean the dataset")
    print(border)

    print("Total record:", df.shape[0])
    print("Total columns:", df.shape[1])

    df.dropna(inplace=True)
    print("Shape of dataset: ", df.shape)

    #Step 3 : Seperate independent and dependent variables
    print(border)
    print("Step 3 : Seperate independent and dependent variables")
    print(border)  

    X = df.drop(columns=['FinalResult'])
    Y = df['FinalResult']


    #Step 4 : Split the data set for training and testing
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
    #Step 5: Build the model
    ###################################

    print(border)
    print("Step 5: Build the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=5)

    print("Model gets created successfully")

    ###################################
    #Step 6: Train the model
    ###################################

    print(border)
    print("Step 6: Train the model")
    print(border)

    model = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    ###################################
    #Step 7: Evaluate/Test the model
    ###################################

    print(border)
    print("Step 7: Evaluate/Test the model")
    print(border)

    Y_pred = model.predict(X_test)
    print("MOdel evaluation/testing done")

    print("Expected answers: ")
    print(Y_test)

    print("Predicted answers :")
    print(Y_pred)

    ###################################
    #Step 8: Evaluate/Test the model performance
    ###################################

    print(border)
    print("Step 8: Evaluate/Test the model performance")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model accurecy is:", accuracy*100,"%")

    print("Confusion matrix: " )
    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    #9 Display confusion matrix
    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Fail", "Pass"]
    )

    display.plot()
    plt.title("Confusion Matrix")
    plt.show()

    # 10. Predict target labels for both datasets
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # 11. Compute the accuracy scores
    train_accuracy = accuracy_score(Y_train, y_train_pred)
    test_accuracy = accuracy_score(Y_test, y_test_pred)

    # 6. Display the metrics
    print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
    print(f"Testing Accuracy:  {test_accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()


#------------------------------------------------------------------


# ----Observation: 
#   Training and testing accuracy are approximately the same, indicating that the model is performing consistently on both 
# training and unseen data. Therefore, there is no significant evidence of overfitting.

# ----General rule

# Training Accuracy	    Testing Accuracy	Interpretation
# High	                High and similar	✅ Good fit
# Very high	                Much lower	    ⚠️ Overfitting
# Low	                    Low	            ⚠️ Underfitting
# Low	                    Higher	        Usually investigate the split/data

# ----For example:

    # Training = 100%
    # Testing  = 60%

    # → Overfitting

    # Training = 65%
    # Testing  = 60%

    # → Likely underfitting / weak model

    # Training = 85%
    # Testing  = 80%

    # → Reasonably good fit