from selenium.webdriver.common.by import By

from SauceLabs.env import constants
from SauceLabs.pages.base_page import BasePage

import time


class LoginPage(BasePage):
    username_input = {'by': By.ID, 'value': 'user-name'}
    password_input = {'by': By.ID, 'value': 'password'}
    submit_button = {'by': By.ID, 'value': 'login-button'}
    label_error = {'by': By.CSS_SELECTOR, 'value': 'h3'}
    cross_error_button = {'by': By.CSS_SELECTOR, 'value': 'svg:nth-child(1)'}

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.click(self.submit_button)

    def validate_incorrect_password(self, error_text):
        return self.get_text(self.label_error) == error_text

    def validate_logout(self):
        return self.is_displayed(self.submit_button)

    def validate_login_url(self):
        return self.get_url() == constants.SAUCE_DEMO_URL
