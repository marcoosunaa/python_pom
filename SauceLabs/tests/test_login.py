"""
import all needed modules
"""
import pytest
from SauceLabs.env import constants
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestLoginPage:
    """
    class for test login page
    """
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """
        This function is auto used to load all pages needed in these tests
        """
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

    @pytest.mark.login
    def test_valid_login(self):
        """
        test validate valid login
        """
        self.login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)
        assert self.inventory_page.validate_login()

    @pytest.mark.login
    def test_logout(self):
        """
        test validate valid login
        """
        self.login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)
        self.inventory_page.logout()
        assert self.login_page.validate_logout()

    @pytest.mark.login
    def test_invalid_password(self):
        """
        test invalid password
        """
        self.login_page.login(constants.VALID_USER, constants.INVALID_PASSWORD)
        assert self.login_page.validate_incorrect_password(constants.ERROR_INVALID_PASSWORD)

    @pytest.mark.login
    def test_no_username(self):
        """
        test null username
        """
        self.login_page.login(constants.EMPTY_VALUE, constants.VALID_PASSWORD)
        assert self.login_page.validate_incorrect_password(constants.ERROR_NO_USERNAME)

    @pytest.mark.login
    def test_no_password(self):
        """
        test null password
        """
        self.login_page.login(constants.VALID_USER, constants.EMPTY_VALUE)
        assert self.login_page.validate_incorrect_password(constants.ERROR_NO_PASSWORD)

    @pytest.mark.login
    def test_locked_login(self):
        """
        test valid login with locked down user
        """
        self.login_page.login(constants.LOCKED_USER, constants.VALID_PASSWORD)
        assert self.login_page.validate_incorrect_password(constants.ERROR_LOCKED_USER)

    @pytest.mark.login
    @pytest.mark.navigation
    def test_url(self):
        """
        test navigation to inventory page
        """
        assert self.login_page.validate_login_url()
