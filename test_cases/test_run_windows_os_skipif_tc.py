import sys

import pytest
from fixtures.browser_setup import driver

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows platform")
def test_mac_specific_feature():
    pass


@pytest.mark.skipif(sys.platform == "win64", reason="Not supported on Windows platform")
def test_windows64_specific_feature(driver):
    assert driver.current_url == "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
