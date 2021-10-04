import allure
from helpers.api import Api
import random

PET_ID = random.randint(1, 9000000)
PET_NAME = "MIKI"
PET_NEW_NAME = "MIKI_NEW"


@allure.feature('API test')
def test_add_update_pet():
    with allure.step(f'add pet with random id {PET_ID} in the store'):
        api_page = Api()
        api_page.add_new_pet(PET_ID, PET_NAME)
    with allure.step('check that pet is added'):
        api_page.check_added_pet(PET_ID)
    with allure.step(f'update pet name {PET_NAME} to {PET_NEW_NAME}'):
        api_page.update_pet_name(PET_ID, PET_NEW_NAME)
    with allure.step('check that pet name is updated'):
        api_page.check_updated_name(PET_ID, PET_NEW_NAME)
