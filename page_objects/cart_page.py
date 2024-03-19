from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page:
    def __init__(self, browser):
        self.browser = browser

    def check_quantity_of_goods(self):
        quantity = Wait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name="quantity"]'))
        )
        quantity = quantity.get_attribute("value")
        assert quantity == "1"
