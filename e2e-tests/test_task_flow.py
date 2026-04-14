import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') # Uncomment for headless execution
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()

def test_add_new_task(driver):
    """
    TODO FOR CANDIDATE:
    This test currently opens the Next.js frontend, but it does not perform the actions
    to fill out the form, submit it, or verify the result.
    
    Your task:
    1. Navigate to the frontend URL (http://localhost:3000)
    2. Find the task title and description input fields and fill them with sample data.
    3. Click the submit button.
    4. Assert that the newly created task appears in the task list on the page.
    """
    
    # 1. Navigate to the app
    driver.get("http://localhost:3000")
    
    # Wait for the main page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    # ----- YOUR CODE HERE -----
    # 2. Fill out the form
    
    # 3. Submit the form
    
    # 4. Verify the new task is present in the table/list
    
    pytest.fail("E2E Test not implemented yet. Implement the interactions and assertions!")
    # --------------------------
