import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class Main_page:
    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step("Клик по меню заказов")
    def menu_orders_click(self):
        self.browser.find_element(
            By.CSS_SELECTOR, '[class="fas fa-shopping-cart"]'
        ).click()
        choose_orders = Wait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="collapse-4"] a'))
        )
        choose_orders.click()

    @allure.step("Открытие выпадающего списка валюты")
    def open_currency_dropbox(self):

        self.browser.find_element(
            By.CSS_SELECTOR, '[id="form-currency"] [data-bs-toggle="dropdown"]'
        ).click()

    @allure.step("Выбор валюты евро")
    def choose_euro_currency(self):
        self.browser.find_element(By.XPATH, '// *[text()="€ Euro"]').click()

    @allure.step("Выбор валюты фунт стерлингов")
    def choose_pound_currency(self):
        self.browser.find_element(By.XPATH, '// *[text()="£ Pound Sterling"]').click()

    @allure.step("Выбор валюты доллар США")
    def choose_dollar_currency(self):
        self.browser.find_element(By.XPATH, '// *[text()="$ US Dollar"]').click()

    @allure.step("Проверка валюты в продуктах")
    def check_currency_in_products(self, currency):
        goods_prices = Wait(self.browser, timeout=5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        assert currency in goods_prices[0].text

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self):

        self.browser.execute_script("window.scrollBy(0, 1000);")

        btn_add_to_cart = Wait(self.browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[title="Add to Cart"]')
            )
        )
        self.browser.execute_script(
            "arguments[0].scrollIntoView();", btn_add_to_cart[0]
        )
        self.browser.execute_script("arguments[0].click();", btn_add_to_cart[0])
        self.browser.execute_script("window.scrollBy(0, -1000);")

    @allure.step("Открытие корзины")
    def open_cart(self):
        btn = Wait(self.browser, 60).until(
            EC.presence_of_element_located((By.XPATH, '// *[text()="Shopping Cart"]'))
        )
        self.browser.execute_script("arguments[0].click();", btn)

    @allure.step("Проверка цены в разделе All Desktops")
    def check_price_in_rubric_all_desktop(self):
        self.browser.find_element(
            By.CSS_SELECTOR,
            'a[href="http://localhost/en-gb/catalog/desktops"][class="nav-link dropdown-toggle"]',
        ).click()
        self.browser.find_element(By.XPATH, '// *[text()="Show All Desktops"]').click()
        self.browser.execute_script("window.scrollBy(0, 500);")
        goods_prices = Wait(self.browser, timeout=5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
        )
        assert "€" in goods_prices[0].text
