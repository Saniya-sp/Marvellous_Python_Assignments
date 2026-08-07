"""Write a program which accepts number from user and check whether that number is positive or negative or zero.
i/p: 11     op: Positive number
i/p: -8     op: Negative number
# i/p: 0     op: ero
"""

def Display(num):

    if num > 0:
        return True
    elif num < 0:
        return False
    else:
        return "Zero"
    

def main():
    num1 = int(input("Enter number: "))

    Ret = Display(num1)

    if Ret:
        print("Positive number")
    else:
        print("Negative number")

    if Ret == "Zero":
        print("Zero")


if __name__ == "__main__":
    main()
    