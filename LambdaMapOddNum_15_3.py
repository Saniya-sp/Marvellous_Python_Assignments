"""Write a lambda function using filter() which accepts a list of numbers and return a list of odd numbers."""

CheckOdd = lambda No: (No % 2 !=0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is :",Data)
  
    FData = list(filter(CheckOdd, Data))   #Passed function(Increment) should return value and should accept only one parameter
    print("Data after filter: ",FData)


if __name__ == "__main__":
    main()
