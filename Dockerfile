# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production
RUN pip install --no-cache-dir gunicorn

# Copy the rest of the application
COPY . .

# Expose port (Render will set PORT env variable)
EXPOSE 5000

# Use gunicorn for production
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 app:app

