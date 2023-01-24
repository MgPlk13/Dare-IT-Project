from test.test_fremowork import SetUp


class HomePageTest(SetUp):

    def test_home_page(self):
        driver = self.driver
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en/login?redirected=true")





if __name__ == '__main__':
   pass


