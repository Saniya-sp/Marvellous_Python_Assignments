"""Write a lambda function which accepts one number and returns square of that number."""


square = lambda a: a*a

def main():

    number = int(input("enter number: "))
    
    Ret = square(number)
    
    print(Ret)

if __name__ == "__main__":
    main()