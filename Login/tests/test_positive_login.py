import re
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.pim_page import PimPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_positive_login(page):
    login_page = LoginPage(page)
    pim_page = PimPage(page)

    login_page.navigate(URL)
    login_page.login("Admin", "admin123")

    # ✅ POSITIVE validation
    expect(page).to_have_url(re.compile("dashboard"))
    assert pim_page.is_pim_visible()
