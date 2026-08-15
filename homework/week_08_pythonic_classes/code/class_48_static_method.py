# Temperature class mein staticmethod c_to_f(c) add karo.
# Add a static method c_to_f(c) to the Temperature class that converts Celsius to Fahrenheit.


class Temperature:
    """
    Provide temperature conversion utilities.
    """

    @staticmethod
    def c_to_f(celsius: float) -> float:
        """
        Convert Celsius temperature to Fahrenheit.
        """
        return (celsius * 9 / 5) + 32


print(Temperature.c_to_f(28))