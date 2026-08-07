"""Write a program which contains filter(), map(), and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user.
Filter should filter out all such numbers which are even. Map function will calculate its
square. Reduce will return addition of all that numbers.
"""

from functools import reduce

CheckEven = lambda x : x if (x % 2) == 0 else False
CalcSquare = lambda x: x ** 2
Addition = lambda x, y : x + y

def main():
    nums = [5,2,3,4,3,4,1,2,8,10]
    
    FData = list(filter(CheckEven, nums))
    MData = list(map(CalcSquare, FData))
    RData = (reduce(Addition, MData))

    print(FData)
    print(MData)
    print(RData)

if __name__ == "__main__":
    main()