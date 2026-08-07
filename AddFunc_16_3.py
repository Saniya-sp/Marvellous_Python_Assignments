"""Write a program which contains one function named as Add()
which accept two numbers from user and return addition of that two numbers."""


def Add(no1, no2):
    return no1 + no2
    
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    Ret = Add(num1, num2)
    
    print(f"Addition is: {Ret}")


if __name__ == "__main__":
    main()
