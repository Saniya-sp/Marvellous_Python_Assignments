"""Write a program which accepts one number and prints sum digits
 IP=123
 op=6"""

def SumOfDigits(no):
    count = 0
    for i in (str(no)):
        count += int(i)
        # print(count)
    return count


def main():

    num = int(input("enter number: "))
    Ret = SumOfDigits(num)
    print("SumOfDigits is : ",Ret)


if __name__ == "__main__":
    main()