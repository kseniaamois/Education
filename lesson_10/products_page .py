from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage:
    """
    PageObject класс для страницы с товарами.

    Args:
        driver (WebDriver): экземпляр selenium WebDriver.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_to_cart(self, product_id: str) -> None:
        """
        Добавляет товар в корзину по уникальному идентификатору product_id,
        соответствующему части атрибута data-test.

        Args:
            product_id (str): часть значения атрибута data-test кнопки,
            например "sauce-labs-backpack"
        """
        button = self.driver.find_element(
            By.CSS_SELECTOR,
            f"button[data-test='add-to-cart-{product_id}']"
        )
        button.click()

    def go_to_cart(self) -> None:
        """
        Переход к корзине.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
