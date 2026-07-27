"""Task 16 — Two Class Comparison (sets)
Do sets banao: python_students aur java_students (kuch naam dono mein common ho). Print karo: (a) dono seekhne wale, (b) sirf Python, (c) total unique students, (d) sirf ek language seekhne wale.

Concepts: set operations &, -, |, symmetric difference ^
Hint: "sirf ek language" = python ^ java (symmetric difference)."""





python_students = {"Asha", "Rahul", "Priya", "Rohan"}
java_students = {"Rahul", "Rohan", "Neha", "Amit"}

print("Students learning both:")
print(python_students & java_students)

print("\nOnly Python Students:")
print(python_students - java_students)

print("\nTotal Unique Students:")
print(len(python_students | java_students))

print("\nStudents learning only one language:")
print(python_students ^ java_students)