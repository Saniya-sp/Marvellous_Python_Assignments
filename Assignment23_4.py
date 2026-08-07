"""WAP that counts how many odd numbers exist between 1 to N using multiprocessing.Pool
"""

from multiprocessing import Pool

# Function to calculate sum of squares from 1 to N
def count_of_odd(n):
    count = 0

    for i in range(1, n + 1,2):
        count += 1

    return count


def main():

    numbers = [1000000, 2000000, 3000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(count_of_odd, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Sum of even numbers from 1 to {n} = {result}")


if __name__ == "__main__":
    main()
    