from pages.base_page import BasePage



class LoginPage(BasePage):

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sing_in_button_xpath = "//button[@type='submit']/span[1]"
    expected_title = "//*[contains(text(),'Scouts panel')]"
    title_url = "https://scouts-test.futbolkolektyw.pl/"
    # expectedTitle = "Scouts panel"
    # login_true = "user01@getnada.com"
    # password_true = "Test-1234"

    a = {'login': "//*[@id='login']",
        'password': "//*[@id='password']"}


    def logo_in_form(self, login, password):
        self.sendKeys(self.login_field_xpath, login)
        self.sendKeys(self.password_field_xpath, password)
        self.clickElement(self.sing_in_button_xpath)


    # def pageTitle(self):
    #     assert self.getTitle(self.title_url) == self.expectedTitle









