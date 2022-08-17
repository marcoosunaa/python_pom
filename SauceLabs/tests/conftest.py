import pytest
from SauceLabs.env import constants
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
os.environ['GH_TOKEN'] = constants.GH_TOKEN


@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(constants.SAUCE_DEMO_URL)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope='class', autouse='True')
def browser(request):
    return request.config.getoption('--browser')
