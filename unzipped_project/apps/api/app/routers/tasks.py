from fastapi import APIRouter, Depends
from app.schemas import Task, TaskCreate
from app.repos.tasks_repo import TasksRepo

router = APIRouter()
repo = TasksRepo()

@router.get("/", response_model=dict)
def get_tasks(skip: int = 0, limit: int = 10):
    items = repo.get_all(skip=skip, limit=limit)
    # BUG: Contract mismatch - frontend expects 'data', backend returns 'items'
    return {"items": items, "total": len(repo.tasks)}
