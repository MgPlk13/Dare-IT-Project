import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import *



class Test(unittest.TestCase):
    login_ = "user01@getnada.com"
    password_ = "Test-1234"

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()

    def test_run(self):
        log = LoginPage(self.driver)
        # log.pageTitle()
        time.sleep(2)
        log.setUsername(self.login_)
        time.sleep(2)
        log.setPassword(self.password_)
        time.sleep(3)
        log.clickSingIn()
        time.sleep(2)
        # dashboard_page = Dashboard(self.driver)
        # dashboard_page.title_of_page()


    def ternDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
