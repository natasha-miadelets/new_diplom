from pages.base_page import BasePage
from locators.Logout_Page_Locators import LogoutPageLocators


class LogoutPage(BasePage):

    def should_be_logout_page(self):
        logout_head_text = self.find_element(
            LogoutPageLocators.LOCATOR_HEAD_TEXT).text
        assert logout_head_text == "Logged out",\
            f'Logged out not eq {logout_head_text}'

    def login_again(self):
        self.find_element(LogoutPageLocators.LOCATOR_LOGIN_BUTTON).click()
