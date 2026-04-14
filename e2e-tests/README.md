# E2E Test Challenge (Selenium)

Welcome to the automated testing portion of the assessment. We use Selenium WebDriver in Python to verify the final end-to-end integration of our Frontend and Backend.

## Setup Instructions

1. Make sure you have **Chrome Browser** installed on your machine.
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Important Check**: Ensure BOTH the Next.js Frontend (`localhost:3000`) and the FastAPI Backend (`localhost:8000`) are running locally before attempting to run tests.
4. Execute the test suite using pytest:
   ```bash
   pytest test_task_flow.py -v
   ```

## Your Task

Open `test_task_flow.py` and locate the `test_add_new_task` function.

Currently, the test navigates to the React app but immediately fails.

**Requirements:**
1. Using Selenium WebDriver, locate the Task Title input field and inject a dummy string.
2. Locate the Description textarea and enter a dummy description.
3. Trigger the submit button action.
4. Implement an assertion (`assert`) to ensure the newly added dummy task appears dynamically in the UI's table underneath the form.

*(Note: Depending on system speeds, you may need to implement `WebDriverWait` to give Next.js time to fetch the updated table from the background!).*
