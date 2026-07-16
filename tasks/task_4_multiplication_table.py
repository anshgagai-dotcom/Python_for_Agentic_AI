"""Task 4 — Multiplication Table (clean)
User se ek number n aur ek limit k lo. n ka table 1 se k tak print karo (loop se).

Concepts: for loop, range(1, k+1), f-string
Hint: range ka stop exclusive hai — k ko shaamil karne ke liye k + 1 likho."""



"""n = int(input("Enter a number: "))
k = int(input("Enter a limit: "))

print("\n")
print(f"Multiplication of table: {n}.")
print("\n")

for i in range(1, k + 1):
    print(f"{n} * {i} = {n * i}")"""
    














"""n = int(input("Enter a number: "))
k = int(input("Enter a limit: "))

print("\n")
print("=" * 25)
print(f"Multiplication of Table: {n}.")
print("=" * 25)

for i in range(1, k + 1):
    print(f"{n} * {i} = {n * i}")"""





n = int(input("Enter a number: "))
k = int(input("Enter a limit: "))

print("=" * 30)
print(f"\n Multiplication of Table: {n}")
print("=" * 30)

for i in range(1, k + 1):
    print(f"{n} * {i} = {n * i}")

    