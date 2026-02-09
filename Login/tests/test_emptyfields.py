from pages.login_page import LoginPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_login_with_empty_credentials(page):
    login_page = LoginPage(page)

    login_page.navigate(URL)
    login_page.login("", "")


    # ✅ ADD HERE
    assert login_page.is_required_error_visible()
