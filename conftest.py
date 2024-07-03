import pytest
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Добавлено: функция для добавления опций командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default="host.docker.internal")
    parser.addoption("--bv", action="store", default="125.0")
    parser.addoption("--vnc", action="store_true")  # Изменено: флаг без аргумента
    parser.addoption("--video", action="store_true")  # Изменено: флаг без аргумента
    parser.addoption("--logs", action="store_true")
    parser.addoption("--base_url", action="store", default="http://host.docker.internal:8082")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--mobile", action="store_true")

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
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    start_time = datetime.datetime.now()
    logger.info("===> Test %s started at %s" % (request.node.name, start_time))

    executor_url = f"http://{executor}:4444/wd/hub"

    options = None
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video
        }
    }

    if options:
        for k, v in caps.items():
            options.set_capability(k, v)

    try:
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )
        driver.base_url = base_url
    except Exception as e:
        logger.error(f"Failed to start browser {browser_name}: {e}")
        pytest.fail(f"Failed to start browser {browser_name}: {e}")

    yield driver
    driver.quit()
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "report", report)

# Добавлено: логирование результатов тестов
@pytest.fixture(autouse=True)
def log_test_result(request):
    yield
    logger = logging.getLogger(request.node.name)
    report = request.node.report
    if report.when == 'call' and report.failed:
        logger.error("Test %s failed: %s" % (request.node.name, report.longrepr))
    elif report.when == 'call' and report.passed:
        logger.info("Test %s passed" % request.node.name)
