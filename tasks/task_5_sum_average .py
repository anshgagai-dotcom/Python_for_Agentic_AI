"""Task 5 — Sum & Average of N Numbers
User se pehle poochho kitne numbers dega (count). Phir loop mein ek-ek karke numbers lo, unka sum aur average print karo.

Concepts: for loop, running total, int(input()), :.2f
Hint: loop se pehle total = 0 banao, andar total = total + num."""



"""count = int(input("How Many numbers will you enter? "))
total = 0

for i in range(1, count + 1):
    number = int(input(f"Enter a number {i}: "))
    total = total + number

average = total / count    

print(f"Sum = {total}")
print(f"Average = {average}")"""






"""count = int(input("How many numbers will you enter? "))

total = 0

for i in range(1, count + 1):
    number = int(input(f"Enter a number {i}: "))
    total = total + number

average = total / count

print("\n==========Result==========")
print(f"Sum = {total}")
print(f"Average = {average}")"""



count = int(input("How many numbers will you enter? "))
total = 0

for i in range(1, count + 1):
    number = int(input(f"Enter a number {i}: "))
    total = total + number

average = total / count

print("\n==========Result==========")
print(f"Sum = {total}")
print(f"Average = {average}")


