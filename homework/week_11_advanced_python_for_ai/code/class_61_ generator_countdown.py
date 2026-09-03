# Ek generator countdown(n) jo n se 1 tak yield kare.
# 2. Write a generator function countdown(n) that yields numbers from n down to 1.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(5)))
