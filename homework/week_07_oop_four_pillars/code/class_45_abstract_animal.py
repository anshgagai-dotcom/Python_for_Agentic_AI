"""
Create an abstract Animal class with an abstract sound() method. 
Create Dog and Cat classes that inherit from Animal and implement the sound() method.
"""
# Ek abstract Animal banao with abstract sound(). Dog aur Cat se implement karo.




from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Represent an abstract animal.
    """

    @abstractmethod
    def sound(self) -> str:
        """
        Return the sound made by the animal.
        """
        ...

class Dog(Animal):
    """
    Represent a dog.
    """
    def sound(self) -> str:
        """
        Return the sound made by a dog.
        """
        return "Woof!"


class Cat(Animal):
    """
    Represent a cat.
    """
    def sound(self) -> str:
        """
        Return the sound made by a cat.
        """
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())