from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from auth import oauth2_scheme, decode_access_token

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the app!"}

@app.get("/protected/")
def protected_route(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(User).filter(User.id == payload.get("id")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "You are authorized!", "user": user.email}
