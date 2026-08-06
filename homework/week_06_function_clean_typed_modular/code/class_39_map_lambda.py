# map + lambda se [1,2,3,4] ke har number ka cube banao.
# Use map() and lambda to create the cube of every number in [1, 2, 3, 4].


# Step 1 – Restate
"""
Take every number from the list.
Find its cube (x³), Use map(), Use lambda.
"""



# Step 2 – Example 
"""
Input [1,2,3,4]

1³ = 1, 2³ = 8, 3³ = 27, 4³ = 64

Output [1,8,27,64]
"""



# Step 3 – Pseudocode
"""
Take the list
Use map()
Use lambda, Cube every number, Convert map to list
Print the result
"""


# Step 4 – Translate

numbers = [1, 2, 3, 4]

cube = list(map(lambda x: x ** 3, numbers))

print(cube)


# Step 5 – Trace Table
"""
| Number | Cube |
|      1 |    1 |
|      2 |    8 |
|      3 |   27 |
|      4 |   64 |
"""

