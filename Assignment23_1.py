"""WAP using multiprocessing.Pool to calculate the sum
 of all even numbers from 1 to N for every number from the given list"""

from multiprocessing import Pool

# Function to calculate sum of squares from 1 to N
def sum_of_even(n):
    sum = 0

    for i in range(2, n + 1,2):
        sum += i

    return sum


def main():

    numbers = [1000000, 2000000, 3000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(sum_of_even, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Sum of even numbers from 1 to {n} = {result}")


if __name__ == "__main__":
    main()
    