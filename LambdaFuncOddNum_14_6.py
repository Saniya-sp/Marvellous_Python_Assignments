"""Write a lambda function which accepts one number and returns True if number is odd otherwise False."""

OddNumber = lambda a: a % 2 != 0    #All logical operators return boolean value (True/False)

def main():

    number = int(input("enter first number: "))
    
    Ret = OddNumber(number)
    
    print(Ret)

if __name__ == "__main__":
    main()
