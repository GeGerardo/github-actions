import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Initial setup and teardown
@pytest.fixture(scope='function')
def setup(request):
    general_driver = webdriver.Chrome(ChromeDriverManager().install())
    # general_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # general_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    # path = 'chromedriver'
    # general_driver = webdriver.Chrome(executable_path=path)
    request.cls.driver = general_driver
    general_driver.maximize_window()
    yield
    general_driver.close()
    general_driver.quit()
