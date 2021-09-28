from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.posts_page import PostsPage
import allure


@allure.feature('Delete image and check that image is deleted')
def test_delete_image(browser):
    with allure.step('open main page'):
        main_page = MainPage(browser)
        main_page.open_main_page()
    with allure.step('check first image date'):
        main_page = MainPage(browser)
        main_page.first_image_date()
    with allure.step('click on the go to admin button'):
        main_page = MainPage(browser)
        main_page.open_login_page()
    with allure.step('user is on login page'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('user login'):
        login_page = LoginPage(browser)
        login_page.login('admin', 'password')
    with allure.step('admin panel page is open'):
        admin_page = AdminPage(browser)
        admin_page.should_be_admin_page()
    with allure.step('click on the change post button'):
        admin_page = AdminPage(browser)
        admin_page.click_change_post_button()
    with allure.step('posts page is open'):
        posts_page = PostsPage(browser)
        posts_page.should_be_posts_page()
    with allure.step('delete first post'):
        posts_page = PostsPage(browser)
        posts_page.delete_post()
    with allure.step('go to main page'):
        posts_page = PostsPage(browser)
        posts_page.go_to_main_page()
    with allure.step('check that image is deleted'):
        main_page = MainPage(browser)
        main_page.check_deleted_image()
