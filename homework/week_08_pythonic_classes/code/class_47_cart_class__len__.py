# Cart class mein __len__ add karo jo items ki sankhya de.
# Add __len__ to the Cart class so that it returns the number of items in the cart.

class Cart:
    """
    Represents a shopping cart.
    """

    def __init__(self) -> None:
        """
        Initialize an empty shopping cart.
        """
        self.items: list[str] = []

    def add(self, item: str) -> None:
        """
        Add an item to the shopping cart."""
        self.items.append(item)


    def __len__(self) -> int:
        """
        Return the number of items in the cart.
        """
        return len(self.items)


cart = Cart()

cart.add("Laptop")
cart.add("Mouse")
cart.add("Keyboard")

print(len(cart))

