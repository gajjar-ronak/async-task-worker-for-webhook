from fastapi import FastAPI
from routes import webhook  # Import router

app = FastAPI()

# Include the router in the app
app.include_router(webhook.router)