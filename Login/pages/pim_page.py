from playwright.sync_api import expect

class PimPage:
    def __init__(self, page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")

    def is_pim_visible(self):
        expect(self.pim_menu).to_be_visible(timeout=10000)
        return True
