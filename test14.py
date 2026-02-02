print("""
### 14. Classes (Basics)
- Create a class
- Use `__init__`
- Create objects
- Store and access object data
""")

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class BookManager:
    def __init__(self, filename="book_list.json"):
        self.filename = filename
        self.book = []
        self.load_books()

    def:




