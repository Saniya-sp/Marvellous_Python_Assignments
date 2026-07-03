"""Write a lambda function using filter() which accepts list of numbers and 
returns count of even numbers"""


EvenNum = lambda x: x if (x % 2 == 0) else False

def main():
    Data = [50,2,31,60,25,3,20,15]

    print("Input data is :",Data)

    FData = list(filter(EvenNum, Data)) 

    print("Total even numbers are: ",len(FData))
 

if __name__ == "__main__":
    main()

