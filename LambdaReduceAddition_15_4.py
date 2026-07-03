"""Write a lambda function using reduce() which accepts a list of numbers and returns addition of numbers."""

from functools import reduce

sum = lambda a, b: a + b

def main():
    Data = [13,12,8,10,11,20]

    print("Input data is :",Data)

    RData = reduce(sum, Data)   
    print("Addition is: ",RData)

  
if __name__ == "__main__":
    main()
