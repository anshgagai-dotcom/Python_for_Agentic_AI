"""
Create an Animal parent class. Create Cat and Cow child classes that inherit from Animal.
Each child class should have its own sound() method.
"""
# Animal parent banao; Cat aur Cow children banao, har ek apni awaaz wala method.


class Animal:
    """
    Represent a general animal.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize an animal with a name.
        """
        self.name = name

    def eat(self) -> None:
        """
        Print that the animal is eating.
        """
        print(f"{self.name} eats")


class Cat(Animal):
    """
    Represent a cat.
    """

    def sound(self) -> str:
        """
        Return the sound made by the cat.
        """
        return f"{self.name} says Meow"


class Cow(Animal):
    """
    Represent a cow.
    """

    def sound(self) -> str:
        """
        Return the sound made by the cow.
        """
        return f"{self.name} says Moo"


cat = Cat("Kitty")
cow = Cow("Kamdhenu")

print(cat.sound())
print(cow.sound())

cat.eat()
cow.eat()
