import time
from pages.base_page import BasePage


class AddPlayer(BasePage):
      add_player_url = "https://scouts-test.futbolkolektyw.pl/"
      add_player_xpath = "//*[@href='/en/players/add']"

      def clickAddPlayer(self):
          self.clickElement(self.add_player_xpath)
