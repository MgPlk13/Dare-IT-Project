from pages.base_page import BasePage


class PageLocator(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sing_in_button_xpath = "//button[@type='submit']/span[2]" "//*[@class='MuiTouchRipple-root']"
    email_xpath = "path.it.user01@getnada.com" "//*[@value='user01@getnada.com']"
