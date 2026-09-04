# @timer ko ek function par lagao jo loop chalata hai.
# Apply @timer to a function that runs a loop.


import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")

        return result

    return wrapper

@timer
def calculate():
    total = 0

    for number in range(1, 100001):
        total += number

    return total

print(calculate())


