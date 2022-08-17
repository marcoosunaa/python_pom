"""
import all needed modules
"""
from selenium.webdriver.common.by import By
from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Dictionaries with locators of each webElement
    """
    username_input = {'by': By.ID, 'value': 'user-name'}
    password_input = {'by': By.ID, 'value': 'password'}
    submit_button = {'by': By.ID, 'value': 'login-button'}
    label_error = {'by': By.CSS_SELECTOR, 'value': 'h3'}
    cross_error_button = {'by': By.CSS_SELECTOR, 'value': 'svg:nth-child(1)'}

    def login(self, username, password):
        """
        function to log in to SauceLabs
        :param username: username to enter
        :param password: password to enter
        """
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.submit_button)

    def validate_incorrect_password(self, error_text):
        """
        function to validate incorrect password
        :param error_text: error text displayed in front-end
        :return: if message matches label
        """
        return self.get_text(self.label_error) == error_text

    def validate_logout(self):
        """
        function to validate if submit button is displayed
        :return: if submit button is visible
        """
        return self.is_displayed(self.submit_button)

    def validate_login_url(self):
        """
        function to validate current url
        :return: if current url matches constant value
        """
        return self.get_url() == constants.SAUCE_DEMO_URL
