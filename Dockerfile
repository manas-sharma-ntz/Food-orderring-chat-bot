# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable to indicate that we're in a container
# ENV FLASK_ENV=production

# Specify the command to run the Flask application
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000" ,"main:app"]
  
