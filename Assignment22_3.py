"""For every number in the given list, count how many prime numbers exist 
between 1 to N using multiprocessing pool
"""

from multiprocessing import Pool
import os

# Function to calculate sum of squares from 1 to N
def prime_numbers(n):
    print("Process Id: ",os.getpid())

    primes = []

    for i in range(2, n + 1):
        
        if i == 2:
           primes.append(i)
           continue

        is_divisible = 0

        for j in range(2, i):
            
            if i%j == 0:
                is_divisible += 1

        if is_divisible < 1:
            primes.append(i)
        
    return primes

def main():
    print("Parent Process Id: ",os.getppid())

    numbers = [10,15,20,25]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(prime_numbers, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Prime numbers are {n} = {len(result)}")


if __name__ == "__main__":
    main()