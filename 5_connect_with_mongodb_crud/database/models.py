from pydantic import BaseModel 
from datetime import datetime 

# define tod p class which inherient base model 

class Todo(BaseModel) : 
    title : str 
    description : str 
    is_completed : bool = False 
    is_delated : bool = False 
    updated_at : int = int(datetime.timestamp(datetime.now())) 
    creation : int = int(datetime.timestamp(datetime.now()))