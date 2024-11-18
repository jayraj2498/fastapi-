from fastapi import FastAPI , APIRouter, HTTPException 
from configrations import collection 
from database.schemas import all_tasks 
from database.models import Todo 
from bson.objectid import ObjectId 
from datetime import datetime

app= FastAPI() 

router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find({"$or": [{"is_deleted": False}, {"is_deleted": {"$exists": False}}]})
    return all_tasks(data)


# Insert the data 
@router.post("/")
async def create_task(new_task:Todo):
    try :
        resp = collection.insert_one(dict(new_task)) 
        return {"staus_code":200 , "id":str(resp.inserted_id)}

    except Exception as e:
        return HTTPException(status_code=500 , detail= f"Error occur is:{e}")
        
        
# update opration 
@router.put("/")
async def update_task(task_id:str  , updated_task:Todo) : 
    try :
        id = ObjectId(task_id)

        # Fetch the existing document
        existing_doc = collection.find_one({"_id": id})

        # Check if the document exists
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")

        # Update the timestamp and other fields
        updated_task_data = dict(updated_task)
        updated_task_data["updated_at"] = int(datetime.timestamp(datetime.now()))

        # Update the document in MongoDB
        resp = collection.update_one({"_id": id}, {"$set": updated_task_data})

        if resp.modified_count == 1:
            return {"status_code": 200, "message": "Task updated successfully"}
        else:
            return {"status_code": 304, "message": "No changes made"}
    
    except Exception as e:
        return HTTPException(status_code=500 , detail= f"Error occur is:{e}")
        





# delete  opration  

# Delete operation
@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        # Convert task_id to ObjectId
        id = ObjectId(task_id)

        # Fetch the existing document without the "is_deleted" condition
        existing_doc = collection.find_one({"_id": id})

        # Check if the document exists
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")

        # Mark the task as deleted
        resp = collection.update_one({"_id": id}, {"$set": {"is_deleted": True}})

        if resp.modified_count == 1:
            return {"status_code": 200, "message": "Task deleted successfully"}
        else:
            return {"status_code": 304, "message": "No changes made"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")   


app.include_router(router)



# jayrajds6699 : zWuMBMonB1cQqXV8