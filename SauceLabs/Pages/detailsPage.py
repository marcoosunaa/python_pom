from selenium.webdriver.common.by import By
from SauceLabs.Locators.locators import Locators
from SauceLabs.Pages.basePage import BasePage
import time


class DetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.details_back_to_products_id = Locators.details_back_to_products_id
        self.details_name_class = Locators.details_name_class
        self.details_description_class = Locators.details_description_class
        self.details_price_class = Locators.details_price_class
        self.details_img_class = Locators.details_img_class
        self.details_button_class = Locators.details_button_class

    def compare_values(self, item_values):
        if item_values['name'] == self.driver.find_element(By.XPATH, self.details_name_class).text and \
                item_values['description'] == self.driver.find_element(By.XPATH, self.details_description_class).text\
                and item_values['price'] == self.driver.find_element(By.XPATH, self.details_price_class).text:
            return True
        else:
            return False
