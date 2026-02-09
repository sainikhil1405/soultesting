import re
from playwright.sync_api import expect
from utils.base_page import BasePage
from utils.logger import get_logger

logger = get_logger()

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        logger.info("Entering username")
        self.username.fill(username)

        logger.info("Entering password")
        self.password.fill(password)

        logger.info("Clicking Login button")
        self.login_button.click()

        expect(self.page).to_have_url(re.compile("dashboard"), timeout=15000)
