# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()     # start Stopwatch
        result = func(*args, **kwargs)
        end = time.time()       # stop stopwatch
        execution_time = end - start
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(2)
    print("Done sleeping")

slow_function()