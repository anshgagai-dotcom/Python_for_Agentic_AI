# Book class banao jisme title aur author ho aur __repr__ add karo.
# Create a Book class with title and author attributes and add a __repr__ method.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({self.title}, {self.author})"


book = Book("Data Science", "Ansh")

print(book)
