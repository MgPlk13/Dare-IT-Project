import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class CleanForm(BasePage):
    xpath_name = "//*[@name='name']"
    button_xpath = "//*[@class='MuiCardContent-root']/a[2]"
    xpath = "//*[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12" \
            " MuiGrid-grid-sm-6 MuiGrid-grid-md-4']/div/div/input"

    def clear_(self):
        # self.click_element(self.button_xpath)
        self.driver.find_element(By.XPATH, self.xpath_name)




