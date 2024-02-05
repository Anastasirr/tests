from unittest import TestCase
from settings import token
import requests

url_api = 'https://cloud-api.yandex.net/v1/disk/resources'

headers = {
    'Authorization': token,
}


class TestYaDisk(TestCase):
    def test_create_folder(self):
        name_folder = 'Test_create_folder'
        url_fold = f'{url_api}?path={name_folder}'
        response = requests.put(url_fold, headers=headers)

        self.assertEqual(response.status_code, 201)

    def test_get_info_folder(self):
        name_folder_info = 'Test_authorize_folder'
        url_auth_fold = f'{url_api}?path={name_folder_info}'
        response = requests.put(url_auth_fold, headers=headers)

        self.assertNotEqual(response.status_code, 401)


