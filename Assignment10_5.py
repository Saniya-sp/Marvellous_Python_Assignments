"""Write a program which accepts one number and prints all odd numbers till that number"""

def CheckAllOdd(no):
    isOdd = []
    
    for i in range(1,no+1):
        if (i % 2 != 0):
            isOdd.append(i)

    return isOdd

def main():
    num = int(input("enter number: "))
    Ret = CheckAllOdd(num)
    print("Odd numbers are:", Ret)


if __name__ == "__main__":
    main()




