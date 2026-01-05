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
        
        # BUG 1: Unstable sorting (missing deterministic tie-breaker)
        # Sorting only by created_at which has many duplicates (i % 24)
        sorted_tasks = sorted(filtered, key=lambda x: x["created_at"])
        
        total = len(sorted_tasks)
        
        # BUG 2: Off-by-one in pagination (incorrect slicing)
        # Using limit:limit+skip instead of skip:skip+limit
        return sorted_tasks[limit : limit + skip], total

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
