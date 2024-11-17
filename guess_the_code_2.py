class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"
book1 = Book("prisoner of azkaban", "J.K_rowling", 5000)
print(book1)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():  # Case-insensitive match
                return book
        return None

library = Library()
library.add_book(book1)  
library.add_book(Book("python 101", "jhonny", 6000) ) 
library.list_books()

result = library.find_book_by_title("prisoner of azkaban")
if result:
    print("Book found:", result)
else:
    print("Book not found")



# 1. Classes and Attributes:

#What is the purpose of the Book class? What attributes does it have?

#------The Book class represents individual book objects, 
#------Attributes of the Book Class:
# title: The title of the book (e.g., "Prisoner of Azkaban").
# author: The author of the book (e.g., "J.K. Rowling").
# copies: The number of copies available (e.g., 5000).

#What is the purpose of the Library class? What does its books attribute store?

# the library holds a kist of books and provides functionality to manage and interact with this collection.
# The books attribute is a list that stores instances of Book objects, acting as a catalog of the library's collection.

# 2. Methods:

#What does the add_book method do?
#-------The add_book method appends a Book object to the books list.

#What happens when the list_books method is called?
# The list_books method iterates through the books list and prints each Book object using the __str__ method of the Book class. 
# This method provides a formatted output for each book.

# 3. Behavior Analysis:

#What is the output of the list_books method after the books are added?
# Title: Prisoner of Azkaban, Author: J.K. Rowling, Copies: 5000


#What happens if you call add_book with a new book object?
# book2 will be added to the books list. Calling library.list_books() afterward will print both book1 and book2:

# 4. Code Change:

#If you wanted to add a method to find a book by title in the library, how would you do it?
# def find_book_by_title(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():  
#                 return book
#         return None

