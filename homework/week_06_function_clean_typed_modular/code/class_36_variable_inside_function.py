# Ek function ke andar variable banao, bahar print karke error dekho.
# Create a variable inside a function, then try printing it outside the function and observe the error.

# Step 1 – Restate
# Create a variable inside a function, Print it inside the function, Call the function, Then try to print the same variable outside the function ,Observe the error, The goal is to understand Local Scope.

# Step 2 – Example 
# Inside Function
# message = "Hello"
# ↓
# print(message)
# ↓
# Hello

# print(message)

# NameError



# Step 3 – Pseudocode
"""
Create a function
Inside the function
Create a variable
Print the variable
Call the function
Try printing the variable outside
Observe the NameError
"""


# Step 4 – Translate 
def create_message():
    message = "Hello Python"
    print(message)

create_message()
print(message)

# Output
# NameError: name 'message' is not defined

"""
A variable created inside a function is called a local variable.
It exists only while the function is running. Once the function finishes, 
the variable is destroyed and cannot be accessed outside the function.
"""


# Step 5 – Trace Table
"""
| Step | Python is Doing            | Memory                      |
| ---- | -------------------------- | --------------------------- |
| 1    | Function is created        | Nothing yet                 |
| 2    | Function is called         | Starts executing            |
| 3    |  message = "Hello Python"  | message is created          |
| 4    |  print(message)`           | Prints Hello Python         |
| 5    | Function finishes          | message is deleted          |
| 6    |  print(message)`           | Python searches for message |
| 7    | Variable not found         | NameError                   |

"""


