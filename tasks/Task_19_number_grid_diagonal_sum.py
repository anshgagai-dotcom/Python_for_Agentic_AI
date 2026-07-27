"""Task 19 — Number Grid + Diagonal Sum (nested list)
Ek 3x3 grid banao:

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Poora grid tidy print karo (rows/columns aligned). Phir main diagonal ka sum (1+5+9) nikaalo.

Concepts: nested list, nested loop, grid[i][i], running total
Hint: diagonal ke liye ek hi index use karo: grid[i][i] for i in range(3)."""





grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("===== Number Grid =====")
for row in grid:
    for num in row:
        print(f"{num:3}", end="")
    print()

diagonal_sum = 0
for i in range(3):
    diagonal_sum = diagonal_sum + grid[i][i]

print("\nMain Diagonal Sum:", diagonal_sum)

