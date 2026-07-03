"""Write a lambda function which accepts two numbers and returns multiplication"""

mult = lambda a, b: a * b     #All logical operators return boolean value (True/False)

def main():

    number1 = int(input("enter first number: "))
    number2= int(input("enter second number: "))
    
    Ret = mult(number1, number2)
    
    print("Multiplication is:",Ret)

if __name__ == "__main__":
    main()
