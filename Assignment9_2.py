"""Write a program which contains one function ChkGreater() 
that accepts two numbers
and prints the greater number."""

def ChkGreater(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

Ret = ChkGreater(10, 20)
print("Greater number is: ", Ret)
