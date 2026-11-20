
from fixtures.browser_setup import driver


def test_page_title(driver):
    assert "Selenium Practice" in driver.title or "Automation" in driver.title
