# Safe division: do numbers lo, divide karo, ZeroDivisionError handle karo.
# Safe division: Take two numbers, divide them, and handle ZeroDivisionError.



def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "You cannot divide by zero"

print(safe_divide(20, 4))    
print(safe_divide(15, 0))