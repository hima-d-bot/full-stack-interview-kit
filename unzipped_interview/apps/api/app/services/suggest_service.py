from typing import List
from app.utils.ops_counter import ops_counter

class SuggestService:
    def suggest_tasks(self, query: str, tasks: List[dict]) -> List[dict]:
        ops_counter.reset()
        
        suggestions = []
        for task in tasks:
            # BUG: Naive O(N*M) implementation with repeated normalization
            # This is the "trap" - it's correct but inefficient
            for word in query.split():
                ops_counter.increment()
                if word.lower() in task["title"].lower():
                    if task not in suggestions:
                        suggestions.append(task)
                
                ops_counter.increment()
                if word.lower() in (task["description"] or "").lower():
                    if task not in suggestions:
                        suggestions.append(task)
        
        return suggestions
