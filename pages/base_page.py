import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.settings import DEFAUlD_LOCATOR_TYPE


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def send_keys(self, selector, value, locator_type=DEFAUlD_LOCATOR_TYPE):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_element(self, selector, locator_type=DEFAUlD_LOCATOR_TYPE):
        return self.driver.find_element(locator_type, selector).click()

    # def click_dropdown_element(self, selector, locator_type=TEXT_LOCATOR_TYPE):
    #     return self.driver.find_element(locator_type).click()

    def find_elems(self, selector, locator_type=DEFAUlD_LOCATOR_TYPE):
        return self.driver.find_elements(locator_type, selector)


    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    # def wait_for_element_to_be_clickable(self, selector, locator_type=DEFAUlD_LOCATOR_TYPE):
    #     wait = WebDriverWait(self.driver, 10)
    #     element = wait.until(EC.element_to_be_clickable((locator_type, selector)))



    # def getTitle(self, url):
    #     self.driver.get(url)
    #     return self.driver.title

    # def assert_element_text(self, driver, selector, text):
    #     element_driver = self.driver.find_element(by=By.XPATH, value=selector)
    #     element_text = element_driver.text
    #     assert element_driver == element_text
