import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest

from SauceLabs.Pages.detailsPage import DetailsPage
from SauceLabs.Pages.inventoryPage import InventoryPage
from SauceLabs.Tests.login import LoginTest


class InventoryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service("C:/Users/marco/PycharmProjects/python_pom/Drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_validate_item_values_across_screens(self):
        driver = self.driver

        LoginTest.test_valid_login(self)

        inventoryPage = InventoryPage(driver)
        item_elements = inventoryPage.get_single_item_elements('Sauce Labs Backpack')
        item_text_values = inventoryPage.get_single_item_text(item_elements['name'].text)
        inventoryPage.click_on_item_image(item_elements['name'].text)

        detailsPage = DetailsPage(driver)
        print(detailsPage.compare_values(item_text_values))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
