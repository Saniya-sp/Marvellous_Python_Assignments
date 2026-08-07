"""Write a program which accept number from user and display below pattern
ip: 5 
op: 
*****
****
***
**
*
"""

def main():
    num = int(input("Enter number: "))

    for i in range(num,0,-1):
        print("*"*i)

        
if __name__ == "__main__":
    main()