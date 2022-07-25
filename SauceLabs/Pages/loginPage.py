from selenium.webdriver.common.by import By
from SauceLabs.Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_name_textbox_id = Locators.user_name_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.error_message_xpath = Locators.error_message_xpath

    def login(self, username, password):
        self.driver.find_element(By.ID, self.user_name_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).clear()

        self.driver.find_element(By.ID, self.user_name_textbox_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, self.login_button_id).click()

    def error_message_isPresent(self):
        self.driver.find_element(By.XPATH, self.error_message_xpath).is_displayed()

    def get_error_text(self):
        return self.driver.find_element(By.XPATH, self.error_message_xpath).get_attribute('innerText')
