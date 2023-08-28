CREATE TABLE IF NOT EXISTS bookstore.book (
    id serial primary key,
    name text not null,
    year int not null,
    author text not null
);
