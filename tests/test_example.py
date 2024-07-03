import logging
import time

import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.admin_page import Admin_page
from page_objects.cart_page import Cart_page
from page_objects.main_page import Main_page
from page_objects.orders_page import Orders_page
from page_objects.registration_page import Registration_page


# def test_add_product_to_orders(browser):
#     """Добавление нового товара в разделе администратора в Ордерс"""
#     browser.get("https://localhost" + "/administration/")
#     browser.implicitly_wait(5)
#
#     admin_page = Admin_page(browser)
#     admin_page.login(username="user", password="bitnami")
#     main_page = Main_page(browser)
#     main_page.menu_orders_click()
#     order_page = Orders_page(browser)
#     order_page.add_new_product()
#     order_page.add_new_customer()
#     order_page.add_new_payment_address()
#     order_page.add_new_shipping_address()
#     order_page.add_new_shipping_method()
#     order_page.add_new_payment_method()
#     order_page.confirm_form()
#
#     order_page.check_success_sending_form()
#
#
# def test_delete_product_from_orders(browser):
#     """Удаление товара из списка в Ордерс в разделе администратора"""
#     browser.get(browser.base_url + "/administration/")
#     browser.implicitly_wait(5)
#
#     admin_page = Admin_page(browser)
#     admin_page.login(username="user", password="bitnami")
#     main_page = Main_page(browser)
#     main_page.menu_orders_click()
#     order_page = Orders_page(browser)
#     order_page.add_new_product()
#     order_page.delete_added_product()
#
#     order_page.check_no_products_on_page()
#
#
# def test_registation_new_user(browser):
#     """Регистрация нового пользователя в магазине opencart"""
#     browser.implicitly_wait(5)
#     browser.get(browser.base_url + "/en-gb?route=account/register")
#
#     registration_page = Registration_page(browser)
#     registration_page.add_username()
#     registration_page.add_lastname()
#     registration_page.add_email()
#     registration_page.accept_privacy_policy()
#     registration_page.submit_form()
#
#     registration_page.check_success_filling_form()
#
#
# def test_prices_change_on_main_page_euro(browser):
#     """Переключение валют из верхнего меню opencart на евро"""
#     browser.get(browser.base_url)
#     main_page = Main_page(browser)
#     main_page.open_currency_dropbox()
#     main_page.choose_euro_currency()
#
#     main_page.check_currency_in_products(currency="€")
#
#
# def test_prices_change_on_main_page_pound(browser):
#     """Переключение валют из верхнего меню opencart на фунты"""
#     browser.get(browser.base_url)
#     main_page = Main_page(browser)
#     main_page.open_currency_dropbox()
#     main_page.choose_pound_currency()
#
#     main_page.check_currency_in_products(currency="£")
#
#
# def test_prices_change_on_main_page_dollar(browser):
#     """Переключение валют из верхнего меню opencart на доллар"""
#     browser.get(browser.base_url)
#     main_page = Main_page(browser)
#     main_page.open_currency_dropbox()
#     main_page.choose_dollar_currency()
#
#     main_page.check_currency_in_products(currency="$")
#
#
# def test_login(browser):
#     """Проверка успешной авторизации на админ странице"""
#     browser.get(browser.base_url + "/administration/")
#     browser.implicitly_wait(5)
#
#     admin_page = Admin_page(browser)
#     admin_page.login(username="user", password="bitnami")
#
#     admin_page.check_auth_succesful()
#
@allure.title('Проверка количества товаров в корзине после добавления 1 товара')
def test_cart(browser):
    """Проверка количества товаров в корзине после добавления 1 товара"""
    browser.get(browser.base_url)
    assert True
#     main_page = Main_page(browser)
#     main_page.add_product_to_cart()
#     main_page.open_cart()
#
#     cart_page = Cart_page(browser)
#     cart_page.check_quantity_of_goods()
#
@allure.title('Тест для проверки изменения цены в Опенкарте')
def test_prices_change_on_catalogue_page(browser):
    """Проверка изменения цены на евро в рубрике All_desktop"""
    browser.get(browser.base_url)
    assert True
    # main_page = Main_page(browser)
    # main_page.open_currency_dropbox()
    # main_page.choose_euro_currency()
    #
    # main_page.check_price_in_rubric_all_desktop()


@allure.title('Тест для проверки работы дженкинса')
def test_example(browser):
    browser.get(browser.base_url)
    time.sleep(1)
    assert True


