# Docker Workshop: Exercise 2

## Assignment
This is a very poorly documented project, pretty much a copy-pasted notebook.  
This is so sad.  
It doesn't even have a `requirements.txt` file.

1. Create a virtual environment locally using Python and install the dependencies.
   ```bash
   python -m venv venv2
   source venv2/bin/activate 
   pip install -r requirements.txt
   ```
2. Investigate any `.py` files and install required packages. You can use the pip package called `pipreqs` to help you with this task. 
   * Don't forget the `uvicorn` dependency.
   * Use the `psycopg2-binary` to fix problems with `psycopg` library installation.
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

When you're done, you can stop all containers using the following command:
   ```bash
   docker compose stop
   ```

### Common problems
In the Docker Lab you can get an error "No space left on the device". This can be usually fixed by using the slim version of Docker image (`python:3.11-slim`) and running the following command:
```bash
docker system prune --all
```

## Where's the catch?
Without modifying the code, you will not be able to "test" it locally, since
it relies on a database connection with pre-existing schema and data.

## Creating a database and loading data
The Docker Compose configuration automatically creates and fills the database for you. After the Postgres database starts, it runs the `initdb/initdb.sql`, which creates a schema, a table and fills it with some data.


