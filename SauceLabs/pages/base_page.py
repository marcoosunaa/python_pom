"""
import all needed modules
"""
import random


class BasePage:
    """
    class is initialized
    :param driver: driver is initialized
    """
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_random_number():
        """
        function that generates a random number from 0 through 5
        :return:
        return a random number from 0 through 5
        """
        number = random.randint(0, 5)
        return number

    def visit(self, url):
        """
        Visit the desired url
        :param url: receives the url to visit
        """
        self.driver.get(url)

    def get_url(self):
        """
        gets current url
        :return: current url
        """
        return self.driver.current_url

    def find(self, locator):
        """
        find a webElement
        :param locator: locator to be found
        :return: the desired WebElement
        """
        return self.driver.find_element(locator['by'], locator['value'])

    def find_all(self, locator):
        """
        find a list of webElements
        :param locator: locator to be found
        :return: the desired WebElement list
        """
        return self.driver.find_elements(locator['by'], locator['value'])

    @staticmethod
    def find_within_element(locator, element):
        """
        find a webElement within another element
        :param element: element to find within
        :param locator: locator to be found
        :return: the desired WebElement
        """
        return element.find_element(locator['by'], locator['value'])

    def get_text_within_element(self, locator, element):
        """
        get text of a webElement within another element
        :param element: element to find within
        :param locator: locator to be found
        :return: the desired WebElement
        """
        return self.find_within_element(locator, element).text

    @staticmethod
    def get_text_element(element):
        """
        get text of a webElement
        :param element: element desired to get text
        :return: text of webElement
        """
        return element.text

    def click(self, locator):
        """
        clicks an element
        :param locator: locator to be found
        """
        self.find(locator).click()

    @staticmethod
    def click_within_element(element):
        """
        clicks an element within another element
        :param element: element to click
        """
        element.click()

    def type(self, locator, input_text):
        """
        enter text
        :param input_text: text to be typed
        :param locator: locator to be found
        """
        self.find(locator).clear()
        self.find(locator).send_keys(input_text)

    def is_displayed(self, locator):
        """
        validate if element is displayed.
        :param locator: locator to be found
        """
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        """
        Get text of an element
        :param locator: locator to be found
        """
        return self.find(locator).text
