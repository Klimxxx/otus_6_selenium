import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

"""Сделал проверку в каждом тесте на 5 элементов - при желании можно разбить на отдельные функции, 
но не вижу в этом никакого смысла.
Также использовал для практики как явные так и неявные ожидания в тестах."""


def test_main_page(browser):
    browser.get(browser.base_url)
    browser.implicitly_wait(5)

    browser.find_elements(By.CSS_SELECTOR, '[class="nav-item dropdown"]')[0].click()
    browser.find_element(By.XPATH, '// *[text()="Mac (1)"]')
    browser.find_element(By.XPATH, '// *[text()="PC (0)"]')
    browser.find_element(
        By.CSS_SELECTOR, '[class="btn btn-lg btn-inverse btn-block dropdown-toggle"]'
    )
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Search"]').send_keys(
        "mac", Keys.ENTER
    )


def test_catalogue_page(browser):
    browser.get(browser.base_url)
    browser.find_elements(By.CSS_SELECTOR, '[class="nav-item dropdown"]')[0].click()
    browser.find_element(By.XPATH, '// *[text()="Mac (1)"]').click()
    browser.execute_script("window.scrollBy(0, 500);")

    Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.XPATH, '// *[text()="Privacy Policy"]'))
    )
    browser.find_element(By.CSS_SELECTOR, '[alt="HP Banner"]')
    show_1_page = browser.find_element(By.CSS_SELECTOR, '[class="col-sm-6 text-end"]')
    assert show_1_page.text == "Showing 1 to 1 of 1 (1 Pages)"
    ex_tax = browser.find_element(By.CSS_SELECTOR, '[class="price-tax"]')
    assert ex_tax.text == "Ex Tax: $100.00"
    price_new = browser.find_element(By.CSS_SELECTOR, '[class="price-new"]')
    assert price_new.text == "$122.00"


def test_item_page(browser):
    browser.get(browser.base_url)
    browser.find_element(By.CSS_SELECTOR, '[alt="iPhone"]').click()

    browser.find_element(
        By.CSS_SELECTOR, '[title="iPhone"][class="img-thumbnail mb-3"]'
    )
    Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.ID, "button-cart"))
    )

    browser.find_element(By.XPATH, '// *[text()="Availability: In Stock"]')
    browser.find_element(By.XPATH, '// *[text()="Ex Tax: $101.00"]')
    price_iphone = browser.find_element(
        By.CSS_SELECTOR, '[id="content"] [class="price-new"]'
    )
    assert price_iphone.text == "$123.20"


def test_admin_page(browser):
    browser.get(browser.base_url + "/administration")

    Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    text_header = browser.find_element(By.CLASS_NAME, "card-header")
    assert text_header.text == "Please enter your login details."
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    text_footer = browser.find_element(By.ID, "footer")
    assert text_footer.text == "OpenCart © 2009-2024 All Rights Reserved."


def test_register_page(browser):
    browser.get(browser.base_url + "/index.php?route=account/register")

    firstname = Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "firstname"))
    )
    firstname.send_keys("Klim")
    lastname = Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "lastname"))
    )
    lastname.send_keys("QA")
    email = Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email.send_keys("123@123.com")
    password = Wait(browser, timeout=2.5).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password.send_keys("12345")
    browser.find_element(By.ID, "input-newsletter").click()
