from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

import time

from SauceLabs.env import constants
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.service = Service(constants.CHROME_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(constants.SAUCE_DEMO_URL)

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)
        inventory_page = InventoryPage(self.driver)
        self.assertTrue(inventory_page.validate_login())
        # crear test case nuevo para logout.
        # cada test case tenga solo 1 assert
        inventory_page.logout()
        self.assertTrue(login_page.validate_logout())

    def test_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.login(constants.VALID_USER, constants.INVALID_PASSWORD)
        self.assertTrue(login_page.validate_incorrect_password(constants.ERROR_INVALID_PASSWORD))

    def test_no_username(self):
        login_page = LoginPage(self.driver)
        login_page.login(constants.EMPTY_VALUE, constants.VALID_PASSWORD)
        self.assertTrue(login_page.validate_incorrect_password(constants.ERROR_NO_USERNAME))

    def test_no_password(self):
        login_page = LoginPage(self.driver)
        login_page.login(constants.VALID_USER, constants.EMPTY_VALUE)
        self.assertTrue(login_page.validate_incorrect_password(constants.ERROR_NO_PASSWORD))

    def test_locked_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(constants.LOCKED_USER, constants.VALID_PASSWORD)
        self.assertTrue(login_page.validate_incorrect_password(constants.ERROR_LOCKED_USER))

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
