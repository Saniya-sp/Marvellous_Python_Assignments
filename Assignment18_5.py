"""write a program which accept N numbers from user and store it into List. 
Return addition of all prime numbers from that list. Main python file accepts N 
numbers from user and pass aech number to ChkPrime() function which is part of our 
user defined module named as MarvellousNum. Name of the function from main python 
file should be ListPrime()
ip: Number of elements : 11
input elements: 13 5 45 7 4 56 10 34 2 5 8
op: 54 (13+5+7+2+5)
"""

from MarvellousNum import ChkPrime
      
def ListPrime(numbers_list):
    sum = 0

    for no in numbers_list:     
        Ret = ChkPrime(no)
        if Ret:
            print(Ret, no)
            sum = sum + no

    return sum

def main():
    n = int(input("Number of elements (N): "))
    
    numbers_list = []
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(num)

    Ret = ListPrime(numbers_list)
    print("Final=",Ret)


if __name__ == "__main__":
    main()


