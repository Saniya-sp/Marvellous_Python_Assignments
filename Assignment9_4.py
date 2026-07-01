"""Write a program which accepts one number and prints cube of that number."""

def Cube(No1):
    return No1 * No1 *No1

no1 = int(input("Enter number: "))
Ret = Cube(no1)
print("Cube is: ",Ret)
