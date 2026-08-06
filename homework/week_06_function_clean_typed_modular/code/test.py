"""
factorial function should do factorial 
for only positive value not negative if user pass negative value then return "accept only positive value"
"""




"""
Factorial function should calculate the factorial
only for non-negative integers.

If the user passes:
- A negative value, return "accept only positive value".
- A non-integer value, return "accept only integer value."
"""


def factorial(num: int) -> int | str:
    """
    Calculates the factorial of a non-negative integer.

    Args:
        num (int): The number whose factorial is to be calculated.

    Returns:
        int: The factorial of the number.
        str: Error message if the input is invalid.
    """

    if not isinstance(num, int):    # Check if input is an integer
        return "accept only integer value."

    elif num < 0:    # Check if input is negative
        return "accept only positive value"

    elif num == 0 or num == 1:     # Base case
        return 1

    return num * factorial(num - 1)    # Recursive case

print("\n" + "*" * 55)
print("*" * 55)

print(factorial(0))
print("\n" + "*" * 55)

print(factorial(5))
print("\n" + "*" * 55)

print(factorial(6))
print("\n" + "*" * 55)

print(factorial(-5))
print("\n" + "*" * 55)

print(factorial("5"))
print("\n" + "*" * 55)
print("*" * 55)
































"""
def factorial(n: ): 
   if n < 0:
       return "accept only positive value"

       
       if user pass negative value then return accept only positive value
       

   elif n == 1:
      return 1
   return n * factorial(n-1)
print(factorial(6))


"""