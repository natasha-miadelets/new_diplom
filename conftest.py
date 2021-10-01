import os
from datetime import datetime

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
def connect_disconnect_with_db():
    db = DB()
    yield
    db.close_cursor()


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

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     if not os.path.exists('reports'):
#         os.makedirs('reports')
#     config.option.htmlpath = f'html_reports/ {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'
