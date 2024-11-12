from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# This is code which connect our data base cluster with our app 


uri = "mongodb+srv://jayraj:9595946682@cluster0.oleve.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db =client.todo_db 

collection = db["todo_data"] 