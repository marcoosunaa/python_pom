import time

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

    def test_click_on_title(self):
        inventory_page = InventoryPage(self.driver)
        position = inventory_page.get_random_number()
        inventory_item = inventory_page.get_specific_inventory_item_text(position)
        inventory_page.click_on_inventory_item_title(position)
        details_page = DetailsPage(self.driver)
        details_item = details_page.get_details_text()
        self.assertEqual(inventory_item, details_item, constants.ERROR_INVENTORY_VS_DETAILS)

    def test_click_on_img(self):
        inventory_page = InventoryPage(self.driver)
        position = inventory_page.get_random_number()
        inventory_item = inventory_page.get_specific_inventory_item_text(position)
        inventory_page.click_on_inventory_item_img(position)
        details_page = DetailsPage(self.driver)
        details_item = details_page.get_details_text()
        self.assertEqual(inventory_item, details_item, constants.ERROR_INVENTORY_VS_DETAILS)

    def test_add_to_cart(self):
        inventory_page = InventoryPage(self.driver)
        position = inventory_page.get_random_number()
        inventory_page.click_on_inventory_item_button(position)
        inventory_page.get_shopping_cart_number()
        self.assertTrue(inventory_page.get_shopping_cart_number() == '1')

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
