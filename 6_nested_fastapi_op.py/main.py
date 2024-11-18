from fastapi import FastAPI
from routes import router  # Import the router

app = FastAPI()

# Include the router
app.include_router(router)
