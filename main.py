from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Book(BaseModel):
    title: str
    description: str | None = None
    author: str


book_list = [
        {
         "title": "sample",
         "description": "sample desc",
         "author": "sample author",
         },
        {
         "title": "sample 2",
         "description": "sample desc",
         "author": "sample author",
         }
        ]
app = FastAPI()

## 20. Simple API Project 🎯
#**Book API (In-Memory)**
#- Add books
#- List books
#- Get book by ID
#- Return proper error messages


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
async def create_item(item: Item):
    item.name = item.name.capitalize()
    return item 


@app.post("/books")
async def add_book(book: Book):
    book_list.append(book)
    return book_list 


@app.delete("/books")
async def delete_book(title: str):
    index = 0
    for book in book_list:
        if book.title == title:
            book_list.pop(index) 
        else:
            index = index + 1

    return book_list 

@app.put("/books")
async def update_book(title: str, updated_book: Book):
    try:
        for index, book in enumerate(book_list):
            if book['title'] == title:
                book_list[index] = updated_book.model_dump() 
                return book_list 

        return {"error": "Book not found"}
    
    except Exception as e:
        print(e)


