# int(input) mein ek try with ValueError aur ek general Exception fallback.
# Use int(input(...)) with one try block, handle ValueError, and add a general Exception fallback.

try:
    number = int(input("Enter a number: "))
    print(f"Number entered: {number}")

except ValueError:
    print("Invalid input. Please enter a whole number.")

except Exception:
    print("Something unexpected went wrong.")