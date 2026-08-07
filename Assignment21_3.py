"""Design a Python Appl where multiple threads update a shared variable
Use a Lock to avoid race conditions
Each thread should increment the shared counter multiple times
Display the final value of the counter after all threads complete execution.

"""

import time
import threading


# Shared variable
counter = 0

# Lock object
lock = threading.Lock()

def increment_counter(times):
    global counter

    for _ in range(times):
        # Acquire lock before modifying shared variable
        with lock:
            counter += 1


def main():

    start_ime = time.perf_counter()
    
    # Number of threads
    num_threads = 5

    # Each thread increments the counter 100000 times
    increments_per_thread = 100000

    threads = []

    # Create and start threads
    for i in range(num_threads):
        t = threading.Thread(target=increment_counter, args=(increments_per_thread,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Expected Counter Value :", num_threads * increments_per_thread)
    print("Actual Counter Value   :", counter)

    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()