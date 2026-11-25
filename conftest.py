
import pytest
def pytest_html_report_title(report):
    report.title = "Selenium Automation Test Suite Execution Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)