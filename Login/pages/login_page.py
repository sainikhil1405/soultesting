from playwright.sync_api import expect
from utils.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

        # 🔴 Error locators (based on screenshots)
        self.required_error = page.locator("span.oxd-input-field-error-message")
        self.invalid_credentials_error = page.locator(".oxd-alert-content-text")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    # For EMPTY username/password
    def is_required_error_visible(self):
        expect(self.required_error.first).to_be_visible(timeout=10000)
        return True

    # For WRONG username/password
    def is_invalid_credentials_visible(self):
        expect(self.invalid_credentials_error).to_be_visible(timeout=10000)
        return True
