import random

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_random_number():
        number = random.randint(0, 5)
        return number

    def visit(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def find_all(self, locator):
        return self.driver.find_elements(locator['by'], locator['value'])

    @staticmethod
    def find_within_element(locator, element):
        return element.find_element(locator['by'], locator['value'])

    def get_text_within_element(self, locator, element):
        return self.find_within_element(locator, element).text

    @staticmethod
    def get_text_element(element):
        return element.text

    def click(self, locator):
        self.find(locator).click()

    @staticmethod
    def click_within_element(element):
        element.click()

    def type(self, locator, input_text):
        self.find(locator).clear()
        self.find(locator).send_keys(input_text)

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text
