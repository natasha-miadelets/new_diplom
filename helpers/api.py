import requests
import json


class Api:

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2/pet"

    def add_new_pet(self, id: int, name: str):
        data_add_pet = {"id": id,
                        "category": {"id": 0, "name": "string"},
                        "name": name,
                        "photoUrls": ["string"],
                        "tags": [{"id": 0, "name": "string"}],
                        "status": "available"}
        headers_add_pet = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.post(self.base_url, headers=headers_add_pet, data=json.dumps(data_add_pet))
        status_code = response.status_code
        assert status_code == 200, f'{status_code} invalid status code'

    def check_added_pet(self, id: int):
        check_pet_url = self.base_url + f"/{id}"
        headers_check_added_pet = {'accept': 'application/json'}
        response = requests.get(check_pet_url, headers=headers_check_added_pet)
        i = 0
        while response.json().get('id') != id and i != 5:
            response = requests.get(check_pet_url, headers=headers_check_added_pet)
            i += 1
        return response.json()

    def update_pet_name(self, id: int, new_name: str):
        new_data_for_pet = {"id": id,
                            "category": {"id": 0, "name": "string"},
                            "name": new_name,
                            "photoUrls": ["string"],
                            "tags": [{"id": 0, "name": "string"}],
                            "status": "available"}
        headers_update_pet_name = {'accept': 'application/json', 'content-type': 'application/json'}
        response = requests.put(self.base_url, headers=headers_update_pet_name, data=json.dumps(new_data_for_pet))
        status_code = response.status_code
        assert status_code == 200, f'{status_code} invalid status code'

    def check_updated_name(self, id: int, new_name: str):
        check_updated_name_url = self.base_url + f"/{id}"
        headers_check_updated_name = {'accept': 'application/json'}
        response = requests.get(check_updated_name_url, headers=headers_check_updated_name)
        i = 0
        while response.json().get('name') != new_name and i != 5:
            response = requests.get(check_updated_name_url, headers=headers_check_updated_name)
            i += 1
        return response.json()
