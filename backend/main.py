from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Task Board API")

# Configure CORS for local Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskBase(BaseModel):
    title: str
    description: str
    status: str = "Todo"

class Task(TaskBase):
    id: int
    created_at: str

# In-memory database
tasks_db: List[Task] = []
current_id = 1

# Seed some initial data
tasks_db.append(Task(id=0, title="Initial Demo Task", description="This is to show the grid works.", status="Done", created_at=datetime.now().isoformat()))

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Returns all current tasks."""
    return tasks_db

@app.post("/api/tasks", response_model=Task)
async def create_task(task_in: TaskBase):
    """
    TODO FOR CANDIDATE:
    Implement this endpoint to receive a new task, assign it a unique ID, 
    record the current creation time, store it in `tasks_db`, and return the created task.
    """
    # ----- YOUR CODE HERE -----
    raise HTTPException(status_code=501, detail="POST /api/tasks not implemented yet. Implement me!")
    # --------------------------
