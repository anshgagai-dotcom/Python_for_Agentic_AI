# Ek Student class with name, marks, aur method report() jo report print kare. 2 objects banao.
# Create three Student objects with different names and marks, and call the report() method for each object.


class Student:
    """
    Represent a student with a name and marks.
    """
    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks


    def report(self) -> None:
        """
        Print the student's name and marks.
        """
        print(f"{self.name} scored {self.marks} marks")

st1 = Student("Ansh", 85)
st2 = Student("Sahil", 90)
st3 = Student("Jai", 78)

st1.report()
st2.report()
st3.report()

