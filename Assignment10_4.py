"""Write a program which accepts one number and prints all even numbers till that number"""

def CheckAllEven(no):
    isEven = []
    
    for i in range(1,no+1):
        if (i % 2 == 0):
            isEven.append(i)

    return isEven

def main():
    num = int(input("enter number: "))
    Ret = CheckAllEven(num)
    print("Even numbers are:", Ret)


if __name__ == "__main__":
    main()




