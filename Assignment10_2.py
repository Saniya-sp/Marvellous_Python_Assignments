"""Write a program which accepts one number and prints sum of first N natural numbers"""

def Summation(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    return sum

num = int(input("enter number:"))
ret = Summation(num)
print("Summation is: ",ret)
    
