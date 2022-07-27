from selenium.webdriver.common.by import By

from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage

import time


class InventoryPage(BasePage):
    # header objects
    hamburger_menu = {'by': By.ID, 'value': 'react-burger-menu-btn'}
    all_items_button = {'by': By.ID, 'value': 'inventory_sidebar_link'}
    about_button = {'by': By.ID, 'value': 'about_sidebar_link'}
    logout_button = {'by': By.ID, 'value': 'logout_sidebar_link'}
    reset_app_state_button = {'by': By.ID, 'value': 'reset_sidebar_link'}
    hamburger_cross_button = {'by': By.ID, 'value': 'react-burger-cross-btn'}
    shopping_cart_badge = {'by': By.CSS_SELECTOR, 'value': '.shopping_cart_badge'}
    # filter objects
    filter_dropdown = {'by': By.CSS_SELECTOR, 'value': '.product_sort_container'}
    filter_option_a_to_z = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(1)'}
    filter_option_z_to_a = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(2)'}
    filter_option_low_to_high = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(3)'}
    filter_option_high_to_low = {'by': By.CSS_SELECTOR, 'value': 'option:nth-child(4)'}
    # inventory items object
    inventory_all_items = {'by': By.CSS_SELECTOR, 'value': '.inventory_item'}
    inventory_item_img = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_img'}
    inventory_item_title = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_name'}
    inventory_item_description = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_desc'}
    inventory_item_price = {'by': By.CSS_SELECTOR, 'value': '.inventory_item_price'}
    inventory_item_button = {'by': By.CSS_SELECTOR, 'value': '.btn'}

    def __init__(self, driver):
        super().__init__(driver)

    def validate_login(self):
        return self.is_displayed(self.hamburger_menu)

    def logout(self):
        self.click(self.hamburger_menu)
        self.click(self.logout_button)

    def validate_inventory_url(self):
        return self.get_url() == constants.INVENTORY_URL

    def navigate_to_about(self):
        self.click(self.hamburger_menu)
        self.click(self.about_button)
        return self.driver.current_url == constants.ABOUT_SAUCE_URL

    def filter_by_a_to_z(self):
        self.click(self.filter_dropdown)
        self.click(self.filter_option_a_to_z)

    def filter_by_z_to_a(self):
        self.click(self.filter_dropdown)
        self.click(self.filter_option_z_to_a)

    def filter_low_to_high(self):
        self.click(self.filter_dropdown)
        self.click(self.filter_option_low_to_high)

    def filter_high_to_low(self):
        self.click(self.filter_dropdown)
        self.click(self.filter_option_high_to_low)

    def get_specific_inventory_item_elements(self, position):
        items = self.find_all(self.inventory_all_items)
        current_item = {'img': self.find_within_element(self.inventory_item_img, items[position]),
                        'title': self.find_within_element(self.inventory_item_title, items[position]),
                        'description': self.find_within_element(self.inventory_item_description, items[position]),
                        'price': self.find_within_element(self.inventory_item_price, items[position]),
                        'button': self.find_within_element(self.inventory_item_button, items[position])}
        return current_item

    def get_specific_inventory_item_text(self, position):
        current_item = self.get_specific_inventory_item_elements(position)
        for key in current_item:
            current_item[key] = current_item[key].text
        return current_item

    def click_on_inventory_item_img(self, position):
        current_item = self.get_specific_inventory_item_elements(position)
        self.click_within_element(current_item['img'])

    def click_on_inventory_item_title(self, position):
        current_item = self.get_specific_inventory_item_elements(position)
        self.click_within_element(current_item['title'])

    def click_on_inventory_item_button(self, position):
        current_item = self.get_specific_inventory_item_elements(position)
        self.click_within_element(current_item['button'])

    def get_shopping_cart_number(self):
        return self.get_text(self.shopping_cart_badge)




