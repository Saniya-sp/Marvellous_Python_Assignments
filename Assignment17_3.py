"""Write a program which accepts one number and prints its factorial
ip = 5
op = 120"""

def FindFactorial(no):
    
    fact = 1
    for i in range(1, no+1):
        fact = fact * i

    return fact


def main():

    num = int(input("enter number: "))
    Ret = FindFactorial(num)
    
    print("Factorial is :",Ret)
    

if __name__ == "__main__":
    main()
