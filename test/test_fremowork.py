from selenium import webdriver
import pytest
from pages.base_page import BasePage
from pages.login_page import PageLocators


class GetPage(BasePage):

    def set_(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en/login?redirected=true")



# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture()
# def init_driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#
#     driver.quit()
