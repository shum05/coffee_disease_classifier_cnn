# set the base image for Docker container(based on the official Python 3.9 image with a slim version of Debian (Buster).) 
FROM python:3.9-slim-buster
# updates the package index and install awscli
RUN apt update -y && apt install awscli -y

#  set the working directory inside the Docker container to /app.
WORKDIR /app
# copy the contents of your current directory into app dir in docker
COPY . /app

RUN pip install -r requirements.txt
#  Python script app.py should be executed when the container starts
CMD ["python3", "app.py"]