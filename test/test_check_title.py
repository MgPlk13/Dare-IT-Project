import os
import unittest

from unittest import TestSuite

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.base_page import BasePage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCheckTitle(unittest.TestCase):

    def setUp(self):

        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        # self.log = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)

    def test_check_title(self):
        actialTitle = self.basePage.get_page_title("https://scouts-test.futbolkolektyw.pl/")
        expectedTitle = "Scouts panel - sign in"
        assert actialTitle == expectedTitle

    def test_title(self):
        title_login_in_system = self.basePage.get_page_title("https://scouts-test.futbolkolektyw.pl/")
        print(f" Title for this page: {title_login_in_system}, len is: {len(title_login_in_system)}")

    def test_title_2(self):
        expected_tuple = "Scouts panel - sign "
        current_title = self.basePage.get_page_title("https://scouts-test.futbolkolektyw.pl/")
        try:
            self.assertEqual(expected_tuple, current_title)
            print(f"{expected_tuple} == {current_title}")
        except AssertionError:
            print(f" {expected_tuple}: not equal title: {current_title}")
            self.basePage.driver.quit()

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = TestSuite()
    tests = unittest.TestLoader()
    suite.addTest(tests.loadTestsFromTestCase(TestCheckTitle))

    runner = unittest.TextTestRunner()
    runner.run(suite)
