import csv
import os
import book


#loads the list into the system, if file is not found, it will ask for the file name again. after function is complete return the list of books to main
def load_books():
    print("Starting the system ...")
    file_name = input(str("Enter the file name: "))
    while not os.path.isfile(file_name):
        file_name = input(str("File not found. Re-enter book catalog filename: "))
         
    print("Book catalog has been loaded.")    
    
    book_list = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for line in reader:
            book_list.append(book.Book(str(line[0]), line[1], line[2], int(line[3]), "True"==(line[4])))
                
    return book_list

#prints out the menu for the user to choose from returns the users selection, if librian menu is created, reprint the menu with the librian options
def print_menu():
    print("\nReader's Guild Library - Main Menu")
    print("==================================")
    print("1. Search for books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("0. Exit the system")
    selection = int(input("Enter your selection: "))
    print(selection)
    while selection > (3) and selection != 2130:
        print("Invalid option")
        selection = int(input("Enter your selection: "))
    return selection

def print_menu_librian():
    print("\nReader's Guild Library - Librian Menu")
    print("==================================")
    print("1. Search for books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a book")
    print("5. Remove a book")
    print("6. Update a book")
    print("0. Exit the system")
    selection = int(input("Enter your selection: "))
    while selection > (6):
        print("Invalid option")
        selection = int(input("Enter your selection: "))
    return selection


#searches for the book in the list and returns the book if found(searches per index), converts everything is in lowercase to scrape data easier
def check_book(book_list):
    print("-- Search for books --")
    index = 0
    search_value = input("Enter a search value:")
    while index < len(book_list):
        current_book = book_list[index]

        for field in current_book.get_all_info():
            if search_value.lower() in str(field).lower():
                print("Found a match... :", current_book.__str__()) #This is the print book function __str__ from book.py
                return
        index += 1

#borrow book function, searches for the book by ISBN, if found, borrow the book, if not found, print no book found
def borrow_book(book_list):
    print("-- Borrow for books --")
    find_book_by_isbn = str(input("Enter the 13 digit ISBN (format 999-9999999999) "))
    index = 0 
    
    while index < len(book_list):
        current_book = book_list[index]
        if find_book_by_isbn == str(current_book.get_isbn()):
            current_book.borrow_it()
            return

        index += 1 

    print("No book found with that ISBN")  

#return book function, searches for the book by ISBN, if found, return the book, if not found, print no book found
def return_book(book_list):
    print("-- Return for books --")
    find_book_by_isbn = str(input("Enter the 13 digit ISBN (format 999-9999999999) "))
    index = 0 
    while index < len(book_list):
        current_book = book_list[index]
        if find_book_by_isbn == str(current_book.get_isbn()):
            current_book.return_it()
            return

        index += 1 
    
    print("No book found with that ISBN")  

#ADDS THE BOOKS TOGETHER!
def add_book(book_list):
    print("-- Add a book --")
    isbn = str(input("Enter the 13 digit ISBN (format 999-9999999999) "))
    title = str(input("Enter the title of the book: "))
    author = str(input("Enter the author of the book: "))
    genre = int(input("Enter the genre of the book (0-9): "))
    availability = True
    new_book = book.Book(isbn, title, author, genre, availability)
    book_list.append(new_book)
    print("Book has been added to the catalog")

#REMOVE THE BOOKS FROM THE LIST~!
def remove_book(book_list):
    print("-- Remove a book --")
    find_book_by_isbn = str(input("Enter the 13 digit ISBN (format 999-9999999999) "))
    index = 0 
    while index < len(book_list):
        current_book = book_list[index]
        if find_book_by_isbn == str(current_book.get_isbn()):
            book_list.remove(current_book)
            print("Book has been removed from the catalog")
            return

        index += 1 
    
    print("No book found with that ISBN")

#PRINTS ALL THE BOOKS IN THE LIST~! checks the list and prints out the books in the list
def print_book(book_list):
    print("\n-- Book Catalog --")
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title",
        "Author", "Genre", "Availability"))
    for b in book_list:
        print(b)

def main():
    book_list = load_books()


    while True:
        selection = print_menu()
        if selection == 1:
            check_book(book_list)
        elif selection == 2:
            borrow_book(book_list)
        elif selection == 3:
            return_book(book_list)
        elif selection == 0:
            print("Exiting the system ...")
            return
        elif selection == 2130:
            selection = print_menu_librian()

            if selection == 1:
                check_book(book_list)
            elif selection == 2:
                borrow_book(book_list)
            elif selection == 3:
                return_book(book_list)
            elif selection == 4:
                add_book(book_list)
            elif selection == 5:
                remove_book(book_list)
            elif selection == 6:
                print_book(book_list)
            elif selection == 0:
                print("Exiting the system ...")
                return
        
      

main()    