from pydantic import BaseModel, EmailStr
from typing import Optional

# Nested model for Owner
class Owner(BaseModel):
    name: str
    email: EmailStr

# Main model for Task
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    owner: Owner
