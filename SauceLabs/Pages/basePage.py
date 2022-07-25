from selenium.webdriver.common.by import By
from SauceLabs.Locators.locators import Locators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.hamburger_menu_id = Locators.hamburger_menu_id
        self.inventory_sidebar_id = Locators.inventory_sidebar_id
        self.logout_sidebar_id = Locators.logout_sidebar_id
        self.twitter_logo_xpath = Locators.twitter_logo_xpath
        self.facebook_logo_xpath = Locators.facebook_logo_xpath
        self.linkedin_logo_xpath = Locators.linkedin_logo_xpath
        self.shopping_cart_class = Locators.shopping_cart_class

    def get_url(self):
        return self.driver.current_url

    def current_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def open_menu(self):
        self.driver.find_element(By.ID, self.hamburger_menu_id).click()

    def logout(self):
        self.driver.find_element(By.ID, self.logout_sidebar_id).click()

    def twitter_logo_click(self):
        self.driver.find_element(By.XPATH, self.twitter_logo_xpath).click()

    def facebook_logo_click(self):
        self.driver.find_element(By.XPATH, self.facebook_logo_xpath).click()

    def linkedin_logo_click(self):
        self.driver.find_element(By.XPATH, self.linkedin_logo_xpath).click()

    def close_window(self):
        self.driver.close()

