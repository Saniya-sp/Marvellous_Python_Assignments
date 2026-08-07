"""WAP that calculates factorial of multiple numbers simultaneously using multiprocessing.Pool
"""

from multiprocessing import Pool

# Function to calculate sum of squares from 1 to N
def count_of_odd(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
            # count += 1

    return factorial


def main():

    numbers = [10, 20, 30]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(count_of_odd, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Sum of even numbers from 1 to {n} = {result}")


if __name__ == "__main__":
    main()
    