import unittest
import os
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_player_base import AddPlayer
from pages.login_page import LoginPage




class Test_player(unittest.TestCase):
    login_ = "user01@getnada.com"
    password_ = "Test-1234"

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en")
        self.driver.implicitly_wait((IMPLICITLY_WAIT))
        self.driver.fullscreen_window()



    def test_add_player(self):
        log = LoginPage(self.driver)
        log.setUsername(self.login_)
        log.setPassword(self.password_)
        log.clickSingIn()
        players = AddPlayer(self.driver)
        time.sleep(3)
        players.clickAddPlayer()
        time.sleep(3)


    def ternDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
