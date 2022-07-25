from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from SauceLabs.Pages.basePage import BasePage
from SauceLabs.Tests.login import LoginTest


class HeaderFooterTest(unittest.TestCase):

    # Class mean Before all tests
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service("C:/Users/marco/PycharmProjects/python_pom/Drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_twitter_logo(self):
        driver = self.driver
        LoginTest.test_login_valid(self)
        landing = BasePage(driver)

        landing.twitter_logo_click()
        landing.current_tab()

        self.assertEqual('https://twitter.com/saucelabs', landing.get_url(), 'Url is incorrect!')
        landing.close_window()
        landing.current_tab()

    def test_facebook_logo(self):
        driver = self.driver
        LoginTest.test_login_valid(self)
        landing = BasePage(driver)

        landing.facebook_logo_click()
        landing.current_tab()

        self.assertEqual('https://www.facebook.com/saucelabs', landing.get_url(), 'Url is incorrect!')
        landing.close_window()
        landing.current_tab()

    def test_linkedin_logo(self):
        driver = self.driver
        LoginTest.test_login_valid(self)
        landing = BasePage(driver)

        landing.linkedin_logo_click()
        landing.current_tab()

        self.assertEqual('https://www.linkedin.com/company/sauce-labs/?original_referer=', landing.get_url(), 'Url is incorrect!')
        landing.close_window()
        landing.current_tab()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
