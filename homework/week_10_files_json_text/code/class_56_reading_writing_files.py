"""Ek file mygoals.txt mein 3 goals likho (write mode).
Use padho aur print karo.
Append mode se ek 4th goal add karo, phir dobara poori file padho. 
"""



"""
1. Write 3 different goals into a file named mygoals.txt.

2. Read the mygoals.txt file and print all the goals on the screen.

3. Add a 4th goal to the same file without deleting the existing goals. Then read the file again and print all 4 goals.

Hint
Use:
"w" mode → to write the first 3 goals
"r" mode → to read the file
"a" mode → to add the 4th goal
"""




# Step 1: Write 3 goals
with open("mygoals.txt", "w", encoding="utf-8") as file:
    file.write("Improve my Python skills\n")
    file.write("Create my first AI project\n")
    file.write("Practice coding every day\n")


# Step 2: Read the file
with open("mygoals.txt", "r", encoding="utf-8") as file:
    print(file.read())


# Step 3: Add a 4th goal
with open("mygoals.txt", "a", encoding="utf-8") as file:
    file.write("Learn something new every week\n")


# Step 4: Read again
with open("mygoals.txt", "r", encoding="utf-8") as file:
    print(file.read())
    