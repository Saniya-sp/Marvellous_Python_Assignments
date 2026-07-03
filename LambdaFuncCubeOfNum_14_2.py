"""Write a lambda function which accepts one number and returns cube of that number."""

cube = lambda a: a*a*a

def main():

    number = int(input("enter number: "))
    
    Ret = cube(number)
    
    print(Ret)

if __name__ == "__main__":
    main()