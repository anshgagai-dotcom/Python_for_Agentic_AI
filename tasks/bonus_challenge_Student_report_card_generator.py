"""Bonus Challenge (sab kuch mila kar)
Student Report Card Generator — Ek list of dicts banao jisme har student ka name aur teen subjects ke marks (ek list) ho. Har student ke liye: total, average, aur grade (A/B/C/D) nikaalo. Sabse aakhir mein class topper aur class average batao. Original data safe rakhne ke liye kaam karne se pehle copy.deepcopy() use karo.

Concepts: list of dicts, nested list, loops, sum()/len(), if/elif/else, sorted(key=...), copy.deepcopy
Yeh capstone hai — agar aap yeh khud bina notes ke bana lete ho, toh aapne Week 1-4 sach mein master kar liya."""






import copy

students = [
    {"name": "Asha", "marks": [80, 90, 70]},
    {"name": "Rahul", "marks": [95, 85, 90]},
    {"name": "Priya", "marks": [60, 75, 70]},
    {"name": "Amit", "marks": [40, 50, 45]}
]

report = copy.deepcopy(students)

for student in report:

    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    student["total"] = total
    student["average"] = average
    student["grade"] = grade

print("===== STUDENT REPORT CARDS =====\n")
for student in report:
    print(f"Name    : {student['name']}")
    print(f"Marks   : {student['marks']}")
    print(f"Total   : {student['total']}")
    print(f"Average : {student['average']:.2f}")
    print(f"Grade   : {student['grade']}")
    print("-" * 30)

topper = sorted(
    report,
    key=lambda s: s["average"],
    reverse=True
)[0]

class_total = 0
for student in report:
    class_total += student["average"]

class_average = class_total / len(report)

print("\n===== CLASS SUMMARY =====")
print(f"Topper       : {topper['name']} ({topper['average']:.2f})")
print(f"Class Average: {class_average:.2f}")