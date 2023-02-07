import unittest
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dropdown_element_page import DropdownElement
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
        self.logo = LoginPage(self.driver)
        self.dopdown_choice = DropdownElement(self.driver)

    def test_choice_language(self):
        time.sleep(3)
        asd = self.dopdown_choice.dropdown()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
