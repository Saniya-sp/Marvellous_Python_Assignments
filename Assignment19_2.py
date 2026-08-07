"""Write a program which contains one lambda function which accepts two parameters and return
its multiplication"""


Mult = lambda x, y : x * y

def main():
    num1 = int(input("enter 1st number: "))
    num2 = int(input("enter 2nd number: "))

    Ret = Mult(num1, num2)
    print(Ret)

if __name__ == "__main__":
    main()