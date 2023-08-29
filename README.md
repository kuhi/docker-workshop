# Docker Workshop: Exercise 2

## Solution
1. First you need to create a Dockerfile. This Dockerfile is very similar to the one you created in the first exercise.
2. You need to figure out what dependencies there are and put them in the `requirements.txt` file.

-------------

## Assignment
This is a very poorly documented project, pretty much a copy-pasted notebook.  
This is so sad.  
It doesn't even have a `requirements.txt` file.

1. Create a virtual environment locally using Python 3.10.
2. Investigate any `.py` files and install required packages.
3. `pip freeze > requirements.txt` and you're halfway there. 
4. Create a `Dockerfile` to dockerize your application.
5. Run the following command to build and start all containers in the project. **You can re-run this command each time you make some changes to apply them**.
   ```bash
   docker compose up --build -d
   ```
   * Docker Compose an orchestration tool to automate building, running and connecting containers together. It is out of scope of this workshop, but we encourage you to [read its documentation](https://docs.docker.com/compose/gettingstarted/).
   * `docker compose up` starts all the containers defined in the `compose.yml` file
   * `--build` always builds your containers first
   * `-d` starts runs the whole process on background
6. When you're done, you can stop all containers using the following command:
   ```bash
   docker compose stop
   ```


### Where's the catch?
Without modifying the code, you will not be able to "test" it locally, since
it relies on a database connection with pre-existing schema and data.

### Creating a database and loading data
1. Log into your databse using the deployed pgAdmin (in browser).
2. Run database.sql, book.sql, database.sql in a/an (depending on your pronunciation of SQL)
sql window (in that order).


