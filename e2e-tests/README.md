# Web Automation Challenge (Selenium)

Welcome to the headless automation portion of the assessment. We use Selenium WebDriver in Python to verify skills related to session management, DOM manipulation, scraping, and authentication bypassing.

## Setup Instructions

1. Make sure you have **Chrome Browser** installed on your machine.
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `facebook_automation.py` to begin.

---

## Task 1: Extracting Session Cookies (`c_user` & `xs`)

**Goal**: Automate the Facebook login process and programmatically extract the `c_user` and `xs` cookies, which represent the active session.

**Requirements**:
1. Navigate to Facebook and use Selenium to input a test email and password.
2. Use `driver.get_cookies()` to retrieve the full list of session cookies after a successful login redirect.
3. Write logic to loop through the cookies and securely extract the specific values for `c_user` and `xs`.

---

## Task 2: Persistent Login & Wall Data Fetching

**Goal**: Use the cookies extracted in Task 1 to "inject" a session into a newly cleared browser instance and scrape post data from a wall.

**Requirements**:
1. Without typing in a username/password, use `driver.add_cookie()` to inject the Session Secret into the WebDriver.
2. Refresh the page to confirm you are successfully logged in and bypassing the login screen.
3. Navigate to a feed and scrape the text content of the first 3 posts.
4. **Automation Challenge:** Implement a "Scroll" function via Javascript in Selenium to ensure at least 3 posts have lazy-loaded before attempting to scrape the DOM elements.
