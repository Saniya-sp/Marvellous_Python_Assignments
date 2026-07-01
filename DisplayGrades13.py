"""Write a program which accepts marks and displays grade
Condition Example:
>= 75 -> Distinction
>= 60 -> First Class
>= 50 -> Second Class
< 50 -> Fail
"""

def checkGrade(n):
    
    if n >= 75:
        return "Dsitinction"
    elif n >= 60:
        return "First Class"
    elif n >= 50:
        return "Second Class"
    elif n < 50:
        return "Fail"
    

def main():

    number = int(input("enter number: "))
    
    Ret = checkGrade(number)
    
    print(Ret)

if __name__ == "__main__":
    main()
