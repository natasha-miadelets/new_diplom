import allure
from pages.api_page import Api
from time import sleep


@allure.feature('API test')
def test_add_update_pet():
    with allure.step('add pet in the store'):
        api_page = Api()
        api_page.add_new_pet()
        # sleep(5)
    with allure.step('check that pet is added'):
        api_page = Api()
        api_page.check_added_pet()
        # sleep(5)
    with allure.step('update pet name'):
        api_page = Api()
        api_page.update_pet_name()
        # sleep(5)
    with allure.step('check that pet name is updated'):
        api_page = Api()
        api_page.check_updated_name()
