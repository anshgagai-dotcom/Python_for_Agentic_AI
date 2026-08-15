# 3 objects ki list banao aur print karke dekho __repr__ kaise kaam karta hai.
# Create a list containing 3 Book objects and print the list to see how __repr__ works.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __repr__(self):
        return f"Book({self.title}, {self.author})"


books = [
    Book("Python Language", "Ansh"),
    Book("ML", "Laado"),
    Book("Data Science", "Golu")
]

print(books)
