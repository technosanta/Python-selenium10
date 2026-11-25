import pytest

from fixtures.browser_setup import driver

@pytest.mark.sanity
def test_page_title(driver):
    assert "Selenium Practice" in driver.title or "Automation" in driver.title

@pytest.mark.sanity
@pytest.mark.regression
def test_page_url(driver):
    assert driver.current_url == "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
