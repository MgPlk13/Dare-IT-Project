from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sing_in_button_xpath = "//button[@type='submit']/span[1]"
    # expected_title = "//*[contains(text(),'Scouts panel')]"
    # title_url = "https://scouts-test.futbolkolektyw.pl/"
    # text_xpath = "//h5[@class= 'MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom']"

    tuple_logo_in_form = ("user01@getnada.com",
                          "Test-1234")

    def logo_in_form(self, login, password):
        self.send_keys(self.login_field_xpath, login)
        self.send_keys(self.password_field_xpath, password)
        self.click_element(self.sing_in_button_xpath)

