"""Write a lambda function using reduce() which accepts list of numbers and 
returns the product of all numbers"""

from functools import reduce

Multiplication = lambda x, y: x * y

def main():
    Data = [5,2,3,20,15]

    print("Input data is :",Data)

    RData = reduce(Multiplication, Data)
    print("FData is: ",RData)
 

if __name__ == "__main__":
    main()

