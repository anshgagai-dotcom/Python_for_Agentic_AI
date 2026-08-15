# User class mein from_dict classmethod banao.
# Create a from_dict class method in the User class that creates a User object from a dictionary.


class User:
    """
    Represent a user with a name and email.
    """

    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a User object.
        """
        self.name = name
        self.email = email

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "User":
        """
        Create a User object from a dictionary.
        """
        return cls(data["name"], data["email"])


user_data = {
    "name": "Ansh",
    "email": "anshgag.ai@gmail.com"
}

user = User.from_dict(user_data)

print(user.name)
print(user.email)