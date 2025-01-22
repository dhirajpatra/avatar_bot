# Use an official Python image
FROM python:3.9-buster

# Set the working directory
WORKDIR /app

# Install system dependencies, including OpenGL libraries
RUN apt-get update && apt-get install -y \
    freeglut3 \
    freeglut3-dev \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libglu1-mesa \
    libglu1-mesa-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
