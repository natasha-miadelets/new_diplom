from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.logout_page import LogoutPage
import random
import allure

USER_NAME = "natasha" + str(random.randint(1, 100))
PASSWORD = "miadelets" + str(random.randint(1, 100))


@allure.feature('Create new user')
def test_create_new_user(browser):
    with allure.step('open main page'):
        main_page = MainPage(browser)
        main_page.open_main_page()
    with allure.step('click on the go to admin button'):
        main_page = MainPage(browser)
        main_page.open_login_page()
    with allure.step('user is on login page'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('user enter admin data'):
        login_page = LoginPage(browser)
        login_page.login('admin', 'password')
    with allure.step('admin panel page is open'):
        admin_page = AdminPage(browser)
        admin_page.should_be_admin_page()
    with allure.step('add new user'):
        admin_page = AdminPage(browser)
        admin_page.add_user(USER_NAME, PASSWORD)
    with allure.step('user is added'):
        admin_page = AdminPage(browser)
        admin_page.user_is_added(USER_NAME)
    with allure.step('add permissions for user'):
        admin_page = AdminPage(browser)
        admin_page.add_permission()
    with allure.step('permissions is added'):
        admin_page = AdminPage(browser)
        admin_page.user_is_added(USER_NAME)
    with allure.step('user logout'):
        admin_page = AdminPage(browser)
        admin_page.logout()
    with allure.step('logout page is open'):
        logout_page = LogoutPage(browser)
        logout_page.should_be_logout_page()
    with allure.step('click log in again button'):
        logout_page = LogoutPage(browser)
        logout_page.login_again()
    with allure.step('user is on login page'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('user log in again'):
        login_page = LoginPage(browser)
        login_page.login(USER_NAME, PASSWORD)
    with allure.step('user account is open'):
        admin_page = AdminPage(browser)
        admin_page.check_user_account(USER_NAME)
