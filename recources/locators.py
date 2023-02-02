from pages.base_page import BasePage



login_field_xpath = "//*[@id='login']"
password_field_xpath = "//*[@id='password']"
sing_in_button_xpath = "//button[@type='submit']/span[2]"       # "//*[@class='MuiTouchRipple-root']"
# email_xpath = "path.it.user01@getnada.com"                      # "//*[@value='user01@getnada.com']"

class TupleAddPlayers(object):

    tuple_players = ("python123@gmail.com",  "Python", "Developer", "21/03/2000", "junior")
