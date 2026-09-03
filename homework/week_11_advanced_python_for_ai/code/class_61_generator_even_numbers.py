# Ek generator even_numbers(n) jo pehle n even numbers yield kare.
# 1. Create a generator even_numbers(n) that yields the first n even numbers.


def even_numbers(n):
    for i in range(0, n * 2, 2):
        yield i

print(list(even_numbers(5)))