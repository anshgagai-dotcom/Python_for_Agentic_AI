# Ek Circle class with radius aur method area() jo area return kare.
# Create a Circle object with a radius() and print its area.



from turtle import circle


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(7)

print(circle.area())
