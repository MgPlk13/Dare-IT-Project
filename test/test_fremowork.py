import unittest
import os
import time
from unittest import TestSuite

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, DEFAUlD_LOCATOR_TYPE
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import *
from pages.base_page import BasePage
from pages.dashboard import Dashboard
# from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from pages.dropdown_element_page import DropdownElement
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.remote.webelement import WebElement
from pages.web_elament_page import WebElementPage


class Test(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.log = LoginPage(self.driver)
        self.text = BasePage(self.driver)
        self.wait = Dashboard(self.driver)
        self.dd = DropdownElement(self.driver)
        self.webel = WebElementPage(self.driver)

    # expectedTitle = "Scouts panel - sign in"
    # dashboard_url = "https://scouts-test.futbolkolektyw.pl/"
    # button_xpath = "//*[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input'"
    # wait = WebDriverWait(driver, 10)

    # element_xpath = "//h6[@class='MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap']"
    # value_ = "Scouts panel"

    # def test_wait(self):
    #     self.wait.wait_for_element_to_be_clickable(self.button_xpath)
    #     assert self.text.get_page_title(self.dashboard_url) != self.expectedTitle
    def test_w(self):
        time.sleep(2)
        asd = self.dd.dropdown()
        time.sleep(4)

    # def test_row_data(self, row_number):
    #     if (row_number == 0):
    #         raise Exception("Row number starts from 1")
    #
    #     row_number = row_number + 1
    #     row = self.table.find_elements_by_xpath("//tr[" + str(row_number) + "]/td")
    #     rData = []
    #     for webElement in row:
    #         rData.append(webElement.text)
    #
    #     return rData
    def test_count_row(self):
        self.webel.web_element()

    # def test_check_title(self):
    #     actialTitle = self.text.get_page_title("https://scouts-test.futbolkolektyw.pl/")
    #     expectedTitle = "Scouts panel - sign in"
    #     assert actialTitle == expectedTitle
    #
    # def test_title(self):
    #     title_login_in_system = self.text.get_page_title("https://scouts-test.futbolkolektyw.pl/")
    #     print(f" Title for this page: {title_login_in_system}, len is: {len(title_login_in_system)}")
    #
    # def test_title_2(self):
    #     expected_tuple = "Scouts panel - sign "
    #     current_title = self.text.get_page_title("https://scouts-test.futbolkolektyw.pl/")
    #     try:
    #         self.assertEqual(expected_tuple, current_title)
    #         print(f"{expected_tuple} == {current_title}")
    #     except AssertionError:
    #         print(f" {expected_tuple}: not equal title: {current_title}")
    #         self.driver.quit()

    def ternDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#     suite = TestSuite()
#     tests = unittest.TestLoader()
#     suite.addTest(tests.loadTestsFromTestCase(Test))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
