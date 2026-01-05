from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from app.schemas import Task, TaskCreate
from app.repos.tasks_repo import TasksRepo

router = APIRouter()
repo = TasksRepo()

@router.get("/")
def list_tasks(skip: int = 0, limit: int = 10, status: Optional[str] = None):
    items = repo.get_all(skip=skip, limit=limit, status=status)
    return {"items": items, "total": len(repo.tasks), "page": (skip // limit) + 1}

@router.post("/", status_code=201)
def create_task(task: TaskCreate):
    return repo.create(task.dict())

@router.get("/{task_id}")
def get_task(task_id: int):
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    updated = repo.update(task_id, task.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}")
def delete_task(task_id: int):
    if not repo.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "deleted"}
