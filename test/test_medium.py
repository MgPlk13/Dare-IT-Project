import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage


class Test(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://medium.com/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.title_ = BasePage(self.driver)

    def test_check_title(self):
        actialTitle = self.title_.get_page_title("https://medium.com/")
        expectedTitle = "Medium_"
        assert actialTitle != expectedTitle
        time.sleep(3)

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
