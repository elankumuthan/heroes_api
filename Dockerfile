# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including the app directory)
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI from the `app` module
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
