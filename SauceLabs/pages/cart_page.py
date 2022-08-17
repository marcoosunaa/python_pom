"""
import all needed modules
"""
from selenium.webdriver.common.by import By
from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage


class CartPage(BasePage):
    """
    Dictionaries with locators of each webElement
    """
    continue_shopping_button = {'by': By.ID, 'value': 'continue-shopping'}
    checkout_button = {'by': By.ID, 'value': 'checkout'}
    cart_all_items = {'by': By.CSS_SELECTOR, 'value': '.cart_item'}
    item_title = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_name'}
    item_description = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_desc'}
    item_price = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_price'}
    item_button = {'by': By.CSS_SELECTOR, 'value': '.btn'}
    item_quantity = {'by': By.CSS_SELECTOR, 'value': '.cart_quantity'}

    def validate_url(self):
        """
        function to get url of browser
        :return: string with url
        """
        return self.get_url() == constants.CART_URL

    def get_all_cart_elements(self):
        """
        function to get all items within the cart
        :return: dictionary with current item
        """
        current_item = {'title': self.get_title_element(),
                        'description': self.get_description_element(),
                        'price': self.get_price_element(),
                        'button': self.get_button_element()}
        return current_item

    def get_cart_item_text(self):
        """
        function to get text of cart item
        :return list with cart items text
        """
        item = self.get_all_cart_elements()
        for key in item:
            item[key] = item[key].text
        return item

    def get_item_quantity_element(self):
        """
        function to get quantity of item
        :return: TBD
        """
        items = self.find_all(self.cart_all_items)
        return self.find_within_element(self.item_title, items[0])

    def get_title_element(self):
        """
        function to get title of item
        :return: TBD
        """
        items = self.find_all(self.cart_all_items)
        return self.find_within_element(self.item_title, items[0])

    def get_description_element(self):
        """
        function to get description of item
        :return: TBD
        """
        items = self.find_all(self.cart_all_items)
        return self.find_within_element(self.item_description, items[0])

    def get_price_element(self):
        """
        function to get price of item
        :return: TBD
        """
        items = self.find_all(self.cart_all_items)
        return self.find_within_element(self.item_price, items[0])

    def get_button_element(self):
        """
        function to get button text of item
        :return: TBD
        """
        items = self.find_all(self.cart_all_items)
        return self.find_within_element(self.item_button, items[0])
