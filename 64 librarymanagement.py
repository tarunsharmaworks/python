# MAIN CONCEPT
# The main working of this program is to manage a simple library with the functionality of adding books by the title, author’s name, ISBN, genre and 
# checking book availability along with that it also has the functionality of borrowing and 
# returning the some functionalities are there which are unused also .
#  Which hopefully will be added later or it is upto you if you add the unused functionalities.
class book:
    def __init__(self,title,author,isbn,condition, available=True):
        self.title=title 
        self.author=author
        self.isbn=isbn
        self.condition=condition
        self.available=available

    def is_available(self):
        return self.available
    
    def borrow(self):
        if self.available:
            self.available=False
            return "BORROWING SUCCESSFUL"
        else:
            return "BORROWING UNSUCCESSFUL:BOOK UNAVAILABLE "
        
    def return_book(self):
        self.available=True
        return "BOOK RETURNED SUCCESSFULLY"
    
class library:
    def __init__(self):
        self.book_list=[]

    def add_book(self,book):
        self.book_list.append(book)

    def borrow_book(self,book):
        if book in self.book_list and book.is_available():
            book.borrow()
            return "BORROWING SUCCESSFUL"
        else:
            return"BORROWING UNSUCCESSFUL:BOOK UNAVAILABLE OR NOT FOUND"
    def return_book(self,book):
        book.return_book()

book1=book("book1","john",1,"mint",)
book2=book("book2","john2",2,"mint",)
book3=book("book3","john3",3,"mint",)
library=library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
borrow_book=library.borrow_book(book1)
borrow_book=library.borrow_book(book2)
print(borrow_book) #borrow success
# borrow_book2=library.borrow_book(book("cec","wcxw","ww","wxw"))
# print(borrow_book2)#book not real

#return borrowed book
library.return_book(book1)
if book1.is_available()==True:
    print("book is available")
    
if book1.is_available()!=True:
    print(f"book is not available")



