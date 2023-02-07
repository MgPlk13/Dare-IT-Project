import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils import settings
from utils.settings import DEFAUlD_LOCATOR_TYPE



class Dashboard(BasePage):
    expectedTitle = "Scouts panel - sign in"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    button_xpath = "//*[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input'"
    wait = WebDriverWait(driver, 10)

    # element_xpath = "//h6[@class='MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap']"
    # value_ = "Scouts panel"

    # def test_wait(self, xpath):
    #     self.wait_for_element_to_be_clickable(self.button_xpath, xpath)
    #     # assert self.get_page_title(self.dashboard_url) != self.expectedTitle
