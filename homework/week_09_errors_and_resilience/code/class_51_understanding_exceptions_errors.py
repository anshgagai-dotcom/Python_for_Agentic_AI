# Jaan-boojh kar 3 alag errors banao (ZeroDivisionError, ValueError, IndexError) aur traceback padho.
# Har error ke liye ek line likho: "Yeh error kab aata hai?"
# int(input(...)) mein letters daalo aur dekho kaunsa error aata hai.


# Intentionally create 3 different errors (ZeroDivisionError, ValueError, IndexError) and read the traceback.
# For each error, write one line: “When does this error occur?”
# Enter letters into int(input(...)) and observe which error occurs.




# 1. ZeroDivisionError
10 / 0
# ZeroDivisionError — This happens when we try to divide a number by 0.
# Example: You cannot divide 10 chocolates into 0 groups.


# 2. ValueError
int("hello")
# ValueError — This happens when Python cannot convert a value into the required type.
# Here, "hello" cannot be converted into an integer.


# 3. IndexError
numbers = [10, 20, 30]
numbers[5]
# IndexError — This happens when we try to access a position that does not exist in the list.
# This list only has indexes 0, 1, and 2.


# 3. Entering letters into int(input(...))
number = int(input("Enter a number: "))
# Input: abc
# ValueError — Python cannot convert "abc" into an integer number.


