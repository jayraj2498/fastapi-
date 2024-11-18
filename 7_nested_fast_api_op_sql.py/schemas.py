from pydantic import BaseModel, EmailStr

# Nested Owner Schema
class Owner(BaseModel):
    name: str
    email: EmailStr

# Task Schema
class TaskCreate(BaseModel):
    title: str
    description: str
    is_completed: bool
    owner: Owner

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    owner_name: str
    owner_email: str

    class Config:
        orm_mode = True
