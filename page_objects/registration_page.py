import allure

from selenium.webdriver.common.by import By


class Registration_page:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Добавление имени")
    def add_username(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-firstname"]').send_keys(
            "Klim"
        )
        self.logger.info("Добавляем имя")

    @allure.step("Добавление фамилии")
    def add_lastname(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-lastname"]').send_keys(
            "Trotsenko"
        )
        self.logger.info("Добавляем фамилию")

    @allure.step("Добавление электронной почты")
    def add_email(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-email"]').send_keys(
            "123@123.com"
        )
        self.logger.info("Добавляем электронную почту")

    @allure.step("Принятие политики конфиденциальности")
    def accept_privacy_policy(self):
        self.browser.find_element(By.CSS_SELECTOR, '[name="agree"]').click()
        self.logger.info("Нажимаем что прочитали соглашение")

    @allure.step("Подтверждение формы")
    def submit_form(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
        self.logger.info("Подтверждаем форму")

    @allure.step("Проверка успешного заполнения формы")
    def check_success_filling_form(self):
        success = self.browser.find_element(By.CSS_SELECTOR, '[id="common-success"] h1')
        assert success.text == "Your Account Has Been Created!"
        self.logger.info("Првоеряем что аккаунт создан")
