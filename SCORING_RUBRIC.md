# Interview Evaluator: Scoring Rubric

**Total Score: 100 Points**  
This standardized grading rubric helps evaluating engineers assess candidates objectively across the three isolated tech stacks. 

---

## 1. FastAPI Backend (30 Points Total)

### Task 1: Async Weather Proxy (15 Points)
*   **[5 pts] Query Construction:** Did they extract the `city` via query parameters and securely append the `appid` without hardcoding it recklessly in a way that would be exposed to the frontend?
*   **[5 pts] Async Implementation:** Did they use `httpx.AsyncClient` optimally with Python's `async/await` syntax, rather than falling back to synchronous `requests`?
*   **[5 pts] Error Handing:** Did they implement a `try/except` block to catch `httpx.HTTPStatusError` (e.g., city not found) and return a clean FastAPI `HTTPException` instead of a harsh internal 500 error?

### Task 2: Childcare Enrollment Form Parser (15 Points)
*   **[5 pts] Form Extraction:** Did they correctly import and utilize FastAPI's specialized `Form(...)` class instead of mistakenly trying to parse a standard Pydantic JSON Body?
*   **[5 pts] Data Types:** Could they handle the complex types safely (ensuring the `date` mapped correctly, the boolean resolved, and specifically parsing the `enrolled_programs` as a `List[str]`)?
*   **[5 pts] Code Cleanliness:** Is the returned dictionary flattened and formatted properly? 

---

## 2. Next.js Frontend (40 Points Total)

### Task 1: CSV-to-Analytics Dashboard (20 Points)
*   **[5 pts] Dropzone Logic:** Did they implement `react-dropzone` smoothly, strictly accepting `.csv` MIME types?
*   **[5 pts] PapaParse Integration:** Are they parsing the CSV asynchronously on the client-side without locking up the UI thread? 
*   **[5 pts] Handling "Dirty" Data:** *Critical Check.* If you pass a CSV missing half its values, does the app crash? Full points if they implemented a mapping `.filter()` that cleans broken rows before passing them to the charts.
*   **[5 pts] Recharts / TanStack:** Are both the table and graphs visually synced to the exact same dataset state?

### Task 2: Pixel-Perfect Clone Fix (20 Points)
*   **[5 pts] Responsive Grid/Flexbox:** Did they fix the overlapping bug? The UI should fluidly stack on mobile (375px width) and display elegantly horizontally on desktop without horizontal scrolling.
*   **[5 pts] Component Mapping:** Did they extract the messy Navbar into a clean `.map()` loop pulling from a JS constant object?
*   **[5 pts] Dark Mode:** Is `next-themes` effectively wired into the root layout so that Tailwind uses `dark:bg-*` classes properly?
*   **[5 pts] Animations:** Did they wrap the hero sections in `framer-motion` `<motion.div>` tags to provide a premium entrance fade-in?

---

## 3. Selenium Web Automation (30 Points Total)

### Task 1: Session Cookie Extraction (10 Points)
*   **[5 pts] DOM Traversal:** Did they use robust, unique selectors (like `By.ID` or distinct `By.XPATH`) to target the Facebook login fields, rather than brittle class names?
*   **[5 pts] Cookie Isolation:** Did they correctly loop through the `driver.get_cookies()` dictionary and safely extract solely `c_user` and `xs` into a return state variable?

### Task 2: Headless Injection & Scraping (20 Points)
*   **[5 pts] Proper Injection:** Did they correctly navigate to the domain *first* before running `driver.add_cookie()`? (Selenium throws an error if injecting cookies onto a blank `data:,` domain).
*   **[10 pts] Dynamic Lazy-Load Scrolling:** *Maximum Difficulty Check.* Did they implement highly effective Javascript `window.scrollTo` commands, `ActionChains`, or `Keys.PAGE_DOWN` logic coupled with `WebDriverWait` to ensure the feed posts loaded into the DOM before searching for them?
*   **[5 pts] DOM Extraction:** Did they accurately pull the `.text` attributes of the first three post nodes without grabbing unintended side-bar text?
