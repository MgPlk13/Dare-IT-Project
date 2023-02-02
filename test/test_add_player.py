import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_player_base import AddPlayer
from pages.login_page import LoginPage
from recources.locators import TupleAddPlayers


class TestPlayer(unittest.TestCase):
    tuple_logo_in_form = ("user01@getnada.com",
                          "Test-1234")

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()
        self.players = AddPlayer(self.driver)
        self.logo = LoginPage(self.driver)

    def test_add_player(self):
        self.logo.logo_in_form(*self.tuple_logo_in_form)
        time.sleep(3)
        self.players.form_add_players(*TupleAddPlayers.tuple_players)
        time.sleep(3)

    def ternDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
