# Official Python image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the necessary ports for Uvicorn and Streamlit
EXPOSE 8000 8501

# Entry point script
ENTRYPOINT ["./entrypoint.sh"]