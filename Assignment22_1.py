"""WAP that accepts a list of integers and uses Pool.map() to calculate the sum
 of squares from 1 to N for every element in the list"""

from multiprocessing import Pool

# Function to calculate sum of squares from 1 to N
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def main():

    numbers = [100, 200, 300]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(sum_of_squares, numbers)

    # Display results
    for n, result in zip(numbers, results):
        print(f"Sum of squares from 1 to {n} = {result}")


if __name__ == "__main__":
    main()