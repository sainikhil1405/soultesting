from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage
from utils.logger import get_logger

logger = get_logger()

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_add_and_shortlist_candidate(page):
    logger.info("Starting test: Add and Shortlist Candidate")

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    recruitment = RecruitmentPage(page)

    login.navigate(URL)
    login.login("Admin", "admin123")

    dashboard.go_to_recruitment()

    recruitment.add_candidate(
        first="sainikhil",
        last="goud",
        email="sai@gmail.com",
        mobile="7386464728"
    )

    recruitment.shortlist_candidate()

    logger.info("Test completed successfully")
