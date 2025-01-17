# official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

# Copy the current directory contents into the container
COPY src/ /app
COPY requirements.txt /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 3000

# Run the Flask server
CMD ["python", "server_v2.py"]
