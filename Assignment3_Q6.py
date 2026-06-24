"""Write a program to display
        Data Type
        Memory address
        Size in byte 
    of variable entered by user
"""
from sys import getsizeof

print("Enter integer number : ")
x = int(input())

print(type(x))
print(id(x))
print(getsizeof(x))

print("Enter decimal number : ")
x = float(input())

print(type(x))
print(id(x))
print(getsizeof(x))

print("Enter any string : ")
x = str(input())

print(type(x))
print(id(x))
print(getsizeof(x))