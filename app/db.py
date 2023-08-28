import psycopg2
from psycopg2 import extras, sql

DEFAULT_FIELDS = ("name", "year", "author")


def connect(database, host, user, password, port):
    conn = psycopg2.connect(database=database,
                            host=host,
                            user=user,
                            password=password,
                            port=port)
    return conn


def query_db(conn, schema, table, select_fields=DEFAULT_FIELDS, name=None, year=None, author=None, limit=100):
    # Nightmare code, originally I wanted this whole thing to be a lambda (sunglasses emoji)
    with conn.cursor(cursor_factory=extras.DictCursor) as cur:
        query = sql.Composed([
            sql.SQL("SELECT "),
            sql.SQL(", ").join(sql.Identifier(field) for field in select_fields),
            sql.SQL(f" FROM "),  sql.Identifier(schema), sql.SQL("."), sql.Identifier(table),
            sql.SQL(f" WHERE "), sql.Identifier('name'), sql.SQL("="), sql.SQL('COALESCE(%s, name) '),
            sql.SQL(f"AND "), sql.Identifier('year'), sql.SQL("="), sql.SQL('COALESCE(%s, year) '),
            sql.SQL(f"AND "), sql.Identifier('author'), sql.SQL("="), sql.SQL('COALESCE(%s, author) '),
            sql.SQL("LIMIT "),
            sql.Literal(limit)
        ])
        cur.execute(query, (name, year, author))
        result = cur.fetchall()
    return result
