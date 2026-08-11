# Ek Temperature class banao with _celsius; ek method set_celsius jo -273 se kam value reject kare.
# Create a Temperature class with _celsius; create a method set_celsius that rejects values below -273.


class Temperature:
    """
    Represent a temperature in Celsius.
    """

    def __init__(self) -> None:
        """
        Initialize the temperature to 0°C.
        """
        self._celsius: float = 0.0

    def set_celsius(self, value: float) -> None:
        """
        Set the Celsius temperature if it is valid.
        """
        if value < -273:
            print("Invalid temperature!")
            return

        self._celsius = value

    def get_celsius(self) -> float:
        """
        Return the current Celsius temperature.
        """
        return self._celsius


temperature = Temperature()

temperature.set_celsius(25)
print(temperature.get_celsius())

temperature.set_celsius(-300)
print(temperature.get_celsius())