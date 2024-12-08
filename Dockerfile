# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn server
CMD ["uvicorn", "fastapi_user_management.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
