class Book:
    def __init__ (self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def title(self):
        print(f"the book title is {self.title}")

    def author(self):
        print(f"the book author is {self.author}")

    def isbn(self):
        print(f"the book isbn is {self.isbn}")

    def available(self):
        print(f"available{self.available}")

    def assignment(self):
        print(f"the book title is {self.title}, the author is {self.author}, the isbn is {self.isbn} and its availability is {self.available}")

    def  details(self):
        print(f"the book title is {self.title}")
        print(f"the book author is {self.author}")
        print(f"the book isbn is {self.isbn}")
        print(f"available{self.available}")


B1 = Book("what i will do", "iano", "1999", True)
B2 = Book("faith", "nyanjui", "2000", True)
B3 = Book("destiny", "Alvin", "1450", True)

print(f"the book details are as follows: {B1.details()}")

print(f"{B1.assignment()}")





