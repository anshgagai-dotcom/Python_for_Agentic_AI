#1 Ek config dict banao, use MappingProxyType se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).
#  Create a config dictionary, lock it using MappingProxyType, read it, then try to modify it.

"""from types import MappingProxyType

config = {
    "theme": "dark"
}

locked = MappingProxyType(config)

print(locked["theme"])

# locked["theme"] = "light"""""




#2
"""from types import MappingProxyType

settings = {
    "language": "English"
}

locked = MappingProxyType(settings)

print(locked["language"])"""






#3
"""from types import MappingProxyType

database = {
    "host": "localhost",
    "port": 5432
}

locked = MappingProxyType(database)

print(locked["host"])
print(locked["port"])"""





#4
"""from types import MappingProxyType

student = {
    "name": "Ansh",
    "course": "Python"
}

locked = MappingProxyType(student)

print(locked["name"])

student["name"] = "Rahul"

print(locked["name"])"""





#5
"""from types import MappingProxyType

app = {
    "version": "1.0",
    "mode": "Production"
}

locked = MappingProxyType(app)

for key, value in locked.items():
    print(key, ":", value)"""

