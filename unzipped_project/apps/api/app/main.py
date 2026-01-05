from fastapi import FastAPI
from app.routers import tasks, labels, stats, suggestions, activity

app = FastAPI(title="Interview API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(labels.router, prefix="/labels", tags=["labels"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
app.include_router(suggestions.router, prefix="/suggestions", tags=["suggestions"])
app.include_router(activity.router, prefix="/activity", tags=["activity"])
