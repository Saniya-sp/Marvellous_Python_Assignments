"""Write a program which contains one function named as ChkNum()
which accept one parameter a snumber. If number is even then it 
should display 'Even number' otherwise display 
'Odd number' on console."""


def ChkNum(no):
    if (no % 2 == 0):
        return True
    else:
        return False
    

def main():
    num = int(input("Enter number: "))
    Ret = ChkNum(num)
    if Ret == True:
        print("Even number.")
    else:
        print("Odd number.")


if __name__ == "__main__":
    main()
