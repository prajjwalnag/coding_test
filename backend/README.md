# Backend Challenge (FastAPI)

Welcome to the backend portion of the assessment. This directory contains a minimal Python FastAPI application that currently operates an in-memory database to manage tasks.

## Setup Instructions

1. Ensure you have **Python 3.9+** installed.
2. It's highly recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the local server using live reload:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will run on `http://localhost:8000`.

## Your Task

Open `main.py` and navigate to the `create_task` function.

Currently, the endpoint `POST /api/tasks` is stubbed out and returns a `501 Not Implemented` exception.

**Requirements:**
1. Parse the incoming request payload (`title` and `description`).
2. Generate a unique integer `id` for the new task.
3. Record the current time in ISO format for `created_at`.
4. Append the newly structured `Task` object to the `tasks_db` array.
5. Return the created task as the JSON response.

Good luck!
