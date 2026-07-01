"""Write a program which accepts one number and prints count of digits in that
 number
 IP=7521
 op=4"""

def reverseNumber(no):
    count = 0
    for i in range(len(str(no))):
        count += 1
        # print(count)
    return count


def main():

    num = int(input("enter number: "))
    Ret = reverseNumber(num)
    print("Count is : ",Ret)


if __name__ == "__main__":
    main()