from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def CheckAccuracy(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    K_values = range(1,15)
    accuracy_scores = []

    #Check for which value of K the accuracy is high and use that value of K 
    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(accuracy)

    print("Accuracy report : ",accuracy_scores)
    for no in accuracy_scores:
        print(no*100)


def MarvellousKNNClassifier():

    border = "-"*30

    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print(border)
    print("Marvellous Play Predictor")
    print(border)

    # Step 2 :Clean, prepare and manupulate the dataset
    print(border)
    print("Step 2: Clean, prepare and manupulate the dataset")
    print(border)

    print(df.head())

    print("Total record:", df.shape[0])
    print("Total columns:", df.shape[1])

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(border)
    print("Encode Features having charachter values into numbers")
    print(border) 

    le = LabelEncoder()

    df["Wether"] = le.fit_transform(df["Wether"])
    df["Temperature"] = le.fit_transform(df["Temperature"])

    print(df.head())

    X = df[['Wether', 'Temperature']]
    Y = df['Play']

    print("Independent variables: ", X.head())
    print("Dependent variables:", Y.head())

    # Step 3 : Train data
    print(border)
    print("Step 3:Train data")
    print(border)
       
    weather = int(input("Enter the weather (0/1/2): "))
    temprature = int(input("Enter the temprature (0/1/2): "))

    pred_play = pd.DataFrame({
            "Wether": [weather],
            "Temperature": [temprature]
        })
    print('pred_play: ',pred_play)
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    # Step 4 : Test data
    print(border)
    print("Step 4 : Test data")
    print(border)

    prediction = model.predict(pred_play)

    print("Prediction =", prediction[0])

    # Step 5 : Calculate accuracy
    print(border)
    print("Step 5 : Calculate accuracy")
    print(border)

    CheckAccuracy(X,Y)


def main():
    
    MarvellousKNNClassifier()
    

if __name__ == "__main__":
    main()
