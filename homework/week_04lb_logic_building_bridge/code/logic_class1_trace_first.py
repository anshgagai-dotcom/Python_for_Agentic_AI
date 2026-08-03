# Har ek ke liye trace table banao, output likho, PHIR code chala kar check karo.
# Create a trace table for each program, Predict the output, Run the code, Compare your prediction with the actual output.


# 1 Running Total

"""| Step   | i | x          |
| ------ | - | ---------- |
| Shuru  | — | 10         |
| Loop 1 | 0 | 10 - 2 = 8 |
| Loop 2 | 1 | 8 - 2 = 6  |
| Loop 3 | 2 | 6 - 2 = 4  |
| Print  | — | 4          |"""

x = 10
for i in range(3):
    x = x - 2
print(x)




# 2 Reverse a String

"""| Step   | c | result             |
| ------ | - | ------------------ |
| Shuru  | — | ""                 |
| Loop 1 | c | "c" + "" = "c"     |
| Loop 2 | a | "a" + "c" = "ac"   |
| Loop 3 | t | "t" + "ac" = "tac" |
| Print  | — | "tac"              |"""

result = ""
for c in "cat":
    result = c + result
print(result)



# 3 Find the Largest Number

"""| Step   | n | biggest |
| ------ | - | ------- |
| Shuru  | — | 4       |
| Loop 1 | 4 | 4       |
| Loop 2 | 1 | 4       |
| Loop 3 | 7 | 7       |
| Loop 4 | 3 | 7       |
| Print  | — | 7       |"""

nums = [4, 1, 7, 3]
biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
print(biggest)





# 4 Sum of Even Numbers

"""| Step   | i | Even? | s         |
| ------ | - | ----- | --------- |
| Shuru  | — | —     | 0         |
| Loop 1 | 1 | No    | 0         |
| Loop 2 | 2 | Yes   | 0 + 2 = 2 |
| Loop 3 | 3 | No    | 2         |
| Loop 4 | 4 | Yes   | 2 + 4 = 6 |
| Loop 5 | 5 | No    | 6         |
| Print  | — | —     | 6         |"""

s = 0
for i in range(1, 6):
    if i % 2 == 0:
        s = s + i
print(s)

