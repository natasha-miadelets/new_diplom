from selenium.webdriver.common.by import By


class AdminPageLocators:

    LOCATOR_HEAD_TEXT = (By.XPATH, "//h1[text()='Site administration']")
    LOCATOR_ADD_USER_BUTTON = (By.XPATH, "//tr[@class='model-user']/td/a")
    LOCATOR_USERNAME_FIELD = (By.XPATH, "//input[@name='username']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//input[@name='password1']")
    LOCATOR_PASSWORD_CONF_FIELD = (By.XPATH, "//input[@name='password2']")
    LOCATOR_SAVE_BUTTON = (By.XPATH, "//input[@value='Save']")
    LOCATOR_SUCCESS_MESSAGE = (By.XPATH, "//li[@class='success']")
    LOCATOR_CHECKBOX_STAFF = (By.XPATH, "//input[@name='is_staff']")
    LOCATOR_CHECKBOX_SUPERUSER = (By.XPATH, "//input[@name='is_superuser']")
    LOCATOR_SAVE_BUTTON_2 = (By.XPATH, "//input[@value='Save']")
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    LOCATOR_CHECK_USERNAME = (By.XPATH, "//div[@id='user-tools']/strong")
    LOCATOR_CHANGE_POSTS = (By.XPATH, "//tr[@class='model-post']/td/a[text()='Change']")

