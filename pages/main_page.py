from pages.base_page import BasePage
from locators.Main_Page_Locators import MainPageLocators


class MainPage(BasePage):

    def should_be_main_page(self):
        head_text = self.find_element(
            MainPageLocators.LOCATOR_HEAD_TEXT).text
        assert head_text == "Simple Django Application",\
            f'Simple Django Application not eq {head_text}'

    def open_login_page(self):
        self.find_element(MainPageLocators.LOCATOR_GO_TO_ADMIN_BUTTON).click()

    def first_image_date(self):
        self.image = self.find_element(MainPageLocators.LOCATOR_FIRST_IMAGE).text

    def check_deleted_image(self):
        find_image = self.find_element(MainPageLocators.LOCATOR_FIRST_IMAGE).text
        assert find_image != self.image, f'{self.image} eq {find_image}'

