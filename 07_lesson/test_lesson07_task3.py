from selenium import webdriver
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    # Добавление товаров
    products = ProductsPage(driver)
    products.add_to_cart("Sauce Labs Backpack")
    products.add_to_cart("Sauce Labs Bolt T-Shirt")
    products.add_to_cart("Sauce Labs Onesie")
    products.go_to_cart()

    # Корзина
    cart = CartPage(driver)
    cart_items = cart.get_cart_items()
    assert set(cart_items) == {
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    }

    cart.click_checkout()

    # Оформление заказа
    checkout = CheckoutPage(driver)
    checkout.fill_first_name("Иван")
    checkout.fill_last_name("Петров")
    checkout.fill_postal_code("123456")
    checkout.click_continue()

    total = checkout.get_total()
    assert total == "58.29", f"Ожидали сумму 58.29, получили {total}"

    driver.quit()
