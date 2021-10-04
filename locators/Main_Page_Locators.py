from selenium.webdriver.common.by import By


class MainPageLocators:

    LOCATOR_GO_TO_ADMIN_BUTTON = (By.XPATH, "//a[text()='Go to Admin']")
    LOCATOR_HEAD_TEXT = (By.XPATH, "//h1[text()='Simple Django Application']")
    LOCATOR_FIRST_IMAGE = (By.XPATH, "//div[@class='col-md-4']/div/img")
