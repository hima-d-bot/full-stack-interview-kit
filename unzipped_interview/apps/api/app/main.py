from fastapi import FastAPI
from app.routers import tasks, suggestions

app = FastAPI(title="Full-Stack Interview API")

app.include_router(tasks.router, tags=["Tasks"])
app.include_router(suggestions.router, tags=["Suggestions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Full-Stack Interview API"}
