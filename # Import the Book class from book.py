# Import the Book class from book.py
from book import Book

# Create some book objects
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Borrow a book
if book1.borrow():
    print("Book 1 is now borrowed.")
else:
    print("Book 1 is already borrowed.")

# Return a book
if book1.return_book():
    print("Book 1 is now returned.")
else:
    print("Book 1 was not borrowed.")

# Try to borrow it again
if book1.borrow():
    print("Book 1 is now borrowed.")
else:
    print("Book 1 is already borrowed.")
