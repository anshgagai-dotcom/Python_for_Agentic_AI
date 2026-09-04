# Make a @count_calls decorator that counts how many times a function has been called.
# Ek @count_calls decorator jo gine function kitni baar call hua.


import functools

def count_calls(func):
    calls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"{func.__name__} called {calls} time(s)")
        return func(*args, **kwargs)

    return wrapper

@count_calls
def hello():
    return "Hello"

hello()
hello()
hello()

