from fastapi import APIRouter, Query
from typing import Optional
from app.repos.tasks_repo import TasksRepo
from app.schemas import PaginatedTasks

router = APIRouter()
repo = TasksRepo()

@router.get("/tasks", response_model=PaginatedTasks)
def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    status: Optional[str] = None
):
    skip = (page - 1) * limit
    tasks, total = repo.get_all(skip=skip, limit=limit, status=status)
    return {
        "data": tasks,
        "total": total,
        "page": page,
        "limit": limit
    }
