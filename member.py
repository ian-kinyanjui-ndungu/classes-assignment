from book import Book

class Member:
    def __init__(self, name, memberid):
        self.name = name
        self.memberid = memberid
        self.borrowedbooks = []

    def borrowed_books(self, book):
        if book.available:
            print("the book  is available")
            book.available = False
            self.borrowedbooks.append(book)
            print(f"{self.name} borrowed:{book}")
        else:
            print("sorry{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowedbooks:
            print(f"you had borrowed:{book}")
            book.available = True
            self.borrowedbooks.remove(book)
            print(f"{self.name} returned:{book}")
        else:
            print(f"{self.name} had not borrowed:{book}")

m1 = Member("nyanjui", "12345")

print(f"")