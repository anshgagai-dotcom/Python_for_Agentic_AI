"""
Create a child class that inherits from Animal but does not implement the sound() method. 
Try to create an object and observe the error.
"""
# Jaan-boojh kar ek child banao jo sound() na likhe — error padho.




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

class Bird(Animal):
    """
    Represent a bird without implementing sound().
    """
    pass

bird = Bird()