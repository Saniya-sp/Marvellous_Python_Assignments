"""Design a Python Appl that creates two thresds named Prime and NonPrime.
Both threads should accept a list of integers
The Prime thread should display all prime numbers from the list.
The NonPrime thread should display all non-prime numbers from the list.
"""

import time
import threading

def Prime(numbers):
    print("TID of Small thread is :",threading.get_ident())
    prime_nums = []

    for n in numbers:
        
        if n == 2:
            prime_nums.append(n)
            continue

        is_divisible = 0

        for i in range(2,n+1):
            if n%i == 0:
                is_divisible = is_divisible + 1

        if is_divisible <= 1:
            prime_nums.append(n)

    print('primes = ',prime_nums)
    

def NonPrime(numbers):
    print("TID of Capital thread is :",threading.get_ident())

    nonprime_nums = []
    for n in numbers:
    
        is_divisible = 0
        for i in range(2, n+1 ):
            if n%i == 0:
                is_divisible += 1

        if is_divisible > 1:
            nonprime_nums.append(n)

    print('nonprime_nums = ',nonprime_nums)



def main():
    print("TID of Main thread is :",threading.get_ident())

    num = int(input("Enter number of elements: "))
    numbers = []
    for n in range(num):
        numbers.append(int(input(f"Enter {n} number: ")))

    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=Prime, args=(numbers,))
    tobj2 = threading.Thread(target=NonPrime, args=(numbers,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    

    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()