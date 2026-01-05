from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

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

class PaginatedTasks(BaseModel):
    data: List[Task]
    total: int
    page: int
    limit: int

class SuggestionRequest(BaseModel):
    query: str

class SuggestionResponse(BaseModel):
    suggestions: List[Task]
    operations: int
