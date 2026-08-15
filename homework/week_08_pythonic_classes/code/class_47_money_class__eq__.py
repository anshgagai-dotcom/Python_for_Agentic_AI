# Money class (amount) mein __eq__ add karo taaki same amount equal ho.
# Add __eq__ to the Money class so that two objects with the same amount are considered equal.


class Money:
    """
    Represents a money amount.
    """

    def __init__(self, amount: int) -> None:
        """
        Initialize a Money object with an amount.
        """
        self.amount = amount

    def __eq__(self, other: "Money") -> bool:
        """
        Return True if both Money objects have the same amount.
        """
        return self.amount == other.amount


money1 = Money(500)
money2 = Money(500)

print(money1 == money2)