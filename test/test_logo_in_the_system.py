import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


class Test(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.log = LoginPage(self.driver)

    def test_login_in_system(self):
        self.log.logo_in_form(*self.log.tuple_logo_in_form)
        time.sleep(4)

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
