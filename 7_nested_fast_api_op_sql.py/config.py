# config.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL
DATABASE_URL =  "postgresql://postgres:9595946682@localhost/chat_db"   # Update with your credentials

# Create the engine to connect to the database
engine = create_engine(DATABASE_URL)

# Create the sessionmaker for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your models
Base = declarative_base()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
