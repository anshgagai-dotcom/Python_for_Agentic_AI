# Call a function using keyword arguments by changing the order of the arguments.
# Ek function ko keyword arguments se call karke dikhao (order badal kar).


#1
def intro(name, age, city="India"):
    return f"{name} is {age} years old and lives in {city}."

print(intro(city="Chennai", age=26, name="Arjun"))

