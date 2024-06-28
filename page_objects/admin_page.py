import logging
import sys
import allure

from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.ERROR, stream=sys.stdout)


class Admin_page:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Вход в систему")
    def login(self, username, password):
        self.logger.info("Попытка входа в систему с логином: %s", username)
        input_username = self.browser.find_element(By.CSS_SELECTOR, '[name="username"]')
        input_username.send_keys(username)
        input_password = self.browser.find_element(By.CSS_SELECTOR, '[name="password"]')
        input_password.send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        self.logger.info("Успешно вошли в систему!")

    @allure.step("Проверка успешной аутентификации")
    def check_auth_succesful(self):
        user_name = self.browser.find_element(
            By.CSS_SELECTOR, '[class="d-none d-md-inline d-lg-inline"]'
        )
        assert user_name.text == "   John Doe", "авторизация не успешна"
        self.logger.info("Проверка успешна что авторизация неуспешна")

        self.browser.find_element(
            By.CSS_SELECTOR, '[class="d-none d-md-inline"]'
        ).click()
        header_login_page = self.browser.find_element(
            By.CSS_SELECTOR, '[class="card-header"]'
        )
        assert (
            header_login_page.text == "Please enter your login details."
        ), "разлог не выполнен"
        self.logger.info("Проверка успешна что разлог не выполнен")
