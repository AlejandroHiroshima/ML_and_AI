from fastapi import FastAPI
from data_processing import library_data

library = library_data("library.json")
books = library.books

app = FastAPI()

@app.get("/books")
async def read_books():
    return books

