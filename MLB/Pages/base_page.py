import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from MLB.Locators.locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_logo_xpath = Locators.menu_logo_xpath
        self.menu_news_xpath = Locators.menu_news_xpath
        self.menu_watch_xpath = Locators.menu_watch_xpath
        self.menu_scores_xpath = Locators.menu_scores_xpath
        self.menu_schedule_xpath = Locators.menu_schedule_xpath
        self.menu_stats_xpath = Locators.menu_stats_xpath
        self.menu_standings_xpath = Locators.menu_standings_xpath
        self.menu_youth_xpath = Locators.menu_youth_xpath
        self.menu_players_xpath = Locators.menu_players_xpath

    def click_logo_button(self):
        self.driver.find_element(By.XPATH, self.menu_logo_xpath).click()

    def click_news_button(self):
        self.driver.find_element(By.XPATH, self.menu_news_xpath).click()

    def click_watch_button(self):
        self.driver.find_element(By.XPATH, self.menu_watch_xpath).click()

    def click_scores_button(self):
        self.driver.find_element(By.XPATH, self.menu_scores_xpath).click()

    def click_schedule_button(self):
        self.driver.find_element(By.XPATH, self.menu_schedule_xpath).click()

    def click_stats_button(self):
        self.driver.find_element(By.XPATH, self.menu_stats_xpath).click()

    def click_standings_button(self):
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.menu_standings_xpath)))
        self.driver.find_element(By.XPATH, self.menu_standings_xpath).click()

    def click_youth_button(self):
        self.driver.find_element(By.XPATH, self.menu_youth_xpath).click()

    def click_players_button(self):
        self.driver.find_element(By.XPATH, self.menu_players_xpath).click()

    def mouse_hover_stats_button(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.menu_stats_xpath)).perform()
