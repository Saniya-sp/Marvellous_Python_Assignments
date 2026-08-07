"""Write a program which accepts number from user and return addition of digits in that number
ip; 5187934     op: 7"""

def Add(num):
    sum = 0
    for no in num:
        sum = sum + int(no)

    return sum

def main():
    num = (input("Enter number: "))
    Ret = Add(num)
    print(Ret)

if __name__ == "__main__":
    main()

    