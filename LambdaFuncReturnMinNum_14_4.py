"""Write a lambda function which accepts two numbers and returns minimum number"""

MinNumber = lambda a, b: a < b     #All logical operators return boolean value (True/False)

def main():

    number1 = int(input("enter first number: "))
    number2= int(input("enter second number: "))
    
    Ret = MinNumber(number1, number2)
    
    print(Ret)

    if (Ret == True):
        print("Minumum number is :",number1)
    else:
        print("Minumum number is :",number2)

if __name__ == "__main__":
    main()
