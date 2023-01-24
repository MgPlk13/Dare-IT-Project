from pages.base_page import BasePage


class AddMatchFormLocators(BasePage):
    menu_player = "//*[@class='MuiList-root MuiList-padding']/div[2]"
    presentation = "//*[@class='MuiList-root MuiList-padding']/parent::div"
    button_submit = "//*[@type='submit']"
    button_clear = "//*[@class='MuiCardActions-root MuiCardActions-spacing']/button[2]"
    previous_element = "//*[@class='MuiList-root MuiList-padding']/following-sibling::*"
    ancestor_element = "//*[@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button']" \
                       "/ancestor::u"
    child_element = "//*[@class='MuiList-root MuiList-padding']/child::*"

