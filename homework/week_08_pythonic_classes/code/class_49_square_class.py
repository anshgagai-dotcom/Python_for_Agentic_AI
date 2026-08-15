# Square class mein area property banao.
# Create an area property in the Square class that calculates the area of the square.


class Square:
    """
    Represent a square with a given side length.
    """

    def __init__(self, side: float) -> None:
        """
        Initialize a square with a side length.
        """
        self.side = side

    @property
    def area(self) -> float:
        """
        Return the area of the square.
        """
        return self.side ** 2


square = Square(9)

print(square.area)