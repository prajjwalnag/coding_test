# Backend Challenge (FastAPI)

Welcome to the backend portion of the assessment. This directory contains a minimal Python FastAPI setup to test your async programming logic and complex payload processing skills.

## Setup Instructions

1. Ensure you have **Python 3.9+** installed.
2. It's highly recommended to use a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the dependencies (which now includes `httpx` and `python-multipart`):
   ```bash
   pip install -r requirements.txt
   ```
4. Start the local server using live reload:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will run on `http://localhost:8000`.

---

## Task 1: The Weather Proxy (Intermediate)

Open `main.py` and locate the `get_weather` function under `GET /api/weather`.

Currently, this endpoint is stubbed out and returns a `501 Not Implemented`.

**The Goal:** Build an endpoint that connects to the OpenWeatherMap API securely from the backend to hide the frontend credential access.

**Requirements:**
1. Extract the `city` string from the query parameters.
2. Create a fake OpenWeatherMap URL using a dummy key: `https://api.openweathermap.org/data/2.5/weather?q={city}&appid=dummy_key_123`
3. Use the `httpx.AsyncClient` package to safely make an **asynchronous** GET request to that URL. 
4. Return the raw JSON payload back to the caller.
5. Provide error handling if the external async request fails or if the city does not exist (raise a proper 404/500 `HTTPException`).

---

## Task 2: The Childcare Enrollment Form (Intermediate/Advanced)

Locate the `enroll_child` function under `POST /api/enrollment`.

Currently, this returns a `501 Not Implemented`.

**The Goal:** Build an endpoint capable of processing a massive, multi-field HTML form payload for a childcare center. This tests your capacity to handle traditional web-forms instead of strict JSON payloads.

**Requirements:**
1. Map incoming form fields correctly using FastAPI's `Form(...)` dependencies.
2. You must enforce the correct typing constraints on the extraction:
   * `parent_name` (string)
   * `child_name` (string)
   * `date_of_birth` (date format)
   * `enrolled_programs` (a **List** of strings, since checkboxes pass multiple values)
   * `agreed_to_terms` (boolean)
3. Return these mapped values as a standardized dictionary in the JSON response to prove you extracted them perfectly from the multipart form payload.

Good luck!
