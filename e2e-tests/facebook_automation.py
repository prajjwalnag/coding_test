from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def get_fb_session(email, password):
    """
    Task 1: Extracting Session Cookies (c_user & xs)
    """
    driver.get("https://www.facebook.com")
    
    # TODO: Perform login (find elements, send keys, click login)
    print("Log in here...")
    
    time.sleep(5) # Wait for redirect
    
    cookies = driver.get_cookies()
    fb_session = {}
    
    # TODO: Loop through 'cookies' and extract 'c_user' and 'xs'
    # TODO: Return a dictionary: {"c_user": "...", "xs": "..."}
    
    return fb_session


def fetch_wall_data(cookies_dict):
    """
    Task 2: Persistent Login & Wall Data Fetching
    """
    # Start a fresh driver instance (or clear existing state)
    driver.delete_all_cookies()
    
    # Note: You have to load the domain first before injecting cookies for that domain.
    driver.get("https://www.facebook.com")
    
    # TODO: Use driver.add_cookie() to inject the 'c_user' and 'xs' values.
    
    # Refresh to apply cookies and bypass login
    driver.refresh()
    time.sleep(5)
    
    # TODO: Implement a "Scroll" function to trigger Lazy-Loading of 3 posts.
    
    # TODO: Extract the text content of the first 3 posts and print them.
    
    pass

if __name__ == "__main__":
    # Remove these hardcoded credentials in production! Use .env or Vault.
    session = get_fb_session("test_email@example.com", "dummy_password")
    fetch_wall_data(session)
    driver.quit()
