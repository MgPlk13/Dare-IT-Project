from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from recources.locators import PageLocator


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_field_xpath = driver.find_element(By.XPATH, PageLocators.login_field_xpath)
        self. password_field_xpath = driver.find_element(By.XPATH, PageLocators.password_field_xpath)










