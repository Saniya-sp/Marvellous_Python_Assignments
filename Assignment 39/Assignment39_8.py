"""Write a single stuctured Python program that will performs:
1.Data loading
2.Data analysis
3.Visualization
4.Train-test-split
5.Model training
6.Prediction
7.Accuracy calculation
8.Confusion matrix generation
9.Final conclusion
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
    #Step 3 : Visualization
    ###################################

    # Calculate correlation
    correlation = df.corr()

    # Display heatmap
    sns.heatmap(correlation, annot=True)

    plt.title("Student Performance Correlation")
    plt.show()


    ###################################
    #Step 4 : Split the data set for training and testing
    ###################################

    print(border)
    print("Step 4 : Split the data set for training and testing")
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
    #Step 5: Train the model
    ###################################

    print(border)
    print("Step 5: Train the model")
    print(border)

    model = DecisionTreeClassifier(max_depth=5)

    print("Model gets created successfully")

    print(border)

    model = model.fit(X_train, Y_train)
    print("Model trained successfully.")

    ###################################
    #Step 6: Evaluate/Test the model
    ###################################

    print(border)
    print("Step 6: Evaluate/Test the model")
    print(border)

    Y_pred = model.predict(X_test)
    print("MOdel evaluation/testing done")

    print("Expected answers: ")
    print(Y_test)

    print("Predicted answers :")
    print(Y_pred)

    ###################################
    #Step 7: Evaluate/Test the model performance
    ###################################

    print(border)
    print("Step 7: Evaluate/Test the model performance")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Model accurecy is:", accuracy*100,"%")

    ###################################
    #Step 8: Confusion matrix generation
    ###################################

    print(border)
    print("Step 8: Confusion matrix generation")
    print(border)

    print("Confusion matrix: " )
    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    print(border)
    print("Display Confusion matrix")
    print(border)
    
    # Display confusion matrix
    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Fail", "Pass"]
    )

    display.plot()
    plt.title("Confusion Matrix")
    plt.show()

    
if __name__ == "__main__":
    main()
    