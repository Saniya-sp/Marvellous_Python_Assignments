"""Write a program which accepts two numbers and prints addition, subtraction, multiplication and division."""


def Addition(no1,no2):
    return no1 + no2

def Subtraction(no1,no2):
    return no1 - no2

def Multiplication(no1,no2):
    return no1 * no2

def Division(no1,no2):
    return no1 / no2


def main():

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    
    Sum = Addition(num1, num2)
    Sub = Subtraction(num1, num2)
    Mult = Multiplication(num1, num2)
    Div = Division(num1, num2)
    
    print("Addition is :",Sum)
    print("Subtraction is :",Sub)
    print("Multiplication is :",Mult)
    print("Division is :",Div)
    

if __name__ == "__main__":
    main()

