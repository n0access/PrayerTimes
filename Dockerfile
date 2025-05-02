# Use an official Python runtime as the base image
FROM python:3.12-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container
COPY . /app
# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 8080 for HTTP server
EXPOSE 8080
# Install an HTTP server and dependencies
RUN pip install Flask
# Create a simple HTTP server to serve the prayer_times.yaml file
COPY app.py /app/app.py
# Run the app.py script
CMD ["python", "app.py"]