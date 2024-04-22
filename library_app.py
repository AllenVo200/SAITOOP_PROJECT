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
            book_list.append(book.Book(line[0], line[1], line[2], int(line[3]), bool(line[4])))

    
            
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
    while selection > (3):
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
                print("Found a match... :", current_book.__str__())
        index += 1
    

def main():
    book_list = load_books()

    print_menu()
   
    check_book(book_list)
   

main()    