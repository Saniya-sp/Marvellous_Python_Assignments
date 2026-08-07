"""Design a Python Appl that creates two threads
Thread 1 should compute the sum of elements from a list.
Thread 2 should compute the product of elements from a list.
return results to main thread and display them
"""

import time
import threading
from functools import reduce

class SumThread(threading.Thread):
    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers
        self.sum = 0

    def run(self):
        
        for no in self.numbers:
            self.sum = self.sum + no
        
        print('sum = ',self.sum)


class ProductThread(threading.Thread):

    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers
        self.prod = 1


    def run(self):
        for no in self.numbers:
            self.prod = self.prod * no
        
    
        print('prod = ',self.prod)
    


def main():

    start_ime = time.perf_counter()
    
    num = int(input("Enter number of elements: "))
    numbers = []

    for n in range(num):
        numbers.append(int(input(f"Enter {n} number: ")))

    start_ime = time.perf_counter()
    
    tobj1 = SumThread(numbers)
    tobj2 = ProductThread(numbers)
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()

    print('sum === ',tobj1.sum)
    print('prod === ',tobj2.prod)
    
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()