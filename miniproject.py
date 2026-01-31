import os

print("""
 11. Mini Project 🎯
**Console Book Manager**
""")

book_list = "book_list.txt"
def addBook():
    book = input("Adding a book\nEnter book name: ")
    try:
        if os.path.exists(book_list):
            content = readBook()
            with open(book_list, 'a') as file:
                if content != '':
                    file.write('\n' + book)
                else:
                    file.write(book)
        else:
            with open(book_list, 'w') as file:
                file.write(book)
    except Exception as e: 
        print(e)

def readBook():
    try:
        if os.path.exists(book_list):
            with open(book_list, 'r') as file:
               return file.read() 
        else:
            return 'Empty List' 
           
    except Exception as e:
        print(e)

def deleteBook():
    print("**Deleting a Book")
    book = input("Enter Book Name: ")
    try: 
        if not os.path.exists(book_list):
            print("No book list found")
            return

        with open(book_list, 'r') as file:
            books = file.read().splitlines()

        if not book in books:
            print("Book not found")
            return

        books.remove(book)

        with open(book_list, 'w') as file:
            file.write('\n'.join(books))

        print("Book " + book + " deleted")
    except Exception as e:
        print(e)


while True:
    print("\nlist of books:\n")
    print(readBook())
    num = int(input("""
Enter a number to use:
1 Add a book
2 List all books
3 Delete a book
0 Exit
Enter a number: """))

    if num > 3 or num < 0:
        print("Invalid number selected")

    if num == 0:
        print("Thank you for using my book list application")
        break  
    if num == 1: 
        addBook()
    if num == 2:
        print("\nlist of books:\n")
        print(readBook())
        print("\n")
    if num == 3:
        deleteBook()
