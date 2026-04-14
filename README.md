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

The backend is completely decoupled into two specific skill tests: a Weather Async Proxy and a multi-part Childcare Enrollment Form parser.

1. Navigate to the `backend/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Open `backend/main.py`.
4. Run the server: `uvicorn main:app --reload`
5. **Your Job**: 
   - **GET `/api/weather`**: Implement an async httpx proxy to OpenWeatherMap.
   - **POST `/api/enrollment`**: Use FastAPI `Form(...)` to parse a complex childcare enrollment form containing lists, dates, and booleans.

## Task 2: The Frontend (Next.js)

The frontend challenge evaluates advanced React patterns, client-side data parsing, and pixel-perfect Tailwind CSS cloning.

1. Navigate to the `frontend/` directory.
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`
4. Open the app at `http://localhost:3000` to view the Task Hub.
5. **Your Job**: 
   - **Task 1 (/dashboard)**: Build a `react-dropzone` CSV uploading tool that visually renders `recharts` and a TanStack Data Table natively in-browser using PapaParse. Handle 'dirty' data elegantly.
   - **Task 2 (/landing)**: Fix a brutally messy SaaS landing page layout using Tailwind CSS Grid/Flexbox, `framer-motion` animations, and a `next-themes` dark mode toggle.

## Task 3: Headless Automation (Selenium Python)

The automation challenge tests your ability to bypass authentications and execute advanced headless DOM scraping.

1. Navigate to the `e2e-tests/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Open `facebook_automation.py`.
4. **Your Job**: 
   - **Task 1**: Script a standard login to extract the `c_user` and `xs` authentication cookies.
   - **Task 2**: Force a new headless session by injecting those cookies (bypassing the login screen directly), scroll the page dynamically to force lazy-loading, and scrape the first 3 text posts.

---

## Submission

Fork this repository, complete the tasks, and submit a pull request or share the repository link when finished! Good luck!
