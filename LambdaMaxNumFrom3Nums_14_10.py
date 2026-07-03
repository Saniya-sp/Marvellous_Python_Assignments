"""Write a lambda function which accepts two numbers and returns maximum number"""

MaxNumber1 = lambda a, b, c: a > b > c    #All logical operators return boolean value (True/False)
MaxNumber2 = lambda b, c: b > c             

def main():

    number1 = int(input("enter first number: "))
    number2= int(input("enter second number: "))
    number3= int(input("enter third number: "))
    
    Ret1 = MaxNumber1(number1, number2, number3)
    
    print(Ret1)

    if (Ret1 == True):
        print("Maximum number is :",number1)
    else:
        
        Ret2 = MaxNumber2(number2, number3)

        if (Ret2 == True):
            print("Maximum number is :",number2)
        else:
            print("Maximum number is :",number3)


if __name__ == "__main__":
    main()

