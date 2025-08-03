import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Добавляем импорт опций
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка оформления заказа на сайте saucedemo.com")
@allure.description(
    "Тест проводит полный сценарий: авторизация, добавление товаров "
    "в корзину, проверка корзины, оформление заказа и проверка итоговой суммы."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout() -> None:
    """
    Тест проверяет полный поток покупки: вход, добавление товаров,
    корзина, оплата.
    """

    # Создаём объект опций для Chrome
    chrome_options = Options()
    # Режим инкогнито для чистого профиля
    chrome_options.add_argument("--incognito")
    # Отключаем менеджер паролей и уведомления
    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)

    # Инициализируем драйвер с заданными опциями
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:
        with allure.step("Авторизация пользователя standard_user"):
            login.enter_username("standard_user")
            login.enter_password("secret_sauce")
            login.click_login()

        with allure.step("Добавление товаров в корзину"):
            # Добавляем товары по product_id из data-test
            products.add_to_cart("sauce-labs-backpack")
            products.add_to_cart("sauce-labs-bolt-t-shirt")
            products.add_to_cart("sauce-labs-onesie")

        products.go_to_cart()

        with allure.step("Проверка товаров в корзине"):
            cart_items = cart.get_cart_items()
            allure.attach(
                "\n".join(cart_items),
                name="Товары в корзине",
                attachment_type=allure.attachment_type.TEXT,
            )

            expected_substrings = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie",
            ]

            for expected in expected_substrings:
                assert any(expected in item for item in cart_items), (
                    f"Товар '{expected}' не найден в корзине: {cart_items}"
                )

        with allure.step("Нажатие кнопки Checkout"):
            cart.click_checkout()

        with allure.step("Заполнение данных для оформления заказа"):
            checkout.fill_first_name("Иван")
            checkout.fill_last_name("Петров")
            checkout.fill_postal_code("123456")
            checkout.click_continue()

        with allure.step("Получение и проверка итоговой суммы заказа"):
            total = checkout.get_total()
            assert total == "58.29", (
                f"Ожидали сумму 58.29, получили {total}"
            )

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
