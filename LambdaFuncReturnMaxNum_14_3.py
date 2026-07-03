"""Write a lambda function which accepts two numbers and returns maximum number"""

MaxNumber = lambda a, b: a > b     #All logical operators return boolean value (True/False)

def main():

    number1 = int(input("enter first number: "))
    number2= int(input("enter second number: "))
    
    Ret = MaxNumber(number1, number2)
    
    print(Ret)

    if (Ret == True):
        print("Maximum number is :",number1)
    else:
        print("Maximum number is :",number2)

if __name__ == "__main__":
    main()
