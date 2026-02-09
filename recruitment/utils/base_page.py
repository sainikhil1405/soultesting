class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)
