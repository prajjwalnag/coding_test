# 🤖 Web Automation Challenge (Selenium)

Welcome to the headless automation portion of the assessment! We use Selenium WebDriver in Python to verify your skills related to session management, DOM manipulation, web scraping, and authentication bypassing safely.

---

## ⚙️ Setup Instructions

1. Make sure you have **Google Chrome** installed on your machine.
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `facebook_automation.py` to begin coding.

---

## 🍪 Task 1: Extracting Session Cookies (`c_user` & `xs`)

**🎯 Goal**: Automate the Facebook login process and programmatically extract the `c_user` and `xs` cookies, which represent the live, active session variable.

**📝 Requirements**:
*   **Authentication:** Navigate to Facebook and use Selenium to robustly input a test email and password.
*   **Cookie Extraction:** Use `driver.get_cookies()` to retrieve the full array of session cookies after a successful login redirect.
*   **Dictionary Filtering:** Write logic to loop through the dense cookies response and securely extract only the exact specific values for `c_user` and `xs`.

---

## 📜 Task 2: Persistent Login & Wall Data Fetching

**🎯 Goal**: Use the cookies extracted uniquely in Task 1 to "inject" a session into a newly cleared browser instance to safely scrape post data from a wall.

**📝 Requirements**:
*   **Session Injection:** Without typing in a username/password, use `driver.add_cookie()` accurately to inject the Session Secret into the fresh, headless WebDriver.
*   **Bypass Validation:** Refresh the page to confirm you are successfully logged in and bypassing the login screen naturally.
*   **Scraping:** Navigate to a target feed and scrape the raw text content of the first 3 posts.

> [!CAUTION]
> **The Automation Challenge:** Facebook uses heavily dynamic DOM loading. You must implement a highly specific "Scroll" function via Javascript bindings (`window.scrollTo()`) or `ActionChains` in Selenium to ensure at least 3 posts have "lazy-loaded" into the DOM before attempting to scrape the DOM elements cleanly!
