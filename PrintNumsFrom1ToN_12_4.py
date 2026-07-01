"""Write a program which accepts one number and prints that many numbers starting from 1
ip =5
op = 1,2,3,4,5"""

def allNumbers(num):
    nums = list()
    for i in range(1, num+1):
        nums.append(i)

    return nums

def main():

    num = int(input("enter number: "))
    Ret = allNumbers(num)
    
    print("All Numbers are :",Ret)
    

if __name__ == "__main__":
    main()