# Start from a Python image
FROM python:3.8-slim

# Set environment variables for pip
ENV PIP_DEFAULT_TIMEOUT=120 \
    PIP_DEFAULT_RETRIES=3

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir ultralytics \
    && pip install --no-cache-dir flask

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "flask_PPE.py"]
