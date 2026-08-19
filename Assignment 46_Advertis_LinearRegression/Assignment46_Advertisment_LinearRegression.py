import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score


def MarvellousRegression(DataPath):

    Border = "-"*40

    #########################################
    #Step 1: Load the Data
    #########################################

    print(Border)
    print("Step 1: Load the Data")
    print(Border)
    
    df = pd.read_csv(DataPath)
    print(df.head())

    #########################################
    #Step 2 : Clean, prepare and manipulate data.
    #########################################
    
    print(Border)
    print("Step 2: Clean, prepare and manipulate data.")
    print(Border)

    #  Remove unwanted columns
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head()) 

    #########################################
    # Check missing values
    #########################################
    
    print(Border)
    print("Step 3: Check missing values")
    print(Border)  

    print("Total missing values:")
    print(Border)  
    print(df.isnull().sum())
    print(Border)  
    
    #########################################
    #Seperate independent and dependent variable
    #########################################

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent variables: ", X.head())
    print("Dependent variables:", Y.head())
 
    #########################################
    #Split the dataset
    #########################################

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Training data: ",X_train.shape)
    print("Testing data: ",X_test.shape)

    #########################################
    #Step 3: Create and train the model
    #########################################
    
    print(Border)
    print("Step 3: Create and train the model")
    print(Border) 

    model = LinearRegression()
    model = model.fit(X_train, Y_train)

    print("Model trained successfully..")

    #########################################
    #Step 4: Test the model
    #########################################
    
    print(Border)
    print("Step 4: Test the model")
    print(Border)    

    Y_pred = model.predict(X_test)

    #########################################
    #Step 5: Display predicted and expected values
    #########################################
    
    print(Border)
    print("Step 5: Display predicted and expected values")
    print(Border) 

    print("Expected answers: ")
    print(Y_test[:3])

    print("Predicted answers")
    print(Y_pred[:3])



def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()

