from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="choose the browser that you want to use"
    )
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="https://www.opencart.com")


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
        service = ChromeService(
            executable_path="/Users/klim/Downloads/chromedriver-mac-arm64/chromedriver"
        )
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    driver.base_url = base_url
    yield driver

    if driver is not None:
        driver.quit()
