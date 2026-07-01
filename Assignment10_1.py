"""Write a program which accepts one number and prints multiplication table of that number."""

def TableOfNumber(no):
    table = []
    for i in range(1,11):
        table.append(i * no)

    return table

num = int(input("enter number: "))
ret = TableOfNumber(num)

print("Table of number is: ", ret)

