from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOCATOR_HEAD_TEXT = (By.XPATH, "//a[text()='Django administrationn']")
    LOCATOR_USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")

