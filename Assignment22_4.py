"""WAP that calculates 
1^5+2^5+.......+N^5 for multiple values of N simultaneously using Pool.
Measure total execution time.
"""

from multiprocessing import Pool
import os
import time

# Function to calculate sum of squares from 1 to N
def power_five(n):
    print("Process Id: ",os.getpid())

    sum = 0

    for i in range(1, n+1):

            sum = sum + i**5

    return sum

def main():
    print("Parent Process Id: ",os.getppid())

    start_time = time.perf_counter()

    numbers = [1000000,2000000,3000000,4000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(power_five, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Sum of power 5 are {n} = {(result)}")

    end_time = time.perf_counter()
    print("Execution time = ", (end_time-start_time))

if __name__ == "__main__":
    main()