from playwright.sync_api import expect
from utils.logger import get_logger

logger = get_logger()

class RecruitmentPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.get_by_role("button", name="Add")
        self.first_name = page.get_by_role("textbox", name="First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")

        self.vacancy_dropdown = page.locator(
            "//label[text()='Vacancy']/following::div[contains(@class,'oxd-select-text')][1]"
        )

        self.email = page.get_by_role("textbox", name="Type here").first
        self.mobile = page.get_by_role("textbox", name="Type here").nth(1)
        self.save_button = page.get_by_role("button", name="Save")

        # ✅ ADD THIS LOCATOR
        self.shortlist_button = page.get_by_role("button", name="Shortlist")

    def add_candidate(self, first, last, email, mobile):
        logger.info("Clicking Add Candidate")
        self.add_button.click()

        logger.info("Filling candidate details")
        self.first_name.fill(first)
        self.last_name.fill(last)

        logger.info("Opening vacancy dropdown")
        self.vacancy_dropdown.click()

        vacancy_option = self.page.get_by_role(
            "option", name="Junior Account Assistant"
        )
        expect(vacancy_option).to_be_visible(timeout=10000)
        vacancy_option.click()

        self.email.fill(email)
        self.mobile.fill(mobile)

        logger.info("Saving candidate")
        self.save_button.click()

    # ✅ ADD THIS METHOD
    def shortlist_candidate(self):
        logger.info("Clicking Shortlist button")
        expect(self.shortlist_button).to_be_visible(timeout=15000)
        self.shortlist_button.click()
