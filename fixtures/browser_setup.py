import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


TARGET_URL = "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"

@pytest.fixture()
def driver():
    # --- SETUP ---
    options = webdriver.ChromeOptions()
    options.add_argument("--headed")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    browser.get(TARGET_URL)

    yield browser  # Pass control to the test

    # --- TEARDOWN ---
    browser.quit()
