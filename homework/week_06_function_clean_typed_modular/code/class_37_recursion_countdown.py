# Recursion se 5 se 1 tak countdown karo.
# Use recursion to print a countdown from 5 to 1.

# Step 1 – Restate
"""
We need to write a recursive function that, Starts from 5.
Prints the current number, Calls itself with the next smaller number.
Stops when it reaches 0.
The goal is to understand how a function can call itself until a stopping condition is met.
"""

# Step 2 – Example 
"""
Start with, countdown(5) ,Print 5
Now call, countdown(4), Print 4
Now call, countdown(3), Print 3
Then countdown(2), Print 2
Then countdown(1, Print 1
Now call, countdown(0), reached 0
we stop.
"""


# Step 3 – Pseudocode
"""
Create countdown(number)
If number is 0
Stop
Print the current number
Call countdown(number - 1)
"""


# Step 4 – Translate
"""
def countdown(number):
    if number == 0:
        return
    print(number)
    countdown(number - 1)
countdown(5)
"""

def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)

countdown(7)         


# Step 5 – Trace Table
"""
|Function Call | Prints | Next Call    |
| countdown(5) | 5      | countdown(4) |
| countdown(4) | 4      |countdown(3)  |
| countdown(3) | 3      | countdown(2) |
| countdown(2) | 2      | countdown(1) |
| countdown(1) | 1      | countdown(0) |
| countdown(0) | Stops  | Returns      |
"""





"""
Every recursive function needs two parts
Base Case  tells the function when to stop.
Recursive Case  tells the function how to call itself again.
"""