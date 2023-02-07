import time
from pages.base_page import BasePage


class DropdownElement(BasePage):
    button_language_xpath = "//*[@class='MuiSelect-root MuiSelect-select" \
                            " MuiSelect-selectMenu MuiInputBase-input MuiInput-input']"
    ul_button = "//*[@data-value='pl']"

    def dropdown(self):
        self.click_element(self.button_language_xpath)
        self.click_element(self.ul_button)
