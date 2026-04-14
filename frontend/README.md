# Frontend Challenge (Next.js)

Welcome to the frontend portion of the assessment. This directory contains a Next.js (App Router) project styled entirely with Tailwind CSS v4.

## Setup Instructions

1. Ensure you have **Node.js 18+** installed.
2. Install the application dependencies:
   ```bash
   npm install
   ```
3. Run the Next.js development server:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Your Task

The UI successfully lists tasks fetched from the API, but the button inside the visual form currently does not work. 

Open `src/components/TaskForm.tsx` and find the `handleSubmit` function.

**Requirements:**
1. Capture the local state (`title` and `description`).
2. Dispatch a `fetch()` POST request to the backend server running at `http://localhost:8000/api/tasks`. Ensure headers securely pass `application/json` properties.
3. If the backend accepts the request (20x status), clear out the form inputs securely and invoke the `onTaskAdded()` prop to refresh the overall table.
4. Check error handling in case the candidate API from Backend Task 1 drops the request.
