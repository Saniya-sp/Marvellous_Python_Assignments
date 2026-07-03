"""Write a lambda function using reduce() which accepts list of numbers and returns the maximum element"""

from functools import reduce

MaxNum = lambda x, y: x if x > y else y

def main():
    Data = [13,12,8,80,11,20]

    print("Input data is :",Data)

    RData = reduce(MaxNum, Data)   
    print("Maximum number is: ",RData)

  
if __name__ == "__main__":
    main()

