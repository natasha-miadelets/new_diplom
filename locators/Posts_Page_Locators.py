from selenium.webdriver.common.by import By


class PostsPageLocators:

    LOCATOR_HEAD_TEXT = (By.XPATH, "//h1[text()='Select post to change']")
    LOCATOR_FIRST_POST = (By.XPATH, "//table[@id='result_list']/tbody/tr/th/a")
    LOCATOR_DELETE_BUTTON = (By.XPATH, "//a[text()='Delete']")
    LOCATOR_SURE_BUTTON = (By.XPATH, "//input[@value='Yes, I’m sure']")
    LOCATOR_VIEW_SITE_BUTTON = (By.XPATH, "//a[text()='View site']")
