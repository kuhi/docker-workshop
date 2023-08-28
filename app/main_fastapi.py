import json

from fastapi import FastAPI

from .config import settings
from .db import connect, query_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the bookstore!"}


@app.get("/book/")
async def book(name: str = None, year: int = None, author: str = None, limit: int = 100):
    conn = connect(
        database=settings.database,
        host=settings.host,
        port=settings.port,
        user=settings.user,
        password=settings.password
    )
    result = query_db(
        conn,
        settings.db_schema,
        "book",
        ("name", "author", "year"),
        name=name,
        year=year,
        author=author,
        limit=limit
    )
    return json.dumps(result)


@app.get("/db_info/")
def db_info():
    try:
        connect(
            database=settings.database,
            host=settings.host,
            port=settings.port,
            user=settings.user,
            password=settings.password
        )
        return {"message": f"Connected to {settings.host}:{settings.port}/{settings.database}. User: {settings.user}."}
    except Exception() as e:
        return {"message":
                f"{str(e)} {settings.host}:{settings.port}/{settings.database}. User: {settings.user}."}
