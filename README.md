# Full-Stack Coding Challenge

Welcome to the Full-Stack Coding Challenge! This assessment is designed to test your proficiency in **Next.js**, **FastAPI**, and **Selenium** end-to-end testing.

## Scenario

You are provided with a minimal "Task Board" application. The frontend is built with Next.js (React) and styled with Tailwind CSS. The backend is a Python FastAPI server.

Currently, the application displays a list of tasks, but the functionality to **add a new task** is broken, and the automated E2E tests are incomplete.

Your goal is to fix the application and complete the test suite.

## Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- Chrome Browser & ChromeDriver (for Selenium)

---

## Task 1: The Backend (FastAPI)

The frontend needs to send a new task to the backend, but the API endpoint is missing.

1. Navigate to the `backend/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Open `backend/main.py`.
4. Run the server: `uvicorn main:app --reload`
5. **Your Job**: Implement the `POST /api/tasks` endpoint using FastAPI. It should receive a task title and description, assign an ID and timestamp, append it to the `tasks_db`, and return the created task.

## Task 2: The Frontend (Next.js)

The button to submit a task is in the UI, but it doesn't do anything yet.

1. Navigate to the `frontend/` directory.
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`
4. Open the app at `http://localhost:3000`.
5. **Your Job**: Open `frontend/src/components/TaskForm.tsx`. Complete the `handleSubmit` function to send a POST request with the `title` and `description` to your backend from Task 1.

## Task 3: The E2E Test (Selenium)

We need to ensure the entire flow works using an automated test.

1. Navigate to the `e2e-tests/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Open `e2e-tests/test_task_flow.py`.
4. Ensure both the frontend and backend servers are running locally.
5. **Your Job**: Complete the `test_add_new_task` function. 
   - Use Selenium to navigate to the Next.js app (`http://localhost:3000`).
   - Fill out the form with a test title and description.
   - Submit the form.
   - Assert that the newly created task appears in the UI table below.
6. Run your test: `pytest test_task_flow.py -v`

---

## Submission

Fork this repository, complete the tasks, and submit a pull request or share the repository link when finished! Good luck!
