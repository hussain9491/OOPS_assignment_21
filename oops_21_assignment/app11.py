#  Class Methods
# Assignment: 11
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.
class Book:
    total_book = 0
    @classmethod
    def increment_book_count(cls):
        cls.total_book += 1
        print(f"Total books: {cls.total_book}")
    def __init__(self, add_book):
        self.add_book = add_book
        Book.increment_book_count()
total_book = Book("Python Programming")
print(f"Book added: {total_book.add_book}")        
total_book.increment_book_count()
        
     
