"""Design a Python Appl that creates two sepearate thresds named EvenList and OddList.
Both threads should accept list of integers as a input.
The EvenList thread should:
    Extract all even elements from list
    Calculate and display the sum
The OddList thread should:
    Extract all odd elements from list
    Calculate and display the sum

Thread should run concurrently
"""

import time
import threading

def EvenList(numbers):
    even = []
    for n in numbers:
        if n%2 == 0:
            even.append(n)
    
    print('Even = ',even)
    sum = 0
    for n in even:
        sum = sum + n

    print(f"Even sum:{sum}")

    
def OddList(numbers):
    odd = []

    for n in numbers:
        if n%2 != 0:
            odd.append(n)

    print('Odd = ',odd)
    
    sum = 0
    for n in odd:
        sum = sum + n

    print(f"Odd sum:{sum}")
    
def main():
    num = int(input("Enter number of elements: "))
    numbers = []
    for n in range(num):
        numbers.append(int(input(f"Enter {n} number: ")))

    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=EvenList, args=(numbers,))
    tobj2 = threading.Thread(target=OddList, args=(numbers,))
    
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
    
    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()