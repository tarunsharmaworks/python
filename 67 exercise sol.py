# class Library1:
#   def __init__(self):
#     self.noBooks = 0
#     self.books = []
    
#   def addBook(self, book):
#     self.books.append(book)
#     self.noBooks = len(self.books)

#   def showInfo(self):
#     print(f"The library has {self.noBooks} books. The books are")
#     for book in self.books:
#       print(book)


# l1 = Library1()
# l1.addBook("Harry Potter1")
# l1.addBook("Harry Potter2")
# l1.addBook("Harry Potter3")
# l1.showInfo()

class library:
  def __init__(self):
    self.no_books=0
    self.books=[]

  def add_book(self,book):
    self.books.append(book)
    self.no_books=len(self.books)

  def library_info(self):
    print(f"The library has {self.no_books} books. The books are") 
    counter=0
    for book in self.books:
      counter+=1
      print(f"{counter}]{book}") 

  def borrow_book(self,n):
    book=self.books.pop(n)
    print(f"borrowed book is-->{book}")


bk1=library()
bk1.add_book("Harry Potter1")    
bk1.add_book("Harry Potter3")    
bk1.add_book("Harry Potter2") 
bk1.library_info()
bk1.borrow_book(0)