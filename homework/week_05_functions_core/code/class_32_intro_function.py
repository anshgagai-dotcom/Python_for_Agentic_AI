# intro(name, age, city="India") banao; ek baar city ke saath, ek baar bina, call karo.
# Write a function intro once without city, once with city


#1
"""def intro(name, age, city="India"):
    return f"My name is {name}. I am {age} years old. I live in {city}."

print(intro("Rohan", 20))"""



#2
def intro(name, age, city="India"):
    return f"My name is {name}. I am {age} years old. I live in {city}."

print(intro("Neha", 22, "Mumbai"))

