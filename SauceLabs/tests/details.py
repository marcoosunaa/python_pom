from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from SauceLabs.env import constants
from SauceLabs.pages.details_page import DetailsPage
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage
import unittest


class DetailsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.service = Service(constants.CHROME_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(constants.SAUCE_DEMO_URL)
        login_page = LoginPage(self.driver)
        login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)

    def test_url(self):
        inventory_page = InventoryPage(self.driver)



    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()