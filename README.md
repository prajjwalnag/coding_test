# Full-Stack Coding Challenge

Welcome to the Full-Stack Coding Challenge! This assessment evaluates your proficiency in isolated **Next.js**, **FastAPI**, and **Selenium** web automation tasks.

## How to Take This Test

To ensure a smooth evaluation, please follow these exact steps:

1. **Fork the Repository:** Click the "Fork" button in the top right corner of this GitHub page to create a personal copy on your own GitHub account.
2. **Clone Locally:** Clone *your* forked repository to your local machine (`git clone https://github.com/YOUR_USERNAME/coding_test.git`).
3. **Complete the Modules:** Iterate through the `backend`, `frontend`, and `e2e-tests` directories below. You may complete them in any order you choose.
4. **Commit Your Code:** Make clear, descriptive commits as you finish the various checkpoints.
5. **Submit Your Work:** Once you are fully finished, push your branches to your GitHub fork and open a **Pull Request (PR)** against this original repository. Our engineering team will review the code natively in the PR.

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

**Good Luck!** We look forward to reviewing your Pull Request.
