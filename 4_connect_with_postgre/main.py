from fastapi import FastAPI ,Depends ,HTTPException
from sqlalchemy.orm import Session 
from schemas import UserCreate 
from crud import *
from database import *

app = FastAPI() 

Base.metadata.create_all(bind= engine) 


def get_db(): 
    db = SessionLocal() 
    try :
        yield db 
    finally:
        db.close() 
        
        

@app.post("/user/create") 
async def create_user_api(user:UserCreate , db:Session=Depends(get_db)) : 
    return create_user(db , user)
    

#to detect data we make a api then go to crud 

@app.get("/users/{user_id}") 
async def read_user_api(user_id:int, db:Session=Depends(get_db)) :
    db_user =  read_user(db , user_id) 
    if db_user is None :
        raise HTTPException(status_code=404 , detail="Sorry User is not found...") 
    
    return db_user  


# Update Key    
@app.post("/user/upadte") 
async def update_user_api(user_id:int ,user:UserCreate, db:Session=Depends(get_db)) :
    db_user = update_user(db , user_id, user)
    
    if db_user is None :
        raise HTTPException(status_code=404 , detail="Sorry User is not found...") 
    
    return db_user   


# delete Opration 

@app.post("/user/delate") 
async def delete_user_api(user_id:int, db:Session=Depends(get_db)) :
    db_user=delete_user(db ,user_id) 
    
    if db_user is None :
        raise HTTPException(status_code=404 , detail="Sorry User is not found...") 
    
    return db_user 
