"""Ek CSV file 3 students ke naam+marks ke saath banao aur DictReader se padho.
Ek sentence se saare numbers re.findall(r"\d+") se nikaalo.
Ek text se saare hashtags """

"""
1. Create a CSV file containing the names and marks of 3 students, and read it using DictReader.

2. Extract all the numbers from a sentence using re.findall(r"\d+").

3. Extract all the hashtags (#word) from a text.
"""



import csv
import re


# ==================================================
# Question 1
# Create a CSV file with 3 students and read it
# using DictReader
# ==================================================

with open("s.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerows([
        ["Name", "Marks"],
        ["A", 80],
        ["B", 90],
        ["C", 70]
    ])

with open("s.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["Name"], row["Marks"])


# ==================================================
# Question 2
# Extract all numbers from a sentence
# ==================================================

print(re.findall(r"\d+", "I am 17, born in 2009"))
# ['17', '2009']


# ==================================================
# Question 3
# Extract all hashtags from a text
# ==================================================

print(re.findall(r"#\w+", "Loving #python and #ai"))
# ['#python', '#ai']

