import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import *



class Test(unittest.TestCase):
    element_xpath = "//h6[@class='MuiTypography-root jss16 MuiTypography-h6 MuiTypography-noWrap']"
    value_ = "Scouts panel"
    tuple_logo_in_form = ("user01@getnada.com",
                          "Test-1234")

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.log = LoginPage(self.driver)

    def test_run(self):
        self.log.logo_in_form(*self.tuple_logo_in_form)
        time.sleep(2)
        # dashboard_page = Dashboard(self.driver)
        # dashboard_page.title_of_page()

    def test_true_element_test(self):
        # log = LoginPage(self.driver)
        # log.setUsername(self.login_)
        # log.setPassword(self.password_)
        # log.clickSingIn()
        text = BasePage(self.driver)
        text.assert_element_text(self.element_xpath, self.value_)
        # assert actialTitle != expectedTitle

    def ternDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
