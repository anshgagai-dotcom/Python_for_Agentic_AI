"""
pathlib se ek folder banao aur usme ek file likho (write_text).
Current folder ki saari .txt files list karo (glob).
safe_read jaisा function banao jo ek allowed folder ke bahar ke path ko reject kare.
"""


"""
1. Create a folder using pathlib and create a file inside that folder using write_text().

2. List all the .txt files in the current folder using glob().

3. Create a function like safe_read() that rejects any path that tries to go outside an allowed/base folder.
Hints
Use Path() to work with paths.
Use .mkdir() to create a folder.
Use .write_text() to write text into a file.
Use .glob("*.txt") to find text files.
Use .resolve() and .is_relative_to() to check whether a path is safe.
"""




from pathlib import Path

# Question 1
folder = Path("test_folder")
folder.mkdir(exist_ok=True)
(folder / "data.txt").write_text("hello", encoding="utf-8")


# Question 2
for f in Path(".").glob("*.txt"):
    print(f.name)


# Question 3
def is_safe(base_name, user_name):
    base = Path(base_name).resolve()
    target = (base / user_name).resolve()
    return target.is_relative_to(base)


print(is_safe("uploads", "ok.txt"))
print(is_safe("uploads", "../secret.txt"))