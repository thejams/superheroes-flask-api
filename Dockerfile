# We Use an official Python runtime as a parent image
FROM python:3.7-alpine

# Set the working directory to /flask-superhero-api
WORKDIR /flask-superhero-api

# set environment variables

# FLASK_APP environment variable is used to specify how to load the application.
ENV FLASK_APP=app.py

# FLASK_RUN is used to execute flask with specific environemtn variables.

# HOST environment variable is used to specify the host where the app will run
ENV FLASK_RUN_HOST=0.0.0.0

# PORT environment variable is used to specify the port where the app will run
ENV FLASK_RUN_PORT=6000

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 6000 in the container
EXPOSE 6000

# Run proyect
CMD ["flask", "run"]