"""Write a program which accepts one number and checks whether it is palindrome 
or not
ip = 121
op = Palindrome"""

def CheckPalindrome(no):
    rev = ''

    for ch in str(no):
        rev = ch + rev
        # print(rev)
    return rev


def main():

    num = int(input("enter number: "))
    Ret = CheckPalindrome(num)
    if num == int(Ret):
        print("Number is Palindrome")
    else:
        print("Number is NOT Palindrome")


if __name__ == "__main__":
    main()
