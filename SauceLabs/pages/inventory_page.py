"""
import all needed modules
"""
from selenium.webdriver.common.by import By
from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Dictionaries with locators of each webElement
    """
    # header objects
    hamburger_menu = {'by': By.ID, 'value': 'react-burger-menu-btn'}
    all_items_button = {'by': By.ID, 'value': 'inventory_sidebar_link'}
    about_button = {'by': By.ID, 'value': 'about_sidebar_link'}
    logout_button = {'by': By.ID, 'value': 'logout_sidebar_link'}
    reset_app_state_button = {'by': By.ID, 'value': 'reset_sidebar_link'}
    hamburger_cross_button = {'by': By.ID, 'value': 'react-burger-cross-btn'}
    # inventory items object
    inventory_all_items = {'by': By.CSS_SELECTOR, 'value': '.inventory_item'}
    item_img = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_img'}
    item_title = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_name'}
    item_description = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_desc'}
    item_price = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_price'}
    item_button = {'by': By.CSS_SELECTOR, 'value': '.btn'}
    # shopping cart objects
    shopping_cart_button = {'by': By.CSS_SELECTOR, 'value': '.shopping_cart_link'}
    shopping_cart_badge = {'by': By.CSS_SELECTOR, 'value': '.shopping_cart_badge'}
    # filter objects
    filter_dropdown = {'by': By.CSS_SELECTOR, 'value': '.product_sort_container'}
    filter_option_a_to_z = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(1)'}
    filter_option_z_to_a = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(2)'}
    filter_option_low_to_high = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(3)'}
    filter_option_high_to_low = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(4)'}

    # NAVIGATION

    def validate_login(self):
        """
        validate valid login
        :return: if login was valid
        """
        return self.is_displayed(self.hamburger_menu)

    def logout(self):
        """
        function to logout
        """
        self.click(self.hamburger_menu)
        self.click(self.logout_button)

    def validate_url(self):
        """
        Validate current url matches constant value
        :return: if current url matches constant value
        """
        return self.get_url() == constants.INVENTORY_URL

    def navigate_to_about(self):
        """
        function to navigate to about url
        :return: if url matches constant value
        """
        self.click(self.hamburger_menu)
        self.click(self.about_button)
        return self.driver.current_url == constants.ABOUT_SAUCE_URL

    # INVENTORY

    def get_all_item_elements(self, position):
        """
        function to get all elements of an item
        :param position: Item that will be focused
        :return: all webElements of an item
        """
        current_item = {'img': self.get_img_element(position),
                        'title': self.get_title_element(position),
                        'description': self.get_description_element(position),
                        'price': self.get_price_element(position),
                        'button': self.get_button_element(position)}
        return current_item

    def get_inventory_item_text(self, position):
        """
        function to get all text values of an item
        :param position: item that will be focused
        :return: all text values
        """
        current_item = self.get_all_item_elements(position)
        current_item.pop('img')
        for key in current_item:
            current_item[key] = current_item[key].text
        return current_item

    def get_img_element(self, position):
        """
        function to get img webElement of an item
        :param position: item that will be focused
        :return: img webElement
        """
        items = self.find_all(self.inventory_all_items)
        return self.find_within_element(self.item_img, items[position])

    def get_title_element(self, position):
        """
        function to get title webElement of an item
        :param position: item that will be focused
        :return: title webElement
        """
        items = self.find_all(self.inventory_all_items)
        return self.find_within_element(self.item_title, items[position])

    def get_description_element(self, position):
        """
        function to get description webElement of an item
        :param position: item that will be focused
        :return: description webElement
        """
        items = self.find_all(self.inventory_all_items)
        return self.find_within_element(self.item_description, items[position])

    def get_price_element(self, position):
        """
        function to get price webElement of an item
        :param position: item that will be focused
        :return: price webElement
        """
        items = self.find_all(self.inventory_all_items)
        return self.find_within_element(self.item_price, items[position])

    def get_button_element(self, position):
        """
        function to get button webElement of an item
        :param position: item that will be focused
        :return: button webElement
        """
        items = self.find_all(self.inventory_all_items)
        return self.find_within_element(self.item_button, items[position])

    def click_item_img(self, position):
        """
        function to click on an item img
        :param position: item that will be focused
        """
        self.click_within_element(self.get_img_element(position))

    def click_item_title(self, position):
        """
        function to click on an item title
        :param position: item that will be focused
        """
        self.click_within_element(self.get_title_element(position))

    def click_item_button(self, position):
        """
        function to click on an item button
        :param position: item that will be focused.
        """
        self.click_within_element(self.get_button_element(position))

    # SHOPPING CART

    def click_shopping_cart_button(self):
        """
        function to click on shopping cart button
        """
        self.click(self.shopping_cart_button)

    def get_shopping_cart_number(self):
        """
        function to get shopping cart value
        :return: string with cart value
        """
        return self.get_text(self.shopping_cart_badge)

    # FILTERS

    def get_all_prices(self):
        """
        function to get all prices of the inventory items
        :return: list with prices
        """
        items_list = self.find_all(self.inventory_all_items)
        for key in range(len(items_list)):
            items_list[key] = float(self.find_within_element
                                    (self.item_price, items_list[key]).text.replace('$', ''))
        return items_list

    def get_all_titles(self):
        """
        function to get all titles of the inventory items
        :return: list with titles
        """
        items_list = self.find_all(self.inventory_all_items)
        for key in range(len(items_list)):
            items_list[key] = self.find_within_element(self.item_title, items_list[key]).text
        return items_list

    @staticmethod
    def sort_by_low_to_high(prices_list):
        """
        function that sorts internally all prices by low to high
        :param prices_list: list with prices
        :return: sorted prices list
        """
        sorted_list = sorted(prices_list)
        return sorted_list

    @staticmethod
    def sort_by_high_to_low(prices_list):
        """
        function that sorts internally all prices by high to low
        :param prices_list: list with prices
        :return: sorted price list
        """
        sorted_list = sorted(prices_list, reverse=True)
        return sorted_list

    @staticmethod
    def sort_by_a_to_z(titles_list):
        """
        function that sorts internally all titles by A to Z
        :param titles_list: list with titles
        :return: sorted titles list
        """
        sorted_list = sorted(titles_list)
        return sorted_list

    @staticmethod
    def sort_by_z_to_a(titles_list):
        """
        function that sorts internally all titles by Z to A
        :param titles_list: list with titles
        :return: sorted titles list
        """
        sorted_list = sorted(titles_list, reverse=True)
        return sorted_list

    def click_filter_by_a_to_z(self):
        """
        function that clicks on filter A to Z
        """
        self.click(self.filter_dropdown)
        self.click(self.filter_option_a_to_z)

    def click_filter_by_z_to_a(self):
        """
        function that clicks on filter Z to A
        """
        self.click(self.filter_dropdown)
        self.click(self.filter_option_z_to_a)

    def click_filter_low_to_high(self):
        """
        function that clicks on filter low to high
        """
        self.click(self.filter_dropdown)
        self.click(self.filter_option_low_to_high)

    def click_filter_high_to_low(self):
        """
        function that clicks on filter high to low
        """
        self.click(self.filter_dropdown)
        self.click(self.filter_option_high_to_low)
