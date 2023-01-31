from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sendKeys(self, selector, value):
        return self.driver.find_element(By.XPATH, selector).send_keys(value)

    def clickElement(self, selector):
        return self.driver.find_element(By.XPATH, selector).click()

    def getTitle(self, url):
        self.driver.get(url)
        return self.driver.title
