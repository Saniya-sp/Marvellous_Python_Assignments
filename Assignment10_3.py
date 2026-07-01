"""Write a program which accepts one number and prints factorial of that number."""

def Factorial(no):

    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    return fact

def main():
    num = int(input("enter number: "))
    Ret = Factorial(num)
    print("Factorial is:", Ret)

if __name__ == "__main__":
    main()
    