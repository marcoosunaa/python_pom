"""
import all needed modules
"""
from selenium.webdriver.common.by import By
from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage


class DetailsPage(BasePage):
    """
    Dictionaries with locators of each webElement
    """
    details_back_to_products = {'by': By.CSS_SELECTOR, 'value': '#back-to-products'}
    details_item_img = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_img'}
    details_item_title = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_name'}
    details_item_description = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_desc'}
    details_item_price = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_price'}
    details_item_button = {'by': By.CSS_SELECTOR, 'value': '.btn_primary'}

    def validate_details_url(self):
        """
        Validates that url contains substring
        :return: if url meets conditions
        """
        return constants.DETAILS_URL in self.get_url()

    def get_details_text(self):
        """
        function to get text values of current item
        :return: dictionary with text values
        """
        current_item = {
            'title': self.get_text(self.details_item_title),
            'description': self.get_text(self.details_item_description),
            'price': self.get_text(self.details_item_price),
            'button': self.get_text(self.details_item_button)
        }
        return current_item
