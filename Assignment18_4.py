"""write a program which accept N numbers from user and store it into List. 
Accept one another number from user and return frequency of that number from List.
ip: Number of elements : 11
input elements: 13 5 45 7 4 56 5 34 2 5 65
element to search : 5
op: 3
"""

def Frequency(numbers_list, no):
    count = 0
    for x in numbers_list:
        if x == no:
            count = count + 1

    return count        


def main():
    n = int(input("Number of elements (N): "))
    
    numbers_list = []
    
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers_list.append(num)

    no = int(input("Element to search: "))
    
    Ret = Frequency(numbers_list, no)
    print(Ret)


if __name__ == "__main__":
    main()


