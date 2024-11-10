from sqlalchemy.orm import Session 
from models import User 
from schemas import UserCreate

#TO create the user 
def create_user(db:Session , user:UserCreate): 
    db_user = User(name = user.name , email= user.email) 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user) 
    return db_user  

# to get data funt
def read_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# to updata data funt 
def update_user(db:Session , user_id:int , user:UserCreate) :
    db_user = db.query(User).filter(User.id == user_id).first() 
    if db_user is None:
        return None 
    
    # update only if db_user found 
    db_user.name = user.name 
    db_user.email = user.email 
    db.commit() 
    db.refresh(db_user)
    return db_user      

# To delete 
def delete_user(db:Session , user_id:int) :
    db_user= db.query(User).filter(User.id==user_id).first() 
    if not db_user :
        return "This User is not inside DataBase Plz check again"  
    
    db.delete(db_user)
    db.commit()
    return db_user
