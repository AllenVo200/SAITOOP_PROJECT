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

    #getter method to get genre name
    def get_genre_name(self):
        genre_dict = {0: "Romance", 1: "Mystery", 2: "Science Fiction", 3: "Thriller", 4: "Young Adult", 5: "Children's Fiction", 6: "Self-help", 7: "Fantasy", 8: "Historical Fiction", 9: "Poetry"}
        return genre_dict[self.genre]

    #Additional getter method to return string on available attribute
    def get_availability(self):
        return "Available" if self.availability else "Not Available"
    
    #setter methods to return parameters.
    def get_isbn(self):
        return self.isbn
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_genre(self):
        return self.genre
    #setter method to get all the information of the book
    def get_all_info(self):
        return self.isbn, self.title, self.author, self.genre, self.availability

    #setter that changes a certain object in the list
    def set_isbn(self,isbn):
        self.isbn=isbn
    def set_title(self,title):
        self.title=title
    def set_author(self,author):
        self.author=author
    def set_genre(self,genre):
        self.genre=genre
    
    #method to borrow the book
    def borrow_it(self):
        if self.availability:
            self.availability = False
        else:
            print("Sorry, the book", self.title, "is not available for borrowing.")

    #method to return the book
    def return_it(self):
        if not self.availability:
            self.availability = True
        else:
            print("Error: The book", self.title, "is already available.")

    #Return the string representation of the book object formated for display table
    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.isbn, self.title, self.author, self.get_genre_name(), self.get_availability())
    
