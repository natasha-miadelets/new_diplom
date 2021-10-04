import allure
from helpers.db import DB
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome("./chromedriver 3", chrome_options=chrome_options)
    browser = webdriver.Chrome("./chromedriver 3")
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def connect_with_db():
    db = DB()
    conn = db.create_connection()
    cursor = conn.cursor()
    yield cursor
    cursor.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                print('Does not have browser fixture')
                return
            allure.attach(browser.get_screenshot_as_png(), "Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f'Failed to make screensot: {e}')
