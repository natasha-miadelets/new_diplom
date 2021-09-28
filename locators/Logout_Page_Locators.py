from selenium.webdriver.common.by import By


class LogoutPageLocators:

    LOCATOR_HEAD_TEXT = (By.XPATH, "//h1[text()='Logged out']")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//a[text()='Log in again']")
