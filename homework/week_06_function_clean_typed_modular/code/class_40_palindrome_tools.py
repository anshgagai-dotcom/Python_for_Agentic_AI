# tools.py mein is_palindrome(text: str) -> bool function add karo (type hints + docstring ke saath).
# Add an is_palindrome(text: str) -> bool function to tools.py with type hints and a docstring.


# Step 1 – Restate
# Create a function that checks whether a word reads the same forwards and backwards.


# Step 2 – Example 
# madam - Reverse - madam - True


# Step 3 – Pseudocode
"""
Create function, Accept text, Reverse text
Compare original and reversed
Return True or False
"""


# Step 4 – Translate

def is_palindrome(text: str) -> bool:
    """ Check if a word is Palindrome. """
    return text == text[::-1]

print(is_palindrome("python"))
print(is_palindrome("level"))    
