import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestYandexAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.yandex.ru/auth/")

    def test_successful_authorization(self):
        login = self.driver.find_element_by_id("pass-field-login")
        password = self.driver.find_element_by_id("pass-field-passwd")
        submit_button = self.driver.find_element_by_xpath('//button[@type="submit"]')

        login.send_keys("your_username")
        password.send_keys("your_password")
        submit_button.click()

        time.sleep(5)  # waiting for page to load

        welcome_message = self.driver.find_element_by_xpath('//div[@class="personal-info__text"]')
        self.assertEqual(welcome_message.text, "Привет, your_username!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
