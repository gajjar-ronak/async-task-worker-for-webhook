# Async Task Worker with FastAPI and Celery

![Async Task Worker](https://github.com/user-attachments/assets/a3e25004-a425-4d23-bf2e-18fd3a3fba4f)


This project sets up a simple asynchronous task worker using FastAPI, Celery, and Redis. It processes webhooks from any e-commerce store using a background task.

## Prerequisites

- Docker and Docker Compose
- Python 3.x (for local development)
- Redis (used as the broker and backend for Celery)

## Project Structure

- `app.py`: FastAPI application with webhook endpoint.
- `routes/webhook.py`: Router for handling webhook events.
- `worker.py`: Celery worker configuration and task definitions.
- `celery_config.py`: Celery configuration.
- `Dockerfile`: Dockerfile for building the FastAPI and Celery image.
- `docker-compose.yml`: Docker Compose configuration for orchestrating the services.

## Setup and Installation

### Local Development

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server**

   To run the FastAPI server locally:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

   If port `8000` is in use, specify a different port:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8001
   ```

5. **Run the Celery Worker**

   In a new terminal window or tab, run the Celery worker:

   ```bash
   celery -A worker.celery worker --loglevel=info
   ```

6. **Send Test Webhooks**

   Use [Postman](https://www.postman.com/) or `curl` to send a POST request to the webhook endpoint:

   ```bash
   curl -X POST http://localhost:8000/webhook \
   -H "Content-Type: application/json" \
   -d '{"scope": "store/product/created", "data": {"id": 1234, "name": "Sample Order"}}'
   ```

### Using Docker

1. **Build and Start Containers**

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the FastAPI server, Celery worker, and Redis container.

2. **Stopping Containers**

   To stop and remove the containers:

   ```bash
   docker-compose down
   ```

3. **Accessing the Application**

   - **FastAPI Server:** `http://localhost:8000/webhook`
   - **Redis:** Exposed on port `6379` (not directly accessed for this project)

## Troubleshooting

1. **Port Already in Use**

   If you see the error `[Errno 48] error while attempting to bind on address ('0.0.0.0', 8000): address already in use`, follow these steps:

   - **Find and Stop the Process Using the Port:**

     - **macOS/Linux:**

       ```bash
       lsof -i :8000
       kill -9 <PID>
       ```

     - **Windows:**

       ```bash
       netstat -ano | findstr :8000
       taskkill /PID <PID> /F
       ```

   - **Change the Port Number:**

     Run the FastAPI server on a different port:

     ```bash
     uvicorn app:app --host 0.0.0.0 --port 8001
     ```

2. **Docker Container Issues**

   - **Check Container Logs:**

     ```bash
     docker-compose logs <service_name>
     ```

   - **Rebuild and Restart:**

     ```bash
     docker-compose down
     docker-compose up --build
     ```

## Project Structure

- **`app.py`**: Contains FastAPI application code and route definitions.
- **`routes/webhook.py`**: Handles webhook events and processing.
- **`worker.py`**: Defines Celery tasks and configuration.
- **`celery_config.py`**: Defines Celery configuration.
- **`Dockerfile`**: Defines the Docker image build process.
- **`docker-compose.yml`**: Configures and orchestrates the Docker services.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
