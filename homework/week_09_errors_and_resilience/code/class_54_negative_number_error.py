# Ek custom exception NegativeNumberError banao aur ek function jo negative par use raise kare.
# Create a custom exception called NegativeNumberError and write a function that raises it when the number is negative.


class NegativeNumberError(Exception):
    pass


def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

    return n


try:
    print(check_number(-10))
except NegativeNumberError as e:
    print(e)  
