# Recursion se ek list [1, 2, 3, 4, 5] ka sum nikaalo (loop use NA karo).
# Use recursion to find the sum of the list [1, 2, 3, 4, 5] (do NOT use a loop).

# Step 1 – Restate
"""
Take a list of numbers.
Do not use for or while loops.
Use recursion to calculate the total sum.
Return the final answer.
"""


# Step 2 – Example 
"""
sum([1,2,3,4,5])

1 + sum([2,3,4,5])    so on...
"""


# Step 3 – Pseudocode
"""
Create recursive function, Receive a list
If list is empty
Return 0
Otherwise
Return first element
Recursive call on remaining list
"""


# Step 4 – Translate

def list_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])    

print(list_sum([1, 2, 3, 4, 5]))




# Step 5 – Trace Table
"""
| Function Call         |First Number  | Remaining List | Returns |
| list_sum([1,2,3,4,5]) |            1 | [2,3,4,5]     |      15 |
| list_sum([2,3,4,5])   |            2 | [3,4,5]       |      14 |
| list_sum([3,4,5])     |            3 | [4,5]         |      12 |
| list_sum([4,5])       |            4 | [5]           |       9 |
| list_sum([5])         |            5 | []            |       5 |
| list_sum([])          |              |               |       0 |

"""


