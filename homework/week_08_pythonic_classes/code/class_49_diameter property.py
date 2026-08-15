# Circle mein diameter property banao jo 2 * radius return kare.
# Create a diameter property in the Circle class that returns 2 * radius.


class Circle:
    """
    Represent a circle with a given radius.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a circle with a radius
        """
        self.radius = radius

    @property
    def diameter(self) -> float:
        """
        Return the diameter of the circle.
        """
        return 2 * self.radius


circle = Circle(6)

print(circle.diameter)