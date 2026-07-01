"""Write a program which accepts one number and checks whether it is perfect number or not
ip = 6
op = Perfect Number
A perfect number is a positive integer that equals the sum of its proper 
positive divisors (excluding the number itself). For example, the proper divisors of 6 are 1, 2, and 3, and \(1 + 2 + 3 = 6\)"""

def Add(nums):
    sum = 0
    for n in nums:
        sum = sum + n

    return sum
def checkIfPerfectNumber(num):
    nums = []
    for n in range(1, num):
        if num % n == 0:
            nums.append(n)

    return nums

def main():

    number = int(input("enter number: "))
    
    Ret = checkIfPerfectNumber(number)
    Sum = Add(Ret)
    print(Ret, Sum)

    if number == Sum:
        print("Number is Perfect NUmber")
    

if __name__ == "__main__":
    main()
