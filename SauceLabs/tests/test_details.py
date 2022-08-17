"""
import all needed modules
"""
import pytest
from SauceLabs.env import constants
from SauceLabs.pages.details_page import DetailsPage
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestDetailsPage:
    """
    class for test details page
    """
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """
        This function is auto used to load all pages needed in these tests
        """
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.details_page = DetailsPage(self.driver)

    @pytest.fixture()
    def set_up(self):
        """
        function is used after every test case
        """
        self.login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)

    @pytest.mark.navigation
    def test_url(self, set_up):
        """
        test navigation to inventory page
        :param set_up: initialize pre steps
        """
        position = self.inventory_page.get_random_number()
        self.inventory_page.click_item_title(position)
        assert self.details_page.validate_details_url()
