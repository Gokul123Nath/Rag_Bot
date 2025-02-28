## RAG Application
### Overview
This application is designed to provide a user-friendly interface for uploading PDF documents, extracting text for use as the chatbot's knowledge base, and interacting with the chatbot. The application is containerized using Docker for easy deployment.

### Features
Document Upload API

API Endpoint: Create an API endpoint allowing users to upload PDF documents.

Text Extraction: Extract and process text from uploaded documents for use as the chatbot’s knowledge base.

### Chatbot API

Conversational Endpoint: Implement an API endpoint where users can submit questions, and the chatbot responds with answers based on the document content.

AI Models: Hugging face model - bigscience/bloom-1b7 has been used for generation (Sometimes model is too busy to interact)

### User Interface

Interface Design: Develop a basic, user-friendly interface that allows users to:

Upload PDF documents.

Interact with the chatbot.

Usability: Ensure the interface is simple, clear, and facilitates easy interaction with the chatbot.

### Deployment with Docker

Containerization: Write a Dockerfile to containerize the application for easy deployment.

Dependencies and Configuration: Ensure all dependencies and configurations are included in the Docker container.

### Getting Started
Prerequisites
Docker installed on your machine.
Python environment set up with necessary packages.

Build the Docker container:
    Command : docker build -t rag-application .

Run the docker container: 
    Command : docker run -p 8000:8000 -p 8501:8501 rag-application
