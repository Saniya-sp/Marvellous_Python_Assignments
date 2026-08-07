"""Write a program which accepts number from user and 
return true if number is divisible by 5 otherwise return false
"""

def Display(num):

    if num % 5 == 0:
        return True
    else:
        return False
    

def main():
    num1 = int(input("Enter number: "))

    Ret = Display(num1)

    print(Ret)


if __name__ == "__main__":
    main()
    