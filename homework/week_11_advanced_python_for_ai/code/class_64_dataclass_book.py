# Ek @dataclass Book banao (title, author, year) aur 2 objects compare karo.
# Create a @dataclass called Book with title, author, and year, and compare two objects.


from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int


book1 = Book("Python Basics", "Rahul", 2025)
book2 = Book("Python Basics", "Rahul", 2025)

print(book1 == book2)   

