# ⚛️ Frontend Challenge (Next.js)

Welcome to the Next.js portion of the assessment! You are meant to solve two distinct modern web-development challenges located inside the `src/app` routing directory.

---

## ⚙️ Setup Instructions

1. Ensure you have **Node.js 18+** installed.
2. Install the application dependencies:
   ```bash
   npm install
   ```
3. Run the Next.js development server:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser to access the interactive Task Hub.

---

## 📊 Task 1: The CSV-to-Analytics Dashboard

Located in `src/app/dashboard/page.tsx`.

**🎯 Goal:** Build a rich dashboard that allows a user to upload a CSV file (e.g., lead data or ad spend) and visualizes the data using charts entirely natively on the client.

**📝 Requirements:**
*   **File Upload:** Create an intuitive drag-and-drop zone using `react-dropzone`.
*   **Parsing Strategy:** Use `PapaParse` to convert the CSV rows into a JSON array safely on the client side.
*   **Data Visualization:** Use `Recharts` to display at least two charts:
    1.  A **Bar Chart** showing a count of categories (e.g., leads by status).
    2.  A **Line Chart** showing a trend over time (e.g., revenue/date).
*   **Data Table:** Display the raw parsed data in a searchable/sortable table using `@tanstack/react-table`.

> [!WARNING]
> **The Technical Challenge:** You must handle "dirty" data elegantly. If a CSV row is missing a value or structurally broken, ensure the dashboard drops/repairs the row safely without crashing the React render loop!

---

## 🎨 Task 2: The "Pixel-Perfect" UI Fix

Located in `src/app/landing/page.tsx`.

**🎯 Goal:** Take the provided intentionally "broken" and "ugly" clone of a high-end SaaS landing page layout and meticulously fix the CSS/Layout using Tailwind CSS.

**📝 Requirements:**
*   **Layout Correction:** Fix a brutally broken Flexbox/Grid layout where elements severely overlap on smaller screens. 
*   **Theme Implementation:** Implement an interactive "Dark/Light Mode" toggle using `next-themes` that changes the entire UI color palette.
*   **Component Refactoring:** Convert the messy, hardcoded navigation bar into a clean, mapped array component that iterates over a JSON object for menu items.
*   **Animations:** Add subtle but premium entrance animations (e.g., fade-in or slide-up) using `framer-motion` to give the clone a high-end SaaS feel.

> [!IMPORTANT]
> **The Technical Challenge:** Responsive Design. The UI must look absolutely perfect on an ultrafast 1920px monitor and a tiny 375px phone screen without *any* horizontal scrolling or overlapping elements.
