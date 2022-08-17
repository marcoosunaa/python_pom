"""
import all needed modules
"""
import pytest
from SauceLabs.env import constants
from SauceLabs.pages.cart_page import CartPage
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestCartPage:
    """
    class for test cart page
    """
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """
        This function is auto used to load all pages needed in these tests
        """
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)

    @pytest.fixture()
    def set_up(self):
        """
        function is used after every test case
        """
        self.login_page.login(constants.VALID_USER, constants.VALID_PASSWORD)

    def test_url(self, set_up):
        """
        test navigation to inventory page
        :param set_up: initialize pre steps
        """
        self.inventory_page.click_shopping_cart_button()
        assert self.cart_page.validate_url(), constants.ERROR_WRONG_URL

    def test_cart_item(self, set_up):
        """
        test add item to cart
        :param set_up: initialize pre steps
        """
        position = self.inventory_page.get_random_number()
        self.inventory_page.click_item_button(position)
        inventory_item = self.inventory_page.get_inventory_item_text(position)
        self.inventory_page.click_shopping_cart_button()
        assert self.cart_page.get_cart_item_text() == \
               inventory_item, constants.ERROR_INVENTORY_VS_CART
