# 🚀 Full-Stack Engineering Assessment

Welcome to the Full-Stack Coding Challenge! This assessment is designed to evaluate your proficiency across three isolated domains: **Next.js** (Frontend), **FastAPI** (Backend), and **Selenium** (QA/Web Automation).

---

## 📌 How to Take This Test

To ensure a smooth evaluation, please follow these exact steps:

1. **Fork the Repository:** Click the "Fork" button in the top right corner of this GitHub page to create a personal copy on your own GitHub account.
2. **Clone Locally:** Clone *your* forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/coding_test.git
   ```
3. **Complete the Modules:** Iterate through the `backend/`, `frontend/`, and `e2e-tests/` directories. *You may complete them in any order you choose.*
4. **Commit Your Code:** Make clear, descriptive commits as you solve the various checkpoints.
5. **Submit Your Work (PR):** Once fully finished, push your branches up to your GitHub fork and open a **Pull Request (PR)** against this original repository. Our engineering team will review your code natively in the PR!

---

## 🐍 Task 1: The Backend (FastAPI)

> The backend is completely decoupled into two specific skill tests: building a **Weather Async Proxy** and parsing a **Childcare Enrollment Form**.

**Getting Started:**
```bash
cd backend/
pip install -r requirements.txt
uvicorn main:app --reload
```

**Your Assignments (in `backend/main.py`):**
*   🟢 **`GET /api/weather`**: Implement an async `httpx` proxy to OpenWeatherMap. Handle errors safely.
*   🟢 **`POST /api/enrollment`**: Use FastAPI `Form(...)` to parse a complex childcare enrollment HTML form containing lists, dates, and booleans.

---

## ⚛️ Task 2: The Frontend (Next.js)

> The frontend challenge evaluates advanced React patterns, client-side data parsing, and pixel-perfect Tailwind CSS cloning.

**Getting Started:**
```bash
cd frontend/
npm install
npm run dev
# Open http://localhost:3000
```

**Your Assignments:**
*   🔵 **Task 1 (`/dashboard`)**: Build a `react-dropzone` CSV uploading tool that visually renders `recharts` and a TanStack Data Table natively in-browser using `PapaParse`. You must elegantly handle 'dirty' CSV data.
*   🔵 **Task 2 (`/landing`)**: Fix a brutally messy SaaS landing page layout using Tailwind CSS Grid/Flexbox, `framer-motion` animations, and a `next-themes` dark mode toggle.

---

## 🤖 Task 3: Headless Automation (Selenium Python)

> The automation challenge tests your ability to bypass authentications and execute advanced headless DOM scraping.

**Getting Started:**
```bash
cd e2e-tests/
pip install -r requirements.txt
# Code inside facebook_automation.py
```

**Your Assignments:**
*   🟣 **Task 1 (Cookies)**: Script a standard Facebook login to dynamically extract the `c_user` and `xs` authentication cookies.
*   🟣 **Task 2 (Injection)**: Force a new headless session by injecting those cookies (bypassing the login screen directly). Dynamically *scroll* the page to force lazy-loading, and safely scrape the first 3 text posts.

---

### 🎉 Good Luck!
*We look forward to reviewing your Pull Request.*
