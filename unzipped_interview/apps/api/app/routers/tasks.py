from fastapi import APIRouter, Query
from typing import Optional
from app.repos.tasks_repo import TasksRepo

router = APIRouter()
repo = TasksRepo()

@router.get("/tasks")
def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = None
):
    skip = (page - 1) * limit
    tasks, total = repo.get_all(skip=skip, limit=limit, status=status)
    
    # BUG: Integration mismatch - returning 'items' instead of 'data'
    # Also not using the schema to allow for this mismatch to happen
    return {
        "items": tasks,
        "total": total,
        "page": page,
        "limit": limit
    }
