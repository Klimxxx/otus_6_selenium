from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC



def test_login(browser):
    browser.get(browser.base_url + "/administration/")
    browser.implicitly_wait(5)

    browser.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys("user")
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    user_name = browser.find_element(
        By.CSS_SELECTOR, '[class="d-none d-md-inline d-lg-inline"]'
    )
    assert user_name.text == "   John Doe", "авторизация не успешна"
    browser.find_element(By.CSS_SELECTOR, '[class="d-none d-md-inline"]').click()
    header_login_page = browser.find_element(By.CSS_SELECTOR, '[class="card-header"]')
    assert (
        header_login_page.text == "Please enter your login details."
    ), "разлог не выполнен"


def test_cart(browser):
    browser.get(browser.base_url)
    browser.execute_script("window.scrollBy(0, 1000);")
    btn_add_to_cart = Wait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[title="Add to Cart"]'))
    )
    browser.execute_script("arguments[0].scrollIntoView();", btn_add_to_cart[0])
    browser.execute_script("arguments[0].click();", btn_add_to_cart[0])
    browser.execute_script("window.scrollBy(0, -1000);")
    btn = Wait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[text()="Shopping Cart"]'))
    )
    browser.execute_script("arguments[0].click();", btn)

    quantity = Wait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="quantity"]'))
    )
    quantity = quantity.get_attribute("value")
    assert quantity == "1"


def test_prices_change_on_main_page(browser):
    browser.get(browser.base_url)
    browser.find_element(
        By.CSS_SELECTOR, '[id="form-currency"] [data-bs-toggle="dropdown"]'
    ).click()

    browser.find_element(By.XPATH, '// *[text()="€ Euro"]').click()

    goods_prices = Wait(browser, timeout=5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
    )
    assert "€" in goods_prices[0].text


def test_prices_change_on_catalogue_page(browser):
    browser.get(browser.base_url)
    browser.find_element(
        By.CSS_SELECTOR, '[id="form-currency"] [data-bs-toggle="dropdown"]'
    ).click()
    browser.find_element(By.XPATH, '// *[text()="€ Euro"]').click()
    browser.find_element(
        By.CSS_SELECTOR,
        'a[href="http://localhost/en-gb/catalog/desktops"][class="nav-link dropdown-toggle"]',
    ).click()
    browser.find_element(By.XPATH, '// *[text()="Show All Desktops"]').click()
    browser.execute_script("window.scrollBy(0, 500);")
    goods_prices = Wait(browser, timeout=5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
    )
    assert "€" in goods_prices[0].text
