from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from SauceLabs.env import constants
from SauceLabs.pages.details_page import DetailsPage
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage
import unittest


class InventoryTest(unittest.TestCase):

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
        self.assertTrue(inventory_page.validate_inventory_url())

    def test_compare_inventory_vs_details(self):
        inventory_page = InventoryPage(self.driver)
        # obtener un item por posicion
        inventory_item = inventory_page.get_current_inventory_item_text('Sauce Labs Fleece Jacket')
        inventory_page.click_on_inventory_item_title('Sauce Labs Fleece Jacket')
        details_page = DetailsPage(self.driver)
        details_item = details_page.get_details_text()
        self.assertEqual(inventory_item, details_item, constants.ERROR_INVENTORY_VS_DETAILS)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

