"""Task 18 — Contact Book with Search (nested dict)
Ek dictionary of dicts banao:

contacts = {
    "Asha":  {"phone": "98765", "city": "Mumbai"},
    "Rahul": {"phone": "91234", "city": "Delhi"},
}
User se ek naam maango. .get() se safely dhoondho — mile toh phone + city print karo, na mile toh "Contact not found".

Concepts: nested dict, .get(), input(), if/else
Hint: contacts.get(name) pehle — agar None mila toh not found, warna andar ke fields access karo."""




contacts = {
    "Asha": {
        "phone": "98765",
        "city": "Mumbai"
    },

    "Rahul": {
        "phone": "91234",
        "city": "Delhi"
    }
}

name = input("Enter name: ")
contact = contacts.get(name)

if contact:
    print("\nContact Found")
    print(f"Phone : {contact['phone']}")
    print(f"City  : {contact['city']}")
else:
    print("\nContact not found")