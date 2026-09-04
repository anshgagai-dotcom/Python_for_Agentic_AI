# Ek @uppercase decorator banao jo function ke string-result ko uppercase kare.
# Make an @uppercase decorator that converts a function's string result to uppercase.


import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return str(value).upper()
    return wrapper

@uppercase
def welcome(name):
    return f"welcome {name}"

print(welcome("Ansh G"))

