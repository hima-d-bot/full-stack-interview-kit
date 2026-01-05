from typing import List, Optional, Tuple
from datetime import datetime

class TasksRepo:
    def __init__(self):
        self.tasks = [
            {
                "id": i, 
                "title": f"Task {i}", 
                "description": f"Description for {i}", 
                "status": "open" if i % 2 == 0 else "closed", 
                "created_at": datetime(2023, 1, 1, i % 24, 0, 0), 
                "updated_at": datetime(2023, 1, 1, i % 24, 0, 0)
            }
            for i in range(1, 101)
        ]

    def get_all(self, skip: int = 0, limit: int = 10, status: Optional[str] = None) -> Tuple[List[dict], int]:
        filtered = self.tasks
        if status:
            filtered = [t for t in self.tasks if t["status"] == status]
        
        # Deterministic sorting: by created_at then by id
        sorted_tasks = sorted(filtered, key=lambda x: (x["created_at"], x["id"]))
        
        total = len(sorted_tasks)
        # Correct slicing
        return sorted_tasks[skip : skip + limit], total

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
