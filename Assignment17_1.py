"""Create a module named as Arithmetic which contains 4 functions as Add() for addition
, SUb() for subtraction, Mult() for multiplication, and Div() for division. All functions accepts
two parameters as number and perform the operation. Write on python program which call all
the functions from Arithmetic module by accepting the parameters from user."""

from Arithmatic import Add, Sub, Mult, Div


def main():

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    
    Sum = Add(num1, num2)
    Sub_ = Sub(num1, num2)
    Mult_ = Mult(num1, num2)
    Div_ = Div(num1, num2)
    
    print("Addition is :",Sum)
    print("Subtraction is :",Sub_)
    print("Multiplication is :",Mult_)
    print("Division is :",Div_)
    

if __name__ == "__main__":
    main()