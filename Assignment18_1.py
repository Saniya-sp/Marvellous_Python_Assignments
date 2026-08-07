"""write a program which accept N numbers from user and store it into List. 
Return addition of all elements from that List
ip: Number of elements : 6
input elements: 13 5 45 7 4 56
op: 130
"""


def Add(numbers_list):
    sum = 0
    for no in numbers_list:
        sum = sum + no

    return sum


def main():
    n = int(input("Number of elements (N): "))
    
    numbers_list = []
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(num)
    
    Ret = Add(numbers_list)
    print(Ret)


if __name__ == "__main__":
    main()


