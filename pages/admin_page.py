from pages.base_page import BasePage
from locators.Admin_Page_Locators import AdminPageLocators
import psycopg2


class AdminPage(BasePage):

    def should_be_admin_page(self):
        head_admin_text = self.find_element(
            AdminPageLocators.LOCATOR_HEAD_TEXT).text
        assert head_admin_text == "Site administration",\
            f'Site administration not eq {head_admin_text}'

    def add_user(self, email: str, passwd: str):
        self.find_element(AdminPageLocators.LOCATOR_ADD_USER_BUTTON).click()
        username_field = self.find_element(AdminPageLocators.LOCATOR_USERNAME_FIELD)
        username_field.send_keys(email)
        password = self.find_element(AdminPageLocators.LOCATOR_PASSWORD_FIELD)
        password.send_keys(passwd)
        password_conf = self.find_element(AdminPageLocators.LOCATOR_PASSWORD_CONF_FIELD)
        password_conf.send_keys(passwd)
        save_button = self.find_element(AdminPageLocators.LOCATOR_SAVE_BUTTON)
        save_button.click()

    def user_is_added(self, user_mame: str):
        psycopg2.connect(host='localhost',
                         user='postgres',
                         password='postgres')
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='postgres',
                                host='localhost')

        cursor = conn.cursor()
        query = "SELECT object_repr FROM django_admin_log"
        cursor.execute(query)
        users = cursor.fetchall()

        user_list = list(sum(users, ()))

        for i in user_list:
            if i == user_mame:
                a = []
                a.append(i)
                assert a[0] == user_mame, f'{a[0]} not eq {user_mame}'

    def logout(self):
        self.find_element(AdminPageLocators.LOCATOR_LOGOUT_BUTTON).click()

    def check_user_account(self, username: str):
        username_text = self.find_element(
            AdminPageLocators.LOCATOR_CHECK_USERNAME).text
        assert username_text == username.upper(), \
            f'{username} not eq {username_text}'

    def add_permission(self):
        self.find_element(AdminPageLocators.LOCATOR_CHECKBOX_STAFF).click()
        self.find_element(AdminPageLocators.LOCATOR_CHECKBOX_SUPERUSER).click()
        self.find_element(AdminPageLocators.LOCATOR_SAVE_BUTTON_2).click()

    def click_change_post_button(self):
        self.find_element(AdminPageLocators.LOCATOR_CHANGE_POSTS).click()
