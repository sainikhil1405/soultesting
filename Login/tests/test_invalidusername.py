from pages.login_page import LoginPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_login_with_invalid_username(page):
    login_page = LoginPage(page)

    login_page.navigate(URL)
    login_page.login("WrongUser", "admin123")


    # ✅ ADD HERE
    assert login_page.is_invalid_credentials_visible()
