from fastapi import APIRouter
from models import Task  # Import the Task model

router = APIRouter()

# Mock database
tasks = []

@router.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task created successfully", "task": task}

@router.get("/tasks/")
async def get_tasks():
    return tasks
