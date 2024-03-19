from selenium.webdriver.common.by import By


class Registration_page:
    def __init__(self, browser):
        self.browser = browser

    def add_username(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-firstname"]').send_keys(
            "Klim"
        )

    def add_lastname(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-lastname"]').send_keys(
            "Trotsenko"
        )

    def add_email(self):
        self.browser.find_element(By.CSS_SELECTOR, '[id="input-email"]').send_keys(
            "123@123.com"
        )

    def accept_privacy_policy(self):
        self.browser.find_element(By.CSS_SELECTOR, '[name="agree"]').click()

    def submit_form(self):
        self.browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

    def check_success_filling_form(self):
        success = self.browser.find_element(By.CSS_SELECTOR, '[id="common-success"] h1')
        assert success.text == "Your Account Has Been Created!"
