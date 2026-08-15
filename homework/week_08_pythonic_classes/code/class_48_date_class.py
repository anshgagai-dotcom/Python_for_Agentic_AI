# Date class banao with from_string("2026-06-28") classmethod, jo string ko year, month, aur day mein tod de.
# Create a Date class with a from_string("2026-06-28") class method that converts the string into year, month, and day.


class Date:
    """
    Represent a date using year, month, and day.
    """

    def __init__(self, year: int, month: int, day: int) -> None:
        """
        Initialize a Date object.
        """
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text: str) -> "Date":
        """
        Create a Date object from a YYYY-MM-DD string.
        """
        year, month, day = text.split("-")
        return cls(int(year), int(month), int(day))


date = Date.from_string("2026-08-15")

print(date.year)
print(date.month)
print(date.day)