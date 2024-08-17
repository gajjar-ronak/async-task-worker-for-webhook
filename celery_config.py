from celery import Celery

celery = Celery(
    "bigcommerce_tasks",
    broker="redis://localhost:6379/0",  # Replace with your broker URL
    backend="redis://localhost:6379/0",  # Replace with backend URL
)