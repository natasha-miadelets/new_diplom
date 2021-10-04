from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.logout_page import LogoutPage
from helpers.db import DB
import random
import allure

USER_NAME = "natasha" + str(random.randint(1, 100))
PASSWORD = "miadelets" + str(random.randint(1, 100))


@allure.feature('Create new user')
def test_create_new_user(browser, connect_with_db):
    with allure.step('open main page'):
        main_page = MainPage(browser)
        main_page.open_main_page()
    with allure.step('click on the go to admin button'):
        main_page.open_login_page()
    with allure.step('user is on login page'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('user enter admin data'):
        login_page.login('admin', 'password')
    with allure.step('admin panel page is open'):
        admin_page = AdminPage(browser)
        admin_page.should_be_admin_page()
    with allure.step('admin add new user'):
        admin_page.add_user(USER_NAME, PASSWORD)
    with allure.step('admin add permissions for new user'):
        admin_page.add_permission()
    with allure.step('check that new user is on db'):
        db = DB()
        cursor = connect_with_db
        db.user_is_added(USER_NAME, cursor)
    with allure.step('admin logout'):
        admin_page.logout()
    with allure.step('logout page is open'):
        logout_page = LogoutPage(browser)
        logout_page.should_be_logout_page()
    with allure.step('click log in again button'):
        logout_page.login_again()
    with allure.step('user is on login page'):
        login_page.should_be_login_page()
    with allure.step('new user log in'):
        login_page.login(USER_NAME, PASSWORD)
    with allure.step('new user account is open'):
        admin_page.check_user_account(USER_NAME)
