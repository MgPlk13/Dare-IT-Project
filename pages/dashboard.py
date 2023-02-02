import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expectedTitle = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    # element_xpath = "//h6[@class='MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap']"
    # value_ = "Scouts panel"

    def title_of_page(self):
        assert self.getTitle(self.dashboard_url) == self.expectedTitle

    # def elements_text(self):
    #     assert self.assert_element_text(self.element_xpath) == self.value_
