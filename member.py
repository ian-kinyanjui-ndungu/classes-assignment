from book import B1, B2, B3


class Member:
    
    # defining a constructor
    def __init__(self, name, memberid):
        self.name = name
        self.memberid = memberid
        self.borrowedbooks = []
    #defining a method to borrow books
    def borrowed_books(self, book):
        if book.available:
            print("the book  is available")
            book.available = False
            self.borrowedbooks.append(book)
            print(f"{self.name} borrowed:{book.title}")
        else:
            print(f"sorry{book.title} is not available.")
    #defining a method to return books
    def return_book(self, book):
        if book in self.borrowedbooks:
            print(f"you had borrowed:{book.title}")
            book.available = True
            self.borrowedbooks.remove(book)
            print(f"{self.name} returned:{book.title}")
        else:
            print(f"{self.name} had not borrowed:{book.title}")

# Creating an object
m1 = Member("nyanjui", "12345")
m2 = Member("Byron", "12356")


# calling a method

# print(f"{m1.borrowed_books(B2)}")
# m1.borrowed_books(B3)
# m1.return_book(B3)
# print(f"")

# m1.return_book(B1)