import datetime
import logging
import allure
import pytest


from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.edge.options import Options as EdgeOptions


o = ChromeOptions()
o.add_experimental_option("detach", True)


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.1.103")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")
    mobile = request.config.getoption("--mobile")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("opencart_tests.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    start_time = datetime.datetime.now()
    logger.info("===> Test %s started at %s" % (request.node.name, start_time))

    executor_url = f"http://{executor}:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")


    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        if headless:
            options.add_argument("--headless")
    elif browser == "yandex":
        options = ChromiumOptions()
        options.set_capability("browserVersion", "100")
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        if headless:
            options.add_argument("--headless")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "screenResolution": "1280x2000",
            "enableVideo": video,
            "enableLog": logs,
            "timeZone": "Europe/Moscow",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
        },
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(command_executor=executor_url, options=options)

    driver.log_level = log_level
    logger = logging.getLogger(request.node.name)
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    if not mobile:
        driver.maximize_window()

    driver.base_url = base_url

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )

    end_time = datetime.datetime.now()
    logger.info(
        "===> Test %s finished at %s \n _________ \n" % (request.node.name, end_time)
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver
