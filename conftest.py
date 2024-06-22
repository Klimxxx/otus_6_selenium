import pytest
import os
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

# options.add_argument('==window_size=1920, 1080')
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="choose the browser that you want to use"
    )
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", action="store", default=f"http://localhost/", help="Base URL for testing")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Driver not supported")

    driver.maximize_window()

    driver.base_url = base_url

    request.addfinalizer(driver.quit)


    return driver
