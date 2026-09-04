# Create a TypedDict called User with name: str and age: int.
# Ek TypedDict User banao (name: str, age: int).


from typing import TypedDict

class User(TypedDict):
    name: str
    age: int


user_data: User = {
    "name": "Ansh",
    "age": 26
}

print(user_data)
print(user_data["name"])
print(user_data["age"])

