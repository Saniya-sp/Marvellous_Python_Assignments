"""Write a program which accepts one number and checks whether it is divisible by 3 and 5"""

def IsDivisible(No):
    if (No % 3 == 0) and (No % 5 == 0):
        print("Number is divisible by 3 and 5.")
    else:
        print("Number is not divisible by 3 and 5.")

no = int(input("Enter number: "))
IsDivisible(no)

