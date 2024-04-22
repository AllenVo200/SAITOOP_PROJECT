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
    book_list = open(file_name, "r")
    return book_list

#prints out the menu for the user to choose from returns the users selection
def print_menu():
    print("\nReader's Guild Library - Main Menu")
    print("==================================")
    print("1. Search for books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("0. Exit the system")
    selection = input("enter your selection: ")
    return selection

#searches for the book in the list and returns the book if found
def check_book(book_list):
    print("-- Search for books --")
    index = 0
    search_value = input("Enter a search value:")
    while index < len(book_list):
        current_book = book_list[index]
        if search_value.lower() in current_book.get_title().lower():
            print("Found a match... Title:", current_book.get_title(),
                   ", ISBN:", current_book.get_isbn())
        index += 1
    

def main():
    load_books()

    print_menu()
   
    check_book()

main()    