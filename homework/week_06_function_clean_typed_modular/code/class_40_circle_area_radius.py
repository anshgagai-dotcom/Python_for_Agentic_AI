# math module use karke circle_area(radius) function tools.py mein add karo.
# Use the math module to add a circle_area(radius) function to tools.py.

# Step 1 – Restate
# Import the function and call it twice.



# Step 2 – Example First
"""
Radius = 7
Calculation = π * 7 ** 2
3.14 * 49 = 153.86
"""



# Step 3 – Pseudocode
"""
Import math
Create function
Accept radius
Calculate π * radius ** 2
Return area
"""



# Step 4 – Translate

import math

def circle_area(radius: float) -> float:
    """ Return the area of circle """
    return math.pi * radius ** 2

print(round(circle_area(7), (2)))
print(round(circle_area(5), (2)))
print(round(circle_area(10), (2)))


# Step 5 – Trace Table
"""
| Radius | Formula      | Return |
|      7 | 3.14 * 7**2  | 153.94 |
|      5 | 3.14 * 5**2  |  78.54 |
|     10 | 3.14 * 10**2 | 314.16 |
"""

