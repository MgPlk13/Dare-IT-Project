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
        self.driver.get("https://medium.com/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()


    def test_check_title(self):
        actialTitle = self.getTitle("https://medium.com/")
        expectedTitle = "Medium_"
        assert actialTitle != expectedTitle


    def getTitle(self, url):
        self.driver.get(url)
        return self.driver.title




    def ternDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
