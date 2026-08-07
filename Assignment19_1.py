"""Write a program which contains one lambda function which accepts one parameter and return
power of two"""


Power2OfNum = lambda x : x ** 2

def main():
    num = int(input("enter number: "))
    Ret = Power2OfNum(num)
    print(Ret)

if __name__ == "__main__":
    main()