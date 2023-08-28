# Docker Workshop

## 2023-06-23, Brno

This is a very poorly documented project, pretty much a copy-pasted notebook.  
This is so sad.  
It doesn't even have a `requirements.txt` file.

### What can we do?
1. Create a virtual environment locally using Python 3.10.
2. Investigate any `.py` files and install required packages.
3. `pip freeze > requirements.txt` and you're halfway there. 
4. Create a `Dockerfile`, you may use [this](https://mtr.devops.telekom.de/repository/ai_incubator/python3.10) image.

### Where's the catch?
Without modifying the code, you will not be able to "test" it locally, since
it relies on a database connection with pre-existing schema and data.

### Creating a database and loading data
1. Log into your databse using the deployed pgAdmin (in browser).
2. Run database.sql, book.sql, database.sql in a/an (depending on your pronunciation of SQL)
sql window (in that order).


