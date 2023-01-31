import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expectedTitle = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        assert self.getTitle(self.dashboard_url) == self.expectedTitle
