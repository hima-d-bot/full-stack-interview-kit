from typing import List
from app.utils.ops_counter import ops_counter

class SuggestService:
    def suggest_tasks(self, query: str, tasks: List[dict]) -> List[dict]:
        ops_counter.reset()
        query_lower = query.lower()
        ops_counter.increment() # One op for normalizing query
        
        suggestions = []
        for task in tasks:
            ops_counter.increment() # One op per task check
            if query_lower in task["title"].lower() or query_lower in (task["description"] or "").lower():
                suggestions.append(task)
        
        return suggestions
