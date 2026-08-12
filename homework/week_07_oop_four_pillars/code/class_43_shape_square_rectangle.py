"""
Create a Shape parent class with a name attribute. 
Create Square and Rectangle child classes that inherit from Shape and use super() to initialize the parent class.
"""
# Shape parent (with name); Square aur Rectangle children with super().


class Shape:
    """
    Represent a general shape.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a shape with a name.
        """
        self.name = name


class Square(Shape):
    """
    Represent a square.
    """

    def __init__(self, name: str, side: float) -> None:
        """
        Initialize a square.
        """
        super().__init__(name)
        self.side = side


class Rectangle(Shape):
    """
    Represent a rectangle.
    """

    def __init__(self,name: str, width: float, height: float ) -> None:
        """
        Initialize a rectangle.
        """
        super().__init__(name)
        self.width = width
        self.height = height


square = Square("Square", 5)
rectangle = Rectangle("Rectangle", 10, 4)

print(square.name)
print(square.side)

print(rectangle.name)
print(rectangle.width)
print(rectangle.height)