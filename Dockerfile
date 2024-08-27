# Use an official Python runtime as a parent image
FROM python:3.9.5-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt /usr/src/app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /usr/src/app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run on container start
CMD ["gunicorn", "--workers=3", "secure_django.wsgi:application"]
