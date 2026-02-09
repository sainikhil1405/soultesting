from utils.logger import get_logger

logger = get_logger()

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.recruitment_menu = page.get_by_role("link", name="Recruitment")

    def go_to_recruitment(self):
        logger.info("Navigating to Recruitment module")
        self.recruitment_menu.click()
