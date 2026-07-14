#1
"""numbers = (1, 2, 3)

numbers[0] = 10"""

#TypeError: 'tuple' object does not support item assignment
# Tuples are immutable, so their values cannot be changed after creation.



#2
"""colors = ("Red", "Green", "Blue")

colors[1] = "Yellow" """
# TypeError: 'tuple' object does not support item assignment
#You cannot replace "Green" with "Yellow" because tuples are immutable.




#3
"""student = ("Rahul", 18)

student[0] = "Ansh"""

#TypeError: 'tuple' object does not support item assignment
# The first item of the tuple cannot be modified.




#4
"""languages = ("Python", "Java", "C++")

languages[2] = "JavaScript""""

# TypeError: 'tuple' object does not support item assignment
# Tuple elements are fixed after creation.


#5
"""marks = (80, 90, 95)

marks[1] = 100"""

# TypeError: 'tuple' object does not support item assignment
# The tuple cannot be updated because it is immutable.




#6
"""car = ("BMW", "Black")

car[0] = "Audi"""

# TypeError: 'tuple' object does not support item assignment
# Once a tuple is created, its items cannot be changed.
