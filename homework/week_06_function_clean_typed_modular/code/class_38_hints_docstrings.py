# Apne my_tools.py (Week 5) ke 3 functions mein type hints + Google-style docstrings add karo.
# Add type hints and Google-style docstrings to any 3 functions in your my_tools.py file (from Week 5).

# Type Hint = tells other programmers what kind of value is expected.
# Docstring = explains what the function does.


# Step 1 – Restate
"""
Accepts a radius.
Uses a type hint to indicate the input should be a float.
Returns the area of a circle.
Uses a
"""

# Step 2 – Example 
"""
radius = 5
Formula Area 3.14 * 5 * 5
3.14 * 25
 = 78.5
"""



# Step 3 – Pseudocode
"""
Create function area_circle
Accept radius
Add a type hint for radius
Add a return type hint
Write a docstring explaining the function
Calculate
3.14 * radius * radius
Return the area
Call the function
Print the result
"""





# Step 4 – Translate

def area_circle(radius: float) -> float:

    """
    Calculate and return the area of a circle
    """
    return 3.14 * radius ** 2

print(area_circle(5))    



# Step 5 – Trace Table
"""
| Step | radius | Calculation   | Return |
|    1 |      5 | 3.14 * 5**2   |   78.5 |
"""

