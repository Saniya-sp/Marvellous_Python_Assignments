"""Write a program which accepts one number and prints its factors
ip = 12
op = 1,2,3,4,6,12"""

def FindFactorials(no):
    factorials = list()

    for num in range(1, no+1):
        if no % num == 0:
            factorials.append(num)
        # print(rev)
    return factorials


def main():

    num = int(input("enter number: "))
    Ret = FindFactorials(num)
    
    print("Factorials are :",Ret)
    

if __name__ == "__main__":
    main()
