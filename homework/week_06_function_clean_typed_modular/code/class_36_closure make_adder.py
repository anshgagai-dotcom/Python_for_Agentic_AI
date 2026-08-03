# make_adder(n) closure banao jo n add kare; add5 = make_adder(5) test karo.
# Create a closure make_adder(n) that adds n to another number; test it using add5 = make_adder(5).


# Step 1 – Restate
"""
We need to create a function called make_adder(), This function should, Accept one number (n),
Create another function inside it, The inner function should take another number, Add both numbers together.
Return the inner function.
The important part is,The inner function should remember the value of n even after the outer function has finished.
This "remembering" is called a Closure.
"""


# Step 2 – Example First
"""
Suppose we create, make_adder(5) Python stores Remember n = 5, Now we use it
add5(10) Python remembers
n = 5, number = 10
Answer 15
"""


# Step 3 – Pseudocode
"""
Create outer function, Receive n
Create inner function, Receive another number
Return
number + n
Return inner function, Store returned function
Call it with different numbers
"""


# Step 4 – Translate

def make_adder(n):
    def add(number):
        return number + n
    return add

add5 = make_adder(5)

print(add5(20))



"""
def make_adder(n):
    def add(number):
        return number + n
    return add

add5 = make_adder(5)

print(add5(10))
"""



# Step 5 – Trace Table

"""
| Step | Logic                             | Value                |
| ---- | --------------------------------- | -------------------- |
| 1    | make_adder(5)                     |    n = 5             |
| 2    | Inner function add()              | Remembers   n = 5    |
| 3    | return add                        | Function    returned |
| 4    |  add5 = returned function         |  add5` remembers  5  |
| 5    |  add5(10)                         |  10 + 5 = 15         |
"""




"""
A closure is a function inside another function that remembers the variables of its outer function,
even after the outer function has finished executing.
"""