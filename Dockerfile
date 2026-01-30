# Use an official lightweight Python image
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (optimizes caching during rebuilds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

# Copy the rest of the application code and model
COPY . .

# Expose the port Flask will run on
EXPOSE 8080

# Use gunicorn for production
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT} app:app"]