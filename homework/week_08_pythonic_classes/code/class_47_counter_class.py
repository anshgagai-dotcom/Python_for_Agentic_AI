# Ek Counter class banao jisme class attribute total ho jo har object par badhe.
# Create a Counter class with a class attribute total that increases whenever a new object is created.



class Counter:
    """
    Counts how many Counter objects have been created.
    """

    total: int = 0

    def __init__(self) -> None:
        """
        Create a Counter object and increase the total count.
        """
        Counter.total += 1


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

print(Counter.total)
