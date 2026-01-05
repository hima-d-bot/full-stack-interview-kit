from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "open"

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Label(BaseModel):
    id: int
    name: str
    color: str

class Activity(BaseModel):
    id: int
    task_id: int
    action: str
    timestamp: datetime
