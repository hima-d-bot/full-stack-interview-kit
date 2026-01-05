from typing import List, Optional
from datetime import datetime
from app.schemas import Task

class TasksRepo:
    def __init__(self):
        self.tasks = [
            {"id": i, "title": f"Task {i}", "description": f"Description for {i}", "status": "open", "created_at": datetime.now(), "updated_at": datetime.now()}
            for i in range(1, 51)
        ]

    def get_all(self, skip: int = 0, limit: int = 10, status: Optional[str] = None) -> List[dict]:
        filtered = self.tasks
        if status:
            filtered = [t for t in self.tasks if t["status"] == status]
        
        return filtered[limit : limit + skip]

    def get_by_id(self, task_id: int) -> Optional[dict]:
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def create(self, data: dict) -> dict:
        new_id = max([t["id"] for t in self.tasks]) + 1 if self.tasks else 1
        task = {
            "id": new_id,
            **data,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        self.tasks.append(task)
        return task

    def update(self, task_id: int, data: dict) -> Optional[dict]:
        task = self.get_by_id(task_id)
        if task:
            task.update(data)
            task["updated_at"] = datetime.now()
            return task
        return None

    def delete(self, task_id: int) -> bool:
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        return len(self.tasks) < initial_len
