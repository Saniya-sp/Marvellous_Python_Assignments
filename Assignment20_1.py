"""Design a Python Appl that creates two sepearate thresds Even and Odd.
The Even thread should display the first 10 even numbers
The Odd thread should display the first 10 odd numbers
Both threads should execute independently using the threading module.
Ensure proper thread creation and execution
"""

import time
import threading

def Even(no):

    for n in range(2,no,2):
        print(n)


def Odd(no):
    for n in range(1,no,2):
        print(n)
            

def main():
    
    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=Even, args=(21,))
    tobj2 = threading.Thread(target=Odd, args=(20,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()