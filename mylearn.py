import json

import getpass

Books = []

mylearning = "Books.json"

def Add_book():
    title =input("Enter the title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")
    genre = input("Enter the Genre: ")
    
    books = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "genre": genre
    }
    Books.append(books)
    save_books_to_file()
    print("Books succesfully added")
    
def update_book():
    title = input("Enter the book to be updated: ")
    for books in Books:
        if books["title"] == title:
            print("book found, enter your update")
            books["title"] = input("update the title of the books: ")
            books["author"] = input("update the author of the book: ")
            books["isbn"] =  input("update book isbn: ")
            books["genre"] =input("update the book genre: ")
            save_books_to_file()
            print("book successfully updated")
            return
    print("book not found!")
    
def Delete_book():
    title = input("Enter the book title to be deleted: ")
    for books in Books:
        if books["title"] == title:
            print("book found!")
            del books["title"]
            print("book successfully deleted!")
    print("book not found")
    
def search_book():
    keyword = input("Enter the keyword to search: ")
    found_books = []
    for books in Books:
        if keyword.lower() in books['title'].lower() or keyword.lower() in books['author'].lower() or keyword.lower() in books['isbn'].lower() or keyword.lower() in books['genre'].lower():
            found_books.append(books)
            
            
        if found_books:
            display_books(found_books)
            print("this is the found list")
        else:
            print("no such keyword!")
    
    
    
def display_books(book_list=None):
    if not book_list:
        book_list = Books
    print("books list")
        
    for books in book_list:
        print("Title-", books['title'])
        print("author-", books['author'])
        print("isbn-", books['isbn'])
        print("genre-", books['genre'])
        print("")
            
            
def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    for books in Books:
        if books["title"] == title:
            if books.get('borrower'):
                print("sorry, book is already borrowed. ")
            else:
                borrower_Name = input("Enter the borrower name: ")
                books["borrower"] = borrower_Name
                save_books_to_file()
                print("Book successfully borrowed")
            return
    print("book not found")

def return_book():
    title = input("Enter the title of the book that was borrowed: ")
    for books in Books:
        if books["title"] ==title:
            if books.get('borrower'):
                borrower_Name = books["borrower"]
                del books['borrower']
                print("Book successfully borrowed.")
                print("borrower",Delete_book)
            else:
                print("Book is not currently borrowed")
    print("book not found")
def generate_report():
    print("^^^^^^REPOTR^^^^^^^")
    print("1. The total number of books")
    print("2. The number of genre")
    print("3. Return to the menu")
    print()
    print()
    
    
    choice = input("Enter the chioce from (1-3): ")
    
    if choice =='1':
        total_book = len(Books)
        print("The total number of books is", total_book)
    elif choice == '2':
        genre_count = {}
        if Books in Books:
            genre_count = Books["genre"]
            genre_count[genre] = genre_count.get(genre, 0) + 1
        print("print number of genre in genre")
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")
    elif choice =="3":
        return
    else:
        print("invalid chioce, please enter again")
    
    print()
    generate_report()     # Recursively call the function to generate more reports if desired
        
def display_menu():
    print("^^^^^MENU^^^^^^^")
    print("1. add a book")
    print("2. search a book")
    print("3. update")
    print("4. Delete a book")
    print("5. Borrow book ")
    print("6. return book")
    print("7. generate report ")
    print("8. registration ")
    print("9. logout")
    print("10. reset passward ")
    print("11. exite page")    
def handle_user_choice():
    print("Make a choice here")
    while True:
        #display_menu()  this make the dispay_menu up to print again
        choice =input("Make a chioce from (1-11): ")
        
        if choice == '1':
            Add_book()
        elif choice == '2':
            search_book()
            
        elif choice == '3':
            update_book()
            
        elif choice == '4':
            Delete_book()
        elif choice =='5':
            borrow_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            generate_report()
        elif choice == '8':
            register_user()
        elif choice == '9':
            current_user = None
            print(" logout successful")
            
            break
        elif choice =='10':
            reset_passward()
        elif choice == '11':
            save_books_to_file()
            print("Exiting the application")
            break
        else:
            print("invalid choice, please enter choice again")
            
             
        
def save_books_to_file():
    with open(mylearning, "w") as file:
        json.dump(Books, file, indent=4)
    print("book successfully save")
    
def load_book_from_file():
    global Books
    try:
        with open(mylearning, 'r') as file:
            Books = json.load(file)
        print("books succesfully loaded from file.")
    except FileNotFoundError:
        print("No such existing file found, with an empty books list: ")  
        
            
  # the variable to store the list of users information           
users =[]


#   global variable to store user login user 
current_user= None

# global variable to store the list of books

Books = []
       
def save_users_to_file():
    with open("users.json","w") as file:
        json.dump(users, file, indent=4)   
    print("user successfully save")
    
def load_users_from_file():
    global users  # this global means it json should store all the users perminently even when the has been corupted
                  #an if you dont incude the global, anytime you run the cmd is corupted all the user will not active again
    try:
        with open("users.json", "r") as file:
            users = json.load(file) 
        print("user file successfully loaded")
    except FileNotFoundError:
        print("user file not found")
        
def register_user():
    username = input("Enter your user name")
    passward = input("Enter your passward")
    
    user = {
        "username": username,
        "passward": passward
    }
    users.append(user)
    save_users_to_file()
    print("user succesfully added")
    
def login():
    global current_user
    username = input("Enter your user name")
    passward = getpass.getpass("Enter your passward")
    
    for user in users:
        if user["username"] == username and passward == passward:    
            print("user login succesful")
            current_user = user
            return
        
        
    print("invalid passward or username")
    
def reset_passward():
    global users
    
    username = input("Enter your user name")
    
    passward =input("Enter you old passward: ")
    for user in users:
        if user["username"]==username:
            new_username = input("Enter you new username")
            if user["passward"] != passward:
                print("enter the right passward")
            else:
                new_passward = input("new passward")
                return new_passward
            save_users_to_file()
            print("passward succesfully created") 
            return
               
    print("user not found")
    
if __name__ == "__main__":
    load_users_from_file()
    load_book_from_file()
    while current_user is None:
        print("^^^^^^^^^USER MENU CRITERIALS^^^^^^^^")
        print("1. register")
        print("2. login")
        print("3. reset passward")
        print("4. logout")  
        
        choice = input("Enter your choice from (1-4)")
        if choice == '1':
            register_user()
        elif choice == '2':
            login()
        elif choice == '3':
            reset_passward()
        elif choice == '4':
            print("exiting the program")
            break
        else:
            print("invalid choice, please enter again")
            
    if current_user is not None:
        display_menu()
        
        
def main():
    load_book_from_file()
    handle_user_choice()
    
if __name__ == "__main__":
    main()
            

