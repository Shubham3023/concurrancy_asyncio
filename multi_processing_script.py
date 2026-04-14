# multiprocessing helps when we have to do a lot of work and we want to do it in parallel.
# it allows us to create multiple processes that can run concurrently, which can speed up our program.
# we can use the multiprocessing module in Python to create and manage multiple processes.
# we can use the Process class from the multiprocessing module to create a new process.
# we can also use the Pool class from the multiprocessing module to create a pool of worker processes that can execute tasks in parallel.   
# Multi processing works for CPi-bound tasks, which are tasks that require a lot of CPU time.
# Multi threading works for IO-bound tasks, which are tasks that require a lot of input/output operations, such as reading and writing files, or making network requests.

import time 
import multiprocessing

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')

if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start() # starts the process p1, which runs the do_something function in a separate process.
    p2.start()

    # waits for the process p1 to finish before moving on to the next line of code. 
    # This is important because we want to make sure that the process has finished before we try to access any of its 
    # resources or data.
    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish - start, 2)} seconds")