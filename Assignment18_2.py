"""write a program which accept N numbers from user and store it into List. 
Return maximum number from that List
ip: Number of elements : 6
input elements: 13 5 45 7 4 56
op: 130
"""
from functools import reduce

def MaxNum(x, y):
    
    if x > y:
        return x
    else:
        return y


def main():
    n = int(input("Number of elements (N): "))
    
    numbers_list = []
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(num)
    
    Ret = reduce(MaxNum, numbers_list)
    print(Ret)


if __name__ == "__main__":
    main()


