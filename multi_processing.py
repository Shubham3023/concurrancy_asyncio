# This code demonstrates the use of multiprocessing in Python to execute a 
# function that simulates sleeping for a specified number of seconds. 
# The `ProcessPoolExecutor` from the `concurrent.futures` module is used to manage a 
# pool of processes, allowing for concurrent execution of the function. The total time taken 
# to execute the function is measured and printed at the end.

# import time
# import concurrent.futures

# def sleep_for_a_sec(seconds):
#     print(f"Sleeping for {seconds} seconds...")
#     time.sleep(seconds)
#     return f"Slept for {seconds} seconds"

# if __name__ == "__main__":
#     start = time.perf_counter()
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(sleep_for_a_sec, 1)
#          f2 = executor.submit(sleep_for_a_sec, 1)

        
#         print(f1.result())
#         print(f2.result())

#     finish = time.perf_counter()
#     print(f"Finished in {round(finish-start, 2)} seconds")


import time
import concurrent.futures

def sleep_for_a_sec(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:

        result = [executor.submit(sleep_for_a_sec, 1) for _ in range(15)]

        for f in concurrent.futures.as_completed(result):
            print(f.result())

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} seconds")