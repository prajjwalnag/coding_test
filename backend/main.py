from fastapi import FastAPI, HTTPException, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import httpx
from datetime import date

app = FastAPI(title="Backend Coding Challenge")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/weather")
async def get_weather(city: str):
    """
    Task 1: The Weather Proxy (Intermediate)
    
    TODO FOR CANDIDATE:
    1. Retrieve the city name from the query parameters.
    2. Securely append a dummy API key (e.g., "dummy_key_123") and construct the 
       OpenWeatherMap API URL: https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}
    3. Use `httpx.AsyncClient()` to safely make an asynchronous GET request to the URL.
    4. Return the JSON payload back to the client.
    5. Handle expected errors (e.g., city not found -> 404 Exception).
    """
    
    # ----- YOUR CODE HERE -----
    raise HTTPException(status_code=501, detail="GET /api/weather not implemented yet. Show us your async httpx skills!")
    # --------------------------


@app.post("/api/enrollment")
async def enroll_child(
    # ----- YOUR CODE HERE -----
    # Define your Form(...) dependencies here to capture the incoming multiparts!
    # Hint: You need to capture string fields, a date field, and a boolean!
    # --------------------------
):
    """
    Task 2: The Childcare Enrollment Form Form (Intermediate/Advanced)
    
    TODO FOR CANDIDATE:
    1. The client is submitting a complex HTML Form Data payload (NOT JSON).
    2. You need to map the incoming form correctly using FastAPI's `Form(...)`.
    3. Required Fields to parse:
        - `parent_name` (string)
        - `child_name` (string)
        - `date_of_birth` (date type)
        - `enrolled_programs` (A list of strings, since it's a multi-select checkbox)
        - `agreed_to_terms` (boolean)
    4. Compile these parsed fields into a python dictionary and return them as the JSON response 
       to prove they were successfully extracted.
    """
    
    # ----- YOUR CODE HERE -----
    raise HTTPException(status_code=501, detail="POST /api/enrollment not implemented yet. Ensure you use python-multipart Form extraction!")
    # --------------------------
