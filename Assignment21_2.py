"""Design a Python Appl that creates two thresds.
Thread 1 should calculate and display maximum element from an list.
Thread 2 should calculate and display minimum element from the same list.
List should be accepted from user.
"""

import time
import threading
from functools import reduce


def Thread1(numbers):
    
    max_element = lambda x, y: x if x > y else y
    
    maximum = reduce(max_element, numbers)
    print('maximum = ',maximum)
    

def Thread2(numbers):
    
    min_element = lambda x, y: x if x < y else y
    
    minimum = reduce(min_element, numbers)
    print('minimum = ',minimum)
    

def main():
    
    num = int(input("Enter number of elements: "))
    numbers = []
    for n in range(num):
        numbers.append(int(input(f"Enter {n} number: ")))

    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=Thread1, args=(numbers,))
    tobj2 = threading.Thread(target=Thread2, args=(numbers,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    

    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()