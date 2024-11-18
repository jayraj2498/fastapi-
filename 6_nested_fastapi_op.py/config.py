from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection URI (replace with your actual credentials)
MONGO_URI = "mongodb+srv://jayraj:9595946682@cluster0.oleve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a MongoDB client
client = MongoClient(MONGO_URI, server_api=ServerApi("1"))

# Access your database
db = client.todo_db

# Access your collection
collection = db["todo_data"]
