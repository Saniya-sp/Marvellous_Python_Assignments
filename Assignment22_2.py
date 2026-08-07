"""WAP that calculates factorials of multiple numbers simultaneously using Pool.map() to calculate the sum
"""

from multiprocessing import Pool
import os

# Function to calculate sum of squares from 1 to N
def factorials(n):
    print("Process Id: ",os.getpid())

    total = 0
    facts = []
    for i in range(1, n + 1):
        if n%i == 0:
            facts.append(i)
        
    return facts

def main():
    print("Parent Process Id: ",os.getppid())

    numbers = [10,15,20,25]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(factorials, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Factorials of {n} = {result}")


if __name__ == "__main__":
    main()