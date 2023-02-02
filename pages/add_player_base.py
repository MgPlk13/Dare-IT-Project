import time
from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_xpath = "//*[@href='/en/players/add']"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    birthday_xpath = "//*[@name='age']"
    position_xpath = "//*[@name='mainPosition']"
    button_xpath = "//*[@type='submit']"

    """ Send element at form add player """

    def form_add_players(self, email, name, surname, birthday, position):
        self.clickElement(self.add_player_xpath)
        self.sendKeys(self.email_xpath, email)
        self.sendKeys(self.name_xpath, name)
        self.sendKeys(self.surname_xpath, surname)
        self.sendKeys(self.birthday_xpath, birthday)
        self.sendKeys(self.position_xpath, position)
        self.clickElement(self.button_xpath)
