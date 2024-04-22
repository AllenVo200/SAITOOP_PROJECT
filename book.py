class Book:

    #method is a constructor that initializes the book object
    def __init__(self, isbn, title, author, genre, availability):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = availability
    #method points out the information of the book
    def display_info(self):
        print("ISBN:", self.isbn)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Genre:", self.genre)
        print("Availability:", self.availability)
    def borrow_book(self):
        if self.available:
            print("You have borrowed the book:", self.title)
            self.available = False
        else:
            print("Sorry, the book", self.title, "is not available for borrowing.")

    def return_book(self):
        if not self.available:
            print("You have returned the book:", self.title)
            self.available = True
        else:
            print("Error: The book", self.title, "is already available.")