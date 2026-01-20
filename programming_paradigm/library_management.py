class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    
    def __init__(self):
        self.books = []
        self.checked_out_books = {}  # Store checked out books by title
        
    def add_book(self, book):
        self.books.append(book)
        
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.checked_out_books[title] = book  # Save for later
                return True
        return False
    
    def return_book(self, title):
        if title in self.checked_out_books:
            self.books.append(self.checked_out_books[title])
            del self.checked_out_books[title]
        return
    
    def list_available_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")