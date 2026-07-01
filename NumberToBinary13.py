"""Write a program which accepts one number and prints binary equivalent.

To convert a decimal number to binary, repeatedly divide it by 2 and record the remainders. Reading these remainders in reverse gives the binary representation.
"""

def numberToBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        print('bit = ',bit)
        binArr.append(str(bit))
        n //= 2
        print('n = ',n)

    print('binArr = ',binArr)
    binArr.reverse()
    print('reverse binArr = ',binArr)

    return "".join(binArr)


def main():

    number = int(input("enter number: "))
    
    Ret = numberToBinary(number)
    
    print("Ret",Ret)
    
    
if __name__ == "__main__":
    main()

