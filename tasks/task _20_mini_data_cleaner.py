"""Task 20 — Mini Data Cleaner (comprehensions — capstone)
Ek messy list of raw user inputs lo:

raw = ["  Asha ", "RAHUL", "", "  priya  ", "Amit", "rahul  "]
Ek hi line ke comprehension se: har naam ko strip + lower karo aur khaali strings hatao. Phir us cleaned list se unique naam (set) nikaalo aur alphabetical order mein sorted print karo.

Concepts: list comprehension + if filter, .strip(), .lower(), set(), sorted()
Hint: [n.strip().lower() for n in raw if n.strip()] — filter if n.strip() khaali strings ko hata deta hai."""





raw = [
    "  Asha ",
    "RAHUL",
    "",
    "  priya  ",
    "Amit",
    "rahul  "
]

cleaned = [
    name.strip().lower()
    for name in raw
    if name.strip()
]

unique_names = set(cleaned)

sorted_names = sorted(unique_names)

print("Raw Data:")
print(raw)

print("\nCleaned List:")
print(cleaned)

print("\nUnique Names:")
print(unique_names)

print("\nSorted Names:")
print(sorted_names)