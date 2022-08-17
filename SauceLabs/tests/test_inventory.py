"""
import all needed modules
"""
import pytest
from SauceLabs.env import constants
from SauceLabs.pages.details_page import DetailsPage
from SauceLabs.pages.inventory_page import InventoryPage
from SauceLabs.pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestInventoryPage:
    """
    class for test inventory page
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
        assert self.inventory_page.validate_url()

    @pytest.mark.inventory
    def test_click_on_title(self, set_up):
        """
        test click on title on any item in inventory page
        :param set_up: initialize pre steps
        """
        position = self.inventory_page.get_random_number()
        inventory_item = self.inventory_page.get_inventory_item_text(position)
        self.inventory_page.click_item_title(position)
        details_item = self.details_page.get_details_text()
        assert inventory_item == details_item, constants.ERROR_INVENTORY_VS_DETAILS

    @pytest.mark.inventory
    def test_click_on_img(self, set_up):
        """
        test click on img on any item in inventory page
        :param set_up: initialize pre steps
        """
        position = self.inventory_page.get_random_number()
        inventory_item = self.inventory_page.get_inventory_item_text(position)
        self.inventory_page.click_item_img(position)
        details_item = self.details_page.get_details_text()
        assert inventory_item == details_item, constants.ERROR_INVENTORY_VS_DETAILS

    @pytest.mark.inventory
    @pytest.mark.cart
    def test_add_to_cart(self, set_up):
        """
        test click on add to cart button on any item in inventory page
        :param set_up: initialize pre steps
        """
        position = self.inventory_page.get_random_number()
        self.inventory_page.click_item_button(position)
        self.inventory_page.get_shopping_cart_number()
        assert self.inventory_page.get_shopping_cart_number() == '1'

    @pytest.mark.inventory
    @pytest.mark.filters
    def test_filter_price_low_to_high(self, set_up):
        """
        test filter low to high is applied correctly in inventory page
        :param set_up: initialize pre steps
        """
        original_list = self.inventory_page.\
            sort_by_low_to_high(self.inventory_page.get_all_prices())
        self.inventory_page.click_filter_low_to_high()
        sorted_list = self.inventory_page.get_all_prices()
        assert original_list == sorted_list, constants.ERROR_SORTED_LIST

    @pytest.mark.inventory
    @pytest.mark.filters
    def test_filter_price_high_to_low(self, set_up):
        """
        test filter high to low is applied correctly in inventory page
        :param set_up: initialize pre steps
        """
        original_list = self.inventory_page.\
            sort_by_high_to_low(self.inventory_page.get_all_prices())
        self.inventory_page.click_filter_high_to_low()
        sorted_list = self.inventory_page.get_all_prices()
        assert original_list == sorted_list, constants.ERROR_SORTED_LIST

    @pytest.mark.inventory
    @pytest.mark.filters
    def test_filter_a_to_z(self, set_up):
        """
        test filter low to A is Z correctly in inventory page
        :param set_up: initialize pre steps
        """
        original_list = self.inventory_page.sort_by_a_to_z(self.inventory_page.get_all_titles())
        self.inventory_page.click_filter_by_a_to_z()
        sorted_list = self.inventory_page.get_all_titles()
        assert original_list == sorted_list, constants.ERROR_SORTED_LIST

    @pytest.mark.inventory
    @pytest.mark.filters
    def test_filter_z_to_a(self, set_up):
        """
        test filter Z to A is applied correctly in inventory page
        :param set_up: initialize pre steps
        """
        original_list = self.inventory_page.sort_by_z_to_a(self.inventory_page.get_all_titles())
        self.inventory_page.click_filter_by_z_to_a()
        sorted_list = self.inventory_page.get_all_titles()
        assert original_list == sorted_list, constants.ERROR_SORTED_LIST
