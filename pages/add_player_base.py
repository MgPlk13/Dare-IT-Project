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

    tuple_players = ("python123@gmail.com", "Python", "Developer", "21/03/2000", "junior")

    """ Send element at form add player """

    def form_add_players(self, email, name, surname, birthday, position):
        self.click_element(self.add_player_xpath)
        self.send_keys(self.email_xpath, email)
        self.send_keys(self.name_xpath, name)
        self.send_keys(self.surname_xpath, surname)
        self.send_keys(self.birthday_xpath, birthday)
        self.send_keys(self.position_xpath, position)
        self.click_element(self.button_xpath)
