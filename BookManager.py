import json
class Book:
    def __init__(self, title, description, author):
        if not title or not  description or not author:
            raise ValueError("All fields are required")

        self.title = title
        self.description = description
        self.author = author

class BookManager:
    def __init__(self, filename="book_list.json"):
        self.filename = filename
        self.book = {}
        self.load_books()

    def load_books(): 
        try:
            with open(self.filename, "r") as file:
                books = json.load(file)
        except Exception as e:
            self.books = {}


