"""Write a program which accept number from user and display below pattern
ip: 5 
op: 
12345
12345
12345
12345
12345
"""

def main():
    num = int(input("Enter number: "))

    for i in range(num):
        for j in range(1,num+1):
            print(j, end="")
        print()
        
if __name__ == "__main__":
    main()