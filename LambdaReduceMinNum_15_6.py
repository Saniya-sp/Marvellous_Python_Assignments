"""Write a lambda function using reduce() which accepts list of numbers and returns the minimum element"""

from functools import reduce

MinNum = lambda x, y: x if x < y else y

def main():
    Data = [13,12,18,80,11,20]

    print("Input data is :",Data)

    RData = reduce(MinNum, Data)   
    print("Minimum number is: ",RData)


if __name__ == "__main__":
    main()

  