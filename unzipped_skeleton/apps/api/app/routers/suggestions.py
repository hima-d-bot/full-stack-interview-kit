from fastapi import APIRouter
from app.services.suggest_service import SuggestService
from app.repos.tasks_repo import TasksRepo
from app.schemas import SuggestionRequest, SuggestionResponse
from app.utils.ops_counter import ops_counter

router = APIRouter()
service = SuggestService()
repo = TasksRepo()

@router.post("/suggestions", response_model=SuggestionResponse)
def get_suggestions(request: SuggestionRequest):
    tasks, _ = repo.get_all(limit=1000)
    suggestions = service.suggest_tasks(request.query, tasks)
    return {
        "suggestions": suggestions,
        "operations": ops_counter.get_count()
    }
