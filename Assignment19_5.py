"""Write a program which contains filter(), map(), and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user.
Filter should filter out all prime numbers. Map function will multiply each number by 2.
Reduce will return maximum num of all that numbers.
"""
from functools import reduce

def ChkPrime(no):
    if no == 2:
        return True
    
    if no % 2 == 0:
        return False
    
    # print(int(no**0.5)+1)
    for i in range(3,int(no**0.5)+1,2):
        print("i = ",i)
        if no % i == 0:
            return False
        
    return True

# CheckEven = lambda x : x if (x % 2) == 0 else False
MultBy2 = lambda x: x * 2
MaxNum = lambda x, y :x if x > y else y

def main():
    nums = [2,70,11,10,17,23,31,77]
    prime_nums = []
    for no in nums:
        Ret = ChkPrime(no)
        if Ret:
            prime_nums.append(no)
    print('prime_nums = ',prime_nums)

    FData = list(filter(ChkPrime, nums))
    MData = list(map(MultBy2, FData))
    RData = (reduce(MaxNum, MData))

    print(FData)
    print(MData)
    print(RData)

if __name__ == "__main__":
    main()