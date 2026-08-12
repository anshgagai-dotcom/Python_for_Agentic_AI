"""
Create a list containing different shape objects and use a loop to call area() for each shape and print the result.
"""
# Ek list mein alag shapes daalo aur loop se sabka area print karo. 




"""
Create a list containing different shape objects and use a loop
to call area() for each shape and print the result.
"""

class Shape:
    """Represent a general shape."""

    def area(self) -> float:
        """Return the default area."""
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

shapes: list[Shape] = [square, triangle]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area()}")