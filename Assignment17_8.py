"""Write a program which accept number from user and display below pattern
ip: 5 
op: 
1
12
123
1234
12345
"""

def main():
    num = int(input("Enter number: "))

    for i in range(1,num+1):
        for i in range(1,i+1):
        
            print(i, end="")
        print()
        
if __name__ == "__main__":
    main()