# make_counter() banao jo har call par badhta number de (closure se).
# Create a make_counter() function that returns an increasing number on every call (using a closure).

# Step 1 – Restate
"""
We need to create a function called make_counter()
Inside this function, Start a variable called count with value 0.
Create another function inside it.
Every time the inner function is called, Increase count by 1.
Return the updated value.
Return the inner function.
function should remember the previous count.
"""


# Step 2 – Example 
"""
my_counter = make_counter(), initially count = 0
First Call
my_counter(), Python does, mcount = count + 1
1
Returns 1
Second Call, my_counter(), Python remembers, count = 1
Then count = 2, Returns2
"""


# Step 3 – Pseudocode
"""
Create outer function
Create count variable
Set count = 0
Create inner function
Tell Python we want to use the outer count, Increase count by 1
Return count
Return the inner function
Store the returned function, Call it multiple times, count increases
"""


# Step 4 – Translate
"""
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()

print(my_counter())
print(my_counter())
"""


def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = make_counter()

print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
print(my_counter())
       


"""
A closure remembers variables from its outer function. 
If the inner function needs to change one of those variables,
 use the nonlocal keyword.
"""
