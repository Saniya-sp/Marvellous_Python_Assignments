"""Write a program which accepts one number and prints reverse of number.
ip = 123
op = 321"""



def ReverseNumber(no):
    rev = ''

    for ch in str(no):
        rev = ch + rev
        # print(rev)
    return rev


def main():

    num = int(input("enter number: "))
    Ret = ReverseNumber(num)
    print("Reversed Number is : ",Ret)


if __name__ == "__main__":
    main()