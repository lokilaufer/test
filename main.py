import requests
import unittest


class TestYandexDiskAPI(unittest.TestCase):

    def test_create_folder_success(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": "Bearer YOUR_YANDEX_DISK_TOKEN",
            "Content-Type": "application/json"
        }
        params = {
            "path": "/test_folder"
        }
        response = requests.put(url, headers=headers, params=params)
        self.assertEqual(response.status_code, 201)

        # Check if folder exists
        response = requests.get(url, headers=headers)
        self.assertIn("/test_folder", [file['name'] for file in response.json()['items']])

    def test_create_folder_already_exists(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": "Bearer YOUR_YANDEX_DISK_TOKEN",
            "Content-Type": "application/json"
        }
        params = {
            "path": "/test_folder"
        }

        # Attempt to create folder twice
        response1 = requests.put(url, headers=headers, params=params)
        response2 = requests.put(url, headers=headers, params=params)

        self.assertEqual(response2.status_code, 409)  # Folder already exists

    def test_create_folder_invalid_token(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            "Authorization": "Bearer INVALID_TOKEN",
            "Content-Type": "application/json"
        }
        params = {
            "path": "/test_folder"
        }
        response = requests.put(url, headers=headers, params=params)
        self.assertNotEqual(response.status_code, 201)  # Token is invalid


if __name__ == '__main__':
    unittest.main()


def get_top_mentors():
    return None
