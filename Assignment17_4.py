"""Write a program which accepts one number and return addition of its factors
ip = 12
op = 1+2+3+4+6"""

def FindSumOfFactors(no):
    factors = list()

    for num in range(1, no):
        if no % num == 0:
            factors.append(num)
        
    sum = 0
    for num in factors:
        sum = sum + num

    return sum


def main():

    num = int(input("enter number: "))
    Ret = FindSumOfFactors(num)
    
    print("Sum of Factors is :",Ret)
    

if __name__ == "__main__":
    main()
