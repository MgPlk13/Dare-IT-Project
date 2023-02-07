from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from utils.settings import DRIVER_PATH

from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class WebElementPage(BasePage):
    web_element_name_xpath = "//tr[@id='MUIDataTableBodyRow-0']/td"
    web_element_button_xpath = "//ul[1]/div[2]/div[2]/span"

    def click_(self):
        self.click_element(self.web_element_button_xpath)

    def find_web_element(self):
        data = []
        elems = self.find_elems(self.web_element_name_xpath)
        for elem in elems:
            data.append(elem.text)
        print(data)





