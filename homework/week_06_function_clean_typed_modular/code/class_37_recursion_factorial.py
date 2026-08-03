# Recursion se factorial(6) nikaalo.
# Use recursion to calculate factorial(6).

# Step 1 – Restate
"""
We need to write a recursive function that calculates the factorial of a number.
The function should, Take one number as input.
Multiply it by the factorial of the previous number.
Keep doing this until it reaches 1, Return the final answer.
"""


# Step 2 – Example 
"""
factorial(6),  6 * factorial(5)
Now it needs, factorial(5),   5 * factorial(4)
Then 4 * factorial(3), Then 3 * factorial(2), Then 2 * factorial(1)
Finally factorial(1)
"""

# Step 3 – Pseudocode
"""
Create factorial(number)
If number is 1
Return 1
Otherwise
Return number * factorial(number - 1)
Call factorial(6)
Print the answer
"""


# Step 4 – Translate
"""
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)
print(factorial(6))
"""



def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))



# Step 5 – Trace Table
"""
| Function Call  | factorial        | Returns |
| factorial(6)   | 6 * factorial(5) | 720     |
| factorial(5)   | 5 * factorial(4) | 120     |
| factorial(4)   | 4 * factorial(3) | 24      |
| factorial(3)   | 3 * factorial(2) | 6       |
| factorial(2)   | 2 * factorial(1) | 2       |
| factorial(1)   |                  | 1       |
"""




"""
A recursive factorial function breaks a big multiplication problem into smaller 
factorial problems, It keeps calling itself until it reaches the base case (1), 
then returns back while multiplying each result together.
"""

