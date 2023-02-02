from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sendKeys(self, selector, value):
        return self.driver.find_element(By.XPATH, selector).send_keys(value)

    def clickElement(self, selector):
        return self.driver.find_element(By.XPATH, selector).click()

    def getTitle(self, url):
        return self.driver.title

    def assert_element_text(self, selector, text_value):
        element = self.driver.find_element(By.XPATH, value=selector)
        element_text = element.text
        assert text_value == element_text
