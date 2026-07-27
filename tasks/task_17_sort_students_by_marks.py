"""Task 17 — Sort Students by Marks (list of dicts)
Ek list of dicts banao: [{"name": "Asha", "marks": 85}, ...] (kam se kam 4 students). Unhe marks ke descending order mein sort karke print karo (rank ke saath). Original list ko mat badlo.

Concepts: sorted(key=lambda ...), reverse=True, enumerate, nested access
Hint: sorted(students, key=lambda s: s["marks"], reverse=True). Rank ke liye enumerate(..., start=1)."""





students = [
    {"name": "Asha", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78},
    {"name": "Neha", "marks": 88}
]

sorted_students = sorted(
    students,
    key=lambda s: s["marks"],
    reverse=True
)

print("===== Student Ranking =====")

for rank, student in enumerate(sorted_students, start=1):
    print(f"{rank}. {student['name']} - {student['marks']} marks")