from pages.base_page import BasePage
from locators.Login_Page_Locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        head_login_text = self.find_element(
            LoginPageLocators.LOCATOR_HEAD_TEXT).text
        assert head_login_text == "Django administration",\
            f'Django administration not eq {head_login_text}'

    def login(self, email: str, passwd: str):
        username = self.find_element(LoginPageLocators.LOCATOR_USERNAME_FIELD)
        username.send_keys(email)
        password = self.find_element(LoginPageLocators.LOCATOR_PASSWORD_FIELD)
        password.send_keys(passwd)
        login_button = self.find_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON)
        login_button.click()

