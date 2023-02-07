import unittest
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.clean_form import CleanForm
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
        self.clear_el = CleanForm(self.driver)
        self.logo = LoginPage(self.driver)
        self.base = BasePage(self.driver)

    def test_login_in_system(self):
        self.logo.logo_in_form(*self.logo.tuple_logo_in_form)
        self.base.click_element(self.clear_el.button_xpath)
        el = self.driver.find_elements(By.XPATH, self.clear_el.xpath)
        data = [i.send_keys(Keys.BACKSPACE * 25) for i in el if len(i.text) < 6]
        time.sleep(3)

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
