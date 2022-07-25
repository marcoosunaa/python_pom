from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from SauceLabs.Pages.loginPage import LoginPage
from SauceLabs.Pages.basePage import BasePage
import time


class LoginTest(unittest.TestCase):

    # Class mean Before all tests
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service("C:/Users/marco/PycharmProjects/python_pom/Drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        loginPage = LoginPage(driver)
        loginPage.login('standard_user', 'secret_sauce')

    def test_invalid_login_valid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # locked out user
        loginPage = LoginPage(driver)
        loginPage.login('locked_out_user', 'secret_sauce')

        self.assertEqual("Epic sadface: Sorry, this user has been locked out.", loginPage.get_error_text(),
                         "Text do not match!")
        # wrong username
        loginPage.login('standard_user', 'secret_sauce123')

        self.assertEqual("Epic sadface: Username and password do not match any user in this service",
                         loginPage.get_error_text(), "Text do not match!")
        # wrong password
        loginPage.login('standard_user123', 'secret_sauce')

        self.assertEqual("Epic sadface: Username and password do not match any user in this service",
                         loginPage.get_error_text(), "Text do not match!")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
