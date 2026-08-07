"""Design a Python Appl that creates two sepearate thresds named EvenFactor and OddFactor.
Both threads should accept one integer number as a parameter.
The EvenFactor thread should:
    Identify all even factors of the given number
    Calculate and display the sum of even factors
The OddFactor thread should:
    Identify all odd factors of the given number
    Calculate and display the sum of odd factors

After both threads complete execution, the main thread should display the message:
'Exit from main'
"""

import time
import threading

def EvenFactor(no):
    factors = []
    for n in range(2,no+1,2):
        if no%n == 0:
            factors.append(n)
    
    print('EvenFactor = ',factors)
    sum = 0
    for n in factors:
        sum = sum + n

    print(f"Even factors sum:{sum}")

    
def OddFactor(no):
    factors = []

    for n in range(1,no+1,2):
        if no%n == 0:
            factors.append(n)

    print('OddFactor = ',factors)
    
    sum = 0
    for n in factors:
        sum = sum + n

    print(f"Odd factors sum:{sum}")
    
def main():
    num = int(input("Enter number: "))
    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=EvenFactor, args=(num,))
    tobj2 = threading.Thread(target=OddFactor, args=(num,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    
    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()