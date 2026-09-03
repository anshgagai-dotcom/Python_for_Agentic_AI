"""
Ek dict banao aur use json.dumps(indent=2) se sundar print karo.
Ek JSON string '{"city": "Mumbai", "pin": 400001}' ko dict mein load karke city print karo.
Apni Week 4 ki contact book (list of dicts) ko JSON file mein save aur reload karo.
"""

"""
1. Create a dictionary and print it in a nicely formatted way using json.dumps(indent=2).

2. Load the JSON string '{"city": "Mumbai", "pin": 400001}' into a dictionary and print the city.

3. Save your Week 4 contact book (a list of dictionaries) into a JSON file and then reload it.
"""





import json

# ==================================================
# Question 1
# Create a dictionary and print it using json.dumps(indent=2)
# ==================================================

data = {
    "name": "Priya",
    "hobbies": ["reading", "coding"]
}

print("Question 1:")
print(json.dumps(data, indent=2))


# ==================================================
# Question 2
# Convert a JSON string into a dictionary and print city
# ==================================================

s = '{"city": "Mumbai", "pin": 400001}'

d = json.loads(s)

print("\nQuestion 2:")
print(d["city"])


# ==================================================
# Question 3
# Save and reload the contact book as a JSON file
# ==================================================

contacts = [
    {"name": "Asha", "phone": "98765"},
    {"name": "Rahul", "phone": "91234"}
]

with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=2)

with open("contacts.json", "r", encoding="utf-8") as f:
    print("\nQuestion 3:")
    print(json.load(f))


