# Student class mein __str__ add karo jo "NAME scored MARKS" return kare.
# Add a __str__ method to the Student class that returns "NAME scored MARKS".


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"


student = Student("Ansh", 92)

print(student)