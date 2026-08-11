# Ek Car class banao with brand, speed, aur ek method drive() jo "BRAND is driving at SPEED" print kare.
# Create two objects of the Car class with different brands and speeds, and call the drive() method for both objects.


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed}")

car1 = Car("Marauti", 80) 
car2 = Car("BMW", 120)

car1.drive()
car2.drive()