from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config import engine, Base, get_db
from models import Task
from schemas import TaskCreate, TaskResponse

# Initialize FastAPI application
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        owner_name=task.owner.name,
        owner_email=task.owner.email,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.get("/tasks/", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
