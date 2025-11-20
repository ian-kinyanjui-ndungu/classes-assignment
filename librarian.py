from django.utils.translation.trans_real import catalog

from member import *
class Librarian(Member):
    def __init__(self, book, catalogue):
        self.book = book
        self.catalogue = []
        
    def add_book(self,book):
        if book in self.catalogue:
            print(f"{book} is already in the catalogue")
        else:
            self.catalogue.append(book)
            print(f"{book} has been added to the catalogue")
            
    def remove_book (self,book):
        if book in self.catalogue:
            self.catalogue.remove(book)
            print(f"you have successfully removed {book} from catalogue")
        else:
            print(f"{book} is not in the catalogue")
       
#creating objects
b1= Librarian("wellness", "mainlib")

b1.add_book("wellness")
# b1.remove_book("wellness")
# b1.add_book("wellness")

b1.remove_book("Alvin")

