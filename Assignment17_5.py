"""Write a program which accepts one number and checks whether it is prime or not"""


def CheckPrime(no):
    isOdd = []
    # print("** : ",no**no)
    if (no % 2 == 0):
        return False
    
    for i in range(2, int(no**0.5)+1): 

        if (no % i == 0):
            return False
            
        else:
            return True

def main():

    num = int(input("enter number: "))
    Ret = CheckPrime(num)
    
    if Ret:
        print("Number is prime:")
    else:
        print("Not prime number:")


if __name__ == "__main__":
    main()

