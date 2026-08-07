"""Write a program which contains filter(), map(), and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user.
Filter should filter out all such numbers which are greater that or equal to 70 and less than
or equal to 90. Map function will increase each number by 10. Reduce will return product of
all that numbers.
"""
from functools import reduce

FilterNum = lambda x: x if x >= 70 and x <= 90 else False
Increase = lambda x : x + 10
Product = lambda x, y : x * y

def main():
    nums = [4, 34,36,76,68,24,89,23,86,90,45,70]
    FData = list(filter(FilterNum, nums))
    MData = list(map(Increase, FData))
    RData = (reduce(Product, MData))

    print(FData)
    print(MData)
    print(RData)

if __name__ == "__main__":
    main()