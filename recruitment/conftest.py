import pytest
import pytest_html
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot = f"reports/screenshots/{item.name}_{datetime.now().strftime('%H%M%S')}.png"
            page.screenshot(path=screenshot, full_page=True)
            report.extra = getattr(report, "extra", [])
            report.extra.append(pytest_html.extras.image(screenshot))
