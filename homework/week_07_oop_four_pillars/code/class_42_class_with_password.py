# Ek Password class with _password aur ek check(guess) method jo True/False de.
# Create a Password class with _password and a check(guess) method that returns True or False.


class Password:
    """
    Represent a password and provide a method to check it.
    """

    def __init__(self, password: str) -> None:
        """
        Initialize the Password object with a password.
        """
        self._password: str = password

    def check(self, guess: str) -> bool:
        """
        Check whether the given password guess is correct.
        """
        return guess == self._password


password = Password("secret123")

print(password.check("wrong"))
print(password.check("secret123"))


