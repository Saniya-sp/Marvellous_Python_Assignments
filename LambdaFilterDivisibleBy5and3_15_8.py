"""Write a lambda function using filter() which accepts list of numbers and 
returns the list of numbers which are divisible by both 3 & 5"""


IsDivisible = lambda x: x if (x % 5 == 0) and (x % 3 == 0) else False
  
def main():
    Data = [5,2,30,60,25,3,20,15]

    print("Input data is :",Data)

    FData = list(filter(IsDivisible, Data))  
    print("FData is: ",FData)


if __name__ == "__main__":
    main()

