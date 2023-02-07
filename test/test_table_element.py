import unittest
import os
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.web_elament_page import WebElementPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/pl/players?lng=pl&subpath=pl&start=1")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.web_el = WebElementPage(self.driver)
        self.logo = LoginPage(self.driver)

    def test_login_in_system(self):
        self.logo.logo_in_form(*self.logo.tuple_logo_in_form)
        self.web_el.click_()
        self.web_el.find_web_element()
        time.sleep(2)



    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
