# Docker Workshop: Exercise 1

### Assignment
Dockerize a simple Python application.

1. Create a virtual environment locally using Python and install pip dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   ```
2. Run the aplication locally using the following command:
    ```bash
    uvicorn app.main:app --host "0.0.0.0" --port 8000
    ```
3. Create a file called `Dockerfile` to dockerize the application.
   ```
   touch Dockerfile
   ```
4. Open the `Dockerfile` and update it to dockerize the application. Feel free to inspire by the example Dockerfile from the presentation. Note that the command after `CMD` keyword is different. You need to use the command from step 2.
5. Build the application using the following command (don't forget the dot at the end!):
   ```bash
   docker build -t docker-workshop:app1 .
   ```
6. Run the application using thw following command:
   ```bash
   docker run --rm -p 8000:8000 docker-workshop:app1
   ```
   * `docker run` start the application in a container
   * `--rm` delete the container after it is stopped
   * `-p` expose the port 8000 to the host machine
   * `workshop:app1` use the image `workshop` with tag `app1` as the blueprint for container

### Common problems
In the Docker Lab you can get an error "No space left on the device". This can be usually fixed by using the slim version of Docker image (`python:3.11-slim`) and running the following command:
```bash
docker system prune --all
```