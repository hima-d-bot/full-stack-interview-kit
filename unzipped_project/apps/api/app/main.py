from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tasks, labels, stats, suggestions, activity
import time

app = FastAPI(title="Production Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": time.time(), "version": "1.0.0"}

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(labels.router, prefix="/labels", tags=["labels"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
app.include_router(suggestions.router, prefix="/suggestions", tags=["suggestions"])
app.include_router(activity.router, prefix="/activity", tags=["activity"])
