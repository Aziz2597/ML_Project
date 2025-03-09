# Use FastAPI base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port
EXPOSE 5000

# Start FastAPI
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "5000"]
