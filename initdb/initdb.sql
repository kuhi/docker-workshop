CREATE SCHEMA IF NOT EXISTS bookstore;

CREATE TABLE IF NOT EXISTS bookstore.book (
    id serial primary key,
    name text not null,
    year int not null,
    author text not null
);

INSERT INTO bookstore.book
    (name, author, year)
VALUES
    ('Terry Pratchett, Otec prasátek', 'Bill Kaye, Stephen Player', 2007),
    ('TERRY PRATCHETT DISCWORLD NOVEL COLLECTION.', 'TERRY. PRATCHETT', 2012),
    ('Terry Pratchett''s Discworld Coloring Book', 'Terry Pratchett', 2017),
    ('Sourcery', 'Terry Pratchett', 2014),
    ('Dodger', 'Terry Pratchett', 2019),
    ('Seriously Funny', 'Terry Pratchett', 2016),
    ('Nation', 'Terry Pratchett', 2009),
    ('The Carpet People', 'Terry Pratchett', 2015),
    ('Truckers', 'Terry Pratchett', 2015),
    ('Sekáč', 'Terry Pratchett, Jan Kantůrek', 2011);
