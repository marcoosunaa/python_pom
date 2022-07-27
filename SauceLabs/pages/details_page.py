from selenium.webdriver.common.by import By

from SauceLabs.pages.base_page import BasePage


class DetailsPage(BasePage):
    details_back_to_products = {'by': By.CSS_SELECTOR, 'value': '#back-to-products'}
    details_item_img = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_img'}
    details_item_title = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_name'}
    details_item_description = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_desc'}
    details_item_price = {'by': By.CSS_SELECTOR, 'value': '.inventory_details_price'}
    details_item_button = {'by': By.CSS_SELECTOR, 'value': '#add-to-cart-sauce-labs-fleece-jacket'}

    def __init__(self, driver):
        super().__init__(driver)

    def get_details_text(self):
        current_item = {
            'img': self.get_text(self.details_item_img),
            'title': self.get_text(self.details_item_title),
            'description': self.get_text(self.details_item_description),
            'price': self.get_text(self.details_item_price),
            'button': self.get_text(self.details_item_button)
        }
        return current_item
