from typing import List, Optional
from app.schemas import Task

class TasksRepo:
    def __init__(self):
        self.tasks = []

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Task]:
        # BUG: Swapped skip and limit in realistic production-like mistake
        return self.tasks[limit : limit + skip]

    def add(self, task: Task):
        self.tasks.append(task)
