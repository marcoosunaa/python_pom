from selenium.webdriver.common.by import By
from SauceLabs.Locators.locators import Locators
from SauceLabs.Pages.basePage import BasePage
import time


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_items = Locators.inventory_items
        self.inventory_item_name_class = Locators.inventory_item_name_class
        self.inventory_item_desc_class = Locators.inventory_item_desc_class
        self.inventory_item_price_class = Locators.inventory_item_price_class
        self.inventory_item_img_class = Locators.inventory_item_img_class
        self.inventory_item_btn_class = Locators.inventory_item_btn_class

    def get_all_inventory_items_text(self):
        items_list = []
        item_list_raw = self.driver.find_elements(By.XPATH, self.inventory_items)
        for item in item_list_raw:
            items_list.append({'name': item.find_element(By.XPATH, self.inventory_item_name_class).text,
                               'description': item.find_element(By.XPATH, self.inventory_item_desc_class).text,
                               'price': item.find_element(By.XPATH, self.inventory_item_price_class).text,
                               'image': item.find_element(By.XPATH, self.inventory_item_img_class).get_attribute(
                                   'currentSrc'),
                               'button': item.find_element(By.XPATH, self.inventory_item_btn_class).text})
        return items_list

    def get_single_item_elements(self, item_name):
        item_values = {}
        items_list_raw = self.driver.find_elements(By.XPATH, self.inventory_items)
        for item in items_list_raw:
            if item_name == item.find_element(By.XPATH, self.inventory_item_name_class).text:
                item_values['name'] = item.find_element(By.XPATH, self.inventory_item_name_class)
                item_values['description'] = item.find_element(By.XPATH, self.inventory_item_desc_class)
                item_values['price'] = item.find_element(By.XPATH, self.inventory_item_price_class)
                item_values['image'] = item.find_element(By.XPATH, self.inventory_item_img_class)
                item_values['button'] = item.find_element(By.XPATH, self.inventory_item_btn_class)
                return item_values
        return False

    def get_single_item_text(self, item_name):
        item_values = {}
        item = self.get_single_item_elements(item_name)
        item_values['name'] = item['name'].text
        item_values['description'] = item['description'].text
        item_values['price'] = item['price'].text
        item_values['image'] = item['image'].text
        item_values['button'] = item['button'].text
        return item_values

    def click_on_item_image(self, item_name):
        item_values = self.get_single_item_elements(item_name)
        item_values['image'].click()

    def add_to_cart(self, item_name):
        items_list_raw = self.driver.find_elements(By.XPATH, self.inventory_items)
        for item in items_list_raw:
            if item_name == item.find_element(By.XPATH, self.inventory_item_name_class).text:
                item.find_element(By.XPATH, self.inventory_item_btn_class).click()

    def get_shopping_cart_number(self):
        return self.driver.find_element(By.XPATH, self.shopping_cart_class).text
