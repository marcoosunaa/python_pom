import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from MLB.Pages.base_page import BasePage
from MLB.Pages.standings_page import StandingsPage


class StandingsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service("C:/Users/marco/PycharmProjects/python_pom/Drivers/chromedriver102.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(1)
        cls.driver.maximize_window()

    def test_navigate_to_url(self):
        driver = self.driver
        driver.get("https://www.mlb.com/standings")

        # standings_page = BasePage(driver)
        # standings_page.click_standings_button()

        standings_page = StandingsPage(driver)
        standings_page.validate_first_place(standings_page.get_AL_east_table())


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
