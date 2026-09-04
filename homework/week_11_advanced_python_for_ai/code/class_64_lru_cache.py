# @lru_cache ek fibonacci function par lagao aur speed mehsoos karo.
# Apply @lru_cache to a Fibonacci function and observe the performance improvement.


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))


