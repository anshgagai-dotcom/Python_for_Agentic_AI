# Words ki list ["hi","hello","hey","welcome"] mein se sirf 4 ya usse zyada letters waale words filter karo.
# Use filter() to keep only the words that have 4 or more letters from ["hi", "hello", "hey", "welcome"].


# Step 1 – Restate
"""
Check the length of every word.
Keep only words whose length is at least 4.
"""


# Step 2 – Example 
"""
Input = ["hi","hello","hey","welcome"]

Checking -
hi - two letters - remove
hello - five letters - keep
"""



# Step 3 – Pseudocode
"""
Create list
Use filter()
Check length, Keep words with length >= 4
Print
"""



# Step 4 – Translate

words = ["hi", "hello", "hey", "welcome"]

result = list(filter(lambda word: len(word) >= 4, words))

print(result)




# Step 5 – Trace Table
"""
| Word    | Length | Keep  |
| hi      |      2 |   no  |
| hello   |      5 |   yes |
| hey     |      3 |   no  |
| welcome |      7 |   yes |
print(result)
result = ['hello', 'welcome']
"""


