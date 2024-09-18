# Pull base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 and run Django
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
