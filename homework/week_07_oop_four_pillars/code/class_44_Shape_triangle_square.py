"""
Create a Shape parent class. Create Triangle and Square child classes. 
Each child class should have its own area() method that calculates its area.
"""
# Shape parent; Triangle aur Square children, dono ka apna area().



class Shape:
    """
    Represent a general shape.
    """

    def area(self) -> float:
        """
        Return a default area.
        """
        return 0.0


class Square(Shape):
    """
    Represent a square.
    """

    def __init__(self, side: float) -> None:
        """
        Initialize a square with a side length.
        """
        self.side = side

    def area(self) -> float:
        """
        Calculate and return the area of the square.
        """
        return self.side ** 2


class Triangle(Shape):
    """
    Represent a triangle.
    """

    def __init__(self, base: float, height: float) -> None:
        """
        Initialize a triangle with base and height.
        """
        self.base = base
        self.height = height

    def area(self) -> float:
        """
        Calculate and return the area of the triangle.
        """
        return 0.5 * self.base * self.height


square = Square(6)
triangle = Triangle(8, 5)

print("Square area:", square.area())
print("Triangle area:", triangle.area())