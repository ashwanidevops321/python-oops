class Book:                                               # ye class ek independent class hai jo kisi aur class par depend nahi hai.
    def __init__(self, title, auther, isbn):              # ye constructor hai jo book ka title, auther aur isbn leta hai.
        self.title = title
        self.auther = auther
        self.__isbn = isbn                                # ye private variable hai jo kisi aur class se access nahi kiya ja sakta.
        self.is_available = True                          # ye variable book ki availability ko track karta hai.
        
    def get_isbn(self):                                   # ye method private variable ko access karne ke liye hai.
        return self.__isbn                                # ye private variable ko return karta hai.
        
        
class User:                                               # ye class bhi ek independent class hai jo kisi aur class par depend nahi hai.
    def __init__(self, name):                             # ye constructor hai jo user ka naam leta hai.                      
        self.name = name                                  # ye public variable hai jo kisi aur class se bhi access kiya ja sakta hai.   
        self.borrowed_book = []                           # ye list hai jo user ke dwara borrow kiye gaye books ko track karti hai.
        
          
    def borrow_book(self, book):                          # ye method book ko borrow karne ke liye hai.
        if book.is_available:                             # ye check karta hai ki book available hai ya nahi.
            self.borrowed_book.append(book)               # agar book available hai to use user ki borrowed list(self.borrowed_book) me add karta hai.
            book.is_available = False                     # book ko unavailable mark karta hai.
            print(f"{self.name} borrowed {book.title}")   # print karta hai ki user ne book borrow ki hai.
        else:
            print(f"{book.title} is not available for borrowing.")   # print karta hai ki book available nahi hai.
            
    def return_book(self, book):                         # ye method book ko return karne ke liye hai.
        if book in self.borrowed_book:                   # ye check karta hai ki book user ke borrowed list me hai ya nahi.
            self.borrowed_book.remove(book)              # agar book user ke borrowed list me hai to use remove karta hai.
            book.is_available = True                     # book ko available mark karta hai.
            print(f"{self.name} returned {book.title}")  # print karta hai ki user ne book return ki hai.
        else:
            print(f"{self.name} did not borrow {book.title}") # print karta hai ki user ne book borrow nahi ki hai.
            
class AdminUser(User):
    def __init__(self, name):                           # ye constructor hai jo user ka naam leta hai. 
        super().__init__(name)                          # ye parent class ka constructor call karta hai.
        
    def add_book(self, library, book):                   # ye method library me book add karne ke liye hai.
        library.add_book(book)                           # ye method library me book add karne ke liye hai.
        print(f"{self.name} added {book.title} to library.") # print karta hai ki user ne book library me add ki hai.
            
            
class Library:
    def __init__(self):                             # ye constructor hai jo library ka object create karta hai.
        self.books = []                                  # ye list hai jo library me books ko track karti hai.
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Auther: {book.auther}, ISBN: {book.get_isbn()}")
            
library = Library()                                   # ye library ka object create karta hai.


book1 = Book("Book 1", "Author 1", "ISBN001")         # ye book ka object create karta hai.
book2 = Book("Book 2", "Author 2", "ISBN002")         # ye book ka object create karta hai.
book3 = Book("Book 3", "Author 3", "ISBN003")         # ye book ka object create karta hai.

admin = AdminUser("Sudhanshu")                       # ye admin ka object create karta hai.
admin.add_book(library, book1)                       # ye admin library me book add karta hai.
admin.add_book(library, book2)                       # ye admin library me book add karta hai.
admin.add_book(library, book3)                       # ye admin library me book add karta hai.


user1 = User("Ashwani")                             # ye user ka object create karta hai.
user2 = User("Ravi")                                # ye user ka object create karta hai.

user1.borrow_book(book1)                          # ye user book ko borrow karta hai.
user1.borrow_book(book2)                          # ye user book ko borrow karta hai.
user1.borrow_book(book3)                          # ye user book ko borrow karta hai.

user2.borrow_book(book1)                          # ye user book ko borrow karta hai.
user2.borrow_book(book2)                          # ye user book ko borrow karta hai.
user2.borrow_book(book3)                          # ye user book ko borrow karta hai.

user1.return_book(book1)                         # ye user book ko return karta hai.
user1.return_book(book2)                         # ye user book ko return karta hai.
user1.return_book(book3)                         # ye user book ko return karta hai.

library.show_books()                               # ye library me books ko show karta hai.
user2.return_book(book1)                         # ye user book ko return karta hai.

    