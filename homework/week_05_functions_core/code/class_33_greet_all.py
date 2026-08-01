# Write a function greet_all(*names) that prints
# greet_all(*names) jo har naam ko "Hello NAME" print kare (loop se).


#1
def greet_all(*names):

    for name in names:
        print(f"Hello {name}")

greet_all("Ansh", "Golu", "Sham")



