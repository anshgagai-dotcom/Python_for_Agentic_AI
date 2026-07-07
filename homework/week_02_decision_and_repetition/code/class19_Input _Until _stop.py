#1
"""total = 0

while True:
    entry = input("Enter number (or 'stop'): ")

    if entry.lower() == "stop":
        break

    total += int(entry)

print(f"Total = {total}")"""


#2
"""count = 0

while True:
    entry = input("Enter number (or 'stop'): ")

    if entry.lower() == "stop":
        break

    count += 1

print(f"Numbers Entered = {count}")"""


#3
"""largest = None

while True:
    entry = input("Enter number (or 'stop'): ")

    if entry.lower() == "stop":
        break

    number = int(entry)

    if largest is None or number > largest:
        largest = number

print(f"Largest Number = {largest}")"""


#4
"""total = 0
count = 0

while True:
    entry = input("Enter number (or 'stop'): ")

    if entry.lower() == "stop":
        break

    total += int(entry)
    count += 1

if count > 0:
    print(f"Average = {total / count}")
else:
    print("No numbers entered.")"""



#5
"""positive = 0
negative = 0

while True:
    entry = input("Enter number (or 'stop'): ")

    if entry.lower() == "stop":
        break

    number = int(entry)

    if number >= 0:
        positive += 1
    else:
        negative += 1

print(f"Positive Numbers = {positive}")
print(f"Negative Numbers = {negative}")"""



