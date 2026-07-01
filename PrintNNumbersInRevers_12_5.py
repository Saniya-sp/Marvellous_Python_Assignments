"""Write a program which accepts one number and prints that many numbers in reverse order
ip = 5
op = 5 4 3 2 1"""

def allReverseNumbers(num):
    nums = list()
    for i in range(num, 0, -1):
        nums.append(i)
    
    return nums

def main():

    num = int(input("enter number: "))
    Ret = allReverseNumbers(num)
    
    print("All reverse Numbers are :",Ret)
    

if __name__ == "__main__":
    main()