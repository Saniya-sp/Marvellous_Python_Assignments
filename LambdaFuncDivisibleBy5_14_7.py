"""Write a lambda function which accepts one number and returns True if divisible by 5."""

Divisible = lambda a: a % 5 == 0    #All logical operators return boolean value (True/False)

def main():

    number = int(input("enter first number: "))
    
    Ret = Divisible(number)
    
    print(Ret)

if __name__ == "__main__":
    main()
