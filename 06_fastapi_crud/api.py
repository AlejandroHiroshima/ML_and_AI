from fastapi import FastAPI
from data_processing import library_data, Book

library = library_data("library.json")

books: list[Book] = library.books

app = FastAPI()

@app.get("/books")
async def read_books():
    return books

@app.get("/book/{id}")
async def read_book_by_id(id: int):
    return [book for book in books if book.id == id]

@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)
    return new_book

@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] = updated_book

    return updated_book

@app.delete("/books/delete_book/{id}")
async def update_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            break
            
    