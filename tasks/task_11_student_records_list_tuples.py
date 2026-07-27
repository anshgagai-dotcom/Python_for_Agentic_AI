"""Task 11 — Student Records (list of tuples)
Ek list of tuples banao: [("Asha", 85), ("Rahul", 92), ("Priya", 78)]. Har student ka naam aur marks unpacking se print karo. Phir sabse zyada marks waale ka naam batao.

Concepts: list of tuples, tuple unpacking in for, running max
Hint: for name, mark in students: — yeh unpacking hai."""





students = [
    ("Asha", 85),
    ("Rahul", 92),
    ("Priya", 78)
]

top_name = students[0][0]
top_marks = students[0][1]

print("Student Records\n")

for name, mark in students:
    print(f"{name} scored {mark} marks.")

    if mark > top_marks:
        top_marks = mark
        top_name = name

print("\nTop Student")
print(f"{top_name} scored the highest marks ({top_marks}).")
