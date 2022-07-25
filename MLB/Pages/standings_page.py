from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MLB.Locators.locators import Locators
from MLB.Pages.base_page import BasePage


class StandingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.AL_east_table_xpath = Locators.AL_east_table_xpath
        self.AL_central_table_xpath = Locators.AL_central_table_xpath
        self.AL_west_table_xpath = Locators.AL_west_table_xpath
        self.columns_xpath = Locators.columns_xpath

    def print_AL_east_table(self):
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.AL_east_table_xpath)))
        rows = self.driver.find_elements(By.XPATH, self.AL_east_table_xpath)
        for row in rows:
            for column in range(16):
                print(row.find_elements(By.XPATH, self.columns_xpath)[column].get_attribute('innerText'))
        print('--------')

    def get_AL_east_table(self):
        return self.driver.find_elements(By.XPATH, self.AL_east_table_xpath)

    def validate_first_place(self, table):
        for row in range(len(table)):
            print(table[row].text)