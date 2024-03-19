import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class Orders_page:
    def __init__(self, browser):
        self.browser = browser

    def add_new_product(self):
        add_new = Wait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="fa-solid fa-plus"]'))
        )
        self.browser.execute_script("arguments[0].click();", add_new)
        self.browser.find_element(
            By.CSS_SELECTOR, '[data-bs-target="#modal-cart"]'
        ).click()
        self.browser.find_element(By.CSS_SELECTOR, '[name="product"]').click()
        self.browser.find_element(By.XPATH, '//*[text()="Canon EOS 5D"]').click()
        time.sleep(2)
        self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-option-226"] [value="15"]'
        ).click()
        btn_save = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-product-add"]'
        )
        btn_save.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-cart"] [data-bs-dismiss="modal"]'
        )
        close_window.click()

    def delete_added_product(self):
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, '[title="Remove"]').click()

    def add_new_customer(self):
        time.sleep(2)
        open_customer = self.browser.find_element(
            By.CSS_SELECTOR,
            '[data-bs-target="#modal-customer"] [class="fa-solid fa-cog"]',
        )
        open_customer.click()
        input_firstname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-firstname"]'
        )
        input_firstname.send_keys("Klim")
        input_lastname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-lastname"]'
        )
        input_lastname.send_keys("Trotsenko")
        input_email = self.browser.find_element(By.CSS_SELECTOR, '[id="input-email"]')
        input_email.send_keys("123@123.com")
        save_btn = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-customer"] [class="fa-solid fa-floppy-disk"]'
        )
        save_btn.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-customer"] [class="btn-close"]'
        )
        close_window.click()

    def add_new_payment_address(self):
        time.sleep(2)
        open_wnd_pmt_address = self.browser.find_element(
            By.CSS_SELECTOR,
            '[data-bs-target="#modal-payment-address"] [class="fa-solid fa-cog"]',
        )
        open_wnd_pmt_address.click()
        input_firstname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-payment-firstname"]'
        )
        input_firstname.click()
        input_firstname.send_keys("Klim")
        input_lastname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-payment-lastname"]'
        )
        input_lastname.click()
        input_lastname.send_keys("Trotsenko")
        input_address1 = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-payment-address-1"]'
        )
        input_address1.click()
        input_address1.send_keys("Ad1")
        input_city = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-payment-city"]'
        )
        input_city.click()
        input_city.send_keys("1 krug")
        save_btn = self.browser.find_element(
            By.CSS_SELECTOR,
            '[id="button-payment-address"] [class="fa-solid fa-floppy-disk"]',
        )
        save_btn.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-payment-address"] [class="btn-close"]'
        )
        close_window.click()

    def add_new_shipping_address(self):
        time.sleep(2)
        open_wnd_ship_address = self.browser.find_element(
            By.CSS_SELECTOR,
            '[data-bs-target="#modal-shipping-address"] [class="fa-solid fa-cog"]',
        )
        open_wnd_ship_address.click()
        input_firstname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-shipping-firstname"]'
        )
        input_firstname.click()
        input_firstname.send_keys("Klim")
        input_lastname = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-shipping-lastname"]'
        )
        input_lastname.click()
        input_lastname.send_keys("Trotsenko")
        input_address1 = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-shipping-address-1"]'
        )
        input_address1.click()
        input_address1.send_keys("Ad1")
        input_city = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-shipping-city"]'
        )
        input_city.click()
        input_city.send_keys("1 krug")
        save_btn = self.browser.find_element(
            By.CSS_SELECTOR,
            '[id="button-shipping-address"] [class="fa-solid fa-floppy-disk"]',
        )
        save_btn.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-shipping-address"] [class="btn-close"]'
        )
        close_window.click()

    def add_new_shipping_method(self):
        time.sleep(2)
        open_wnd_ship_metod = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-shipping-methods"] [class="fa-solid fa-cog"]'
        )
        open_wnd_ship_metod.click()
        choose_shipping_metod = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-shipping-method-flat-flat"]'
        )
        choose_shipping_metod.click()
        press_continue_btn = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-shipping-method"]'
        )
        press_continue_btn.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-shipping"] [class="btn-close"]'
        )
        close_window.click()

    def add_new_payment_method(self):
        time.sleep(2)
        open_payment_metod = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-payment-methods"] [class="fa-solid fa-cog"]'
        )
        open_payment_metod.click()

        choose_payment_metod = self.browser.find_element(
            By.CSS_SELECTOR, '[id="input-payment-method-cod-cod"]'
        )
        choose_payment_metod.click()
        press_continue_btn = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-payment-method"]'
        )
        press_continue_btn.click()
        close_window = self.browser.find_element(
            By.CSS_SELECTOR, '[id="modal-payment"] [class="btn-close"]'
        )
        close_window.click()

    def confirm_form(self):
        confirm_btn = self.browser.find_element(
            By.CSS_SELECTOR, '[id="button-confirm"] [class="fa-solid fa-floppy-disk"]'
        )
        self.browser.execute_script("arguments[0].click();", confirm_btn)

    def check_success_sending_form(self):
        time.sleep(1)
        Wait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '// *[text()=" Success: You have modified orders! "]')
            )
        )

    def check_no_products_on_page(self):
        no_results = self.browser.find_element(
            By.CSS_SELECTOR, '[id="order-vouchers"] [class="text-center"]'
        )
        assert no_results.text == "No results!"
