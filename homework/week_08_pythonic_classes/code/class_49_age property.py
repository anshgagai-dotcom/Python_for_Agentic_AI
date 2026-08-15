# Person class mein age property + setter banao jo negative age reject kare.
# Create an age property and setter in the Person class that rejects negative ages.


class Person:
    """
    Represent a person with a validated age.
    """

    def __init__(self, age: int) -> None:
        """
        Initialize a person with an age.
        """
        self._age = age

    @property
    def age(self) -> int:
        """
        Return the person's age.
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """
        Set the person's age and reject negative values.
        """
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value


person = Person(20)

person.age = 26

print(person.age)