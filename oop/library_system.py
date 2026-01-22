class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  
        self.file_size = file_size
    
    def __str__(self):
        return f"E-Book: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"Print Book: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"{book}")
        else:
            print("Error: Can only add Book objects")
    
    def list_books(self):

        def __str__(self):
            if not self.books:
                return f"{self} has no books"
            else:
                return f"\n{self} - Books:"
            for i, book in enumerate(self.books, 1):
                return f"  {i}. {book}"

