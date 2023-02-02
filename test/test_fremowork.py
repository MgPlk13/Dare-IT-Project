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

    def getTitle(self, url):
        self.driver.get(url)
        return self.driver.title

    def test_check_title(self):
        actialTitle = self.getTitle("https://scouts-test.futbolkolektyw.pl/")
        expectedTitle = "Scouts panel"
        assert actialTitle != expectedTitle

    def test_login(self):
        str_ = "@"
        self.assertIn(str_, self.login_)

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
