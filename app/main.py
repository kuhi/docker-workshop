from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse(
        {
            "message": "Welcome to the bookstore! Open the /docs path to see the API documentation."
        }
    )


books = [
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"name": "The Trial", "author": "Franz Kafka", "year": 1925},
    {"name": "The Stranger", "author": "Albert Camus", "year": 1942},
]


@app.get("/book/")
async def book():
    return JSONResponse(books)
