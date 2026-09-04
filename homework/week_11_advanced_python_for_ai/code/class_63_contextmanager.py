"""
Create your own context manager using @contextmanager that prints "Enter"/"Exit".
Find the frequency of every word in a sentence using Counter.
Use defaultdict(list) to group students according to their grade.
"""

"""
Apna context manager @contextmanager se banao jo "Enter"/"Exit" print kare.
Ek sentence mein har word ki frequency Counter se nikaalo.
defaultdict(list) se students ko unki grade ke hisaab se group karo.
"""



from contextlib import contextmanager
from collections import Counter, defaultdict

# 1
@contextmanager
def section():
    print("Enter")
    yield
    print("Exit")

with section():
    print("Inside")

# Enter
# Inside
# Exit


# 2
print(Counter("the cat sat on the mat".split()))

# Counter({'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1})


# 3
students = [("Asha", "A"), ("Rahul", "B"), ("Priya", "A")]

groups = defaultdict(list)

for name, grade in students:
    groups[grade].append(name)

print(dict(groups))




