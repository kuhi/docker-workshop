import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database = os.getenv("POSTGRES_DB", "book")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", 5432)
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "default")
    db_schema = os.getenv("POSTGRES_SCHEMA", "bookstore")


settings = Settings()
