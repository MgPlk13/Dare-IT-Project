from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    # def clear(self, lacator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(lacator)).clear()

    def send_Key(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).sens_key(text)

    # def title_(self, locator, title):
    #     return WebDriverWait(self.driver, 10).until(EC.title_is(title))
