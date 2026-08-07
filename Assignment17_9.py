"""Write a program which accepts number from user and return number of digits in that number
ip; 5187934 op: 7"""

# def LenOfNUmber(num):


def main():
    num = int(input("Enter number: "))
    # LenOfNUmber(num)
    print(len(str(num)))

if __name__ == "__main__":
    main()