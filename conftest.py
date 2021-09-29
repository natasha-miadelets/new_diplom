import os
from datetime import datetime
from helpers.db import DB
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome("./chromedriver 3", chrome_options=chrome_options)
    # browser = webdriver.Chrome("./chromedriver 3")
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def connect_disconnect_with_db():
    db = DB()
    yield
    db.close_cursor()


# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     if not os.path.exists('reports'):
#         os.makedirs('reports')
#     config.option.htmlpath = f'html_reports/ {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'


