import datetime
import logging

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
    parser.addoption("--base_url", default="http://localhost")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    driver = None
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("example.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "=====> Test %s started %s" % (request.node.name, datetime.datetime.now())
    )

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

    driver.log_level = logging.INFO
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info(
        "=====> Browser %s opened at %s" % (request.node.name, datetime.datetime.now())
    )

    driver.maximize_window()
    driver.base_url = base_url

    def fin():

        driver.quit()
        logger.info(
            "=====> Test %s finished at %s"
            % (request.node.name, datetime.datetime.now())
        )

    request.addfinalizer(fin)
    return driver
