# Docker Workshop: Exercise 1

### Solution
The only file you have to create is the `Dockerfile`. It contains the necessary commands to use a Python image, copy the files, install pip dependencies and finally run the application.

Notice that we used the `FROM python:3.11-slim-bookworm` to use a smaller up-to-date Docker image instead of `python:3.9`.
* `python:3.11` is an image with Python 3.11 installed
* `-bookworm` stands for the latest Debian Linux distribution version 12 called Bookworm.
* `-slim` is a slimmed-down version of of the image. Usually it has ~10-20% size of the full version, but might have some system packages missing. You can always install them using the `apt` command in the Dockerfile.


### Assignment
Dockerize a simple Python application. Feel free to inspire by the example Dockerfile from the presentation.

1. Create a virtual environment locally using Python 3.9 or higher.
2. Run the aplication locally using the following command:
    ```bash
    uvicorn app.main:app --host "0.0.0.0" --port 8000
    ```
3. Create a Dockerfile to dockerize the application.
4. Build the application using the following command (don't forget the dot at the end!):
   ```bash
   docker build -t docker-workshop:app1 .
   ```
5. Run the application using thw following command:
   ```bash
   docker run --rm -p 8000:8000 workshop:app1
   ```
   * `docker run` start the application in a container
   * `--rm` delete the container after it is stopped
   * `-p` expose the port 8000 to the host machine
   * `workshop:app1` use the image `workshop` with tag `app1` as the blueprint for container


