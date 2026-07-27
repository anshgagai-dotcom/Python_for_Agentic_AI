"""Task 9 — Marks List Analyzer
Ek list marks = [45, 78, 92, 33, 88, 20, 67] lo. Bina max()/min() use kiye (loop se khud nikaalo) print karo: highest, lowest. Phir sum()/len() se average. Aur batao kitne students pass hue (>= 33).

Concepts: for loop, comparison, running max/min, counter
Hint: highest = marks[0] se shuru karo, phir loop mein if m > highest: highest = m."""




marks = [45, 78, 92, 33, 88, 20, 67]

highest = marks[0]
lowest = marks[0]
pass_count = 0

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    if m >= 33:
        pass_count += 1

average = sum(marks) / len(marks)

print("===== RESULT =====")
print(f"Highest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")
print(f"Average Marks : {average:.2f}")
print(f"Passed Students : {pass_count}")