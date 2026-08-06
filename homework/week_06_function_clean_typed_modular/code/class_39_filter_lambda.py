#filter + lambda se [3,8,1,9,4] mein se sirf 5 se bade numbers rakho.
#Use filter() and lambda to keep only the numbers greater than 5 from [3, 8, 1, 9, 4].


# Step 1 – Restate
"""
Check every number.
Keep only numbers greater than 5.
Use filter()
"""



# Step 2 – Example 
"""
Input [3,8,1,9,4]
Checking
3 > 5 no
8 > 5 yes
1 > 5 no
9 > 5 yes
4 > 5 no
Output [8,9]
"""



# Step 3 – Pseudocode
"""
Create list
Use filter()
Keep numbers greater than 5
Convert to list
Print
"""



# Step 4 – Translate

numbers = [3, 8, 1, 9, 4]

result = list(filter(lambda x: x > 5, numbers))

print(result)



# Step 5 – Trace Table
"""
| Number |  > 5  | 
|      3 | False |       
|      8 |  True |   
|      1 | False |   
|      9 |  True |   
|      4 | False |
print(result)
result = [8, 9]
"""

